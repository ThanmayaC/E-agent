"""Decision Intelligence — the Brain reasoning about the organization.

V2.4 turns the Enterprise Brain from an information system into a decision
system. The existing Decision Engine executes one recommendation well; this
layer sits beside it and decides *what is worth deciding about*:

    Observe (trends, anomalies, risks, repeated RCAs, missed items,
             delayed decisions, KPI deterioration, knowledge gaps)
      → Candidate decisions (full lifecycle records, remembered by the Brain)
      → Rank (impact, confidence, urgency, evidence, history, risk, strategy)
      → Approve / Reject (a human, or the Decision Engine's autonomy rules)
      → Execute through the existing Action Queue
      → Learn from the outcome (organizational memory, never retraining)

Nothing here is a second runtime: observation runs as scheduler jobs and bus
subscriptions, execution goes through the existing Decision Engine and Action
Queue, memory lives in the KnowledgeStore, and every decision becomes a node
in the Enterprise Knowledge Graph (the Decision Graph is the same graph). The
whole layer is disable-able (``EDIP_DECISION_INTELLIGENCE_ENABLED=false``)
back to V2.3 behaviour.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

from app.core.logging import get_logger
from app.runtime.events import Event, EventBus
from app.runtime.store import RuntimeStore, new_id, now_iso

logger = get_logger(__name__)

# Lifecycle statuses a decision record moves through (the SDS vocabulary).
DECISION_STATUSES = ("proposed", "modified", "approved", "rejected",
                     "executed", "expired", "cancelled")
# Statuses that count as "open" — an equivalent open decision blocks a
# duplicate proposal, and only open decisions are ranked.
OPEN_STATUSES = ("proposed", "modified", "approved")

MAX_DECISION_RECORDS = 500
MAX_SIGNALS = 300

# Ranking weights (sum to 1.0). Transparent by design: every ranked decision
# carries its factor breakdown, so "why is this first?" is answered by data.
RANKING_WEIGHTS = {
    "impact": 0.25, "urgency": 0.20, "confidence": 0.15, "evidence": 0.15,
    "history": 0.10, "risk": 0.10, "strategic": 0.05,
}

# How each signal kind maps to a candidate decision. severity → priority is
# resolved per signal; these carry the stable parts.
SIGNAL_PLAYBOOK = {
    "kpi_deterioration": {
        "action": "Investigate the deterioration in {subject}",
        "kind": "investigation", "teams": ["analytics"], "strategic": 0.8},
    "trend_decline": {
        "action": "Investigate the declining trend in {subject}",
        "kind": "investigation", "teams": ["analytics"], "strategic": 0.7},
    "risk_increase": {
        "action": "Escalate the increase in {subject} to Operations",
        "kind": "escalation", "teams": ["operations"], "strategic": 0.8},
    "anomaly": {
        "action": "Investigate the anomaly in {subject}",
        "kind": "investigation", "teams": ["operations"], "strategic": 0.6},
    "repeated_rca": {
        "action": "Recommend an SOP review — {subject} recurs across RCAs",
        "kind": "sop_review", "teams": ["operations", "quality"],
        "strategic": 0.7},
    "conflicting_sop": {
        "action": "Reconcile conflicting SOP guidance on {subject}",
        "kind": "sop_review", "teams": ["quality"], "strategic": 0.6},
    "meeting_decision": {
        "action": "Create follow-up tasks for the decision: {subject}",
        "kind": "follow_up", "teams": ["management"], "strategic": 0.5},
    "missed_action_item": {
        "action": "Chase the overdue action item: {subject}",
        "kind": "follow_up", "teams": ["management"], "strategic": 0.4},
    "delayed_decision": {
        "action": "Review the stalled decision: {subject}",
        "kind": "review", "teams": ["management"], "strategic": 0.5},
    "knowledge_gap": {
        "action": "Close the knowledge gap: {subject}",
        "kind": "knowledge", "teams": ["analytics"], "strategic": 0.4},
    "forecast_confidence": {
        "action": "Review the low-confidence forecast for {subject}",
        "kind": "review", "teams": ["analytics"], "strategic": 0.5},
    "growth_risk": {
        "action": "Recommend mitigation for the growth risk: {subject}",
        "kind": "mitigation", "teams": ["product"], "strategic": 0.9},
}

SEVERITY_PRIORITY = {"critical": 1, "high": 2, "medium": 3, "low": 5}


class DecisionIntelligence:
    """Continuous organizational reasoning over the surfaces that already
    exist. Collaborators are injected by the runtime; every one is optional
    and every detector degrades to a recorded skip."""

    def __init__(self, store: RuntimeStore, bus: EventBus, engine,
                 knowledge, graph=None, portfolio=None, tasks=None,
                 documents=None, product=None, enabled: bool = True,
                 ttl_days: int = 14):
        self._store = store
        self._bus = bus
        self._engine = engine          # DecisionEngine — execution pipeline
        self._knowledge = knowledge    # KnowledgeStore — decision memory
        self._graph = graph            # EnterpriseKnowledgeGraph — decision graph
        self._portfolio = portfolio
        self._tasks = tasks
        self._documents = documents
        self._product = product
        self.enabled = enabled
        self._ttl_days = ttl_days
        self._last_observed = ""
        if enabled:
            self._subscribe()

    # ------------------------------------------------------- subscriptions
    def _subscribe(self) -> None:
        """Significant observations arrive two ways: the periodic sweep, and
        these live events. Both funnel into ``propose``."""
        live = {
            "AnomalyDetected": ("anomaly", "detail"),
            "RiskIncreased": ("risk_increase", "top_risk"),
            "KPIThresholdCrossed": ("kpi_deterioration", "kpi"),
            "GrowthRiskDetected": ("growth_risk", "detail"),
            "PredictionConfidenceDropped": ("forecast_confidence", "metric"),
        }
        for kind, (signal_kind, field) in live.items():
            self._bus.subscribe(kind, self._event_handler(signal_kind, field),
                                name="decision_intelligence.observe")
        self._bus.subscribe("PortfolioChanged", self._on_portfolio_changed,
                            name="decision_intelligence.observe")
        # Monitor: when the queued execution of an approved decision lands,
        # the record moves to its terminal status and the Brain remembers.
        self._bus.subscribe("ActionExecuted", self._on_action_executed,
                            name="decision_intelligence.monitor")
        self._bus.subscribe("ActionFailed", self._on_action_failed,
                            name="decision_intelligence.monitor")

    def _event_handler(self, signal_kind: str, field: str):
        def handler(event: Event) -> None:
            subject = str(event.payload.get(field)
                          or event.payload.get("detail") or event.kind)[:160]
            self._signal(signal_kind, subject,
                         detail=str(event.payload)[:300],
                         severity=str(event.payload.get("severity", "medium")),
                         project_id=event.project_id,
                         evidence=[event.event_id])
        return handler

    def _on_portfolio_changed(self, event: Event) -> None:
        change = event.payload.get("health_change")
        if isinstance(change, (int, float)) and change <= -3:
            self._signal("trend_decline",
                         f"portfolio health (fell {abs(change)} points)",
                         detail=str(event.payload)[:300], severity="high",
                         evidence=[event.event_id])

    # ------------------------------------------------------------- signals
    def _signal(self, kind: str, subject: str, detail: str = "",
                severity: str = "medium", project_id: str = "",
                evidence: list[str] | None = None) -> dict | None:
        """Record one significant observation and turn it into a candidate
        decision. Returns the decision, or None when an equivalent one is
        already open (observation without duplication)."""
        signal = {"signal_id": new_id("sig"), "kind": kind,
                  "subject": subject[:200], "detail": detail[:400],
                  "severity": severity, "project_id": project_id,
                  "evidence": list(evidence or [])[:10], "created_at": now_iso()}
        decision = self.propose_from_signal(signal)
        if decision is None:
            # An equivalent decision is already open — the sweep saw the same
            # condition again, which is repetition, not a new observation.
            return None
        self._store.append("signals", signal, cap=MAX_SIGNALS)
        try:
            self._bus.publish("SignalDetected",
                              {"signal_id": signal["signal_id"], "kind": kind,
                               "subject": signal["subject"],
                               "severity": severity},
                              project_id=project_id,
                              source="decision_intelligence")
        except Exception:  # noqa: BLE001 — announcing degrades, never fails
            logger.exception("SignalDetected publication failed")
        return decision

    def propose_from_signal(self, signal: dict) -> dict | None:
        play = SIGNAL_PLAYBOOK.get(signal["kind"])
        if play is None:
            return None
        return self.propose(
            play["action"].format(subject=signal["subject"])[:300],
            kind=play["kind"],
            reasoning=f"Observed {signal['kind'].replace('_', ' ')}: "
                      f"{signal['detail'] or signal['subject']}"[:400],
            priority=SEVERITY_PRIORITY.get(signal["severity"], 3),
            evidence_ids=signal["evidence"],
            affected_teams=play["teams"],
            strategic_weight=play["strategic"],
            project_id=signal["project_id"],
            signal=signal, created_by="decision_intelligence")

    # ----------------------------------------------------------- lifecycle
    def propose(self, action: str, kind: str = "recommendation",
                reasoning: str = "", priority: int = 3,
                confidence: float | None = None,
                evidence_ids: list[str] | None = None,
                affected_products: list[str] | None = None,
                affected_teams: list[str] | None = None,
                expected_impact: str = "", owner: str = "",
                dependencies: list[str] | None = None,
                strategic_weight: float = 0.5, project_id: str = "",
                signal: dict | None = None,
                created_by: str = "manual") -> dict | None:
        """Create a candidate decision with the full lifecycle record. The
        same open decision is never proposed twice (signature dedupe)."""
        action = action.strip()
        if not action:
            raise ValueError("A decision needs an action")
        signature = f"{kind}:{action[:80].lower()}"
        for record in self._store.read("decision_records"):
            if record.get("signature") == signature and \
                    record.get("status") in OPEN_STATUSES:
                return None

        evidence = [str(e) for e in (evidence_ids or []) if e][:20]
        if confidence is None:
            # Same evidence-bounded rule the Decision Engine uses: cited
            # observations outrank uncited ones, learning adjusts later.
            confidence = 0.4 if not evidence else \
                round(min(0.5 + 0.1 * len(evidence), 0.95), 3)
        history_factor = self._historical_success(kind)
        record = {
            "decision_id": new_id("dcn"),
            "action": action[:300], "kind": kind,
            "priority": max(1, min(int(priority), 9)),
            "confidence": round(float(confidence), 3),
            "reasoning": reasoning[:500] or f"Proposed by {created_by}",
            "evidence_ids": evidence,
            "affected_products": list(affected_products or [])[:10],
            "affected_teams": list(affected_teams or [])[:10],
            "expected_impact": expected_impact[:300],
            "owner": owner, "status": "proposed",
            "dependencies": list(dependencies or [])[:10],
            "strategic_weight": max(0.0, min(float(strategic_weight), 1.0)),
            "historical_success": history_factor,
            "project_id": project_id, "signature": signature,
            "signal": {k: signal[k] for k in ("signal_id", "kind", "subject")}
            if signal else None,
            "engine_decision_id": "", "queued_action_id": "",
            "created_by": created_by, "created_at": now_iso(),
            "updated_at": now_iso(),
            "history": [{"status": "proposed", "at": now_iso(),
                         "by": created_by, "note": "Decision created"}],
        }
        self._store.append("decision_records", record,
                           cap=MAX_DECISION_RECORDS)
        self._remember(record, "created")
        self._graph_decision(record)
        try:
            self._bus.publish("DecisionProposed",
                              {"decision_id": record["decision_id"],
                               "action": record["action"][:200],
                               "kind": kind, "priority": record["priority"],
                               "confidence": record["confidence"]},
                              project_id=project_id,
                              source="decision_intelligence")
        except Exception:  # noqa: BLE001
            logger.exception("DecisionProposed publication failed")
        return record

    def set_status(self, decision_id: str, status: str, by: str = "",
                   note: str = "") -> dict | None:
        """Move a decision through its lifecycle. Approval hands execution to
        the existing Decision Engine → Action Queue pipeline; every
        transition is remembered by the Brain and recorded in the graph."""
        if status not in DECISION_STATUSES:
            raise ValueError(f"Unknown decision status: {status}. "
                             f"One of {', '.join(DECISION_STATUSES)}")
        updated: dict | None = None
        with self._store.mutate("decision_records") as records:
            for record in records:
                if record["decision_id"] == decision_id:
                    record["status"] = status
                    record["updated_at"] = now_iso()
                    record["history"].append(
                        {"status": status, "at": now_iso(), "by": by,
                         "note": note[:300]})
                    updated = record
                    break
        if updated is None:
            return None
        if status == "approved":
            self._execute(updated)
            # _execute mutates a fresh copy read from disk, so re-read to
            # return the record with its engine/queue linkage populated.
            updated = self.get(decision_id) or updated
        self._remember(updated, status)
        self._graph_decision(updated)
        try:
            self._bus.publish("DecisionStatusChanged",
                              {"decision_id": decision_id, "status": status,
                               "by": by, "action": updated["action"][:200]},
                              project_id=updated.get("project_id", ""),
                              source="decision_intelligence")
        except Exception:  # noqa: BLE001
            logger.exception("DecisionStatusChanged publication failed")
        return updated

    def modify(self, decision_id: str, by: str = "", **fields) -> dict | None:
        """Edit a decision before it is decided on. Editable fields only —
        the trace, identity, and lifecycle fields are the platform's."""
        editable = {k: v for k, v in fields.items() if v is not None and k in
                    ("action", "reasoning", "priority", "confidence", "owner",
                     "expected_impact", "affected_products", "affected_teams",
                     "dependencies")}
        if not editable:
            return self.get(decision_id)
        updated: dict | None = None
        with self._store.mutate("decision_records") as records:
            for record in records:
                if record["decision_id"] == decision_id:
                    if record["status"] not in ("proposed", "modified"):
                        raise ValueError(
                            f"A {record['status']} decision cannot be edited")
                    record.update(editable)
                    record["status"] = "modified"
                    record["updated_at"] = now_iso()
                    record["history"].append(
                        {"status": "modified", "at": now_iso(), "by": by,
                         "note": f"Edited: {', '.join(sorted(editable))}"})
                    updated = record
                    break
        if updated is not None:
            self._remember(updated, "modified")
        return updated

    def _execute(self, record: dict) -> None:
        """An approved decision executes through the pipeline that already
        exists: Decision Engine → Action Queue → executor. The record links
        to the engine decision so the two trails reference each other."""
        if self._engine is None:
            return
        try:
            outcome = self._engine.decide(
                {"action": record["action"],
                 "confidence": record["confidence"],
                 "priority": record["priority"],
                 "evidence_ids": record["evidence_ids"],
                 "expected_impact": record["expected_impact"]},
                project_id=record.get("project_id", ""),
                source=f"decision_intelligence:{record['decision_id']}")
            with self._store.mutate("decision_records") as records:
                for r in records:
                    if r["decision_id"] == record["decision_id"]:
                        r["engine_decision_id"] = outcome["decision_id"]
                        r["queued_action_id"] = outcome.get(
                            "queued_action_id", "")
                        break
        except Exception:  # noqa: BLE001 — approval stands even if queueing fails
            logger.exception("Executing approved decision %s failed",
                             record["decision_id"])

    # ------------------------------------------------------------- monitor
    def _on_action_executed(self, event: Event) -> None:
        self._close_by_action(event.payload.get("action_id", ""), "executed",
                              "The approved decision was executed")

    def _on_action_failed(self, event: Event) -> None:
        # The decision stays approved — failure is recorded, a human decides
        # whether to retry (the queue keeps its own retry trail).
        action_id = event.payload.get("action_id", "")
        if not action_id:
            return
        with self._store.mutate("decision_records") as records:
            for record in records:
                if record.get("queued_action_id") == action_id:
                    record["history"].append(
                        {"status": record["status"], "at": now_iso(),
                         "by": "queue",
                         "note": f"Execution failed: "
                                 f"{str(event.payload.get('error', ''))[:150]}"})
                    record["updated_at"] = now_iso()
                    break

    def _close_by_action(self, action_id: str, status: str,
                         note: str) -> None:
        if not action_id:
            return
        found = None
        with self._store.mutate("decision_records") as records:
            for record in records:
                if record.get("queued_action_id") == action_id and \
                        record["status"] == "approved":
                    record["status"] = status
                    record["updated_at"] = now_iso()
                    record["history"].append({"status": status,
                                              "at": now_iso(),
                                              "by": "queue", "note": note})
                    found = record
                    break
        if found is not None:
            self._remember(found, status)
            self._graph_decision(found)

    # ------------------------------------------------------ decision memory
    def _remember(self, record: dict, transition: str) -> None:
        """The Brain remembers organizational decisions: each transition is
        a learning event, and creation registers the decision itself."""
        if self._knowledge is None:
            return
        try:
            if transition == "created":
                self._knowledge.record_decision(
                    record["action"],
                    context=record["reasoning"][:200],
                    project_id=record.get("project_id", ""),
                    source="decision_intelligence")
            self._knowledge.record_learning_event(
                f"decision_{transition}", source="decision_intelligence",
                project_id=record.get("project_id", ""),
                details={"decision_id": record["decision_id"],
                         "action": record["action"][:200],
                         "kind": record["kind"],
                         "confidence": record["confidence"],
                         "priority": record["priority"]})
        except Exception:  # noqa: BLE001 — memory degrades, never fails
            logger.exception("Decision memory write failed")

    # ------------------------------------------------------- decision graph
    def _graph_decision(self, record: dict) -> None:
        """The Decision Graph is the Enterprise Knowledge Graph: a decision
        is a node, and its relations use the SDS vocabulary — depends_on a
        meeting, implements an RCA, updates an SOP, affects a product,
        creates a task."""
        if self._graph is None:
            return
        try:
            node_id = f"decision:{record['decision_id']}"
            with self._graph.batch() as graph:
                graph._upsert_node(  # noqa: SLF001 — batch exposes the graph itself
                    node_id, kind="decision", label=record["action"][:120],
                    project_id=record.get("project_id", ""),
                    status=record["status"], decision_kind=record["kind"],
                    confidence=record["confidence"],
                    priority=record["priority"],
                    created_by=record["created_by"])
                for product in record.get("affected_products", []):
                    graph._relate(node_id, f"concept:{str(product).lower()}",
                                  "affects",
                                  project_id=record.get("project_id", ""))
                for dep in record.get("dependencies", []):
                    graph._relate(node_id, str(dep), "depends_on")
                signal = record.get("signal") or {}
                if signal.get("kind") == "repeated_rca":
                    graph._relate(node_id,
                                  f"concept:{signal['subject'][:60].lower()}",
                                  "implements")
                if signal.get("kind") in ("conflicting_sop", "repeated_rca"):
                    graph._relate(node_id,
                                  f"concept:sop:{signal['subject'][:60].lower()}",
                                  "updates")
                if record["status"] == "executed" and \
                        record.get("queued_action_id"):
                    graph._relate(node_id,
                                  f"action:{record['queued_action_id']}",
                                  "creates")
        except Exception:  # noqa: BLE001 — the graph enriches, never gates
            logger.exception("Decision graph update failed")

    # ------------------------------------------------------------- learning
    def _historical_success(self, kind: str) -> float:
        """Learning without retraining: the approval record of past
        decisions of this kind, Laplace-smoothed so a new kind starts
        neutral. Approved and executed decisions raise it; rejections and
        cancellations lower it."""
        won = lost = 0
        for record in self._store.read("decision_records"):
            if record.get("kind") != kind:
                continue
            terminal = {h["status"] for h in record.get("history", [])}
            if {"approved", "executed"} & terminal:
                won += 1
            elif {"rejected", "cancelled"} & terminal:
                lost += 1
        return round((won + 1) / (won + lost + 2), 3)

    # -------------------------------------------------------------- ranking
    def rank(self, limit: int = 5, status: str = "") -> list[dict]:
        """The highest-value open decisions, scored on the SDS factors.
        Every ranked record carries its factor breakdown."""
        statuses = (status,) if status else OPEN_STATUSES
        ranked = []
        for record in self._store.read("decision_records"):
            if record["status"] not in statuses:
                continue
            factors = self._factors(record)
            score = round(sum(RANKING_WEIGHTS[name] * value
                              for name, value in factors.items()), 4)
            ranked.append({**record, "score": score, "factors": factors})
        ranked.sort(key=lambda r: (-r["score"], r["priority"],
                                   r["created_at"]))
        return ranked[:limit]

    def _factors(self, record: dict) -> dict[str, float]:
        severity_impact = {1: 1.0, 2: 0.85, 3: 0.6, 4: 0.45, 5: 0.35}
        priority = record.get("priority", 5)
        impact = severity_impact.get(priority, 0.25)
        if record.get("expected_impact"):
            impact = min(1.0, impact + 0.1)
        risk_kinds = {"escalation": 0.9, "mitigation": 0.9,
                      "investigation": 0.7, "sop_review": 0.5}
        return {
            "impact": impact,
            "urgency": round((10 - priority) / 9, 3),
            "confidence": record.get("confidence", 0.4),
            "evidence": min(1.0, len(record.get("evidence_ids", [])) / 5),
            "history": self._historical_success(record.get("kind", "")),
            "risk": risk_kinds.get(record.get("kind", ""), 0.3),
            "strategic": record.get("strategic_weight", 0.5),
        }

    # ------------------------------------------------- proactive detection
    def observe(self) -> dict:
        """The periodic sweep: every detector runs, each producing signals
        that become candidate decisions. Detectors are independent — one
        failing never stops the sweep — and the sweep also retires stale
        proposals."""
        if not self.enabled:
            return {"skipped": "decision intelligence disabled"}
        outcome: dict[str, Any] = {}
        for name, detector in (
                ("kpi_deterioration", self._detect_kpi_deterioration),
                ("repeated_rcas", self._detect_repeated_rcas),
                ("conflicting_sops", self._detect_conflicting_sops),
                ("meeting_follow_ups", self._detect_meeting_follow_ups),
                ("missed_action_items", self._detect_missed_action_items),
                ("delayed_decisions", self._detect_delayed_decisions),
                ("knowledge_gaps", self._detect_knowledge_gaps)):
            try:
                outcome[name] = detector()
            except Exception:  # noqa: BLE001 — one detector never stops the sweep
                logger.exception("Detector %s failed", name)
                outcome[name] = {"error": "detector failed"}
        outcome["expired"] = self._expire_stale()
        self._last_observed = now_iso()
        return outcome

    def _detect_kpi_deterioration(self) -> dict:
        """Product KPIs breaching thresholds and portfolio health erosion.
        Live events already catch crossings as they happen; the sweep
        catches what happened while the heartbeat was off."""
        found = 0
        if self._product is not None:
            for breach in self._product_kpi_breaches():
                if self._signal("kpi_deterioration", breach["subject"],
                                detail=breach["detail"],
                                severity=breach.get("severity", "high")):
                    found += 1
        return {"signals": found}

    def _product_kpi_breaches(self) -> list[dict]:
        breaches = []
        try:
            for item in (self._product.kpi_alerts()
                         if hasattr(self._product, "kpi_alerts") else []):
                breaches.append({
                    "subject": str(item.get("kpi", item.get("name", "KPI"))),
                    "detail": str(item)[:300],
                    "severity": str(item.get("severity", "high"))})
        except Exception:  # noqa: BLE001
            logger.exception("Reading product KPI alerts failed")
        return breaches[:5]

    def _detect_repeated_rcas(self) -> dict:
        """Two or more RCAs about the same subject mean the fix did not hold —
        the organization should review the SOP, not write a third RCA. RCA
        titles vary ("...in March" vs "...(repeat)"), so subjects are matched
        by shared significant terms, not exact titles."""
        if self._documents is None:
            return {"skipped": "document intelligence unavailable"}
        rcas = self._documents.documents(category="rca", limit=100)
        found = 0
        for cluster in _cluster_by_subject(rcas):
            docs = cluster["docs"]
            if len(docs) >= 2:
                if self._signal("repeated_rca", cluster["subject"],
                                detail=f"{len(docs)} RCAs share this subject: "
                                       + "; ".join(d.get("title", "")[:60]
                                                   for d in docs[:3]),
                                severity="high",
                                evidence=[d.get("document_id", "")
                                          for d in docs[:5]]):
                    found += 1
        return {"rcas": len(rcas), "signals": found}

    def _detect_conflicting_sops(self) -> dict:
        """Two SOPs on the same subject from different sources is guidance
        that disagrees with itself. Subjects are matched by shared terms."""
        if self._documents is None:
            return {"skipped": "document intelligence unavailable"}
        sops = self._documents.documents(category="sop", limit=100)
        found = 0
        for cluster in _cluster_by_subject(sops):
            docs = cluster["docs"]
            sources = {d.get("source_name", d.get("source", "")) for d in docs}
            if len(docs) >= 2 and len(sources) >= 2:
                if self._signal("conflicting_sop", cluster["subject"],
                                detail=f"{len(docs)} SOPs cover this subject "
                                       f"from {len(sources)} sources",
                                severity="medium",
                                evidence=[d.get("document_id", "")
                                          for d in docs[:5]]):
                    found += 1
        return {"sops": len(sops), "signals": found}

    def _detect_meeting_follow_ups(self) -> dict:
        """A decision recorded in a meeting with no task behind it is a
        decision the organization will forget."""
        if self._knowledge is None or self._tasks is None:
            return {"skipped": "knowledge or tasks unavailable"}
        open_titles = {str(t.get("title", "")).strip().lower()
                       for t in self._tasks.tasks(limit=500)}
        found = 0
        for decision in self._knowledge.decisions(20):
            text = str(decision.get("decision", "")).strip()
            if not text or text.lower() in open_titles:
                continue
            if self._signal("meeting_decision", text[:160],
                            detail=str(decision.get("context", ""))[:300],
                            severity="medium"):
                found += 1
        return {"signals": found}

    def _detect_missed_action_items(self) -> dict:
        if self._tasks is None:
            return {"skipped": "tasks unavailable"}
        today = datetime.now(timezone.utc).date().isoformat()
        found = 0
        for task in self._tasks.tasks(limit=500):
            due = str(task.get("due_date", "") or "")[:10]
            if task.get("status") in ("pending", "follow_up") and due and \
                    due < today:
                if self._signal("missed_action_item",
                                str(task.get("title", ""))[:160],
                                detail=f"due {due}, still "
                                       f"{task.get('status')}",
                                severity="medium",
                                project_id=task.get("project_id", "")):
                    found += 1
        return {"signals": found}

    def _detect_delayed_decisions(self) -> dict:
        """A proposal nobody approved or rejected is itself a finding."""
        cutoff = datetime.now(timezone.utc) - timedelta(days=3)
        found = 0
        for record in self._store.read("decision_records"):
            if record["status"] not in ("proposed", "modified"):
                continue
            if record.get("kind") == "review":
                continue  # a review of a review helps nobody
            created = _parse_iso(record.get("created_at", ""))
            if created is not None and created < cutoff:
                if self._signal("delayed_decision",
                                record["action"][:160],
                                detail=f"proposed {record['created_at'][:10]}, "
                                       f"still {record['status']}",
                                severity="medium"):
                    found += 1
        return {"signals": found}

    def _detect_knowledge_gaps(self) -> dict:
        """Projects the portfolio carries but the Brain has never seen a
        report for — the organization is flying blind there."""
        if self._portfolio is None:
            return {"skipped": "portfolio unavailable"}
        overview = self._portfolio.overview()
        found = 0
        for project in overview.get("projects", []):
            if project.get("status") == "ready" and \
                    project.get("health_score") is None:
                if self._signal("knowledge_gap",
                                f"no health signal for "
                                f"{project.get('name', project.get('project_id'))}",
                                severity="low",
                                project_id=project.get("project_id", "")):
                    found += 1
        return {"signals": found}

    def _expire_stale(self) -> int:
        cutoff = datetime.now(timezone.utc) - timedelta(days=self._ttl_days)
        expired = []
        with self._store.mutate("decision_records") as records:
            for record in records:
                if record["status"] not in ("proposed", "modified"):
                    continue
                created = _parse_iso(record.get("created_at", ""))
                if created is not None and created < cutoff:
                    record["status"] = "expired"
                    record["updated_at"] = now_iso()
                    record["history"].append(
                        {"status": "expired", "at": now_iso(),
                         "by": "decision_intelligence",
                         "note": f"No response within {self._ttl_days} days"})
                    expired.append(record)
        for record in expired:
            self._remember(record, "expired")
        return len(expired)

    # -------------------------------------------------------------- reports
    def report(self, period: str = "daily") -> dict:
        """Decision reports over organizational memory: what was decided,
        what it led to, and how well recommendations are landing."""
        days = {"daily": 1, "weekly": 7, "monthly": 30}.get(period)
        if days is None:
            raise ValueError("period must be daily, weekly, or monthly")
        cutoff = datetime.now(timezone.utc) - timedelta(days=days)
        records = [r for r in self._store.read("decision_records")
                   if (_parse_iso(r.get("updated_at", "")) or cutoff) >= cutoff]
        by_status: dict[str, int] = {}
        for r in records:
            by_status[r["status"]] = by_status.get(r["status"], 0) + 1
        decided = [r for r in records
                   if r["status"] in ("approved", "executed", "rejected")]
        executed = [r for r in records if r["status"] == "executed"]
        approved_conf = [r["confidence"] for r in records
                         if r["status"] in ("approved", "executed")]
        rejected_conf = [r["confidence"] for r in records
                         if r["status"] == "rejected"]
        return {
            "period": period, "generated_at": now_iso(),
            "window_days": days,
            "decisions": len(records), "by_status": by_status,
            "decided": len(decided), "executed": len(executed),
            "effectiveness": {
                "execution_rate": round(len(executed) / len(decided), 3)
                if decided else None,
                "approval_confidence_avg":
                    round(sum(approved_conf) / len(approved_conf), 3)
                    if approved_conf else None,
                "rejection_confidence_avg":
                    round(sum(rejected_conf) / len(rejected_conf), 3)
                    if rejected_conf else None,
                "success_by_kind": {
                    kind: self._historical_success(kind)
                    for kind in sorted({r["kind"] for r in records})},
            },
            "top_decisions": [
                {"decision_id": r["decision_id"], "action": r["action"],
                 "status": r["status"], "priority": r["priority"],
                 "confidence": r["confidence"], "score": r["score"]}
                for r in self.rank(5)],
            "recommendation_outcomes": (self._engine.stats()
                                        if self._engine else {}),
        }

    def generate_scheduled_report(self, period: str = "daily") -> dict:
        """The scheduler's report body: compose, remember, announce."""
        body = self.report(period)
        if self._knowledge is not None:
            try:
                self._knowledge.record_learning_event(
                    f"decision_report_{period}",
                    source="decision_intelligence",
                    details={"decisions": body["decisions"],
                             "executed": body["executed"],
                             "by_status": body["by_status"]})
            except Exception:  # noqa: BLE001
                logger.exception("Recording the decision report failed")
        try:
            self._bus.publish("DecisionReportGenerated",
                              {"period": period,
                               "decisions": body["decisions"],
                               "executed": body["executed"]},
                              source="decision_intelligence")
        except Exception:  # noqa: BLE001
            logger.exception("DecisionReportGenerated publication failed")
        return body

    # ------------------------------------------------------ executive brief
    def brief(self, queue=None) -> dict:
        """What requires attention, composed for the executive workspace:
        top decisions, recommended actions, risks, approvals, and what
        changed in the organization."""
        risks = []
        if self._portfolio is not None:
            try:
                risks = [{"insight": str(r.get("insight", ""))[:200],
                          "project_id": r.get("project_id", "")}
                         for r in self._portfolio.overview().get("risks", [])
                         [:5]]
            except Exception:  # noqa: BLE001
                logger.exception("Reading portfolio risks failed")
        change_kinds = {"KnowledgeUpdated", "SourcesProcessed",
                        "DocumentsUpdated", "SourceSynchronized",
                        "ProductUpdated", "DecisionStatusChanged",
                        "ReportGenerated"}
        changes = [e for e in self._bus.history(50)
                   if e.get("kind") in change_kinds][:8]
        top = self.rank(5)
        return {
            "generated_at": now_iso(),
            "top_decisions": top,
            "recommended_actions": [
                {"decision_id": r["decision_id"], "action": r["action"],
                 "kind": r["kind"], "priority": r["priority"],
                 "score": r["score"], "reasoning": r["reasoning"]}
                for r in top if r["status"] in ("proposed", "modified")],
            "critical_risks": risks,
            "pending_approvals": (queue.pending_approvals(5)
                                  if queue is not None else []),
            "recent_changes": [
                {"kind": e["kind"], "at": e["created_at"],
                 "source": e.get("source", ""),
                 "summary": _change_summary(e)} for e in changes],
            "stats": self.stats(),
        }

    # ---------------------------------------------------------------- read
    def get(self, decision_id: str) -> dict | None:
        return self._store.get("decision_records", "decision_id", decision_id)

    def decisions(self, status: str = "", kind: str = "",
                  limit: int = 50) -> list[dict]:
        items = self._store.read("decision_records")
        if status:
            items = [d for d in items if d["status"] == status]
        if kind:
            items = [d for d in items if d.get("kind") == kind]
        return list(reversed(items))[:limit]  # newest first

    def signals(self, kind: str = "", limit: int = 50) -> list[dict]:
        items = self._store.read("signals")
        if kind:
            items = [s for s in items if s["kind"] == kind]
        return list(reversed(items))[:limit]

    def stats(self) -> dict:
        records = self._store.read("decision_records")
        by_status: dict[str, int] = {}
        for r in records:
            by_status[r["status"]] = by_status.get(r["status"], 0) + 1
        return {"enabled": self.enabled, "decisions": len(records),
                "by_status": by_status,
                "open": sum(1 for r in records
                            if r["status"] in OPEN_STATUSES),
                "signals": len(self._store.read("signals")),
                "last_observed": self._last_observed,
                "ranking_weights": RANKING_WEIGHTS}

    def status(self) -> dict:
        return self.stats()


# ------------------------------------------------------------------ helpers
_STOPWORDS = frozenset(
    "a an and are as at be by for from in into is it of on or rca report "
    "review sop the to update v1 v2 with".split())


def _significant_words(title: str) -> set[str]:
    """The content words of a title: the subject, with boilerplate removed —
    good enough to notice the third RCA about settlement failures."""
    return {w for w in "".join(
        c if c.isalnum() else " " for c in title.lower()).split()
        if len(w) > 2 and w not in _STOPWORDS and not w.isdigit()}


def _cluster_by_subject(docs: list[dict],
                        min_shared: int = 2) -> list[dict]:
    """Greedily cluster documents whose titles share ``min_shared`` content
    words. Matching by shared terms (not identical titles) is what lets two
    RCAs about the same failure land in one cluster even when their titles
    differ. Each cluster's ``subject`` is the shared core, sorted."""
    clusters: list[dict] = []
    for doc in docs:
        words = _significant_words(doc.get("title", ""))
        if not words:
            continue
        for cluster in clusters:
            if len(words & cluster["tokens"]) >= min_shared:
                cluster["docs"].append(doc)
                cluster["tokens"] &= words  # keep the shared core
                break
        else:
            clusters.append({"docs": [doc], "tokens": set(words)})
    for cluster in clusters:
        cluster["subject"] = " ".join(sorted(cluster["tokens"])[:6])
    return clusters


def _parse_iso(value: str) -> datetime | None:
    try:
        parsed = datetime.fromisoformat(value)
    except (ValueError, TypeError):
        return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def _change_summary(event: dict) -> str:
    payload = event.get("payload") or {}
    for key in ("action", "detail", "kind", "status", "source"):
        if payload.get(key):
            return f"{event['kind']}: {str(payload[key])[:120]}"
    return event["kind"]

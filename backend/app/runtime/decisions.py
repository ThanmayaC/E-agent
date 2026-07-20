"""Decision Engine — the pipeline from a recommendation to a learned outcome.

    Recommendation → Evidence → Confidence → Priority → Approval required?
                   → Execute → Monitor → Learn

Every stage is recorded on the decision record, so "why did the agent do
that?" is answered by data rather than by reading code: which evidence was
cited, what confidence it carried, why it needed (or did not need) a human,
what the queue did with it, and what the platform learned from the outcome.

The engine decides; the Action Queue executes. Low-confidence and
high-impact decisions route to a human via the queue's approval layer —
autonomy is bounded by evidence, never by optimism.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.knowledge.store import KnowledgeStore
from app.runtime.events import Event, EventBus
from app.runtime.queue import ActionQueue
from app.runtime.store import RuntimeStore, new_id, now_iso

logger = get_logger(__name__)

# Confidence below this always asks a human, whatever the action kind is.
DEFAULT_AUTONOMY_THRESHOLD = 0.7
# Priority 1 is most urgent; anything at or above this is routine.
ROUTINE_PRIORITY = 4

STAGES = ("recommendation", "evidence", "confidence", "priority", "approval",
          "execute", "monitor", "learn")

MAX_DECISIONS = 300


class DecisionEngine:
    def __init__(self, store: RuntimeStore, bus: EventBus, queue: ActionQueue,
                 knowledge: KnowledgeStore,
                 autonomy_threshold: float = DEFAULT_AUTONOMY_THRESHOLD):
        self._store = store
        self._bus = bus
        self._queue = queue
        self._knowledge = knowledge
        self._threshold = autonomy_threshold
        # Monitor stage: the queue announces outcomes, the engine learns.
        bus.subscribe("ActionExecuted", self._on_action_executed,
                      name="decision_engine.monitor")
        bus.subscribe("ActionFailed", self._on_action_failed,
                      name="decision_engine.monitor")
        bus.subscribe("ActionRejected", self._on_action_rejected,
                      name="decision_engine.monitor")

    # ------------------------------------------------------------ pipeline
    def decide(self, recommendation: dict, project_id: str = "",
               action_kind: str = "create_task",
               source: str = "recommendation_engine") -> dict:
        """Run one recommendation through the pipeline. Returns the decision
        record; ``queued_action_id`` is set when an action was created."""
        action_text = str(recommendation.get("action")
                          or recommendation.get("recommendation", "")).strip()
        if not action_text:
            raise ValueError("Recommendation has no action text")

        trace: list[dict] = []

        def stage(name: str, **detail: Any) -> None:
            trace.append({"stage": name, "at": now_iso(), **detail})

        stage("recommendation", action=action_text[:200], source=source)

        evidence_ids = self._evidence_for(recommendation)
        stage("evidence", evidence_ids=evidence_ids, count=len(evidence_ids))

        confidence = self._confidence_for(recommendation, evidence_ids)
        stage("confidence", confidence=confidence, threshold=self._threshold)

        priority = self._priority_for(recommendation, confidence)
        stage("priority", priority=priority)

        needs_approval = (self._queue.requires_approval(action_kind)
                          or confidence < self._threshold
                          or priority < ROUTINE_PRIORITY)
        reason = self._approval_reason(action_kind, confidence, priority)
        stage("approval", required=needs_approval, reason=reason)

        decision = {
            "decision_id": new_id("dec"), "action": action_text[:300],
            "action_kind": action_kind, "project_id": project_id,
            "source": source, "evidence_ids": evidence_ids,
            "confidence": confidence, "priority": priority,
            "requires_approval": needs_approval, "approval_reason": reason,
            "status": "queued", "queued_action_id": "", "outcome": "",
            "trace": trace, "created_at": now_iso(), "updated_at": now_iso(),
            "expected_impact": str(recommendation.get("expected_impact",
                                                      ""))[:300],
        }

        queued = self._queue.submit(
            action_kind, action_text[:300],
            payload={"recommendation": recommendation,
                     "decision_id": decision["decision_id"]},
            detail=decision["expected_impact"], priority=priority,
            project_id=project_id, source="decision_engine",
            source_ref=f"{project_id}:{action_text[:60].lower()}",
            confidence=confidence, evidence_ids=evidence_ids)

        if queued is None:  # an equivalent action is already in flight
            decision["status"] = "duplicate"
            stage("execute", queued=False, reason="equivalent action in flight")
        else:
            decision["queued_action_id"] = queued["action_id"]
            stage("execute", queued=True, action_id=queued["action_id"],
                  queue_status=queued["status"])

        self._save(decision)
        self._bus.publish("RecommendationCreated",
                          {"decision_id": decision["decision_id"],
                           "action": action_text[:200],
                           "confidence": confidence, "priority": priority},
                          project_id=project_id, source="decision_engine")
        return decision

    def decide_many(self, recommendations: list[dict], project_id: str = "",
                    action_kind: str = "create_task",
                    source: str = "recommendation_engine") -> dict[str, int]:
        decided, skipped = 0, 0
        for rec in recommendations:
            if not isinstance(rec, dict):
                continue
            try:
                outcome = self.decide(rec, project_id=project_id,
                                      action_kind=action_kind, source=source)
                if outcome["status"] == "duplicate":
                    skipped += 1
                else:
                    decided += 1
            except ValueError:
                skipped += 1
            except Exception:  # noqa: BLE001 — one bad rec never stops the batch
                logger.exception("Decision pipeline failed for a recommendation")
                skipped += 1
        return {"decided": decided, "skipped": skipped}

    # -------------------------------------------------------------- stages
    def _evidence_for(self, recommendation: dict) -> list[str]:
        ids = recommendation.get("evidence_ids") or recommendation.get(
            "citations") or []
        return [str(i) for i in ids if i][:20] if isinstance(ids, list) else []

    def _confidence_for(self, recommendation: dict,
                        evidence_ids: list[str]) -> float:
        """Stated confidence when the producer gave one; otherwise derived
        from evidence: a cited recommendation outranks an uncited one."""
        stated = recommendation.get("confidence")
        if isinstance(stated, (int, float)) and 0 <= float(stated) <= 1:
            return round(float(stated), 3)
        if not evidence_ids:
            return 0.4  # deterministic rules with no citation — a human looks
        return round(min(0.5 + 0.1 * len(evidence_ids), 0.95), 3)

    def _priority_for(self, recommendation: dict, confidence: float) -> int:
        stated = recommendation.get("priority")
        if isinstance(stated, int) and 1 <= stated <= 9:
            return stated
        severity = str(recommendation.get("severity", "")).lower()
        if severity in ("critical", "high"):
            return 1 if severity == "critical" else 2
        return 3 if confidence >= 0.8 else 5

    def _approval_reason(self, action_kind: str, confidence: float,
                         priority: int) -> str:
        if self._queue.requires_approval(action_kind):
            return f"action kind '{action_kind}' always requires approval"
        if confidence < self._threshold:
            return (f"confidence {confidence:.2f} is below the autonomy "
                    f"threshold {self._threshold:.2f}")
        if priority < ROUTINE_PRIORITY:
            return f"priority {priority} is above the routine threshold"
        return "autonomous: confident, routine, and internally reversible"

    # ------------------------------------------------- monitor → learn
    def _on_action_executed(self, event: Event) -> None:
        self._close(event.payload.get("action_id", ""), "executed",
                    "The decision was executed successfully")

    def _on_action_failed(self, event: Event) -> None:
        self._close(event.payload.get("action_id", ""), "failed",
                    f"Execution failed: {event.payload.get('error', '')[:150]}")

    def _on_action_rejected(self, event: Event) -> None:
        self._close(event.payload.get("action_id", ""), "rejected",
                    f"A human rejected it: "
                    f"{event.payload.get('reason', '')[:150]}")

    def _close(self, action_id: str, outcome: str, note: str) -> None:
        """Monitor + Learn: record the outcome on the decision and write a
        learning event, so the platform's next decision knows how the last
        one landed."""
        if not action_id:
            return
        with self._store.mutate("decisions") as decisions:
            record = next((d for d in decisions
                           if d.get("queued_action_id") == action_id), None)
            if record is None:
                return
            record["trace"].append({"stage": "monitor", "at": now_iso(),
                                    "outcome": outcome, "note": note})
            record["trace"].append({"stage": "learn", "at": now_iso(),
                                    "recorded": True})
            record["status"] = outcome
            record["outcome"] = note
            record["updated_at"] = now_iso()
        try:
            self._knowledge.record_learning_event(
                f"decision_{outcome}", source="decision_engine",
                project_id=record.get("project_id", ""),
                details={"decision_id": record["decision_id"],
                         "action": record["action"],
                         "confidence": record["confidence"],
                         "outcome": note})
        except Exception:  # noqa: BLE001 — learning degrades, never fails
            logger.exception("Decision learning event failed")

    # ---------------------------------------------------------------- read
    def _save(self, decision: dict) -> None:
        self._store.append("decisions", decision, cap=MAX_DECISIONS)

    def decisions(self, status: str = "", project_id: str = "",
                  limit: int = 50) -> list[dict]:
        items = self._store.read("decisions")
        if status:
            items = [d for d in items if d["status"] == status]
        if project_id:
            items = [d for d in items if d.get("project_id") == project_id]
        return list(reversed(items))[:limit]  # newest first

    def stats(self) -> dict:
        items = self.decisions(limit=MAX_DECISIONS)
        by_status: dict[str, int] = {}
        for d in items:
            by_status[d["status"]] = by_status.get(d["status"], 0) + 1
        autonomous = sum(1 for d in items if not d["requires_approval"])
        return {"total": len(items), "by_status": by_status,
                "autonomous": autonomous,
                "escalated_to_human": len(items) - autonomous,
                "autonomy_threshold": self._threshold}

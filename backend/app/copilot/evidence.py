"""Evidence Collector — the facts, gathered before the model is asked.

The order matters and is the whole point: **evidence is collected first, then
the LLM is asked to reason over it**. The model never fetches, never queries,
and never decides what is true. It receives a closed set of facts, each with an
id, and may only make claims it can attach those ids to.

    analytics · KPIs · forecasts · recommendations · reports · knowledge
    relationships · business rules · product reviews · portfolio health

Every item carries an `id`, because the ids are the contract: the prompt tells
the model to cite them, and the validator later checks that what it cited
actually exists. Evidence with no id would be evidence the validator cannot
enforce, which is to say: not evidence.

Nothing here computes. Each fact is read from the module that produced it —
the KPI module's KPIs, the Analytics module's signals, the Forecasting
module's forecasts (validation gate and all), the Product layer's health.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from app.core.logging import get_logger

logger = get_logger(__name__)

MAX_PER_KIND = 10
# Figures embedded in a retrieved passage are sourced — the passage IS the
# evidence the model was shown, so a number inside it is not an invention.
_NUMBER_IN_TEXT = re.compile(r"-?\d[\d,]*\.?\d*")
# Below this many evidence items, an answer's confidence is capped — a
# conclusion drawn from almost nothing is a guess wearing a number.
WEAK_EVIDENCE = 3


@dataclass
class Evidence:
    """The closed set of facts one answer may stand on."""
    items: list[dict] = field(default_factory=list)
    by_kind: dict[str, list[dict]] = field(default_factory=dict)
    missing: list[str] = field(default_factory=list)

    def add(self, kind: str, item_id: str, summary: str,
            payload: dict | None = None) -> None:
        if not item_id:
            return  # evidence the validator could not enforce is not evidence
        item = {"id": item_id, "kind": kind, "summary": summary[:300],
                **(payload or {})}
        self.items.append(item)
        self.by_kind.setdefault(kind, []).append(item)

    @property
    def ids(self) -> set[str]:
        return {i["id"] for i in self.items}

    @property
    def is_weak(self) -> bool:
        return len(self.items) < WEAK_EVIDENCE

    def numbers(self) -> set[float]:
        """Every number the evidence contains — what the validator checks a
        model's figures against. This includes figures written inside a
        retrieved passage's ``text``: a document chunk carries its numbers in
        prose (a 94.2% success rate, a March 2026 date), and a number the model
        quotes from the passage it was given is sourced, not invented."""
        found: set[float] = set()
        for item in self.items:
            for key, value in item.items():
                if isinstance(value, bool):
                    continue
                if isinstance(value, (int, float)):
                    found.add(round(float(value), 4))
                elif isinstance(value, str) and key == "text":
                    for raw in _NUMBER_IN_TEXT.findall(value):
                        try:
                            found.add(round(float(raw.replace(",", "")), 4))
                        except ValueError:
                            continue
        return found

    def kpi_names(self) -> set[str]:
        return {str(i.get("name", "")).strip().lower()
                for i in self.by_kind.get("kpi", []) if i.get("name")}

    def describe(self) -> dict:
        return {"total": len(self.items),
                "by_kind": {k: len(v) for k, v in self.by_kind.items()},
                "weak": self.is_weak, "missing": self.missing}


class EvidenceCollector:
    """Collects a request's evidence from the modules that own the facts."""

    def __init__(self, knowledge, artifacts, product=None, sync=None,
                 portfolio=None, manager=None, search=None):
        self._knowledge = knowledge
        self._artifacts = artifacts
        self._product = product
        self._sync = sync
        self._portfolio = portfolio
        self._manager = manager
        # The enterprise search engine. Stored under its own name so it does
        # not shadow the ``_search`` collector method below — a shadow that
        # silently kept enterprise-search evidence from ever reaching answers.
        self._enterprise_search = search

    # ------------------------------------------------------------ collect
    def collect(self, plan, message: str = "") -> Evidence:
        """Gather exactly the evidence the plan asked for."""
        evidence = Evidence()
        collectors = {
            "kpis": lambda: self._kpis(evidence, plan.subject),
            "signals": lambda: self._signals(evidence, plan.subject),
            "forecasts": lambda: self._forecasts(evidence, plan.subject),
            "quality": lambda: self._quality(evidence),
            "recommendations": lambda: self._recommendations(evidence),
            "reports": lambda: self._reports(evidence),
            "knowledge": lambda: self._knowledge_items(evidence),
            "relationships": lambda: self._relationships(evidence,
                                                         plan.subject),
            "business_rules": lambda: self._rules(evidence),
            "product_health": lambda: self._product_health(evidence,
                                                           plan.subject),
            "product_reviews": lambda: self._reviews(evidence, plan.subject),
            "portfolio_health": lambda: self._portfolio_health(evidence),
            "portfolio_ranking": lambda: self._ranking(evidence),
            "growth": lambda: self._growth(evidence, plan.subject),
            "top_risks": lambda: self._top(evidence, "risks"),
            "top_opportunities": lambda: self._top(evidence, "opportunities"),
            "pending_approvals": lambda: self._approvals(evidence),
            "tasks": lambda: self._tasks(evidence),
            "decisions": lambda: self._decisions(evidence),
            "search_results": lambda: self._search(evidence, message),
            "document_chunks": lambda: self._document_chunks(evidence, message),
        }
        for kind in plan.evidence:
            collector = collectors.get(kind)
            if collector is None:
                continue
            try:
                collector()
            except _Unavailable as absent:
                evidence.missing.append(f"{kind}: {absent}")
            except Exception as exc:  # noqa: BLE001 — one source never fails the answer
                logger.exception("Copilot evidence source %s failed", kind)
                evidence.missing.append(f"{kind}: {str(exc)[:120]}")
        return evidence

    # ---------------------------------------------------------- analytics
    def _projects(self, subject: str) -> list[str]:
        """The projects a request is scoped to: the subject product's, else
        every project the platform has analysed."""
        if subject and self._product is not None:
            product = self._product.catalog.resolve(subject)
            if product and product.get("projects"):
                return product["projects"]
        return list(self._artifacts.list_projects())

    def _kpis(self, evidence: Evidence, subject: str) -> None:
        for pid in self._projects(subject):
            for kpi in (self._artifacts.load(pid, "kpis", []) or [])[:MAX_PER_KIND]:
                if not isinstance(kpi, dict):
                    continue
                evidence.add(
                    "kpi", str(kpi.get("id") or kpi.get("name", "")),
                    f"{kpi.get('name')}: {kpi.get('current_value')}"
                    f"{kpi.get('unit', '')} ({kpi.get('growth_pct')}% "
                    f"period-over-period, trend {kpi.get('trend')})",
                    {"name": kpi.get("name"),
                     "current_value": kpi.get("current_value"),
                     "growth_pct": kpi.get("growth_pct"),
                     "unit": kpi.get("unit", ""),
                     "trend": kpi.get("trend"), "project_id": pid})

    def _signals(self, evidence: Evidence, subject: str) -> None:
        for pid in self._projects(subject):
            for signal in (self._artifacts.load(pid, "signals", [])
                           or [])[:MAX_PER_KIND]:
                if not isinstance(signal, dict):
                    continue
                evidence.add(
                    "signal", str(signal.get("id", "")),
                    f"{signal.get('kind')} signal on "
                    f"{signal.get('kpi_name')} (strength "
                    f"{signal.get('strength')})",
                    {"signal_kind": signal.get("kind"),
                     "kpi_name": signal.get("kpi_name"),
                     "strength": signal.get("strength"),
                     "stats": signal.get("stats", {}), "project_id": pid})

    def _forecasts(self, evidence: Evidence, subject: str) -> None:
        for pid in self._projects(subject):
            payload = self._artifacts.load(pid, "forecasts", []) or []
            if isinstance(payload, dict):
                payload = payload.get("forecasts") or payload.get("series") or []
            for forecast in payload[:MAX_PER_KIND]:
                if not isinstance(forecast, dict):
                    continue
                # The forecasting module's validation gate travels with the
                # fact: a low-confidence forecast must never be quoted as if
                # it were a validated one.
                evidence.add(
                    "forecast", f"forecast:{forecast.get('kpi_id')}",
                    f"{forecast.get('kpi_name')} forecast "
                    f"({forecast.get('horizon')}): "
                    f"{forecast.get('values')} via {forecast.get('method')}, "
                    f"status {forecast.get('status')}, confidence "
                    f"{forecast.get('confidence')}",
                    {"kpi_name": forecast.get("kpi_name"),
                     "values": forecast.get("values"),
                     "status": forecast.get("status"),
                     "confidence": forecast.get("confidence"),
                     "validation": forecast.get("validation", []),
                     "project_id": pid})

    def _quality(self, evidence: Evidence) -> None:
        for pid in self._artifacts.list_projects():
            quality = self._artifacts.load(pid, "quality", {}) or {}
            if isinstance(quality, dict) and quality.get("overall_score") is not None:
                evidence.add("quality", f"quality:{pid}",
                             f"Data quality for {pid}: "
                             f"{quality['overall_score']}/100",
                             {"overall_score": quality["overall_score"],
                              "project_id": pid})

    # ------------------------------------------------------------ product
    def _product_health(self, evidence: Evidence, subject: str) -> None:
        if self._product is None:
            raise _Unavailable("the product intelligence layer is disabled")
        records = self._product.health.all_health()
        if subject:
            records = [r for r in records
                       if subject.lower() in r["product"].lower()] or records
        for record in records[:MAX_PER_KIND]:
            evidence.add(
                "product_health", f"health:{record['product_id']}",
                f"{record['product']} health "
                f"{record['health_score']}/100 ({record['band']}), "
                f"confidence {record['confidence']}",
                {"product": record["product"],
                 "health_score": record["health_score"],
                 "band": record["band"], "scores": record["scores"],
                 "reasons": record["reasons"],
                 "confidence": record["confidence"]})

    def _reviews(self, evidence: Evidence, subject: str) -> None:
        if self._product is None:
            raise _Unavailable("the product intelligence layer is disabled")
        product = self._product.catalog.resolve(subject) if subject else None
        reviews = self._product.reviews.reviews(
            product_id=product["product_id"] if product else "", limit=3)
        for review in reviews:
            evidence.add(
                "product_review", f"review:{review['review_id']}",
                f"{review['product']} review: {review['executive_summary']}",
                {"product": review["product"],
                 "health_score": review.get("health_score"),
                 "risks": [r["risk"] for r in review["risks"]][:3],
                 "strengths": [s["strength"] for s in review["strengths"]][:3]})

    def _growth(self, evidence: Evidence, subject: str) -> None:
        if self._product is None:
            raise _Unavailable("the product intelligence layer is disabled")
        findings = self._product.growth.analyse()["findings"]
        if subject:
            findings = [f for f in findings
                        if subject.lower() in str(f.get("product", "")).lower()
                        ] or findings
        for i, finding in enumerate(findings[:MAX_PER_KIND]):
            evidence.add(
                "growth_finding", f"growth:{finding['kind']}:{i}",
                finding["finding"],
                {"finding_kind": finding["kind"],
                 "product": finding["product"],
                 "confidence": finding["confidence"],
                 "supporting_evidence": finding["evidence_ids"]})

    def _recommendations(self, evidence: Evidence) -> None:
        if self._product is None:
            raise _Unavailable("the product intelligence layer is disabled")
        for rec in self._product.strategy.recommendations(status="open",
                                                          limit=MAX_PER_KIND):
            evidence.add(
                "recommendation", f"rec:{rec['recommendation_id']}",
                f"{rec['recommendation']} (priority {rec['priority']}, "
                f"{rec['estimated_effort']} effort)",
                {"product": rec["product"], "priority": rec["priority"],
                 "impact": rec["business_impact"],
                 "confidence": rec["confidence"],
                 "effort": rec["estimated_effort"]})

    def _portfolio_health(self, evidence: Evidence) -> None:
        if self._product is not None:
            evaluation = self._product.portfolio.evaluate()
            health = evaluation["portfolio_health"]
            evidence.add(
                "portfolio_health", "portfolio:product",
                f"Product portfolio health {health['score']}/100 "
                f"({health['band']}); growth "
                f"{evaluation['portfolio_growth']['band']}, risk "
                f"{evaluation['portfolio_risk']['band']}",
                {"score": health["score"], "band": health["band"],
                 "measured": evaluation["coverage"]["measured"],
                 "products": evaluation["coverage"]["products"]})
        if self._portfolio is not None:
            overview = self._portfolio.overview()
            health = overview["portfolio_health"]
            evidence.add(
                "portfolio_health", "portfolio:projects",
                f"Project portfolio: "
                f"{health.get('average_health_score')}/100 average across "
                f"{health.get('projects_total')} project(s)",
                {"average_health_score": health.get("average_health_score"),
                 "projects_total": health.get("projects_total")})
        if self._product is None and self._portfolio is None:
            raise _Unavailable("no portfolio is wired")

    def _ranking(self, evidence: Evidence) -> None:
        if self._product is None:
            raise _Unavailable("the product intelligence layer is disabled")
        for entry in self._product.portfolio.evaluate()[
                "product_ranking"][:MAX_PER_KIND]:
            evidence.add(
                "portfolio_ranking", f"rank:{entry['product_id']}",
                f"#{entry['rank']} {entry['product']}: health "
                f"{entry['health_score']}, priority "
                f"{entry['investment_priority']} — {entry['priority_reason']}",
                {"product": entry["product"], "rank": entry["rank"],
                 "health_score": entry["health_score"],
                 "investment_priority": entry["investment_priority"]})

    def _top(self, evidence: Evidence, which: str) -> None:
        if self._product is None:
            raise _Unavailable("the product intelligence layer is disabled")
        evaluation = self._product.portfolio.evaluate()
        key = "top_risks" if which == "risks" else "top_opportunities"
        for i, item in enumerate(evaluation[key]):
            evidence.add(
                f"top_{which}", f"{key}:{i}", item["finding"],
                {"product": item["product"], "kind": item["kind"],
                 "confidence": item["confidence"]})

    # -------------------------------------------------- knowledge / manager
    def _knowledge_items(self, evidence: Evidence) -> None:
        snapshot = self._knowledge.snapshot()
        for term, entry in list(snapshot.get("terminology", {}).items())[:MAX_PER_KIND]:
            evidence.add("knowledge", f"term:{term}",
                         f"{entry.get('term', term)}: "
                         f"{entry.get('definition', '')}",
                         {"term": entry.get("term", term)})
        for i, insight in enumerate(self._knowledge.insights(MAX_PER_KIND)):
            evidence.add("knowledge", f"insight:{i}",
                         str(insight.get("insight", "")),
                         {"statement_type": insight.get("statement_type")})

    def _relationships(self, evidence: Evidence, subject: str) -> None:
        if self._sync is None:
            raise _Unavailable("the synchronization layer is disabled")
        entity = (self._sync.organization.resolve(subject) if subject else None)
        links = self._sync.relationships.relationships(
            entity_id=entity["entity_id"] if entity else "",
            limit=MAX_PER_KIND)
        for link in links:
            evidence.add(
                "relationship",
                f"rel:{link['relationship_id'][:60]}",
                f"{link['source']} —{link['kind']}→ {link['target']} "
                f"({link['confidence']:.0%}): {link['evidence']}",
                {"relationship_kind": link["kind"],
                 "confidence": link["confidence"]})

    def _rules(self, evidence: Evidence) -> None:
        rules = self._knowledge.snapshot().get("business_rules", [])
        for i, rule in enumerate(rules[:MAX_PER_KIND]):
            evidence.add("business_rule", f"rule:{i}",
                         str(rule.get("rule", "")),
                         {"scope": rule.get("scope", "global")})

    def _approvals(self, evidence: Evidence) -> None:
        if self._manager is None:
            raise _Unavailable("no manager workspace is wired")
        for i, approval in enumerate(self._manager.pending_approvals()[:MAX_PER_KIND]):
            evidence.add("pending_approval", f"approval:{i}",
                         f"{approval['title']} ({approval['kind']})",
                         {"approval_kind": approval["kind"],
                          "ref": approval.get("ref", "")})

    def _tasks(self, evidence: Evidence) -> None:
        if self._manager is None:
            raise _Unavailable("no manager workspace is wired")
        for task in self._manager.tasks.open_tasks(MAX_PER_KIND):
            evidence.add("task", f"task:{task['task_id']}",
                         f"{task['title']} (status {task['status']}, "
                         f"priority {task.get('priority')})",
                         {"status": task["status"],
                          "priority": task.get("priority")})

    def _decisions(self, evidence: Evidence) -> None:
        for i, decision in enumerate(self._knowledge.decisions(MAX_PER_KIND)):
            evidence.add("decision", f"decision:{i}",
                         str(decision.get("decision", "")),
                         {"context": decision.get("context", "")})

    def _reports(self, evidence: Evidence) -> None:
        for report in self._knowledge.report_history(MAX_PER_KIND):
            evidence.add(
                "report",
                f"report:{report.get('project_id')}:{report.get('title', '')[:30]}",
                f"{report.get('title')} — health "
                f"{report.get('health_score')}",
                {"title": report.get("title"),
                 "health_score": report.get("health_score"),
                 "project_id": report.get("project_id")})

    def _search(self, evidence: Evidence, message: str) -> None:
        if self._search_engine is None:
            raise _Unavailable("enterprise search is unavailable")
        outcome = self._search_engine.search(message, limit=MAX_PER_KIND)
        for i, hit in enumerate(outcome["results"]):
            evidence.add("search_result", f"search:{i}",
                         f"[{hit['surface']}] {hit['title']}: {hit['detail']}",
                         {"surface": hit["surface"], "matched": hit["matched"]})

    def _document_chunks(self, evidence: Evidence, message: str) -> None:
        """Passages from the enterprise's own documents — SOPs, RCAs, meeting
        notes, policies, reports, and the email/Teams corpus. This is what
        lets the copilot answer *across* sources: the model receives the actual
        passage and cites the document it came from, rather than retrieving a
        single file. Each chunk is citable by its document id."""
        documents = getattr(self._sync, "documents", None)
        if documents is None:
            raise _Unavailable("document intelligence is disabled")
        for i, match in enumerate(documents.search(message, limit=MAX_PER_KIND)):
            payload = match.get("payload") or match
            text = str(payload.get("text") or "").strip()
            if not text:
                continue
            document = str(payload.get("document") or "document")
            category = str(payload.get("category") or "document")
            evidence.add(
                "document_chunk",
                str(payload.get("document_id") or f"doc:{i}"),
                f"[{category}] {document}: {text[:220]}",
                {"document": document, "category": category,
                 "source": payload.get("source"),
                 "text": text[:1200]})

    @property
    def _search_engine(self):
        return self._enterprise_search


class _Unavailable(RuntimeError):
    """A source is not wired — an expected condition, not a failure."""

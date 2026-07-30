"""Enterprise AI Orchestrator — the platform's central intelligence layer.

    question → classify → plan → route → engines (parallel) → merge → context

This is the execution graph (Phase 13) that turns the chat from a single RAG
call into a router over every reasoning engine the platform owns. It does not
answer questions itself and it holds no truth: it decides *which* engines a
question needs, runs them, and merges their evidence into the set the existing
copilot pipeline already reasons over. The LLM still narrates a closed,
validated set of facts — the orchestrator only makes sure the right engines
put facts in that set.

What it returns is two things:

- **evidence** — engine-produced facts, ready to merge into the copilot's
  ``Evidence`` (each with an id and its numbers in ``text`` so the validator
  grounds them).
- **an observability record** — the intent, the query classification, the
  engines selected and why, each engine's timing and its SQL / model / retrieved
  documents, and the total latency. This is Phase 14, and it is the honest
  account of how an answer was produced.

The whole layer is gated by ``settings.orchestrator_enabled``. Off, the copilot
behaves exactly as before; on, every question is understood and routed.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field

from app.core.logging import get_logger
from app.orchestrator.base import EngineRequest, EngineResult
from app.orchestrator.classifier import QueryClassifier
from app.orchestrator.router import EngineRouter

logger = get_logger(__name__)


@dataclass
class OrchestrationResult:
    """The engines' merged output plus the trace of how it was produced."""
    classification: dict = field(default_factory=dict)
    engines: list[dict] = field(default_factory=list)   # per-engine describe()
    evidence: list[dict] = field(default_factory=list)   # merge-ready items
    graph: list[dict] = field(default_factory=list)      # execution graph nodes
    latency_ms: float = 0.0
    engines_run: list[str] = field(default_factory=list)

    def describe(self) -> dict:
        return {"classification": self.classification, "engines": self.engines,
                "engines_run": self.engines_run,
                "evidence_added": len(self.evidence),
                "graph": self.graph,
                "latency_ms": round(self.latency_ms, 1)}


class EnterpriseOrchestrator:
    """Classify a question, route it to engines, and merge their evidence."""

    def __init__(self, classifier: QueryClassifier, router: EngineRouter):
        self._classifier = classifier
        self._router = router

    def set_vocab(self, entity_vocab: dict[str, list[str]]) -> None:
        self._classifier.set_vocab(entity_vocab)

    # ---------------------------------------------------------------- run
    def run(self, message: str, intent) -> OrchestrationResult:
        start = time.perf_counter()
        classification = self._classifier.classify(message, intent)
        request = EngineRequest(
            message=message, intent=classification.intent,
            subject=getattr(intent, "subject", ""),
            categories=classification.categories,
            time_range=classification.time_range,
            kpi_hints=classification.kpi_hints,
            entities=classification.entities)

        results = self._router.route(request)
        evidence: list[dict] = []
        engine_records: list[dict] = []
        engines_run: list[str] = []
        for res in results:
            engine_records.append(res.describe())
            if res.status in ("ok", "empty") and res.evidence:
                engines_run.append(res.engine)
            for item in res.evidence:
                evidence.append(item.as_dict())

        result = OrchestrationResult(
            classification=classification.describe(),
            engines=engine_records, evidence=evidence,
            engines_run=engines_run,
            graph=self._graph(classification, results))
        result.latency_ms = (time.perf_counter() - start) * 1000
        return result

    def context_for(self, message: str, intent) -> dict:
        """A dry run for the /copilot/orchestration surface — what the
        orchestrator would do with this question, without narrating it."""
        return self.run(message, intent).describe()

    # ------------------------------------------------------------- graph
    @staticmethod
    def _graph(classification, results: list[EngineResult]) -> list[dict]:
        """The execution graph as a list of nodes the UI renders as a flow:
        User → Classify → Router → [engines] → Merge → LLM."""
        nodes = [
            {"node": "classify", "label": "Query Classification",
             "detail": {"intent": classification.intent,
                        "categories": list(classification.categories),
                        "hybrid": classification.hybrid}},
            {"node": "route", "label": "Engine Router",
             "detail": {"selected": [r.engine for r in results]}},
        ]
        for r in results:
            nodes.append({
                "node": f"engine:{r.engine}", "label": r.label,
                "detail": {"status": r.status,
                           "latency_ms": round(r.latency_ms, 1),
                           "evidence": len(r.evidence), **r.detail}})
        nodes.append({"node": "merge", "label": "Context Builder",
                      "detail": {"evidence_merged":
                                 sum(len(r.evidence) for r in results)}})
        return nodes

    def describe(self) -> dict:
        return {"engines": self._router.describe(),
                "categories": QueryClassifier.vocabulary()}

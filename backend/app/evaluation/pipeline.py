"""Evaluation Pipeline — many evaluators, one verdict the Runtime can act on.

The pipeline runs every applicable evaluator, aggregates their results, and
returns a decision. Aggregation is deliberately **not** an average: an output
that is beautifully formatted, well cited, and contradicts a business rule is
not 75% acceptable. The pipeline takes the most severe recommendation any
evaluator returns, and reports the whole panel so a human can see why.

    accept              → use it
    request_approval    → queue it; a human decides
    regenerate          → ask again, with the reasons attached
    reject              → do not show it; use the honest fallback

Evaluation is **optional by design**. A deployment that disables it behaves
exactly as V2.1 did, because the existing V1 guards (``_verify_evidence``,
``ResponseValidator``) are still in place underneath. This layer adds
inspectability and policy, not the only line of defence.
"""
from __future__ import annotations

import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from app.core.logging import get_logger
from app.evaluation.base import (
    DECISIONS, SEVERITY, EvaluationInput, EvaluationResult, Evaluator,
)
from app.evaluation.evaluators import build_evaluators

logger = get_logger(__name__)

MAX_HISTORY = 500


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class Evaluation:
    """The panel's combined verdict on one output."""
    decision: str = "accept"
    score: float = 1.0
    results: list[EvaluationResult] = field(default_factory=list)
    kind: str = ""
    produced_by: str = ""
    project_id: str = ""
    prompt_id: str = ""
    duration_ms: int = 0
    evaluated_at: str = field(default_factory=now_iso)

    @property
    def accepted(self) -> bool:
        return self.decision == "accept"

    @property
    def failures(self) -> list[EvaluationResult]:
        return [r for r in self.results if not r.passed]

    def reasons(self) -> list[str]:
        """Why the pipeline decided what it decided — the text that goes into
        a regeneration prompt or in front of a human approver."""
        return [f"{r.evaluator}: {r.reason}" for r in self.failures]

    def describe(self) -> dict:
        return {"decision": self.decision, "score": round(self.score, 3),
                "kind": self.kind, "produced_by": self.produced_by,
                "project_id": self.project_id, "prompt_id": self.prompt_id,
                "duration_ms": self.duration_ms,
                "evaluated_at": self.evaluated_at,
                "results": [r.describe() for r in self.results],
                "failures": self.reasons()}


class EvaluationPipeline:
    """Runs the evaluator panel and records every verdict."""

    def __init__(self, evaluators: list[Evaluator] | None = None,
                 enabled: bool = True, bus=None):
        self._evaluators = evaluators if evaluators is not None else build_evaluators()
        self.enabled = enabled
        self._bus = bus
        self._history: list[dict] = []
        self._lock = threading.RLock()

    def attach_bus(self, bus) -> None:
        self._bus = bus

    # ------------------------------------------------------- registration
    def register(self, evaluator: Evaluator) -> None:
        """Add an evaluator. A deployment with its own compliance check adds
        it here rather than editing the pipeline."""
        with self._lock:
            self._evaluators.append(evaluator)

    def evaluators(self) -> list[Evaluator]:
        with self._lock:
            return list(self._evaluators)

    # ---------------------------------------------------------- evaluation
    def evaluate(self, request: EvaluationInput) -> Evaluation:
        """Run the panel. Never raises: a broken evaluator is recorded and
        skipped, because an evaluation layer that can fail an analysis is a
        liability, not a safeguard."""
        evaluation = Evaluation(kind=request.kind,
                                produced_by=request.produced_by,
                                project_id=request.project_id,
                                prompt_id=request.prompt_id)
        if not self.enabled:
            evaluation.results = []
            return evaluation

        started = time.monotonic()
        results: list[EvaluationResult] = []
        for evaluator in self.evaluators():
            if not evaluator.enabled or not evaluator.applies_to(request):
                continue
            try:
                results.append(evaluator.evaluate(request))
            except Exception as exc:  # noqa: BLE001 — an evaluator never fails the work
                logger.exception("Evaluator %s failed", evaluator.name)
                results.append(EvaluationResult(
                    evaluator=evaluator.name, score=1.0,
                    reason=f"evaluator failed and was skipped: "
                           f"{type(exc).__name__}",
                    recommendation="accept",
                    details={"error": str(exc)[:200]}))

        evaluation.results = results
        evaluation.duration_ms = int((time.monotonic() - started) * 1000)
        evaluation.decision = self._decide(results)
        evaluation.score = (round(sum(r.score for r in results) / len(results), 3)
                            if results else 1.0)
        self._record(evaluation)
        self._announce(evaluation)
        return evaluation

    @staticmethod
    def _decide(results: list[EvaluationResult]) -> str:
        """The most severe recommendation on the panel.

        Not an average: one hard failure is a failure however good the rest
        of the panel looks.
        """
        if not results:
            return "accept"
        return max((r.recommendation for r in results),
                   key=lambda d: SEVERITY.get(d, 0))

    # ------------------------------------------------------------ history
    def _record(self, evaluation: Evaluation) -> None:
        with self._lock:
            self._history.append(evaluation.describe())
            del self._history[:-MAX_HISTORY]

    def _announce(self, evaluation: Evaluation) -> None:
        if self._bus is None or evaluation.accepted:
            return
        try:
            self._bus.publish("EvaluationFailed", {
                "decision": evaluation.decision, "kind": evaluation.kind,
                "produced_by": evaluation.produced_by,
                "score": evaluation.score, "reasons": evaluation.reasons()[:5]},
                project_id=evaluation.project_id, source="evaluation")
        except Exception:  # noqa: BLE001 — announcing never fails an evaluation
            logger.exception("Evaluation event publication failed")

    def history(self, limit: int = 50, decision: str = "") -> list[dict]:
        with self._lock:
            items = list(self._history)
        if decision:
            items = [e for e in items if e["decision"] == decision]
        return list(reversed(items))[:limit]

    # --------------------------------------------------------- inspection
    def describe(self) -> list[dict]:
        return [e.describe() for e in self.evaluators()]

    def status(self) -> dict:
        """Evaluation Metrics for the Observability dashboard."""
        with self._lock:
            history = list(self._history)
        by_decision = {d: sum(1 for e in history if e["decision"] == d)
                       for d in DECISIONS}
        by_evaluator: dict[str, dict[str, Any]] = {}
        for entry in history:
            for result in entry["results"]:
                stats = by_evaluator.setdefault(
                    result["evaluator"], {"runs": 0, "failures": 0,
                                          "score_total": 0.0})
                stats["runs"] += 1
                stats["score_total"] += result["score"]
                stats["failures"] += int(result["recommendation"] != "accept")
        for stats in by_evaluator.values():
            stats["avg_score"] = (round(stats.pop("score_total") / stats["runs"], 3)
                                  if stats["runs"] else None)
        return {
            "enabled": self.enabled,
            "evaluators": len(self.evaluators()),
            "evaluated": len(history),
            "by_decision": by_decision,
            "acceptance_rate": (round(by_decision["accept"] / len(history), 3)
                                if history else None),
            "by_evaluator": by_evaluator,
            "avg_score": (round(sum(e["score"] for e in history) / len(history), 3)
                          if history else None),
        }

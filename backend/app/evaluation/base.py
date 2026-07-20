"""Enterprise Evaluation Layer — the contract every evaluator implements.

The platform already refuses to let a model assert things the evidence does
not support: ``AIReasoningEngine._verify_evidence`` guards reports and
``ResponseValidator`` guards conversation. Both are correct, both are
specific, and neither can be inspected, scored, or extended without editing
the code that calls it.

V2.2 makes that capability a **layer**: named evaluators, each returning a
score, a reason, and a recommendation, composed by a pipeline whose verdict
the Runtime acts on. The existing checkers are not replaced — the grounding
and citation evaluators delegate to them, because a second implementation of
"does this number appear in the evidence" is a second thing to get wrong.

Every evaluator answers the same question in its own dimension: *should an
executive be shown this sentence?* The pipeline turns those answers into one
of four outcomes:

    accept              good enough to use
    regenerate          fixable — ask the model again, with the reasons
    request_approval    plausible but consequential; a human decides
    reject              cannot be shown; the honest fallback is used instead
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

# What the pipeline can decide. Ordered by severity: a pipeline takes the
# most severe recommendation any evaluator returns.
DECISIONS = ("accept", "request_approval", "regenerate", "reject")
SEVERITY = {d: i for i, d in enumerate(DECISIONS)}

# What is being evaluated. An evaluator declares which kinds it understands,
# so the pipeline never asks a citation evaluator about a spreadsheet.
OUTPUT_KINDS = ("report", "answer", "summary", "draft", "brief",
                "recommendation")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class EvaluationInput:
    """What an evaluator is given.

    ``output`` is the generated artifact; ``evidence`` is the closed set of
    facts it was allowed to use; everything else is context an evaluator may
    or may not need. Passing one object rather than eight arguments is what
    lets a new evaluator be added without changing every call site.
    """
    kind: str                                   # OUTPUT_KINDS
    output: Any
    evidence: list[dict] = field(default_factory=list)
    business_rules: list[str] = field(default_factory=list)
    context: dict[str, Any] = field(default_factory=dict)
    project_id: str = ""
    prompt_id: str = ""
    produced_by: str = ""                       # agent id
    prior_outputs: list[str] = field(default_factory=list)  # for duplicates

    # Fields that carry prose an executive reads — where a metric claim or a
    # policy violation actually lives. Titles, ids, and enums are labels, not
    # assertions, and flattening them into the prose creates false adjacencies
    # (a "Growth" heading next to a number from another field). Evaluators that
    # reason about wording use ``prose``; only grounding, which cares about
    # every figure wherever it sits, uses the full ``text``.
    PROSE_FIELDS = ("answer", "executive_summary", "portfolio_health",
                    "management_commentary", "confidence_explanation",
                    "summary", "detail", "narrative", "body")

    def text(self) -> str:
        """The output as one searchable string, whatever shape it arrived in.

        Used where position does not matter (does this figure appear at all).
        """
        if isinstance(self.output, str):
            return self.output
        if isinstance(self.output, dict):
            return " ".join(str(v) for v in _walk(self.output))
        return str(self.output)

    def prose_segments(self) -> list[str]:
        """The narrative fields, each kept separate so a claim is judged
        within the sentence that made it, never across a field boundary."""
        if isinstance(self.output, str):
            return [self.output]
        if not isinstance(self.output, dict):
            return [str(self.output)]
        segments: list[str] = []

        def collect(node: Any) -> None:
            if isinstance(node, dict):
                for key, value in node.items():
                    if key in self.PROSE_FIELDS and isinstance(value, str):
                        segments.append(value)
                    else:
                        collect(value)
            elif isinstance(node, (list, tuple)):
                for value in node:
                    collect(value)

        collect(self.output)
        return segments or [self.text()]

    def prose(self) -> str:
        return " ".join(self.prose_segments())


def _walk(node: Any) -> list[Any]:
    """Every leaf string/number in a nested structure."""
    out: list[Any] = []
    if isinstance(node, dict):
        for value in node.values():
            out.extend(_walk(value))
    elif isinstance(node, (list, tuple)):
        for value in node:
            out.extend(_walk(value))
    elif node is not None:
        out.append(node)
    return out


@dataclass
class EvaluationResult:
    """One evaluator's verdict — score, reason, recommendation.

    ``score`` is 0..1 where 1 is "no concern". ``reason`` is written for a
    human reading an audit log, not for a developer reading a stack trace:
    "3 of 5 claims cite no evidence" beats "citation_check_failed".
    """
    evaluator: str
    score: float
    reason: str = ""
    recommendation: str = "accept"              # DECISIONS
    details: dict[str, Any] = field(default_factory=dict)
    evaluated_at: str = field(default_factory=now_iso)

    def __post_init__(self) -> None:
        if self.recommendation not in DECISIONS:
            raise ValueError(
                f"{self.evaluator}: unknown recommendation "
                f"{self.recommendation!r}")
        self.score = max(0.0, min(1.0, float(self.score)))

    @property
    def passed(self) -> bool:
        return self.recommendation == "accept"

    def describe(self) -> dict:
        return {"evaluator": self.evaluator, "score": round(self.score, 3),
                "reason": self.reason, "recommendation": self.recommendation,
                "details": self.details, "evaluated_at": self.evaluated_at}


class Evaluator(ABC):
    """Base class for every evaluator."""

    name: str = "evaluator"
    description: str = ""
    kinds: tuple[str, ...] = OUTPUT_KINDS       # what it can evaluate
    # Below this score the evaluator's recommendation is applied. Declared per
    # evaluator because "acceptable grounding" and "acceptable formatting" are
    # not the same bar.
    threshold: float = 0.7
    # What this evaluator asks for when it fails.
    on_failure: str = "regenerate"
    # An evaluator that cannot run (missing dependency, absent context) is
    # skipped, never guessed at.
    enabled: bool = True

    def applies_to(self, request: EvaluationInput) -> bool:
        return request.kind in self.kinds

    @abstractmethod
    def evaluate(self, request: EvaluationInput) -> EvaluationResult:
        """Score the output in this evaluator's dimension."""

    def _result(self, score: float, reason: str = "",
                details: dict | None = None) -> EvaluationResult:
        """Build a result, applying this evaluator's threshold and policy."""
        return EvaluationResult(
            evaluator=self.name, score=score, reason=reason,
            recommendation=("accept" if score >= self.threshold
                            else self.on_failure),
            details=details or {})

    def describe(self) -> dict:
        return {"name": self.name, "description": self.description,
                "kinds": list(self.kinds), "threshold": self.threshold,
                "on_failure": self.on_failure, "enabled": self.enabled}

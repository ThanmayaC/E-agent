"""The enterprise evaluators.

Eight dimensions, each answering "should an executive be shown this?" from a
different angle. Three of them delegate to checkers the platform already
has — grounding, citations, and business rules were solved in V1's
``ResponseValidator``, and re-deriving "does this number appear in the
evidence" here would produce two answers to one question.

Scores are 0..1 where 1 is no concern. Every failing result explains itself
in a sentence an auditor can read.
"""
from __future__ import annotations

import re
from typing import Any

from app.core.logging import get_logger
from app.evaluation.base import EvaluationInput, EvaluationResult, Evaluator

logger = get_logger(__name__)

NUMBER = re.compile(r"-?\d[\d,]*\.?\d*")
# Words a prohibition shares with ordinary prose; they carry no prohibition
# signal, so requiring them would make every rule trivially "matched".
_STOPWORDS = frozenset({"never", "always", "must", "should", "attribute",
                        "change", "with", "that", "this", "from", "into",
                        "when", "because", "about", "which", "their"})
# Below this Jaccard similarity two outputs are different enough to be worth
# showing separately. Above it the newer one is a restatement.
DUPLICATE_SIMILARITY = 0.85
MIN_TOKENS_FOR_DUPLICATE = 12


class _EvidenceView:
    """Adapts a plain evidence list to the interface ``ResponseValidator``
    expects, so the V1 checkers can be reused unchanged."""

    def __init__(self, evidence: list[dict]):
        self.items = evidence or []
        self.ids = {str(e.get("id")) for e in self.items if e.get("id")}

    def texts(self) -> list[str]:
        return [str(e) for e in self.items]


# ------------------------------------------------------------- grounding
class GroundingEvaluator(Evaluator):
    """Every figure asserted must appear in the evidence.

    Delegates the number matching to the V1 validator's helpers, which
    already handle rounding, percentage restatement, and trivial prose
    numbers — the three things that make a naive implementation reject
    correct answers.
    """

    name = "grounding"
    description = ("Checks that every figure in the output appears in the "
                   "evidence it was given.")
    kinds = ("report", "answer", "summary", "brief", "recommendation")
    threshold = 0.8
    on_failure = "regenerate"

    def evaluate(self, request: EvaluationInput) -> EvaluationResult:
        from app.copilot.validator import (
            TRIVIAL_NUMBER, _matches_any, _numbers_in,
        )

        evidence = _EvidenceView(request.evidence)
        if not evidence.items:
            return EvaluationResult(
                evaluator=self.name, score=0.0,
                reason="no evidence was supplied, so nothing in this output "
                       "can be grounded",
                recommendation="reject")

        known = _numbers_in(evidence.texts() + list(request.business_rules))
        quoted = [round(float(n.replace(",", "")), 4)
                  for n in NUMBER.findall(request.text())
                  if _safe_float(n) is not None]
        checkable = [n for n in quoted if abs(n) > TRIVIAL_NUMBER]
        if not checkable:
            return self._result(1.0, "no quantitative claims to verify")

        ungrounded = [n for n in checkable if not _matches_any(n, known)]
        score = 1.0 - (len(ungrounded) / len(checkable))
        reason = ("every figure traces to the evidence" if not ungrounded else
                  f"{len(ungrounded)} of {len(checkable)} figures do not "
                  f"appear in the evidence: "
                  f"{', '.join(str(n) for n in ungrounded[:3])}")
        return self._result(score, reason,
                            {"checked": len(checkable),
                             "ungrounded": ungrounded[:10]})


# -------------------------------------------------------------- citations
class CitationEvaluator(Evaluator):
    """Claims must cite evidence ids that exist."""

    name = "citation"
    description = ("Checks that cited evidence ids exist and that claims are "
                   "cited at all.")
    kinds = ("report", "answer", "recommendation")
    threshold = 0.7
    on_failure = "regenerate"

    def evaluate(self, request: EvaluationInput) -> EvaluationResult:
        evidence = _EvidenceView(request.evidence)
        cited = _cited_ids(request.output)
        if not cited:
            return EvaluationResult(
                evaluator=self.name, score=0.0,
                reason="the output cites no evidence at all",
                recommendation="request_approval",
                details={"cited": 0})

        invalid = [c for c in cited if c not in evidence.ids]
        score = 1.0 - (len(invalid) / len(cited))
        reason = ("every citation resolves to supplied evidence"
                  if not invalid else
                  f"{len(invalid)} of {len(cited)} cited ids do not exist: "
                  f"{', '.join(invalid[:3])}")
        return self._result(score, reason,
                            {"cited": len(cited), "invalid": invalid[:10]})


# --------------------------------------------------- evidence completeness
class EvidenceCompletenessEvaluator(Evaluator):
    """Is there enough evidence for this output to be worth generating?

    This one runs *before* trusting an output, not after: an answer built on
    two stale facts can be perfectly grounded and still misleading.
    """

    name = "evidence_completeness"
    description = ("Checks whether the evidence set is substantial enough to "
                   "support the output.")
    threshold = 0.5
    on_failure = "request_approval"
    # Below this many evidence items an output is thin however well written.
    thin_evidence = 3

    def evaluate(self, request: EvaluationInput) -> EvaluationResult:
        count = len(request.evidence)
        if not count:
            return EvaluationResult(
                evaluator=self.name, score=0.0,
                reason="no evidence supplied", recommendation="reject")
        kinds = {str(e.get("kind", "")) for e in request.evidence if e.get("kind")}
        score = min(count / (self.thin_evidence * 2), 1.0)
        # Variety matters as much as volume: six KPIs and no quality finding
        # is a narrower picture than three KPIs plus quality plus a signal.
        if len(kinds) > 1:
            score = min(score + 0.15, 1.0)
        reason = (f"{count} evidence item(s) across {len(kinds) or 1} kind(s)"
                  if score >= self.threshold else
                  f"only {count} evidence item(s) — thin support for a "
                  f"{request.kind}")
        return self._result(score, reason,
                            {"items": count, "kinds": sorted(kinds)})


# ------------------------------------------------------ policy compliance
class PolicyComplianceEvaluator(Evaluator):
    """Does the output violate an explicit organizational prohibition?

    Only rules phrased as prohibitions are enforceable deterministically;
    everything else is context for the model, not a gate. That restriction is
    inherited from the V1 validator rather than re-invented.
    """

    name = "policy_compliance"
    description = ("Checks the output against the organization's explicitly "
                   "prohibitive business rules.")
    threshold = 1.0                  # any violation fails
    on_failure = "reject"

    def evaluate(self, request: EvaluationInput) -> EvaluationResult:
        from app.copilot.validator import _prohibition

        if not request.business_rules:
            return self._result(1.0, "no prohibitive rules configured")
        segments = [s.lower() for s in request.prose_segments()]
        violations = []
        for rule in request.business_rules:
            forbidden = _prohibition(rule)
            if forbidden and self._violated(forbidden, segments):
                violations.append(rule)
        score = 0.0 if violations else 1.0
        reason = ("no organizational prohibition is contradicted"
                  if not violations else
                  f"contradicts {len(violations)} business rule(s): "
                  f"{violations[0][:120]}")
        return self._result(score, reason, {"violations": violations[:5]})

    @staticmethod
    def _violated(forbidden: str, segments: list[str]) -> bool:
        """Whether a prohibition is contradicted within a single sentence.

        Verbatim match first (the V1 mechanism). Then a conservative content
        match: the prohibition's significant words all present, and *stemmed*,
        so "attribute revenue change to churn" catches "revenue … churned"
        while staying within one segment to avoid stitching a violation out of
        unrelated fields. All-tokens-present keeps false positives rare — a
        report that merely mentions revenue does not trip a churn rule.
        """
        significant = [w for w in re.findall(r"[a-z]+", forbidden)
                       if len(w) > 3 and w not in _STOPWORDS]
        if not significant:
            return False
        for segment in segments:
            if forbidden in segment:
                return True
            stems = {w[:5] for w in re.findall(r"[a-z]+", segment)}
            if all(any(word[:5] == stem for stem in stems)
                   for word in significant):
                return True
        return False


# ------------------------------------------------------------- formatting
class FormattingEvaluator(Evaluator):
    """Is the output the shape the consumer expects?

    A report missing its executive summary is not a style problem — it is a
    report the assembler cannot render.
    """

    name = "formatting"
    description = "Checks the output's structure against its expected shape."
    threshold = 0.8
    on_failure = "regenerate"

    REQUIRED: dict[str, tuple[str, ...]] = {
        "report": ("executive_summary", "key_insights", "recommendations"),
        "answer": ("answer",),
        "brief": ("date",),
        "recommendation": ("action",),
    }

    def evaluate(self, request: EvaluationInput) -> EvaluationResult:
        required = self.REQUIRED.get(request.kind, ())
        if not required:
            return self._result(1.0, "no structural requirements for this kind")
        if not isinstance(request.output, dict):
            return EvaluationResult(
                evaluator=self.name, score=0.0,
                reason=f"a {request.kind} must be a structured object, got "
                       f"{type(request.output).__name__}",
                recommendation="regenerate")
        missing = [f for f in required if not request.output.get(f)]
        score = 1.0 - (len(missing) / len(required))
        reason = ("every required field is present" if not missing else
                  f"missing required field(s): {', '.join(missing)}")
        return self._result(score, reason, {"missing": missing})


# ------------------------------------------------------------- confidence
class ConfidenceEvaluator(Evaluator):
    """Is the stated confidence defensible given the evidence?

    Overconfidence is the failure mode that actually hurts: an executive acts
    on a number presented as certain. An output claiming 0.9 on two evidence
    items is downgraded, not accepted.
    """

    name = "confidence_estimation"
    description = ("Checks that stated confidence is supported by the volume "
                   "and quality of evidence.")
    threshold = 0.7
    on_failure = "request_approval"

    def evaluate(self, request: EvaluationInput) -> EvaluationResult:
        stated = _stated_confidence(request.output)
        if stated is None:
            return self._result(1.0, "no confidence claimed")
        supportable = self.supportable_for(len(request.evidence))
        if stated <= supportable:
            return self._result(
                1.0, f"stated confidence {stated:.2f} is within what "
                     f"{len(request.evidence)} evidence item(s) support")
        # Overclaiming decays the score below the threshold immediately: the
        # boundary case must not report "exceeds" and then pass itself.
        overclaim = stated - supportable
        score = max(0.0, self.threshold - overclaim * 2)
        return self._result(
            score,
            f"stated confidence {stated:.2f} exceeds what "
            f"{len(request.evidence)} evidence item(s) support "
            f"({supportable:.2f})",
            {"stated": stated, "supportable": round(supportable, 2)})

    @staticmethod
    def supportable_for(evidence_count: int) -> float:
        """The highest defensible confidence for a given evidence volume.

        Calibrated so a normally-evidenced output is not flagged: three
        independent facts already support 0.74, which is where a careful
        analyst would sit. The curve only bites at the tails — near-zero
        evidence, or near-certainty.
        """
        return round(min(0.5 + 0.08 * evidence_count, 0.95), 2)


# -------------------------------------------------------------- duplicates
class DuplicateDetectionEvaluator(Evaluator):
    """Is this output a restatement of one the executive already received?

    An enterprise platform that emails the same insight every morning trains
    people to ignore it, which is worse than not sending it.
    """

    name = "duplicate_detection"
    description = ("Checks whether the output substantially repeats a recent "
                   "one.")
    threshold = 0.7
    on_failure = "reject"

    def evaluate(self, request: EvaluationInput) -> EvaluationResult:
        if not request.prior_outputs:
            return self._result(1.0, "nothing prior to compare against")
        current = _tokens(request.text())
        if len(current) < MIN_TOKENS_FOR_DUPLICATE:
            return self._result(1.0, "output too short to judge as duplicate")
        best, best_score = "", 0.0
        for prior in request.prior_outputs:
            similarity = _jaccard(current, _tokens(prior))
            if similarity > best_score:
                best, best_score = prior, similarity
        if best_score >= DUPLICATE_SIMILARITY:
            return EvaluationResult(
                evaluator=self.name, score=round(1.0 - best_score, 3),
                reason=f"{int(best_score * 100)}% identical to a recent "
                       f"output: {best[:80]}…",
                recommendation="reject",
                details={"similarity": round(best_score, 3)})
        return self._result(1.0, f"most similar prior output is "
                                 f"{int(best_score * 100)}% similar",
                            {"similarity": round(best_score, 3)})


# --------------------------------------------------- business rule validity
class BusinessRuleEvaluator(Evaluator):
    """Does the output respect the organization's declared metric definitions?

    Distinct from policy compliance: that checks prohibitions, this checks
    that a named KPI is one the organization actually defines. Naming a metric
    the business does not have is how a fluent answer becomes wrong.
    """

    name = "business_rule_validation"
    description = ("Checks that metrics named in the output exist in the "
                   "organization's evidence and terminology.")
    kinds = ("report", "answer", "summary", "recommendation")
    threshold = 0.8
    on_failure = "regenerate"

    def evaluate(self, request: EvaluationInput) -> EvaluationResult:
        evidence = _EvidenceView(request.evidence)
        known = " ".join(evidence.texts()).lower()
        known += " " + " ".join(str(t) for t in
                                request.context.get("terminology", []) or []).lower()
        # Judge each prose segment on its own so a heading in one field is
        # never read as a metric claim about a number in another.
        candidates: list[str] = []
        for segment in request.prose_segments():
            candidates.extend(_asserted_metrics(segment))
        candidates = list(dict.fromkeys(candidates))
        if not candidates:
            return self._result(1.0, "no metric names asserted")
        unknown = [p for p in candidates if not _known_metric(p, known)]
        score = 1.0 - (len(unknown) / len(candidates))
        reason = ("every metric named exists in the evidence" if not unknown
                  else f"{len(unknown)} metric name(s) are not defined by the "
                       f"organization: {', '.join(unknown[:3])}")
        return self._result(score, reason, {"unknown": unknown[:10],
                                            "checked": candidates[:10]})


# --------------------------------------------------------------- helpers
def _safe_float(raw: str) -> float | None:
    try:
        return float(raw.replace(",", ""))
    except (ValueError, AttributeError):
        return None


def _cited_ids(output: Any) -> list[str]:
    """Every evidence id cited anywhere in a nested output."""
    found: list[str] = []

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "evidence_ids" and isinstance(value, (list, tuple)):
                    found.extend(str(v) for v in value)
                else:
                    walk(value)
        elif isinstance(node, (list, tuple)):
            for value in node:
                walk(value)

    walk(output)
    return list(dict.fromkeys(found))


def _stated_confidence(output: Any) -> float | None:
    if isinstance(output, dict) and output.get("confidence") is not None:
        try:
            return float(output["confidence"])
        except (TypeError, ValueError):
            return None
    return None


def _tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", str(text).lower())
            if len(w) > 2}


def _jaccard(left: set[str], right: set[str]) -> float:
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def _asserted_metrics(text: str) -> list[str]:
    """Capitalised metric phrases the output *asserts a figure about*.

    Deliberately the same discipline as the V1 validator's ``_check_kpis``:
    a bare capitalised word is a heading, a product, or a month, and flagging
    it produces false rejections rather than safety. Only a metric-looking
    phrase followed closely by a number is a claim about a metric.
    """
    from app.copilot.validator import _looks_like_metric

    found: list[str] = []
    for match in re.finditer(
            r"\b([A-Z][A-Za-z]+(?: [A-Z][A-Za-z]+){0,3})\b(?=[^.]{0,40}?\d)",
            str(text)):
        phrase = match.group(1).strip()
        if len(phrase) < 6 or not _looks_like_metric(phrase):
            continue
        if phrase not in found:
            found.append(phrase)
    return found


def _known_metric(phrase: str, known: str) -> bool:
    """Whether a named metric appears in the evidence or terminology, matching
    in both directions so "Revenue" resolves against "Total Revenue"."""
    lowered = phrase.lower()
    if lowered in known:
        return True
    return any(word in known for word in lowered.split() if len(word) > 3)


def build_evaluators() -> list[Evaluator]:
    """The default evaluator suite, in the order the pipeline runs them."""
    return [
        EvidenceCompletenessEvaluator(),
        GroundingEvaluator(),
        CitationEvaluator(),
        BusinessRuleEvaluator(),
        PolicyComplianceEvaluator(),
        FormattingEvaluator(),
        ConfidenceEvaluator(),
        DuplicateDetectionEvaluator(),
    ]

"""Response Validator — the model's answer is checked before an executive sees it.

The reasoning model is a narrator, not a source. This module is the gate that
enforces that, deterministically, after generation:

    invented citations   an evidence id that does not exist is stripped
    invented KPIs        a KPI name the evidence never mentioned is a rejection
    invented numbers     a figure absent from the evidence is a rejection
    contradicted rules   an answer that violates a business rule is a rejection
    uncited answers      a claim citing nothing cannot be presented as fact
    weak evidence        confidence is capped at what the evidence supports

Rejection is not deletion. A rejected answer is replaced by an honest one —
what was asked, what evidence exists, and what could not be supported — because
"I cannot answer that from the evidence" is a correct answer, and a fluent
fabrication is not.

The platform already applies this contract to generated *reports*
(``AIReasoningEngine._verify_evidence``). This is the same contract applied to
*conversation*, where an executive is most likely to act on a sentence
immediately.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from app.core.logging import get_logger

logger = get_logger(__name__)

VERDICTS = ("verified", "downgraded", "rejected")

# Confidence ceilings. An answer that cites nothing, or rests on thin
# evidence, may not present itself as certain however fluent it is.
UNCITED_CEILING = 0.3
WEAK_EVIDENCE_CEILING = 0.4
# Numbers this small are ordinary prose ("the top 3 risks"), not claims about
# the business — checking them produces false rejections, not safety.
TRIVIAL_NUMBER = 10.0
# A quoted figure may differ from the evidence by this much and still be the
# same number: models legitimately round 120000.0 to 120,000 or 12.04% to 12%.
ROUNDING_TOLERANCE = 0.02

NUMBER_PATTERN = re.compile(r"-?\d[\d,]*\.?\d*")
# Words that mean the model is declining to answer — such an answer is allowed
# to cite nothing, because it asserts nothing.
NON_ANSWER_MARKERS = (
    "cannot answer", "can't answer", "insufficient", "not available",
    "no evidence", "cannot be determined", "would be required",
    "unable to", "not enough data", "does not contain", "no data",
)


@dataclass
class Validation:
    """What the validator found, and what it did about it."""
    verdict: str = "verified"
    confidence: float = 0.0
    original_confidence: float = 0.0
    rejections: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    verified_ids: list[str] = field(default_factory=list)
    rejected_ids: list[str] = field(default_factory=list)

    def describe(self) -> dict:
        return {"verdict": self.verdict, "confidence": self.confidence,
                "original_confidence": self.original_confidence,
                "rejections": self.rejections, "warnings": self.warnings,
                "verified_evidence_ids": self.verified_ids,
                "rejected_evidence_ids": self.rejected_ids}


class ResponseValidator:
    """Checks a generated answer against the evidence it was given."""

    def validate(self, response: dict[str, Any], evidence,
                 business_rules: list[str] | None = None) -> tuple[dict, Validation]:
        """Return ``(response, validation)``. The response is returned already
        corrected: citations stripped, confidence capped, or the whole answer
        replaced when it cannot be supported."""
        validation = Validation(
            confidence=float(response.get("confidence") or 0.0),
            original_confidence=float(response.get("confidence") or 0.0))

        if response.get("status") != "ok":
            validation.verdict = "verified"  # nothing was claimed
            return response, validation

        answer = str(response.get("answer", ""))
        rules = business_rules or []
        self._check_citations(response, evidence, validation)
        self._check_kpis(answer, evidence, validation)
        # Rules are checked before numbers: contradicting the business is a
        # more serious finding than quoting an unsourced figure, and when both
        # are true the executive should be told the important one first.
        self._check_rules(answer, rules, validation)
        self._check_numbers(answer, evidence, rules, validation)
        self._cap_confidence(answer, evidence, validation)

        if validation.rejections:
            validation.verdict = "rejected"
            return self._replace(response, evidence, validation), validation
        if validation.confidence < validation.original_confidence \
                or validation.warnings:
            validation.verdict = "downgraded"
        response["confidence"] = validation.confidence
        response["evidence_ids"] = validation.verified_ids
        return response, validation

    # -------------------------------------------------------------- checks
    def _check_citations(self, response: dict, evidence,
                         validation: Validation) -> None:
        """A citation to evidence that was never supplied is an invention.
        It is stripped, not trusted — the model does not get to name its own
        sources."""
        cited = [str(e) for e in response.get("evidence_ids") or []]
        valid = evidence.ids
        validation.verified_ids = [e for e in cited if e in valid]
        validation.rejected_ids = [e for e in cited if e not in valid]
        if validation.rejected_ids:
            validation.warnings.append(
                f"{len(validation.rejected_ids)} cited evidence id(s) do not "
                f"exist and were stripped: "
                f"{', '.join(validation.rejected_ids[:3])}")

    def _check_kpis(self, answer: str, evidence,
                    validation: Validation) -> None:
        """A KPI the evidence never mentioned is a KPI the model invented.

        The match is on the metric's **core words**, not its surface form: an
        executive-facing model writes "the Success Rate", "Success Rate (%)",
        and "success rate" interchangeably, and all three name the same KPI the
        evidence holds. Comparing raw strings rejected the first two — a false
        alarm that depends only on how the model phrased a real, evidenced
        metric. So both sides are normalised (articles, unit suffixes like
        "(%)"/"(M/day)", and punctuation stripped) and compared on their
        significant words. A phrase only fails when it shares no core term with
        any evidenced KPI — i.e. it names something genuinely absent.
        """
        known = evidence.kpi_names()
        if not known:
            return
        # Only a Title-Case phrase stated next to a figure is a candidate KPI
        # *claim* — capturing lowercase continuation words grabs sentence
        # fragments ("Rate showed an overall"), not metric names.
        for match in re.finditer(r"\b([A-Z][A-Za-z]+(?: [A-Z][A-Za-z]+){0,3})\b"
                                 r"(?=[^.]{0,40}?\d)", answer):
            phrase = match.group(1).strip()
            if not _looks_like_metric(phrase):
                continue
            # A phrase with no identifying word (only generic terms like "Rate",
            # "The Total") cannot be judged invented — skip rather than reject.
            if not _key_tokens(_normalize_metric(phrase)):
                continue
            if not _metric_in_evidence(phrase, known):
                validation.rejections.append(
                    f"the answer names a KPI that is not in the evidence: "
                    f"'{phrase}'")
                return

    def _check_numbers(self, answer: str, evidence, business_rules: list[str],
                       validation: Validation) -> None:
        """Every material figure must come from the evidence.

        This is the check that matters most: an executive acts on numbers, and
        a number the platform cannot source is the single most dangerous thing
        this layer could emit.

        Business rules are a legitimate source too. The rules are given to the
        model as context, so a figure quoted from one ("never discount above
        20%") is sourced, not invented — flagging it would reject a correct
        answer, and a gate that cries wolf gets switched off.
        """
        known = evidence.numbers() | _numbers_in(business_rules)
        if not known:
            return
        for raw in NUMBER_PATTERN.findall(answer):
            try:
                value = float(raw.replace(",", ""))
            except ValueError:
                continue
            if abs(value) <= TRIVIAL_NUMBER:
                continue  # ordinary prose, not a claim about the business
            if not _matches_any(value, known):
                validation.rejections.append(
                    f"the answer states a figure that is not in the "
                    f"evidence: {raw}")
                return

    def _check_rules(self, answer: str, business_rules: list[str],
                     validation: Validation) -> None:
        """An answer that contradicts one of the organization's own rules is
        wrong however well it reads.

        Detection is deliberately narrow: a rule is contradicted when the
        answer recommends the opposite of an explicit prohibition. Anything
        subtler is a warning, not a rejection — a validator that guesses at
        semantics would reject correct answers, and a gate nobody trusts gets
        switched off.
        """
        lowered = answer.lower()
        for rule in business_rules:
            prohibition = _prohibition(rule)
            if prohibition and prohibition in lowered:
                validation.rejections.append(
                    f"the answer contradicts a business rule: {rule[:120]!r}")
                return

    def _cap_confidence(self, answer: str, evidence,
                        validation: Validation) -> None:
        """Confidence must reflect the evidence, not the model's fluency."""
        if evidence.is_weak and validation.confidence > WEAK_EVIDENCE_CEILING:
            validation.confidence = WEAK_EVIDENCE_CEILING
            validation.warnings.append(
                f"confidence capped at {WEAK_EVIDENCE_CEILING} — only "
                f"{len(evidence.items)} evidence item(s) support this answer")
        if not validation.verified_ids and not _is_non_answer(answer) \
                and validation.confidence > UNCITED_CEILING:
            validation.confidence = UNCITED_CEILING
            validation.warnings.append(
                f"confidence capped at {UNCITED_CEILING} — the answer cites "
                f"no verifiable evidence")

    # ------------------------------------------------------------- replace
    def _replace(self, response: dict, evidence,
                 validation: Validation) -> dict:
        """Replace a rejected answer with an honest one.

        The executive is told what was rejected and why, and given the
        evidence that *does* exist. This is the whole justification for the
        validator: without it the alternative is not a worse answer, it is a
        confident wrong one.
        """
        reasons = "; ".join(validation.rejections[:3])
        summaries = [i["summary"] for i in evidence.items[:5]]
        supported = ("\n\nWhat the evidence does support:\n"
                     + "\n".join(f"- {s}" for s in summaries)
                     if summaries else
                     "\n\nNo evidence was found for this question.")
        response = dict(response)
        response["answer"] = (
            "I can't give you that answer from the evidence the platform "
            f"holds. The generated response was rejected because {reasons}."
            f"{supported}")
        response["confidence"] = 0.0
        response["cited_facts"] = []
        response["evidence_ids"] = []
        response["limitations"] = validation.rejections[:3]
        response["suggested_actions"] = []
        validation.confidence = 0.0
        logger.warning("Copilot response rejected: %s", reasons)
        return response


# --------------------------------------------------------------- utilities
def _numbers_in(texts: list[str]) -> set[float]:
    """Every figure appearing in a list of strings — used to treat the
    organization's own business rules as a legitimate source of numbers."""
    found: set[float] = set()
    for text in texts:
        for raw in NUMBER_PATTERN.findall(str(text)):
            try:
                found.add(round(float(raw.replace(",", "")), 4))
            except ValueError:
                continue
    return found


def _matches_any(value: float, known: set[float]) -> bool:
    """Whether a quoted figure is one of the evidence's numbers, allowing for
    legitimate rounding and percentage/ratio restatement."""
    for candidate in known:
        if candidate == value:
            return True
        scale = max(abs(candidate), abs(value), 1.0)
        if abs(candidate - value) / scale <= ROUNDING_TOLERANCE:
            return True
        # A model may quote 0.82 as 82 (a rate stated as a percentage).
        if candidate and abs(abs(candidate * 100) - abs(value)) / max(
                abs(value), 1.0) <= ROUNDING_TOLERANCE:
            return True
    return False


# Generic measurement words that do not, on their own, identify a metric —
# "rate", "total", "average" describe many KPIs, so a shared "rate" is not
# evidence that two phrases name the same one.
_METRIC_GENERIC = {"the", "a", "an", "of", "per", "and", "for", "over", "in",
                   "rate", "ratio", "total", "avg", "average", "percent",
                   "percentage", "pct", "score", "number", "count", "level"}


def _normalize_metric(phrase: str) -> str:
    """Lower-case, drop unit parentheticals ("(%)", "(M/day)") and punctuation,
    collapse whitespace — the surface noise that makes the same metric look
    like three different names."""
    s = phrase.lower()
    s = re.sub(r"\([^)]*\)", " ", s)     # unit suffixes: (%), (Mn), (M/day)
    s = re.sub(r"[^a-z0-9 ]", " ", s)    # slashes, %, ₹, punctuation
    return re.sub(r"\s+", " ", s).strip()


def _key_tokens(norm: str) -> set[str]:
    """The words that actually identify a metric — significant, non-generic."""
    return {t for t in norm.split() if len(t) > 2 and t not in _METRIC_GENERIC}


def _metric_in_evidence(phrase: str, known: set[str]) -> bool:
    """Whether a named metric matches one the evidence holds, comparing core
    words rather than surface form. True (do not reject) when the phrase equals,
    is contained in, contains, or shares an identifying word with any evidenced
    KPI; False only when it names something with no core term in the evidence."""
    norm = _normalize_metric(phrase)
    if not norm:
        return True
    ptok = set(norm.split())
    pkey = _key_tokens(norm)
    for name in known:
        kn = _normalize_metric(name)
        if not kn:
            continue
        if norm == kn or norm in kn or kn in norm:
            return True
        ktok = set(kn.split())
        if ptok and (ptok <= ktok or ktok <= ptok):
            return True
        if pkey and _key_tokens(kn) & pkey:
            return True
    return False


def _looks_like_metric(phrase: str) -> bool:
    """Whether a capitalised phrase is plausibly a metric name rather than a
    product, person, or month."""
    metric_words = ("revenue", "volume", "rate", "customers", "users",
                    "transactions", "retention", "churn", "growth", "score",
                    "margin", "conversion", "adoption", "failures", "value")
    lowered = phrase.lower()
    return any(word in lowered for word in metric_words)


def _prohibition(rule: str) -> str:
    """The action an explicitly prohibitive rule forbids, if any.

    Only rules phrased as prohibitions are enforceable this way; everything
    else is context for the model, not a gate.
    """
    lowered = str(rule).strip().lower()
    for marker in ("never ", "do not ", "don't ", "must not ", "no "):
        if lowered.startswith(marker):
            return lowered[len(marker):].strip(" .")
        if f" {marker}" in lowered:
            return lowered.split(f" {marker}", 1)[1].strip(" .")
    return ""


def _is_non_answer(answer: str) -> bool:
    """Whether the model declined to answer. A refusal asserts nothing, so it
    is allowed to cite nothing."""
    lowered = answer.lower()
    return any(marker in lowered for marker in NON_ANSWER_MARKERS)

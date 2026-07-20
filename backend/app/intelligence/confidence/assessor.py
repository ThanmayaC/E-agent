"""Understanding confidence assessment.

After schema discovery, semantics, and KPI discovery, this engine scores how
well the platform understands the uploaded data and derives the clarification
questions that are genuinely necessary — one per real ambiguity, never
generic. Everything here is deterministic (facts about the platform's own
inferences); the pipeline uses the result to decide whether to proceed to LLM
reasoning or pause and ask the user.

Confidence is scored independently per understanding category (entities,
metrics, time, relationships, ...) and aggregated by WEIGHTED scoring, never
by multiplication: one uncertain inference lowers only its own category, so a
dataset with a strong entity, revenue, and time understanding scores high even
when some attribute columns remain unrecognized.

Schema signatures make answers reusable: an equivalent schema — same
normalized columns, any file name, any project — produces the same signature,
so a clarification answered once is never asked again.
"""
from __future__ import annotations

import hashlib
from typing import Any

from app.domain.entities import (
    KPI, ClarificationOption, ClarificationQuestion, ColumnProfile, InferenceConfidence,
    Relationship, TableProfile, UnderstandingAssessment,
)
from app.domain.enums import BusinessConcept, ColumnRole, SemanticType
from app.intelligence.semantics.ontology import ENTITY_CONCEPTS

MONETARY_CONCEPTS = {
    BusinessConcept.REVENUE, BusinessConcept.VALUE,
    BusinessConcept.FEE, BusinessConcept.PRICE,
}

# lower number = asked first (more blocking for business reasoning)
QUESTION_PRIORITY = {
    "unknown_dataset": 0,
    "revenue_ambiguity": 1,
    "identifier_ambiguity": 2,
    "time_ambiguity": 3,
    "no_kpis": 4,
}

# independent understanding categories and their weight in the overall score
CATEGORY_WEIGHTS: dict[str, float] = {
    "entity_understanding": 0.20,
    "metric_understanding": 0.20,
    "time_understanding": 0.15,
    "business_meaning": 0.15,
    "relationship_understanding": 0.10,
    "dimension_understanding": 0.05,
    "schema_completeness": 0.07,
    "data_quality": 0.08,
}

CATEGORY_LABELS = {
    "entity_understanding": "Entity Understanding",
    "metric_understanding": "Metric Understanding",
    "time_understanding": "Time Understanding",
    "business_meaning": "Business Meaning",
    "relationship_understanding": "Relationship Understanding",
    "dimension_understanding": "Dimension Understanding",
    "schema_completeness": "Schema Completeness",
    "data_quality": "Data Quality",
}


def _mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def dataset_signature(profile: TableProfile) -> str:
    """Deterministic signature of one dataset's schema (normalized column
    names only — identical for the same schema in any file or project)."""
    key = "|".join(sorted(c.normalized_name for c in profile.columns))
    return hashlib.sha1(key.encode()).hexdigest()[:12]


def schema_signature(profiles: list[TableProfile]) -> str:
    """Project-level signature: the set of dataset signatures."""
    key = "|".join(sorted(dataset_signature(p) for p in profiles))
    return hashlib.sha1(key.encode()).hexdigest()[:12]


class ConfidenceAssessor:
    """Scores schema understanding and drafts only-when-necessary
    clarification questions from detected ambiguities."""

    def __init__(self, threshold: float = 0.55, max_questions: int = 6,
                 clear_confidence: float = 0.75):
        self.threshold = threshold
        self.max_questions = max_questions
        self.clear_confidence = clear_confidence

    # ------------------------------------------------------------------ API
    def assess(self, profiles: list[TableProfile], kpis: list[KPI],
               relationships: list[Relationship] | None = None,
               quality: Any = None) -> UnderstandingAssessment:
        signature = schema_signature(profiles)
        questions: list[ClarificationQuestion] = []
        for p in profiles:
            sig = dataset_signature(p)
            questions += self._revenue_ambiguity(p, sig)
            questions += self._identifier_ambiguity(p, sig)
            questions += self._time_ambiguity(p, sig)
            questions += self._unknown_dataset(p, sig)
        if not kpis and profiles:
            questions.append(self._question(
                "no_kpis", "", signature, [],
                "No measurable KPIs were discovered automatically. Which columns "
                "represent the measures that matter to your business "
                "(e.g. revenue, volume, users)?"))

        questions.sort(key=lambda q: (QUESTION_PRIORITY.get(q.kind, 9), q.dataset, q.id))
        questions = questions[: self.max_questions]

        categories = self._categories(profiles, kpis, relationships, quality)
        confidence = self._aggregate(categories, questions)
        return UnderstandingAssessment(
            confidence=confidence,
            threshold=self.threshold,
            schema_signature=signature,
            categories=categories,
            explanation=self._explanation(confidence, categories, questions),
            inferences=self._inferences(profiles),
            questions=questions,
        )

    # ------------------------------------------------------------ questions
    def _revenue_ambiguity(self, p: TableProfile, sig: str) -> list[ClarificationQuestion]:
        monetary = [c for c in p.columns
                    if c.role == ColumnRole.MEASURE
                    and (c.semantic_type == SemanticType.CURRENCY
                         or c.concept in MONETARY_CONCEPTS)]
        if len(monetary) < 2:
            return []
        revenue = [c for c in monetary if c.concept == BusinessConcept.REVENUE]
        vague = [c for c in monetary
                 if c.concept is BusinessConcept.UNKNOWN
                 or c.concept_confidence < self.clear_confidence]
        # one confident revenue column and nothing vague — no question needed
        if len(revenue) <= 1 and not vague:
            return []
        names = ", ".join(c.name for c in monetary)
        return [self._question(
            "revenue_ambiguity", p.name, sig, [c.name for c in monetary],
            f"I found {len(monetary)} monetary columns in '{p.name}' ({names}). "
            "Which one represents actual business revenue?",
            options=[self._option(c) for c in monetary])]

    def _identifier_ambiguity(self, p: TableProfile, sig: str) -> list[ClarificationQuestion]:
        groups: dict[BusinessConcept, list] = {}
        for c in p.columns:
            if c.semantic_type in (SemanticType.IDENTIFIER, SemanticType.CODE) \
                    and c.concept in ENTITY_CONCEPTS:
                groups.setdefault(c.concept, []).append(c)
        out = []
        for concept, cols in sorted(groups.items(), key=lambda kv: kv[0].value):
            if len(cols) < 2:
                continue
            # exactly one primary-key candidate resolves the ambiguity itself
            if sum(1 for c in cols if c.is_pk_candidate) == 1:
                continue
            names = ", ".join(c.name for c in cols)
            out.append(self._question(
                "identifier_ambiguity", p.name, sig, [c.name for c in cols],
                f"I detected multiple possible {concept.value} identifiers in "
                f"'{p.name}' ({names}). Which should be treated as the primary "
                f"{concept.value} identifier?",
                options=[self._option(c) for c in cols]))
        return out

    def _time_ambiguity(self, p: TableProfile, sig: str) -> list[ClarificationQuestion]:
        dates = [c for c in p.columns if c.role == ColumnRole.TIME_DIMENSION]
        if len(dates) < 2:
            return []
        names = ", ".join(c.name for c in dates)
        return [self._question(
            "time_ambiguity", p.name, sig, [c.name for c in dates],
            f"I found multiple date columns in '{p.name}' ({names}). "
            "Which one represents the business reporting period?",
            options=[self._option(c) for c in dates])]

    def _unknown_dataset(self, p: TableProfile, sig: str) -> list[ClarificationQuestion]:
        if p.confidence >= 0.35 or p.column_count < 2:
            return []
        names = ", ".join(c.name for c in p.columns[:8])
        return [self._question(
            "unknown_dataset", p.name, sig, [c.name for c in p.columns[:8]],
            f"I could not confidently determine what the dataset '{p.name}' "
            f"represents (columns: {names}). What business process does this "
            "dataset describe, and which columns matter most?")]

    @staticmethod
    def _question(kind: str, dataset: str, signature: str, candidates: list[str],
                  text: str, options: list[ClarificationOption] | None = None
                  ) -> ClarificationQuestion:
        qid = hashlib.sha1(f"{kind}|{signature}|{dataset}|{','.join(candidates)}"
                           .encode()).hexdigest()[:10]
        return ClarificationQuestion(id=qid, question=text, kind=kind,
                                     dataset=dataset, candidates=candidates,
                                     options=options or [], signature=signature)

    @staticmethod
    def _option(col: ColumnProfile) -> ClarificationOption:
        """Business context for one candidate: what the platform inferred and a
        real sample value, so the user can decide without opening the file."""
        parts = []
        if col.concept is not BusinessConcept.UNKNOWN:
            parts.append(f"detected as {col.concept.value} "
                         f"({col.concept_confidence:.0%})")
        else:
            parts.append(f"type: {col.semantic_type.value}")
        if col.is_pk_candidate:
            parts.append("unique per row")
        if col.samples:
            parts.append(f"sample: {col.samples[0]}")
        return ClarificationOption(value=col.name, detail="; ".join(map(str, parts)))

    # ----------------------------------------------------------- confidence
    @staticmethod
    def _categories(profiles: list[TableProfile], kpis: list[KPI],
                    relationships: list[Relationship] | None,
                    quality: Any) -> dict[str, float]:
        """Independent per-category understanding scores (each 0..1).
        Every score reflects the BEST evidence in its category — a weak
        attribute column never drags down entity or metric understanding."""
        if not profiles:
            return {name: 0.0 for name in CATEGORY_WEIGHTS}
        cols = [c for p in profiles for c in p.columns]
        cat: dict[str, float] = {}

        # entities: how confidently each table's business entity was identified
        per_table = []
        for p in profiles:
            if p.entity is not BusinessConcept.UNKNOWN:
                votes = [c.concept_confidence for c in p.columns if c.concept == p.entity]
                per_table.append(max(votes, default=max(p.confidence, 0.5)))
            else:
                per_table.append(0.25)
        cat["entity_understanding"] = _mean(per_table)

        # metrics: recognized measure columns + whether KPIs were derivable
        measures = [c for c in cols if c.role == ColumnRole.MEASURE]
        col_score = _mean([c.concept_confidence if c.concept is not BusinessConcept.UNKNOWN
                           else 0.3 for c in measures]) if measures else 0.0
        kpi_score = min(len(kpis) / 3.0, 1.0)
        cat["metric_understanding"] = 0.6 * col_score + 0.4 * kpi_score

        # time: fact tables need a detected reporting period; others don't
        facts = [p for p in profiles if p.is_fact]
        pool = facts or profiles
        per_time = [(0.95 if p.time_grain else 0.75) if p.time_column
                    else (0.3 if p.is_fact else 0.6) for p in pool]
        cat["time_understanding"] = _mean(per_time)

        # business meaning: concept coverage across ALL columns (the only
        # category where unrecognized attributes count — by design)
        cat["business_meaning"] = _mean([c.concept_confidence for c in cols])

        # relationships: only meaningful with 2+ datasets
        if len(profiles) < 2:
            cat["relationship_understanding"] = 1.0
        elif relationships:
            cat["relationship_understanding"] = _mean([r.confidence for r in relationships])
        else:
            cat["relationship_understanding"] = 0.35

        # dimensions: recognized dimension/category columns
        dims = [c for c in cols if c.role == ColumnRole.DIMENSION]
        cat["dimension_understanding"] = _mean(
            [c.concept_confidence if c.concept is not BusinessConcept.UNKNOWN else 0.4
             for c in dims]) if dims else 0.6

        # schema completeness: parsed headers + how much data is populated
        cat["schema_completeness"] = _mean([1.0 - min(c.null_pct, 100.0) / 100.0
                                            for c in cols])

        # data quality: from the quality engine when available
        score = getattr(quality, "overall_score", None)
        if score is None and isinstance(quality, dict):
            score = quality.get("overall_score")
        cat["data_quality"] = float(score) / 100.0 if score is not None else 0.7

        return {k: round(min(max(v, 0.0), 1.0), 3) for k, v in cat.items()}

    @staticmethod
    def _aggregate(categories: dict[str, float],
                   questions: list[ClarificationQuestion]) -> float:
        """Weighted aggregation — never multiplication. Unanswered questions
        apply a small bounded penalty so real ambiguity still gates."""
        total_w = sum(CATEGORY_WEIGHTS.values())
        overall = sum(categories.get(name, 0.0) * w
                      for name, w in CATEGORY_WEIGHTS.items()) / total_w
        unanswered = sum(1 for q in questions if not q.answered)
        penalty = min(0.05 * unanswered, 0.15)
        return round(min(max(overall - penalty, 0.0), 1.0), 3)

    @staticmethod
    def _explanation(confidence: float, categories: dict[str, float],
                     questions: list[ClarificationQuestion]) -> str:
        """Deterministic statement of what limits understanding (a fact about
        the platform's own inferences — not business narrative)."""
        weak = sorted(((n, v) for n, v in categories.items() if v < 0.5),
                      key=lambda kv: kv[1])
        parts = [f"Overall understanding {confidence:.0%}."]
        if weak:
            parts.append("Limited by: " + ", ".join(
                f"{CATEGORY_LABELS.get(n, n)} ({v:.0%})" for n, v in weak[:3]) + ".")
        unanswered = sum(1 for q in questions if not q.answered)
        if unanswered:
            parts.append(f"{unanswered} clarification question(s) need an answer "
                         "before business reasoning proceeds.")
        return " ".join(parts)

    @staticmethod
    def _inferences(profiles: list[TableProfile]) -> list[InferenceConfidence]:
        out: list[InferenceConfidence] = []
        for p in profiles:
            if p.entity is not BusinessConcept.UNKNOWN:
                votes = [c.concept_confidence for c in p.columns if c.concept == p.entity]
                out.append(InferenceConfidence(
                    inference=f"{p.entity.value} Entity", subject=p.name,
                    confidence=round(max(votes, default=p.confidence), 3)))
            for c in p.columns:
                if c.concept == BusinessConcept.REVENUE and c.role == ColumnRole.MEASURE:
                    out.append(InferenceConfidence(
                        inference="Revenue Column", subject=f"{p.name}.{c.name}",
                        confidence=c.concept_confidence))
                if c.is_pk_candidate and c.concept in ENTITY_CONCEPTS:
                    out.append(InferenceConfidence(
                        inference=f"{c.concept.value} Identifier",
                        subject=f"{p.name}.{c.name}",
                        confidence=c.concept_confidence))
            if p.time_column:
                col = next((c for c in p.columns if c.name == p.time_column), None)
                if col is not None:
                    out.append(InferenceConfidence(
                        inference="Time Dimension", subject=f"{p.name}.{col.name}",
                        confidence=max(col.concept_confidence, 0.6)))
        return out


# --------------------------------------------------------- report confidence
# Deterministic overall confidence of a generated report. Documented formula:
#
#   report_confidence = 0.8 * understanding_confidence
#                     + 0.2 * mean_forecast_confidence
#
# where understanding_confidence is the weighted aggregation over the
# independent understanding categories above (entity 20%, metric 20%,
# time 15%, business meaning 15%, relationships 10%, dimensions 5%,
# schema completeness 7%, data quality 8%, minus the bounded
# unanswered-question penalty), and mean_forecast_confidence is the mean
# statistical confidence of the non-unavailable forecasts (0.5 neutral prior
# when no KPI could be forecast — absence of forecasts neither boosts nor
# collapses report confidence). Never model-reported, never arbitrary.
UNDERSTANDING_WEIGHT = 0.8
FORECAST_WEIGHT = 0.2
NEUTRAL_FORECAST_CONFIDENCE = 0.5


def report_confidence(understanding: UnderstandingAssessment,
                      forecasts: list[Any]) -> dict[str, Any]:
    """Compute the deterministic report confidence and return it with every
    component, so the number is auditable end to end."""
    usable = [f for f in forecasts if getattr(f, "status", "ok") != "unavailable"]
    mean_forecast = (
        sum(f.confidence for f in usable) / len(usable)
        if usable else NEUTRAL_FORECAST_CONFIDENCE)
    overall = (UNDERSTANDING_WEIGHT * understanding.confidence
               + FORECAST_WEIGHT * mean_forecast)
    return {
        "overall": round(min(max(overall, 0.0), 1.0), 3),
        "formula": (f"{UNDERSTANDING_WEIGHT} * understanding_confidence "
                    f"+ {FORECAST_WEIGHT} * mean_forecast_confidence"),
        "components": {
            "understanding_confidence": understanding.confidence,
            "understanding_categories": understanding.categories,
            "category_weights": CATEGORY_WEIGHTS,
            "mean_forecast_confidence": round(mean_forecast, 3),
            "forecasts_used": len(usable),
            "forecasts_unavailable": len(forecasts) - len(usable),
        },
    }

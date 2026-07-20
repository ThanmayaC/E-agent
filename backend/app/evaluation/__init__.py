"""Enterprise Evaluation Layer (Version 2.2).

Every AI-generated output can pass through a panel of named evaluators, each
returning a score, a reason, and a recommendation. The pipeline aggregates
them into one decision the Runtime acts on: accept, regenerate, request
approval, or reject.

    base         Evaluator · EvaluationInput · EvaluationResult
    evaluators   grounding · citation · evidence completeness · policy
                 compliance · formatting · confidence · duplicates ·
                 business rules
    pipeline     EvaluationPipeline — runs the panel, aggregates, records

This layer adds inspectability and policy on top of the V1 guards
(``AIReasoningEngine._verify_evidence``, ``ResponseValidator``), which remain
in place. Disabling evaluation returns the platform to exactly V2.1
behaviour — it is a second line of defence, never the only one.
"""
from app.evaluation.base import (
    DECISIONS, OUTPUT_KINDS, EvaluationInput, EvaluationResult, Evaluator,
)
from app.evaluation.evaluators import (
    BusinessRuleEvaluator, CitationEvaluator, ConfidenceEvaluator,
    DuplicateDetectionEvaluator, EvidenceCompletenessEvaluator,
    FormattingEvaluator, GroundingEvaluator, PolicyComplianceEvaluator,
    build_evaluators,
)
from app.evaluation.pipeline import Evaluation, EvaluationPipeline

__all__ = [
    "BusinessRuleEvaluator", "CitationEvaluator", "ConfidenceEvaluator",
    "DECISIONS", "DuplicateDetectionEvaluator", "Evaluation",
    "EvaluationInput", "EvaluationPipeline", "EvaluationResult", "Evaluator",
    "EvidenceCompletenessEvaluator", "FormattingEvaluator",
    "GroundingEvaluator", "OUTPUT_KINDS", "PolicyComplianceEvaluator",
    "build_evaluators",
]

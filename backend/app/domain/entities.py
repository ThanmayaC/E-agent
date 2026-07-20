"""Domain entities — the ubiquitous language of the platform.

These are pure Pydantic models with no infrastructure dependencies (DDD).
Every artifact the pipeline produces is expressed in these terms.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field

from app.domain.enums import (
    BusinessConcept,
    Cardinality,
    ColumnRole,
    PipelineStage,
    RelationshipType,
    SemanticType,
    Severity,
    SignalKind,
    StageStatus,
    TimeGrain,
)


# ---------------------------------------------------------------- discovery
class ColumnProfile(BaseModel):
    name: str
    normalized_name: str
    dtype: str
    semantic_type: SemanticType = SemanticType.UNKNOWN
    role: ColumnRole = ColumnRole.ATTRIBUTE
    concept: BusinessConcept = BusinessConcept.UNKNOWN
    concept_confidence: float = 0.0
    null_count: int = 0
    null_pct: float = 0.0
    distinct_count: int = 0
    unique_ratio: float = 0.0
    is_pk_candidate: bool = False
    samples: list[Any] = Field(default_factory=list)
    min_value: Optional[str] = None
    max_value: Optional[str] = None
    mean_value: Optional[float] = None
    std_value: Optional[float] = None
    aliases: list[str] = Field(default_factory=list)
    description: str = ""


class TableProfile(BaseModel):
    dataset_id: str
    name: str
    source_file: str
    source_sheet: str
    row_count: int
    column_count: int
    columns: list[ColumnProfile]
    is_fact: bool = False
    is_dimension: bool = False
    entity: BusinessConcept = BusinessConcept.UNKNOWN
    time_column: Optional[str] = None
    time_grain: Optional[TimeGrain] = None
    primary_key: Optional[str] = None
    merged_from: list[str] = Field(default_factory=list)
    description: str = ""
    confidence: float = 0.0


class WorkbookInfo(BaseModel):
    file_name: str
    file_size: int
    sheet_count: int
    hidden_sheets: list[str] = Field(default_factory=list)
    named_ranges: list[str] = Field(default_factory=list)
    merged_cell_regions: int = 0
    charts: int = 0
    tables_found: int = 0


# ---------------------------------------------------------------- semantics
class Relationship(BaseModel):
    id: str
    from_dataset: str
    from_column: str
    to_dataset: str
    to_column: str
    rel_type: RelationshipType
    cardinality: Cardinality = Cardinality.ONE_TO_MANY
    overlap: float = 0.0
    confidence: float = 0.0
    evidence: str = ""


class SemanticMapping(BaseModel):
    dataset_id: str
    column: str
    concept: BusinessConcept
    semantic_type: SemanticType
    role: ColumnRole
    canonical_name: str
    confidence: float


class KPI(BaseModel):
    id: str
    name: str
    concept: BusinessConcept = BusinessConcept.UNKNOWN
    dataset_id: str
    expression: str  # e.g. SUM(txn_value)
    column: Optional[str] = None
    unit: str = ""
    time_column: Optional[str] = None
    current_value: Optional[float] = None
    previous_value: Optional[float] = None
    growth_pct: Optional[float] = None
    trend: str = "flat"  # up | down | flat
    sparkline: list[float] = Field(default_factory=list)
    sparkline_labels: list[str] = Field(default_factory=list)
    forecast_next: Optional[float] = None
    forecast_confidence: Optional[float] = None
    confidence: float = 0.0


class QualityIssue(BaseModel):
    dataset_id: str
    column: Optional[str] = None
    kind: str
    severity: Severity
    count: int = 0
    detail: str = ""


class QualityReport(BaseModel):
    overall_score: float
    issues: list[QualityIssue] = Field(default_factory=list)
    per_dataset: dict[str, float] = Field(default_factory=dict)


class AnalyticsSignal(BaseModel):
    """A deterministic statistical fact. No business language — only numbers,
    metric references, and machine-readable statistics. Narrative belongs to
    the AI reasoning layer."""
    id: str
    kind: SignalKind
    kpi_id: Optional[str] = None
    kpi_name: Optional[str] = None
    dataset_id: Optional[str] = None
    stats: dict[str, Any] = Field(default_factory=dict)
    strength: float = 0.0  # 0..1 statistical strength / signal-to-noise


class InferenceConfidence(BaseModel):
    """Confidence score for one automatic inference (entity, revenue column,
    time dimension, identifier, ...)."""
    inference: str   # e.g. "Merchant Entity", "Revenue Column", "Time Dimension"
    subject: str     # dataset / column the inference is about
    confidence: float


class ClarificationOption(BaseModel):
    """One selectable answer for a clarification question, with the business
    context the user needs to choose (what the platform inferred and why)."""
    value: str               # the column / answer value to submit
    detail: str = ""         # e.g. "detected as Revenue (75%), sample: 1,240.50"


class ClarificationQuestion(BaseModel):
    """A question the platform must ask instead of guessing. Answered
    questions are stored in enterprise knowledge and never asked again for an
    equivalent schema (matched by signature)."""
    id: str
    question: str
    kind: str                 # revenue_ambiguity | identifier_ambiguity | time_ambiguity | unknown_dataset | no_kpis
    dataset: str = ""
    candidates: list[str] = Field(default_factory=list)
    options: list[ClarificationOption] = Field(default_factory=list)
    signature: str = ""       # schema signature for knowledge reuse
    answer: str = ""          # filled when recalled from knowledge
    answered: bool = False


class UnderstandingAssessment(BaseModel):
    """How well the platform understands the uploaded data. Confidence is
    scored independently per understanding category and aggregated by weighted
    scoring — one uncertain inference never collapses the overall score. When
    overall confidence is below the configured threshold and questions remain
    unanswered, the pipeline pauses instead of guessing."""
    confidence: float
    threshold: float
    schema_signature: str
    categories: dict[str, float] = Field(default_factory=dict)
    explanation: str = ""     # deterministic statement of what limits understanding
    inferences: list[InferenceConfidence] = Field(default_factory=list)
    questions: list[ClarificationQuestion] = Field(default_factory=list)


class AIReport(BaseModel):
    """Structured output of the LLM reasoning pipeline. The backend prepares
    facts; every narrative field here is model-generated."""
    status: str = "ok"  # ok | unavailable | failed
    error: str = ""
    provider: str = ""
    model: str = ""
    executive_summary: str = ""
    portfolio_health: str = ""
    key_insights: list[Any] = Field(default_factory=list)
    root_causes: list[Any] = Field(default_factory=list)
    risks: list[Any] = Field(default_factory=list)
    opportunities: list[Any] = Field(default_factory=list)
    recommendations: list[Any] = Field(default_factory=list)
    priority_actions: list[Any] = Field(default_factory=list)
    data_limitations: list[Any] = Field(default_factory=list)
    management_commentary: str = ""
    next_investigation_areas: list[Any] = Field(default_factory=list)
    confidence_explanation: str = ""
    confidence: float = 0.0
    prompt_confidence: float = 1.0
    clarification_questions: list[Any] = Field(default_factory=list)


class Forecast(BaseModel):
    kpi_id: str
    kpi_name: str
    horizon: str  # next_period | next_quarter | next_year
    periods: list[str]
    values: list[float]
    lower: list[float]
    upper: list[float]
    method: str
    confidence: float
    # validation gate: forecasts never run blindly. "unavailable" carries no
    # values (nothing misleading to display); "low_confidence" carries values
    # plus the deterministic reasons that limit trust.
    status: str = "ok"  # ok | low_confidence | unavailable
    validation: list[str] = Field(default_factory=list)


class DeterministicRecommendation(BaseModel):
    """A recommendation derived by rule from a deterministic finding — never
    from LLM narrative. Each one cites the evidence that triggered it."""
    id: str
    action: str
    trigger: str            # the deterministic finding that fired the rule
    evidence_ids: list[str] = Field(default_factory=list)
    priority: int = 2       # 1 = act now, 2 = plan, 3 = monitor
    source: str = "deterministic"


class StageRun(BaseModel):
    stage: PipelineStage
    status: StageStatus = StageStatus.PENDING
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    detail: str = ""


class ProjectState(BaseModel):
    project_id: str
    name: str
    created_at: datetime
    status: str = "created"  # created | analyzing | awaiting_clarification | ready | failed
    files: list[WorkbookInfo] = Field(default_factory=list)
    stages: list[StageRun] = Field(default_factory=list)
    # report provenance shown on the Projects page
    report_generated_at: Optional[datetime] = None
    report_version: int = 0
    report_confidence: Optional[float] = None  # deterministic (see ConfidenceModel)

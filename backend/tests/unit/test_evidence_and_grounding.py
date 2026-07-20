"""The anti-hallucination contract: evidence verification, forecast gates,
data limitations, deterministic recommendations, and report confidence."""
import pandas as pd

from app.agents.reasoning import AIReasoningEngine
from app.domain.entities import (
    KPI, AIReport, AnalyticsSignal, Forecast, QualityIssue, QualityReport,
    UnderstandingAssessment,
)
from app.domain.enums import Severity, SignalKind
from app.intelligence.confidence.assessor import report_confidence
from app.intelligence.connectors.excel import ExtractedTable
from app.intelligence.context.builder import BusinessContextBuilder
from app.intelligence.forecasting.engine import ForecastEngine
from app.intelligence.profiling.profiler import ColumnProfiler
from app.intelligence.recommendations import RecommendationEngine
from app.intelligence.semantics.meaning import MeaningDetector


# --------------------------------------------------- evidence verification
def test_unsupported_fact_is_downgraded_to_hypothesis():
    report = AIReport(key_insights=[
        {"title": "Supported", "statement_type": "fact",
         "evidence_ids": ["kpi_1"], "confidence": 0.9},
        {"title": "Invented", "statement_type": "fact",
         "evidence_ids": ["made_up_id"], "confidence": 0.9},
    ])
    AIReasoningEngine._verify_evidence(report, {"kpi_1"})
    supported, invented = report.key_insights
    assert supported["verification"] == "evidence_verified"
    assert supported["statement_type"] == "fact"
    assert invented["verification"] == "unverified"
    assert invented["statement_type"] == "hypothesis"  # never presented as fact
    assert invented["confidence"] <= 0.4
    assert invented["evidence_ids"] == []
    assert invented["rejected_evidence_ids"] == ["made_up_id"]


def test_root_causes_are_always_hypotheses():
    report = AIReport(root_causes=[
        {"problem": "Revenue fell", "possible_cause": "competition",
         "statement_type": "fact", "evidence_ids": []},
    ])
    AIReasoningEngine._verify_evidence(report, {"kpi_1"})
    assert report.root_causes[0]["statement_type"] == "hypothesis"
    assert "missing_evidence" in report.root_causes[0]


def test_collect_evidence_ids_walks_context():
    ctx = {"kpis": [{"id": "kpi_1"}], "quality": {"id": "quality:overall"},
           "forecast": [{"id": "forecast:kpi_1"}], "noise": [1, "x", None]}
    ids = AIReasoningEngine._collect_evidence_ids(ctx)
    assert ids == {"kpi_1", "quality:overall", "forecast:kpi_1"}


# ------------------------------------------------------- forecast validation
def test_flat_series_forecast_unavailable():
    kpi = KPI(id="k1", name="Flat", dataset_id="ds1", expression="SUM(x)",
              sparkline=[100.0] * 12,
              sparkline_labels=[f"2024-{m:02d}-01" for m in range(1, 13)])
    fc = ForecastEngine().forecast(kpi)
    assert fc.status == "unavailable"
    assert fc.values == []          # nothing misleading to display
    assert any("insufficient_variance" in r for r in fc.validation)


def test_short_history_is_flagged_low_confidence():
    kpi = KPI(id="k1", name="Short", dataset_id="ds1", expression="SUM(x)",
              sparkline=[100, 130, 90, 145, 110, 160],
              sparkline_labels=[f"2024-{m:02d}-01" for m in range(1, 7)])
    fc = ForecastEngine().forecast(kpi)
    assert fc.status == "low_confidence"
    assert any("history_below_minimum" in r for r in fc.validation)
    assert fc.confidence < 0.6


def test_unavailable_forecast_never_enriches_kpi():
    kpi = KPI(id="k1", name="Flat", dataset_id="ds1", expression="SUM(x)",
              sparkline=[50.0] * 12,
              sparkline_labels=[f"2024-{m:02d}-01" for m in range(1, 13)])
    ForecastEngine().forecast_all([kpi])
    assert kpi.forecast_next is None
    assert kpi.forecast_confidence is None


# --------------------------------------------------------- data limitations
def test_limitations_detected_for_minimal_dataset():
    df = pd.DataFrame({
        "Month": pd.date_range("2024-01-01", periods=12, freq="MS"),
        "Revenue": [100 + i * 3 for i in range(12)],
        "Volume": [50 + i for i in range(12)],
    })
    p = ColumnProfiler().profile_table(ExtractedTable("kpis", "f.xlsx", "s", 0, df), "ds1")
    MeaningDetector().annotate([p])
    lim = BusinessContextBuilder.limitations([p], [])
    missing = {m["dimension"] for m in lim["missing_dimensions"]}
    assert {"customer", "merchant", "geography", "product"} <= missing
    assert "external_variables" in missing
    impacts = " ".join(m["impact"] for m in lim["missing_dimensions"])
    assert "Customer behaviour cannot be analysed" in impacts


# ------------------------------------------- deterministic recommendations
def test_recommendations_derive_only_from_findings():
    quality = QualityReport(overall_score=72, issues=[
        QualityIssue(dataset_id="ds1", column="Region", kind="missing_values",
                     severity=Severity.HIGH, count=120)])
    forecasts = [Forecast(kpi_id="k1", kpi_name="Revenue", horizon="next_period",
                          periods=[], values=[1.0], lower=[0.5], upper=[1.5],
                          method="linear trend", confidence=0.4,
                          status="low_confidence",
                          validation=["history_below_minimum: 6 periods"])]
    signals = [AnalyticsSignal(id="sig_1", kind=SignalKind.ANOMALY,
                               kpi_name="Revenue", strength=0.9)]
    recs = RecommendationEngine().derive(
        quality, forecasts, signals,
        {"missing_dimensions": [{"dimension": "customer", "impact": "no customer data"}]})
    actions = " ".join(r.action for r in recs)
    assert "Improve data quality" in actions
    assert "Collect additional historical observations" in actions
    assert "Investigate the anomaly" in actions
    assert "customer-level data" in actions
    # every recommendation states its deterministic trigger
    assert all(r.trigger for r in recs)
    assert all(r.source == "deterministic" for r in recs)


# ------------------------------------------------------- confidence model
def test_report_confidence_is_deterministic_and_documented():
    understanding = UnderstandingAssessment(
        confidence=0.8, threshold=0.55, schema_signature="abc",
        categories={"entity_understanding": 0.9})
    forecasts = [
        Forecast(kpi_id="k1", kpi_name="A", horizon="next_period", periods=[],
                 values=[1.0], lower=[0.5], upper=[1.5], method="m", confidence=0.7),
        Forecast(kpi_id="k2", kpi_name="B", horizon="next_period", periods=[],
                 values=[], lower=[], upper=[], method="none", confidence=0.0,
                 status="unavailable"),
    ]
    result = report_confidence(understanding, forecasts)
    # 0.8 * 0.8 + 0.2 * 0.7 = 0.78 — exactly the documented formula
    assert result["overall"] == 0.78
    assert "formula" in result
    assert result["components"]["forecasts_unavailable"] == 1
    # deterministic: same inputs, same output
    assert report_confidence(understanding, forecasts) == result

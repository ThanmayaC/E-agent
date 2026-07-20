"""Deterministic layer must produce facts only; context builder must be compact."""
import json

from app.domain.entities import KPI, QualityReport
from app.domain.enums import SignalKind
from app.intelligence.analytics.signals import SignalEngine
from app.intelligence.context.builder import BusinessContextBuilder


def _kpi(name: str, values: list[float], kpi_id: str = "k1") -> KPI:
    k = KPI(id=kpi_id, name=name, dataset_id="ds1", expression="SUM(x)",
            sparkline=values,
            sparkline_labels=[f"2024-{i % 12 + 1:02d}-01" for i in range(len(values))])
    if len(values) >= 2:
        k.current_value, k.previous_value = values[-1], values[-2]
        k.growth_pct = round((values[-1] - values[-2]) / abs(values[-2]) * 100, 2)
    return k


def test_trend_and_anomaly_signals_are_numeric_facts():
    rising = _kpi("Revenue", [100, 110, 121, 133, 146, 161, 177, 195, 400])  # jump at end
    signals = SignalEngine().compute([rising], [])
    kinds = {s.kind for s in signals}
    assert SignalKind.TREND in kinds
    assert SignalKind.ANOMALY in kinds
    for s in signals:
        # facts only: stats are numbers/strings, no narrative fields
        assert not hasattr(s, "title")
        assert not hasattr(s, "detail")
        assert 0 <= s.strength <= 1
        json.dumps(s.stats)  # must be serializable


def test_inverse_correlation_signal():
    a = _kpi("Product A", [100, 95, 90, 84, 80, 74, 70, 65], "ka")
    b = _kpi("Product B", [10, 16, 22, 27, 33, 39, 44, 50], "kb")
    signals = SignalEngine().compute([a, b], [])
    inv = [s for s in signals if s.kind == SignalKind.INVERSE_CORRELATION]
    assert inv and inv[0].stats["correlation"] < -0.9


def test_concentration_signal():
    breakdowns = [{"dataset": "txns", "measure": "amount", "dimension": "merchant",
                   "title": "amount by merchant", "columns": ["dim", "total"],
                   "rows": [["M1", 900], ["M2", 40], ["M3", 30], ["M4", 20], ["M5", 10]]}]
    signals = SignalEngine().compute([], breakdowns)
    conc = [s for s in signals if s.kind == SignalKind.CONCENTRATION]
    assert conc and conc[0].stats["top20pct_share"] >= 0.85


def test_context_builder_is_compact_and_json_serializable():
    kpis = [_kpi(f"KPI {i}", [100 + j * i for j in range(12)], f"k{i}") for i in range(1, 20)]
    quality = QualityReport(overall_score=88.0, issues=[], per_dataset={})
    ctx = BusinessContextBuilder().build("Demo", [], [], kpis, [], [], quality)
    for key in ["portfolio_summary", "schema", "relationships", "quality", "kpis",
                "forecast", "anomalies", "correlations", "top_changes",
                "cannibalization", "growth", "executive_metrics"]:
        assert key in ctx, key
    assert len(ctx["kpis"]) <= 12                      # compact, not everything
    assert all(len(k["history_tail"]) <= 12 for k in ctx["kpis"])
    payload = json.dumps(ctx, default=str)
    assert len(payload) < 60_000                       # never raw data dumps
    assert isinstance(ctx["executive_metrics"]["health_score"], float)

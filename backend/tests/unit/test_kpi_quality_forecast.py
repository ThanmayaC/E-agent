import pandas as pd

from app.domain.entities import KPI
from app.intelligence.forecasting.engine import ForecastEngine
from app.intelligence.connectors.excel import ExtractedTable
from app.intelligence.kpi.discovery import KPIDiscovery
from app.intelligence.profiling.profiler import ColumnProfiler
from app.intelligence.quality.engine import QualityEngine
from app.intelligence.semantics.meaning import MeaningDetector
from app.intelligence.timeseries.detector import TimeSeriesDetector


def _profiles_and_frames(txn_frame):
    p = ColumnProfiler().profile_table(
        ExtractedTable("txns", "t.xlsx", "s", 0, txn_frame), "ds1")
    MeaningDetector().annotate([p])
    frames = {"ds1": txn_frame}
    TimeSeriesDetector().annotate([p], frames)
    return [p], frames


def test_kpis_discovered(txn_frame):
    profiles, frames = _profiles_and_frames(txn_frame)
    kpis = KPIDiscovery().discover(profiles, frames)
    names = " ".join(k.name for k in kpis).lower()
    assert any("value" in n or "revenue" in n for n in names.split())
    assert any("success rate" in k.name.lower() for k in kpis)
    ts_kpis = [k for k in kpis if k.sparkline]
    assert ts_kpis, "expected time-series KPIs from dated data"
    assert ts_kpis[0].current_value is not None


def test_quality_flags_nulls_and_dupes(txn_frame):
    frame = txn_frame.copy()
    frame.loc[:100, "Region"] = None
    frame = pd.concat([frame, frame.head(30)], ignore_index=True)
    profiles, _ = _profiles_and_frames(frame)
    report = QualityEngine().assess(profiles, {"ds1": frame})
    kinds = {i.kind for i in report.issues}
    assert "missing_values" in kinds
    assert "duplicate_rows" in kinds
    assert 0 < report.overall_score <= 100


def test_forecast_produces_intervals():
    kpi = KPI(id="k1", name="Revenue", dataset_id="ds1", expression="SUM(x)",
              sparkline=[100, 110, 120, 128, 140, 150, 155, 168, 180, 190, 200, 212],
              sparkline_labels=[f"2024-{m:02d}-01" for m in range(1, 13)])
    fc = ForecastEngine().forecast(kpi, horizon=3)
    assert len(fc.values) == 3
    assert fc.values[0] > 200          # continues upward trend
    assert fc.lower[0] < fc.values[0] < fc.upper[0]
    assert 0.2 <= fc.confidence <= 0.95

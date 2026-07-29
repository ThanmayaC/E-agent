"""Evidence-aware analysis: incomplete periods and non-additive columns.

These guard the two defects that made a single upload produce a fabricated
"-98.9% revenue collapse": a three-day trailing month compared against a full
one, and identifier columns summed as if they were quantities.
"""
import pandas as pd

from app.domain.enums import ColumnRole, SemanticType
from app.intelligence.connectors.excel import ExtractedTable
from app.intelligence.feasibility import AnalysisFeasibility
from app.intelligence.kpi.discovery import KPIDiscovery
from app.intelligence.profiling.profiler import ColumnProfiler
from app.intelligence.semantics.meaning import MeaningDetector
from app.intelligence.timeseries.detector import period_coverage
from app.intelligence.timeseries.detector import resample_series


def _frame(months: int = 12, trailing_days: int | None = None,
           per_month: int = 300, extra: dict | None = None) -> pd.DataFrame:
    """Monthly data, optionally with a short (incomplete) trailing month."""
    rows = []
    for m in range(1, months + 1):
        days = pd.Period(f"2024-{m:02d}", freq="M").days_in_month
        for i in range(per_month):
            rows.append({"txndate": f"2024-{m:02d}-{(i % days) + 1:02d}",
                         "amount": 100.0})
    if trailing_days:
        for d in range(1, trailing_days + 1):
            rows.append({"txndate": f"2025-01-{d:02d}", "amount": 100.0})
    df = pd.DataFrame(rows)
    for name, values in (extra or {}).items():
        df[name] = [values[i % len(values)] for i in range(len(df))]
    return df


def _single_period_frame(rows: int = 200) -> pd.DataFrame:
    """One reporting period: every row lands on the same day, so the series
    resamples to a single bucket."""
    return pd.DataFrame([{"txndate": "2024-01-15", "amount": 100.0}
                         for _ in range(rows)])


def _profile(df: pd.DataFrame):
    p = ColumnProfiler().profile_table(
        ExtractedTable("txns", "t.csv", "s", 0, df), "ds1")
    MeaningDetector().annotate([p])
    p.time_column = "txndate"
    return p


# ------------------------------------------------------- period completeness
def test_trailing_partial_period_is_detected_and_excluded():
    df = _frame(months=12, trailing_days=3)
    cov = period_coverage(df, "txndate")

    assert cov.periods == 13
    assert cov.complete_periods == 12
    assert cov.trailing is not None
    assert cov.trailing.label == "2025-01"
    assert cov.trailing.coverage < 0.2
    assert "excluded" in cov.trailing.reason

    complete = resample_series(df, "txndate", "amount", "sum",
                               coverage=cov, complete_only=True)
    assert len(complete) == 12
    assert "2025-01" not in [str(i)[:7] for i in complete.index]


def test_comparison_uses_last_two_complete_periods():
    """The partial month must not become 'current' — that is the bug that
    turned three days of data into a 98.9% revenue collapse."""
    df = _frame(months=12, trailing_days=3, per_month=300)
    kpis = KPIDiscovery().discover([_profile(df)], {"ds1": df})
    amount = next(k for k in kpis if k.column == "amount")

    assert amount.current_period_label == "2024-12"
    assert amount.previous_period_label == "2024-11"
    assert amount.excluded_periods == ["2025-01"]
    # equal volume per month => no change; the partial month would have shown -99%
    assert amount.growth_pct == 0.0


def test_quiet_but_complete_period_is_kept():
    """A genuinely low month is complete and must not be discarded."""
    df = _frame(months=6, per_month=300)
    quiet = pd.DataFrame([{"txndate": f"2024-07-{d:02d}", "amount": 100.0}
                          for d in range(1, 32)])          # full month, few rows
    df = pd.concat([df, quiet], ignore_index=True)
    cov = period_coverage(df, "txndate")

    assert cov.trailing is None, "a complete month must never be excluded"
    assert cov.complete_periods == 7


def test_single_period_refuses_a_comparison_with_a_reason():
    df = _single_period_frame()
    kpis = KPIDiscovery().discover([_profile(df)], {"ds1": df})
    amount = next(k for k in kpis if k.column == "amount")

    assert amount.growth_pct is None
    assert amount.previous_value is None
    assert "at least 2" in amount.comparison_unavailable_reason


# ------------------------------------------------ non-additive numeric columns
def test_phone_numbers_never_become_a_kpi():
    df = _frame(months=6, extra={
        "prdmobile": [9775838840 + i for i in range(500)],
    })
    profile = _profile(df)
    mobile = next(c for c in profile.columns if c.name == "prdmobile")

    assert mobile.role != ColumnRole.MEASURE
    assert mobile.exclusion_reason

    kpis = KPIDiscovery().discover([profile], {"ds1": df})
    assert not any("prdmobile" in (k.column or "") and k.expression.startswith("SUM")
                   for k in kpis)


def test_low_cardinality_codes_are_dimensions_not_measures():
    # a name that hints at neither an identifier nor a quantity, so only the
    # value-shape heuristic can catch it
    df = _frame(months=6, extra={"riskband": [0, 14, 77, 4]})
    profile = _profile(df)
    col = next(c for c in profile.columns if c.name == "riskband")

    assert col.role != ColumnRole.MEASURE
    assert col.exclusion_reason
    assert "distinct" in col.exclusion_reason


def test_quantity_like_columns_stay_measures():
    """The heuristics must not swallow real low-cardinality quantities."""
    df = _frame(months=6, extra={"item_qty": [1, 2, 3, 4, 5]})
    profile = _profile(df)
    qty = next(c for c in profile.columns if c.name == "item_qty")

    assert qty.role == ColumnRole.MEASURE
    assert qty.semantic_type in (SemanticType.MEASURE, SemanticType.CURRENCY)


# ------------------------------------------------------------- feasibility
def test_feasibility_reports_what_is_unsupported_and_why():
    df = _single_period_frame()
    profile = _profile(df)
    discovery = KPIDiscovery()
    kpis = discovery.discover([profile], {"ds1": df})

    result = AnalysisFeasibility().assess([profile], kpis, discovery.coverage)

    assert "period_comparison" in result["unsupported"]
    assert "forecast" in result["unsupported"]
    comparison = next(c for c in result["checks"]
                      if c["analysis"] == "period_comparison")
    assert "required" in comparison["reason"]
    # one dataset can never be compared against another
    assert "cross_dataset_comparison" in result["unsupported"]


def test_feasibility_allows_analysis_when_history_supports_it():
    df = _frame(months=12, trailing_days=3)
    profile = _profile(df)
    discovery = KPIDiscovery()
    kpis = discovery.discover([profile], {"ds1": df})

    result = AnalysisFeasibility().assess([profile], kpis, discovery.coverage)

    assert "period_comparison" in result["supported"]
    assert result["complete_periods"] == 12
    assert result["excluded_partial_periods"][0]["period"] == "2025-01"

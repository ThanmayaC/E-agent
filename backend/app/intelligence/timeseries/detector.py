"""Time series detection: grain, trend, seasonality, growth rates.

Also owns **period completeness**, which every downstream analytic depends on.
A resampled series' first and last buckets are frequently incomplete — an
upload that stops on the 3rd of the month produces a final "month" holding
three days. Comparing that bucket against a full one manufactures a
catastrophic decline that never happened, and the same artifact then
propagates into anomaly z-scores, forecasts, and the health score.

So completeness is measured here, once, and the partial buckets are excluded
from analysis rather than silently averaged in. They are never deleted: the
coverage record names them, so a report can state exactly what was set aside
and why.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import pandas as pd

from app.domain.entities import TableProfile
from app.domain.enums import TimeGrain

# A bucket counts as complete when the data covers at least this much of the
# calendar period AND the bucket holds at least this share of the median
# bucket's rows. BOTH must indicate "partial" before a bucket is excluded — a
# genuinely quiet month is complete, and must not be thrown away for being small.
MIN_CALENDAR_COVERAGE = 0.9
MIN_ROW_SHARE = 0.5

# pandas resample rule -> the Period freq that describes the same span
_PERIOD_FREQ = {"D": "D", "W": "W", "MS": "M", "QS": "Q", "YS": "Y"}


class TimeSeriesDetector:
    def annotate(self, profiles: list[TableProfile], frames: dict[str, pd.DataFrame]) -> None:
        for p in profiles:
            if not p.time_column:
                continue
            df = frames.get(p.dataset_id)
            if df is None or p.time_column not in df:
                continue
            dates = pd.to_datetime(df[p.time_column], errors="coerce", format="mixed").dropna().sort_values()
            if len(dates) < 3:
                continue
            p.time_grain = self._grain(dates)

    @staticmethod
    def _grain(dates: pd.Series) -> TimeGrain:
        deltas = dates.drop_duplicates().diff().dropna().dt.days
        if deltas.empty:
            return TimeGrain.IRREGULAR
        median = float(deltas.median())
        if median <= 1.5:
            return TimeGrain.DAILY
        if median <= 8:
            return TimeGrain.WEEKLY
        if median <= 45:
            return TimeGrain.MONTHLY
        if median <= 120:
            return TimeGrain.QUARTERLY
        if median <= 400:
            return TimeGrain.YEARLY
        return TimeGrain.IRREGULAR


@dataclass
class PartialPeriod:
    """One incomplete bucket at an end of the series, and why it is incomplete."""
    label: str
    coverage: float          # 0..1 of the calendar period actually observed
    rows: int
    reason: str

    def describe(self) -> dict:
        return {"period": self.label, "coverage_pct": round(self.coverage * 100, 1),
                "rows": self.rows, "reason": self.reason}


@dataclass
class PeriodCoverage:
    """What the time axis of one table actually supports.

    Depends only on the time column, so it is computed once per table and
    reused for every KPI derived from it.
    """
    rule: str = "MS"
    grain: str = "monthly"
    periods: int = 0
    complete_periods: int = 0
    labels: list[str] = field(default_factory=list)
    complete_labels: list[str] = field(default_factory=list)
    leading: PartialPeriod | None = None
    trailing: PartialPeriod | None = None
    median_rows: float = 0.0
    total_rows: int = 0
    coverage_assessable: bool = True

    @property
    def excluded(self) -> list[PartialPeriod]:
        return [p for p in (self.leading, self.trailing) if p is not None]

    def describe(self) -> dict:
        return {
            "grain": self.grain,
            "periods_observed": self.periods,
            "complete_periods": self.complete_periods,
            "first_period": self.labels[0] if self.labels else "",
            "last_period": self.labels[-1] if self.labels else "",
            "last_complete_period": self.complete_labels[-1] if self.complete_labels else "",
            "median_rows_per_period": round(self.median_rows, 1),
            "excluded_partial_periods": [p.describe() for p in self.excluded],
            "coverage_assessable": self.coverage_assessable,
        }


def _resample_rule(index: pd.DatetimeIndex) -> tuple[str, TimeGrain]:
    grain = TimeSeriesDetector._grain(index.to_series())
    rule = {"daily": "D", "weekly": "W", "monthly": "MS", "quarterly": "QS",
            "yearly": "YS"}.get(grain.value, "MS")
    # collapse to at most ~60 points for stable analytics: daily data -> monthly
    if grain in (TimeGrain.DAILY, TimeGrain.WEEKLY) and (index.max() - index.min()).days > 92:
        rule, grain = "MS", TimeGrain.MONTHLY
    return rule, grain


def period_coverage(df: pd.DataFrame, time_col: str) -> PeriodCoverage:
    """Assess which resampled buckets are complete.

    Only the first and last buckets are judged: an interior gap is a data
    quality problem, not a partial reporting period, and the quality engine
    already reports it.
    """
    stamps = pd.to_datetime(df[time_col], errors="coerce", format="mixed").dropna()
    if stamps.empty:
        return PeriodCoverage(periods=0)
    stamps = stamps.sort_values()
    index = pd.DatetimeIndex(stamps)
    rule, grain = _resample_rule(index)

    counts = pd.Series(1, index=index).resample(rule).sum()
    counts = counts[counts > 0]
    if counts.empty:
        return PeriodCoverage(rule=rule, grain=grain.value, periods=0)

    labels = [_label(ts, rule) for ts in counts.index]
    coverage = PeriodCoverage(
        rule=rule, grain=grain.value, periods=len(counts), labels=labels,
        median_rows=float(counts.median()), total_rows=int(counts.sum()))

    # A timestamp resolution coarser than (or equal to) the bucket makes
    # calendar coverage meaningless — every date-only daily bucket would look
    # like a single instant. Say so rather than guessing.
    resolution = _resolution(index)
    period_freq = _PERIOD_FREQ.get(rule, "M")
    sample_period = pd.Period(counts.index[0], freq=period_freq)
    bucket_span = sample_period.end_time - sample_period.start_time
    coverage.coverage_assessable = bucket_span > resolution * 1.5

    if len(counts) >= 2 and coverage.coverage_assessable:
        edges = {"leading": counts.index[0], "trailing": counts.index[-1]}
        for which, bucket in edges.items():
            partial = _assess_bucket(index, bucket, period_freq, resolution,
                                     int(counts.loc[bucket]), coverage.median_rows,
                                     counts, which)
            setattr(coverage, which, partial)

    excluded = {p.label for p in coverage.excluded}
    coverage.complete_labels = [lb for lb in labels if lb not in excluded]
    coverage.complete_periods = len(coverage.complete_labels)
    return coverage


def _assess_bucket(index: pd.DatetimeIndex, bucket, period_freq: str,
                   resolution: pd.Timedelta, rows: int, median_rows: float,
                   counts: pd.Series, which: str) -> PartialPeriod | None:
    period = pd.Period(bucket, freq=period_freq)
    start, end = period.start_time, period.end_time
    inside = index[(index >= start) & (index <= end)]
    if len(inside) == 0:
        return None

    span = (end - start) + resolution
    if which == "leading":
        observed = (end - inside.min()) + resolution
    else:
        observed = (inside.max() - start) + resolution
    calendar = min(max(observed / span, 0.0), 1.0)

    # Compare against the other buckets, so the edge is not its own baseline.
    others = counts.drop(index=[bucket])
    baseline = float(others.median()) if len(others) else median_rows
    row_share = rows / baseline if baseline else 1.0

    if calendar >= MIN_CALENDAR_COVERAGE or row_share >= MIN_ROW_SHARE:
        return None
    return PartialPeriod(
        label=_label(bucket, _rule_for_period(period_freq)),
        coverage=round(float(calendar), 4), rows=rows,
        reason=(f"{which} period covers {calendar:.0%} of the calendar period "
                f"and holds {rows} row(s) vs a median of {baseline:.0f} — "
                f"excluded from period comparisons, trends, anomalies and forecasts"))


def _resolution(index: pd.DatetimeIndex) -> pd.Timedelta:
    """Finest unit the timestamps actually distinguish."""
    if len(index) and (index.hour == 0).all() and (index.minute == 0).all() \
            and (index.second == 0).all():
        return pd.Timedelta(days=1)
    return pd.Timedelta(seconds=1)


def _rule_for_period(period_freq: str) -> str:
    for rule, freq in _PERIOD_FREQ.items():
        if freq == period_freq:
            return rule
    return "MS"


def _label(ts, rule: str) -> str:
    if rule == "MS":
        return pd.Timestamp(ts).strftime("%Y-%m")
    if rule == "YS":
        return pd.Timestamp(ts).strftime("%Y")
    if rule == "QS":
        return str(pd.Period(ts, freq="Q"))
    return pd.Timestamp(ts).strftime("%Y-%m-%d")


def resample_series(df: pd.DataFrame, time_col: str, value_col: str, agg: str = "sum",
                    coverage: PeriodCoverage | None = None,
                    complete_only: bool = False) -> pd.Series:
    """Resample a value column onto the table's reporting grain.

    With ``complete_only`` the partial edge buckets named by ``coverage`` are
    dropped, which is what every KPI, signal and forecast consumes.
    """
    data = df[[time_col, value_col]].copy()
    data[time_col] = pd.to_datetime(data[time_col], errors="coerce", format="mixed")
    data[value_col] = pd.to_numeric(data[value_col], errors="coerce")
    data = data.dropna()
    if data.empty:
        return pd.Series(dtype=float)
    series = data.set_index(time_col)[value_col].sort_index()
    rule = coverage.rule if coverage else _resample_rule(pd.DatetimeIndex(series.index))[0]
    resampled = series.resample(rule).sum() if agg == "sum" else series.resample(rule).mean()
    resampled = resampled.dropna()
    if complete_only and coverage is not None:
        resampled = drop_partial(resampled, coverage)
    return resampled


def drop_partial(series: pd.Series, coverage: PeriodCoverage) -> pd.Series:
    """Remove the partial edge buckets from an already-resampled series."""
    excluded = {p.label for p in coverage.excluded}
    if not excluded or series.empty:
        return series
    keep = [lb not in excluded for lb in (_label(ts, coverage.rule) for ts in series.index)]
    return series[pd.Series(keep, index=series.index)]

"""Time series detection: grain, trend, seasonality, growth rates."""
from __future__ import annotations

import pandas as pd

from app.domain.entities import TableProfile
from app.domain.enums import TimeGrain


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


def resample_series(df: pd.DataFrame, time_col: str, value_col: str, agg: str = "sum") -> pd.Series:
    """Return a monthly-resampled series for KPI/insight/forecast computations."""
    data = df[[time_col, value_col]].copy()
    data[time_col] = pd.to_datetime(data[time_col], errors="coerce", format="mixed")
    data[value_col] = pd.to_numeric(data[value_col], errors="coerce")
    data = data.dropna()
    if data.empty:
        return pd.Series(dtype=float)
    series = data.set_index(time_col)[value_col].sort_index()
    grain = TimeSeriesDetector._grain(series.index.to_series())
    rule = {"daily": "D", "weekly": "W", "monthly": "MS", "quarterly": "QS", "yearly": "YS"}.get(grain.value, "MS")
    # collapse to at most ~60 points for stable analytics: daily data -> monthly
    if grain in (TimeGrain.DAILY, TimeGrain.WEEKLY) and (series.index.max() - series.index.min()).days > 92:
        rule = "MS"
    resampled = series.resample(rule).sum() if agg == "sum" else series.resample(rule).mean()
    return resampled.dropna()

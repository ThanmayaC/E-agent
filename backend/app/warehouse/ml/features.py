"""Feature engineering — raw transactions to a modelling frame.

The models never see a transaction. They see a daily frame in which every
column is either (a) something the business already knows on the morning of
that day, or (b) a lagged fact from days already closed. That discipline is
what makes a backtest honest: no feature here can leak the value it is used to
predict.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

# Lags and rolling windows chosen around the weekly and monthly cycles that
# actually exist in payments data.
LAGS = (1, 2, 3, 7, 14, 21, 28)
ROLLS = (3, 7, 14, 28)

CALENDAR_COLS = ["day_of_week", "is_weekend", "is_holiday", "is_salary_window",
                 "is_month_end", "is_quarter_end", "day_of_month",
                 "week_of_month", "month"]


def build_daily_frame(analytics, filters, *, target: str = "attempts",
                      with_calendar: bool = True) -> pd.DataFrame:
    """Daily fact frame for one slice of the corpus, with calendar joined in."""
    rows = analytics.daily_series(filters)
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)

    if with_calendar:
        cal = pd.DataFrame(analytics.calendar(filters))
        if not cal.empty:
            cal["date"] = pd.to_datetime(cal["date"])
            keep = ["date", "is_salary_window", "is_month_end",
                    "is_quarter_end", "spend_multiplier",
                    "settlement_multiplier", "holiday", "festival"]
            cal = cal[[c for c in keep if c in cal.columns]]
            df = df.merge(cal, on="date", how="left", suffixes=("", "_cal"))

    df["day_of_month"] = df["date"].dt.day
    df["week_of_month"] = ((df["date"].dt.day - 1) // 7) + 1
    df["month"] = df["date"].dt.month
    df["day_of_week"] = df["date"].dt.dayofweek
    df["is_weekend"] = df["day_of_week"] >= 5
    for c in ("is_holiday", "is_salary_window", "is_month_end",
              "is_quarter_end"):
        if c not in df.columns:
            df[c] = False
        df[c] = df[c].fillna(False).astype(int)
    df["is_weekend"] = df["is_weekend"].astype(int)
    df["has_festival"] = df.get(
        "festival", pd.Series([None] * len(df))).notna().astype(int)
    df["trend_index"] = np.arange(len(df))
    if target not in df.columns:
        raise ValueError(f"target {target!r} is not in the daily frame")
    return df


def add_supervised_features(df: pd.DataFrame, target: str) -> pd.DataFrame:
    """Lags, rolling statistics and calendar encodings for one target."""
    out = df.copy()
    y = pd.to_numeric(out[target], errors="coerce")
    out[target] = y

    for lag in LAGS:
        out[f"{target}_lag_{lag}"] = y.shift(lag)
    for w in ROLLS:
        # shift(1) first: a rolling mean that includes today would leak it.
        s = y.shift(1)
        out[f"{target}_roll_mean_{w}"] = s.rolling(w, min_periods=2).mean()
        out[f"{target}_roll_std_{w}"] = s.rolling(w, min_periods=2).std()
    out[f"{target}_wow_ratio"] = (
        out[f"{target}_lag_1"] / out[f"{target}_lag_8"]
        if f"{target}_lag_8" in out else
        out[f"{target}_lag_1"] / out[f"{target}_lag_7"].replace(0, np.nan))
    out[f"{target}_momentum_7"] = (
        out[f"{target}_roll_mean_7"] - out[f"{target}_roll_mean_28"])

    # Cyclical encodings beat one-hot for weekday/month on small samples.
    out["dow_sin"] = np.sin(2 * np.pi * out["day_of_week"] / 7)
    out["dow_cos"] = np.cos(2 * np.pi * out["day_of_week"] / 7)
    out["dom_sin"] = np.sin(2 * np.pi * out["day_of_month"] / 30.5)
    out["dom_cos"] = np.cos(2 * np.pi * out["day_of_month"] / 30.5)
    return out


def feature_columns(df: pd.DataFrame, target: str) -> list[str]:
    """Every numeric column that is safe to train on for this target."""
    banned = {target, "date", "attempts", "successful", "failed", "pending",
              "value_inr", "avg_ticket_inr", "median_ticket_inr",
              "active_customers", "active_merchants", "p95_latency_ms",
              "p50_latency_ms", "retries", "success_rate",
              "technical_decline_pct", "business_decline_pct",
              "risk_decline_pct", "timeout_pct", "retry_rate_pct",
              "calendar_event", "holiday", "festival"}
    cols = []
    for c in df.columns:
        if c in banned or c.endswith("_cal"):
            continue
        if pd.api.types.is_numeric_dtype(df[c]) or \
                pd.api.types.is_bool_dtype(df[c]):
            cols.append(c)
    return cols


FEATURE_LABELS = {
    "trend_index": "underlying growth trend",
    "dow_sin": "day-of-week cycle", "dow_cos": "day-of-week cycle",
    "dom_sin": "day-of-month cycle", "dom_cos": "day-of-month cycle",
    "day_of_week": "day of week", "day_of_month": "day of month",
    "week_of_month": "week of month", "month": "month of year",
    "is_weekend": "weekend effect", "is_holiday": "bank holiday",
    "is_salary_window": "salary-credit window",
    "is_month_end": "month-end settlement push",
    "is_quarter_end": "quarter-end settlement push",
    "has_festival": "festival effect",
    "spend_multiplier": "modelled consumer-spend calendar",
    "settlement_multiplier": "bank settlement availability",
}


def humanise(feature: str, target: str) -> str:
    """A feature name a product manager can read."""
    if feature in FEATURE_LABELS:
        return FEATURE_LABELS[feature]
    base = target.replace("_", " ")
    if feature.startswith(f"{target}_lag_"):
        n = feature.rsplit("_", 1)[1]
        return f"{base} {n} day{'s' if n != '1' else ''} ago"
    if "_roll_mean_" in feature:
        n = feature.rsplit("_", 1)[1]
        return f"{n}-day average {base}"
    if "_roll_std_" in feature:
        n = feature.rsplit("_", 1)[1]
        return f"{n}-day volatility of {base}"
    if feature.endswith("_wow_ratio"):
        return f"week-on-week {base} ratio"
    if feature.endswith("_momentum_7"):
        return f"short-vs-long term momentum in {base}"
    return feature.replace("_", " ")

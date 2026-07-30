"""Automated exploratory data analysis.

Runs the pass an analyst would run before touching a model: distribution shape,
trend significance, seasonal strength, stationarity, autocorrelation, breaks in
the level, and cross-metric correlation. Every result is a number with a stated
test behind it, so the narrative layer can say *why* it believes something
rather than asserting a vibe.
"""
from __future__ import annotations

import math

import numpy as np
import pandas as pd
from scipy import stats


def _clean(series: pd.Series) -> np.ndarray:
    return pd.to_numeric(series, errors="coerce").dropna().to_numpy(float)


def distribution(series: pd.Series) -> dict:
    y = _clean(series)
    if len(y) < 3:
        return {"n": int(len(y))}
    q = np.percentile(y, [1, 5, 25, 50, 75, 95, 99])
    iqr = q[4] - q[2]
    outliers = int(((y < q[2] - 1.5 * iqr) | (y > q[4] + 1.5 * iqr)).sum())
    return {
        "n": int(len(y)), "mean": round(float(y.mean()), 4),
        "std": round(float(y.std(ddof=1)), 4),
        "cv_pct": round(float(100 * y.std(ddof=1) / abs(y.mean())), 2)
        if y.mean() else None,
        "min": round(float(y.min()), 4), "max": round(float(y.max()), 4),
        "p1": round(float(q[0]), 4), "p5": round(float(q[1]), 4),
        "p25": round(float(q[2]), 4), "median": round(float(q[3]), 4),
        "p75": round(float(q[4]), 4), "p95": round(float(q[5]), 4),
        "p99": round(float(q[6]), 4),
        "skew": round(float(stats.skew(y)), 4),
        "kurtosis": round(float(stats.kurtosis(y)), 4),
        "iqr_outliers": outliers,
        "outlier_pct": round(100 * outliers / len(y), 2),
    }


def trend(series: pd.Series) -> dict:
    """OLS slope with significance, plus the non-parametric Mann-Kendall test
    (which does not assume linearity — payments series rarely are linear)."""
    y = _clean(series)
    n = len(y)
    if n < 8:
        return {"detected": False, "reason": "not enough history"}
    x = np.arange(n, dtype=float)
    lr = stats.linregress(x, y)
    mk_tau, mk_p = stats.kendalltau(x, y)
    total_change = float(y[-1] - y[0])
    pct = round(100 * total_change / abs(y[0]), 2) if y[0] else None
    # Slope per day expressed as a percentage of the mean level.
    daily_pct = round(100 * lr.slope / abs(y.mean()), 4) if y.mean() else None
    significant = bool(lr.pvalue < 0.05 and mk_p < 0.05)
    if not significant:
        direction = "flat"
    else:
        direction = "increasing" if lr.slope > 0 else "decreasing"
    return {
        "detected": significant, "direction": direction,
        "slope_per_day": round(float(lr.slope), 6),
        "slope_pct_per_day": daily_pct,
        "r_squared": round(float(lr.rvalue ** 2), 4),
        "p_value": round(float(lr.pvalue), 6),
        "mann_kendall_tau": round(float(mk_tau), 4),
        "mann_kendall_p": round(float(mk_p), 6),
        "start_value": round(float(y[0]), 4), "end_value": round(float(y[-1]), 4),
        "total_change": round(total_change, 4), "total_change_pct": pct,
        "annualised_pct": round(pct * 365 / n, 1) if pct is not None else None,
    }


def decompose(series: pd.Series, period: int = 7) -> dict:
    """Additive trend / seasonal / residual split by centred moving average —
    the classic decomposition, done without a statsmodels dependency."""
    y = _clean(series)
    n = len(y)
    if n < period * 3:
        return {"available": False, "reason": "series shorter than 3 cycles"}
    s = pd.Series(y)
    trend_c = s.rolling(period, center=True, min_periods=period).mean()
    if period % 2 == 0:
        trend_c = trend_c.rolling(2, center=True).mean()
    detrended = s - trend_c
    idx = np.arange(n) % period
    seasonal_means = pd.Series(detrended.to_numpy()).groupby(idx).mean()
    seasonal_means -= seasonal_means.mean()
    seasonal = seasonal_means.reindex(idx).to_numpy()
    resid = s.to_numpy() - trend_c.to_numpy() - seasonal

    var_total = float(np.nanvar(y))
    var_resid = float(np.nanvar(resid))
    var_seas = float(np.nanvar(seasonal))
    seasonal_strength = max(0.0, 1 - var_resid / max(1e-9, var_resid + var_seas))
    trend_strength = max(0.0, 1 - var_resid / max(1e-9, var_total))
    return {
        "available": True, "period": period,
        "seasonal_strength": round(float(seasonal_strength), 4),
        "trend_strength": round(float(trend_strength), 4),
        "residual_std": round(float(np.nanstd(resid)), 4),
        "seasonal_pattern": [
            {"position": int(i), "effect": round(float(v), 4)}
            for i, v in enumerate(seasonal_means.to_numpy())],
        "explained_pct": round(
            100 * (1 - var_resid / max(1e-9, var_total)), 2),
    }


def weekly_seasonality(df: pd.DataFrame, target: str) -> dict:
    """Day-of-week effect measured against the series mean, with an ANOVA test
    for whether the weekday differences are real."""
    if "day_of_week" not in df.columns or target not in df.columns:
        return {"detected": False}
    d = df[["day_of_week", target]].dropna()
    if len(d) < 21:
        return {"detected": False, "reason": "not enough history"}
    groups = [g[target].to_numpy(float)
              for _, g in d.groupby("day_of_week") if len(g) >= 2]
    if len(groups) < 3:
        return {"detected": False}
    fstat, pval = stats.f_oneway(*groups)
    overall = float(d[target].mean())
    names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
             "Saturday", "Sunday"]
    effects = []
    for dow, g in d.groupby("day_of_week"):
        m = float(g[target].mean())
        effects.append({
            "day": names[int(dow)] if 0 <= int(dow) < 7 else str(dow),
            "day_index": int(dow), "mean": round(m, 3),
            "vs_overall_pct": round(100 * (m - overall) / overall, 2)
            if overall else None, "observations": int(len(g))})
    effects.sort(key=lambda r: r["day_index"])
    return {"detected": bool(pval < 0.05), "f_statistic": round(float(fstat), 3),
            "p_value": round(float(pval), 6), "overall_mean": round(overall, 3),
            "by_day": effects,
            "peak_day": max(effects, key=lambda r: r["mean"])["day"],
            "trough_day": min(effects, key=lambda r: r["mean"])["day"]}


def autocorrelation(series: pd.Series, max_lag: int = 30) -> list[dict]:
    y = _clean(series)
    n = len(y)
    if n < 10:
        return []
    y = y - y.mean()
    denom = float((y ** 2).sum()) or 1.0
    ci = 1.96 / math.sqrt(n)
    out = []
    for lag in range(1, min(max_lag, n - 2) + 1):
        r = float((y[lag:] * y[:-lag]).sum() / denom)
        out.append({"lag": lag, "acf": round(r, 4),
                    "significant": abs(r) > ci})
    return out


def stationarity(series: pd.Series) -> dict:
    """A light stationarity read: compare the level and variance of the first
    and second halves. Enough to tell the modelling layer whether to difference."""
    y = _clean(series)
    if len(y) < 20:
        return {"stationary": None}
    a, b = y[: len(y) // 2], y[len(y) // 2:]
    t_stat, t_p = stats.ttest_ind(a, b, equal_var=False)
    lev_stat, lev_p = stats.levene(a, b)
    return {
        "stationary": bool(t_p >= 0.05 and lev_p >= 0.05),
        "mean_shift_p": round(float(t_p), 6),
        "variance_shift_p": round(float(lev_p), 6),
        "first_half_mean": round(float(a.mean()), 4),
        "second_half_mean": round(float(b.mean()), 4),
        "level_shift_pct": round(100 * (b.mean() - a.mean()) / abs(a.mean()), 2)
        if a.mean() else None,
    }


def change_points(series: pd.Series, min_segment: int = 10,
                  threshold: float = 3.0) -> list[dict]:
    """Level shifts found by scanning for the split that maximises the
    between-segment t-statistic, recursively. Catches regulatory step changes
    and product launches that a trend line would smooth away."""
    y = _clean(series)
    found: list[dict] = []

    def scan(lo: int, hi: int, depth: int = 0) -> None:
        if depth > 3 or hi - lo < 2 * min_segment:
            return
        best_t, best_i = 0.0, None
        for i in range(lo + min_segment, hi - min_segment):
            a, b = y[lo:i], y[i:hi]
            if len(a) < 3 or len(b) < 3:
                continue
            t, _p = stats.ttest_ind(a, b, equal_var=False)
            if abs(t) > best_t:
                best_t, best_i = abs(t), i
        if best_i is None or best_t < threshold:
            return
        a, b = y[lo:best_i], y[best_i:hi]
        found.append({
            "index": int(best_i), "t_statistic": round(float(best_t), 3),
            "before_mean": round(float(a.mean()), 3),
            "after_mean": round(float(b.mean()), 3),
            "shift_pct": round(100 * (b.mean() - a.mean()) / abs(a.mean()), 2)
            if a.mean() else None,
            "direction": "up" if b.mean() > a.mean() else "down"})
        scan(lo, best_i, depth + 1)
        scan(best_i, hi, depth + 1)

    scan(0, len(y))
    return sorted(found, key=lambda r: r["index"])


def correlations(df: pd.DataFrame, columns: list[str],
                 min_abs: float = 0.30) -> list[dict]:
    """Pairwise Pearson + Spearman with significance, strongest first."""
    cols = [c for c in columns
            if c in df.columns and pd.api.types.is_numeric_dtype(df[c])]
    out = []
    for i, a in enumerate(cols):
        for b in cols[i + 1:]:
            d = df[[a, b]].dropna()
            if len(d) < 10:
                continue
            x, y = d[a].to_numpy(float), d[b].to_numpy(float)
            if x.std() == 0 or y.std() == 0:
                continue
            r, p = stats.pearsonr(x, y)
            rho, _ = stats.spearmanr(x, y)
            if abs(r) < min_abs or p >= 0.05:
                continue
            out.append({"a": a, "b": b, "pearson_r": round(float(r), 4),
                        "spearman_rho": round(float(rho), 4),
                        "p_value": round(float(p), 6), "n": int(len(d)),
                        "strength": ("very strong" if abs(r) > 0.85 else
                                     "strong" if abs(r) > 0.65 else
                                     "moderate"),
                        "direction": "positive" if r > 0 else "negative"})
    out.sort(key=lambda r: abs(r["pearson_r"]), reverse=True)
    return out


def data_quality(df: pd.DataFrame) -> dict:
    """Completeness and continuity of the modelling frame itself."""
    if df.empty:
        return {"rows": 0}
    missing = {c: int(df[c].isna().sum()) for c in df.columns
               if df[c].isna().any()}
    gaps = 0
    if "date" in df.columns and len(df) > 1:
        d = pd.to_datetime(df["date"]).sort_values()
        gaps = int(((d.diff().dt.days.fillna(1)) > 1).sum())
    return {"rows": int(len(df)), "columns": int(len(df.columns)),
            "missing_by_column": missing, "date_gaps": gaps,
            "complete_pct": round(
                100 * (1 - sum(missing.values())
                       / max(1, len(df) * len(df.columns))), 2)}


def run_eda(df: pd.DataFrame, target: str, *,
            extra_metrics: list[str] | None = None) -> dict:
    """The full automated pass for one target."""
    if df.empty or target not in df.columns:
        return {"available": False, "reason": "no data for this slice"}
    s = df[target]
    metrics = extra_metrics or [
        "attempts", "success_rate", "value_inr", "avg_ticket_inr",
        "active_customers", "p95_latency_ms", "technical_decline_pct",
        "business_decline_pct", "retry_rate_pct"]
    metrics = [m for m in metrics if m in df.columns]
    return {
        "available": True,
        "target": target,
        "observations": int(len(df)),
        "period": {"start": str(df["date"].min().date()),
                   "end": str(df["date"].max().date())}
        if "date" in df.columns else {},
        "distribution": distribution(s),
        "trend": trend(s),
        "decomposition": decompose(s, period=7),
        "weekly_seasonality": weekly_seasonality(df, target),
        "autocorrelation": autocorrelation(s, 28),
        "stationarity": stationarity(s),
        "change_points": change_points(s),
        "correlations": correlations(df, metrics),
        "data_quality": data_quality(df),
    }

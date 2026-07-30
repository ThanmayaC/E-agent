"""Anomaly detection — and the honesty of scoring it against ground truth.

The simulator writes an incident ledger (PSP outages, bank degradations, fraud
spikes, latency events). That ledger is never shown to the detector; it is kept
back as an answer key. So when this module reports "precision 0.8", that is a
measured fact about caught-vs-missed real incidents, not a claim.

Two detectors run together: a seasonal-residual robust z-score (catches a day
that breaks its own weekday pattern) and a multivariate IsolationForest (catches
a day that is odd across metrics at once, e.g. latency up *and* success down).
"""
from __future__ import annotations

import numpy as np
import pandas as pd

try:
    from sklearn.ensemble import IsolationForest
    _SKLEARN = True
except ImportError:  # pragma: no cover
    _SKLEARN = False

_MULTI_METRICS = ["attempts", "success_rate", "p95_latency_ms",
                  "technical_decline_pct", "value_inr", "retry_rate_pct"]


def _robust_z(y: np.ndarray) -> np.ndarray:
    med = np.median(y)
    mad = np.median(np.abs(y - med)) or (y.std() or 1.0)
    return (y - med) / (1.4826 * mad)


def seasonal_residual_anomalies(df: pd.DataFrame, target: str,
                                z_threshold: float = 3.0) -> list[dict]:
    """Deviation from the day-of-week seasonal median, robustly scored."""
    if target not in df.columns or "day_of_week" not in df.columns:
        return []
    d = df[["date", "day_of_week", target]].dropna().reset_index(drop=True)
    if len(d) < 21:
        return []
    y = d[target].to_numpy(float)
    dow = d["day_of_week"].to_numpy(int)
    baseline = np.zeros_like(y)
    for k in range(7):
        m = dow == k
        if m.sum() >= 2:
            baseline[m] = np.median(y[m])
    resid = y - baseline
    z = _robust_z(resid)
    out = []
    for i in np.where(np.abs(z) >= z_threshold)[0]:
        out.append({
            "date": str(pd.to_datetime(d.iloc[i]["date"]).date()),
            "metric": target,
            "value": round(float(y[i]), 3),
            "expected": round(float(baseline[i]), 3),
            "deviation_pct": round(100 * (y[i] - baseline[i]) / baseline[i], 2)
            if baseline[i] else None,
            "z_score": round(float(z[i]), 2),
            "direction": "spike" if z[i] > 0 else "drop",
            "severity": ("critical" if abs(z[i]) >= 5 else
                         "high" if abs(z[i]) >= 4 else "moderate"),
            "detector": "seasonal-residual"})
    return sorted(out, key=lambda r: abs(r["z_score"]), reverse=True)


def multivariate_anomalies(df: pd.DataFrame,
                           contamination: float = 0.05) -> list[dict]:
    """Days that are jointly unusual across metrics (IsolationForest)."""
    if not _SKLEARN:
        return []
    cols = [c for c in _MULTI_METRICS if c in df.columns]
    if len(cols) < 3:
        return []
    d = df[["date"] + cols].dropna().reset_index(drop=True)
    if len(d) < 30:
        return []
    X = d[cols].to_numpy(float)
    Xs = (X - X.mean(0)) / (X.std(0) + 1e-9)
    iso = IsolationForest(contamination=contamination, n_estimators=200,
                          random_state=7)
    pred = iso.fit_predict(Xs)
    score = -iso.score_samples(Xs)   # higher = more anomalous
    out = []
    for i in np.where(pred == -1)[0]:
        # Which metric contributed most: largest standardised deviation.
        devs = {c: round(float(Xs[i, j]), 2) for j, c in enumerate(cols)}
        driver = max(devs, key=lambda c: abs(devs[c]))
        out.append({
            "date": str(pd.to_datetime(d.iloc[i]["date"]).date()),
            "anomaly_score": round(float(score[i]), 4),
            "primary_driver": driver,
            "driver_z": devs[driver],
            "metric_deviations": devs,
            "detector": "isolation-forest"})
    return sorted(out, key=lambda r: r["anomaly_score"], reverse=True)


def score_against_incidents(anomalies: list[dict], incidents: list[dict],
                            window_days: int = 1) -> dict:
    """Precision / recall of the detector against the real incident ledger."""
    if not incidents:
        return {"scored": False, "reason": "no incident ledger for this slice"}
    inc_days: set = set()
    spans = []
    for inc in incidents:
        try:
            s = pd.to_datetime(inc.get("start_date"))
            e = pd.to_datetime(inc.get("end_date") or inc.get("start_date"))
        except (ValueError, TypeError):
            continue
        spans.append((s, e, inc))
        for day in pd.date_range(s - pd.Timedelta(days=window_days),
                                 e + pd.Timedelta(days=window_days)):
            inc_days.add(day.date())
    flagged = {pd.to_datetime(a["date"]).date() for a in anomalies}
    true_pos = len(flagged & inc_days)
    false_pos = len(flagged - inc_days)
    precision = true_pos / max(1, true_pos + false_pos)

    caught = 0
    for s, e, _inc in spans:
        span_days = {d.date() for d in pd.date_range(s, e)}
        if span_days & flagged:
            caught += 1
    recall = caught / max(1, len(spans))
    f1 = (2 * precision * recall / (precision + recall)
          if (precision + recall) else 0.0)
    return {
        "scored": True, "incidents_in_ledger": len(spans),
        "incidents_detected": caught,
        "anomalies_flagged": len(flagged),
        "true_positives": true_pos, "false_positives": false_pos,
        "precision": round(precision, 3), "recall": round(recall, 3),
        "f1": round(f1, 3)}


def detect(df: pd.DataFrame, target: str, incidents: list[dict] | None = None,
           *, extra_targets: list[str] | None = None) -> dict:
    """Full anomaly pass for a slice, scored against ground truth if given."""
    if df.empty:
        return {"available": False}
    seasonal = seasonal_residual_anomalies(df, target)
    for t in (extra_targets or []):
        if t != target and t in df.columns:
            seasonal.extend(seasonal_residual_anomalies(df, t))
    multivariate = multivariate_anomalies(df)
    all_dates = {a["date"] for a in seasonal} | {a["date"] for a in multivariate}
    scoring = score_against_incidents(
        [{"date": d} for d in all_dates], incidents or [])
    return {
        "available": True,
        "seasonal_anomalies": seasonal[:25],
        "multivariate_anomalies": multivariate[:15],
        "distinct_anomaly_days": len(all_dates),
        "validation": scoring}

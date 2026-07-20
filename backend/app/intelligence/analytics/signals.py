"""Deterministic signal engine.

Computes objective statistical facts over KPI time series and dimensional
breakdowns: trends, latest-period anomalies, seasonality, concentration,
correlations (including inverse / cannibalization candidates).

This layer NEVER generates narrative, recommendations, or business language.
Every output is numbers + metric references. Interpretation is the exclusive
responsibility of the AI reasoning layer.
"""
from __future__ import annotations

import uuid

import numpy as np

from app.domain.entities import KPI, AnalyticsSignal
from app.domain.enums import SignalKind


def _new_id() -> str:
    return uuid.uuid4().hex[:10]


class SignalEngine:
    def __init__(self, min_strength: float = 0.3):
        self.min_strength = min_strength

    def compute(self, kpis: list[KPI], breakdowns: list[dict]) -> list[AnalyticsSignal]:
        signals: list[AnalyticsSignal] = []
        for kpi in kpis:
            signals.extend(self._series_signals(kpi))
        signals.extend(self._correlation_signals(kpis))
        signals.extend(self._concentration_signals(breakdowns))
        signals = [s for s in signals if s.strength >= self.min_strength]
        signals.sort(key=lambda s: s.strength, reverse=True)
        return signals

    # -------------------------------------------------------- per-series
    def _series_signals(self, kpi: KPI) -> list[AnalyticsSignal]:
        out: list[AnalyticsSignal] = []
        y = np.array(kpi.sparkline, dtype=float)
        if len(y) < 4:
            return out
        x = np.arange(len(y))
        slope, intercept = np.polyfit(x, y, 1)
        mean_abs = float(np.mean(np.abs(y))) or 1.0
        slope_pct = slope / mean_abs * 100

        if abs(slope_pct) >= 1.5:
            out.append(AnalyticsSignal(
                id=_new_id(), kind=SignalKind.TREND,
                kpi_id=kpi.id, kpi_name=kpi.name, dataset_id=kpi.dataset_id,
                stats={
                    "slope_pct_per_period": round(slope_pct, 2),
                    "first_value": round(float(y[0]), 2),
                    "last_value": round(float(y[-1]), 2),
                    "total_change_pct": round((y[-1] - y[0]) / (abs(y[0]) or 1) * 100, 2),
                    "periods": len(y),
                    "direction": 1 if slope_pct > 0 else -1,
                },
                strength=round(min(0.95, 0.5 + abs(slope_pct) / 20), 2),
            ))

        recent = y[:-1][-6:]
        if len(recent) >= 3 and recent.std() > 0:
            z = float((y[-1] - recent.mean()) / recent.std())
            if abs(z) >= 2.0:
                out.append(AnalyticsSignal(
                    id=_new_id(), kind=SignalKind.ANOMALY,
                    kpi_id=kpi.id, kpi_name=kpi.name, dataset_id=kpi.dataset_id,
                    stats={
                        "zscore": round(z, 2),
                        "latest_value": round(float(y[-1]), 2),
                        "baseline_mean": round(float(recent.mean()), 2),
                        "baseline_std": round(float(recent.std()), 2),
                        "baseline_periods": len(recent),
                    },
                    strength=round(min(0.95, 0.55 + abs(z) / 10), 2),
                ))

        if len(y) >= 24:
            detrended = y - (intercept + slope * x)
            monthly = [detrended[i::12] for i in range(12)]
            denom = float(np.std(detrended)) or 1.0
            season_strength = float(np.std([m.mean() for m in monthly if len(m)])) / denom
            if season_strength > 0.5:
                peak_month = int(np.argmax([m.mean() if len(m) else -1e18 for m in monthly]))
                trough_month = int(np.argmin([m.mean() if len(m) else 1e18 for m in monthly]))
                out.append(AnalyticsSignal(
                    id=_new_id(), kind=SignalKind.SEASONALITY,
                    kpi_id=kpi.id, kpi_name=kpi.name, dataset_id=kpi.dataset_id,
                    stats={
                        "season_strength": round(season_strength, 2),
                        "peak_month": peak_month + 1,
                        "trough_month": trough_month + 1,
                        "period_length": 12,
                    },
                    strength=round(min(0.9, 0.4 + season_strength / 3), 2),
                ))
        return out

    # ------------------------------------------------------- correlations
    def _correlation_signals(self, kpis: list[KPI]) -> list[AnalyticsSignal]:
        out: list[AnalyticsSignal] = []
        with_ts = [k for k in kpis if len(k.sparkline) >= 6]
        for i, a in enumerate(with_ts):
            for b in with_ts[i + 1:]:
                if a.dataset_id == b.dataset_id and a.column and a.column == b.column:
                    continue  # same underlying series, comparison is meaningless
                n = min(len(a.sparkline), len(b.sparkline))
                ya, yb = np.array(a.sparkline[-n:]), np.array(b.sparkline[-n:])
                if ya.std() == 0 or yb.std() == 0:
                    continue
                r = float(np.corrcoef(ya, yb)[0, 1])
                if np.isnan(r) or abs(r) < 0.75:
                    continue
                out.append(AnalyticsSignal(
                    id=_new_id(),
                    kind=SignalKind.INVERSE_CORRELATION if r < 0 else SignalKind.CORRELATION,
                    kpi_id=a.id, kpi_name=a.name,
                    stats={
                        "correlation": round(r, 3),
                        "kpi_a": a.name, "kpi_a_id": a.id,
                        "kpi_b": b.name, "kpi_b_id": b.id,
                        "periods_compared": n,
                    },
                    strength=round(min(0.9, abs(r) * 0.85), 2),
                ))
        return out[:10]

    # ------------------------------------------------------ concentration
    def _concentration_signals(self, breakdowns: list[dict]) -> list[AnalyticsSignal]:
        out: list[AnalyticsSignal] = []
        for chart in breakdowns:
            totals = [row[1] for row in chart.get("rows", []) if row[1] is not None]
            if len(totals) < 3:
                continue
            values = np.sort(np.array(totals, dtype=float))[::-1]
            total = float(values.sum())
            if total <= 0:
                continue
            top_n = max(1, len(values) // 5)
            top_share = float(values[:top_n].sum() / total)
            if top_share >= 0.6:
                out.append(AnalyticsSignal(
                    id=_new_id(), kind=SignalKind.CONCENTRATION,
                    stats={
                        "measure": chart["measure"],
                        "dimension": chart["dimension"],
                        "dataset": chart["dataset"],
                        "top20pct_share": round(top_share, 3),
                        "leader_value": str(chart["rows"][0][0]),
                        "leader_total": round(float(chart["rows"][0][1] or 0), 2),
                        "categories": len(values),
                    },
                    strength=round(min(0.9, top_share), 2),
                ))
        return out

"""Predictive analytics: trend + seasonal-naive blended forecasts with intervals.

Forecasting never runs blindly. Every series passes deterministic validation
gates before a forecast is trusted:

  - history < MIN_HISTORY periods       -> at best "low_confidence"
  - insufficient variance (CV < 1%)     -> "unavailable" (nothing to model)
  - no detectable trend or seasonality  -> at best "low_confidence"
  - confidence < LOW_CONFIDENCE         -> "low_confidence"

"unavailable" forecasts carry no point values, so nothing misleading can be
displayed or reasoned over; "low_confidence" forecasts carry values plus the
machine-readable reasons that limit trust.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from app.domain.entities import KPI, Forecast

MIN_HISTORY = 12          # periods of history a trustworthy forecast requires
MIN_VARIATION = 0.01      # coefficient of variation below this = flat series
LOW_CONFIDENCE = 0.6      # statistical confidence below this is flagged


class ForecastEngine:
    def forecast_all(self, kpis: list[KPI]) -> list[Forecast]:
        forecasts: list[Forecast] = []
        for kpi in kpis:
            if len(kpi.sparkline) < 4:
                continue
            fc = self.forecast(kpi, horizon=6)
            forecasts.append(fc)
            # only validated forecasts enrich the KPI — never misleading numbers
            kpi.forecast_next = fc.values[0] if fc.values else None
            kpi.forecast_confidence = fc.confidence if fc.status != "unavailable" else None
        return forecasts

    def forecast(self, kpi: KPI, horizon: int = 6) -> Forecast:
        y = np.array(kpi.sparkline, dtype=float)
        n = len(y)
        x = np.arange(n, dtype=float)

        # ---- gate 1: insufficient variance — a flat series has no signal to
        # model, so no forecast is produced at all
        mean_abs = float(np.mean(np.abs(y))) or 1.0
        if float(np.std(y)) / mean_abs < MIN_VARIATION:
            return Forecast(
                kpi_id=kpi.id, kpi_name=kpi.name, horizon="next_period",
                periods=[], values=[], lower=[], upper=[],
                method="none", confidence=0.0, status="unavailable",
                validation=[f"insufficient_variance: series varies less than "
                            f"{MIN_VARIATION:.0%} around its mean"])

        # linear trend
        slope, intercept = np.polyfit(x, y, 1)
        trend = intercept + slope * np.arange(n, n + horizon)

        # seasonal component (period 12 if enough data, else 4)
        period = 12 if n >= 24 else (4 if n >= 8 else 0)
        seasonal = np.zeros(horizon)
        if period:
            detrended = y - (intercept + slope * x)
            season_means = np.array([
                detrended[i::period].mean() if len(detrended[i::period]) else 0.0
                for i in range(period)
            ])
            seasonal = np.array([season_means[(n + h) % period] for h in range(horizon)])

        point = trend + seasonal

        # residual spread drives the interval and confidence
        fitted = intercept + slope * x
        if period:
            fitted = fitted + np.array([
                (y - (intercept + slope * x))[i % period::period].mean() if n > period else 0.0
                for i in range(n)
            ])
        resid_std = float(np.std(y - fitted)) or (abs(float(np.mean(y))) * 0.05 + 1e-9)
        widen = np.sqrt(np.arange(1, horizon + 1))
        lower = point - 1.28 * resid_std * widen
        upper = point + 1.28 * resid_std * widen

        noise_ratio = resid_std / mean_abs
        confidence = round(float(np.clip(0.95 - noise_ratio * 1.5 - (6 / max(n, 6)) * 0.2, 0.2, 0.95)), 2)

        # ---- validation gates 2-4: collect deterministic reasons that limit
        # trust; any reason caps the status at "low_confidence"
        reasons: list[str] = []
        if n < MIN_HISTORY:
            reasons.append(f"history_below_minimum: {n} periods observed, "
                           f"{MIN_HISTORY} required for a trustworthy forecast")
        # trend is detectable when its total movement clears the noise floor
        trend_detectable = abs(slope) * n > resid_std
        season_detectable = period > 0 and float(np.std(seasonal)) > 0.1 * resid_std
        if not trend_detectable and not season_detectable:
            reasons.append("no_detectable_trend: signal does not exceed noise")
        if confidence < LOW_CONFIDENCE:
            reasons.append(f"low_statistical_confidence: {confidence:.2f} "
                           f"(threshold {LOW_CONFIDENCE})")
        if reasons:
            confidence = min(confidence, LOW_CONFIDENCE - 0.01)

        periods = self._future_labels(kpi.sparkline_labels, horizon)
        return Forecast(
            kpi_id=kpi.id, kpi_name=kpi.name, horizon="next_period",
            periods=periods,
            values=[round(float(v), 2) for v in point],
            lower=[round(float(v), 2) for v in lower],
            upper=[round(float(v), 2) for v in upper],
            method=f"linear trend + seasonal({period})" if period else "linear trend",
            confidence=round(confidence, 2),
            status="low_confidence" if reasons else "ok",
            validation=reasons,
        )

    @staticmethod
    def _future_labels(labels: list[str], horizon: int) -> list[str]:
        if len(labels) >= 2:
            try:
                last = pd.Timestamp(labels[-1])
                delta = pd.Timestamp(labels[-1]) - pd.Timestamp(labels[-2])
                if 27 <= delta.days <= 32:
                    idx = pd.date_range(last, periods=horizon + 1, freq="MS")[1:]
                else:
                    idx = pd.date_range(last + delta, periods=horizon, freq=delta)
                return [d.strftime("%Y-%m-%d") for d in idx]
            except Exception:
                pass
        return [f"t+{i + 1}" for i in range(horizon)]

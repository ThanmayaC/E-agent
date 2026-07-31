"""The ML pipeline — one call, the whole analyst's day.

    raw transactions
        → EDA (trend, seasonality, correlation, change points, stationarity)
        → feature engineering (leak-free daily frame)
        → training (gradient boosting / ridge)
        → validation (walk-forward backtest vs seasonal-naive)
        → forecasting (recursive, with prediction intervals)
        → reason generation, confidence, recommendations

Every field the platform ever shows for a prediction is produced here, together,
from the same slice — so the number, the confidence and the story can never drift
apart. Results are memoised on the corpus signature and the slice, because the
whole run is deterministic given the data.
"""
from __future__ import annotations

import time

from app.core.logging import get_logger
from app.warehouse.analytics import KPI_META, TransactionAnalytics
from app.warehouse.filters import Filters
from app.warehouse.ml import anomaly, eda as eda_mod, insight
from app.warehouse.ml.forecast import Forecaster

logger = get_logger(__name__)

FORECASTABLE = ("attempts", "successful", "value_inr", "success_rate",
                "active_customers", "avg_ticket_inr", "technical_decline_pct",
                "retry_rate_pct", "p95_latency_ms")


class MLPipeline:
    """Stateless orchestration over the analytics + ML modules."""

    def __init__(self, analytics: TransactionAnalytics):
        self.a = analytics
        self._cache: dict[tuple, tuple[float, dict]] = {}

    @property
    def available(self) -> bool:
        return self.a.available

    def _sig(self):
        return self.a.wh.signature()

    # ------------------------------------------------------------ full run
    def run(self, filters: Filters, *, target: str = "attempts",
            horizon: int = 14, include_anomaly: bool = True,
            cache: bool = True) -> dict:
        if target not in FORECASTABLE:
            target = "attempts"
        key = (self._sig(), target, horizon, include_anomaly,
               filters.cache_key() if hasattr(filters, "cache_key")
               else str(filters))
        if cache and key in self._cache and self._cache[key][0] == self._sig():
            return self._cache[key][1]

        t0 = time.perf_counter()
        fc = Forecaster(target, horizon=horizon)
        frame = fc.prepare(self.a, filters)
        if frame.empty or len(frame) < 20:
            return {"available": False, "target": target,
                    "reason": "insufficient history for this slice"}

        eda = eda_mod.run_eda(frame, target)
        bt = fc.backtest(frame)
        forecast = fc.forecast(frame, bt)
        importances = fc.importances(frame)
        anomalies = None
        if include_anomaly:
            incidents = self.a.incidents(self.a.resolve(filters))
            anomalies = anomaly.detect(
                frame, target, incidents,
                extra_targets=["success_rate", "p95_latency_ms"])

        conf = insight.confidence(bt, eda, len(frame))
        meta = KPI_META.get(target, {})
        # What the anomalous days did to the level the forecast starts from.
        anom_effect = insight.anomaly_impact(
            frame["date"].astype(str).tolist() if "date" in frame else None,
            frame[target].tolist() if target in frame else None, anomalies)
        result = {
            "available": True,
            "target": target,
            "target_label": meta.get("label", target),
            "unit": meta.get("unit"),
            "slice": filters.describe() if hasattr(filters, "describe") else {},
            "window": eda.get("period", {}),
            "observations": len(frame),
            "eda": eda,
            "backtest": _bt_dict(bt),
            "forecast": forecast,
            "confidence": conf,
            "most_influential_features": importances,
            "supporting_factors": insight.supporting_factors(
                eda, importances, target, anom_effect),
            "anomaly_impact": anom_effect,
            "business_reason": insight.business_reason(
                eda, forecast, bt, target, meta),
            "potential_risks": insight.potential_risks(
                eda, bt, anomalies, target),
            "suggested_actions": insight.suggested_actions(
                eda, forecast, target, conf["band"]),
            "anomalies": anomalies,
            "model": "HistGradientBoosting" if len(frame) >= 90 else "Ridge",
            "runtime_ms": round((time.perf_counter() - t0) * 1000, 1),
        }
        if cache:
            if len(self._cache) > 128:
                self._cache.pop(next(iter(self._cache)))
            self._cache[key] = (self._sig(), result)
        return result

    # -------------------------------------------------------- lightweight
    def forecast_only(self, filters: Filters, *, target: str = "attempts",
                      horizon: int = 14) -> dict:
        """Just the projection + confidence — for compact dashboard cards."""
        full = self.run(filters, target=target, horizon=horizon,
                        include_anomaly=False)
        if not full.get("available"):
            return full
        return {"available": True, "target": target,
                "target_label": full["target_label"], "unit": full["unit"],
                "forecast": full["forecast"], "confidence": full["confidence"],
                "business_reason": full["business_reason"],
                "backtest": full["backtest"]}

    def anomaly_scan(self, filters: Filters, *,
                     target: str = "success_rate") -> dict:
        """Anomaly detection for a slice, scored against the incident ledger."""
        fc = Forecaster(target)
        frame = fc.prepare(self.a, filters)
        if frame.empty:
            return {"available": False}
        incidents = self.a.incidents(self.a.resolve(filters))
        return anomaly.detect(frame, target, incidents,
                              extra_targets=["attempts", "p95_latency_ms",
                                             "technical_decline_pct"])

    def eda_only(self, filters: Filters, *, target: str = "attempts") -> dict:
        fc = Forecaster(target)
        frame = fc.prepare(self.a, filters)
        if frame.empty:
            return {"available": False}
        return eda_mod.run_eda(frame, target)

    def cache_stats(self) -> dict:
        return {"entries": len(self._cache),
                "targets": sorted({k[1] for k in self._cache})}


def _bt_dict(bt) -> dict | None:
    if bt is None:
        return None
    return {"folds": bt.folds, "mape": bt.mape, "smape": bt.smape,
            "rmse": bt.rmse, "mae": bt.mae, "r2": bt.r2,
            "naive_mape": bt.naive_mape, "skill_vs_naive": bt.skill_vs_naive,
            "residual_std": bt.residual_std, "coverage_80": bt.coverage_80,
            "recent_predictions": bt.predictions}

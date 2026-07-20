"""Model Selection Framework (03-ml-platform.md §5) — never hardcoded.

A three-stage funnel over each discovered KPI series:

    meta-features (deterministic)
        → eligibility gates (hard, statistical — a 40-row sheet can never
          spawn a transformer)
        → priors order the eligible candidates (they never decide)
        → rolling-origin champion/challenger vs the deterministic baseline

A candidate is admitted only if it beats the baseline by the configured
margin in one-step-ahead backtests; ties go to the simpler model. Failing
every non-baseline gate is a NORMAL outcome — the deterministic engine
already serves the answer, and the full selection trace records why.

Numpy-only candidates keep the lite profile dependency-free. Heavier
families (GBM, LSTM, TFT) keep their gates in the trace: they are recorded
as ineligible until a dataset actually clears them.
"""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field

import numpy as np

from app.core.logging import get_logger

logger = get_logger(__name__)

MIN_STEPS = 8          # below this no candidate family is evaluated at all
MIN_BACKTEST_POINTS = 3


@dataclass
class SelectionOutcome:
    kpi_id: str
    model_name: str | None = None   # None = no model admitted (normal outcome)
    family: str = ""
    metrics: dict = field(default_factory=dict)
    predictions: list[dict] = field(default_factory=list)
    trace: dict = field(default_factory=dict)


# ------------------------------------------------------------- meta-features
def meta_features(series: np.ndarray) -> dict:
    n = len(series)
    feats: dict = {"n_steps": n}
    if n < 3:
        return feats
    mean = float(np.mean(series))
    feats["mean"] = round(mean, 6)
    feats["cv"] = round(float(np.std(series) / abs(mean)), 4) if mean else None
    feats["intermittency"] = round(float(np.mean(series == 0)), 4)
    # trend strength: R² of a linear fit
    x = np.arange(n, dtype=float)
    slope, intercept = np.polyfit(x, series, 1)
    fitted = slope * x + intercept
    ss_res = float(np.sum((series - fitted) ** 2))
    ss_tot = float(np.sum((series - np.mean(series)) ** 2))
    feats["trend_strength"] = round(1 - ss_res / ss_tot, 4) if ss_tot > 0 else 0.0
    # seasonality: strongest autocorrelation of the detrended series at
    # candidate periods (deterministic STL stand-in). Residuals that are
    # negligible next to the series scale are numerical noise, not season —
    # a perfectly linear series must never test "seasonal".
    detrended = series - fitted
    best_period, best_acf = 0, 0.0
    significant = float(np.std(detrended)) > max(1e-9, 0.01 * float(np.std(series)))
    for period in (4, 7, 12) if significant else ():
        if n >= 2 * period + 2:
            a, b = detrended[:-period], detrended[period:]
            if np.std(a) > 0 and np.std(b) > 0:
                acf = float(np.corrcoef(a, b)[0, 1])
                if acf > best_acf:
                    best_period, best_acf = period, acf
    feats["seasonality_period"] = best_period
    feats["seasonality_strength"] = round(max(best_acf, 0.0), 4)
    return feats


# ------------------------------------------------------- forecast candidates
# Each candidate: fit(train) -> predict-next callable. All deterministic.
def _naive(train: np.ndarray) -> float:
    return float(train[-1])


def _drift(train: np.ndarray) -> float:
    if len(train) < 2:
        return float(train[-1])
    return float(train[-1] + (train[-1] - train[0]) / (len(train) - 1))


def _seasonal_naive(period: int) -> Callable[[np.ndarray], float]:
    def predict(train: np.ndarray) -> float:
        return float(train[-period]) if len(train) >= period else float(train[-1])
    return predict


def _linear_trend(train: np.ndarray) -> float:
    x = np.arange(len(train), dtype=float)
    slope, intercept = np.polyfit(x, train, 1)
    return float(slope * len(train) + intercept)


def _holt(train: np.ndarray, alpha: float = 0.5, beta: float = 0.3) -> float:
    level, trend = float(train[0]), float(train[1] - train[0]) if len(train) > 1 else 0.0
    for v in train[1:]:
        prev = level
        level = alpha * float(v) + (1 - alpha) * (level + trend)
        trend = beta * (level - prev) + (1 - beta) * trend
    return level + trend


def _seasonal_linear(period: int) -> Callable[[np.ndarray], float]:
    """Linear trend + additive seasonal index estimated from detrended means."""
    def predict(train: np.ndarray) -> float:
        n = len(train)
        x = np.arange(n, dtype=float)
        slope, intercept = np.polyfit(x, train, 1)
        detrended = train - (slope * x + intercept)
        idx = [float(np.mean(detrended[i::period])) for i in range(period)]
        return float(slope * n + intercept + idx[n % period])
    return predict


def _explain_linear(series: np.ndarray) -> dict:
    x = np.arange(len(series), dtype=float)
    slope, intercept = np.polyfit(x, series, 1)
    return {"method": "ordinary least squares on time index",
            "slope_per_period": round(float(slope), 6),
            "intercept": round(float(intercept), 6)}


def _explain_holt(series: np.ndarray) -> dict:
    return {"method": "Holt double exponential smoothing",
            "alpha": 0.5, "beta": 0.3,
            "last_level_window": [round(float(v), 4) for v in series[-4:]]}


def _explain_seasonal(series: np.ndarray, period: int) -> dict:
    e = _explain_linear(series)
    e["method"] = "linear trend + additive seasonal indices"
    e["seasonal_period"] = period
    return e


# ---------------------------------------------------------------- evaluation
def _backtest(series: np.ndarray, predict: Callable[[np.ndarray], float],
              test_points: int) -> float:
    """Rolling-origin one-step-ahead MAE (03-ml-platform §5.3)."""
    errors = []
    for i in range(len(series) - test_points, len(series)):
        train = series[:i]
        if len(train) < 2:
            continue
        errors.append(abs(predict(train) - float(series[i])))
    return float(np.mean(errors)) if errors else float("inf")


class ModelSelectionFramework:
    """gates → priors → champion/challenger. One instance per run."""

    def __init__(self, beat_margin: float = 0.05):
        self.beat_margin = float(beat_margin)

    def run_for_kpi(self, kpi) -> SelectionOutcome:
        series = np.asarray([float(v) for v in (kpi.sparkline or [])
                             if v is not None], dtype=float)
        outcome = SelectionOutcome(kpi_id=kpi.id)
        feats = meta_features(series)
        trace: dict = {"kpi_id": kpi.id, "kpi_name": kpi.name,
                       "meta_features": feats, "gates": {}, "candidates": [],
                       "verdict": "no_model_admitted", "reason": ""}
        outcome.trace = trace

        n = len(series)
        if n < MIN_STEPS:
            trace["reason"] = (f"series too short ({n} steps < {MIN_STEPS}) — "
                               "deterministic engine already serves the answer")
            return outcome

        period = int(feats.get("seasonality_period") or 0)
        seasonal = (feats.get("seasonality_strength") or 0) >= 0.30 and period > 0

        # ---- eligibility gates (hard, statistical — recorded even when shut)
        gates = trace["gates"]
        gates["linear/ets"] = "eligible (baseline family)"
        gates["seasonal_linear"] = ("eligible" if seasonal and n >= 2 * period + 4
                                    else "gated: no stable seasonality detected")
        gates["gbm"] = ("eligible" if n >= 1000
                        else f"gated: {n} rows < 1000 (xgboost/lightgbm floor)")
        gates["lstm/deepar"] = (f"gated: {n} steps — needs ≥500 single-series "
                                "steps or ≥50×20 multi-entity")
        gates["tft"] = "gated: needs ≥100 steps, multi-series, exogenous covariates"

        # ---- deterministic baseline: what the platform already answers with
        test_points = max(MIN_BACKTEST_POINTS, n // 5)
        baseline_pred = _seasonal_naive(period) if seasonal else _drift
        baseline_name = "seasonal_naive" if seasonal else "drift"
        baseline_mae = _backtest(series, baseline_pred, test_points)
        naive_mae = _backtest(series, _naive, test_points)  # MASE denominator
        trace["baseline"] = {"name": baseline_name,
                             "mae": round(baseline_mae, 6),
                             "naive_mae": round(naive_mae, 6),
                             "backtest_points": test_points}

        # ---- candidates, in prior order (priors order the search, never decide)
        candidates: list[tuple[str, str, Callable, Callable]] = [
            ("linear_trend", "linear", _linear_trend,
             lambda: _explain_linear(series)),
            ("holt_smoothing", "ets", _holt, lambda: _explain_holt(series)),
        ]
        if seasonal and n >= 2 * period + 4:
            candidates.append(("seasonal_linear", "linear",
                               _seasonal_linear(period),
                               lambda: _explain_seasonal(series, period)))

        best: tuple[str, str, Callable, Callable, float] | None = None
        for name, family, predict, explain in candidates:
            try:
                mae = _backtest(series, predict, test_points)
            except Exception as exc:  # a failing candidate is a trace entry, not a crash
                trace["candidates"].append({"name": name, "error": str(exc)[:200]})
                continue
            beats = (baseline_mae > 0
                     and mae < baseline_mae * (1 - self.beat_margin))
            trace["candidates"].append({
                "name": name, "family": family, "mae": round(mae, 6),
                "baseline_mae": round(baseline_mae, 6),
                "beats_baseline": bool(beats)})
            # champion/challenger: ties go to the simpler (earlier-prior) model
            if beats and (best is None or mae < best[4]):
                best = (name, family, predict, explain, mae)

        if best is None:
            trace["reason"] = (f"no candidate beat the deterministic baseline "
                               f"'{baseline_name}' by ≥{self.beat_margin:.0%} — "
                               "baseline retained (the gate working is the feature)")
            return outcome

        name, family, predict, explain, mae = best
        trace["verdict"] = "model_admitted"
        trace["reason"] = (f"{name} beat {baseline_name} by "
                           f"{(1 - mae / baseline_mae):.1%} on {test_points} "
                           "rolling-origin backtest points")
        value = predict(series)
        # 80% interval from backtest residual scale (evidence consumers —
        # forecast gates — require intervals, 03-ml-platform §5.3)
        spread = 1.28 * mae
        mase = round(mae / naive_mae, 4) if naive_mae > 0 else None
        outcome.model_name = name
        outcome.family = family
        outcome.metrics = {"mae": round(mae, 6),
                           "baseline_mae": round(baseline_mae, 6),
                           "mase": mase,
                           "improvement": round(1 - mae / baseline_mae, 4)}
        outcome.predictions = [{
            "id": f"ml:{kpi.id}:next_period",
            "kpi_id": kpi.id, "kpi_name": kpi.name, "task": "kpi_forecast",
            "horizon": "next_period", "unit": kpi.unit,
            "value": round(float(value), 6),
            "lower": round(float(value - spread), 6),
            "upper": round(float(value + spread), 6),
            "explanation": explain(),
            "backtest": dict(outcome.metrics),
        }]
        return outcome

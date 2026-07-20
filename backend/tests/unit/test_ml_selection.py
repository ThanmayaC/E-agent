"""Model Selection Framework contract (03-ml-platform.md §5).

The gate working IS the feature: a model exists only when rolling-origin
champion/challenger proves lift over the deterministic baseline, and "no
model admitted" is a normal, fully-traced outcome.
"""
from __future__ import annotations

import numpy as np
import pytest

from app.domain.entities import KPI
from app.evidence.ledger import EvidenceLedger
from app.ml.selection import MIN_STEPS, ModelSelectionFramework


def _kpi(values, kpi_id="k1", name="Revenue") -> KPI:
    return KPI(id=kpi_id, name=name, dataset_id="d1",
               expression="SUM(revenue)", unit="₹", sparkline=list(values))


@pytest.fixture()
def framework() -> ModelSelectionFramework:
    return ModelSelectionFramework(beat_margin=0.05)


def test_short_series_admits_nothing(framework):
    out = framework.run_for_kpi(_kpi([1, 2, 3]))
    assert out.model_name is None
    assert out.predictions == []
    assert "too short" in out.trace["reason"]
    assert out.trace["meta_features"]["n_steps"] == 3 < MIN_STEPS


def test_perfect_trend_keeps_deterministic_baseline(framework):
    """Drift is exact on a noiseless linear series — no challenger can beat
    it, so no model is admitted. FP noise must never fake seasonality."""
    out = framework.run_for_kpi(_kpi([100 + 5 * i for i in range(24)]))
    assert out.model_name is None
    assert out.trace["verdict"] == "no_model_admitted"
    assert out.trace["baseline"]["name"] == "drift"
    assert out.trace["baseline"]["mae"] == 0.0
    assert out.trace["meta_features"]["seasonality_period"] == 0


def test_heavy_gates_stay_shut_on_small_series(framework):
    out = framework.run_for_kpi(_kpi([100 + 5 * i for i in range(24)]))
    gates = out.trace["gates"]
    assert gates["gbm"].startswith("gated")          # < 1000 rows
    assert gates["lstm/deepar"].startswith("gated")  # transformer floor
    assert gates["tft"].startswith("gated")
    assert "eligible" in gates["linear/ets"]


def test_noisy_trend_admits_challenger_with_explanation(framework):
    rng = np.random.default_rng(0)
    out = framework.run_for_kpi(
        _kpi([100 + 5 * i + rng.normal(0, 12) for i in range(36)]))
    assert out.model_name is not None
    assert out.trace["verdict"] == "model_admitted"
    assert out.metrics["improvement"] >= 0.05  # beat margin enforced
    (pred,) = out.predictions
    # the ML anti-hallucination rule: citable id, interval, explanation, backtest
    assert pred["id"] == "ml:k1:next_period"
    assert pred["lower"] < pred["value"] < pred["upper"]
    assert pred["explanation"]["method"]
    assert pred["backtest"]["baseline_mae"] > pred["backtest"]["mae"]


def test_seasonal_series_selects_seasonal_family(framework):
    rng = np.random.default_rng(7)
    values = [100 + 3 * i + 25 * np.sin(2 * np.pi * i / 12) + rng.normal(0, 1)
              for i in range(48)]
    out = framework.run_for_kpi(_kpi(values, kpi_id="k3"))
    assert out.trace["meta_features"]["seasonality_period"] == 12
    assert out.model_name == "seasonal_linear"
    assert out.trace["baseline"]["name"] == "seasonal_naive"


def test_flat_series_admits_nothing(framework):
    out = framework.run_for_kpi(_kpi([100.0] * 24))
    assert out.model_name is None
    # every candidate evaluated and recorded — auditable AutoML, not a black box
    assert all("mae" in c or "error" in c for c in out.trace["candidates"])


def test_model_registry_versions_and_purge(tmp_path):
    ledger = EvidenceLedger(f"sqlite:///{(tmp_path / 'control.db').as_posix()}")
    v1 = ledger.register_model("p1", "r1", name="linear_trend", family="linear",
                               task="kpi_forecast", metrics={"mae": 1.0},
                               selection_trace={"verdict": "model_admitted"})
    v2 = ledger.register_model("p1", "r2", name="linear_trend", family="linear",
                               task="kpi_forecast", metrics={"mae": 0.9},
                               selection_trace={"verdict": "model_admitted"})
    assert (v1, v2) == (1, 2)  # versions are per (project, name)
    models = ledger.models("p1")
    assert len(models) == 2 and models[0]["version"] == 2
    assert models[0]["stage"] == "run_scoped"  # promotion needs human approval
    ledger.purge_project("p1")
    assert ledger.models("p1") == []

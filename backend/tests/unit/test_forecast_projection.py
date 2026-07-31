"""Forecasts must be learned from history, and honest about their limits.

`forecasts.csv` is read by ~38 modules — the forecasting engine, the copilot and
its planner, report generation, product growth and scenarios, the Enterprise
Brain, prompt builders, the tool layer. It used to be produced by

    forecast_next = last_7d + (last_7d - prev_7d) / 7

a straight-line extrapolation with no confidence, no validation and no idea
whether the series was forecastable at all. Every downstream "prediction" in the
platform inherited those properties.

These tests hold the replacement to the standard the platform claims: a forecast
carries the model that produced it, an out-of-sample error, its skill against a
naive baseline, and the reason and risk an executive needs — or it says plainly
that it could not be produced.
"""
from __future__ import annotations

import csv
from pathlib import Path

import pytest

from app.warehouse.ml.insight import confidence

DATA = Path(__file__).resolve().parents[3] / "enterprise_data"
CUBES = DATA / "master" / "analytics"
FORECASTS = CUBES / "forecasts.csv"

published = pytest.mark.skipif(
    not FORECASTS.exists(),
    reason="projected forecasts not present in this checkout")


class _BT:
    """Minimal stand-in for a BacktestResult."""

    def __init__(self, mape, skill):
        self.mape = mape
        self.skill_vs_naive = skill
        self.smape = self.rmse = self.mae = self.r2 = None
        self.naive_mape = None
        self.residual_std = self.coverage_80 = None
        self.folds = 30
        self.predictions = []


# ------------------------------------------------------- confidence honesty
def test_a_model_that_loses_to_naive_is_never_high_confidence():
    """A near-flat series scores well on accuracy and regularity and would
    otherwise reach "high" while being beaten by "assume next week looks like
    this one" — and the high-confidence wording asserts it beat that baseline."""
    eda = {"decomposition": {"seasonal_strength": 0.9},
           "distribution": {"cv_pct": 1.0}}
    got = confidence(_BT(mape=0.4, skill=-29.1), eda, n_obs=206)
    assert got["band"] == "moderate"
    assert got["beat_naive_baseline"] is False
    assert "did not beat" in got["interpretation"]


def test_high_confidence_still_available_when_the_model_earns_it():
    eda = {"decomposition": {"seasonal_strength": 0.9},
           "distribution": {"cv_pct": 5.0}}
    got = confidence(_BT(mape=3.8, skill=62.6), eda, n_obs=206)
    assert got["band"] == "high"
    assert got["beat_naive_baseline"] is True
    assert "beat a seasonal-naive baseline" in got["interpretation"]


def test_the_claim_of_beating_the_baseline_is_never_made_falsely():
    """The exact defect: 'high confidence ... and beat a seasonal-naive
    baseline' printed for a model that lost to it."""
    eda = {"decomposition": {"seasonal_strength": 0.95},
           "distribution": {"cv_pct": 0.5}}
    got = confidence(_BT(mape=0.2, skill=-5.0), eda, n_obs=206)
    assert "and beat a seasonal-naive baseline" not in got["interpretation"]


def test_unknown_skill_does_not_assert_either_way():
    got = confidence(_BT(mape=5.0, skill=None), {}, n_obs=100)
    assert got["beat_naive_baseline"] is None


# ----------------------------------------------------- the published cube
@pytest.fixture(scope="module")
def rows():
    with FORECASTS.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


@published
def test_every_series_states_whether_it_could_be_forecast(rows):
    assert rows
    for r in rows:
        assert r["available"] in ("true", "false"), r["series"]


@published
def test_available_forecasts_carry_their_evidence(rows):
    """A number without the model, error and reason behind it is the template
    logic this replaced."""
    live = [r for r in rows if r["available"] == "true"]
    assert live, "no forecast was produced at all"
    for r in live:
        assert r["forecast_next"], f"{r['series']} has no forecast"
        assert r["model"], f"{r['series']} does not name its model"
        assert r["backtest_mape"], f"{r['series']} has no out-of-sample error"
        assert r["confidence_pct"], f"{r['series']} has no confidence"
        assert r["confidence_band"] in ("high", "moderate", "low")
        assert r["business_reason"], f"{r['series']} has no explanation"
        assert r["top_feature"], f"{r['series']} names no driver"


@published
def test_unavailable_forecasts_state_a_reason_and_no_number(rows):
    """The honesty rule: no fabricated value where the model declined."""
    for r in rows:
        if r["available"] == "false":
            assert r["unavailable_reason"], f"{r['series']} declined silently"
            assert not r["forecast_next"], \
                f"{r['series']} is unavailable but still quotes a number"


@published
def test_no_published_forecast_claims_high_confidence_after_losing_to_naive(rows):
    for r in rows:
        if r["available"] != "true" or not r["skill_vs_naive_pct"]:
            continue
        if float(r["skill_vs_naive_pct"]) < 0:
            assert r["confidence_band"] != "high", (
                f"{r['series']} claims high confidence with negative skill")


@published
def test_series_use_warehouse_product_names(rows):
    """The old cube published "UPI Lite X" and "Person to Merchant" — names no
    other part of the platform uses, so a lookup by product name silently
    missed."""
    names = {r["series"] for r in rows}
    assert "feature::UPI Lite Auto Top-Up" in names or \
           any(s.startswith("feature::UPI ") for s in names)
    assert "feature::UPI Lite X" not in names
    assert "feature::Person to Merchant" not in names


# -------------------------------------------------- product lifecycle cube
@published
def test_lifecycle_stage_is_consistent_with_measured_growth():
    """The stage label is a function of the numbers, not a hand-written tag."""
    path = CUBES / "product_lifecycle.csv"
    if not path.exists():
        pytest.skip("product_lifecycle not projected")
    with path.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    assert rows
    for r in rows:
        mom = r["mom_growth_pct"]
        if not mom:
            assert r["lifecycle_stage"] == "New"
            continue
        m = float(mom)
        stage = r["lifecycle_stage"]
        if m >= 25:
            assert stage == "Hypergrowth", f"{r['product']} {r['month']} {m}%"
        elif m <= -8:
            assert stage == "Decline", f"{r['product']} {r['month']} {m}%"
        assert stage in ("New", "Hypergrowth", "Growth", "Decline",
                         "Saturation", "Mature")


@published
def test_monthly_shares_sum_to_a_whole_market():
    path = CUBES / "product_lifecycle.csv"
    if not path.exists():
        pytest.skip("product_lifecycle not projected")
    with path.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    by_month: dict[str, float] = {}
    for r in rows:
        by_month[r["month"]] = by_month.get(r["month"], 0.0) + float(
            r["market_share_pct"])
    assert by_month
    for month, total in by_month.items():
        assert total == pytest.approx(100.0, abs=0.5), f"{month}: {total}"

"""Forecast projection — learned forecasts replace template extrapolation.

Why this module exists
----------------------
``master/analytics/forecasts.csv`` is read by ~38 modules: the forecasting
engine, the copilot and its planner, report generation, product growth and
scenarios, the Enterprise Brain, prompt builders and the tool layer. It was
produced by ``generate_enterprise.py::build_forecasts(trends)``, which is a
straight-line extrapolation of a moving average:

    forecast_next = last_7d + (last_7d - prev_7d) / 7

That is template logic. It cannot be wrong in an interesting way, it carries no
confidence, and it has no idea whether the series it extrapolates is even
forecastable. Every downstream "prediction" in the platform inherited those
properties.

``MLPipeline`` already does the real thing on the raw corpus — walk-forward
backtest against a seasonal-naive baseline, gradient boosting or ridge by
history depth, recursive multi-step forecasting with prediction intervals,
feature importances, change-point and stationarity tests, and a confidence score
decomposed into its components. This module writes that pipeline's output into
the two cubes the platform already reads, so every consumer gets a learned
forecast without changing a line of consumer code.

Honesty rule
------------
A series the pipeline declines to model (too little history, empty slice) is
written with empty forecast fields and a stated reason, never with a fabricated
number. "We cannot forecast this yet" is a correct answer; a confident straight
line through six data points is not.
"""
from __future__ import annotations

import csv
from pathlib import Path

from app.core.logging import get_logger
from app.warehouse.filters import Filters
from app.warehouse.projection import NATIONAL_SCALE_M_PER_TXN

logger = get_logger(__name__)

# The four platform-wide series, mapped to the warehouse target that answers
# them. Names are kept exactly as the existing cube publishes them so the ~38
# consumers keep resolving the rows they already look up.
TOTAL_SERIES: tuple[tuple[str, str], ...] = (
    ("total::sample_txns", "attempts"),
    ("total::sample_value_inr", "value_inr"),
    ("total::success_rate", "success_rate"),
    ("total::avg_ticket_inr", "avg_ticket_inr"),
)

# Forward-projection KPIs the corpus can answer, and the target + scale that
# produce them. KPIs owned by other subsystems (complaints, fraud alerts,
# adoption counts, risk score) are deliberately absent — their existing rows are
# preserved untouched rather than invented from payment data.
FORWARD_KPIS: tuple[tuple[str, str, float], ...] = (
    ("UPI Transactions (M/day)", "attempts", NATIONAL_SCALE_M_PER_TXN),
    ("Success Rate (%)", "success_rate", 1.0),
    ("Technical Declines (%)", "technical_decline_pct", 1.0),
    ("Response Time (ms)", "p95_latency_ms", 1.0),
)

FORECAST_HEADER = [
    # The original contract, unchanged.
    "series", "today", "forecast_next", "forecast_7d", "ma_7d", "growth_pct",
    # Appended: what a forecast must carry to be actionable. Consumers read
    # these cubes with csv.DictReader, so extra trailing columns are additive.
    "model", "confidence_pct", "confidence_band", "backtest_mape",
    "skill_vs_naive_pct", "observations", "top_feature", "top_feature_pct",
    "business_reason", "primary_risk", "recommended_action", "available",
    "unavailable_reason",
]

FORWARD_HEADER = ["kpi", "horizon_day", "date", "forecast", "lower", "upper",
                  "confidence_pct"]


def _pct(v) -> float | None:
    try:
        return round(float(v), 2)
    except (TypeError, ValueError):
        return None


class ForecastProjection:
    """Writes ``forecasts.csv`` and ``forecast_forward.csv`` from MLPipeline."""

    def __init__(self, pipeline, analytics, out_dir: str | Path,
                 *, horizon: int = 14):
        self.ml = pipeline
        self.a = analytics
        self.out = Path(out_dir)
        self.horizon = horizon

    # ------------------------------------------------------------- helpers
    def _run(self, target: str, filters: Filters) -> dict:
        try:
            return self.ml.run(filters, target=target, horizon=self.horizon,
                               include_anomaly=True)
        except Exception as exc:  # noqa: BLE001 - one bad series must not stop the build
            logger.warning("forecast failed for %s: %s", target, exc)
            return {"available": False, "reason": str(exc)[:160]}

    @staticmethod
    def _row(series: str, result: dict, history: list[float]) -> dict:
        today = history[-1] if history else None
        ma7 = (round(sum(history[-7:]) / len(history[-7:]), 2)
               if history else None)

        if not result.get("available"):
            # State the gap rather than filling it.
            return {"series": series, "today": today, "forecast_next": "",
                    "forecast_7d": "", "ma_7d": ma7, "growth_pct": "",
                    "available": "false",
                    "unavailable_reason": result.get(
                        "reason", "insufficient history to model this series")}

        points = result.get("forecast") or []
        nxt = points[0]["forecast"] if points else None
        # The cube's `forecast_7d` is the level a week out, not a sum.
        seventh = next((p["forecast"] for p in points if p.get("horizon") == 7),
                       points[-1]["forecast"] if points else None)
        conf = result.get("confidence") or {}
        bt = result.get("backtest") or {}
        feats = result.get("most_influential_features") or []
        risks = result.get("potential_risks") or []
        actions = result.get("suggested_actions") or []
        top = feats[0] if feats else {}
        first_action = actions[0] if actions else {}

        growth = None
        if today not in (None, 0) and nxt is not None:
            growth = round(100.0 * (nxt - today) / abs(today), 2)

        return {
            "series": series,
            "today": _pct(today), "forecast_next": _pct(nxt),
            "forecast_7d": _pct(seventh), "ma_7d": ma7, "growth_pct": growth,
            "model": result.get("model"),
            "confidence_pct": _pct(conf.get("score")),
            "confidence_band": conf.get("band"),
            "backtest_mape": _pct(bt.get("mape")),
            "skill_vs_naive_pct": _pct(bt.get("skill_vs_naive")),
            "observations": result.get("observations"),
            "top_feature": top.get("label") or top.get("feature"),
            "top_feature_pct": _pct(top.get("importance_pct")),
            "business_reason": result.get("business_reason"),
            "primary_risk": risks[0] if risks else "",
            "recommended_action": (first_action.get("action")
                                   if isinstance(first_action, dict)
                                   else first_action),
            "available": "true", "unavailable_reason": "",
        }

    def _history(self, filters: Filters, target: str) -> list[float]:
        try:
            rows = self.a.daily_series(filters)
        except Exception:  # noqa: BLE001
            return []
        out = []
        for r in rows:
            try:
                out.append(float(r.get(target)))
            except (TypeError, ValueError):
                continue
        return out

    # --------------------------------------------------------------- build
    def build(self) -> dict[str, int]:
        self.out.mkdir(parents=True, exist_ok=True)
        return {"forecasts": self._forecasts(),
                "forecast_forward": self._forward(),
                "forecast_validation": self._validation()}

    # ---------------------------------------------------------- validation
    def _validation(self) -> int:
        """How well the forecaster actually did, out of sample.

        The cube this replaces was written by fitting a 14-day least-squares
        line and reporting its own error — a self-assessment by the thing
        being assessed. What is written here is the walk-forward backtest the
        ML pipeline already performs on held-out days, plus the skill against
        a seasonal-naive baseline. Skill is the number that matters: a series
        sitting flat near 99% can post a 0.4% error and still be worse than
        assuming next week looks like this one, and a validation table that
        cannot say so is not a validation table.
        """
        rows: list[dict] = []
        base = Filters()
        for series, target in TOTAL_SERIES:
            result = self._run(target, base)
            if not result.get("available"):
                rows.append({
                    "series": series, "target": target, "method": "",
                    "horizon_days": self.horizon, "observations": "",
                    "mape_pct": "", "accuracy_pct": "", "mean_abs_error": "",
                    "skill_vs_naive_pct": "", "beat_naive_baseline": "",
                    "interval_coverage_pct": "", "folds": "",
                    "confidence_pct": "", "confidence_band": "",
                    "verdict": "not modelled",
                    "unavailable_reason": result.get(
                        "reason", "insufficient history to validate")})
                continue
            bt = result.get("backtest") or {}
            conf = result.get("confidence") or {}
            mape = bt.get("mape")
            skill = bt.get("skill_vs_naive")
            beat = bool(skill is not None and skill > 0)
            if skill is None:
                verdict = "unscored"
            elif not beat:
                verdict = ("worse than seasonal-naive — the series is flat "
                           "enough that last week is a strong baseline")
            elif (mape or 100) < 5:
                verdict = "accurate and beats seasonal-naive"
            else:
                verdict = "beats seasonal-naive with material error"
            rows.append({
                "series": series, "target": target,
                "method": result.get("model"),
                "horizon_days": self.horizon,
                "observations": result.get("observations"),
                "mape_pct": _pct(mape),
                "accuracy_pct": _pct(100 - mape) if mape is not None else "",
                "mean_abs_error": _pct(bt.get("mae")),
                "skill_vs_naive_pct": _pct(skill),
                "beat_naive_baseline": str(beat).lower(),
                "interval_coverage_pct": _pct(bt.get("coverage_80")),
                "folds": bt.get("folds"),
                "confidence_pct": _pct(conf.get("score")),
                "confidence_band": conf.get("band"),
                "verdict": verdict, "unavailable_reason": ""})

        header = ["series", "target", "method", "horizon_days", "observations",
                  "mape_pct", "accuracy_pct", "mean_abs_error",
                  "skill_vs_naive_pct", "beat_naive_baseline",
                  "interval_coverage_pct", "folds", "confidence_pct",
                  "confidence_band", "verdict", "unavailable_reason"]
        path = self.out / "forecast_validation.csv"
        with path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=header, extrasaction="ignore")
            w.writeheader()
            for r in rows:
                w.writerow({k: ("" if r.get(k) is None else r.get(k))
                            for k in header})
        logger.info("projected forecast_validation.csv: %d series", len(rows))
        return len(rows)

    def _forecasts(self) -> int:
        rows: list[dict] = []
        base = Filters()

        for series, target in TOTAL_SERIES:
            result = self._run(target, base)
            rows.append(self._row(series, result,
                                  self._history(base, target)))

        # One row per product. The product's *warehouse* name is used, not the
        # old generator's label — the previous cube published "UPI Lite X" and
        # "Person to Merchant", names no other part of the platform uses, so a
        # lookup by product name silently missed.
        try:
            products = self.a.products()
        except Exception:  # noqa: BLE001
            products = []
        for p in products:
            code = p.get("product_code")
            name = p.get("product_name") or code
            if not code:
                continue
            f = Filters(product=code)
            rows.append(self._row(f"feature::{name}",
                                  self._run("attempts", f),
                                  self._history(f, "attempts")))

        path = self.out / "forecasts.csv"
        with path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=FORECAST_HEADER,
                               extrasaction="ignore")
            w.writeheader()
            for r in rows:
                w.writerow({k: ("" if r.get(k) is None else r.get(k))
                            for k in FORECAST_HEADER})
        logger.info("projected forecasts.csv: %d series", len(rows))
        return len(rows)

    def _forward(self) -> int:
        """Per-horizon forward projections with real prediction intervals.

        Rows for KPIs the corpus cannot answer are carried over from the
        existing file untouched — the same restraint the KPI workbook uses.
        """
        path = self.out / "forecast_forward.csv"
        owned = {k for k, _t, _s in FORWARD_KPIS}
        preserved: list[dict] = []
        if path.exists():
            with path.open(encoding="utf-8") as fh:
                preserved = [r for r in csv.DictReader(fh)
                             if r.get("kpi") not in owned]

        rows: list[dict] = []
        for kpi, target, scale in FORWARD_KPIS:
            result = self._run(target, Filters())
            if not result.get("available"):
                continue
            conf = _pct((result.get("confidence") or {}).get("score"))
            for p in result.get("forecast") or []:
                rows.append({
                    "kpi": kpi, "horizon_day": p.get("horizon"),
                    "date": p.get("date"),
                    "forecast": _pct(p.get("forecast", 0) * scale),
                    "lower": _pct(p.get("lower_80", 0) * scale),
                    "upper": _pct(p.get("upper_80", 0) * scale),
                    "confidence_pct": conf,
                })

        with path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=FORWARD_HEADER,
                               extrasaction="ignore")
            w.writeheader()
            for r in rows + preserved:
                w.writerow(r)
        logger.info("projected forecast_forward.csv: %d modelled + %d preserved",
                    len(rows), len(preserved))
        return len(rows) + len(preserved)

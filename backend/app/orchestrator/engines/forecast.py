"""Forecast Engine — where a metric is heading, with earned confidence.

"Predict next month's transaction volume", "what will the success rate be" —
these want a projection, and a projection is the output of a model that has been
trained on the raw transaction history and *validated by backtest*, not a
document and not a guess from the LLM. The engine runs the warehouse ML pipeline
(gradient boosting over the leak-free daily frame) on the KPI and slice the
question names, and reports the forecast with its backtest accuracy, its skill
over a seasonal-naive baseline, its confidence band and the business reason —
a low-confidence forecast is labelled as such, never smoothed over.
"""
from __future__ import annotations

from app.orchestrator.base import Engine, EngineRequest, EngineResult
from app.orchestrator.engines import _slice


class ForecastEngine(Engine):
    key = "forecast"
    label = "Forecast Engine"
    categories = ("forecast",)

    def __init__(self, ml_pipeline=None, analytics=None):
        self._ml = ml_pipeline
        self._a = analytics

    def available(self) -> bool:
        return bool(self._ml is not None and self._ml.available)

    def _horizon(self, request: EngineRequest) -> int:
        tr = request.time_range or {}
        if tr.get("token") == "next_ndays" and tr.get("n"):
            return max(7, min(60, int(tr["n"])))
        return 14

    def run(self, request: EngineRequest) -> EngineResult:
        res = self._result()
        if not self.available():
            res.status = "unavailable"
            res.ran = False
            res.note = "ML pipeline holds no transaction history"
            return res

        filters, _window = _slice.build_training_filters(request, self._a)
        horizon = self._horizon(request)
        targets = self._targets(request)
        cards: dict[str, dict] = {}
        for target in targets:
            r = self._ml.run(filters, target=target, horizon=horizon,
                             include_anomaly=False)
            if not r.get("available"):
                res.note = r.get("reason", "forecast unavailable")
                continue
            fwd = r.get("forecast", [])
            last = fwd[-1] if fwd else {}
            conf = r.get("confidence", {})
            bt = r.get("backtest") or {}
            label = r.get("target_label", target)
            unit = r.get("unit") or ""
            cards[target] = {"backtest": bt, "confidence": conf,
                             "model": r.get("model")}
            drivers = ", ".join(
                d["label"] for d in r.get("most_influential_features", [])[:3])
            res.add(
                "forecast", f"forecast:{target}",
                f"{label} {horizon}-day forecast → "
                f"{last.get('forecast')}{unit} "
                f"({conf.get('band')} confidence {conf.get('score')})",
                {"kpi": target, "label": label, "unit": unit,
                 "horizon": horizon, "confidence": conf.get("score"),
                 "confidence_band": conf.get("band"),
                 "forecast_end": last.get("forecast"),
                 "interval": [last.get("lower_80"), last.get("upper_80")],
                 "backtest_mape": bt.get("mape"),
                 "skill_vs_naive": bt.get("skill_vs_naive"),
                 "series": fwd,
                 "text": (
                     f"{label} for slice {filters.describe() or 'the platform'}: "
                     f"a gradient-boosting model projects {horizon} days ending "
                     f"at {last.get('forecast')}{unit} "
                     f"(80% interval {last.get('lower_80')}–"
                     f"{last.get('upper_80')}{unit}). The model backtests at "
                     f"{bt.get('mape')}% error, "
                     f"{bt.get('skill_vs_naive')}% better than a seasonal-naive "
                     f"baseline; confidence is {conf.get('band')} "
                     f"({conf.get('score')}/100). Main drivers: {drivers or 'n/a'}. "
                     f"{r.get('business_reason', '')}")})
            # A second fact carrying the reasoning, so the narration can cite it.
            for i, risk in enumerate(r.get("potential_risks", [])[:2]):
                res.add("forecast_risk", f"forecast:{target}:risk:{i}",
                        f"Forecast risk: {risk[:80]}",
                        {"text": f"Risk to the {label} forecast: {risk}"})

        res.detail = {"horizon_days": horizon, "targets": list(targets),
                      "slice": filters.describe(),
                      "model": "HistGradientBoosting / Ridge (backtested)",
                      "cards": cards}
        return res

    def _targets(self, request: EngineRequest) -> list[str]:
        targets = []
        for hint in request.kpi_hints or ():
            t = _slice.KPI_TO_TARGET.get(hint)
            if t and t not in targets:
                targets.append(t)
        return targets or ["attempts"]

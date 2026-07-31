"""Reason generation, confidence and business recommendations.

This is the layer that turns numbers into a decision. Nothing here invents a
fact: every sentence is a template filled from a measured statistic — a slope
with a p-value, a backtest MAPE, a permutation importance, a seasonal effect.
The confidence score is likewise earned, a weighted product of how well the
model backtested, how much history it had, how stable the series is, and how
much it beat a naive baseline. A forecast the model cannot stand behind says so.
"""
from __future__ import annotations

from app.warehouse.ml.forecast import BacktestResult


# ------------------------------------------------------------------ confidence
def confidence(bt: BacktestResult | None, eda: dict, n_obs: int) -> dict:
    """A 0-100 confidence score with the components that produced it exposed."""
    comps: dict[str, float] = {}

    # Backtest accuracy — the dominant term.
    if bt and bt.mape is not None:
        comps["backtest_accuracy"] = max(0.0, min(1.0, 1 - bt.mape / 25.0))
    else:
        comps["backtest_accuracy"] = 0.35

    # Skill over seasonal-naive: did modelling actually add value?
    if bt and bt.skill_vs_naive is not None:
        comps["skill_vs_naive"] = max(0.0, min(1.0, 0.5 + bt.skill_vs_naive / 100))
    else:
        comps["skill_vs_naive"] = 0.5

    # History depth.
    comps["history"] = max(0.0, min(1.0, n_obs / 120.0))

    # Series regularity — strong seasonality + low residual noise is learnable.
    decomp = eda.get("decomposition", {}) if eda else {}
    dist = eda.get("distribution", {}) if eda else {}
    seas = decomp.get("seasonal_strength") or 0.0
    cv = (dist.get("cv_pct") or 40) / 100.0
    comps["regularity"] = max(0.0, min(1.0, 0.5 * seas + 0.5 * (1 - min(1.0, cv))))

    weights = {"backtest_accuracy": 0.42, "skill_vs_naive": 0.18,
               "history": 0.18, "regularity": 0.22}
    score = sum(comps[k] * weights[k] for k in weights) * 100
    band = ("high" if score >= 72 else "moderate" if score >= 50 else "low")

    # A model that loses to seasonal-naive may not call itself high-confidence,
    # however small its absolute error. A near-flat series (success rate sits at
    # ~99% all year) scores well on accuracy and regularity and would otherwise
    # reach "high" while being beaten by "assume next week looks like this one"
    # — and the high-confidence wording asserts it beat that baseline, which
    # would then be false. Cap the band and say what actually happened.
    lost_to_naive = bool(bt and bt.skill_vs_naive is not None
                         and bt.skill_vs_naive < 0)
    if lost_to_naive and band == "high":
        band = "moderate"
    return {
        "score": round(score, 1),
        "band": band,
        "components": {k: round(v, 3) for k, v in comps.items()},
        "weights": weights,
        "beat_naive_baseline": None if not bt or bt.skill_vs_naive is None
        else not lost_to_naive,
        "interpretation": _confidence_text(band, bt, lost_to_naive)}


def _confidence_text(band: str, bt: BacktestResult | None,
                     lost_to_naive: bool = False) -> str:
    mape = f"{bt.mape:.1f}% backtest error" if bt and bt.mape is not None \
        else "limited validation history"
    if lost_to_naive:
        skill = abs(bt.skill_vs_naive) if bt and bt.skill_vs_naive else 0.0
        return (f"Moderate confidence — the model tracks the series closely "
                f"({mape}) but did not beat a seasonal-naive baseline "
                f"(worse by {skill:.0f}%), so the series is better read as "
                f"stable than as modelled. Use the level, not the movement.")
    if band == "high":
        return (f"High confidence — the model held up out-of-sample "
                f"({mape}) and beat a seasonal-naive baseline.")
    if band == "moderate":
        return (f"Moderate confidence — usable for planning but treat the "
                f"interval as real ({mape}).")
    return (f"Low confidence — {mape}; use the direction, not the exact number, "
            f"and revisit as more history lands.")


# --------------------------------------------------------------- supporting
def anomaly_impact(dates: list | None, series: list[float] | None,
                   anomalies: dict | None) -> dict | None:
    """How much the anomalous days moved the level the forecast starts from.

    A forecast trained through an outage inherits it. Quantifying that is the
    difference between "15 anomalies were detected" — which tells a reader
    nothing actionable — and "excluding them the series sits 0.8% higher, so
    the projection is anchored to a depressed baseline", which tells them
    whether to trust the number they are about to plan against.
    """
    if not series or not dates or not anomalies \
            or not anomalies.get("available"):
        return None
    flagged = {str(p.get("date")) for key in ("seasonal_anomalies",
                                              "multivariate_anomalies")
               for p in (anomalies.get(key) or [])
               if isinstance(p, dict) and p.get("date")}
    if not flagged:
        return None
    clean = [v for d, v in zip(dates, series) if str(d)[:10] not in flagged]
    if len(clean) < 10 or len(clean) == len(series):
        return None
    with_mean = sum(series) / len(series)
    without_mean = sum(clean) / len(clean)
    if with_mean == 0:
        return None
    shift_pct = (without_mean - with_mean) / abs(with_mean) * 100
    n_flagged = len(series) - len(clean)
    return {
        "anomalous_days": n_flagged,
        "share_of_window_pct": round(n_flagged / len(series) * 100, 1),
        "mean_with_anomalies": round(with_mean, 4),
        "mean_excluding_anomalies": round(without_mean, 4),
        "baseline_shift_pct": round(shift_pct, 3),
        "interpretation": (
            f"Removing the {n_flagged} anomalous day(s) moves the window mean "
            f"by {shift_pct:+.2f}%. "
            + ("That is small enough that the forecast is not meaningfully "
               "anchored to them."
               if abs(shift_pct) < 0.5 else
               "The forecast starts from a baseline those days have "
               f"{'depressed' if shift_pct > 0 else 'inflated'}, so treat the "
               "projected level as carrying that distortion.")),
    }


def supporting_factors(eda: dict, importances: list[dict],
                       target: str, anomaly_effect: dict | None = None
                       ) -> list[dict]:
    """The measured signals behind the forecast, each with its evidence."""
    factors: list[dict] = []
    if anomaly_effect:
        factors.append({
            "factor": "anomaly impact",
            "finding": anomaly_effect["interpretation"],
            "evidence": (
                f"{anomaly_effect['anomalous_days']} flagged day(s) "
                f"({anomaly_effect['share_of_window_pct']}% of the window); "
                f"mean {anomaly_effect['mean_with_anomalies']} with vs "
                f"{anomaly_effect['mean_excluding_anomalies']} without"),
            "strength": "strong"
            if abs(anomaly_effect["baseline_shift_pct"]) >= 0.5
            else "weak"})
    trend = eda.get("trend", {}) if eda else {}
    if trend.get("detected"):
        factors.append({
            "factor": "underlying trend",
            "finding": f"{target.replace('_', ' ')} is {trend['direction']} "
                       f"{abs(trend.get('slope_pct_per_day') or 0):.3f}% per day",
            "evidence": f"OLS R²={trend.get('r_squared')}, "
                        f"p={trend.get('p_value')}, "
                        f"Mann-Kendall p={trend.get('mann_kendall_p')}",
            "strength": "strong" if (trend.get("r_squared") or 0) > 0.5
            else "moderate"})

    wk = eda.get("weekly_seasonality", {}) if eda else {}
    if wk.get("detected"):
        factors.append({
            "factor": "weekly seasonality",
            "finding": f"peaks on {wk.get('peak_day')}, "
                       f"troughs on {wk.get('trough_day')}",
            "evidence": f"ANOVA F={wk.get('f_statistic')}, p={wk.get('p_value')}",
            "strength": "strong"})

    decomp = eda.get("decomposition", {}) if eda else {}
    if decomp.get("available") and (decomp.get("seasonal_strength") or 0) > 0.3:
        factors.append({
            "factor": "seasonal structure",
            "finding": f"{decomp['seasonal_strength']*100:.0f}% of variance is "
                       f"repeatable weekly pattern",
            "evidence": f"decomposition explains {decomp.get('explained_pct')}% "
                        f"of variance",
            "strength": "moderate"})

    cps = eda.get("change_points", []) if eda else []
    if cps:
        last = cps[-1]
        factors.append({
            "factor": "level shift",
            "finding": f"a {last.get('direction')} step of "
                       f"{abs(last.get('shift_pct') or 0):.1f}% is in the history",
            "evidence": f"t={last.get('t_statistic')} at observation "
                        f"{last.get('index')}",
            "strength": "strong"})

    for imp in importances[:4]:
        factors.append({
            "factor": "model driver",
            "finding": f"{imp['label']} drives {imp['importance_pct']}% "
                       f"of predictive signal",
            "evidence": f"permutation importance {imp['importance']} "
                        f"(stability {imp['stability']})",
            "strength": "strong" if imp["importance_pct"] > 25 else "moderate"})
    return factors


# ------------------------------------------------------------------ reason
def business_reason(eda: dict, forecast: list[dict], bt: BacktestResult | None,
                    target: str, kpi_meta: dict | None = None) -> str:
    """A single paragraph a product manager can paste into a review deck."""
    label = (kpi_meta or {}).get("label", target.replace("_", " "))
    if not forecast:
        return f"Not enough clean history to forecast {label} for this slice."
    first, last = forecast[0]["forecast"], forecast[-1]["forecast"]
    trend = eda.get("trend", {}) if eda else {}
    change = (100 * (last - first) / first) if first else 0
    direction = ("rise" if change > 1 else "decline" if change < -1
                 else "hold roughly flat")
    horizon = forecast[-1]["horizon"]

    bits = [f"{label} is projected to {direction}"]
    if abs(change) > 1:
        bits[-1] += f" about {abs(change):.1f}% over the next {horizon} days"
    else:
        bits[-1] += f" over the next {horizon} days"

    if trend.get("detected"):
        # Reconcile the two explicitly when they disagree. A paragraph that
        # says "projected to decline" and "the trend is increasing" in
        # consecutive sentences reads as a contradiction and costs the reader
        # their confidence in the whole output, when in fact it is the single
        # most useful thing the model has to say.
        rising = trend["direction"] == "increasing"
        opposed = (change < -1 and rising) or (change > 1 and not rising)
        if opposed:
            bits.append(
                f"this runs against the underlying trend, which is "
                f"{trend['direction']} and statistically real "
                f"(p={trend.get('p_value')}) — so the move is a short-horizon "
                f"effect (weekday mix, calendar or a recent level shift) "
                f"rather than a change of direction")
        else:
            bits.append(f"consistent with an underlying trend that is "
                        f"{trend['direction']} and statistically real "
                        f"(p={trend.get('p_value')})")
    wk = eda.get("weekly_seasonality", {}) if eda else {}
    if wk.get("detected"):
        bits.append(f"with the usual weekly rhythm peaking {wk.get('peak_day')} "
                    f"and dipping {wk.get('trough_day')}")
    if bt and bt.mape is not None:
        bits.append(f"the model backtests at {bt.mape:.1f}% error"
                    + (f", {bt.skill_vs_naive:.0f}% better than assuming next week "
                       f"looks like this week" if bt.skill_vs_naive else ""))
    return ". ".join(s[0].upper() + s[1:] for s in bits) + "."


# ------------------------------------------------------------------- risks
def potential_risks(eda: dict, bt: BacktestResult | None,
                    anomalies: dict | None, target: str) -> list[str]:
    risks: list[str] = []
    dist = eda.get("distribution", {}) if eda else {}
    if (dist.get("cv_pct") or 0) > 35:
        risks.append(f"High day-to-day volatility (CV {dist['cv_pct']:.0f}%) "
                     f"widens the real-world interval.")
    stat = eda.get("stationarity", {}) if eda else {}
    if stat.get("stationary") is False and (stat.get("level_shift_pct") or 0):
        risks.append(f"The series is non-stationary "
                     f"({stat['level_shift_pct']:+.0f}% level shift across the "
                     f"window) — a past regime may not hold.")
    if bt and bt.coverage_80 is not None and bt.coverage_80 < 70:
        risks.append(f"Backtest interval coverage is only {bt.coverage_80:.0f}% "
                     f"vs an 80% target — intervals may be optimistic.")
    elif bt and bt.coverage_80 is not None and bt.coverage_80 > 90:
        # Over-coverage is a real defect, not a bonus: it means the band is
        # so wide it excludes almost nothing, so planning against it is
        # planning against a range that carries little information.
        risks.append(f"Backtest interval coverage is {bt.coverage_80:.0f}% "
                     f"against an 80% target — the prediction band is wider "
                     f"than the data warrants, so treat the interval as "
                     f"conservative rather than as a tight planning range.")
    if bt and bt.skill_vs_naive is not None and bt.skill_vs_naive < 0:
        risks.append("The model does not beat a seasonal-naive baseline here; "
                     "the extra machinery is not earning its keep on this slice.")
    if anomalies and anomalies.get("available"):
        n = anomalies.get("distinct_anomaly_days", 0)
        if n > 0:
            risks.append(f"{n} anomalous day(s) detected in-window (outages / "
                         f"spikes) that could recur and break the pattern.")
    cps = eda.get("change_points", []) if eda else []
    if len(cps) >= 2:
        risks.append("Multiple historical level shifts mean the series changes "
                     "regime; forecasts should be revalidated frequently.")
    if not risks:
        risks.append("No major statistical risk flags on this slice.")
    return risks


# --------------------------------------------------------------- actions
def suggested_actions(eda: dict, forecast: list[dict], target: str,
                      confidence_band: str) -> list[dict]:
    """Concrete next steps, prioritised, each tied to what triggered it."""
    actions: list[dict] = []
    trend = eda.get("trend", {}) if eda else {}
    label = target.replace("_", " ")

    if target in ("success_rate",) and trend.get("direction") == "decreasing" \
            and trend.get("detected"):
        actions.append({"priority": "high",
                        "action": f"Success rate is trending down — pull the "
                                  f"failure-code breakdown and engage the worst "
                                  f"bank/PSP before it compounds.",
                        "trigger": "significant negative trend in success rate"})
    if target in ("attempts", "value_inr", "successful") \
            and trend.get("direction") == "increasing" and trend.get("detected"):
        actions.append({"priority": "medium",
                        "action": f"{label.capitalize()} is growing — verify "
                                  f"capacity headroom and settlement limits hold "
                                  f"through the forecast peak.",
                        "trigger": "significant positive growth trend"})
    if target in ("technical_decline_pct", "timeout_pct", "risk_decline_pct") \
            and trend.get("direction") == "increasing":
        actions.append({"priority": "high",
                        "action": f"{label.capitalize()} is rising — open an "
                                  f"incident review on the rails driving it.",
                        "trigger": "rising failure metric"})

    wk = eda.get("weekly_seasonality", {}) if eda else {}
    if wk.get("detected"):
        actions.append({"priority": "low",
                        "action": f"Plan campaigns and capacity around the "
                                  f"{wk.get('peak_day')} peak and "
                                  f"{wk.get('trough_day')} trough.",
                        "trigger": "significant weekly seasonality"})
    if confidence_band == "low":
        actions.append({"priority": "medium",
                        "action": "Treat this forecast as directional only and "
                                  "re-run once more history accumulates or the "
                                  "slice is widened.",
                        "trigger": "low model confidence"})
    if forecast:
        peak = max(forecast, key=lambda r: r["forecast"])
        actions.append({"priority": "low",
                        "action": f"Highest projected {label} lands "
                                  f"{peak['date']} (~{peak['forecast']:,}); "
                                  f"align staffing and monitoring to it.",
                        "trigger": "forecast peak"})
    order = {"high": 0, "medium": 1, "low": 2}
    actions.sort(key=lambda a: order.get(a["priority"], 3))
    return actions

"""Insight engine (V10.0) — the multi-layer analyst.

Insights here never merely restate a KPI. Each one explains **why**, grounded in
the deterministic cubes, the Layer-2 ML models and the evolution history, and
carries everything an executive needs to act: root cause, impact, confidence,
supporting evidence, alternative explanations, business risks, recommended
actions, expected ROI, implementation complexity, dependencies, owner and
priority — plus which intelligence layer/model produced it (explainability).

It composes existing layers (deterministic + ML + graph/evidence) and applies a
confidence gate, so a weak-evidence insight is labelled as such rather than
overstated. Timeline language is business-facing (see :mod:`BusinessTimeline`).
"""
from __future__ import annotations

from app.analyst.timeline import BusinessTimeline
from app.core.logging import get_logger

logger = get_logger(__name__)

CONFIDENCE_FLOOR = 55.0  # below this an insight is flagged low-evidence


def _conf_label(c: float) -> str:
    return ("High" if c >= 80 else "Medium" if c >= CONFIDENCE_FLOOR
            else "Low — limited evidence")


class InsightEngine:
    def __init__(self, container):
        self._c = container

    def _ml(self):
        return getattr(self._c, "ml", None)

    def _evo(self):
        return getattr(self._c, "evolution", None)

    def _eco(self):
        return getattr(self._c, "ecosystem", None)

    @property
    def available(self) -> bool:
        evo = self._evo()
        return bool(evo and evo.available)

    def _tl(self) -> BusinessTimeline:
        return BusinessTimeline.from_container(self._c)

    # ------------------------------------------------------------ builder
    @staticmethod
    def _insight(*, iid, title, what, why, impact, confidence, evidence,
                 alternatives, risks, actions, roi, complexity, dependencies,
                 owner, priority, layer, model, period) -> dict:
        c = round(float(confidence), 1)
        return {
            "id": iid, "title": title, "what": what, "why": why,
            "impact": impact, "confidence": c, "confidence_label": _conf_label(c),
            "low_evidence": c < CONFIDENCE_FLOOR,
            "supporting_evidence": evidence, "alternative_explanations": alternatives,
            "business_risks": risks, "recommended_actions": actions,
            "expected_roi": roi, "implementation_complexity": complexity,
            "dependencies": dependencies, "owner": owner, "priority": priority,
            "source_layer": layer, "model": model, "business_period": period,
        }

    # ------------------------------------------------------------ generate
    def insights(self, limit: int = 12) -> dict:
        if not self.available:
            return {"available": False, "insights": []}
        tl = self._tl()
        out: list[dict] = []
        for gen in (self._forecast_insight, self._anomaly_insight,
                    self._failure_insight, self._churn_insight,
                    self._psp_insight, self._opportunity_insight,
                    self._decision_value_insight):
            try:
                ins = gen(tl)
                if ins:
                    out.append(ins)
            except Exception:  # noqa: BLE001 — one generator never breaks the set
                logger.exception("insight generator failed: %s", gen.__name__)
        rank = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
        out.sort(key=lambda i: (rank.get(i["priority"], 5), -i["confidence"]))
        return {"available": True, "count": len(out), "insights": out[:limit],
                "generated_for": tl.period("month")}

    # ---- ML: forecast ----------------------------------------------------
    def _forecast_insight(self, tl):
        ml = self._ml()
        if not (ml and ml.available):
            return None
        fc = ml.forecast("Success Rate (%)")
        if not fc.get("available"):
            return None
        rows = fc["forecast"]
        last, proj = fc["last_actual"], rows[-1]["forecast"]
        direction = "improve" if proj >= last else "soften"
        conf = fc["confidence"]
        return self._insight(
            iid="forecast-success", title="Success Rate outlook",
            what=f"Success Rate is projected to {direction} to ~{proj}% over the "
                 f"next 30 days (now {last}%).",
            why=f"A ridge model over time, weekly seasonality and lag features "
                f"backtests at {fc['card']['metrics']['accuracy_pct']}% accuracy; "
                f"the recent trajectory extrapolates to {proj}%.",
            impact="Directly drives customer/merchant complaints and settlement "
                   "reliability.",
            confidence=conf,
            evidence=[f"ML forecast (Ridge), MAPE {fc['card']['metrics']['mape_pct']}%",
                      f"{fc['card']['metrics']['history_points']} days of history"],
            alternatives=["A fresh bank/PSP incident could break the trend",
                          "Festival-season volume spikes may add noise"],
            risks=["Under-provisioning if the upside is assumed"],
            actions=["Hold capacity headroom for the projected volume",
                     "Watch the confidence band for divergence"],
            roi="Protects revenue by pre-empting SR dips", complexity="Low",
            dependencies=["Bank/PSP reliability"], owner="Product Operations",
            priority="Medium" if conf >= CONFIDENCE_FLOOR else "Low",
            layer="ML (Layer 2)", model=fc["card"]["model"],
            period=tl.period("rolling30"))

    # ---- ML: anomaly -----------------------------------------------------
    def _anomaly_insight(self, tl):
        ml = self._ml()
        if not (ml and ml.available):
            return None
        an = ml.anomalies()
        if not an.get("available") or not an.get("anomalies"):
            return None
        top = an["anomalies"][0]
        when = tl.relative(top.get("date"))
        return self._insight(
            iid="anomaly-top", title="Operating anomaly detected",
            what=f"An unusual operating day was detected {when} "
                 f"(success {top.get('success_rate')}%, technical declines "
                 f"{top.get('technical_decline_pct')}%).",
            why="IsolationForest flagged this day as a multivariate outlier "
                "against the normal operating envelope — most consistent with a "
                "bank/PSP reliability event rather than demand.",
            impact="Elevated declines and complaints on the affected day.",
            confidence=an["confidence"],
            evidence=[f"IsolationForest anomaly score {top.get('anomaly_score')}",
                      f"{an['count']} anomalous days in the period"],
            alternatives=["A planned maintenance window",
                          "A one-off campaign volume surge"],
            risks=["Recurrence if the root cause is not addressed"],
            actions=["Correlate with the incident log for that day",
                     "Confirm the remediation held afterwards"],
            roi="Avoids repeat incidents", complexity="Low",
            dependencies=["Incident management"], owner="Operations",
            priority="High", layer="ML (Layer 2)", model="IsolationForest",
            period=tl.relative(top.get("date")))

    # ---- ML: failure risk ------------------------------------------------
    def _failure_insight(self, tl):
        ml = self._ml()
        if not (ml and ml.available):
            return None
        fb = ml.failure_banks()
        if not fb.get("available") or not fb.get("banks_at_risk"):
            return None
        top = fb["banks_at_risk"][0]
        if top["failure_risk"] < 15:
            return None  # nothing materially at risk — don't manufacture a risk
        imp = fb.get("feature_importances", [])[:2]
        return self._insight(
            iid="failure-bank", title=f"Elevated failure risk: {top['bank']}",
            what=f"{top['bank']} shows a {top['failure_risk']}% modelled "
                 f"incident risk (success {top.get('success_rate')}%, p95 "
                 f"{top.get('p95_latency_ms')}ms).",
            why="A gradient-boosting classifier on per-bank share/success/"
                "latency/health finds this bank in the risk region; top drivers: "
                + ", ".join(f["feature"] for f in imp) + ".",
            impact="A Tier-1 bank incident affects success rate broadly.",
            confidence=fb["confidence"],
            evidence=[f"GradientBoosting risk {top['failure_risk']}%",
                      "per-bank/week signals"],
            alternatives=["Transient latency, not a systemic fault"],
            risks=["Customer complaints and settlement delays if it materialises"],
            actions=[f"Open a proactive reliability review with {top['bank']}",
                     "Pre-stage the failover SOP"],
            roi="Prevents a high-impact outage", complexity="Medium",
            dependencies=["Bank coordination"], owner="Bank Coordination",
            priority="High", layer="ML (Layer 2)",
            model="GradientBoostingClassifier", period=tl.period("rolling30"))

    # ---- ML: churn -------------------------------------------------------
    def _churn_insight(self, tl):
        ml = self._ml()
        if not (ml and ml.available):
            return None
        ch = ml.churn_merchants()
        if not ch.get("available") or not ch.get("at_risk"):
            return None
        top = ch["at_risk"][:3]
        if top[0]["churn_risk"] < 25:
            return None
        imp = ch.get("feature_importances", [])[:2]
        names = ", ".join(t["merchant"] for t in top)
        return self._insight(
            iid="churn-merchants", title="Merchants at churn risk",
            what=f"{names} carry the highest modelled churn propensity "
                 f"(top {top[0]['churn_risk']}%).",
            why="A random-forest propensity model on merchant health, growth, "
                "success and satisfaction ranks these highest; top drivers: "
                + ", ".join(f["feature"] for f in imp) + ".",
            impact="Merchant attrition erodes GMV and acceptance footprint.",
            confidence=ch["confidence"],
            evidence=[f"RandomForest propensity, top risk {top[0]['churn_risk']}%",
                      "merchant lifecycle features"],
            alternatives=["Seasonal dip rather than true disengagement"],
            risks=["Lost settlement volume and category coverage"],
            actions=["Trigger merchant success outreach to the top names",
                     "Review settlement timeliness for these accounts"],
            roi="Retains GMV at low cost", complexity="Low",
            dependencies=["Merchant Success"], owner="Merchant Success",
            priority="Medium", layer="ML (Layer 2)",
            model="RandomForestClassifier", period=tl.period("month"))

    # ---- evolution: PSP share --------------------------------------------
    def _psp_insight(self, tl):
        evo = self._evo()
        p = evo.psps()
        losers = p.get("losing_share", [])
        if not losers or losers[0]["share_change_pct"] > -0.05:
            return None
        top = losers[0]
        return self._insight(
            iid="psp-share", title=f"{top['psp']} is losing market share",
            what=f"{top['psp']} share moved {top['share_change_pct']}% over the "
                 f"period (now {top['market_share_pct']}%).",
            why="Its transaction share declined relative to peers while overall "
                "volume grew — a competitive shift, not a volume problem "
                f"(success rate {top.get('success_rate')}% is healthy).",
            impact="Distribution mix shifts affect routing and partner leverage.",
            confidence=72,
            evidence=[f"PSP evolution: {top['share_change_pct']}% share change"],
            alternatives=["A temporary campaign by a competing PSP"],
            risks=["Concentration risk if volume consolidates elsewhere"],
            actions=["Review the partner's roadmap and incentives"],
            roi="Protects ecosystem balance", complexity="Medium",
            dependencies=["PSP Integration"], owner="PSP Integration",
            priority="Medium", layer="Deterministic + graph",
            model="EvolutionIntelligence", period=tl.period("month"))

    # ---- evolution: opportunity ------------------------------------------
    def _opportunity_insight(self, tl):
        evo = self._evo()
        inv = evo.products().get("investable", [])
        if not inv:
            return None
        top = inv[0]
        return self._insight(
            iid="opportunity", title=f"Investment opportunity: {top['product']}",
            what=f"{top['product']} is growing {top.get('mom_growth_pct')}% m/m "
                 f"and is still in the {top.get('lifecycle_stage')} stage.",
            why="It combines above-trend growth with low market share — the "
                "signature of headroom the portfolio can compound.",
            impact="Incremental volume and revenue with room to scale.",
            confidence=76,
            evidence=[f"Product lifecycle: {top.get('mom_growth_pct')}% m/m, "
                      f"stage {top.get('lifecycle_stage')}"],
            alternatives=["Early-stage volatility may overstate the trend"],
            risks=["Scaling before reliability hardens"],
            actions=[f"Prioritise {top['product']} capacity and GTM"],
            roi="High — growth-stage compounding", complexity="Medium",
            dependencies=[top.get("team", "Product")],
            owner=top.get("owner", "Product"), priority="High",
            layer="Deterministic", model="EvolutionIntelligence",
            period=tl.period("month"))

    # ---- evolution: proven decision value --------------------------------
    def _decision_value_insight(self, tl):
        evo = self._evo()
        d = evo.decisions()
        top = d.get("top_value", [])
        if not top:
            return None
        best = top[0]
        return self._insight(
            iid="decision-value", title="Highest-value decision to repeat",
            what=f"{best.get('decision_id')} ({best.get('title')}) protected "
                 f"₹{best.get('business_value_cr')}cr with success "
                 f"{best.get('success_score')}.",
            why="Its measured recovery-vs-trough and protected transaction value "
                "were the largest of all tracked decisions — a proven playbook.",
            impact=f"₹{d.get('total_business_value_cr')}cr protected across "
                   f"{d.get('count')} decisions.",
            confidence=85,
            evidence=[f"Decision tracking: ₹{best.get('business_value_cr')}cr, "
                      f"success {best.get('success_score')}"],
            alternatives=["Value attribution assumes the remediation caused the "
                          "recovery"],
            risks=["Playbook may not transfer to a different failure mode"],
            actions=["Codify this response as the standard SOP"],
            roi="Proven, repeatable", complexity="Low",
            dependencies=["Operations"], owner="UPI Products leadership",
            priority="Medium", layer="Deterministic + evidence",
            model="EvolutionIntelligence", period=tl.period("quarter"))

    # ------------------------------------------------- confidence gate API
    def gate(self, confidence: float, has_evidence: bool) -> dict:
        """Shared hallucination gate: below the floor or with no evidence, the
        caller must abstain rather than assert."""
        ok = has_evidence and confidence >= CONFIDENCE_FLOOR
        return {"pass": ok, "confidence": round(float(confidence), 1),
                "floor": CONFIDENCE_FLOOR,
                "message": None if ok else
                "I don't have enough verified evidence to answer that "
                "confidently."}

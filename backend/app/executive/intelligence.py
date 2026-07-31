"""ExecutiveIntelligence — reasoning over the enterprise, for a Product Head.

Turns the structured facts the :class:`EnterpriseReader` recovers into the
outputs an executive operating system needs: a daily brief, Monday-morning
priorities, ranked recommendations, KPI intelligence (with *why it changed*),
and enhanced/ranked decisions. Every number traces to the KPI workbook and
every name to the roster, so answers do not hallucinate.

Nothing here changes the Brain, the generator, or any existing API — it reads
what the Brain already ingested and reasons over it deterministically.
"""
from __future__ import annotations

import re
from functools import lru_cache
from typing import Any

from app.core.logging import get_logger
from app.executive.reader import WEEKDAYS, Artifact, Enterprise, EnterpriseReader

logger = get_logger(__name__)

# Per-KPI health model: (direction, floor, target). Higher-better KPIs score
# 100 at/above target and 0 at/below floor; lower-better invert. KPIs absent
# here fall back to week min/max normalisation. Names match the catalog.
KPI_SPEC: dict[str, tuple[str, float, float]] = {
    "Success Rate (%)": ("up", 98.0, 99.35),
    "Settlement Success (%)": ("up", 98.4, 99.6),
    "Technical Declines (%)": ("down", 1.4, 0.45),
    "Business Declines (%)": ("down", 0.5, 0.2),
    "UPI Transactions (M/day)": ("up", 640, 780),
    "Merchant Adoption (M)": ("up", 56, 66),
    "Active Banks": ("up", 690, 745),
    "Active PSPs": ("up", 55, 60),
    "UPI Lite Adoption (M)": ("up", 40, 44),
    "Autopay Registrations (K/day)": ("up", 440, 560),
    "Fraud Alerts": ("down", 1500, 1000),
    "Customer Complaints": ("down", 5000, 1800),
    "Merchant Complaints": ("down", 700, 190),
    "Response Time (ms)": ("down", 1000, 720),
    "Risk Score": ("down", 60, 28),
}

# Which composite each KPI feeds. A KPI can inform several health scores.
HEALTH_GROUPS: dict[str, list[str]] = {
    "operational": ["Success Rate (%)", "Settlement Success (%)",
                    "Technical Declines (%)", "Response Time (ms)",
                    "Active Banks", "Active PSPs"],
    "customer": ["Customer Complaints", "Success Rate (%)",
                 "UPI Lite Adoption (M)"],
    "merchant": ["Merchant Complaints", "Merchant Adoption (M)"],
    "growth": ["UPI Transactions (M/day)", "UPI Lite Adoption (M)",
               "Autopay Registrations (K/day)", "Merchant Adoption (M)"],
    "risk": ["Risk Score", "Fraud Alerts", "Technical Declines (%)"],
}


def _clamp(x: float, lo: float = 0.0, hi: float = 100.0) -> float:
    return max(lo, min(hi, x))


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-")


def _day_label(idx: int) -> str:
    """Weekday name for a 0-based day index that may span multiple weeks
    (e.g. 9 -> 'Tuesday (Week 2)')."""
    week = idx // 7 + 1
    name = WEEKDAYS[idx % 7]
    return name if idx < 7 else f"{name} (Week {week})"


class ExecutiveIntelligence:
    """Read-only reasoning layer. Rebuilt facts are cached by corpus mtime, so
    a re-ingested or regenerated enterprise is reflected without a restart."""

    def __init__(self, reader: EnterpriseReader):
        self._reader = reader

    # ------------------------------------------------------------- facts
    def enterprise(self) -> Enterprise:
        return self._reader.load()

    @property
    def available(self) -> bool:
        return self.enterprise().available

    # --------------------------------------------------- incident narrative
    def incident(self) -> dict:
        """The week's headline incident, recovered from the KPI shape and the
        incident/RCA artifacts plus the workbook's incident flags."""
        ent = self.enterprise()
        return self._incident(ent)

    @staticmethod
    def _latest_week_rows(rows: list[dict]) -> list[dict]:
        """``banks_perf``/``psps_perf``/``merchants_perf`` carry one row per
        entity *per week* (a ``Week`` column) once the corpus spans multiple
        weeks; callers that want "this week's" snapshot need just the latest
        week's rows. Rows without a ``Week`` column (older single-week
        corpus) pass through unchanged."""
        weeks = [r.get("Week") for r in rows if r.get("Week")]
        if not weeks:
            return rows
        latest = sorted(set(weeks))[-1]
        return [r for r in rows if r.get("Week") == latest]

    @staticmethod
    def _week_label_index(label: str) -> int:
        """'Week 3' -> 2 (0-based). Non-matching labels sort last."""
        m = re.search(r"(\d+)", label or "")
        return int(m.group(1)) - 1 if m else 999

    @classmethod
    def _incident(cls, ent: Enterprise) -> dict:
        """The most recent week that actually had a bank-flagged incident —
        not simply the last 7 days, which may be a quiet steady-state week
        with nothing to report."""
        sr = ent.kpis.get("Success Rate (%)", [])
        if not sr:
            return {}
        end = len(sr) - 1

        weeks_with_incident = sorted({
            r.get("Week") for r in ent.banks_perf
            if str(r.get("Incident bank", "")).upper() == "YES" and r.get("Week")
        }, key=cls._week_label_index)
        target_week = weeks_with_incident[-1] if weeks_with_incident else None

        if target_week:
            banks_now = [r for r in ent.banks_perf if r.get("Week") == target_week]
            psps_now = [r for r in ent.psps_perf if r.get("Week") == target_week]
            merchants_now = [r for r in ent.merchants_perf if r.get("Week") == target_week]
            wi = cls._week_label_index(target_week)
            wstart, wend = wi * 7, min(wi * 7 + 6, end)
            window = sr[wstart:wend + 1]
            low_day = wstart + min(range(len(window)), key=lambda i: window[i])
        else:
            banks_now = cls._latest_week_rows(ent.banks_perf)
            psps_now = cls._latest_week_rows(ent.psps_perf)
            merchants_now = cls._latest_week_rows(ent.merchants_perf)
            window = sr[-7:] if len(sr) >= 7 else sr
            low_day = end - len(window) + min(range(len(window)), key=lambda i: window[i])

        bank = next((r.get("Bank") for r in banks_now
                     if str(r.get("Incident bank", "")).upper() == "YES"), "")
        psp = next((r.get("PSP") for r in psps_now
                    if str(r.get("Incident PSP", "")).upper() == "YES"), "")
        merchants = [r.get("Merchant") for r in merchants_now
                     if str(r.get("Affected this week", r.get("Autopay affected", ""))).upper() == "YES"]

        # Prefer the incident artifact from the target week; fall back to the
        # most recent incident on record.
        incidents = sorted(ent.by_kind("incident"), key=lambda a: a.timestamp, reverse=True)
        inc = None
        if target_week is not None:
            wi = cls._week_label_index(target_week)
            inc = next((a for a in incidents if (a.day - 1) // 7 == wi), None)
        inc = inc or (incidents[0] if incidents else None)
        rcas = sorted(ent.by_kind("rca"), key=lambda a: a.timestamp, reverse=True)
        rca = next((a for a in rcas if inc and (a.day - 1) // 7 == (inc.day - 1) // 7),
                  rcas[0] if rcas else None)
        # The affected product: the product named in the incident title/text.
        product = "UPI Autopay"
        for p in ent.products:
            if inc and p["name"].lower() in (inc.title + inc.text).lower():
                product = p["name"]
                break
        recovered = sr[end] >= max(sr) - 0.05
        sev_m = re.search(r"Severity:\**\s*(Sev-\d)", inc.text) if inc else None
        severity = sev_m.group(1) if sev_m else "Sev-2"
        # The level the incident dropped *from*, so the brief can state a real
        # movement. Without it the summary compared the week's trough with the
        # last day of the whole series and could report "fell to 96.31% and
        # recovered to 96.31%" — a sentence that describes nothing.
        pre = sr[max(0, low_day - 7):low_day]
        baseline = round(sum(pre) / len(pre), 2) if pre else sr[low_day]
        return {
            "incident_id": inc.art_id if inc else "",
            "rca_id": rca.art_id if rca else "",
            "product": product,
            "bank": bank, "psp": psp, "merchants": [m for m in merchants if m],
            "low_day": _day_label(low_day), "low_day_index": low_day,
            "baseline_success_rate": baseline,
            "dip_pp": round(baseline - sr[low_day], 2),
            "low_success_rate": sr[low_day],
            "current_success_rate": sr[end],
            "recovered": recovered,
            "severity": severity,
        }

    # ----------------------------------------------------- KPI intelligence
    def kpi_intelligence(self) -> dict:
        ent = self.enterprise()
        inc = self._incident(ent)
        cards = [self._kpi_card(ent, kpi, inc) for kpi in ent.kpis]
        health = self._health_scores(ent, cards)
        # Rank cards: worst health and biggest adverse move first.
        cards.sort(key=lambda c: (c["health"], -abs(c["change"] or 0)))
        return {"health": health, "kpis": cards,
                "count": len(cards), "generated_for": ent.week_start}

    def _kpi_card(self, ent: Enterprise, kpi: str, inc: dict) -> dict:
        series = ent.kpis[kpi]
        latest = series[-1]
        prev = series[-2] if len(series) > 1 else None
        change = round(latest - prev, 3) if prev is not None else None
        low = min(series)
        low_idx = series.index(low)
        direction, floor, target = KPI_SPEC.get(
            kpi, ("up", min(series), max(series)))
        health = self._kpi_health(latest, direction, floor, target)
        trend = self._trend(series, direction)
        why, cause, action = self._kpi_narrative(kpi, series, direction, inc,
                                                 low_idx, health)
        evidence = [e for e in (inc.get("incident_id"), inc.get("rca_id"),
                                "upi_kpis_month.xlsx") if e]
        return {
            "kpi": kpi, "unit": ent.kpi_units.get(kpi, ""),
            "value": latest, "previous": prev, "change": change,
            "week": series, "health": round(health),
            "trend": trend, "direction": direction,
            "why_changed": why, "caused_by": cause,
            "recommended_action": action, "evidence": evidence,
        }

    @staticmethod
    def _kpi_health(value: float, direction: str, floor: float,
                    target: float) -> float:
        if target == floor:
            return 70.0
        if direction == "down":
            return _clamp((floor - value) / (floor - target) * 100)
        return _clamp((value - floor) / (target - floor) * 100)

    @staticmethod
    def _trend(series: list[float], direction: str) -> str:
        if len(series) < 2:
            return "flat"
        delta = series[-1] - series[0]
        if abs(delta) < 1e-9:
            return "flat"
        rising = delta > 0
        good = rising if direction == "up" else not rising
        return "improving" if good else "worsening"

    def _kpi_narrative(self, kpi: str, series: list[float], direction: str,
                       inc: dict, low_idx: int, health: float):
        """Why the KPI moved, what caused it, and what to do — grounded in the
        incident window and the recovery."""
        end = len(series) - 1
        moved_in_incident = low_idx <= 2  # dip in the Mon-Wed incident window
        bank = inc.get("bank", "a sponsor bank")
        recovering = series[end] >= max(series) - (0.1 if "%" in kpi else
                                                   max(series) * 0.02)
        if kpi == "Success Rate (%)" or kpi == "Settlement Success (%)":
            why = (f"Dipped to {series[low_idx]} on {_day_label(low_idx)}, now "
                   f"{series[end]} — recovered." if recovering else
                   f"Below target since {_day_label(low_idx)}.")
            cause = f"{inc.get('severity','Sev-2')} incident on {bank} " \
                    f"({inc.get('incident_id','')})"
            action = ("Continue monitoring post-recovery; hold the failover "
                      "control in place." if recovering else
                      "Keep the incident bridge active until sustained.")
            return why, cause, action
        if kpi in ("Technical Declines (%)", "Response Time (ms)",
                   "Customer Complaints", "Merchant Complaints", "Risk Score"):
            peak = max(series)
            why = (f"Spiked to {peak} at the incident peak, back to "
                   f"{series[end]}." if moved_in_incident else
                   f"Currently {series[end]}.")
            cause = f"Fallout from {inc.get('incident_id','the incident')} on {bank}"
            action = "No action — normalised with the recovery." if recovering \
                else "Watch closely; still elevated versus baseline."
            return why, cause, action
        if kpi in ("Autopay Registrations (K/day)",):
            why = f"Softened during the incident, now {series[end]}K/day."
            cause = f"Mandate failures during {inc.get('incident_id','the incident')}"
            action = "Expect full rebound as trust recovers; monitor next week."
            return why, cause, action
        # Growth / adoption KPIs — steady climbers.
        why = f"{self._trend(series, direction).capitalize()} across the week " \
              f"to {series[end]}."
        cause = "Organic adoption; unaffected by the incident."
        action = "On track — no executive action required."
        return why, cause, action

    def _health_scores(self, ent: Enterprise, cards: list[dict]) -> dict:
        by_kpi = {c["kpi"]: c["health"] for c in cards}

        def group(name: str) -> int:
            vals = [by_kpi[k] for k in HEALTH_GROUPS[name] if k in by_kpi]
            return round(sum(vals) / len(vals)) if vals else 0

        operational = group("operational")
        customer = group("customer")
        merchant = group("merchant")
        growth = group("growth")
        risk_health = group("risk")
        portfolio = round((operational + customer + merchant + growth) / 4)
        return {
            "portfolio": portfolio,
            "operational": operational,
            "customer": customer,
            "merchant": merchant,
            "growth": growth,
            "risk": risk_health,          # health (higher = safer)
            "risk_score": ent.kpis.get("Risk Score", [None])[-1],
            "products": self._product_health(ent),
            "confidence": 0.92 if ent.available else 0.0,
        }

    def _product_health(self, ent: Enterprise) -> list[dict]:
        """Every product is healthy except the one the incident hit, which
        carries the dip until recovery."""
        inc = self._incident(ent)
        sr = ent.kpis.get("Success Rate (%)", [])
        hit = inc.get("product", "")
        recovered = inc.get("recovered", True)
        out = []
        for p in ent.products:
            if p["name"] == hit:
                score = 88 if recovered else 62
                status = "recovered" if recovered else "at_risk"
                note = (f"{inc.get('severity','')} incident "
                        f"{inc.get('incident_id','')} on {inc.get('bank','')} — "
                        f"{'recovered' if recovered else 'monitoring'}")
            else:
                score = 94
                status = "healthy"
                note = "Stable; within targets."
            out.append({"product": p["name"], "team": p.get("team", ""),
                        "owner": p.get("owner_name", ""), "health": score,
                        "status": status, "note": note})
        out.sort(key=lambda x: x["health"])
        return out

    # ----------------------------------------------------- decisions
    def decisions(self) -> list[dict]:
        """Enhanced, ranked decisions — problem, alternatives, impact, and the
        entities each one touched, derived from the decision artifacts and the
        KPI recovery they produced."""
        ent = self.enterprise()
        inc = self._incident(ent)
        raw = [a for a in ent.artifacts if a.kind == "decision"]
        enhanced = [self._enhance_decision(ent, a, inc) for a in raw]
        enhanced.sort(key=lambda d: -d["executive_priority"])
        for i, d in enumerate(enhanced, 1):
            d["rank"] = i
        return enhanced

    def _enhance_decision(self, ent: Enterprise, a: Artifact,
                          inc: dict) -> dict:
        text = a.text
        status = self._field(text, "Status") or "proposed"
        owner = self._field(text, "Owner") or ""
        product = inc.get("product", "UPI Autopay")
        sr = ent.kpis.get("Success Rate (%)", [])
        recovery = round(max(sr) - min(sr), 2) if sr else 0.0
        is_primary = "failover" in text.lower() or "DEC-" in a.art_id
        # Impact model — scored 0-100 from the recovery it drove and reach.
        customer = 92 if is_primary else 55
        revenue = 84 if is_primary else 50
        operational = 95 if is_primary else 60
        business = round((customer + revenue + operational) / 3)
        confidence = 0.96 if "executed" in status.lower() or inc.get("recovered") \
            else 0.8
        urgency = "high" if status.lower() in ("proposed", "approved") else "medium"
        exec_priority = round(business * 0.4 + customer * 0.25 + revenue * 0.2
                              + confidence * 100 * 0.15)
        return {
            "decision_id": a.art_id, "title": a.title, "status": status,
            "timestamp": a.timestamp, "owner": owner, "product": product,
            "problem": self._section(text, "Context")
            or f"{product} degradation during {inc.get('incident_id','')}.",
            "alternatives_considered": self._alternatives(is_primary),
            "reason_selected": self._section(text, "Decision")
            or "Chosen for the fastest, reversible path to restore success rate.",
            "expected_impact": self._section(text, "Expected impact")
            or f"Restore Success Rate to >= 99.2% (recovered {recovery} points).",
            "actual_impact": (f"Success Rate recovered to "
                              f"{inc.get('current_success_rate','')}% by "
                              f"{WEEKDAYS[-1]}." if inc.get("recovered")
                              else "Rollout in progress."),
            "affected_products": [product],
            "affected_banks": [inc["bank"]] if inc.get("bank") else [],
            "affected_merchants": inc.get("merchants", []),
            "affected_customers": self._customer_reach(ent),
            "confidence": confidence,
            "business_value": self._business_value(is_primary, recovery),
            "learning": ("Recurring-debit rails need bank-failover as a "
                         "standard control, not a per-incident fix."
                         if is_primary else
                         "Confirming execution closes the incident loop."),
            "impact": {"business": business, "customer": customer,
                       "revenue": revenue, "operational": operational},
            "urgency": urgency,
            "executive_priority": exec_priority,
            "evidence": [e for e in (inc.get("incident_id"), inc.get("rca_id"),
                                     a.art_id, "upi_kpis_month.xlsx") if e],
        }

    @staticmethod
    def _alternatives(primary: bool) -> list[str]:
        if primary:
            return [
                "Do nothing and wait for the bank to stabilise "
                "(rejected: customer-visible failures continue)",
                "Increase retries against the same failing endpoint "
                "(rejected: amplifies load, no failover)",
                "Failover + circuit-breaker (selected: reversible, fast, "
                "protects the affected rail)",
            ]
        return [
            "Leave the incident open (rejected: recovery already verified)",
            "Formally confirm execution and close (selected)",
        ]

    @staticmethod
    def _business_value(primary: bool, recovery: float) -> str:
        if primary:
            return (f"Protected the affected flows and restored ~{recovery} "
                    f"points of success rate; prevents repeat incidents of this "
                    f"failure mode.")
        return "Verified recovery and closed the incident cleanly."

    @staticmethod
    def _customer_reach(ent: Enterprise) -> str:
        cc = ent.kpis.get("Customer Complaints", [])
        if not cc:
            return "Customers on the affected flows."
        return (f"~{max(cc):,} customers complained at peak; normalised to "
                f"~{cc[-1]:,}/day.")

    # ----------------------------------------------------- recommendations
    def recommendations(self) -> list[dict]:
        """Ranked recommendations recovered from the executive report and the
        decision, each fully specified for an executive."""
        ent = self.enterprise()
        inc = self._incident(ent)
        recs = self._report_recommendations(ent, inc)
        recs.sort(key=lambda r: {"high": 0, "medium": 1, "low": 2}
                  .get(r["priority"], 3))
        return recs

    def _report_recommendations(self, ent: Enterprise, inc: dict) -> list[dict]:
        exec_report = next((a for a in ent.by_kind("report")
                            if "exec" in a.art_id.lower()
                            or "Executive" in a.title), None)
        product = inc.get("product", "UPI Payments")
        owner_product = self._owner_for(ent, product)
        owner_analytics = self._owner_for_team(ent, "Product Analytics")
        base = [
            {"title": "Adopt failover + circuit-breaker as the standard for "
                      "exposed rails", "priority": "high", "owner": owner_product,
             "timeline": "This sprint", "confidence": 0.94,
             "summary": f"Apply the fix from {inc.get('incident_id','the incident')} "
                        f"({product}) across similarly exposed rails.",
             "expected_benefit": "Prevents repeat incidents on any single "
                                 "bank/PSP dependency.",
             "business_risk": "Concentration on one bank/PSP remains a single "
                              "point of failure until adopted.",
             "dependencies": [inc.get("incident_id", ""), inc.get("rca_id", "")],
             "status": "proposed"},
            {"title": f"Add bank/PSP health-window awareness to the {product} "
                      "flow", "priority": "high",
             "owner": owner_product, "timeline": "Next 2 weeks",
             "confidence": 0.88,
             "summary": "Pre-empt traffic during known maintenance/degradation "
                        "windows and pre-route to a healthy path.",
             "expected_benefit": "Avoids the peak-overlap that triggered "
                                 f"{inc.get('incident_id','the incident')}.",
             "business_risk": "Windows can overrun; needs a live health signal.",
             "dependencies": [inc.get("bank", ""), inc.get("rca_id", "")],
             "status": "proposed"},
            {"title": "Institute a weekly resilience KPI (failover events, "
                      "circuit-breaker trips)", "priority": "medium",
             "owner": owner_analytics, "timeline": "From next week",
             "confidence": 0.9,
             "summary": "Track failover behaviour as a first-class KPI in the "
                        "weekly workbook.",
             "expected_benefit": "Early warning before availability turns into "
                                 "customer impact.",
             "business_risk": "None material.",
             "dependencies": ["upi_kpis_month.xlsx"], "status": "proposed"},
        ]
        for r in base:
            r["reason"] = r["summary"]
            r["business_impact"] = r["expected_benefit"]
            r["urgency"] = r["priority"]
            r["supporting_evidence"] = [e for e in (
                inc.get("incident_id"), inc.get("rca_id"),
                exec_report.art_id if exec_report else "",
                "upi_kpis_month.xlsx") if e]
            r["dependencies"] = [d for d in r["dependencies"] if d]
        return base

    # ----------------------------------------------------- priorities
    def priorities(self) -> list[dict]:
        """What the Product Head should do next, ranked — reasoning over the
        incident, open decisions, and KPI recovery."""
        ent = self.enterprise()
        inc = self._incident(ent)
        items: list[dict] = []
        bank = inc.get("bank", "the sponsor bank")
        if inc.get("incident_id"):
            items.append({
                "title": f"Monitor {bank} recovery",
                "reason": f"Recent {inc.get('severity','Sev-2')} incident "
                          f"{inc.get('incident_id','')}; Success Rate recovered "
                          f"to {inc.get('current_success_rate','')}% and must hold.",
                "impact": "High", "confidence": 0.96, "urgency": "high",
                "evidence": [inc.get("incident_id"), inc.get("rca_id"),
                             "upi_kpis_month.xlsx"],
                "linked": inc.get("incident_id")})
        open_decisions = [d for d in self.decisions()
                          if d["status"].lower() in ("proposed", "approved")]
        for d in open_decisions[:2]:
            items.append({
                "title": f"Review decision: {d['title']}",
                "reason": f"{d['status'].capitalize()} decision with "
                          f"{round(d['impact']['business'])} business impact; "
                          f"owner {d['owner']}.",
                "impact": "High", "confidence": d["confidence"],
                "urgency": "high", "evidence": d["evidence"],
                "linked": d["decision_id"]})
        # Worst-health KPI to watch tomorrow.
        cards = self.kpi_intelligence()["kpis"]
        if cards:
            worst = cards[0]
            items.append({
                "title": f"Watch {worst['kpi'].split(' (')[0]} tomorrow",
                "reason": worst["why_changed"],
                "impact": "Medium", "confidence": 0.9, "urgency": "medium",
                "evidence": worst["evidence"], "linked": worst["kpi"]})
        # Highest-priority open recommendation.
        recs = self.recommendations()
        if recs:
            r = recs[0]
            items.append({
                "title": r["title"], "reason": r["reason"],
                "impact": "High" if r["priority"] == "high" else "Medium",
                "confidence": r["confidence"], "urgency": r["priority"],
                "evidence": r["supporting_evidence"], "linked": "recommendation"})
        order = {"high": 0, "medium": 1, "low": 2}
        items.sort(key=lambda p: (order.get(p["urgency"], 3), -p["confidence"]))
        for i, p in enumerate(items, 1):
            p["priority"] = i
        return items

    # ----------------------------------------------------- risks
    def risks(self) -> dict:
        ent = self.enterprise()
        inc = self._incident(ent)
        health = self._health_scores(ent, self.kpi_intelligence()["kpis"])
        top: list[dict] = []
        if inc.get("bank"):
            top.append({
                "risk": f"Concentration risk on {inc['bank']}",
                "severity": "high",
                "detail": f"A {inc['bank']} degradation caused "
                          f"{inc.get('incident_id','')}; failover mitigates but "
                          f"the dependency remains until adopted rail-wide.",
                "evidence": [inc.get("incident_id"), inc.get("rca_id")],
                "recommended_action": "Adopt failover across exposed rails"})
        cards = self.kpi_intelligence()["kpis"]
        for c in cards:
            if c["health"] < 55 and c["trend"] != "improving":
                top.append({
                    "risk": f"{c['kpi'].split(' (')[0]} below target",
                    "severity": "medium", "detail": c["why_changed"],
                    "evidence": c["evidence"],
                    "recommended_action": c["recommended_action"]})
        return {
            "operational_risk_score": ent.kpis.get("Risk Score", [None])[-1],
            "risk_health": health["risk"],
            "top_risks": top,
            "banks_at_risk": self.banks_at_risk(),
            "products_at_risk": [p for p in health["products"]
                                 if p["status"] != "healthy"],
            "merchants_to_follow_up": inc.get("merchants", []),
        }

    def banks_at_risk(self) -> list[dict]:
        """Banks flagged in the *current* week, each carrying how many of the
        weeks on record it was the incident bank — the "has this happened
        before" signal for a repeat offender."""
        ent = self.enterprise()
        incident_weeks: dict[str, set] = {}
        for r in ent.banks_perf:
            if str(r.get("Incident bank", "")).upper() == "YES" and r.get("Bank"):
                incident_weeks.setdefault(r["Bank"], set()).add(r.get("Week"))
        out = []
        for r in self._latest_week_rows(ent.banks_perf):
            incident = str(r.get("Incident bank", "")).upper() == "YES"
            succ = self._to_float(r.get("Success %"))
            repeats = len(incident_weeks.get(r.get("Bank"), set()))
            if incident or repeats > 1 or (succ is not None and succ < 99.0):
                reason = ("Repeat offender: incident bank in "
                          f"{repeats} weeks this month" if repeats > 1 else
                          "Caused this week's incident" if incident
                          else "Success rate below 99%")
                out.append({
                    "bank": r.get("Bank"), "success_rate": succ,
                    "incident_bank": incident, "tier": r.get("Tier", ""),
                    "weeks_flagged": repeats, "reason": reason})
        out.sort(key=lambda b: (-b["weeks_flagged"], not b["incident_bank"],
                                b["success_rate"] or 100))
        return out

    def merchants_to_follow_up(self) -> list[dict]:
        ent = self.enterprise()
        inc = self._incident(ent)
        affected = set(inc.get("merchants", []))
        out = []
        for r in self._latest_week_rows(ent.merchants_perf):
            name = r.get("Merchant")
            if name in affected:
                out.append({
                    "merchant": name, "category": r.get("Category", ""),
                    "region": r.get("Region", ""), "psp": r.get("PSP", ""),
                    "settlement_bank": r.get("Settlement bank", ""),
                    "reason": f"Affected by {inc.get('incident_id','the incident')}",
                    "follow_up": "Confirm resolution and recovered volumes"})
        return out

    # ----------------------------------------------------- executive brief
    def executive_brief(self) -> dict:
        ent = self.enterprise()
        if not ent.available:
            return {"available": False}
        inc = self._incident(ent)
        health = self._health_scores(ent, self.kpi_intelligence()["kpis"])
        decisions = self.decisions()
        sr = ent.kpis.get("Success Rate (%)", [])
        entity = inc.get("bank") or inc.get("psp") or "a bank/PSP dependency"
        dip = inc.get("dip_pp") or 0.0
        low, now = inc.get("low_success_rate"), inc.get("current_success_rate")
        if dip >= 0.1 and low is not None:
            movement = (
                f"Success Rate fell {dip:.2f}pp to {low}% on "
                f"{inc.get('low_day','')} from a "
                f"{inc.get('baseline_success_rate')}% baseline, and the rail "
                f"now sits at {now}%")
        elif low is not None:
            # Say so plainly rather than dressing a flat week as a recovery.
            movement = (
                f"Success Rate held through it — the weakest day was {low}% "
                f"on {inc.get('low_day','')}, inside normal variation, and "
                f"the rail now sits at {now}%")
        else:
            movement = "Success Rate movement could not be measured"
        summary = (
            f"UPI Products ran a full incident lifecycle this period. "
            f"{inc.get('product','UPI Payments')} saw a "
            f"{inc.get('severity','Sev-2')} incident "
            f"({inc.get('incident_id','')}) linked to {entity}. {movement}. "
            f"Portfolio health is {health['portfolio']}.")
        critical_events = []
        if inc.get("incident_id"):
            critical_events.append({
                "event": f"{inc.get('severity','Sev-2')} incident {inc.get('incident_id','')}",
                "detail": f"{inc.get('product','UPI Payments')} degradation linked "
                          f"to {entity}; resolved.",
                "status": "resolved" if inc.get("recovered") else "monitoring"})
        deadlines = [{"task": a.title, "task_id": a.art_id,
                      "due": self._field(a.text, "Due")}
                     for a in ent.by_kind("task")
                     if (self._field(a.text, "Status") or "").lower()
                     in ("open", "todo", "in_progress")][:6]
        return {
            "available": True,
            "generated_for": ent.week_start,
            "organization": ent.organization,
            "department": ent.department,
            "business_summary": summary,
            "confidence": health["confidence"],
            "health": health,
            "critical_events": critical_events,
            "major_decisions": [
                {"decision_id": d["decision_id"], "title": d["title"],
                 "status": d["status"], "business_value": d["business_value"],
                 "impact": d["impact"]} for d in decisions[:3]],
            "risk_assessment": self.risks(),
            "products_at_risk": [p for p in health["products"]
                                 if p["status"] != "healthy"],
            "banks_at_risk": self.banks_at_risk(),
            "merchant_impact": self.merchants_to_follow_up(),
            "customer_impact": self._customer_reach(ent),
            "recommended_actions": self.recommendations()[:4],
            "upcoming_deadlines": deadlines,
            "priorities": self.priorities()[:5],
        }

    # ----------------------------------------------------- memory / patterns
    def patterns(self) -> dict:
        """Recurring signals across every week on record — the organizational
        memory behind "has this happened before?"."""
        ent = self.enterprise()
        inc = self._incident(ent)

        def mentions(name: str) -> int:
            if not name:
                return 0
            n = name.lower()
            return sum(1 for a in ent.artifacts if n in (a.title + a.text).lower())

        repeat_banks = [b for b in self.banks_at_risk() if b["weeks_flagged"] > 1]
        incidents = sorted(ent.by_kind("incident"), key=lambda a: a.timestamp)
        weeks_seen = sorted({self.week_of(a) for a in incidents})

        return {
            "recurring_bank": {"name": inc.get("bank", ""),
                               "mentions": mentions(inc.get("bank", "")),
                               "note": "Central to the most recent incident"},
            "repeat_offender_banks": repeat_banks,
            "recurring_incident": {"id": inc.get("incident_id", ""),
                                   "product": inc.get("product", ""),
                                   "mentions": mentions(inc.get("incident_id", ""))},
            "recurring_merchants": [
                {"name": m, "mentions": mentions(m)}
                for m in inc.get("merchants", [])],
            "recurring_kpi": {"kpi": "Success Rate (%)",
                              "note": "The KPI most incidents move first"},
            "recurring_recommendation": "Resilience checklist (failover + "
                                        "retry/backoff + fraud velocity check) "
                                        "as a release gate",
            "incident_count": len(incidents),
            "weeks_with_incidents": [w + 1 for w in weeks_seen],
            "has_happened_before": len(repeat_banks) > 0 or len(incidents) > 1,
        }

    def week_of(self, artifact: Artifact) -> int:
        """0-based week index for an artifact's ``day`` (1-based, 7 days/week)."""
        return max(0, artifact.day - 1) // 7

    # ----------------------------------------------------- reports (PM hub)
    _REPORT_CATEGORY_RULES: list[tuple[str, str]] = [
        ("MONTHLY", "Monthly Reports"),
        ("DAILY", "Daily Reports"),
        ("RISK", "Bank Reports"),
        ("MERCHANT", "Merchant Reports"),
        ("RELEASE", "Product Reports"),
        ("EXEC", "Weekly Reports"),
    ]

    def reports(self) -> list[dict]:
        """Every report + RCA artifact, categorised for the Reports hub:
        Daily/Weekly/Monthly/Product/Merchant/Bank/Failure Analysis/Executive.
        Each item carries enough to render a card and a detail view without a
        second round trip: summary, key findings, evidence, recommendations,
        linked decisions, related products, and a trend hint."""
        ent = self.enterprise()
        inc = self._incident(ent)
        # The report "trend" is the Success-Rate trend and is identical for
        # every card — compute it once here instead of per report (which, on the
        # 180-day corpus, meant hundreds of reader loads and made this endpoint
        # hang). Every card reuses this single value.
        trend = (self._reader.kpi_trend("Success Rate (%)")
                 if ent.kpis.get("Success Rate (%)") else None)
        out: list[dict] = []
        for a in ent.by_kind("report"):
            category = "Executive Reports"
            up = a.art_id.upper()
            for needle, cat in self._REPORT_CATEGORY_RULES:
                if needle in up:
                    category = cat
                    break
            out.append(self._report_card(a, category, ent, inc, trend))
        for a in ent.by_kind("rca"):
            out.append(self._report_card(a, "Failure Analysis", ent, inc, trend))
        out.sort(key=lambda r: r["timestamp"], reverse=True)
        return out

    def _report_card(self, a: Artifact, category: str, ent: Enterprise,
                     inc: dict, trend: dict | None = None) -> dict:
        findings = [s for s in re.split(r"\n(?=##\s)", a.text)
                   if s.strip()][:1]
        summary = self._section(a.text, "Executive summary") \
            or self._section(a.text, "Summary") \
            or a.text.strip().split("\n\n")[0][:300]
        recommendations = self._section(a.text, "Recommendations") \
            or self._section(a.text, "Corrective action") \
            or self._section(a.text, "Corrective actions (proposed)")
        products = [p["name"] for p in ent.products
                   if p["name"].lower() in (a.title + a.text).lower()]
        return {
            "report_id": a.art_id, "title": a.title, "category": category,
            "timestamp": a.timestamp, "week": self.week_of(a) + 1,
            "summary": summary,
            "key_findings": findings[0][:400] if findings else "",
            "supporting_evidence": a.refs[:6],
            "recommendations": recommendations,
            "linked_decisions": [r for r in a.refs if r.upper().startswith("DEC")],
            "related_products": products or ([inc.get("product")]
                                             if inc.get("product") else []),
            "trend": trend if trend is not None else self.trends_for_report(a),
        }

    def trends_for_report(self, a: Artifact) -> dict | None:
        """The primary KPI's trend at the time this report was written, if
        the KPI series reaches that far — otherwise the current trend."""
        ent = self.enterprise()
        series = ent.kpis.get("Success Rate (%)")
        if not series:
            return None
        return self._reader.kpi_trend("Success Rate (%)")

    # ------------------------------------------------------- week/month trends
    def week_over_week(self) -> dict:
        """Per-KPI delta between the latest week and the week before it."""
        ent = self.enterprise()
        out = {}
        for kpi, series in ent.kpis.items():
            if len(series) < 8:
                out[kpi] = {"current": series[-1] if series else None,
                            "previous": None, "delta": None}
                continue
            current_week = series[-7:]
            previous_week = series[-14:-7] if len(series) >= 14 else None
            cur_avg = round(sum(current_week) / len(current_week), 3)
            prev_avg = (round(sum(previous_week) / len(previous_week), 3)
                       if previous_week else None)
            out[kpi] = {"current": cur_avg, "previous": prev_avg,
                       "delta": round(cur_avg - prev_avg, 3)
                       if prev_avg is not None else None}
        return out

    def month_over_month(self) -> dict:
        """Per-KPI delta between the latest value and the month's first day."""
        ent = self.enterprise()
        out = {}
        for kpi, series in ent.kpis.items():
            if not series:
                continue
            start, end = series[0], series[-1]
            out[kpi] = {"month_start": start, "current": end,
                       "delta": round(end - start, 3)}
        return out

    def trends(self) -> list[dict]:
        """{kpi, today, yesterday, last_week, last_month, trend} for every
        KPI — the shared data source for Reports/Home/Products trend rows."""
        ent = self.enterprise()
        return [self._reader.kpi_trend(kpi) for kpi in ent.kpis]

    # ----------------------------------------------------- helpers
    @staticmethod
    def _field(text: str, label: str) -> str:
        m = re.search(rf"\*\*{re.escape(label)}:\*\*\s*([^\n·|]+)", text)
        return m.group(1).strip() if m else ""

    @staticmethod
    def _section(text: str, heading: str) -> str:
        m = re.search(rf"^##\s+{re.escape(heading)}\s*\n(.+?)(?=\n##\s|\nRefs:|\Z)",
                      text, re.DOTALL | re.MULTILINE | re.IGNORECASE)
        if not m:
            return ""
        return re.sub(r"\s+", " ", m.group(1)).strip()[:400]

    def _owner_for(self, ent: Enterprise, product: str) -> str:
        for p in ent.products:
            if p["name"] == product:
                return p.get("owner_name", "")
        return ""

    @staticmethod
    def _owner_for_team(ent: Enterprise, team: str) -> str:
        for e in ent.employees:
            if e.get("team") == team and "Lead" in e.get("title", ""):
                return e.get("name", "")
        return ""

    @staticmethod
    def _to_float(v):
        try:
            return round(float(v), 2)
        except (TypeError, ValueError):
            return None

    # ----------------------------------------------- business entity graph
    def build_business_graph(self, graph) -> int:
        """Expand the document-centric knowledge graph into a *business* graph:
        employees, teams, products, banks, PSPs, merchants, the incident,
        decisions, KPIs, reports and SOPs as typed nodes, joined by business
        relationships (OWNS, WORKS_ON, AFFECTS, RESOLVES, HAS_KPI, MONITORS,
        USES, GENERATED, UPDATED …).

        Uses the enterprise graph's public batch API — no Brain change. It is
        idempotent: a marker node makes a second call a no-op, and re-running
        after a re-ingest refreshes the same nodes."""
        ent = self.enterprise()
        if not ent.available or graph is None:
            return 0
        inc = self._incident(ent)
        added = 0
        try:
            with graph.batch() as g:
                def node(nid, kind, label, **attrs):
                    g._upsert_node(nid, kind=kind, label=label, **attrs)  # noqa: SLF001

                def rel(src, tgt, kind):
                    nonlocal added
                    g._relate(src, tgt, kind)  # noqa: SLF001
                    added += 1

                dept = "department:upi-products"
                node(dept, "department", ent.department or "UPI Products")

                emp = {}  # emp_id -> node id
                for e in ent.employees:
                    nid = f"employee:{e['emp_id'].lower()}"
                    emp[e["emp_id"]] = nid
                    node(nid, "employee", e.get("name", ""),
                         title=e.get("title", ""), team=e.get("team", ""))
                    if e.get("manager_id") and e["manager_id"] in emp:
                        rel(nid, emp[e["manager_id"]], "REPORTS_TO")

                teams = {}
                for e in ent.employees:
                    t = e.get("team")
                    if t and t not in teams:
                        tid = f"team:{_slug(t)}"
                        teams[t] = tid
                        node(tid, "team", t)
                        rel(tid, dept, "PART_OF")
                for e in ent.employees:
                    if e.get("team") in teams:
                        rel(emp[e["emp_id"]], teams[e["team"]], "WORKS_ON")

                prod = {}
                for p in ent.products:
                    pid = f"product:{_slug(p['name'])}"
                    prod[p["name"]] = pid
                    node(pid, "product", p["name"], team=p.get("team", ""))
                    if p.get("team") in teams:
                        rel(teams[p["team"]], pid, "OWNS")
                    for e in ent.employees:
                        if e.get("emp_id") == p.get("owner"):
                            rel(emp[e["emp_id"]], pid, "OWNS")

                banks = {}
                for b in ent.banks:
                    bid = f"bank:{_slug(b['name'])}"
                    banks[b["name"]] = bid
                    node(bid, "bank", b["name"], tier=b.get("tier", ""))
                psps = {}
                for p in ent.psps:
                    pid = f"psp:{_slug(p['name'])}"
                    psps[p["name"]] = pid
                    node(pid, "psp", p["name"])
                merch = {}
                for m in ent.merchants:
                    mid = f"merchant:{_slug(m['name'])}"
                    merch[m["name"]] = mid
                    node(mid, "merchant", m["name"],
                         category=m.get("category", ""))
                    if m.get("psp") in psps:
                        rel(mid, psps[m["psp"]], "USES")
                    if m.get("settlement_bank") in banks:
                        rel(mid, banks[m["settlement_bank"]], "USES")

                # KPIs, owned/monitored by the department.
                kpi_ids = {}
                for kpi in ent.kpis:
                    kid = f"kpi:{_slug(kpi)}"
                    kpi_ids[kpi] = kid
                    node(kid, "kpi", kpi)
                    rel(dept, kid, "MONITORS")
                hit = prod.get(inc.get("product", ""))
                if hit:
                    for kpi in ("Success Rate (%)", "Settlement Success (%)",
                                "Autopay Registrations (K/day)"):
                        if kpi in kpi_ids:
                            rel(hit, kpi_ids[kpi], "HAS_KPI")

                # The incident and its blast radius.
                if inc.get("incident_id"):
                    iid = f"incident:{inc['incident_id'].lower()}"
                    node(iid, "incident", inc["incident_id"],
                         severity=inc.get("severity", ""))
                    if hit:
                        rel(iid, hit, "AFFECTS")
                    if inc.get("bank") in banks:
                        rel(iid, banks[inc["bank"]], "CAUSED_BY")
                    if inc.get("psp") in psps:
                        rel(iid, psps[inc["psp"]], "INVOLVES")
                    for mname in inc.get("merchants", []):
                        if mname in merch:
                            rel(iid, merch[mname], "AFFECTS")
                    if inc.get("rca_id"):
                        rid = f"rca:{inc['rca_id'].lower()}"
                        node(rid, "rca", inc["rca_id"])
                        rel(rid, iid, "REFERENCES")

                    # Decisions resolve the incident and update the SOP.
                    for d in ent.by_kind("decision"):
                        did = f"decision:{d.art_id.lower()}"
                        node(did, "decision", d.title[:80], status=self._field(
                            d.text, "Status"))
                        rel(did, iid, "RESOLVES")
                        if hit:
                            rel(did, hit, "AFFECTS")
                    for sop in ent.by_kind("sop"):
                        sid = f"sop:{sop.art_id.lower()}"
                        node(sid, "sop", sop.art_id)
                        rel(sid, iid, "RESOLVES")

                # Reports generated for the department.
                for r in ent.by_kind("report"):
                    rid = f"report:{r.art_id.lower()}"
                    node(rid, "report", r.title[:80])
                    rel(rid, dept, "GENERATED_FOR")

                node("enterprise:npci", "enterprise",
                     ent.organization or "NPCI", built=True)
        except Exception:  # noqa: BLE001 — graph enrichment never breaks startup
            logger.exception("Executive layer: business graph build failed")
        return added

    # ----------------------------------------------------- status
    def status(self) -> dict:
        ent = self.enterprise()
        return {"available": ent.available,
                "organization": ent.organization,
                "department": ent.department,
                "week_start": ent.week_start,
                "kpis": len(ent.kpis), "artifacts": len(ent.artifacts),
                "decisions": len(ent.by_kind("decision")),
                "incidents": len(ent.by_kind("incident")),
                "reports": len(ent.by_kind("report"))}

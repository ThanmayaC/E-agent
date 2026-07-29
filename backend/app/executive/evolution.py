"""EvolutionIntelligence (V8.0) — the six-month digital twin.

The V8.0 generator extends the synthetic UPI enterprise from a 35-day demo to a
continuous 180-day operating history and derives, from the same ledger/KPI
ground truth, a family of *evolution* cubes: customer lifecycle (DAU/WAU/MAU,
retention, churn, power vs dormant), feature adoption, and merchant / bank / PSP
/ product evolution; multi-granularity KPI roll-ups (weekly / monthly /
quarterly) and rolling 30- / 90-day windows; forecast validation (predicted vs
realised); executive decision tracking (expected vs actual impact, success
score, business value); cross-entity relationships; and weekly storylines.

This layer reads those cubes (via the shared :class:`EcosystemReader`) and
answers the questions a Product Manager replaying six months of history asks —
who is growing, who is churning, which PSP is losing share, which feature is
saturating, where to invest next, how accurate the forecasts were, and which
executive decisions produced measurable business value. It computes nothing the
generator did not already ground in the ledger; if the corpus has not been
generated it degrades to empty results, exactly like the other executive layers.
"""
from __future__ import annotations

from app.core.logging import get_logger
from app.executive.ecosystem import Ecosystem, EcosystemReader

logger = get_logger(__name__)


def _f(v, default: float = 0.0) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return default


def _latest_per(rows: list[dict], key: str, order_key: str) -> dict[str, dict]:
    """Latest row per entity, by the given ordering column."""
    out: dict[str, dict] = {}
    for r in rows:
        e = str(r.get(key))
        if e not in out or _f(r.get(order_key)) >= _f(out[e].get(order_key)):
            out[e] = r
    return out


def _series_per(rows: list[dict], key: str, entity: str,
                order_key: str) -> list[dict]:
    got = [r for r in rows if str(r.get(key)) == str(entity)]
    got.sort(key=lambda r: _f(r.get(order_key)))
    return got


class EvolutionIntelligence:
    """Read-only analytics over the V8.0 evolution cubes + executive Q&A."""

    def __init__(self, reader: EcosystemReader):
        self._reader = reader

    def eco(self) -> Ecosystem:
        return self._reader.load()

    @property
    def available(self) -> bool:
        return bool(self.eco().customer_evolution)

    # ----------------------------------------------------------- status
    def status(self) -> dict:
        e = self.eco()
        return {
            "available": self.available,
            "horizon_days": len(e.customer_evolution),
            "cubes": {
                "customer_evolution": len(e.customer_evolution),
                "feature_adoption": len(e.feature_adoption),
                "merchant_evolution": len(e.merchant_evolution),
                "bank_evolution": len(e.bank_evolution),
                "psp_evolution": len(e.psp_evolution),
                "product_lifecycle": len(e.product_lifecycle),
                "kpi_rollups": len(e.kpi_rollups),
                "kpi_rolling": len(e.kpi_rolling),
                "forecast_validation": len(e.forecast_validation),
                "forecast_forward": len(e.forecast_forward),
                "decision_tracking": len(e.decision_tracking),
                "cross_entity": len(e.cross_entity),
                "storylines": len(e.storylines),
            },
        }

    # -------------------------------------------------------- customers
    def customers(self) -> dict:
        e = self.eco()
        rows = e.customer_evolution
        if not rows:
            return {"available": False}
        latest = rows[-1]
        first = rows[0]
        return {
            "available": True,
            "latest": latest,
            "period": {"start": first["date"], "end": latest["date"],
                       "days": len(rows)},
            "growth": {
                "dau_m": {"start": _f(first["dau_m"]), "end": _f(latest["dau_m"])},
                "mau_m": {"start": _f(first["mau_m"]), "end": _f(latest["mau_m"])},
                "registered_base_m": {"start": _f(first["registered_base_m"]),
                                      "end": _f(latest["registered_base_m"])},
            },
            "series": rows,
        }

    # -------------------------------------------------------- merchants
    def merchants(self) -> dict:
        e = self.eco()
        rows = e.merchant_evolution
        if not rows:
            return {"available": False}
        latest = _latest_per(rows, "merchant", "month_index")
        table = sorted(latest.values(), key=lambda r: _f(r.get("txns")),
                       reverse=True)
        counts: dict[str, int] = {}
        for r in table:
            counts[r.get("status", "Active")] = counts.get(
                r.get("status", "Active"), 0) + 1
        stages: dict[str, int] = {}
        for r in table:
            stages[r.get("lifecycle_stage", "")] = stages.get(
                r.get("lifecycle_stage", ""), 0) + 1
        return {"available": True, "merchants": table,
                "status_counts": counts, "stage_counts": stages,
                "growing": [r for r in table
                            if _f(r.get("mom_growth_pct")) > 10][:5],
                "declining": [r for r in table
                              if _f(r.get("mom_growth_pct")) < -5][:5]}

    def merchant(self, name: str) -> dict:
        e = self.eco()
        series = _series_per(e.merchant_evolution, "merchant", name, "month_index")
        return {"merchant": name, "series": series,
                "available": bool(series)}

    # ------------------------------------------------------------ banks
    def banks(self) -> dict:
        e = self.eco()
        rows = e.bank_evolution
        if not rows:
            return {"available": False}
        latest = _latest_per(rows, "bank", "week_index")
        table = sorted(latest.values(),
                       key=lambda r: _f(r.get("market_share_pct")), reverse=True)
        improving, declining = [], []
        for name, last in latest.items():
            series = _series_per(rows, "bank", name, "week_index")
            if len(series) < 2:
                continue
            first = series[0]
            share_chg = round(_f(last["market_share_pct"])
                              - _f(first["market_share_pct"]), 2)
            lat_chg = round(_f(last["p95_latency_ms"])
                            - _f(first["p95_latency_ms"]), 0)
            sr_chg = round(_f(last["success_rate"])
                           - _f(first["success_rate"]), 2)
            rec = {"bank": name, "tier": last.get("tier"),
                   "market_share_pct": _f(last["market_share_pct"]),
                   "share_change_pct": share_chg,
                   "latency_change_ms": lat_chg, "sr_change_pct": sr_chg,
                   "success_rate": _f(last["success_rate"]),
                   "health_grade": last.get("health_grade"),
                   "total_incidents": sum(int(_f(r.get("incidents")))
                                          for r in series)}
            (improving if (sr_chg >= 0 and lat_chg <= 0) else declining).append(rec)
        improving.sort(key=lambda r: (r["sr_change_pct"], -r["latency_change_ms"]),
                       reverse=True)
        declining.sort(key=lambda r: r["sr_change_pct"])
        return {"available": True, "banks": table,
                "improving": improving[:5], "declining": declining[:5]}

    # ------------------------------------------------------------- psps
    def psps(self) -> dict:
        e = self.eco()
        rows = e.psp_evolution
        if not rows:
            return {"available": False}
        latest = _latest_per(rows, "psp", "week_index")
        gainers, losers = [], []
        table = []
        for name, last in latest.items():
            series = _series_per(rows, "psp", name, "week_index")
            first = series[0] if series else last
            share_chg = round(_f(last["market_share_pct"])
                              - _f(first["market_share_pct"]), 2)
            rec = {"psp": name, "sponsor_bank": last.get("sponsor_bank"),
                   "market_share_pct": _f(last["market_share_pct"]),
                   "share_change_pct": share_chg,
                   "success_rate": _f(last["success_rate"]),
                   "satisfaction": _f(last["satisfaction"]),
                   "is_market_leader": last.get("is_market_leader")}
            table.append(rec)
            (gainers if share_chg >= 0 else losers).append(rec)
        table.sort(key=lambda r: r["market_share_pct"], reverse=True)
        gainers.sort(key=lambda r: r["share_change_pct"], reverse=True)
        losers.sort(key=lambda r: r["share_change_pct"])
        return {"available": True, "psps": table,
                "gaining_share": gainers[:5], "losing_share": losers[:5]}

    # --------------------------------------------------------- products
    def products(self) -> dict:
        e = self.eco()
        rows = e.product_lifecycle
        if not rows:
            return {"available": False}
        latest = _latest_per(rows, "product", "month_index")
        table = sorted(latest.values(),
                       key=lambda r: _f(r.get("market_share_pct")), reverse=True)
        return {"available": True, "products": table,
                "saturating": [r for r in table
                               if r.get("lifecycle_stage") in
                               ("Saturation", "Maturity")
                               and _f(r.get("mom_growth_pct")) < 4],
                "investable": sorted(
                    [r for r in table
                     if r.get("lifecycle_stage") in ("Growth", "Introduction")],
                    key=lambda r: _f(r.get("mom_growth_pct")), reverse=True)}

    def product(self, name: str) -> dict:
        e = self.eco()
        series = _series_per(e.product_lifecycle, "product", name, "month_index")
        return {"product": name, "series": series, "available": bool(series)}

    def feature_adoption(self) -> dict:
        e = self.eco()
        rows = e.feature_adoption
        if not rows:
            return {"available": False}
        latest = _latest_per(rows, "feature", "month_index")
        table = sorted(latest.values(), key=lambda r: _f(r.get("share_pct")),
                       reverse=True)
        return {"available": True, "features": table,
                "saturating": [r for r in table
                               if r.get("stage") in ("Saturation", "Decline")],
                "growing": [r for r in table if r.get("stage") in
                            ("Growth", "Introduction")]}

    # ------------------------------------------------------- KPI trends
    def trends(self, grain: str = "monthly") -> dict:
        e = self.eco()
        rows = [r for r in e.kpi_rollups if r.get("grain") == grain]
        by_kpi: dict[str, list] = {}
        for r in rows:
            by_kpi.setdefault(str(r.get("kpi")), []).append(r)
        for series in by_kpi.values():
            series.sort(key=lambda r: _f(r.get("period_index")))
        return {"available": bool(rows), "grain": grain, "kpis": by_kpi}

    def trend(self, kpi: str) -> dict:
        e = self.eco()
        out = {"kpi": kpi, "grains": {}}
        for grain in ("weekly", "monthly", "quarterly"):
            series = [r for r in e.kpi_rollups
                      if r.get("kpi") == kpi and r.get("grain") == grain]
            series.sort(key=lambda r: _f(r.get("period_index")))
            out["grains"][grain] = series
        out["rolling"] = _series_per(e.kpi_rolling, "kpi", kpi, "day")
        out["available"] = bool(out["rolling"] or out["grains"]["monthly"])
        return out

    # ------------------------------------------------------- forecasts
    def forecast_accuracy(self) -> dict:
        e = self.eco()
        rows = e.forecast_validation
        if not rows:
            return {"available": False}
        accs = [_f(r.get("accuracy_pct")) for r in rows]
        hits = sum(1 for r in rows
                   if str(r.get("direction_correct")).lower() == "true")
        return {"available": True,
                "mean_accuracy_pct": round(sum(accs) / len(accs), 1),
                "direction_hit_rate_pct": round(100 * hits / len(rows), 1),
                "validations": sorted(rows, key=lambda r: _f(r.get("accuracy_pct")),
                                      reverse=True)}

    def forecast(self, kpi: str) -> dict:
        e = self.eco()
        fwd = [r for r in e.forecast_forward if r.get("kpi") == kpi]
        fwd.sort(key=lambda r: _f(r.get("horizon_day")))
        val = next((r for r in e.forecast_validation if r.get("kpi") == kpi), None)
        return {"kpi": kpi, "forward": fwd, "validation": val,
                "available": bool(fwd)}

    # ------------------------------------------------- decision tracking
    def decisions(self) -> dict:
        e = self.eco()
        rows = e.decision_tracking
        if not rows:
            return {"available": False}
        table = sorted(rows, key=lambda r: _f(r.get("business_value_cr")),
                       reverse=True)
        succ = [_f(r.get("success_score")) for r in rows]
        return {"available": True, "decisions": table,
                "count": len(rows),
                "avg_success_score": round(sum(succ) / len(succ), 1),
                "total_business_value_cr": round(
                    sum(_f(r.get("business_value_cr")) for r in rows), 1),
                "resolved": sum(1 for r in rows
                                if r.get("status") == "Resolved"),
                "top_value": table[:5]}

    def decision(self, decision_id: str) -> dict:
        e = self.eco()
        rec = next((r for r in e.decision_tracking
                    if r.get("decision_id") == decision_id), None)
        return {"decision": rec, "available": rec is not None}

    # --------------------------------------------------- cross-entity
    def cross_entity(self, entity: str | None = None) -> dict:
        e = self.eco()
        rows = e.cross_entity
        if entity:
            rows = [r for r in rows if entity.lower() in
                    (str(r.get("source", "")).lower(),
                     str(r.get("target", "")).lower())
                    or entity.lower() in str(r.get("source", "")).lower()
                    or entity.lower() in str(r.get("target", "")).lower()]
        return {"available": bool(e.cross_entity), "relationships": rows}

    # ------------------------------------------------------ storylines
    def stories(self) -> dict:
        e = self.eco()
        rows = e.storylines
        if not rows:
            return {"available": False}
        by_week: dict[int, dict] = {}
        for r in rows:
            w = int(_f(r.get("week")))
            wk = by_week.setdefault(w, {"week": w, "week_start": r.get("week_start"),
                                        "has_incident": r.get("has_incident"),
                                        "steps": []})
            wk["steps"].append(r)
        weeks = [by_week[w] for w in sorted(by_week)]
        for wk in weeks:
            wk["steps"].sort(key=lambda r: _f(r.get("step_no")))
        return {"available": True, "weeks": weeks}

    def story(self, week: int) -> dict:
        s = self.stories()
        if not s.get("available"):
            return {"available": False}
        wk = next((w for w in s["weeks"] if w["week"] == week), None)
        return {"available": wk is not None, "week": wk}

    # =====================================================================
    # Executive workspace Q&A — routes a natural question to the right
    # evolution surface and returns an evidence-backed answer.
    # =====================================================================
    def ask(self, question: str) -> dict:
        q = (question or "").lower().strip()
        if not q:
            return {"question": question, "answer": "Ask about growth, churn, "
                    "banks, PSPs, features, forecasts or decisions.",
                    "topic": "help"}
        if not self.available:
            return {"question": question, "available": False,
                    "answer": "The six-month evolution corpus has not been "
                              "generated yet."}

        def resp(topic, answer, evidence, data):
            return {"question": question, "topic": topic, "available": True,
                    "answer": answer, "evidence": evidence, "data": data}

        # transaction value / volume increase → growth drivers
        if (("value" in q or "volume" in q or "transaction" in q or "grow" in q)
                and ("increase" in q or "why" in q or "driv" in q or "up" in q)):
            feats = self.feature_adoption().get("growing", [])[:3]
            cust = self.customers()
            base = cust.get("growth", {}).get("registered_base_m", {})
            names = ", ".join(f"{f['feature']} ({f.get('mom_growth_pct')}% m/m)"
                              for f in feats) or "broad-based adoption"
            return resp("growth",
                        f"Transaction value is rising on the back of {names}, "
                        f"with the registered base growing from "
                        f"{base.get('start')}M to {base.get('end')}M over the "
                        f"six months.", ["feature_adoption", "customer_evolution"],
                        {"drivers": feats, "user_base": base})

        # which banks are improving
        if "bank" in q and ("improv" in q or "better" in q or "best" in q):
            b = self.banks()
            imp = b.get("improving", [])
            names = ", ".join(f"{r['bank']} (SR {r['sr_change_pct']:+}%, "
                              f"latency {r['latency_change_ms']:+.0f}ms)"
                              for r in imp[:3]) or "no clear improvers"
            return resp("banks_improving",
                        f"Improving banks: {names}.",
                        ["bank_evolution"], {"improving": imp})

        # which PSP is losing market share
        if "psp" in q and ("los" in q or "declin" in q or "share" in q):
            p = self.psps()
            los = p.get("losing_share", [])
            if "gain" in q or "grow" in q:
                los = p.get("gaining_share", [])
            names = ", ".join(f"{r['psp']} ({r['share_change_pct']:+}%)"
                              for r in los[:3]) or "none materially"
            return resp("psp_share",
                        f"PSP share movement: {names}.",
                        ["psp_evolution"], {"movers": los})

        # feature approaching saturation
        if "featur" in q and ("saturat" in q or "matur" in q or "plateau" in q):
            f = self.feature_adoption()
            sat = f.get("saturating", [])
            names = ", ".join(f"{r['feature']} ({r.get('share_pct')}% share, "
                              f"{r.get('mom_growth_pct')}% m/m, {r.get('stage')})"
                              for r in sat[:3]) or "none yet"
            return resp("saturation",
                        f"Features approaching saturation: {names}.",
                        ["feature_adoption"], {"saturating": sat})

        # where should product invest next
        if "invest" in q or "where" in q or "opportunit" in q:
            prod = self.products().get("investable", [])[:3]
            feats = self.feature_adoption().get("growing", [])[:3]
            names = ", ".join(f"{r['product']} ({r.get('mom_growth_pct')}% m/m, "
                              f"{r.get('lifecycle_stage')})" for r in prod) \
                or "the fastest-growing features"
            return resp("investment",
                        f"Highest-headroom bets: {names} — still in "
                        f"growth/introduction with room to scale.",
                        ["product_lifecycle", "feature_adoption"],
                        {"products": prod, "features": feats})

        # which decision / recommendation generated business value
        if ("decision" in q or "recommend" in q or "value" in q):
            d = self.decisions()
            top = d.get("top_value", [])
            names = "; ".join(f"{r['decision_id']} ({r['title']}, "
                              f"₹{r['business_value_cr']}cr, "
                              f"success {r['success_score']})" for r in top[:3])
            return resp("decision_value",
                        f"Decisions with measurable value: {names}. Total "
                        f"protected value ₹{d.get('total_business_value_cr')}cr "
                        f"across {d.get('count')} tracked decisions.",
                        ["decision_tracking"], {"top": top,
                                                "summary": {k: d.get(k) for k in
                                                            ("avg_success_score",
                                                             "total_business_value_cr",
                                                             "resolved", "count")}})

        # forecast accuracy
        if "forecast" in q or "predict" in q or "accura" in q:
            fa = self.forecast_accuracy()
            return resp("forecast_accuracy",
                        f"Backtested forecast accuracy averages "
                        f"{fa.get('mean_accuracy_pct')}% with a "
                        f"{fa.get('direction_hit_rate_pct')}% direction hit rate.",
                        ["forecast_validation"], fa)

        # churn / retention
        if "churn" in q or "retention" in q or "dormant" in q:
            c = self.customers()
            last = c.get("latest", {})
            return resp("retention",
                        f"Latest retention {last.get('retention_pct')}% "
                        f"(churn {last.get('churn_pct')}%); "
                        f"{last.get('power_users_m')}M power vs "
                        f"{last.get('dormant_users_m')}M dormant users.",
                        ["customer_evolution"], {"latest": last})

        return resp("overview",
                    "I can answer on growth drivers, improving banks, PSP share, "
                    "feature saturation, investment priorities, decision value, "
                    "forecast accuracy and churn/retention.",
                    [], {"topics": ["growth", "banks", "psps", "features",
                                    "invest", "decisions", "forecast", "churn"]})

    # ----------------------------------------------------------- summary
    def overview(self) -> dict:
        """A compact evolution dashboard: user base, entity movers, decisions."""
        if not self.available:
            return {"available": False}
        cust = self.customers()
        return {
            "available": True,
            "period": cust.get("period"),
            "users": cust.get("latest"),
            "user_growth": cust.get("growth"),
            "banks_improving": self.banks().get("improving", [])[:3],
            "psps_losing_share": self.psps().get("losing_share", [])[:3],
            "features_saturating": self.feature_adoption().get("saturating", [])[:3],
            "products_investable": self.products().get("investable", [])[:3],
            "decisions": {k: self.decisions().get(k) for k in
                          ("count", "avg_success_score",
                           "total_business_value_cr", "resolved")},
            "forecast_accuracy": self.forecast_accuracy().get("mean_accuracy_pct"),
        }

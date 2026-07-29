"""EcosystemIntelligence (V7.0) — analytics over the simulated UPI ecosystem.

The V7.0 generator writes a sampled transaction ledger and rolls it up into
aggregate *cubes* under ``enterprise_data/master/analytics/`` (daily_metrics,
feature_daily, bank_daily, psp_daily, merchant_daily, city_daily,
hourly_distribution, transaction_mix, customer_activity, trends, bi_findings,
forecasts). This layer reads those cubes and answers the ecosystem questions a
Product Manager asks — compare features / banks / PSPs, market share and its
trend, growth leaders, per-feature analytics, city trends, hourly distribution,
transaction mix, anomalies and forecasts.

It computes nothing the generator did not already ground in the ledger; it only
reshapes the cubes for the dashboard and the Brain. If the corpus has not been
generated it degrades to empty results, exactly like :class:`EnterpriseReader`.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

from app.core.logging import get_logger

logger = get_logger(__name__)


def _num(v):
    """Coerce a CSV cell to int/float where possible, else return as-is."""
    if v is None or v == "":
        return None
    try:
        f = float(v)
        return int(f) if f.is_integer() else round(f, 4)
    except (TypeError, ValueError):
        return v


@dataclass
class Ecosystem:
    daily_metrics: list[dict] = field(default_factory=list)
    feature_daily: list[dict] = field(default_factory=list)
    bank_daily: list[dict] = field(default_factory=list)
    psp_daily: list[dict] = field(default_factory=list)
    merchant_daily: list[dict] = field(default_factory=list)
    city_daily: list[dict] = field(default_factory=list)
    hourly: list[dict] = field(default_factory=list)
    mix: list[dict] = field(default_factory=list)
    customer_activity: list[dict] = field(default_factory=list)
    trends: list[dict] = field(default_factory=list)
    bi: list[dict] = field(default_factory=list)
    forecasts: list[dict] = field(default_factory=list)
    # V8.0 six-month evolution cubes.
    customer_evolution: list[dict] = field(default_factory=list)
    feature_adoption: list[dict] = field(default_factory=list)
    merchant_evolution: list[dict] = field(default_factory=list)
    bank_evolution: list[dict] = field(default_factory=list)
    psp_evolution: list[dict] = field(default_factory=list)
    product_lifecycle: list[dict] = field(default_factory=list)
    kpi_rollups: list[dict] = field(default_factory=list)
    kpi_rolling: list[dict] = field(default_factory=list)
    forecast_validation: list[dict] = field(default_factory=list)
    forecast_forward: list[dict] = field(default_factory=list)
    decision_tracking: list[dict] = field(default_factory=list)
    cross_entity: list[dict] = field(default_factory=list)
    storylines: list[dict] = field(default_factory=list)

    @property
    def available(self) -> bool:
        return bool(self.daily_metrics)


class EcosystemReader:
    """Loads the analytics cubes as lists of dicts, cached by corpus mtime so a
    regenerated or re-ingested corpus is picked up without a restart."""

    _CUBES = ["daily_metrics", "feature_daily", "bank_daily", "psp_daily",
              "merchant_daily", "city_daily", "hourly_distribution",
              "transaction_mix", "customer_activity", "trends", "bi_findings",
              "forecasts", "customer_evolution", "feature_adoption",
              "merchant_evolution", "bank_evolution", "psp_evolution",
              "product_lifecycle", "kpi_rollups", "kpi_rolling",
              "forecast_validation", "forecast_forward", "decision_tracking",
              "cross_entity", "storylines"]

    def __init__(self, enterprise_dir: Path):
        self._analytics = Path(enterprise_dir) / "master" / "analytics"

    def load(self) -> Ecosystem:
        if not self._analytics.exists():
            return Ecosystem()
        try:
            return self._load(self._mtime())
        except Exception:  # noqa: BLE001 — never break the app
            logger.exception("Ecosystem layer: reading the cubes failed")
            return Ecosystem()

    def _mtime(self) -> float:
        latest = 0.0
        for p in self._analytics.glob("*.csv"):
            latest = max(latest, p.stat().st_mtime)
        return latest

    @lru_cache(maxsize=4)
    def _load(self, _sig: float) -> Ecosystem:
        def rows(name: str) -> list[dict]:
            path = self._analytics / f"{name}.csv"
            if not path.exists():
                return []
            with path.open(encoding="utf-8") as f:
                return [{k: _num(v) for k, v in r.items()}
                        for r in csv.DictReader(f)]
        return Ecosystem(
            daily_metrics=rows("daily_metrics"),
            feature_daily=rows("feature_daily"),
            bank_daily=rows("bank_daily"),
            psp_daily=rows("psp_daily"),
            merchant_daily=rows("merchant_daily"),
            city_daily=rows("city_daily"),
            hourly=rows("hourly_distribution"),
            mix=rows("transaction_mix"),
            customer_activity=rows("customer_activity"),
            trends=rows("trends"),
            bi=rows("bi_findings"),
            forecasts=rows("forecasts"),
            customer_evolution=rows("customer_evolution"),
            feature_adoption=rows("feature_adoption"),
            merchant_evolution=rows("merchant_evolution"),
            bank_evolution=rows("bank_evolution"),
            psp_evolution=rows("psp_evolution"),
            product_lifecycle=rows("product_lifecycle"),
            kpi_rollups=rows("kpi_rollups"),
            kpi_rolling=rows("kpi_rolling"),
            forecast_validation=rows("forecast_validation"),
            forecast_forward=rows("forecast_forward"),
            decision_tracking=rows("decision_tracking"),
            cross_entity=rows("cross_entity"),
            storylines=rows("storylines"),
        )


def _sum(rows: list[dict], key: str) -> float:
    return float(sum((r.get(key) or 0) for r in rows))


def _totals(rows: list[dict], entity_key: str) -> dict[str, dict]:
    """Month totals per entity from a *_daily cube (txns/value + avg success)."""
    out: dict[str, dict] = {}
    for r in rows:
        e = r.get(entity_key)
        if e is None:
            continue
        agg = out.setdefault(str(e), {"txns": 0.0, "value": 0.0, "sr": [],
                                      "category": r.get("category")})
        agg["txns"] += float(r.get("txns") or 0)
        agg["value"] += float(r.get("value") or 0)
        if r.get("success_rate") is not None:
            agg["sr"].append(float(r["success_rate"]))
    return out


class EcosystemIntelligence:
    """Read-only analytics over the ecosystem cubes."""

    def __init__(self, reader: EcosystemReader):
        self._reader = reader

    def ecosystem(self) -> Ecosystem:
        return self._reader.load()

    @property
    def available(self) -> bool:
        return self.ecosystem().available

    # ------------------------------------------------------------- helpers
    def _growth(self, prefix: str) -> dict[str, float]:
        return {t["series"].split("::", 1)[1]: (t.get("growth_pct") or 0.0)
                for t in self.ecosystem().trends
                if str(t.get("series", "")).startswith(prefix)}

    @staticmethod
    def _rank(totals: dict[str, dict], growth: dict[str, float]) -> list[dict]:
        rows = []
        grand = sum(v["txns"] for v in totals.values()) or 1.0
        for name, v in totals.items():
            rows.append({
                "name": name,
                "txns": int(v["txns"]),
                "value_inr": int(v["value"]),
                "avg_ticket_inr": round(v["value"] / v["txns"], 0) if v["txns"] else 0,
                "avg_success_rate": round(sum(v["sr"]) / len(v["sr"]), 2)
                if v["sr"] else None,
                "share_pct": round(100 * v["txns"] / grand, 2),
                "growth_pct": round(growth.get(name, 0.0), 1),
                "category": v.get("category"),
            })
        rows.sort(key=lambda r: r["txns"], reverse=True)
        return rows

    # ------------------------------------------------------------- surfaces
    def status(self) -> dict:
        e = self.ecosystem()
        return {"available": e.available,
                "days": len(e.daily_metrics),
                "cubes": {c: len(getattr(e, c if c != "hourly_distribution"
                                         else "hourly", []))
                          for c in ("daily_metrics", "feature_daily",
                                    "bank_daily", "psp_daily", "city_daily")}}

    def overview(self) -> dict:
        e = self.ecosystem()
        if not e.available:
            return {"available": False}
        dm = e.daily_metrics
        feats = self.compare_features()
        banks = self.compare_banks()
        psps = self.compare_psps()
        cities = self.city_trends()
        return {
            "available": True,
            "period": {"start": dm[0]["date"], "end": dm[-1]["date"],
                       "days": len(dm)},
            "sample_transactions": int(_sum(dm, "sample_txns")),
            "sample_value_inr": int(_sum(dm, "sample_value_inr")),
            "latest": dm[-1],
            "counts": {"features": len(feats), "banks": len(banks),
                       "psps": len(psps), "cities": len(cities)},
            "top_feature": feats[0] if feats else None,
            "top_bank": banks[0] if banks else None,
            "top_psp": psps[0] if psps else None,
            "top_city": cities[0] if cities else None,
        }

    def compare_features(self) -> list[dict]:
        e = self.ecosystem()
        return self._rank(_totals(e.feature_daily, "feature"),
                          self._growth("feature::"))

    def feature_analytics(self, feature: str) -> dict:
        e = self.ecosystem()
        series = [{"day": r["day"], "date": r.get("date"),
                   "txns": r.get("txns"), "value_inr": r.get("value"),
                   "success_rate": r.get("success_rate")}
                  for r in e.feature_daily if str(r.get("feature")) == feature]
        series.sort(key=lambda r: r["day"])
        totals = _totals(e.feature_daily, "feature").get(feature, {})
        growth = self._growth("feature::").get(feature)
        return {"feature": feature, "series": series,
                "txns": int(totals.get("txns", 0)),
                "value_inr": int(totals.get("value", 0)),
                "avg_ticket_inr": round(totals.get("value", 0)
                                        / max(1, totals.get("txns", 0)), 0),
                "avg_success_rate": round(sum(totals.get("sr", []))
                                          / max(1, len(totals.get("sr", []))), 2)
                if totals.get("sr") else None,
                "growth_pct": round(growth, 1) if growth is not None else None}

    def compare_banks(self) -> list[dict]:
        e = self.ecosystem()
        return self._rank(_totals(e.bank_daily, "bank"), self._growth("bank::"))

    def compare_psps(self) -> list[dict]:
        e = self.ecosystem()
        return self._rank(_totals(e.psp_daily, "psp"), self._growth("psp::"))

    def city_trends(self) -> list[dict]:
        e = self.ecosystem()
        rows = self._rank(_totals(e.city_daily, "city"), self._growth("city::"))
        # city cube has no success column; drop the null field for clarity
        for r in rows:
            r.pop("avg_success_rate", None)
        return rows

    def market_share(self) -> dict:
        """Share now, and the share trend (first vs last day) per dimension."""
        e = self.ecosystem()

        def share_trend(cube: list[dict], key: str) -> list[dict]:
            days = sorted({r["day"] for r in cube if r.get("day") is not None})
            if not days:
                return []
            first, last = days[0], days[-1]
            def day_share(d):
                rows = [r for r in cube if r.get("day") == d]
                tot = sum(r.get("txns") or 0 for r in rows) or 1
                return {str(r[key]): (r.get("txns") or 0) / tot for r in rows}
            s0, s1 = day_share(first), day_share(last)
            names = set(s0) | set(s1)
            out = [{"name": n,
                    "share_start_pct": round(100 * s0.get(n, 0), 2),
                    "share_end_pct": round(100 * s1.get(n, 0), 2),
                    "share_change_pct": round(100 * (s1.get(n, 0) - s0.get(n, 0)), 2)}
                   for n in names]
            out.sort(key=lambda r: r["share_end_pct"], reverse=True)
            return out
        return {
            "features": share_trend(e.feature_daily, "feature"),
            "banks": share_trend(e.bank_daily, "bank"),
            "psps": share_trend(e.psp_daily, "psp"),
        }

    def growth_leaders(self) -> dict:
        feats = self.compare_features()
        banks = self.compare_banks()
        psps = self.compare_psps()
        cities = self.city_trends()

        def top(rows, n=3):
            return sorted(rows, key=lambda r: r["growth_pct"], reverse=True)[:n]

        def bottom(rows, n=3):
            return sorted(rows, key=lambda r: r["growth_pct"])[:n]

        return {
            "fastest_growing_features": top(feats),
            "declining_features": bottom(feats),
            "fastest_growing_banks": top(banks),
            "fastest_growing_psps": top(psps),
            "psps_losing_share": bottom(psps),
            "fastest_growing_cities": top(cities),
        }

    def hourly_distribution(self) -> list[dict]:
        return self.ecosystem().hourly

    def transaction_mix(self) -> list[dict]:
        e = self.ecosystem()
        grand = sum(r.get("sample_txns") or 0 for r in e.mix) or 1
        return [{**r, "share_pct": round(100 * (r.get("sample_txns") or 0) / grand, 2)}
                for r in e.mix]

    def anomalies(self) -> list[dict]:
        return [f for f in self.ecosystem().bi
                if f.get("category") in ("anomaly", "high_risk_bank",
                                         "psp_share_loss", "declining_features")]

    def bi_findings(self) -> list[dict]:
        return self.ecosystem().bi

    def forecasts(self) -> list[dict]:
        return self.ecosystem().forecasts

    def customer_activity(self) -> list[dict]:
        return self.ecosystem().customer_activity

    def executive_kpis(self) -> dict:
        """A compact ecosystem dashboard: latest daily metrics + headline
        trends + the top entities."""
        e = self.ecosystem()
        if not e.available:
            return {"available": False}
        heads = {t["series"]: t for t in e.trends
                 if str(t.get("series", "")).startswith("total::")}
        return {
            "available": True,
            "latest": e.daily_metrics[-1],
            "trends": heads,
            "top_features": self.compare_features()[:5],
            "top_banks": self.compare_banks()[:5],
            "top_psps": self.compare_psps()[:5],
            "growth_leaders": self.growth_leaders(),
        }

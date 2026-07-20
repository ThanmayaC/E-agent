"""KPI Intelligence — the metrics that matter, watched continuously.

The KPI Module discovers KPIs and computes their values; this engine watches
them from a business point of view, classifies them, and acts when a threshold
is crossed:

    business KPIs      revenue, value, growth
    growth KPIs        adoption, conversion, retention
    operational KPIs   failures, errors, quality, volume
    portfolio KPIs     health scores across products

A crossed threshold produces work through the machinery that already exists —
an executive task, a strategic recommendation, a risk on the product's review,
or an executive alert (an internal notification). Nothing here sends anything
or invents a metric; it reads the KPI module's numbers and applies thresholds
the manager can configure.

Thresholds are data, not code: defaults ship, and any KPI can be given its own
rule over the API without a deploy.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.product.evidence import (
    ADOPTION_TERMS, FAILURE_TERMS, RETENTION_TERMS, REVENUE_TERMS,
    VOLUME_TERMS,
)
from app.product.store import ProductStore, new_id, now_iso

logger = get_logger(__name__)

CATEGORIES = ("business", "growth", "operational", "portfolio")
DIRECTIONS = ("higher_is_better", "lower_is_better")
SEVERITIES = ("info", "warning", "critical")

# Default thresholds on period-over-period change, by category. A manager can
# override any of these per KPI; these are the starting rules, not the law.
DEFAULT_THRESHOLDS = {
    "business": {"warning": -5.0, "critical": -15.0,
                 "direction": "higher_is_better"},
    "growth": {"warning": -5.0, "critical": -15.0,
               "direction": "higher_is_better"},
    "operational": {"warning": 10.0, "critical": 25.0,
                    "direction": "lower_is_better"},
    "portfolio": {"warning": -5.0, "critical": -10.0,
                  "direction": "higher_is_better"},
}

MAX_ALERTS = 300


class KPIIntelligence:
    """Classifies and monitors the enterprise's KPIs."""

    def __init__(self, store: ProductStore, catalog, health_engine, gatherer,
                 tasks=None, notifications=None, bus=None):
        self._store = store
        self._catalog = catalog
        self._health = health_engine
        self._gatherer = gatherer
        self._tasks = tasks
        self._notifications = notifications
        self._bus = bus

    def attach_bus(self, bus) -> None:
        self._bus = bus

    # ------------------------------------------------------------- monitor
    def monitor(self) -> dict[str, Any]:
        """Check every product's KPIs against their thresholds and act.

        Reports two different facts a manager needs kept apart: how many KPIs
        are *currently* breaching (the state of the business) and how many of
        those are *new* since the last check (what deserves attention now). A
        breach that is still breaching is still true — it just must not raise
        the same task and the same alert every fifteen minutes.
        """
        breaching, new, created = [], [], {"tasks": 0, "alerts": 0, "risks": 0}
        for product in self._catalog.products(status="active"):
            evidence = self._gatherer.gather(product)
            for kpi in evidence.kpis:
                breach = self._check(kpi, product)
                if breach is None:
                    continue
                breaching.append(breach)
                if self._act(breach, created):
                    new.append(breach)

        # Portfolio KPIs: the health scores themselves are KPIs.
        for record in self._health.all_health():
            breach = self._check_health(record)
            if breach is None:
                continue
            breaching.append(breach)
            if self._act(breach, created):
                new.append(breach)

        return {"kpis_breaching": len(breaching), "kpis_breached": len(new),
                "breaches": new[:20], "currently_breaching": breaching[:20],
                "generated": created, "monitored_at": now_iso()}

    def _check(self, kpi: dict, product: dict) -> dict | None:
        category = classify(str(kpi.get("name", "")))
        if category is None:
            return None
        change = kpi.get("growth_pct")
        if not isinstance(change, (int, float)):
            return None
        rule = self.threshold_for(str(kpi.get("name", "")), category)
        severity = _severity(change, rule)
        if severity is None:
            return None
        return {
            "alert_id": new_id("kpa"), "kpi": str(kpi.get("name", "")),
            "kpi_id": str(kpi.get("id") or kpi.get("kpi_id") or ""),
            "category": category, "product_id": product["product_id"],
            "product": product["name"], "change_pct": round(float(change), 2),
            "current_value": kpi.get("current_value"),
            "unit": kpi.get("unit", ""), "severity": severity,
            "direction": rule["direction"],
            "threshold": rule["critical" if severity == "critical"
                              else "warning"],
            "evidence_ids": [f"kpi:{kpi.get('id') or kpi.get('name')}"],
            "signature": f"{product['product_id']}:{kpi.get('name')}:{severity}",
            "detected_at": now_iso(),
        }

    def _check_health(self, record: dict) -> dict | None:
        change = record.get("change")
        if not isinstance(change, (int, float)):
            return None
        rule = self.threshold_for("portfolio health", "portfolio")
        severity = _severity(change, rule)
        if severity is None:
            return None
        return {
            "alert_id": new_id("kpa"), "kpi": "Product health score",
            "kpi_id": "", "category": "portfolio",
            "product_id": record["product_id"], "product": record["product"],
            "change_pct": round(float(change), 2),
            "current_value": record.get("health_score"), "unit": "/100",
            "severity": severity, "direction": rule["direction"],
            "threshold": rule["critical" if severity == "critical"
                              else "warning"],
            "evidence_ids": record.get("evidence_ids", []),
            "signature": f"{record['product_id']}:health:{severity}",
            "detected_at": now_iso(),
        }

    # ---------------------------------------------------------------- act
    def _act(self, breach: dict, created: dict) -> bool:
        """A crossed threshold becomes work — through the existing task
        manager, notification centre, and event bus. This engine creates no
        new delivery mechanism. Returns whether the breach was new."""
        if self._recorded(breach):
            return False  # the same breach must not nag every fifteen minutes
        self._store.append("kpi_alerts", breach, cap=MAX_ALERTS)

        direction = ("fell" if breach["change_pct"] < 0 else "rose")
        headline = (f"{breach['kpi']} {direction} "
                    f"{abs(breach['change_pct']):.1f}% — {breach['product']}")

        if self._tasks is not None and breach["severity"] == "critical":
            task = self._tasks.create(
                f"Investigate: {headline}", status="pending", priority=1,
                source_kind="business_rule",
                source_ref=f"kpi:{breach['signature']}",
                detail=f"{breach['category'].title()} KPI crossed its "
                       f"critical threshold of {breach['threshold']}%.")
            created["tasks"] += 1 if task else 0

        if self._notifications is not None:
            notification = self._notifications.notify(
                "critical_risk" if breach["severity"] == "critical"
                else "portfolio_change", headline,
                detail=f"{breach['category'].title()} KPI, now "
                       f"{breach['current_value']}{breach['unit']}",
                ref=f"kpi:{breach['signature']}")
            created["alerts"] += 1 if notification else 0

        if breach["severity"] == "critical":
            created["risks"] += 1

        if self._bus is not None:
            try:
                self._bus.publish("KPIThresholdCrossed", {
                    "kpi": breach["kpi"], "category": breach["category"],
                    "product": breach["product"],
                    "product_id": breach["product_id"],
                    "change_pct": breach["change_pct"],
                    "severity": breach["severity"],
                    "detail": headline}, source="kpi_intelligence")
            except Exception:  # noqa: BLE001
                logger.exception("KPI event publication failed")
        return True

    def _recorded(self, breach: dict) -> bool:
        return any(a["signature"] == breach["signature"]
                   for a in self._store.read("kpi_alerts"))

    # ------------------------------------------------------- thresholds
    def set_threshold(self, kpi_name: str, warning: float, critical: float,
                      direction: str = "higher_is_better",
                      category: str = "") -> dict:
        """Give one KPI its own rule. Configuration, not code."""
        if direction not in DIRECTIONS:
            raise ValueError(f"Unknown direction: {direction}")
        if category and category not in CATEGORIES:
            raise ValueError(f"Unknown KPI category: {category}")
        rule = {"kpi": kpi_name.strip().lower(), "warning": float(warning),
                "critical": float(critical), "direction": direction,
                "category": category or classify(kpi_name) or "business",
                "updated_at": now_iso()}
        with self._store.mutate("kpi_thresholds") as rules:
            rules[:] = [r for r in rules if r["kpi"] != rule["kpi"]]
            rules.append(rule)
        return rule

    def threshold_for(self, kpi_name: str, category: str) -> dict:
        """The rule for one KPI: its own if configured, else its category's."""
        name = kpi_name.strip().lower()
        for rule in self._store.read("kpi_thresholds"):
            if rule["kpi"] == name:
                return rule
        return DEFAULT_THRESHOLDS[category]

    def thresholds(self) -> dict[str, Any]:
        return {"defaults": DEFAULT_THRESHOLDS,
                "overrides": self._store.read("kpi_thresholds")}

    # ---------------------------------------------------------------- read
    def overview(self) -> dict[str, Any]:
        """Every monitored KPI, by category — the KPI panel."""
        by_category: dict[str, list] = {c: [] for c in CATEGORIES}
        for product in self._catalog.products(status="active"):
            evidence = self._gatherer.gather(product)
            for kpi in evidence.kpis:
                category = classify(str(kpi.get("name", "")))
                if category is None:
                    continue
                by_category[category].append({
                    "kpi": kpi.get("name"), "product": product["name"],
                    "product_id": product["product_id"],
                    "value": kpi.get("current_value"),
                    "unit": kpi.get("unit", ""),
                    "change_pct": kpi.get("growth_pct"),
                    "trend": kpi.get("trend", "flat")})
        for record in self._health.all_health():
            by_category["portfolio"].append({
                "kpi": "Product health score", "product": record["product"],
                "product_id": record["product_id"],
                "value": record.get("health_score"), "unit": "/100",
                "change_pct": record.get("change"),
                "trend": _trend_of(record.get("change"))})
        return {"by_category": {k: v[:25] for k, v in by_category.items()},
                "counts": {k: len(v) for k, v in by_category.items()},
                "alerts": self.alerts(limit=10)}

    def alerts(self, severity: str = "", product_id: str = "",
               limit: int = 50) -> list[dict]:
        items = self._store.read("kpi_alerts")
        if severity:
            items = [a for a in items if a["severity"] == severity]
        if product_id:
            items = [a for a in items if a["product_id"] == product_id]
        return list(reversed(items))[:limit]


# --------------------------------------------------------------- utilities
def classify(kpi_name: str) -> str | None:
    """Which business category a KPI belongs to, by what the KPI module named
    it. Order matters: a "failed payment value" KPI is operational, not
    revenue, because the failure is the thing being measured."""
    name = str(kpi_name).strip().lower()
    if any(term in name for term in FAILURE_TERMS):
        return "operational"
    if any(term in name for term in REVENUE_TERMS):
        return "business"
    if any(term in name for term in ADOPTION_TERMS + RETENTION_TERMS):
        return "growth"
    if any(term in name for term in VOLUME_TERMS):
        return "operational"
    return None


def _severity(change: float, rule: dict) -> str | None:
    """Whether a change breaches a rule, in the direction that matters."""
    if rule["direction"] == "higher_is_better":
        if change <= rule["critical"]:
            return "critical"
        if change <= rule["warning"]:
            return "warning"
        return None
    if change >= rule["critical"]:
        return "critical"
    if change >= rule["warning"]:
        return "warning"
    return None


def _trend_of(change: float | None) -> str:
    if change is None:
        return "flat"
    return "up" if change > 0 else "down" if change < 0 else "flat"

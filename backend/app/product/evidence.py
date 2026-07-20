"""Product evidence — the facts a product judgement is allowed to stand on.

The Product Intelligence layer computes no analytics. It reads what the
platform already produced — KPIs, deterministic signals, forecasts, quality
reports, verified insights, report history — and every score, opportunity, and
recommendation above carries the evidence ids it was derived from.

This module is the single place that gathers those facts for one product, so
the engines above cannot accidentally invent one. If a fact is not here, no
engine can cite it, and an engine that cannot cite must not conclude.

``ProductEvidence`` is deliberately dumb: it collects and indexes, it does not
interpret. Interpretation is the engines' job, and keeping the two apart is
what makes "evidence-based" checkable rather than aspirational.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.core.logging import get_logger

logger = get_logger(__name__)

# Signals the platform emits, in the vocabulary the SDS uses for products.
TREND = "trend"
ANOMALY = "anomaly"
CONCENTRATION = "concentration"
CORRELATION = "correlation"
INVERSE_CORRELATION = "inverse_correlation"  # the cannibalization candidate
SEASONALITY = "seasonality"

# KPI names, by the business concept they measure. The KPI module names KPIs
# after what it discovered; this is how the product layer reads that naming
# without redefining a single metric.
REVENUE_TERMS = ("revenue", "value", "gmv", "sales", "income", "turnover")
VOLUME_TERMS = ("volume", "transactions", "txn", "orders", "count", "payments")
ADOPTION_TERMS = ("active", "adoption", "usage", "registered", "signup",
                  "onboard", "conversion")
RETENTION_TERMS = ("retention", "churn", "repeat", "loyalty", "satisfaction",
                   "nps")
FAILURE_TERMS = ("failure", "failed", "error", "decline", "reject", "fraud",
                 "chargeback", "dispute")
MERCHANT_TERMS = ("merchant", "seller", "partner", "store", "vendor")
CUSTOMER_TERMS = ("customer", "user", "client", "account", "member")


@dataclass
class ProductEvidence:
    """Everything known about one product, gathered from existing artifacts."""
    product: dict
    kpis: list[dict] = field(default_factory=list)
    signals: list[dict] = field(default_factory=list)
    forecasts: list[dict] = field(default_factory=list)
    quality: dict = field(default_factory=dict)
    insights: list[dict] = field(default_factory=list)
    reports: list[dict] = field(default_factory=list)
    projects: list[str] = field(default_factory=list)

    # ------------------------------------------------------------- lookups
    def kpis_matching(self, terms: tuple[str, ...]) -> list[dict]:
        return [k for k in self.kpis
                if _mentions_any(str(k.get("name", "")), terms)]

    def signals_of(self, kind: str) -> list[dict]:
        return [s for s in self.signals if s.get("kind") == kind]

    @property
    def has_facts(self) -> bool:
        """Whether anything at all is known. A product with no evidence gets
        no score — not a zero, which would read as "bad" rather than
        "unknown"."""
        return bool(self.kpis or self.signals or self.forecasts
                    or self.reports)

    def cite(self, limit: int = 8) -> list[str]:
        """Evidence ids for everything gathered — what a judgement may cite."""
        ids = [f"kpi:{k.get('kpi_id') or k.get('name')}" for k in self.kpis]
        ids += [f"signal:{s.get('id')}" for s in self.signals if s.get("id")]
        ids += [f"forecast:{f.get('kpi_id')}" for f in self.forecasts
                if f.get("kpi_id")]
        ids += [f"report:{r.get('project_id')}:{r.get('title', '')[:30]}"
                for r in self.reports[-2:]]
        return ids[:limit]

    def describe(self) -> dict:
        return {"kpis": len(self.kpis), "signals": len(self.signals),
                "forecasts": len(self.forecasts),
                "reports": len(self.reports),
                "quality_score": self.quality.get("overall_score"),
                "projects": self.projects}


class EvidenceGatherer:
    """Collects a product's evidence from the platform's existing artifacts."""

    def __init__(self, artifacts, knowledge):
        self._artifacts = artifacts
        self._knowledge = knowledge

    def gather(self, product: dict) -> ProductEvidence:
        """Read every fact the platform holds about one product.

        Scope: the projects the product is associated with. Without an
        association the product's own KPI list (resolved by the catalogue) is
        used, so a product still gets an honest, if narrower, evidence base.
        """
        projects = list(product.get("projects") or [])
        if not projects:
            projects = self._projects_mentioning(product)

        evidence = ProductEvidence(product=product, projects=projects)
        kpi_names = {str(k.get("name", "")) for k in product.get("kpis") or []}

        for pid in projects:
            for kpi in self._load(pid, "kpis", []):
                if kpi_names and str(kpi.get("name", "")) not in kpi_names:
                    continue
                evidence.kpis.append({**kpi, "project_id": pid})
            for signal in self._load(pid, "signals", []):
                evidence.signals.append({**signal, "project_id": pid})
            forecasts = self._load(pid, "forecasts", [])
            if isinstance(forecasts, dict):
                forecasts = forecasts.get("forecasts") or forecasts.get(
                    "series") or []
            for forecast in forecasts:
                if isinstance(forecast, dict):
                    evidence.forecasts.append({**forecast, "project_id": pid})
            quality = self._load(pid, "quality", {})
            if isinstance(quality, dict) and quality.get("overall_score") \
                    is not None:
                # Several projects: the weakest data wins, because a product is
                # only as trustworthy as its worst input.
                current = evidence.quality.get("overall_score")
                if current is None or quality["overall_score"] < current:
                    evidence.quality = {**quality, "project_id": pid}

        evidence.reports = list(product.get("reports") or [])
        evidence.insights = [
            i for i in self._safe(lambda: self._knowledge.insights(50), [])
            if i.get("project_id") in projects]
        return evidence

    def _projects_mentioning(self, product: dict) -> list[str]:
        """Fall back to projects whose name mentions the product."""
        canonical = str(product.get("canonical", "")).replace("_", " ")
        if not canonical:
            return []
        out = []
        for pid in self._artifacts.list_projects():
            state = self._artifacts.load(pid, "state") or {}
            if canonical in str(state.get("name", "")).lower():
                out.append(pid)
        return out

    def _load(self, project_id: str, name: str, default):
        payload = self._safe(
            lambda: self._artifacts.load(project_id, name, default), default)
        return payload if isinstance(payload, type(default)) else default

    @staticmethod
    def _safe(read, default):
        """A missing or unreadable artifact means "unknown", never a crash —
        the product layer degrades to less evidence, not to an error."""
        try:
            return read()
        except Exception:  # noqa: BLE001
            logger.exception("Product evidence read failed")
            return default


def _mentions_any(text: str, terms: tuple[str, ...]) -> bool:
    lowered = str(text).strip().lower()
    return any(term in lowered for term in terms)

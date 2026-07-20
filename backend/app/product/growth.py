"""Growth Intelligence Engine — where the business can grow, and where it is losing.

Seven findings, each derived from a deterministic fact the platform already
computed, each citing it:

    growth_opportunity   a KPI growing strongly, or a forecast pointing up
    declining_product    KPIs falling, or health trending down
    emerging_trend       a strong TREND signal the platform detected
    cannibalization      an INVERSE_CORRELATION signal — the Analytics module
                         already names this the cannibalization candidate, so
                         this engine reads it rather than re-deriving it
    cross_sell           two products sharing merchants or customers, where
                         one is healthy and the other is not
    portfolio_gap        a CONCENTRATION signal, or a lifecycle stage with no
                         products in it
    expansion            a product healthy and growing, ready for more

**No business facts are invented here.** Every finding points at a signal id,
a KPI, or a health record. Where the platform has detected nothing, this
engine reports nothing — an empty growth list means "no evidence", and saying
so is more useful to a manager than a plausible guess.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.product.evidence import (
    CONCENTRATION, EvidenceGatherer, FAILURE_TERMS, INVERSE_CORRELATION,
    ProductEvidence, TREND,
)
from app.product.store import now_iso

logger = get_logger(__name__)

FINDING_KINDS = ("growth_opportunity", "declining_product", "emerging_trend",
                 "cannibalization", "cross_sell", "portfolio_gap",
                 "expansion")

STRONG_GROWTH = 10.0      # % period-over-period that counts as strong growth
MATERIAL_DECLINE = -5.0   # % that counts as a real decline
STRONG_SIGNAL = 0.6       # signal strength worth an executive's attention
HEALTHY = 70.0
STRUGGLING = 50.0


class GrowthIntelligenceEngine:
    """Continuously identifies where the portfolio grows and where it leaks."""

    def __init__(self, catalog, health_engine, gatherer: EvidenceGatherer,
                 bus=None):
        self._catalog = catalog
        self._health = health_engine
        self._gatherer = gatherer
        self._bus = bus

    def attach_bus(self, bus) -> None:
        self._bus = bus

    # ------------------------------------------------------------- analyse
    def analyse(self) -> dict[str, Any]:
        """Look across the whole portfolio. Returns findings by kind."""
        products = self._catalog.products(status="active")
        evidence = {p["product_id"]: self._gatherer.gather(p)
                    for p in products}

        findings: list[dict] = []
        for product in products:
            product_evidence = evidence[product["product_id"]]
            findings += self._opportunities(product, product_evidence)
            findings += self._decline(product, product_evidence)
            findings += self._trends(product, product_evidence)
            findings += self._cannibalization(product, product_evidence)
            findings += self._expansion(product, product_evidence)
        findings += self._cross_sell(products)
        findings += self._gaps(products, evidence)

        findings.sort(key=lambda f: (-f["confidence"], f["kind"]))
        by_kind: dict[str, int] = {}
        for finding in findings:
            by_kind[finding["kind"]] = by_kind.get(finding["kind"], 0) + 1
        self._announce(findings)
        return {"findings": findings, "by_kind": by_kind,
                "products_analysed": len(products),
                "analysed_at": now_iso()}

    def findings(self, kind: str = "", product_id: str = "",
                 limit: int = 50) -> list[dict]:
        items = self.analyse()["findings"]
        if kind:
            items = [f for f in items if f["kind"] == kind]
        if product_id:
            items = [f for f in items if f.get("product_id") == product_id]
        return items[:limit]

    # ------------------------------------------------------------ findings
    def _opportunities(self, product: dict,
                       evidence: ProductEvidence) -> list[dict]:
        out = []
        for kpi in evidence.kpis:
            growth = kpi.get("growth_pct")
            if not isinstance(growth, (int, float)) or growth < STRONG_GROWTH:
                continue
            if not _higher_is_better(kpi.get("name", "")):
                continue  # a rising failure rate is a risk, not an opportunity
            out.append(_finding(
                "growth_opportunity", product,
                f"{kpi['name']} is growing {growth:+.1f}% — "
                f"{product['name']} has room to scale what is working",
                confidence=_confidence_from_growth(growth),
                evidence_ids=[f"kpi:{kpi.get('id') or kpi['name']}"],
                detail=f"{kpi['name']} at {kpi.get('current_value')}"
                       f"{kpi.get('unit', '')}, {growth:+.1f}% "
                       f"period-over-period"))
        for forecast in evidence.forecasts:
            if str(forecast.get("status")) != "ok":
                continue  # the forecasting module's own validation gate
            if not _higher_is_better(forecast.get("kpi_name", "")):
                continue
            direction = _direction(forecast)
            confidence = float(forecast.get("confidence") or 0)
            if direction > 0 and confidence >= 0.6:
                out.append(_finding(
                    "growth_opportunity", product,
                    f"{forecast.get('kpi_name')} is forecast to rise over "
                    f"the {forecast.get('horizon', 'next period')}",
                    confidence=round(confidence, 3),
                    evidence_ids=[f"forecast:{forecast.get('kpi_id')}"],
                    detail=f"method {forecast.get('method')}, confidence "
                           f"{confidence:.0%}"))
        return out[:5]

    def _decline(self, product: dict, evidence: ProductEvidence) -> list[dict]:
        out = []
        # A falling failure rate is good news, not a decline — direction is
        # a property of what the KPI measures, not of the arithmetic.
        falling = [k for k in evidence.kpis
                   if isinstance(k.get("growth_pct"), (int, float))
                   and k["growth_pct"] <= MATERIAL_DECLINE
                   and _higher_is_better(k.get("name", ""))]
        if falling:
            worst = min(falling, key=lambda k: k["growth_pct"])
            out.append(_finding(
                "declining_product", product,
                f"{product['name']} is declining — {worst['name']} fell "
                f"{worst['growth_pct']:+.1f}%",
                confidence=_confidence_from_growth(abs(worst["growth_pct"])),
                evidence_ids=[f"kpi:{k.get('id') or k['name']}"
                              for k in falling][:5],
                detail=f"{len(falling)} KPI(s) declining materially"))
        health = self._health.health(product["product_id"])
        if health and health.get("change") is not None \
                and health["change"] <= -5:
            out.append(_finding(
                "declining_product", product,
                f"{product['name']} health fell "
                f"{abs(health['change']):.0f} points to "
                f"{health['health_score']:.0f}",
                confidence=health.get("confidence", 0.5),
                evidence_ids=health.get("evidence_ids", []),
                detail=health["reasons"].get("growth", "")))
        return out[:3]

    def _trends(self, product: dict, evidence: ProductEvidence) -> list[dict]:
        out = []
        for signal in evidence.signals_of(TREND):
            strength = float(signal.get("strength") or 0)
            if strength < STRONG_SIGNAL:
                continue
            stats = signal.get("stats") or {}
            out.append(_finding(
                "emerging_trend", product,
                f"{signal.get('kpi_name') or 'a metric'} shows a sustained "
                f"trend for {product['name']}",
                confidence=round(strength, 3),
                evidence_ids=[f"signal:{signal.get('id')}"],
                detail=f"trend strength {strength:.0%}"
                       + (f", slope {stats.get('slope')}"
                          if stats.get("slope") is not None else "")))
        return out[:3]

    def _cannibalization(self, product: dict,
                         evidence: ProductEvidence) -> list[dict]:
        """The Analytics module already labels inverse correlation the
        cannibalization candidate — this reads that signal, it does not
        recompute a correlation."""
        out = []
        for signal in evidence.signals_of(INVERSE_CORRELATION):
            strength = float(signal.get("strength") or 0)
            if strength < STRONG_SIGNAL:
                continue
            stats = signal.get("stats") or {}
            pair = stats.get("kpi_b_name") or stats.get("other_kpi") or "another metric"
            out.append(_finding(
                "cannibalization", product,
                f"{signal.get('kpi_name') or 'a metric'} moves inversely to "
                f"{pair} — {product['name']} may be cannibalizing demand",
                confidence=round(strength, 3),
                evidence_ids=[f"signal:{signal.get('id')}"],
                detail=f"inverse correlation r={stats.get('r', '?')}, "
                       f"strength {strength:.0%}"))
        return out[:3]

    def _expansion(self, product: dict,
                   evidence: ProductEvidence) -> list[dict]:
        health = self._health.health(product["product_id"])
        if not health or health.get("health_score") is None:
            return []
        growth = (health["scores"] or {}).get("growth")
        if health["health_score"] >= HEALTHY and isinstance(growth, (int, float)) \
                and growth >= 60:
            return [_finding(
                "expansion", product,
                f"{product['name']} is healthy ({health['health_score']:.0f}) "
                f"and growing — a candidate for expansion or investment",
                confidence=health.get("confidence", 0.5),
                evidence_ids=health.get("evidence_ids", []),
                detail=health["reasons"].get("growth", ""))]
        return []

    def _cross_sell(self, products: list[dict]) -> list[dict]:
        """Two products sharing merchants or customers, where one is doing
        well and the other is not: the audience is proven, the product is
        not reaching it."""
        out = []
        scored = {p["product_id"]: self._health.health(p["product_id"])
                  for p in products}
        for i, first in enumerate(products):
            for second in products[i + 1:]:
                shared_merchants = set(first["merchants"]) & set(
                    second["merchants"])
                shared_customers = set(first["customers"]) & set(
                    second["customers"])
                if not shared_merchants and not shared_customers:
                    continue
                strong, weak = _stronger(first, second, scored)
                if strong is None:
                    continue
                audience = (f"{len(shared_merchants)} merchant(s)"
                            if shared_merchants
                            else f"{len(shared_customers)} customer(s)")
                out.append(_finding(
                    "cross_sell", weak,
                    f"{strong['name']} and {weak['name']} share {audience}, "
                    f"but {weak['name']} is performing worse — a cross-sell "
                    f"opportunity into a proven audience",
                    confidence=0.6,
                    evidence_ids=(scored[strong["product_id"]] or {}).get(
                        "evidence_ids", []),
                    detail=f"shared via the organizational model: "
                           f"{', '.join(sorted(shared_merchants | shared_customers)[:5])}"))
        return out[:5]

    def _gaps(self, products: list[dict],
              evidence: dict[str, ProductEvidence]) -> list[dict]:
        out = []
        # Concentration is a portfolio gap the Analytics module already found.
        for product in products:
            for signal in evidence[product["product_id"]].signals_of(
                    CONCENTRATION):
                strength = float(signal.get("strength") or 0)
                if strength < STRONG_SIGNAL:
                    continue
                stats = signal.get("stats") or {}
                out.append(_finding(
                    "portfolio_gap", product,
                    f"{product['name']} is concentrated — a few "
                    f"{stats.get('dimension', 'segments')} carry most of "
                    f"{signal.get('kpi_name') or 'the value'}",
                    confidence=round(strength, 3),
                    evidence_ids=[f"signal:{signal.get('id')}"],
                    detail=f"top share {stats.get('top_share', '?')}, "
                           f"concentration strength {strength:.0%}"))
        # A lifecycle stage with nothing in it is a portfolio gap the manager
        # can act on — and it is a fact about the catalogue, not a guess.
        if products:
            occupied = {p["lifecycle"] for p in products}
            for stage in ("launch", "growth"):
                if stage not in occupied:
                    out.append({
                        "kind": "portfolio_gap", "product_id": "",
                        "product": "portfolio",
                        "finding": f"No product is in the '{stage}' stage — "
                                   f"the portfolio has no {stage} pipeline",
                        "confidence": 0.9,
                        "evidence_ids": ["catalog:lifecycle"],
                        "detail": f"lifecycle stages present: "
                                  f"{', '.join(sorted(occupied))}",
                        "found_at": now_iso()})
        return out[:5]

    def _announce(self, findings: list[dict]) -> None:
        if self._bus is None:
            return
        for finding in findings:
            if finding["kind"] not in ("declining_product", "cannibalization"):
                continue
            if finding["confidence"] < STRONG_SIGNAL:
                continue
            try:
                self._bus.publish("GrowthRiskDetected", {
                    "kind": finding["kind"],
                    "product": finding["product"],
                    "product_id": finding.get("product_id", ""),
                    "finding": finding["finding"][:200],
                    "confidence": finding["confidence"]},
                    source="growth_intelligence")
            except Exception:  # noqa: BLE001 — announcing never fails analysis
                logger.exception("Growth event publication failed")


# --------------------------------------------------------------- utilities
def _finding(kind: str, product: dict, text: str, confidence: float,
             evidence_ids: list[str], detail: str = "") -> dict:
    if kind not in FINDING_KINDS:
        raise ValueError(f"Unknown growth finding kind: {kind}")
    return {"kind": kind, "product_id": product.get("product_id", ""),
            "product": product.get("name", ""), "finding": text[:300],
            "confidence": round(float(confidence), 3),
            "evidence_ids": evidence_ids[:8], "detail": detail[:300],
            "found_at": now_iso()}


def _higher_is_better(kpi_name: str) -> bool:
    """Whether growth in this KPI is good news.

    A failure, error, or chargeback metric is lower-is-better: rising failed
    transactions is a risk, and reporting it as a growth opportunity to
    "scale what is working" is worse than saying nothing. The KPI module
    already names what it measures — this reads that naming rather than
    assuming every number should go up.
    """
    lowered = str(kpi_name).strip().lower()
    return not any(term in lowered for term in FAILURE_TERMS)


def _confidence_from_growth(growth_pct: float) -> float:
    """A bigger move is a more reliable signal, to a ceiling — a 200% swing
    is not 20x more certain than a 10% one, it is usually a data problem."""
    return round(min(0.5 + abs(growth_pct) / 100, 0.9), 3)


def _direction(forecast: dict) -> float:
    values = forecast.get("values") or []
    if len(values) < 2:
        return 0.0
    try:
        return 1.0 if float(values[-1]) > float(values[0]) else -1.0
    except (TypeError, ValueError):
        return 0.0


def _stronger(first: dict, second: dict,
              scored: dict) -> tuple[dict | None, dict | None]:
    """Which of two products is doing better, when both are known."""
    first_health = (scored.get(first["product_id"]) or {}).get("health_score")
    second_health = (scored.get(second["product_id"]) or {}).get("health_score")
    if first_health is None or second_health is None:
        return None, None
    if first_health >= HEALTHY and second_health < STRUGGLING:
        return first, second
    if second_health >= HEALTHY and first_health < STRUGGLING:
        return second, first
    return None, None

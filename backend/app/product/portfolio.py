"""Portfolio Intelligence — the whole product portfolio, judged as one thing.

The Manager Module already has a PortfolioWorkspace: per-*project* health,
trends, and report history for the executive. This engine is the product
manager's portfolio: per-*product* health, risk, growth, investment priority,
ranking, and the top opportunities and risks across the business.

The two are complementary, not duplicative — one answers "how are our analyses
doing?", this one answers "how is our product portfolio doing, and where
should the next pound go?". Every number here is composed from the Product
Health Engine's scores and the Growth Engine's findings; nothing is
recomputed.

Investment priority is the one genuine judgement, and it is a stated rule
rather than a hidden model: invest where growth is proven and health is good,
fix where risk is high and revenue is real, watch what is unmeasured, and
question what is declining with no growth signal. The rule is in the code, in
one function, and the reason travels with every verdict.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.product.store import now_iso

logger = get_logger(__name__)

PRIORITIES = ("invest", "fix", "maintain", "watch", "question")

HEALTHY = 70.0
WEAK = 50.0
STRONG_GROWTH_SCORE = 60.0


class PortfolioIntelligence:
    """Evaluates the complete enterprise product portfolio."""

    def __init__(self, catalog, health_engine, growth, strategy, bus=None):
        self._catalog = catalog
        self._health = health_engine
        self._growth = growth
        self._strategy = strategy
        self._bus = bus

    def attach_bus(self, bus) -> None:
        self._bus = bus

    # ----------------------------------------------------------- portfolio
    def evaluate(self) -> dict[str, Any]:
        """The portfolio view: health, risk, growth, ranking, priorities."""
        products = self._catalog.products(status="active")
        health = {h["product_id"]: h for h in self._health.all_health()}
        analysis = self._growth.analyse()
        findings = analysis["findings"]

        ranked = self._rank(products, health, findings)
        scored = [r for r in ranked if r["health_score"] is not None]

        return {
            "portfolio_health": self._portfolio_health(scored),
            "portfolio_risk": self._portfolio_risk(scored, findings),
            "portfolio_growth": self._portfolio_growth(scored, findings),
            "product_ranking": ranked,
            "investment_priorities": _group(ranked, "investment_priority"),
            "top_opportunities": self._top(findings, ("growth_opportunity",
                                                      "expansion",
                                                      "cross_sell")),
            "top_risks": self._top(findings, ("declining_product",
                                              "cannibalization",
                                              "portfolio_gap")),
            "coverage": {
                "products": len(products),
                "measured": len(scored),
                "unmeasured": len(ranked) - len(scored),
                "by_lifecycle": _group(ranked, "lifecycle"),
            },
            "evaluated_at": now_iso(),
        }

    def _rank(self, products: list[dict], health: dict,
              findings: list[dict]) -> list[dict]:
        """Rank every product, and say why each sits where it does."""
        by_product: dict[str, list[dict]] = {}
        for finding in findings:
            if finding.get("product_id"):
                by_product.setdefault(finding["product_id"], []).append(finding)

        ranked = []
        for product in products:
            record = health.get(product["product_id"]) or {}
            score = record.get("health_score")
            scores = record.get("scores") or {}
            product_findings = by_product.get(product["product_id"], [])
            priority, reason = _investment_priority(score, scores,
                                                    product_findings)
            ranked.append({
                "product_id": product["product_id"],
                "product": product["name"], "owner": product["owner"],
                "lifecycle": product["lifecycle"],
                "business_unit": product["business_unit"],
                "health_score": score, "band": record.get("band", "unknown"),
                "change": record.get("change"),
                "growth_score": scores.get("growth"),
                "risk_score": scores.get("risk"),
                "revenue_score": scores.get("revenue"),
                "confidence": record.get("confidence", 0.0),
                "investment_priority": priority,
                "priority_reason": reason,
                "opportunities": sum(1 for f in product_findings
                                     if f["kind"] in ("growth_opportunity",
                                                      "expansion",
                                                      "cross_sell")),
                "risks": sum(1 for f in product_findings
                             if f["kind"] in ("declining_product",
                                              "cannibalization")),
                "evidence_ids": record.get("evidence_ids", []),
            })
        # Unmeasured products sort last: absence of a score is not a low score.
        ranked.sort(key=lambda r: (r["health_score"] is None,
                                   -(r["health_score"] or 0)))
        for position, entry in enumerate(ranked, start=1):
            entry["rank"] = position
        return ranked

    def _portfolio_health(self, scored: list[dict]) -> dict[str, Any]:
        if not scored:
            return {"score": None, "band": "unknown",
                    "detail": "no product has enough evidence to be scored"}
        average = round(sum(r["health_score"] for r in scored) / len(scored), 1)
        return {
            "score": average,
            "band": ("healthy" if average >= HEALTHY
                     else "watch" if average >= WEAK else "at_risk"),
            "healthy": sum(1 for r in scored if r["health_score"] >= HEALTHY),
            "watch": sum(1 for r in scored
                         if WEAK <= r["health_score"] < HEALTHY),
            "at_risk": sum(1 for r in scored if r["health_score"] < WEAK),
            "confidence": round(sum(r["confidence"] for r in scored)
                                / len(scored), 3),
            "detail": f"mean health across {len(scored)} measured product(s)",
        }

    def _portfolio_risk(self, scored: list[dict],
                        findings: list[dict]) -> dict[str, Any]:
        risks = [r["risk_score"] for r in scored
                 if isinstance(r.get("risk_score"), (int, float))]
        declining = [f for f in findings if f["kind"] == "declining_product"]
        cannibalizing = [f for f in findings if f["kind"] == "cannibalization"]
        average = round(sum(risks) / len(risks), 1) if risks else None
        return {
            "score": average,  # inverted: 100 is safe
            "band": ("low" if average is None else
                     "low" if average >= HEALTHY else
                     "medium" if average >= WEAK else "high"),
            "products_at_risk": sum(1 for r in scored
                                    if r["band"] == "at_risk"),
            "declining_products": len({f["product_id"] for f in declining}),
            "cannibalization_signals": len(cannibalizing),
            "concentration": sum(1 for f in findings
                                 if f["kind"] == "portfolio_gap"),
            "detail": (f"mean risk posture across {len(risks)} product(s)"
                       if risks else "no product carries risk evidence"),
        }

    def _portfolio_growth(self, scored: list[dict],
                          findings: list[dict]) -> dict[str, Any]:
        growth = [r["growth_score"] for r in scored
                  if isinstance(r.get("growth_score"), (int, float))]
        opportunities = [f for f in findings
                         if f["kind"] in ("growth_opportunity", "expansion")]
        average = round(sum(growth) / len(growth), 1) if growth else None
        return {
            "score": average,
            "band": ("unknown" if average is None else
                     "growing" if average >= STRONG_GROWTH_SCORE else
                     "flat" if average >= WEAK else "shrinking"),
            "growing_products": sum(1 for r in scored
                                    if isinstance(r.get("growth_score"),
                                                  (int, float))
                                    and r["growth_score"] >= STRONG_GROWTH_SCORE),
            "opportunities": len(opportunities),
            "emerging_trends": sum(1 for f in findings
                                   if f["kind"] == "emerging_trend"),
            "cross_sell": sum(1 for f in findings if f["kind"] == "cross_sell"),
            "detail": (f"mean growth score across {len(growth)} product(s)"
                       if growth else "no product carries growth evidence"),
        }

    def _top(self, findings: list[dict], kinds: tuple[str, ...],
             limit: int = 5) -> list[dict]:
        selected = [f for f in findings if f["kind"] in kinds]
        selected.sort(key=lambda f: -f["confidence"])
        return [{"kind": f["kind"], "product": f["product"],
                 "product_id": f.get("product_id", ""),
                 "finding": f["finding"], "confidence": f["confidence"],
                 "evidence_ids": f["evidence_ids"]}
                for f in selected[:limit]]


# --------------------------------------------------------------- utilities
def _investment_priority(score: float | None, scores: dict,
                         findings: list[dict]) -> tuple[str, str]:
    """Where the next pound goes, and why. One stated rule, not a model.

    Unmeasured is deliberately its own verdict: a product the platform cannot
    see is a decision about *instrumentation*, not about investment, and
    conflating the two is how unmeasured products quietly get defunded.
    """
    if score is None:
        return "watch", ("not measurable yet — connect this product's data "
                         "before making an investment call")

    growth = scores.get("growth")
    risk = scores.get("risk")
    revenue = scores.get("revenue")
    declining = any(f["kind"] == "declining_product" for f in findings)
    expanding = any(f["kind"] == "expansion" for f in findings)

    if score >= HEALTHY and (expanding or (isinstance(growth, (int, float))
                                           and growth >= STRONG_GROWTH_SCORE)):
        return "invest", ("healthy and growing on measured evidence — "
                          "compounding a proven curve")
    if isinstance(risk, (int, float)) and risk < WEAK \
            and isinstance(revenue, (int, float)) and revenue >= WEAK:
        return "fix", ("real revenue is exposed to elevated risk — protect "
                       "what is already earning")
    if declining and not expanding:
        return "question", ("declining with no growth signal — this needs a "
                            "strategic decision, not more spend")
    if score >= HEALTHY:
        return "maintain", "healthy and steady — no change indicated"
    return "watch", ("below the healthy threshold but without a decisive "
                     "signal either way")


def _group(items: list[dict], field: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for item in items:
        key = str(item.get(field) or "unknown")
        out[key] = out.get(key, 0) + 1
    return out

"""Product Review Engine — the review a product manager would write.

A structured, evidence-cited review per product:

    executive_summary · strengths · weaknesses · risks · recent_changes
    recommendations · evidence · confidence · action_items

Every section is assembled from what the platform already concluded — the
health engine's scores and reasons, the growth engine's findings, the strategy
engine's plays, the product's own history — so a review states nothing the
platform cannot show its working for. Where a section has no evidence it says
so explicitly rather than padding: "no weaknesses evidenced" is a finding, and
an empty section that pretends to be a clean bill of health is a lie.

Reviews are registered with the existing Report Review Center when one is
wired in, so an executive approves a product review through the same flow as
any other report. No second review pipeline is created.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.product.store import ProductStore, new_id, now_iso

logger = get_logger(__name__)

MAX_REVIEWS = 200
STRONG_DIMENSION = 70.0
WEAK_DIMENSION = 50.0

DIMENSION_LABELS = {
    "growth": "Growth", "risk": "Risk posture", "stability": "Stability",
    "adoption": "Adoption", "revenue": "Revenue",
    "satisfaction": "Customer satisfaction",
    "merchant_engagement": "Merchant engagement",
}


class ProductReviewEngine:
    """Generates structured product reviews from existing evidence."""

    def __init__(self, store: ProductStore, catalog, health_engine, growth,
                 strategy, reviews_center=None, bus=None):
        self._store = store
        self._catalog = catalog
        self._health = health_engine
        self._growth = growth
        self._strategy = strategy
        self._reviews = reviews_center  # the existing ReportReviewCenter
        self._bus = bus

    def attach_bus(self, bus) -> None:
        self._bus = bus

    # -------------------------------------------------------------- review
    def review(self, product_id: str, register: bool = False) -> dict:
        """Generate one product's review."""
        product = self._catalog.get(product_id)
        if product is None:
            raise KeyError(f"Unknown product: {product_id}")
        health = self._health.health(product_id) or {}
        findings = [f for f in self._growth.analyse()["findings"]
                    if f.get("product_id") == product_id]
        recommendations = self._strategy.recommendations(product_id=product_id,
                                                         status="open")

        review = {
            "review_id": new_id("prv"), "product_id": product_id,
            "product": product["name"], "lifecycle": product["lifecycle"],
            "owner": product["owner"],
            "executive_summary": self._summary(product, health, findings),
            "strengths": self._strengths(health, findings),
            "weaknesses": self._weaknesses(health),
            "risks": self._risks(health, findings),
            "recent_changes": self._changes(product, health),
            "recommendations": [
                {"recommendation": r["recommendation"],
                 "business_impact": r["business_impact"],
                 "priority": r["priority"], "effort": r["estimated_effort"],
                 "confidence": r["confidence"]}
                for r in recommendations[:5]],
            "evidence": health.get("evidence_ids", []),
            "evidence_summary": health.get("evidence_summary", {}),
            "confidence": health.get("confidence", 0.0),
            "action_items": self._actions(recommendations, health),
            "health_score": health.get("health_score"),
            "generated_at": now_iso(),
        }
        self._store.append("reviews", review, cap=MAX_REVIEWS)
        if register:
            self._register(review)
        self._announce(review)
        return review

    def review_all(self) -> dict[str, Any]:
        generated = []
        for product in self._catalog.products(status="active"):
            try:
                review = self.review(product["product_id"])
                generated.append(review["product"])
            except Exception:  # noqa: BLE001 — one product never stops the sweep
                logger.exception("Product review failed for %s",
                                 product["product_id"])
        return {"reviewed": len(generated), "products": generated}

    # ------------------------------------------------------------ sections
    def _summary(self, product: dict, health: dict,
                 findings: list[dict]) -> str:
        """A summary that states the position, not a mood."""
        name = product["name"]
        score = health.get("health_score")
        if score is None:
            return (f"{name} cannot be scored yet: the platform holds no KPIs, "
                    f"signals, or forecasts for it. Connect its data or "
                    f"associate it with a project to make it measurable.")
        band = health.get("band", "unknown")
        change = health.get("change")
        direction = ("unchanged" if not change
                     else f"{'up' if change > 0 else 'down'} "
                          f"{abs(change):.0f} points")
        declines = sum(1 for f in findings if f["kind"] == "declining_product")
        growth = sum(1 for f in findings if f["kind"] in ("growth_opportunity",
                                                          "expansion"))
        tail = ""
        if declines:
            tail = f" {declines} decline signal(s) need attention."
        elif growth:
            tail = f" {growth} growth opportunit(y/ies) are open."
        return (f"{name} is {band.replace('_', ' ')} at "
                f"{score:.0f}/100 ({direction}), in the "
                f"{product['lifecycle']} stage. Confidence in this assessment "
                f"is {health.get('confidence', 0):.0%} based on "
                f"{health.get('evidence_summary', {}).get('kpis', 0)} KPI(s) "
                f"and {health.get('evidence_summary', {}).get('signals', 0)} "
                f"signal(s).{tail}")

    def _strengths(self, health: dict, findings: list[dict]) -> list[dict]:
        out = []
        for dimension, score in (health.get("scores") or {}).items():
            if isinstance(score, (int, float)) and score >= STRONG_DIMENSION:
                out.append({
                    "strength": f"{DIMENSION_LABELS.get(dimension, dimension)} "
                                f"is strong ({score:.0f}/100)",
                    "evidence": health["reasons"].get(dimension, "")})
        for finding in findings:
            if finding["kind"] in ("growth_opportunity", "expansion"):
                out.append({"strength": finding["finding"],
                            "evidence": finding["detail"]})
        return out[:6] or [{"strength": "No strengths evidenced yet",
                            "evidence": "not enough measured data"}]

    def _weaknesses(self, health: dict) -> list[dict]:
        out = []
        for dimension, score in (health.get("scores") or {}).items():
            if isinstance(score, (int, float)) and score < WEAK_DIMENSION:
                out.append({
                    "weakness": f"{DIMENSION_LABELS.get(dimension, dimension)} "
                                f"is weak ({score:.0f}/100)",
                    "evidence": health["reasons"].get(dimension, "")})
            elif score is None:
                out.append({
                    "weakness": f"{DIMENSION_LABELS.get(dimension, dimension)} "
                                f"cannot be measured",
                    "evidence": health.get("reasons", {}).get(dimension, "")})
        return out[:6] or [{"weakness": "No weaknesses evidenced",
                            "evidence": "every measured dimension is at or "
                                        "above the watch threshold"}]

    def _risks(self, health: dict, findings: list[dict]) -> list[dict]:
        out = []
        risk_score = (health.get("scores") or {}).get("risk")
        if isinstance(risk_score, (int, float)) and risk_score < 60:
            out.append({"risk": f"Elevated risk ({risk_score:.0f}/100)",
                        "evidence": health["reasons"].get("risk", ""),
                        "severity": "high" if risk_score < 40 else "medium"})
        for finding in findings:
            if finding["kind"] in ("declining_product", "cannibalization"):
                out.append({"risk": finding["finding"],
                            "evidence": finding["detail"],
                            "severity": "high"
                            if finding["confidence"] >= 0.7 else "medium"})
        return out[:6] or [{"risk": "No risks evidenced", "evidence": "",
                            "severity": "none"}]

    def _changes(self, product: dict, health: dict) -> list[dict]:
        """What actually moved since the last review — from the product's own
        history and its health trend, both of which are recorded facts."""
        out = []
        change = health.get("change")
        if change:
            out.append({"change": f"Health {'rose' if change > 0 else 'fell'} "
                                  f"{abs(change):.0f} points to "
                                  f"{health['health_score']:.0f}",
                        "at": health.get("evaluated_at", "")})
        for entry in (product.get("history") or [])[-5:]:
            out.append({"change": f"{entry['change'].replace('_', ' ')}: "
                                  f"{entry['detail']}", "at": entry["at"]})
        return out[:6] or [{"change": "No changes recorded since the last "
                                      "review", "at": ""}]

    def _actions(self, recommendations: list[dict], health: dict) -> list[dict]:
        out = [{"action": r["recommendation"], "owner": "",
                "priority": r["priority"], "effort": r["estimated_effort"],
                "depends_on": r["dependencies"]}
               for r in recommendations[:5]]
        if health.get("health_score") is None:
            out.append({"action": "Connect this product's data so it can be "
                                  "measured", "owner": "", "priority": 2,
                        "effort": "small", "depends_on": []})
        return out

    # ------------------------------------------------------------ register
    def _register(self, review: dict) -> None:
        """Put the review into the executive's existing Report Review Center,
        so product reviews are approved the same way every other report is."""
        if self._reviews is None:
            return
        try:
            self._reviews.register(
                review["product_id"], 1,
                f"{review['product']} — product review",
                review.get("health_score"))
        except Exception:  # noqa: BLE001 — registration degrades, never fails
            logger.exception("Product review registration failed")

    def _announce(self, review: dict) -> None:
        if self._bus is None:
            return
        try:
            self._bus.publish("ProductReviewGenerated", {
                "product_id": review["product_id"],
                "product": review["product"],
                "health_score": review["health_score"],
                "risks": len([r for r in review["risks"]
                              if r["severity"] != "none"])},
                source="product_reviews")
        except Exception:  # noqa: BLE001
            logger.exception("Product review event publication failed")

    # ---------------------------------------------------------------- read
    def reviews(self, product_id: str = "", limit: int = 20) -> list[dict]:
        items = self._store.read("reviews")
        if product_id:
            items = [r for r in items if r["product_id"] == product_id]
        return list(reversed(items))[:limit]

    def latest(self, product_id: str) -> dict | None:
        found = self.reviews(product_id=product_id, limit=1)
        return found[0] if found else None

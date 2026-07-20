"""Strategic Recommendation Engine — what the business should actually do.

The platform already has a Recommendation Module (deterministic, data-focused:
"improve this data quality issue", "collect more history"). This engine works
one level up, in the language a product manager uses: improve onboarding,
reduce failures, increase merchant adoption, improve retention, expand
partnerships, optimize pricing, launch a campaign, improve reliability.

Every recommendation is **rule-derived from a growth finding or a health
score**, and carries the six things a manager needs to act:

    business_impact   what changes if this is done, in business terms
    confidence        inherited from the evidence, never asserted
    evidence          the ids behind it — a recommendation that cannot cite
                      does not get made
    priority          1 (now) … 5 (whenever)
    estimated_effort  small | medium | large
    dependencies      what must be true first

Recommendations do not execute themselves: each is handed to the existing
Decision Engine, which decides what a human must approve and routes it to the
Action Queue. This engine proposes; the autonomy layer disposes. No second
approval path is created here.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.product.store import ProductStore, new_id, now_iso

logger = get_logger(__name__)

PLAYS = ("improve_onboarding", "reduce_failures", "increase_merchant_adoption",
         "improve_retention", "expand_partnerships", "optimize_pricing",
         "launch_campaign", "improve_reliability", "investigate_decline",
         "scale_investment", "review_portfolio_gap")

EFFORTS = ("small", "medium", "large")
MAX_RECOMMENDATIONS = 200


class StrategicRecommendationEngine:
    """Turns product evidence into business recommendations."""

    def __init__(self, store: ProductStore, catalog, health_engine, growth,
                 gatherer, decisions=None, bus=None):
        self._store = store
        self._catalog = catalog
        self._health = health_engine
        self._growth = growth
        self._gatherer = gatherer
        self._decisions = decisions  # the existing runtime DecisionEngine
        self._bus = bus

    def attach_bus(self, bus) -> None:
        self._bus = bus

    def attach_decisions(self, decisions) -> None:
        """Route recommendations through the runtime's existing Decision
        Engine, which owns approval. Attached by the runtime, which is built
        after this engine."""
        self._decisions = decisions

    # ------------------------------------------------------------ generate
    def generate(self, route: bool = True) -> dict[str, Any]:
        """Derive recommendations from the current growth findings and health.

        ``route`` hands each one to the Decision Engine, which applies the
        confidence threshold and the approval policy that already exist.
        """
        analysis = self._growth.analyse()
        recommendations: list[dict] = []

        for finding in analysis["findings"]:
            recommendations += self._from_finding(finding)
        for record in self._health.all_health():
            recommendations += self._from_health(record)

        deduped = _dedupe(recommendations)
        stored = [self._save(r) for r in deduped]

        routed = 0
        if route and self._decisions is not None:
            routed = self._route(stored)
        return {"generated": len(stored), "routed_to_decisions": routed,
                "recommendations": stored[:50],
                "by_play": _count(stored, "play"),
                "generated_at": now_iso()}

    # -------------------------------------------------- rules from growth
    def _from_finding(self, finding: dict) -> list[dict]:
        kind = finding["kind"]
        product = finding["product"]
        cite = finding["evidence_ids"]
        confidence = finding["confidence"]

        if kind == "declining_product":
            return [_recommendation(
                "investigate_decline", product,
                f"Investigate and arrest the decline in {product}",
                business_impact=f"Stops further loss in {product}; the "
                                f"decline is measured, not suspected",
                confidence=confidence, evidence_ids=cite, priority=1,
                effort="medium",
                dependencies=["Root-cause analysis of the declining KPIs"],
                rationale=finding["finding"], product_id=finding["product_id"])]

        if kind == "cannibalization":
            return [_recommendation(
                "optimize_pricing", product,
                f"Review positioning and pricing where {product} overlaps "
                f"another product",
                business_impact="Recovers demand currently moving between "
                                "products rather than growing the portfolio",
                confidence=confidence, evidence_ids=cite, priority=2,
                effort="medium",
                dependencies=["Confirm the inverse correlation is causal, "
                              "not seasonal"],
                rationale=finding["finding"], product_id=finding["product_id"])]

        if kind == "cross_sell":
            return [_recommendation(
                "launch_campaign", product,
                f"Run a cross-sell campaign for {product} into the audience "
                f"it already shares with a stronger product",
                business_impact="Reaches a proven audience with no new "
                                "acquisition cost",
                confidence=confidence, evidence_ids=cite, priority=3,
                effort="small",
                dependencies=["Confirm the shared merchants/customers are "
                              "addressable"],
                rationale=finding["finding"], product_id=finding["product_id"])]

        if kind == "expansion":
            return [_recommendation(
                "scale_investment", product,
                f"Increase investment in {product} while it is growing",
                business_impact="Compounds a proven growth curve rather than "
                                "starting a new one",
                confidence=confidence, evidence_ids=cite, priority=2,
                effort="large",
                dependencies=["Capacity to support higher volume"],
                rationale=finding["finding"], product_id=finding["product_id"])]

        if kind == "growth_opportunity":
            return [_recommendation(
                "expand_partnerships", product,
                f"Extend distribution for {product} while its metrics are "
                f"rising",
                business_impact="Converts a measured upward trend into "
                                "durable share",
                confidence=confidence, evidence_ids=cite, priority=3,
                effort="medium", dependencies=[],
                rationale=finding["finding"], product_id=finding["product_id"])]

        if kind == "portfolio_gap":
            return [_recommendation(
                "review_portfolio_gap", product or "portfolio",
                f"Address the portfolio gap: {finding['finding'][:120]}",
                business_impact="Reduces dependence on a narrow set of "
                                "segments or a thin pipeline",
                confidence=confidence, evidence_ids=cite, priority=3,
                effort="large",
                dependencies=["Portfolio strategy review"],
                rationale=finding["finding"],
                product_id=finding.get("product_id", ""))]
        return []

    # -------------------------------------------------- rules from health
    def _from_health(self, record: dict) -> list[dict]:
        """A weak dimension is a specific play, not a general worry."""
        product = record["product"]
        scores = record["scores"] or {}
        cite = record.get("evidence_ids", [])
        confidence = record.get("confidence", 0.5)
        out = []

        def weak(dimension: str, threshold: float = 50.0) -> bool:
            score = scores.get(dimension)
            return isinstance(score, (int, float)) and score < threshold

        if weak("risk", 60):
            out.append(_recommendation(
                "improve_reliability", product,
                f"Improve reliability and reduce risk in {product}",
                business_impact="Protects revenue already being earned",
                confidence=confidence, evidence_ids=cite, priority=1,
                effort="medium",
                dependencies=["Engineering capacity"],
                rationale=record["reasons"].get("risk", ""),
                product_id=record["product_id"]))
        if weak("adoption"):
            out.append(_recommendation(
                "improve_onboarding", product,
                f"Improve onboarding and activation for {product}",
                business_impact="Converts existing demand that is not "
                                "currently reaching first use",
                confidence=confidence, evidence_ids=cite, priority=2,
                effort="medium", dependencies=[],
                rationale=record["reasons"].get("adoption", ""),
                product_id=record["product_id"]))
        if weak("satisfaction"):
            out.append(_recommendation(
                "improve_retention", product,
                f"Improve retention for {product}",
                business_impact="Retained customers cost less than acquired "
                                "ones",
                confidence=confidence, evidence_ids=cite, priority=2,
                effort="medium", dependencies=[],
                rationale=record["reasons"].get("satisfaction", ""),
                product_id=record["product_id"]))
        if weak("merchant_engagement"):
            out.append(_recommendation(
                "increase_merchant_adoption", product,
                f"Increase merchant adoption of {product}",
                business_impact="Merchant reach compounds transaction volume",
                confidence=confidence, evidence_ids=cite, priority=3,
                effort="medium", dependencies=[],
                rationale=record["reasons"].get("merchant_engagement", ""),
                product_id=record["product_id"]))
        if weak("stability", 60):
            out.append(_recommendation(
                "reduce_failures", product,
                f"Reduce failures and volatility in {product}",
                business_impact="Volatility suppresses both conversion and "
                                "forecast confidence",
                confidence=confidence, evidence_ids=cite, priority=1,
                effort="medium",
                dependencies=["Failure root-cause analysis"],
                rationale=record["reasons"].get("stability", ""),
                product_id=record["product_id"]))
        return out

    # ------------------------------------------------------------- routing
    def _route(self, recommendations: list[dict]) -> int:
        """Hand each recommendation to the existing Decision Engine, which
        owns evidence → confidence → priority → approval → execute → learn.
        This engine does not decide and does not execute."""
        routed = 0
        for recommendation in recommendations:
            if recommendation.get("decision_id"):
                continue  # already routed in an earlier pass
            try:
                decision = self._decisions.decide(
                    {"action": recommendation["recommendation"],
                     "confidence": recommendation["confidence"],
                     "priority": recommendation["priority"],
                     "evidence_ids": recommendation["evidence_ids"],
                     "expected_impact": recommendation["business_impact"]},
                    source="product_strategy")
                self._store.update("recommendations", "recommendation_id",
                                   recommendation["recommendation_id"],
                                   {"decision_id": decision["decision_id"],
                                    "decision_status": decision["status"]})
                routed += 1
            except Exception:  # noqa: BLE001 — one bad rec never stops the batch
                logger.exception("Routing recommendation to the decision "
                                 "engine failed")
        return routed

    # ---------------------------------------------------------------- read
    def _save(self, recommendation: dict) -> dict:
        with self._store.mutate("recommendations") as items:
            existing = next((r for r in items
                             if r["signature"] == recommendation["signature"]
                             and r["status"] == "open"), None)
            if existing is not None:
                # Re-derived from fresh evidence: refresh, do not duplicate.
                existing.update({
                    "confidence": recommendation["confidence"],
                    "evidence_ids": recommendation["evidence_ids"],
                    "rationale": recommendation["rationale"],
                    "priority": recommendation["priority"],
                    "updated_at": now_iso(), "observations":
                        existing.get("observations", 1) + 1})
                return existing
            items.append(recommendation)
            if len(items) > MAX_RECOMMENDATIONS:
                del items[:len(items) - MAX_RECOMMENDATIONS]
            return recommendation

    def recommendations(self, product_id: str = "", play: str = "",
                        status: str = "", limit: int = 100) -> list[dict]:
        items = self._store.read("recommendations")
        if product_id:
            items = [r for r in items if r["product_id"] == product_id]
        if play:
            items = [r for r in items if r["play"] == play]
        if status:
            items = [r for r in items if r["status"] == status]
        return sorted(items, key=lambda r: (r["priority"],
                                            -r["confidence"]))[:limit]

    def set_status(self, recommendation_id: str, status: str) -> dict | None:
        if status not in ("open", "accepted", "rejected", "done"):
            raise ValueError(f"Unknown recommendation status: {status}")
        return self._store.update("recommendations", "recommendation_id",
                                  recommendation_id, {"status": status})

    def stats(self) -> dict:
        items = self._store.read("recommendations")
        return {"total": len(items),
                "open": sum(1 for r in items if r["status"] == "open"),
                "by_play": _count(items, "play"),
                "by_priority": _count(items, "priority"),
                "routed": sum(1 for r in items if r.get("decision_id"))}


# --------------------------------------------------------------- utilities
def _recommendation(play: str, product: str, text: str, business_impact: str,
                    confidence: float, evidence_ids: list[str], priority: int,
                    effort: str, dependencies: list[str], rationale: str = "",
                    product_id: str = "") -> dict:
    if play not in PLAYS:
        raise ValueError(f"Unknown strategic play: {play}")
    if effort not in EFFORTS:
        raise ValueError(f"Unknown effort estimate: {effort}")
    if not evidence_ids:
        raise ValueError(
            f"Recommendation '{text[:60]}' cites no evidence — the strategy "
            f"engine may not make a claim the platform cannot support")
    return {
        "recommendation_id": new_id("rec"), "play": play,
        "product_id": product_id, "product": product,
        "recommendation": text[:300], "business_impact": business_impact[:300],
        "confidence": round(float(confidence), 3),
        "evidence_ids": evidence_ids[:8],
        "priority": max(1, min(int(priority), 5)), "estimated_effort": effort,
        "dependencies": dependencies[:5], "rationale": rationale[:300],
        "status": "open", "decision_id": "", "decision_status": "",
        "signature": f"{play}:{product_id or product}".lower(),
        "observations": 1, "created_at": now_iso(), "updated_at": now_iso(),
    }


def _dedupe(recommendations: list[dict]) -> list[dict]:
    """One play per product per pass: the highest-confidence instance wins."""
    best: dict[str, dict] = {}
    for recommendation in recommendations:
        signature = recommendation["signature"]
        current = best.get(signature)
        if current is None or recommendation["confidence"] > current["confidence"]:
            best[signature] = recommendation
    return sorted(best.values(),
                  key=lambda r: (r["priority"], -r["confidence"]))


def _count(items: list[dict], field: str) -> dict:
    out: dict[str, int] = {}
    for item in items:
        key = str(item.get(field))
        out[key] = out.get(key, 0) + 1
    return out

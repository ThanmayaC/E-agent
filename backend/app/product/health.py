"""Product Health Engine — how every product is actually doing.

Eight scores, each 0–100, each derived from evidence the platform already
produced and each carrying the reasons and evidence ids behind it:

    growth         KPI growth rates and forecast direction
    risk           anomalies, quality issues, failure KPIs (inverted)
    stability      anomaly load and forecast confidence
    adoption       adoption/usage KPI direction
    revenue        revenue KPI level and growth
    satisfaction   retention/satisfaction KPIs, inverted failure rates
    merchant       merchant-engagement KPIs and linked merchant count
    health         the weighted composite of the above

A score is **never invented**. Where the evidence does not support a
dimension, the score is ``None`` and the reason says so — "unknown" and "bad"
are different answers, and a product manager who cannot tell them apart makes
bad decisions. The composite is computed over the dimensions that *are*
known, with ``confidence`` reporting how much of the picture was visible.

Nothing here computes analytics: growth comes from the KPI module's
``growth_pct``, anomalies from the Analytics module's signals, forecast trust
from the Forecasting module's own confidence and validation gate.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.product.evidence import (
    ADOPTION_TERMS, ANOMALY, EvidenceGatherer, FAILURE_TERMS, MERCHANT_TERMS,
    ProductEvidence, RETENTION_TERMS, REVENUE_TERMS, VOLUME_TERMS,
)
from app.product.store import ProductStore, now_iso

logger = get_logger(__name__)

DIMENSIONS = ("growth", "risk", "stability", "adoption", "revenue",
              "satisfaction", "merchant_engagement")

# How much each dimension contributes to the composite. Growth and revenue
# dominate because a product manager is accountable for them; risk is heavily
# weighted because a high-risk product is unhealthy however fast it grows.
WEIGHTS = {"growth": 0.20, "risk": 0.20, "revenue": 0.20, "adoption": 0.15,
           "stability": 0.10, "satisfaction": 0.10, "merchant_engagement": 0.05}

NEUTRAL = 50.0          # the score of a dimension with no directional signal
STRONG_ANOMALY = 0.7    # matches the Analytics module's own threshold
MAX_HEALTH_HISTORY = 60


class ProductHealthEngine:
    """Evaluates every product against the evidence the platform holds."""

    def __init__(self, store: ProductStore, catalog, gatherer: EvidenceGatherer,
                 bus=None):
        self._store = store
        self._catalog = catalog
        self._gatherer = gatherer
        self._bus = bus

    def attach_bus(self, bus) -> None:
        self._bus = bus

    # ------------------------------------------------------------ evaluate
    def evaluate(self, product_id: str) -> dict:
        """Score one product. Returns the health record, evidence and all."""
        product = self._catalog.get(product_id)
        if product is None:
            raise KeyError(f"Unknown product: {product_id}")
        evidence = self._gatherer.gather(product)

        scores: dict[str, Any] = {}
        reasons: dict[str, str] = {}
        for dimension, compute in (
                ("growth", self._growth), ("risk", self._risk),
                ("stability", self._stability), ("adoption", self._adoption),
                ("revenue", self._revenue),
                ("satisfaction", self._satisfaction),
                ("merchant_engagement", self._merchant_engagement)):
            score, reason = compute(evidence)
            scores[dimension] = score
            reasons[dimension] = reason

        known = {d: s for d, s in scores.items() if s is not None}
        composite = (round(sum(scores[d] * WEIGHTS[d] for d in known)
                           / sum(WEIGHTS[d] for d in known), 1)
                     if known else None)
        confidence = round(sum(WEIGHTS[d] for d in known), 3) if known else 0.0

        record = {
            "product_id": product_id, "product": product["name"],
            "health_score": composite, "scores": scores, "reasons": reasons,
            "confidence": confidence,
            "band": _band(composite),
            "evidence_ids": evidence.cite(),
            "evidence_summary": evidence.describe(),
            "evaluated_at": now_iso(),
        }
        previous = self._store.get("health", "product_id", product_id)
        record["previous_health_score"] = (previous or {}).get("health_score")
        record["change"] = _change(record["health_score"],
                                   record["previous_health_score"])
        self._save(record)
        self._announce(record)
        return record

    def evaluate_all(self) -> dict[str, Any]:
        """The scheduler's job: re-score every active product."""
        evaluated, unscored = 0, []
        for product in self._catalog.products(status="active"):
            try:
                record = self.evaluate(product["product_id"])
                evaluated += 1
                if record["health_score"] is None:
                    unscored.append(product["name"])
            except Exception:  # noqa: BLE001 — one product never stops the sweep
                logger.exception("Health evaluation failed for %s",
                                 product["product_id"])
        return {"evaluated": evaluated, "unscored": unscored}

    # ---------------------------------------------------------- dimensions
    def _growth(self, evidence: ProductEvidence) -> tuple[float | None, str]:
        """KPI growth, corroborated by forecast direction."""
        rates = [k["growth_pct"] for k in evidence.kpis
                 if isinstance(k.get("growth_pct"), (int, float))]
        if not rates:
            return None, "no KPI carries a growth rate"
        average = sum(rates) / len(rates)
        # +20% growth reads as excellent, -20% as critical; linear between.
        score = _clamp(NEUTRAL + average * 2.5)
        reason = (f"mean KPI growth {average:+.1f}% across {len(rates)} KPI(s)")

        rising = sum(1 for f in evidence.forecasts
                     if str(f.get("status")) == "ok"
                     and _forecast_direction(f) > 0)
        if rising and evidence.forecasts:
            score = _clamp(score + 5)
            reason += f"; {rising} forecast(s) point up"
        return round(score, 1), reason

    def _risk(self, evidence: ProductEvidence) -> tuple[float | None, str]:
        """Risk is inverted into a score: 100 is safe. Anomalies, poor data
        quality, and failure KPIs all subtract."""
        if not evidence.has_facts:
            return None, "no evidence to assess risk from"
        score, parts = 100.0, []

        strong = [s for s in evidence.signals_of(ANOMALY)
                  if float(s.get("strength") or 0) >= STRONG_ANOMALY]
        if strong:
            score -= min(len(strong) * 12, 40)
            parts.append(f"{len(strong)} strong anomaly signal(s)")

        quality = evidence.quality.get("overall_score")
        if isinstance(quality, (int, float)) and quality < 80:
            score -= min((80 - quality) / 2, 25)
            parts.append(f"data quality {quality:.0f}/100")

        failures = evidence.kpis_matching(FAILURE_TERMS)
        rising_failures = [k for k in failures
                           if isinstance(k.get("growth_pct"), (int, float))
                           and k["growth_pct"] > 0]
        if rising_failures:
            score -= min(len(rising_failures) * 10, 30)
            parts.append(f"{len(rising_failures)} failure KPI(s) rising")

        verified_risks = sum(1 for i in evidence.insights
                             if str(i.get("statement_type")) == "risk")
        if verified_risks:
            score -= min(verified_risks * 5, 20)
            parts.append(f"{verified_risks} verified risk insight(s)")
        return round(_clamp(score), 1), "; ".join(parts) or "no risk signals"

    def _stability(self, evidence: ProductEvidence) -> tuple[float | None, str]:
        if not evidence.has_facts:
            return None, "no evidence to assess stability from"
        score, parts = 100.0, []
        anomalies = evidence.signals_of(ANOMALY)
        if anomalies:
            score -= min(len(anomalies) * 8, 45)
            parts.append(f"{len(anomalies)} anomaly signal(s)")
        confidences = [float(f["confidence"]) for f in evidence.forecasts
                       if isinstance(f.get("confidence"), (int, float))]
        if confidences:
            mean = sum(confidences) / len(confidences)
            score = score * (0.6 + 0.4 * mean)
            parts.append(f"mean forecast confidence {mean:.0%}")
        return round(_clamp(score), 1), "; ".join(parts) or "no volatility seen"

    def _adoption(self, evidence: ProductEvidence) -> tuple[float | None, str]:
        return self._directional(evidence, ADOPTION_TERMS + VOLUME_TERMS,
                                 "adoption/usage")

    def _revenue(self, evidence: ProductEvidence) -> tuple[float | None, str]:
        return self._directional(evidence, REVENUE_TERMS, "revenue")

    def _satisfaction(self, evidence: ProductEvidence
                      ) -> tuple[float | None, str]:
        """Retention and satisfaction KPIs, less any rising failure rate —
        the closest honest proxy the platform's own data supports."""
        retention = evidence.kpis_matching(RETENTION_TERMS)
        failures = evidence.kpis_matching(FAILURE_TERMS)
        if not retention and not failures:
            return None, ("no retention, satisfaction, or failure KPI is "
                          "discovered for this product")
        score, parts = NEUTRAL, []
        if retention:
            rates = [k["growth_pct"] for k in retention
                     if isinstance(k.get("growth_pct"), (int, float))]
            if rates:
                average = sum(rates) / len(rates)
                score = _clamp(NEUTRAL + average * 2.5)
                parts.append(f"retention KPIs {average:+.1f}%")
            else:
                parts.append(f"{len(retention)} retention KPI(s), no trend")
        if failures:
            rising = [k for k in failures
                      if isinstance(k.get("growth_pct"), (int, float))
                      and k["growth_pct"] > 0]
            if rising:
                score = _clamp(score - min(len(rising) * 12, 35))
                parts.append(f"{len(rising)} failure KPI(s) rising")
        return round(score, 1), "; ".join(parts)

    def _merchant_engagement(self, evidence: ProductEvidence
                             ) -> tuple[float | None, str]:
        kpis = evidence.kpis_matching(MERCHANT_TERMS)
        linked = len(evidence.product.get("merchants") or [])
        if not kpis and not linked:
            return None, "no merchant KPI or merchant association"
        score, parts = NEUTRAL, []
        if kpis:
            rates = [k["growth_pct"] for k in kpis
                     if isinstance(k.get("growth_pct"), (int, float))]
            if rates:
                average = sum(rates) / len(rates)
                score = _clamp(NEUTRAL + average * 2.5)
                parts.append(f"merchant KPIs {average:+.1f}%")
        if linked:
            score = _clamp(score + min(linked, 10))
            parts.append(f"{linked} merchant(s) associated")
        return round(score, 1), "; ".join(parts)

    def _directional(self, evidence: ProductEvidence, terms: tuple[str, ...],
                     label: str) -> tuple[float | None, str]:
        """The shared shape of a KPI-direction score: level is not knowable
        without a target, so direction is what can honestly be scored."""
        kpis = evidence.kpis_matching(terms)
        if not kpis:
            return None, f"no {label} KPI is discovered for this product"
        rates = [k["growth_pct"] for k in kpis
                 if isinstance(k.get("growth_pct"), (int, float))]
        if not rates:
            return NEUTRAL, (f"{len(kpis)} {label} KPI(s) present but no "
                             f"period-over-period trend")
        average = sum(rates) / len(rates)
        trend_up = sum(1 for k in kpis if k.get("trend") == "up")
        score = _clamp(NEUTRAL + average * 2.5)
        return round(score, 1), (f"{len(kpis)} {label} KPI(s), mean "
                                 f"{average:+.1f}%, {trend_up} trending up")

    # ---------------------------------------------------------------- read
    def health(self, product_id: str) -> dict | None:
        return self._store.get("health", "product_id", product_id)

    def all_health(self) -> list[dict]:
        return sorted(self._store.read("health"),
                      key=lambda h: (h["health_score"] is None,
                                     -(h["health_score"] or 0)))

    def _save(self, record: dict) -> None:
        with self._store.mutate("health") as items:
            for i, existing in enumerate(items):
                if existing["product_id"] == record["product_id"]:
                    history = existing.get("history", [])
                    history.append({"at": existing["evaluated_at"],
                                    "health_score": existing["health_score"]})
                    record["history"] = history[-MAX_HEALTH_HISTORY:]
                    items[i] = record
                    return
            record["history"] = []
            items.append(record)

    def _announce(self, record: dict) -> None:
        if self._bus is None:
            return
        try:
            self._bus.publish("ProductHealthEvaluated", {
                "product_id": record["product_id"],
                "product": record["product"],
                "health_score": record["health_score"],
                "change": record["change"], "band": record["band"]},
                source="product_health")
        except Exception:  # noqa: BLE001 — announcing never fails an evaluation
            logger.exception("Product health event publication failed")


# --------------------------------------------------------------- utilities
def _clamp(value: float) -> float:
    return max(0.0, min(100.0, value))


def _band(score: float | None) -> str:
    if score is None:
        return "unknown"
    if score >= 75:
        return "healthy"
    if score >= 50:
        return "watch"
    return "at_risk"


def _change(current: float | None, previous: float | None) -> float | None:
    if current is None or previous is None:
        return None
    return round(current - previous, 1)


def _forecast_direction(forecast: dict) -> float:
    """+1 when the forecast rises over its horizon, -1 when it falls."""
    values = forecast.get("values") or []
    if len(values) < 2:
        return 0.0
    try:
        return 1.0 if float(values[-1]) > float(values[0]) else -1.0
    except (TypeError, ValueError):
        return 0.0

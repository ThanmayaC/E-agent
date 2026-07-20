"""Scenario Simulation — "what happens if…", answered from real models.

A manager asks a business question:

    customer growth increases 15%      merchant failures increase 20%
    transaction volume decreases 10%   revenue drops 5%
    a new feature launches

and the platform answers by applying that change to the **actual KPI values
and the actual forecasts** the Forecasting Module already produced, then
reporting the projected outcome with the same confidence and validation the
underlying forecast carried.

Three rules keep this honest, and they are the whole design:

1. **Nothing is fabricated.** A scenario over a KPI the platform has never
   measured returns "cannot simulate", naming what is missing. It does not
   invent a baseline.
2. **Confidence is inherited, never asserted.** A projection is exactly as
   trustworthy as the forecast beneath it; where the Forecasting Module's
   validation gate says ``unavailable`` or ``low_confidence``, the scenario
   says so too and carries the same reasons.
3. **Assumptions are stated.** Every result lists what it assumed —
   crucially, that the relationship is linear and that nothing else moves,
   which is a modelling assumption, not a fact about the business.

A scenario is a projection, not a prediction, and this module says so in its
own output rather than leaving the manager to remember it.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.product.evidence import (
    ADOPTION_TERMS, CUSTOMER_TERMS, EvidenceGatherer, FAILURE_TERMS,
    MERCHANT_TERMS, REVENUE_TERMS, VOLUME_TERMS,
)
from app.product.store import ProductStore, new_id, now_iso

logger = get_logger(__name__)

# The business levers a manager can pull, and the KPI vocabulary each one
# addresses. A lever maps to metrics the KPI module already discovered — this
# is a lookup, not a model.
LEVERS = {
    "customer_growth": CUSTOMER_TERMS + ADOPTION_TERMS,
    "merchant_failures": FAILURE_TERMS,
    "merchant_engagement": MERCHANT_TERMS,
    "transaction_volume": VOLUME_TERMS,
    "revenue": REVENUE_TERMS,
    "feature_launch": ADOPTION_TERMS,
}

# How a lever propagates. Each factor says: a 1% move in the lever moves this
# KPI family by N%. These are declared modelling assumptions, surfaced in
# every result, not hidden constants — a manager can see and discount them.
PROPAGATION = {
    "customer_growth": {"revenue": 0.8, "volume": 0.9, "adoption": 1.0},
    "merchant_failures": {"revenue": -0.6, "volume": -0.7,
                          "satisfaction": -0.8},
    "merchant_engagement": {"revenue": 0.5, "volume": 0.6},
    "transaction_volume": {"revenue": 0.9, "volume": 1.0},
    "revenue": {"revenue": 1.0},
    "feature_launch": {"adoption": 1.0, "revenue": 0.3},
}

FAMILIES = {"revenue": REVENUE_TERMS, "volume": VOLUME_TERMS,
            "adoption": ADOPTION_TERMS, "satisfaction": FAILURE_TERMS}

MAX_SCENARIOS = 100


class ScenarioSimulation:
    """Deterministic what-if analysis over existing KPIs and forecasts."""

    def __init__(self, store: ProductStore, catalog, gatherer: EvidenceGatherer,
                 bus=None):
        self._store = store
        self._catalog = catalog
        self._gatherer = gatherer
        self._bus = bus

    def attach_bus(self, bus) -> None:
        self._bus = bus

    # ------------------------------------------------------------ simulate
    def simulate(self, lever: str, change_pct: float, product_id: str = "",
                 question: str = "", persist: bool = True) -> dict[str, Any]:
        """Apply a change to a business lever and project the outcome.

        Returns a scenario record: the projections, their confidence, the
        evidence they rest on, and the assumptions they required.
        """
        if lever not in LEVERS:
            raise ValueError(
                f"Unknown scenario lever: {lever}. Known levers: "
                f"{', '.join(sorted(LEVERS))}")
        products = ([self._require(product_id)] if product_id
                    else self._catalog.products(status="active"))
        if not products:
            return self._unsimulatable(lever, change_pct, question,
                                       "no active products to simulate")

        projections, cited, unsimulatable = [], [], []
        for product in products:
            evidence = self._gatherer.gather(product)
            baseline = evidence.kpis_matching(LEVERS[lever])
            if not baseline:
                unsimulatable.append(
                    f"{product['name']}: no KPI measures '{lever}'")
                continue
            projections += self._project(product, evidence, lever, change_pct)
            cited += evidence.cite(4)

        if not projections:
            return self._unsimulatable(
                lever, change_pct, question,
                "; ".join(unsimulatable[:5])
                or "no measured KPI matches this lever")

        confidence = round(
            sum(p["confidence"] for p in projections) / len(projections), 3)
        scenario = {
            "scenario_id": new_id("scn"),
            "question": question or _question(lever, change_pct),
            "lever": lever, "change_pct": round(float(change_pct), 2),
            "product_id": product_id,
            "projections": projections[:25],
            "summary": self._summary(lever, change_pct, projections),
            "confidence": confidence,
            "evidence_ids": list(dict.fromkeys(cited))[:8],
            "assumptions": self._assumptions(lever),
            "unsimulatable": unsimulatable[:5],
            "simulated_at": now_iso(),
        }
        if persist:
            self._store.append("scenarios", scenario, cap=MAX_SCENARIOS)
        self._announce(scenario)
        return scenario

    def _project(self, product: dict, evidence, lever: str,
                 change_pct: float) -> list[dict]:
        """Move each affected KPI family by the lever's declared factor."""
        out = []
        for family, factor in PROPAGATION[lever].items():
            for kpi in evidence.kpis_matching(FAMILIES[family]):
                current = kpi.get("current_value")
                if not isinstance(current, (int, float)):
                    continue
                delta_pct = change_pct * factor
                projected = current * (1 + delta_pct / 100)
                forecast = _forecast_for(evidence, kpi)
                confidence, basis = _confidence_of(forecast)
                out.append({
                    "product": product["name"],
                    "product_id": product["product_id"],
                    "kpi": kpi.get("name"), "family": family,
                    "current_value": round(float(current), 2),
                    "projected_value": round(float(projected), 2),
                    "change_pct": round(delta_pct, 2),
                    "absolute_change": round(float(projected - current), 2),
                    "unit": kpi.get("unit", ""),
                    "factor": factor,
                    "confidence": confidence, "confidence_basis": basis,
                    "forecast_status": (forecast or {}).get("status",
                                                            "no_forecast"),
                    "forecast_validation": (forecast or {}).get("validation",
                                                               []),
                })
        return out

    def _summary(self, lever: str, change_pct: float,
                 projections: list[dict]) -> str:
        revenue = [p for p in projections if p["family"] == "revenue"]
        direction = "increases" if change_pct > 0 else "decreases"
        if revenue:
            total = sum(p["absolute_change"] for p in revenue)
            way = "rise" if total > 0 else "fall"
            return (f"If {lever.replace('_', ' ')} {direction} by "
                    f"{abs(change_pct):.0f}%, revenue-related metrics would "
                    f"{way} by about {abs(total):,.0f} across "
                    f"{len(revenue)} KPI(s), assuming the relationship holds "
                    f"linearly and nothing else changes.")
        return (f"If {lever.replace('_', ' ')} {direction} by "
                f"{abs(change_pct):.0f}%, {len(projections)} measured KPI(s) "
                f"would move; no revenue KPI is affected directly.")

    def _assumptions(self, lever: str) -> list[str]:
        factors = ", ".join(f"{family} × {factor}"
                            for family, factor in PROPAGATION[lever].items())
        return [
            "The relationship is linear over the range simulated — real "
            "elasticity is rarely linear, so treat large swings with care.",
            "Nothing else moves: no seasonality, no competitive response, no "
            "capacity limit.",
            f"Declared propagation factors: {factors}.",
            "Projections inherit the confidence of the underlying forecast; a "
            "KPI without a validated forecast carries low confidence.",
        ]

    def _unsimulatable(self, lever: str, change_pct: float, question: str,
                       reason: str) -> dict:
        """The honest answer when the platform cannot support the question."""
        return {"scenario_id": new_id("scn"),
                "question": question or _question(lever, change_pct),
                "lever": lever, "change_pct": round(float(change_pct), 2),
                "projections": [], "summary":
                    f"This scenario cannot be simulated: {reason}. The "
                    f"platform will not estimate an outcome it has no "
                    f"measurement for.",
                "confidence": 0.0, "evidence_ids": [],
                "assumptions": [], "unsimulatable": [reason],
                "simulated_at": now_iso()}

    def _require(self, product_id: str) -> dict:
        product = self._catalog.get(product_id)
        if product is None:
            raise KeyError(f"Unknown product: {product_id}")
        return product

    def _announce(self, scenario: dict) -> None:
        if self._bus is None:
            return
        try:
            self._bus.publish("ScenarioSimulated", {
                "scenario_id": scenario["scenario_id"],
                "lever": scenario["lever"],
                "change_pct": scenario["change_pct"],
                "confidence": scenario["confidence"],
                "projections": len(scenario["projections"])},
                source="scenario_simulation")
        except Exception:  # noqa: BLE001
            logger.exception("Scenario event publication failed")

    # ---------------------------------------------------------------- read
    def levers(self) -> list[dict]:
        """What can be asked, and what each lever moves."""
        return [{"lever": lever,
                 "question": _question(lever, 10),
                 "affects": list(PROPAGATION[lever]),
                 "factors": PROPAGATION[lever]}
                for lever in sorted(LEVERS)]

    def scenarios(self, limit: int = 20) -> list[dict]:
        return list(reversed(self._store.read("scenarios")))[:limit]


# --------------------------------------------------------------- utilities
def _question(lever: str, change_pct: float) -> str:
    direction = "increases" if change_pct > 0 else "decreases"
    return (f"What happens if {lever.replace('_', ' ')} {direction} by "
            f"{abs(change_pct):.0f}%?")


def _forecast_for(evidence, kpi: dict) -> dict | None:
    kpi_id = kpi.get("id") or kpi.get("kpi_id")
    name = kpi.get("name")
    for forecast in evidence.forecasts:
        if (kpi_id and forecast.get("kpi_id") == kpi_id) \
                or (name and forecast.get("kpi_name") == name):
            return forecast
    return None


def _confidence_of(forecast: dict | None) -> tuple[float, str]:
    """A projection is exactly as trustworthy as the forecast under it."""
    if forecast is None:
        return 0.3, ("no forecast exists for this KPI — the projection is "
                     "arithmetic on the current value only")
    status = str(forecast.get("status", "ok"))
    confidence = float(forecast.get("confidence") or 0)
    if status == "unavailable":
        return 0.2, ("the forecasting module could not validate a forecast "
                     "for this KPI")
    if status == "low_confidence":
        reasons = ", ".join(forecast.get("validation") or []) or "not stated"
        return round(min(confidence, 0.4), 3), (
            f"the underlying forecast is low confidence ({reasons})")
    return round(confidence, 3), (
        f"inherited from a validated {forecast.get('method', 'forecast')} "
        f"forecast")

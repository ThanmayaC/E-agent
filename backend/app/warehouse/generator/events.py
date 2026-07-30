"""Ecosystem events — the things that actually put shape into a payments chart.

A production UPI series is a smooth-ish trend interrupted by *events*: an issuer
goes down for six hours, a PSP ships a bad release, a merchant runs a cashback
campaign, a fraud ring finds a hole in a new product, the switch degrades and
latency triples, a regulator caps a product and volume steps down overnight.

Each event here declares which entity it hits, when, how hard, and what shape
the impact takes over its lifetime. The simulator applies them multiplicatively
to volume, success rate and latency, and the same event list is written out as
a ground-truth incident table — so anomaly detection and root-cause analysis
can be *scored*, not just asserted.
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass, field

from app.warehouse.generator.catalog import BANKS, MCCS, PRODUCTS, PSPS

# Impact profiles over an event's lifetime, sampled at t in [0, 1].
_SHAPES = {
    # Sudden failure, slow recovery — the classic outage.
    "outage": lambda t: math.exp(-3.2 * t) if t > 0 else 1.0,
    # Ramp up, plateau, ramp down — a campaign.
    "campaign": lambda t: math.sin(math.pi * min(1.0, max(0.0, t))) ** 0.6,
    # Step change that persists — a regulatory or pricing change.
    "step": lambda t: 1.0,
    # Slow build then sharp cut — a fraud ring being found and shut down.
    "fraud": lambda t: (t / 0.75) ** 1.6 if t < 0.75 else max(
        0.0, 1.0 - (t - 0.75) / 0.25),
    # Spike and immediate decay — a switch latency incident.
    "spike": lambda t: math.exp(-6.0 * t),
    # Gradual decay to nothing — dormancy / churn wave.
    "decay": lambda t: 1.0 - t,
}


@dataclass
class Event:
    event_id: str
    kind: str                    # bank_outage | psp_degradation | ...
    shape: str
    title: str
    start_day: int
    duration: int
    severity: str                # Sev-1 | Sev-2 | Sev-3
    scope: dict                  # {'bank': .., 'psp': .., 'product': .., ...}
    volume_impact: float         # multiplicative delta at peak (0.0 = none)
    success_impact: float        # percentage points at peak (negative = worse)
    latency_impact: float        # multiplier at peak
    fraud_impact: float = 0.0    # extra risk-decline propensity at peak
    narrative: str = ""
    detected_day: int | None = None
    resolved_day: int | None = None

    @property
    def end_day(self) -> int:
        return self.start_day + self.duration - 1

    def intensity(self, day: int) -> float:
        """0..1 impact weight for a given day of the simulation."""
        if not (self.start_day <= day <= self.end_day):
            return 0.0
        t = (day - self.start_day) / max(1, self.duration - 1) \
            if self.duration > 1 else 0.0
        sev = {"Sev-1": 1.0, "Sev-2": 0.66, "Sev-3": 0.38}[self.severity]
        return sev * max(0.0, _SHAPES[self.shape](t))

    def matches(self, *, product: str | None = None, bank: str | None = None,
                psp: str | None = None, mcc: str | None = None,
                region: str | None = None) -> bool:
        """An event applies when every scope key it declares is satisfied."""
        s = self.scope
        if "product" in s and product != s["product"]:
            return False
        if "products" in s and product not in s["products"]:
            return False
        if "bank" in s and bank != s["bank"]:
            return False
        if "psp" in s and psp != s["psp"]:
            return False
        if "mcc" in s and mcc != s["mcc"]:
            return False
        if "region" in s and region != s["region"]:
            return False
        return True

    def to_row(self, start_date) -> dict:
        from datetime import timedelta
        return {
            "event_id": self.event_id,
            "kind": self.kind,
            "title": self.title,
            "severity": self.severity,
            "start_date": str(start_date + timedelta(days=self.start_day)),
            "end_date": str(start_date + timedelta(days=self.end_day)),
            "duration_days": self.duration,
            "scope_product": self.scope.get("product") or ",".join(
                self.scope.get("products", [])) or None,
            "scope_bank": self.scope.get("bank"),
            "scope_psp": self.scope.get("psp"),
            "scope_mcc": self.scope.get("mcc"),
            "scope_region": self.scope.get("region"),
            "volume_impact_pct": round(self.volume_impact * 100, 2),
            "success_impact_pp": round(self.success_impact, 3),
            "latency_impact_x": round(self.latency_impact, 3),
            "detected_date": str(start_date + timedelta(days=self.detected_day))
            if self.detected_day is not None else None,
            "narrative": self.narrative,
        }


class EventPlanner:
    """Seeds a realistic incident/campaign calendar across the window."""

    def __init__(self, rng: random.Random, days: int):
        self.rng = rng
        self.days = days
        self.events: list[Event] = []
        self._n = 0

    def _id(self, prefix: str) -> str:
        self._n += 1
        return f"{prefix}-{self._n:04d}"

    def _add(self, **kw) -> Event:
        ev = Event(**kw)
        # Detection lags the start: bigger incidents are caught faster.
        lag = {"Sev-1": 0, "Sev-2": self.rng.randint(0, 1),
               "Sev-3": self.rng.randint(1, 3)}[ev.severity]
        ev.detected_day = min(ev.end_day, ev.start_day + lag)
        self.events.append(ev)
        return ev

    # ------------------------------------------------------------------ plan
    def plan(self) -> list[Event]:
        self._bank_outages()
        self._psp_degradations()
        self._switch_latency()
        self._fraud_rings()
        self._merchant_campaigns()
        self._product_regime_changes()
        self._dormancy_waves()
        self._adoption_surges()
        self._market_corrections()
        self._settlement_incidents()
        self.events.sort(key=lambda e: e.start_day)
        return self.events

    # ---------------------------------------------------------- bank outages
    def _bank_outages(self) -> None:
        rng = self.rng
        # ~1 material issuer outage every 9 days somewhere in the ecosystem.
        for _ in range(max(3, self.days // 9)):
            bank = rng.choices(BANKS, weights=[b["share"] ** 0.5
                                               for b in BANKS])[0]
            sev = rng.choices(["Sev-1", "Sev-2", "Sev-3"],
                              weights=[0.14, 0.42, 0.44])[0]
            dur = {"Sev-1": rng.randint(1, 2), "Sev-2": rng.randint(1, 3),
                   "Sev-3": rng.randint(2, 5)}[sev]
            start = rng.randint(0, max(0, self.days - dur - 1))
            drop = {"Sev-1": rng.uniform(0.34, 0.62),
                    "Sev-2": rng.uniform(0.14, 0.32),
                    "Sev-3": rng.uniform(0.04, 0.12)}[sev]
            self._add(
                event_id=self._id("INC-BANK"), kind="bank_outage",
                shape="outage",
                title=f"{bank['name']} issuer decline spike",
                start_day=start, duration=dur, severity=sev,
                scope={"bank": bank["name"]},
                volume_impact=-drop * 0.55,
                success_impact=-drop * 26.0,
                latency_impact=1.0 + drop * 1.9,
                narrative=(
                    f"{bank['name']} core banking reported elevated U30/U28 "
                    f"declines. Remitter-side debit failures rose sharply and "
                    f"PSPs began routing retries, lifting p95 latency."))

    # ------------------------------------------------------ PSP degradations
    def _psp_degradations(self) -> None:
        rng = self.rng
        for _ in range(max(2, self.days // 16)):
            psp = rng.choices(PSPS, weights=[p["share"] ** 0.4
                                             for p in PSPS])[0]
            sev = rng.choices(["Sev-1", "Sev-2", "Sev-3"],
                              weights=[0.10, 0.40, 0.50])[0]
            dur = rng.randint(1, 4)
            start = rng.randint(0, max(0, self.days - dur - 1))
            drop = {"Sev-1": rng.uniform(0.30, 0.55),
                    "Sev-2": rng.uniform(0.12, 0.28),
                    "Sev-3": rng.uniform(0.03, 0.10)}[sev]
            self._add(
                event_id=self._id("INC-PSP"), kind="psp_degradation",
                shape="outage",
                title=f"{psp['name']} app release regression",
                start_day=start, duration=dur, severity=sev,
                scope={"psp": psp["name"]},
                volume_impact=-drop * 0.72,
                success_impact=-drop * 18.0,
                latency_impact=1.0 + drop * 2.6,
                narrative=(
                    f"A {psp['name']} client release degraded the collect and "
                    f"intent flows. Volume shifted to competing apps for the "
                    f"duration and returned only partially after rollback."))

    # ------------------------------------------------------ switch / network
    def _switch_latency(self) -> None:
        rng = self.rng
        for _ in range(max(2, self.days // 22)):
            dur = rng.randint(1, 3)
            start = rng.randint(0, max(0, self.days - dur - 1))
            mag = rng.uniform(1.7, 3.4)
            self._add(
                event_id=self._id("INC-NET"), kind="network_latency",
                shape="spike",
                title="NPCI switch latency degradation",
                start_day=start, duration=dur,
                severity="Sev-1" if mag > 2.8 else "Sev-2",
                scope={},
                volume_impact=-0.06 * (mag - 1),
                success_impact=-1.8 * (mag - 1),
                latency_impact=mag,
                narrative=(
                    "Central switch p95 response time degraded across all "
                    "PSPs. Timeout-class declines (BT, U54) rose ecosystem-"
                    "wide with no single issuer or app responsible."))

    # ------------------------------------------------------------ fraud rings
    def _fraud_rings(self) -> None:
        rng = self.rng
        risky = [p for p in PRODUCTS if p.lifecycle in ("hyper", "growth")]
        for _ in range(max(2, self.days // 34)):
            prod = rng.choice(risky)
            mcc = rng.choices(MCCS, weights=[m.risk for m in MCCS])[0]
            dur = rng.randint(4, 12)
            start = rng.randint(0, max(0, self.days - dur - 1))
            self._add(
                event_id=self._id("INC-FRAUD"), kind="fraud_spike",
                shape="fraud",
                title=f"Fraud pattern on {prod.name} — {mcc.subcategory}",
                start_day=start, duration=dur,
                severity=rng.choice(["Sev-1", "Sev-2"]),
                scope={"product": prod.code, "mcc": mcc.code},
                volume_impact=rng.uniform(0.05, 0.18),
                success_impact=-rng.uniform(0.8, 2.4),
                latency_impact=1.05,
                fraud_impact=rng.uniform(3.5, 9.0),
                narrative=(
                    f"Coordinated fraud attempts concentrated on {prod.name} "
                    f"at {mcc.subcategory} merchants. Risk declines (U16/K1) "
                    f"climbed until rules were tightened and the ring was "
                    f"shut down."))

    # ------------------------------------------------------ merchant campaigns
    def _merchant_campaigns(self) -> None:
        rng = self.rng
        for _ in range(max(4, self.days // 11)):
            mcc = rng.choices(MCCS, weights=[m.share for m in MCCS])[0]
            dur = rng.randint(3, 9)
            start = rng.randint(0, max(0, self.days - dur - 1))
            lift = rng.uniform(0.22, 0.85)
            self._add(
                event_id=self._id("CMP"), kind="merchant_campaign",
                shape="campaign",
                title=f"{mcc.subcategory} cashback campaign",
                start_day=start, duration=dur, severity="Sev-3",
                scope={"mcc": mcc.code},
                volume_impact=lift,
                success_impact=-0.25 * lift,
                latency_impact=1.0 + 0.18 * lift,
                narrative=(
                    f"A cashback campaign across {mcc.subcategory} merchants "
                    f"lifted volume sharply. Ticket sizes fell as customers "
                    f"split baskets to maximise the offer."))

    # ------------------------------------------------- product regime changes
    def _product_regime_changes(self) -> None:
        rng = self.rng
        # A per-transaction limit hike is a permanent step change in volume/ticket.
        lite = next(p for p in PRODUCTS if p.code == "UPI_LITE")
        start = int(self.days * 0.42)
        self._add(
            event_id=self._id("REG"), kind="regulatory_change", shape="step",
            title="UPI Lite per-transaction cap raised to ₹1,000",
            start_day=start, duration=self.days - start, severity="Sev-3",
            scope={"product": lite.code},
            volume_impact=0.26, success_impact=0.18, latency_impact=1.0,
            narrative=(
                "The Lite per-transaction cap was raised, moving a band of "
                "small-ticket payments off the full UPI rail onto Lite. Lite "
                "volume steps up permanently and average ticket rises."))

        intl = next(p for p in PRODUCTS if p.code == "UPI_INTL")
        s2 = int(self.days * 0.63)
        self._add(
            event_id=self._id("REG"), kind="corridor_launch", shape="step",
            title="UPI International — two new acceptance corridors live",
            start_day=s2, duration=self.days - s2, severity="Sev-3",
            scope={"product": intl.code},
            volume_impact=0.54, success_impact=-0.55, latency_impact=1.12,
            narrative=(
                "Two new cross-border acceptance corridors went live. Volume "
                "steps up; early-corridor settlement immaturity temporarily "
                "depresses the success rate."))

        circle = next(p for p in PRODUCTS if p.code == "UPI_CIRCLE")
        s3 = int(self.days * 0.28)
        self._add(
            event_id=self._id("REG"), kind="feature_launch", shape="step",
            title="UPI Circle full-delegation rollout to all PSPs",
            start_day=s3, duration=self.days - s3, severity="Sev-3",
            scope={"product": circle.code},
            volume_impact=0.88, success_impact=0.42, latency_impact=0.96,
            narrative=(
                "Full-delegation Circle became available across every major "
                "PSP, converting the pilot cohort into mainstream volume."))

        rupay = next(p for p in PRODUCTS if p.code == "RUPAY_CREDIT")
        s4 = int(self.days * 0.75)
        self._add(
            event_id=self._id("REG"), kind="pricing_change", shape="step",
            title="MDR reinstated on RuPay Credit above ₹2,000",
            start_day=s4, duration=self.days - s4, severity="Sev-2",
            scope={"product": rupay.code},
            volume_impact=-0.17, success_impact=0.10, latency_impact=1.0,
            narrative=(
                "Merchant discount rate reinstated on higher-value RuPay "
                "Credit transactions. Large-ticket volume moved back to "
                "debit-funded rails; the product's average ticket falls."))

    # --------------------------------------------------------- dormancy waves
    def _dormancy_waves(self) -> None:
        rng = self.rng
        for _ in range(2):
            dur = rng.randint(10, 20)
            start = rng.randint(0, max(0, self.days - dur - 1))
            region = rng.choice(["North", "South", "East", "West", "Central"])
            self._add(
                event_id=self._id("DORM"), kind="dormancy_wave", shape="decay",
                title=f"{region} region customer dormancy wave",
                start_day=start, duration=dur, severity="Sev-3",
                scope={"region": region},
                volume_impact=-rng.uniform(0.10, 0.22),
                success_impact=0.05, latency_impact=1.0,
                narrative=(
                    f"A cohort of {region}-region customers went inactive "
                    f"after a competing wallet promotion. Per-customer "
                    f"transaction frequency fell without any success-rate "
                    f"degradation — a demand problem, not a reliability one."))

    # -------------------------------------------------------- adoption surges
    def _adoption_surges(self) -> None:
        rng = self.rng
        for code in ("UPI_LITE", "UPI_CREDIT_LINE", "UPI_AUTOPAY"):
            dur = rng.randint(8, 16)
            start = rng.randint(int(self.days * 0.2),
                                max(int(self.days * 0.2) + 1,
                                    self.days - dur - 1))
            self._add(
                event_id=self._id("ADOPT"), kind="adoption_surge",
                shape="campaign",
                title=f"{code.replace('_', ' ').title()} onboarding push",
                start_day=start, duration=dur, severity="Sev-3",
                scope={"product": code},
                volume_impact=rng.uniform(0.18, 0.42),
                success_impact=-rng.uniform(0.1, 0.5),
                latency_impact=1.04,
                narrative=(
                    "A coordinated PSP onboarding push drove a step-in of "
                    "first-time users. New-user cohorts transact at lower "
                    "ticket sizes and slightly lower success rates."))

    # ----------------------------------------------------- market corrections
    def _market_corrections(self) -> None:
        rng = self.rng
        for _ in range(2):
            dur = rng.randint(5, 11)
            start = rng.randint(int(self.days * 0.15),
                                max(int(self.days * 0.15) + 1,
                                    self.days - dur - 1))
            self._add(
                event_id=self._id("MKT"), kind="market_correction",
                shape="campaign",
                title="Discretionary spend correction",
                start_day=start, duration=dur, severity="Sev-3",
                scope={"products": ["UPI_CREDIT_LINE", "RUPAY_CREDIT",
                                    "UPI_P2M", "UPI_INTL"]},
                volume_impact=-rng.uniform(0.09, 0.19),
                success_impact=-0.15, latency_impact=1.0,
                narrative=(
                    "A broad pull-back in discretionary spending compressed "
                    "credit-funded and high-ticket merchant volume while "
                    "essential categories held flat."))

    # ---------------------------------------------------- settlement failures
    def _settlement_incidents(self) -> None:
        rng = self.rng
        for _ in range(max(2, self.days // 40)):
            dur = rng.randint(1, 3)
            start = rng.randint(0, max(0, self.days - dur - 1))
            self._add(
                event_id=self._id("INC-SETL"), kind="settlement_delay",
                shape="outage",
                title="Mandate settlement batch delay",
                start_day=start, duration=dur, severity="Sev-2",
                scope={"products": ["UPI_AUTOPAY", "UPI_RECURRING",
                                    "UPI_LITE_ATU"]},
                volume_impact=-rng.uniform(0.18, 0.38),
                success_impact=-rng.uniform(2.5, 6.5),
                latency_impact=1.6,
                narrative=(
                    "The overnight mandate execution batch ran late, pushing "
                    "debits past the pre-debit notification window. Failed "
                    "mandates were re-presented the following day, producing "
                    "a retry spike."))


def active_multipliers(events: list[Event], day: int, *, product: str,
                       bank: str | None = None, psp: str | None = None,
                       mcc: str | None = None, region: str | None = None
                       ) -> tuple[float, float, float, float]:
    """Combined (volume_mult, success_delta_pp, latency_mult, fraud_delta)."""
    vol, succ, lat, fraud = 1.0, 0.0, 1.0, 0.0
    for ev in events:
        w = ev.intensity(day)
        if w <= 0 or not ev.matches(product=product, bank=bank, psp=psp,
                                    mcc=mcc, region=region):
            continue
        vol *= 1.0 + ev.volume_impact * w
        succ += ev.success_impact * w
        lat *= 1.0 + (ev.latency_impact - 1.0) * w
        fraud += ev.fraud_impact * w
    return max(0.05, vol), succ, max(0.4, lat), fraud

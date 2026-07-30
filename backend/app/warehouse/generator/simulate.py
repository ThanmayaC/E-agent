"""The transaction simulator.

Produces raw, transaction-level records — one row per payment attempt — for
every NPCI product across the whole window. Nothing is aggregated here and no
KPI is asserted: success rates, ticket sizes, growth and seasonality are all
*emergent* from per-transaction outcomes, which is the only way downstream
analytics and ML can be honest about what the data says.

The daily volume of a product is a multiplicative decomposition:

    volume = base × adoption(t) × calendar(day) × events(day) × AR(1) noise

and each transaction then draws its own bank, PSP, merchant, MCC, customer,
amount, latency and outcome conditioned on that day's state. Mandate products
are not sampled at all — they execute from the mandate book.
"""
from __future__ import annotations

import math
from datetime import date, timedelta

import numpy as np

from app.warehouse.generator.calendar_in import DayContext
from app.warehouse.generator.catalog import (
    BANKS, CHANNELS, CITIES, DEVICES, FAILURE_BY_BUCKET, MCCS,
    PRODUCT_MCC_AFFINITY, PRODUCTS, PSPS, SEGMENTS,
)
from app.warehouse.generator.events import Event

_BUCKETS = ("technical", "business", "risk", "timeout")

# Intraday shape by product family. Real UPI has a double hump (late-morning
# and evening); mandates fire in the overnight batch; 123Pay skews to daytime.
_HOUR_PROFILES: dict[str, list[float]] = {
    "consumer": [0.9, 0.5, 0.3, 0.3, 0.4, 0.8, 1.9, 3.2, 4.4, 5.4, 6.1, 6.4,
                 6.0, 5.2, 4.7, 4.8, 5.3, 6.2, 7.1, 7.4, 6.3, 4.6, 2.8, 1.5],
    "mandate": [6.2, 9.8, 14.1, 13.0, 9.4, 6.1, 4.6, 3.4, 2.8, 2.4, 2.1, 2.0,
                1.9, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.1, 1.8, 1.5, 1.2, 0.9],
    "credit": [0.6, 0.4, 0.3, 0.3, 0.3, 0.6, 1.4, 2.6, 3.9, 5.1, 6.0, 6.5,
               6.2, 5.6, 5.2, 5.4, 5.9, 6.6, 7.3, 7.5, 6.4, 4.6, 2.6, 1.3],
    "international": [2.1, 1.8, 1.5, 1.3, 1.4, 1.9, 2.6, 3.4, 4.1, 4.8, 5.3,
                      5.6, 5.5, 5.2, 5.0, 5.1, 5.4, 5.8, 6.1, 6.0, 5.3, 4.3,
                      3.4, 2.6],
    "feature_phone": [0.4, 0.3, 0.2, 0.2, 0.3, 1.1, 3.0, 4.9, 6.3, 7.1, 7.4,
                      7.0, 6.2, 5.8, 5.6, 5.7, 6.0, 6.4, 6.6, 5.6, 4.1, 2.6,
                      1.5, 0.8],
}


def _hour_profile(code: str) -> np.ndarray:
    if code in ("UPI_AUTOPAY", "UPI_RECURRING", "UPI_LITE_ATU"):
        key = "mandate"
    elif code in ("UPI_CREDIT_LINE", "RUPAY_CREDIT"):
        key = "credit"
    elif code == "UPI_INTL":
        key = "international"
    elif code == "UPI_123PAY":
        key = "feature_phone"
    else:
        key = "consumer"
    p = np.array(_HOUR_PROFILES[key], dtype=float)
    return p / p.sum()


def adoption(lifecycle: str, target: float, t: float) -> float:
    """Multiple of the day-0 volume at normalised time t in [0, 1]."""
    t = min(1.0, max(0.0, t))
    if lifecycle == "mature":
        # Slightly concave: growth decelerates as the base gets large.
        return 1.0 + (target - 1.0) * (t ** 0.86)
    if lifecycle == "growth":
        # Logistic with the inflection near the middle of the window.
        s = 1.0 / (1.0 + math.exp(-7.5 * (t - 0.48)))
        s0 = 1.0 / (1.0 + math.exp(-7.5 * (-0.48)))
        s1 = 1.0 / (1.0 + math.exp(-7.5 * (0.52)))
        return 1.0 + (target - 1.0) * (s - s0) / (s1 - s0)
    if lifecycle == "hyper":
        # Late, steep take-off off a small base.
        s = 1.0 / (1.0 + math.exp(-9.5 * (t - 0.60)))
        s0 = 1.0 / (1.0 + math.exp(-9.5 * (-0.60)))
        s1 = 1.0 / (1.0 + math.exp(-9.5 * (0.40)))
        return 1.0 + (target - 1.0) * (s - s0) / (s1 - s0)
    if lifecycle == "declining":
        return 1.0 + (target - 1.0) * (t ** 0.7)
    return 1.0


def _pick(rng: np.random.Generator, cum: np.ndarray, n: int) -> np.ndarray:
    """Vectorised weighted sampling from a cumulative-probability vector."""
    return np.searchsorted(cum, rng.random(n), side="right").clip(
        0, len(cum) - 1)


def _cum(weights: np.ndarray) -> np.ndarray:
    w = np.asarray(weights, dtype=float)
    w = np.where(w < 0, 0.0, w)
    total = w.sum()
    if total <= 0:
        w = np.ones_like(w)
        total = w.sum()
    return np.cumsum(w / total)


class TransactionSimulator:
    """Generates the raw transaction stream day by day."""

    def __init__(self, *, rng: np.random.Generator, pop, book,
                 calendar: list[DayContext], events: list[Event],
                 start_date: date, base_daily: int = 11_000):
        self.rng = rng
        self.pop = pop
        self.book = book
        self.calendar = calendar
        self.events = events
        self.start_date = start_date
        self.days = len(calendar)
        self.base_daily = base_daily

        self._bank_names = np.array([b["name"] for b in BANKS], dtype=object)
        self._bank_success = np.array([b["base_success"] for b in BANKS])
        self._bank_p95 = np.array([b["p95"] for b in BANKS], dtype=float)
        self._bank_cum = _cum(np.array([b["share"] for b in BANKS]))
        self._psp_names = np.array([p["name"] for p in PSPS], dtype=object)
        self._psp_p95 = np.array([p["p95"] for p in PSPS], dtype=float)
        self._psp_cum = _cum(np.array([p["share"] for p in PSPS]))
        self._city_name = np.array([c[0] for c in CITIES], dtype=object)
        self._city_state = np.array([c[1] for c in CITIES], dtype=object)
        self._city_region = np.array([c[2] for c in CITIES], dtype=object)
        self._city_tier = np.array([c[4] for c in CITIES], dtype=np.int8)
        self._dev_names = np.array([d[0] for d in DEVICES], dtype=object)
        self._dev_cum = _cum(np.array([d[1] for d in DEVICES]))
        self._chan_names = np.array([c[0] for c in CHANNELS], dtype=object)
        self._chan_cum = _cum(np.array([c[1] for c in CHANNELS]))
        self._seg_codes = np.array([s["code"] for s in SEGMENTS], dtype=object)
        self._mcc_code = np.array([m.code for m in MCCS], dtype=object)
        self._mcc_cat = np.array([m.category for m in MCCS], dtype=object)
        self._mcc_sub = np.array([m.subcategory for m in MCCS], dtype=object)
        self._mcc_ticket = np.array([m.ticket_mult for m in MCCS])
        self._mcc_share = np.array([m.share for m in MCCS])
        self._mcc_risk = np.array([m.risk for m in MCCS])
        self._mcc_succ = np.array([m.success_delta for m in MCCS])
        self._mcc_season = [m.seasonality for m in MCCS]
        self._hour_cum = {p.code: np.cumsum(_hour_profile(p.code))
                          for p in PRODUCTS}
        # A product's declared median ticket must survive the MCC and segment
        # multipliers layered on top of it, so divide those out up front.
        self._ticket_norm: dict[str, float] = {}
        for p in PRODUCTS:
            aff = PRODUCT_MCC_AFFINITY.get(p.code, {})
            if p.merchant_facing and aff:
                w = self._mcc_share * np.array(
                    [aff.get(c, 0.0) for c in self._mcc_code])
                w = w / w.sum() if w.sum() > 0 else w
                # Geometric, not arithmetic: a few very-high-ticket MCCs
                # (airlines, education) would otherwise drag the whole
                # product's median down once divided out.
                self._ticket_norm[p.code] = float(
                    np.exp((w * np.log(self._mcc_ticket)).sum()))
            else:
                self._ticket_norm[p.code] = 1.0
        self._cust_ticket_norm = float(np.mean(pop.cust_ticket_mult))

        # Per-bank / per-PSP AR(1) reliability wobble across the window: real
        # issuers drift in and out of health independently of any incident.
        self._bank_drift = self._ar1(len(BANKS), 0.86, 0.34)
        self._psp_drift = self._ar1(len(PSPS), 0.82, 0.26)
        self._prod_noise = {p.code: self._ar1(1, 0.58, 0.052)[0]
                            for p in PRODUCTS}
        # Rare demand shocks: 4% of product-days get a one-off jump.
        self._shocks = {
            p.code: np.where(rng.random(self.days) < 0.04,
                             rng.normal(0.0, 0.16, self.days), 0.0)
            for p in PRODUCTS}

        self._txn_seq = 0
        self._scheduled: dict[int, list[dict]] = {}
        self._retry_carry: dict[int, list[tuple]] = {}
        self._mandate_retry: dict[int, list[tuple[int, int]]] = {}

    def _ar1(self, n: int, rho: float, sigma: float) -> np.ndarray:
        """n independent AR(1) paths of length self.days."""
        out = np.zeros((n, self.days))
        e = self.rng.normal(0.0, sigma, (n, self.days))
        for t in range(1, self.days):
            out[:, t] = rho * out[:, t - 1] + e[:, t]
        return out

    # ------------------------------------------------------------- volumes
    def daily_volume(self, product, d: int) -> int:
        cal = self.calendar[d]
        t = d / max(1, self.days - 1)
        base = self.base_daily * product.share * adoption(
            product.lifecycle, product.adoption_target, t)

        if product.settlement_sensitive:
            cal_mult = (cal.spend_mult ** 0.35) * (cal.settlement_mult ** 0.65)
        else:
            cal_mult = cal.spend_mult
        if cal.is_weekend:
            cal_mult *= product.weekend_bias
        else:
            cal_mult *= 1.0 + (1.0 - product.weekend_bias) * 0.32

        ev_vol = 1.0
        for ev in self.events:
            w = ev.intensity(d)
            if w > 0 and ev.matches(product=product.code) and not (
                    ev.scope.get("bank") or ev.scope.get("psp")
                    or ev.scope.get("mcc") or ev.scope.get("region")):
                ev_vol *= 1.0 + ev.volume_impact * w

        noise = math.exp(self._prod_noise[product.code][d]
                         + self._shocks[product.code][d])
        n = base * cal_mult * ev_vol * noise
        # Poisson arrival on top of the deterministic intensity.
        return int(max(0, self.rng.poisson(max(1.0, n))))

    # --------------------------------------------------------------- a day
    def simulate_day(self, d: int) -> list[dict]:
        cal = self.calendar[d]
        rows: list[dict] = []

        cust_w = self.pop.active_weights(d)
        cust_cum = _cum(cust_w)
        merch_w = self.pop.merchant_day_weights(d)

        for product in PRODUCTS:
            if product.code in ("UPI_AUTOPAY", "UPI_RECURRING",
                                "UPI_LITE_ATU"):
                rows.extend(self._simulate_mandates(d, product, cal))
                continue
            n = self.daily_volume(product, d)
            if n:
                rows.extend(self._simulate_product(d, product, cal, n,
                                                   cust_cum, merch_w))

        # Rows scheduled by earlier days: refunds, chargebacks, reversals and
        # next-day retries all land here.
        rows.extend(self._scheduled.pop(d, []))
        rows.extend(self._replay_retries(d, cal))
        return rows

    # ------------------------------------------------------ ordinary product
    def _simulate_product(self, d: int, product, cal: DayContext, n: int,
                          cust_cum: np.ndarray, merch_w: np.ndarray,
                          *, attempt: int = 0,
                          parents: list[dict] | None = None) -> list[dict]:
        rng = self.rng
        t = d / max(1, self.days - 1)

        hours = _pick(rng, self._hour_cum[product.code], n).astype(np.int16)
        minutes = rng.integers(0, 60, n).astype(np.int16)
        seconds = rng.integers(0, 60, n).astype(np.int16)

        cust = _pick(rng, cust_cum, n)
        seg = self.pop.cust_segment[cust]
        city = self.pop.cust_city[cust]
        payer_bank = self.pop.cust_bank[cust]
        payer_psp = self.pop.cust_psp[cust]
        # 22% of payments are made from a secondary app, not the customer's
        # habitual one — that mobility is what makes PSP share move.
        switch = rng.random(n) < 0.22
        payer_psp = np.where(switch, _pick(rng, self._psp_cum, n), payer_psp)

        # Regional holiday suppression: drop a share of the affected states.
        if cal.suppressed_states:
            aff = np.isin(self._city_state[city],
                          np.array(cal.suppressed_states, dtype=object))
            keep = ~aff | (rng.random(n) < 0.58)
            if not keep.all():
                idx = np.flatnonzero(keep)
                n = len(idx)
                if n == 0:
                    return []
                hours, minutes, seconds = hours[idx], minutes[idx], seconds[idx]
                cust, seg, city = cust[idx], seg[idx], city[idx]
                payer_bank, payer_psp = payer_bank[idx], payer_psp[idx]

        region = self._city_region[city]

        # ---- merchant leg -------------------------------------------------
        affinity = PRODUCT_MCC_AFFINITY.get(product.code, {})
        if product.merchant_facing and affinity:
            w = self._mcc_share * np.array(
                [affinity.get(c, 0.0) for c in self._mcc_code])
            w = w * self._season_boost(cal)
            w = w * self._mcc_event_boost(d, product.code)
            mcc_ix = _pick(rng, _cum(w), n)
            merchant = self._pick_merchants(mcc_ix, merch_w, n)
            payee_psp = self.pop.merch_psp[merchant]
            payee_bank = self.pop.merch_bank[merchant]
            merch_city = self.pop.merch_city[merchant]
            # A physical-acceptance payment happens where the merchant is.
            at_merchant = rng.random(n) < 0.62
            city = np.where(at_merchant, merch_city, city)
            region = self._city_region[city]
        else:
            mcc_ix = np.full(n, -1)
            merchant = np.full(n, -1)
            payee_psp = _pick(rng, self._psp_cum, n)
            payee_bank = _pick(rng, self._bank_cum, n)

        # ---- amount -------------------------------------------------------
        ticket = self._amounts(product, n, mcc_ix, cust, cal)

        # ---- outcome ------------------------------------------------------
        status, fail_ix, bucket_ix, fraud = self._outcome(
            d, product, n, t, payer_bank, payer_psp, mcc_ix, ticket, cal,
            region, attempt)

        latency, switch_ms, issuer_ms = self._latency(
            d, product, n, payer_bank, payer_psp, hours, status, region)

        return self._materialise(
            d, product, cal, n, hours, minutes, seconds, cust, seg, city,
            region, payer_bank, payee_bank, payer_psp, payee_psp, merchant,
            mcc_ix, ticket, status, fail_ix, bucket_ix, fraud, latency,
            switch_ms, issuer_ms, attempt=attempt, parents=parents)

    # ------------------------------------------------------------- helpers
    def _season_boost(self, cal: DayContext) -> np.ndarray:
        """Per-MCC calendar boost: festival category lift + cadence."""
        boost = np.ones(len(MCCS))
        for i, m in enumerate(MCCS):
            b = cal.category_boost.get(m.subcategory) or \
                cal.category_boost.get(m.category)
            if b:
                boost[i] *= b
            if m.seasonality == "monthly":
                # Bills, SIPs and EMIs cluster in the first and last week.
                dom = cal.day.day
                boost[i] *= 1.75 if dom <= 7 else (1.35 if dom >= 26 else 0.72)
            elif m.seasonality == "travel":
                boost[i] *= 1.45 if cal.day.month in (4, 5, 10, 12) else 0.88
                if cal.is_weekend:
                    boost[i] *= 1.28
            elif m.seasonality == "festive" and cal.festival:
                boost[i] *= 1.22
            elif m.seasonality == "daily" and cal.is_weekend:
                boost[i] *= 1.12
        return boost

    def _mcc_event_boost(self, d: int, product_code: str) -> np.ndarray:
        boost = np.ones(len(MCCS))
        for ev in self.events:
            w = ev.intensity(d)
            mcc = ev.scope.get("mcc")
            if w <= 0 or not mcc:
                continue
            if not ev.matches(product=product_code, mcc=mcc):
                continue
            i = next((k for k, m in enumerate(MCCS) if m.code == mcc), None)
            if i is not None:
                boost[i] *= 1.0 + ev.volume_impact * w
        return boost

    def _pick_merchants(self, mcc_ix: np.ndarray, merch_w: np.ndarray,
                        n: int) -> np.ndarray:
        out = np.full(n, -1, dtype=np.int64)
        for mi in np.unique(mcc_ix):
            if mi < 0:
                continue
            sel = np.flatnonzero(mcc_ix == mi)
            pool = self.pop.merch_by_mcc[int(mi)]
            w = merch_w[pool]
            if w.sum() <= 0:
                w = np.ones(len(pool))
            out[sel] = pool[_pick(self.rng, _cum(w), len(sel))]
        return out

    def _amounts(self, product, n: int, mcc_ix: np.ndarray,
                 cust: np.ndarray, cal: DayContext) -> np.ndarray:
        rng = self.rng
        median = product.ticket_median
        mult = np.ones(n)
        live = mcc_ix >= 0
        if live.any():
            mult[live] = self._mcc_ticket[mcc_ix[live]]
        mult *= self.pop.cust_ticket_mult[cust] / self._cust_ticket_norm
        mult /= self._ticket_norm.get(product.code, 1.0)
        # Salary-window spending skews larger; the pre-salary trough skews small.
        mult *= (0.90 + 0.22 * min(1.35, cal.spend_mult)) / 1.13
        amt = median * mult * rng.lognormal(0.0, product.ticket_sigma, n)
        # UPI amounts cluster on round numbers — people pay ₹100, not ₹98.37.
        round_mask = rng.random(n) < 0.34
        amt = np.where(round_mask & (amt > 80),
                       np.round(amt / 10.0) * 10.0, np.round(amt, 0))
        amt = np.maximum(amt, 1.0)
        if product.ticket_cap:
            amt = np.minimum(amt, product.ticket_cap)
        return amt

    def _outcome(self, d: int, product, n: int, t: float,
                 payer_bank: np.ndarray, payer_psp: np.ndarray,
                 mcc_ix: np.ndarray, amount: np.ndarray, cal: DayContext,
                 region: np.ndarray, attempt: int):
        rng = self.rng
        p = np.full(n, product.base_success + product.success_drift * t)
        p += (self._bank_success[payer_bank] - 98.42) * 0.75
        p += self._bank_drift[payer_bank, d]
        p += self._psp_drift[payer_psp, d]
        live = mcc_ix >= 0
        if live.any():
            p[live] += self._mcc_succ[mcc_ix[live]]
        # Large tickets fail more (limits, balances, risk rules).
        p -= np.clip(np.log10(np.maximum(amount, 1.0)) - 2.6, 0, None) * 0.92
        # A retry of a previously failed payment succeeds less often.
        p -= attempt * 6.5

        fraud = np.zeros(n)
        bank_names = self._bank_names[payer_bank]
        psp_names = self._psp_names[payer_psp]
        tech_boost = np.ones(n)
        time_boost = np.ones(n)
        for ev in self.events:
            w = ev.intensity(d)
            if w <= 0:
                continue
            if not ev.matches(product=product.code):
                continue
            m = np.ones(n, dtype=bool)
            if ev.scope.get("bank"):
                m &= bank_names == ev.scope["bank"]
            if ev.scope.get("psp"):
                m &= psp_names == ev.scope["psp"]
            if ev.scope.get("region"):
                m &= region == ev.scope["region"]
            if ev.scope.get("mcc"):
                code = ev.scope["mcc"]
                m &= live & (self._mcc_code[np.where(live, mcc_ix, 0)] == code)
            if not m.any():
                continue
            p[m] += ev.success_impact * w
            fraud[m] += ev.fraud_impact * w
            if ev.kind in ("bank_outage", "psp_degradation"):
                tech_boost[m] *= 1.0 + 5.0 * w
            if ev.kind == "network_latency":
                time_boost[m] *= 1.0 + 4.0 * w

        p = np.clip(p + 0.34, 55.0, 99.94)
        u = rng.random(n)
        ok = u < (p / 100.0)
        # A thin slice never resolves within the day — genuinely pending.
        pending = (~ok) & (rng.random(n) < 0.028)

        fm = product.failure_mix
        w_tech = fm[0] * tech_boost
        w_biz = np.full(n, fm[1]) * (1.0 + 0.55 * max(
            0.0, 1.12 - cal.spend_mult))
        w_risk = fm[2] * (1.0 + fraud)
        w_time = fm[3] * time_boost
        stack = np.vstack([w_tech, w_biz, w_risk, w_time])
        stack /= stack.sum(axis=0, keepdims=True)
        cums = np.cumsum(stack, axis=0)
        r = rng.random(n)
        bucket_ix = (r[None, :] > cums).sum(axis=0).clip(0, 3)

        fail_ix = np.full(n, -1, dtype=np.int64)
        for bi, bucket in enumerate(_BUCKETS):
            sel = np.flatnonzero((~ok) & ~pending & (bucket_ix == bi))
            if len(sel) == 0:
                continue
            codes = FAILURE_BY_BUCKET[bucket]
            cum = _cum(np.array([c.weight for c in codes]))
            local = _pick(rng, cum, len(sel))
            fail_ix[sel] = [self._failure_global_ix(bucket, int(j))
                            for j in local]

        status = np.where(ok, "SUCCESS", np.where(pending, "PENDING", "FAILED"))
        return status, fail_ix, bucket_ix, fraud

    @staticmethod
    def _failure_global_ix(bucket: str, local: int) -> int:
        from app.warehouse.generator.catalog import FAILURE_CODES
        code = FAILURE_BY_BUCKET[bucket][local]
        return FAILURE_CODES.index(code)

    def _latency(self, d: int, product, n: int, payer_bank: np.ndarray,
                 payer_psp: np.ndarray, hours: np.ndarray,
                 status: np.ndarray, region: np.ndarray):
        rng = self.rng
        base = product.latency_p50
        sigma = math.log(max(1.2, product.latency_p95 / max(1, base))) / 1.645
        lat = base * rng.lognormal(0.0, sigma, n)
        lat *= (self._bank_p95[payer_bank] / 1000.0) ** 0.42
        lat *= (self._psp_p95[payer_psp] / 800.0) ** 0.34
        # Peak-hour congestion.
        peak = np.isin(hours, [10, 11, 12, 18, 19, 20])
        lat *= np.where(peak, 1.24, 1.0)

        bank_names = self._bank_names[payer_bank]
        psp_names = self._psp_names[payer_psp]
        for ev in self.events:
            w = ev.intensity(d)
            if w <= 0 or ev.latency_impact == 1.0:
                continue
            if not ev.matches(product=product.code):
                continue
            m = np.ones(n, dtype=bool)
            if ev.scope.get("bank"):
                m &= bank_names == ev.scope["bank"]
            if ev.scope.get("psp"):
                m &= psp_names == ev.scope["psp"]
            if ev.scope.get("region"):
                m &= region == ev.scope["region"]
            lat[m] *= 1.0 + (ev.latency_impact - 1.0) * w

        # Timeouts are slow by definition; declines resolve fast.
        lat = np.where(status == "FAILED", lat * rng.uniform(0.5, 1.1, n), lat)
        lat = np.maximum(lat, 40.0)
        switch_ms = lat * rng.uniform(0.16, 0.34, n)
        issuer_ms = lat - switch_ms
        return lat.astype(np.int32), switch_ms.astype(np.int32), \
            issuer_ms.astype(np.int32)

    # --------------------------------------------------------- row assembly
    def _materialise(self, d, product, cal, n, hours, minutes, seconds, cust,
                     seg, city, region, payer_bank, payee_bank, payer_psp,
                     payee_psp, merchant, mcc_ix, amount, status, fail_ix,
                     bucket_ix, fraud, latency, switch_ms, issuer_ms, *,
                     attempt=0, parents=None, mandate_ids=None,
                     txn_type="PAYMENT"):
        from app.warehouse.generator.catalog import FAILURE_CODES
        rng = self.rng
        day = cal.day
        base_seq = self._txn_seq
        self._txn_seq += n
        txn_ids = [f"T{day:%y%m%d}{base_seq + i:07d}" for i in range(n)]

        has_merch = merchant >= 0
        m_id = np.where(has_merch, self.pop.merch_id[np.maximum(merchant, 0)],
                        None)
        m_name = np.where(has_merch,
                          self.pop.merch_name[np.maximum(merchant, 0)], None)
        m_tier = np.where(has_merch,
                          self.pop.merch_tier[np.maximum(merchant, 0)], -1)
        live_mcc = mcc_ix >= 0
        mcc = np.where(live_mcc, self._mcc_code[np.maximum(mcc_ix, 0)], None)
        mcc_cat = np.where(live_mcc, self._mcc_cat[np.maximum(mcc_ix, 0)], None)
        mcc_sub = np.where(live_mcc, self._mcc_sub[np.maximum(mcc_ix, 0)], None)

        has_fail = fail_ix >= 0
        f_code = np.where(has_fail, [FAILURE_CODES[max(0, int(i))].code
                                     for i in fail_ix], None)
        f_reason = np.where(has_fail, [FAILURE_CODES[max(0, int(i))].reason
                                       for i in fail_ix], None)
        f_bucket = np.where(has_fail, [_BUCKETS[int(b)] for b in bucket_ix],
                            None)
        f_owner = np.where(has_fail, [FAILURE_CODES[max(0, int(i))].owner
                                      for i in fail_ix], None)
        retryable = np.where(has_fail, [FAILURE_CODES[max(0, int(i))].retryable
                                        for i in fail_ix], False)

        ptypes = np.array(product.payment_types, dtype=object)
        ptype = ptypes[rng.integers(0, len(ptypes), n)]
        devices = _pick(rng, self._dev_cum, n)
        channels = _pick(rng, self._chan_cum, n)
        if product.code == "UPI_123PAY":
            devices = np.full(n, 2)
            channels = np.full(n, 4)
        elif product.code == "UPI_QR":
            channels = np.where(rng.random(n) < 0.82, 1, channels)

        rows = []
        tier_name = {-1: None, 0: "Long Tail", 1: "Mid Market", 2: "Large",
                     3: "Key Account"}
        parent_ids = parents or [None] * n
        m_ids = mandate_ids if mandate_ids is not None else [None] * n
        for i in range(n):
            rows.append({
                "txn_id": txn_ids[i],
                "txn_ts": f"{day}T{int(hours[i]):02d}:{int(minutes[i]):02d}:"
                          f"{int(seconds[i]):02d}",
                "txn_date": str(day),
                "day_index": d,
                "hour": int(hours[i]),
                "day_of_week": day.weekday(),
                "week_of_year": day.isocalendar()[1],
                "month": day.month,
                "quarter": (day.month - 1) // 3 + 1,
                "is_weekend": cal.is_weekend,
                "is_holiday": bool(cal.holiday),
                "calendar_event": cal.festival or cal.holiday,
                "txn_type": txn_type,
                "product_code": product.code,
                "product_name": product.name,
                "product_family": product.family,
                "payment_type": ptype[i],
                "amount_inr": float(amount[i]),
                "status": status[i],
                "failure_code": f_code[i],
                "failure_reason": f_reason[i],
                "failure_bucket": f_bucket[i],
                "failure_owner": f_owner[i],
                "retryable": bool(retryable[i]) if has_fail[i] else None,
                "attempt_no": attempt,
                "is_retry": attempt > 0,
                "parent_txn_id": parent_ids[i],
                "payer_bank": self._bank_names[payer_bank[i]],
                "payee_bank": self._bank_names[payee_bank[i]],
                "payer_psp": self._psp_names[payer_psp[i]],
                "payee_psp": self._psp_names[payee_psp[i]],
                "merchant_id": m_id[i],
                "merchant_name": m_name[i],
                "merchant_tier": tier_name[int(m_tier[i])],
                "mcc": mcc[i],
                "mcc_category": mcc_cat[i],
                "mcc_subcategory": mcc_sub[i],
                "customer_id": f"CUST-{500000 + int(cust[i])}",
                "customer_segment": self._seg_codes[seg[i]],
                "device": self._dev_names[devices[i]],
                "channel": self._chan_names[channels[i]],
                "city": self._city_name[city[i]],
                "state": self._city_state[city[i]],
                "region": self._city_region[city[i]],
                "city_tier": int(self._city_tier[city[i]]),
                "latency_ms": int(latency[i]),
                "switch_ms": int(switch_ms[i]),
                "issuer_ms": int(issuer_ms[i]),
                "mandate_id": m_ids[i],
                "risk_score": round(float(min(100.0, fraud[i] * 8
                                              + (self._mcc_risk[mcc_ix[i]]
                                                 * 40 if live_mcc[i] else 5))), 2),
            })

        self._schedule_followups(d, rows, product, retryable, has_fail)
        return rows

    # ---------------------------------------------- retries / refunds / etc.
    def _schedule_followups(self, d: int, rows: list[dict], product,
                            retryable: np.ndarray, has_fail: np.ndarray
                            ) -> None:
        rng = self.rng
        for i, r in enumerate(rows):
            if r["attempt_no"] >= 2:
                continue
            if r["status"] == "FAILED" and has_fail[i] and retryable[i]:
                if rng.random() < 0.63:
                    when = d if rng.random() < 0.74 else d + 1
                    if when < self.days:
                        self._retry_carry.setdefault(when, []).append(
                            (product.code, r))
            # A timeout means the debit landed but the credit did not confirm,
            # so the money is auto-reversed — independently of any retry.
            if r["status"] == "FAILED" and r["failure_bucket"] == "timeout" \
                    and rng.random() < 0.58:
                when = d + int(rng.integers(0, 3))
                if when < self.days:
                    self._scheduled.setdefault(when, []).append(
                        self._derived_row(r, "REVERSAL", when))
            if r["status"] == "SUCCESS" and r["merchant_id"]:
                risk = (r["risk_score"] or 0) / 100.0
                if rng.random() < 0.009 + 0.055 * risk:
                    when = d + int(rng.integers(1, 15))
                    if when < self.days:
                        self._scheduled.setdefault(when, []).append(
                            self._derived_row(r, "REFUND", when))
                elif rng.random() < 0.0004 + 0.0032 * risk:
                    when = d + int(rng.integers(5, 46))
                    if when < self.days:
                        self._scheduled.setdefault(when, []).append(
                            self._derived_row(r, "CHARGEBACK", when))

    def _derived_row(self, parent: dict, kind: str, day: int) -> dict:
        cal = self.calendar[day]
        self._txn_seq += 1
        rng = self.rng
        row = dict(parent)
        row["txn_id"] = f"{kind[0]}{cal.day:%y%m%d}{self._txn_seq:07d}"
        row["txn_ts"] = (f"{cal.day}T{int(rng.integers(0, 24)):02d}:"
                         f"{int(rng.integers(0, 60)):02d}:00")
        row["txn_date"] = str(cal.day)
        row["day_index"] = day
        row["hour"] = int(row["txn_ts"][11:13])
        row["day_of_week"] = cal.day.weekday()
        row["week_of_year"] = cal.day.isocalendar()[1]
        row["month"] = cal.day.month
        row["quarter"] = (cal.day.month - 1) // 3 + 1
        row["is_weekend"] = cal.is_weekend
        row["is_holiday"] = bool(cal.holiday)
        row["calendar_event"] = cal.festival or cal.holiday
        row["txn_type"] = kind
        row["parent_txn_id"] = parent["txn_id"]
        row["status"] = "SUCCESS" if kind != "CHARGEBACK" else "DISPUTED"
        row["failure_code"] = row["failure_reason"] = None
        row["failure_bucket"] = row["failure_owner"] = None
        row["retryable"] = None
        row["attempt_no"] = 0
        row["is_retry"] = False
        if kind == "REFUND":
            # Partial refunds are common on multi-item baskets.
            frac = 1.0 if rng.random() < 0.72 else float(
                rng.uniform(0.25, 0.85))
            row["amount_inr"] = round(parent["amount_inr"] * frac, 2)
        row["amount_inr"] = -abs(row["amount_inr"])
        row["latency_ms"] = int(rng.integers(300, 4200))
        row["switch_ms"] = int(row["latency_ms"] * 0.25)
        row["issuer_ms"] = row["latency_ms"] - row["switch_ms"]
        return row

    def _replay_retries(self, d: int, cal: DayContext) -> list[dict]:
        """Re-present the failed, retryable payments carried into today."""
        carried = self._retry_carry.pop(d, [])
        if not carried:
            return []
        rng = self.rng
        out: list[dict] = []
        by_product: dict[str, list[dict]] = {}
        for code, parent in carried:
            by_product.setdefault(code, []).append(parent)
        for code, parents in by_product.items():
            product = next(p for p in PRODUCTS if p.code == code)
            for parent in parents:
                self._txn_seq += 1
                attempt = parent["attempt_no"] + 1
                # A retry keeps every dimension of the original attempt; only
                # the outcome and the clock move.
                p_succ = min(96.0, product.base_success - 6.5 * attempt + 4.0)
                ok = rng.random() < p_succ / 100.0
                row = dict(parent)
                row["txn_id"] = f"R{cal.day:%y%m%d}{self._txn_seq:07d}"
                row["txn_date"] = str(cal.day)
                row["day_index"] = d
                hh = int(rng.integers(0, 24))
                row["txn_ts"] = f"{cal.day}T{hh:02d}:{int(rng.integers(0,60)):02d}:00"
                row["hour"] = hh
                row["day_of_week"] = cal.day.weekday()
                row["week_of_year"] = cal.day.isocalendar()[1]
                row["month"] = cal.day.month
                row["quarter"] = (cal.day.month - 1) // 3 + 1
                row["is_weekend"] = cal.is_weekend
                row["is_holiday"] = bool(cal.holiday)
                row["calendar_event"] = cal.festival or cal.holiday
                row["txn_type"] = "RETRY"
                row["attempt_no"] = attempt
                row["is_retry"] = True
                row["parent_txn_id"] = parent["txn_id"]
                row["status"] = "SUCCESS" if ok else "FAILED"
                if ok:
                    row["failure_code"] = row["failure_reason"] = None
                    row["failure_bucket"] = row["failure_owner"] = None
                    row["retryable"] = None
                row["latency_ms"] = int(parent["latency_ms"] *
                                        rng.uniform(0.7, 1.4))
                row["switch_ms"] = int(row["latency_ms"] * 0.25)
                row["issuer_ms"] = row["latency_ms"] - row["switch_ms"]
                out.append(row)
                if not ok and attempt < 2 and rng.random() < 0.4 \
                        and d + 1 < self.days:
                    self._retry_carry.setdefault(d + 1, []).append(
                        (code, row))
        return out

    # ------------------------------------------------------------- mandates
    def _simulate_mandates(self, d: int, product, cal: DayContext
                           ) -> list[dict]:
        book = self.book
        due = [i for i in book.due.get(d, [])
               if str(book.product[i]) == product.code]
        pending = self._mandate_retry.get(d, [])
        retries = [i for (i, _a) in pending
                   if str(book.product[i]) == product.code]
        if not due and not retries:
            return []
        rows: list[dict] = []
        for attempt, indices in ((0, due), (1, retries)):
            if indices:
                rows.extend(self._execute_mandates(d, product, cal, indices,
                                                   attempt))
        if retries:
            self._mandate_retry[d] = [
                x for x in pending if str(book.product[x[0]]) != product.code]
        return rows

    def _execute_mandates(self, d: int, product, cal: DayContext,
                          indices: list[int], attempt: int) -> list[dict]:
        book, rng, pop = self.book, self.rng, self.pop
        n = len(indices)
        ix = np.array(indices, dtype=np.int64)
        t = d / max(1, self.days - 1)

        cust = book.customer[ix]
        merchant = book.merchant[ix]
        mcc_codes = book.mcc[ix]
        mcc_ix = np.array([next(k for k, m in enumerate(MCCS)
                                if m.code == c) for c in mcc_codes])
        amount = np.where(book.modified_day[ix] <= d,
                          book.modified_amount[ix], book.amount[ix]).astype(float)
        # Variable-amount mandates (utilities, as-presented) vary each cycle.
        variable = np.isin(book.purpose[ix],
                           np.array(["Electricity Bill", "Mobile / DTH Recharge",
                                     "Cloud / SaaS"], dtype=object))
        amount = np.where(variable,
                          np.round(amount * rng.uniform(0.62, 1.55, n), 0),
                          amount)

        hours = book.exec_hour[ix].astype(np.int16)
        minutes = rng.integers(0, 60, n).astype(np.int16)
        seconds = rng.integers(0, 60, n).astype(np.int16)
        seg = pop.cust_segment[cust]
        city = pop.cust_city[cust]
        region = self._city_region[city]
        payer_bank = pop.cust_bank[cust]
        payer_psp = pop.cust_psp[cust]
        payee_psp = pop.merch_psp[merchant]
        payee_bank = pop.merch_bank[merchant]

        status, fail_ix, bucket_ix, fraud = self._outcome(
            d, product, n, t, payer_bank, payer_psp, mcc_ix, amount, cal,
            region, attempt)
        # Mandates fail overwhelmingly on balance, not on technology — and the
        # pre-salary trough is exactly when balances run out.
        if cal.day.day in (24, 25, 26, 27, 28):
            flip = (status == "SUCCESS") & (rng.random(n) < 0.045)
            status = np.where(flip, "FAILED", status)
            from app.warehouse.generator.catalog import FAILURE_CODES
            z9 = next(i for i, c in enumerate(FAILURE_CODES) if c.code == "Z9")
            fail_ix = np.where(flip, z9, fail_ix)
            bucket_ix = np.where(flip, 1, bucket_ix)

        latency, switch_ms, issuer_ms = self._latency(
            d, product, n, payer_bank, payer_psp, hours, status, region)

        mandate_ids = [book.mandate_id[i] for i in indices]
        rows = self._materialise(
            d, product, cal, n, hours, minutes, seconds, cust, seg, city,
            region, payer_bank, payee_bank, payer_psp, payee_psp, merchant,
            mcc_ix, amount, status, fail_ix, bucket_ix, fraud, latency,
            switch_ms, issuer_ms, attempt=attempt, mandate_ids=mandate_ids,
            txn_type="MANDATE_RETRY" if attempt else "MANDATE_EXECUTION")

        for k, i in enumerate(indices):
            r = rows[k]
            book.emit_execution(d, i, r["txn_id"], float(r["amount_inr"]),
                                r["status"], r["failure_code"], attempt)
            if r["status"] == "FAILED" and attempt == 0 and d + 1 < self.days \
                    and rng.random() < 0.68:
                self._mandate_retry.setdefault(d + 1, []).append((i, 1))
        return rows

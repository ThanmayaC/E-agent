"""AutoPay / e-mandate book and its lifecycle event stream.

Mandate products are not sampled like ordinary transactions — they are *driven*
by a book of registered mandates. A mandate is created once, executes on a
schedule, is occasionally modified, paused, resumed, revoked or cancelled, and
eventually expires. Each execution attempt becomes a real transaction, and each
lifecycle event references the transaction it produced.

Building it this way means AutoPay volume, failure rate and retry behaviour all
fall out of the book's composition rather than being asserted — which is what
makes mandate-level analytics (active book, churn, execution success by
purpose, retry recovery) answerable from the raw data.
"""
from __future__ import annotations

from datetime import date, timedelta

import numpy as np

from app.warehouse.generator.catalog import (
    MANDATE_FREQUENCIES, MANDATE_PURPOSES, MCC_BY_CODE, MCCS,
)

_FREQ_DAYS = {f[0]: f[2] for f in MANDATE_FREQUENCIES}
# 'AS_PRESENTED' has no fixed cadence — merchants present when they choose.
_AS_PRESENTED_MEAN = 22


class MandateBook:
    """The registered mandate universe plus its execution schedule."""

    def __init__(self, rng: np.random.Generator, pop, days: int,
                 start_date: date, n_mandates: int = 14_000):
        self.rng = rng
        self.pop = pop
        self.days = days
        self.start_date = start_date
        self.n = n_mandates
        self.events: list[dict] = []
        self._build()

    # ------------------------------------------------------------- building
    def _build(self) -> None:
        rng, n = self.rng, self.n

        freq_names = [f[0] for f in MANDATE_FREQUENCIES]
        freq_p = np.array([f[1] for f in MANDATE_FREQUENCIES])
        freq_p /= freq_p.sum()
        self.freq = rng.choice(len(freq_names), size=n, p=freq_p)
        self.freq_name = np.array(freq_names, dtype=object)[self.freq]

        purpose_p = np.array([p[2] for p in MANDATE_PURPOSES])
        purpose_p /= purpose_p.sum()
        self.purpose_ix = rng.choice(len(MANDATE_PURPOSES), size=n, p=purpose_p)
        # A Lite auto top-up is not a monthly subscription — it fires whenever
        # the on-device balance runs down, which for an active user is weekly.
        atu = self.purpose_ix == next(
            i for i, p in enumerate(MANDATE_PURPOSES)
            if p[0] == "Lite Auto Top-Up")
        self.freq_name = np.where(atu, "WEEKLY", self.freq_name)
        self.purpose = np.array([p[0] for p in MANDATE_PURPOSES],
                                dtype=object)[self.purpose_ix]
        self.mcc = np.array([p[1] for p in MANDATE_PURPOSES],
                            dtype=object)[self.purpose_ix]
        base_amt = np.array([p[3] for p in MANDATE_PURPOSES])[self.purpose_ix]
        self.amount = np.round(base_amt * rng.lognormal(0.0, 0.42, size=n), 0)
        # The mandate's authorised ceiling sits above the recurring amount.
        self.max_amount = np.round(self.amount *
                                   rng.uniform(1.0, 2.4, size=n), 0)

        # Which product executes the mandate.
        prod = np.where(
            self.purpose == "Lite Auto Top-Up", "UPI_LITE_ATU",
            np.where(np.isin(self.purpose,
                             ["Mutual Fund SIP", "Insurance Premium",
                              "Loan EMI", "Electricity Bill"]),
                     rng.choice(["UPI_RECURRING", "UPI_AUTOPAY"], size=n,
                                p=[0.46, 0.54]),
                     "UPI_AUTOPAY"))
        self.product = prod

        # Customers who hold mandates skew to higher-activity segments.
        pop = self.pop
        cw = pop.cust_weight * (pop.cust_onboard_day < self.days)
        cw = np.maximum(cw, 0)
        if cw.sum() <= 0:
            cw = np.ones_like(cw)
        self.customer = rng.choice(pop.n_customers, size=n,
                                   p=cw / cw.sum(), replace=True)

        # Merchant: pick within the purpose's MCC.
        mcc_index = {m.code: ix for ix, m in enumerate(MCCS)}
        self.merchant = np.empty(n, dtype=np.int64)
        for code in set(self.mcc.tolist()):
            sel = np.flatnonzero(self.mcc == code)
            pool = pop.merch_by_mcc[mcc_index[code]]
            w = pop.merch_weight[pool]
            self.merchant[sel] = rng.choice(pool, size=len(sel),
                                            p=w / w.sum(), replace=True)

        # 63% of the book predates the window; the rest registers across it,
        # accelerating as AutoPay adoption grows.
        pre = rng.random(n) < 0.63
        self.created_day = np.where(
            pre, -rng.integers(1, 540, size=n),
            (rng.beta(1.5, 1.0, size=n) * self.days).astype(int))

        # Validity: most mandates run for a year or more.
        self.valid_days = rng.choice([365, 730, 1095, 180, 90], size=n,
                                     p=[0.44, 0.24, 0.14, 0.12, 0.06])
        self.expiry_day = self.created_day + self.valid_days

        self.mandate_id = np.array(
            [f"UMN-{2026000000 + i}" for i in range(n)], dtype=object)

        self._plan_lifecycle()
        self._plan_executions()

    # ------------------------------------------------------------ lifecycle
    def _plan_lifecycle(self) -> None:
        """Pause / resume / modify / revoke / cancel windows per mandate."""
        rng, n, days = self.rng, self.n, self.days

        # Revocation (customer-initiated stop) — the churn signal for the book.
        rev = rng.random(n) < 0.088
        self.revoked_day = np.where(
            rev, np.maximum(self.created_day + 5,
                            rng.integers(0, days, size=n)), days + 1)

        # Cancellation by the merchant (subscription ended, service closed).
        can = (rng.random(n) < 0.031) & ~rev
        self.cancelled_day = np.where(
            can, np.maximum(self.created_day + 8,
                            rng.integers(0, days, size=n)), days + 1)

        # Temporary pause — a real AutoPay behaviour before a full revoke.
        pau = (rng.random(n) < 0.062) & ~rev & ~can
        p_start = np.maximum(self.created_day + 3,
                             rng.integers(0, max(1, days - 12), size=n))
        p_len = rng.integers(4, 40, size=n)
        self.paused_day = np.where(pau, p_start, days + 1)
        self.resumed_day = np.where(pau & (rng.random(n) < 0.71),
                                    p_start + p_len, days + 1)

        # Amount modification (plan upgrade, SIP step-up, tariff revision).
        mod = rng.random(n) < 0.074
        self.modified_day = np.where(
            mod, np.maximum(self.created_day + 10,
                            rng.integers(0, days, size=n)), days + 1)
        self.modified_amount = np.round(
            self.amount * rng.uniform(1.05, 1.85, size=n), 0)

        for i in range(n):
            cd = int(self.created_day[i])
            if 0 <= cd < days:
                self._emit(cd, "MANDATE_CREATED", i, initiator="CUSTOMER")
            if 0 <= int(self.modified_day[i]) < days:
                self._emit(int(self.modified_day[i]), "MANDATE_MODIFIED", i,
                           initiator="CUSTOMER",
                           amount=float(self.modified_amount[i]),
                           detail="Recurring amount revised upward")
            if 0 <= int(self.paused_day[i]) < days:
                self._emit(int(self.paused_day[i]), "MANDATE_PAUSED", i,
                           initiator="CUSTOMER",
                           detail="Customer paused collection")
            if 0 <= int(self.resumed_day[i]) < days:
                self._emit(int(self.resumed_day[i]), "MANDATE_RESUMED", i,
                           initiator="CUSTOMER")
            if 0 <= int(self.revoked_day[i]) < days:
                self._emit(int(self.revoked_day[i]), "MANDATE_REVOKED", i,
                           initiator="CUSTOMER",
                           detail="Customer revoked the mandate")
            if 0 <= int(self.cancelled_day[i]) < days:
                self._emit(int(self.cancelled_day[i]), "MANDATE_CANCELLED", i,
                           initiator="MERCHANT",
                           detail="Merchant cancelled the subscription")
            if 0 <= int(self.expiry_day[i]) < days:
                self._emit(int(self.expiry_day[i]), "MANDATE_EXPIRED", i,
                           initiator="SYSTEM")

    def active(self, i: int, day: int) -> bool:
        return (self.created_day[i] <= day < self.expiry_day[i]
                and day < self.revoked_day[i]
                and day < self.cancelled_day[i]
                and not (self.paused_day[i] <= day < self.resumed_day[i]))

    # ----------------------------------------------------------- executions
    def _plan_executions(self) -> None:
        """Per-day list of mandate indices due for execution."""
        rng, n, days = self.rng, self.n, self.days
        self.due: dict[int, list[int]] = {d: [] for d in range(days)}

        # Execution day-of-cycle offset, so the book is not synchronised.
        offset = rng.integers(0, 30, size=n)
        # Debit hour: mandates execute in the overnight/early-morning batch.
        self.exec_hour = rng.choice(
            [0, 1, 2, 3, 4, 5, 6, 9, 11, 14, 18], size=n,
            p=[.06, .11, .17, .16, .12, .08, .07, .06, .06, .06, .05])

        for i in range(n):
            f = self.freq_name[i]
            if f == "AS_PRESENTED":
                d = int(self.created_day[i]) + int(
                    rng.exponential(_AS_PRESENTED_MEAN))
                while d < days:
                    if d >= 0 and self.active(i, d):
                        self.due[d].append(i)
                    d += max(3, int(rng.exponential(_AS_PRESENTED_MEAN)))
                continue
            step = _FREQ_DAYS[f]
            d = int(self.created_day[i]) + step
            # Align to the mandate's own cycle offset for monthly+ frequencies.
            if step >= 28:
                d = int(self.created_day[i]) + step - (
                    int(self.created_day[i]) + int(offset[i])) % step
            while d < days:
                if d >= 0 and self.active(i, d):
                    self.due[d].append(i)
                d += step

    # ---------------------------------------------------------------- events
    def _emit(self, day: int, event: str, i: int, *, initiator: str = "SYSTEM",
              txn_id: str | None = None, amount: float | None = None,
              status: str | None = None, failure_code: str | None = None,
              detail: str | None = None, attempt: int = 0) -> None:
        m = MCC_BY_CODE.get(str(self.mcc[i]))
        self.events.append({
            "event_id": f"MEV-{len(self.events) + 1:08d}",
            "mandate_id": self.mandate_id[i],
            "event": event,
            "event_date": str(self.start_date + timedelta(days=day)),
            "day_index": day,
            "initiator": initiator,
            "product": str(self.product[i]),
            "purpose": str(self.purpose[i]),
            "frequency": str(self.freq_name[i]),
            "mcc": str(self.mcc[i]),
            "category": m.category if m else None,
            "customer_id": f"CUST-{500000 + int(self.customer[i])}",
            "merchant_id": self.pop.merch_id[int(self.merchant[i])],
            "merchant_name": self.pop.merch_name[int(self.merchant[i])],
            "amount_inr": float(amount if amount is not None
                                else self.amount[i]),
            "max_amount_inr": float(self.max_amount[i]),
            "txn_id": txn_id,
            "status": status,
            "failure_code": failure_code,
            "attempt": attempt,
            "detail": detail,
        })

    def emit_execution(self, day: int, i: int, txn_id: str, amount: float,
                       status: str, failure_code: str | None,
                       attempt: int) -> None:
        """Called by the simulator once an execution's outcome is known."""
        initiator = "MERCHANT" if self.freq_name[i] == "AS_PRESENTED" \
            else "SYSTEM"
        if attempt > 0:
            ev = "MANDATE_RETRY"
        elif status == "SUCCESS":
            ev = "MANDATE_EXECUTED"
        else:
            ev = "MANDATE_FAILED"
        self._emit(day, ev, i, initiator=initiator, txn_id=txn_id,
                   amount=amount, status=status, failure_code=failure_code,
                   attempt=attempt,
                   detail="Execution failed — scheduled for re-presentation"
                   if ev == "MANDATE_FAILED" else None)
        # Pre-debit notification precedes every scheduled (non-presented) debit.
        if attempt == 0 and self.freq_name[i] != "AS_PRESENTED":
            self._emit(max(0, day - 1), "PRE_DEBIT_NOTIFICATION", i,
                       initiator="SYSTEM", amount=amount,
                       detail="24-hour pre-debit notification sent")
        if attempt == 0 and self.freq_name[i] == "AS_PRESENTED":
            self._emit(day, "MERCHANT_INITIATED", i, initiator="MERCHANT",
                       txn_id=txn_id, amount=amount, status=status)

    # ------------------------------------------------------------- registry
    def registry_rows(self) -> list[dict]:
        out = []
        for i in range(self.n):
            cd = int(self.created_day[i])
            end = min(int(self.revoked_day[i]), int(self.cancelled_day[i]),
                      int(self.expiry_day[i]))
            if end > self.days:
                status = "ACTIVE" if not (
                    self.paused_day[i] <= self.days - 1 < self.resumed_day[i]
                ) else "PAUSED"
            elif end == int(self.revoked_day[i]):
                status = "REVOKED"
            elif end == int(self.cancelled_day[i]):
                status = "CANCELLED"
            else:
                status = "EXPIRED"
            out.append({
                "mandate_id": self.mandate_id[i],
                "product": str(self.product[i]),
                "purpose": str(self.purpose[i]),
                "frequency": str(self.freq_name[i]),
                "mcc": str(self.mcc[i]),
                "customer_id": f"CUST-{500000 + int(self.customer[i])}",
                "merchant_id": self.pop.merch_id[int(self.merchant[i])],
                "merchant_name": self.pop.merch_name[int(self.merchant[i])],
                "amount_inr": float(self.amount[i]),
                "max_amount_inr": float(self.max_amount[i]),
                "created_date": str(self.start_date + timedelta(days=cd)),
                "expiry_date": str(self.start_date +
                                   timedelta(days=int(self.expiry_day[i]))),
                "status": status,
                "registered_in_window": 0 <= cd < self.days,
            })
        return out

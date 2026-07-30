"""Indian payments calendar — the exogenous drivers behind daily UPI volume.

Real payment traffic is not a trend line with noise on top; it is a trend line
multiplied by a *calendar*. Salary credits land on fixed days, weekends behave
differently from weekdays, festivals move billions of rupees in a 72-hour
window, bank holidays suppress settlement-heavy flows, and quarter ends pull
mandate executions forward. This module encodes that calendar for the 2026
simulation window so every downstream series inherits real structure instead of
fabricated smoothness.

Nothing here is random. Given a date the multipliers are deterministic, which
is what lets the ML layer actually *learn* seasonality rather than memorise
noise.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta

# ---------------------------------------------------------------------------
# Gazetted / bank holidays and festivals, 2026. Dates follow the 2026 Indian
# calendar; `spend` is the multiplier on discretionary consumer spend and
# `settlement` the multiplier on bank-settlement-dependent flows (mandates,
# credit, cross-border) which stall on a bank holiday.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Festival:
    name: str
    day: date
    kind: str                # festival | bank_holiday | shopping
    spend: float             # peak-day multiplier on consumer spend
    settlement: float        # multiplier on settlement-dependent flows
    lead_days: int = 0       # days of build-up before the peak
    tail_days: int = 0       # days of elevated spend after the peak
    categories: tuple[str, ...] = ()   # merchant categories that spike hardest


FESTIVALS_2026: list[Festival] = [
    Festival("Makar Sankranti / Pongal", date(2026, 1, 14), "festival", 1.22,
             0.86, lead_days=2, tail_days=1,
             categories=("Grocery", "Fashion", "Travel")),
    Festival("Republic Day", date(2026, 1, 26), "bank_holiday", 1.08, 0.35,
             lead_days=1, categories=("E-commerce", "Food Delivery")),
    Festival("Republic Day Sale", date(2026, 1, 23), "shopping", 1.34, 1.02,
             lead_days=2, tail_days=2,
             categories=("E-commerce", "Electronics", "Fashion")),
    Festival("Maha Shivaratri", date(2026, 2, 15), "festival", 1.11, 0.72,
             lead_days=1, categories=("Grocery", "Travel")),
    Festival("Holi", date(2026, 3, 4), "festival", 1.28, 0.55, lead_days=3,
             tail_days=1, categories=("Grocery", "Fashion", "Food Delivery")),
    Festival("Ugadi / Gudi Padwa", date(2026, 3, 19), "festival", 1.19, 0.78,
             lead_days=2, categories=("Fashion", "Electronics", "Grocery")),
    Festival("Financial Year End", date(2026, 3, 31), "bank_holiday", 1.05,
             1.45, lead_days=4,
             categories=("Insurance", "Wealth / SIP", "Utilities")),
    Festival("Eid al-Fitr", date(2026, 3, 21), "festival", 1.24, 0.62,
             lead_days=3, tail_days=1,
             categories=("Fashion", "Grocery", "Food Delivery")),
    Festival("Ram Navami", date(2026, 3, 27), "festival", 1.09, 0.80),
    Festival("Ambedkar Jayanti", date(2026, 4, 14), "bank_holiday", 1.04, 0.40),
    Festival("Akshaya Tritiya", date(2026, 4, 20), "festival", 1.31, 1.05,
             lead_days=2, tail_days=1,
             categories=("Retail", "Wealth / SIP", "E-commerce")),
    Festival("Labour Day", date(2026, 5, 1), "bank_holiday", 1.02, 0.45),
    Festival("Summer Travel Peak", date(2026, 5, 18), "shopping", 1.16, 1.03,
             lead_days=6, tail_days=6, categories=("Travel", "Mobility")),
    Festival("Bakrid / Eid al-Adha", date(2026, 5, 27), "festival", 1.21, 0.60,
             lead_days=2, categories=("Grocery", "Fashion")),
    Festival("Monsoon Sale", date(2026, 6, 20), "shopping", 1.26, 1.01,
             lead_days=2, tail_days=3,
             categories=("E-commerce", "Electronics", "Fashion")),
    Festival("Rath Yatra", date(2026, 6, 16), "festival", 1.07, 0.83),
    Festival("Muharram", date(2026, 6, 26), "bank_holiday", 1.01, 0.48),
    Festival("Guru Purnima", date(2026, 7, 29), "festival", 1.06, 0.88),
    Festival("Quarter Close Q1FY27", date(2026, 6, 30), "bank_holiday", 1.03,
             1.38, lead_days=3, categories=("Insurance", "Wealth / SIP")),
]

# Regional holidays suppress a single state's traffic rather than the country's.
REGIONAL_HOLIDAYS_2026: dict[date, tuple[str, ...]] = {
    date(2026, 1, 15): ("Tamil Nadu", "Andhra Pradesh", "Telangana"),
    date(2026, 4, 14): ("Tamil Nadu", "West Bengal", "Kerala", "Punjab"),
    date(2026, 4, 15): ("West Bengal", "Assam"),
    date(2026, 5, 1): ("Maharashtra", "Gujarat"),
    date(2026, 3, 5): ("Uttar Pradesh", "Bihar", "Rajasthan"),
}


@dataclass
class DayContext:
    """Everything the volume model needs to know about one calendar day."""
    day_index: int
    day: date
    weekday: int                     # 0 = Monday
    is_weekend: bool
    is_salary_window: bool
    is_month_end: bool
    is_quarter_end: bool
    holiday: str | None
    festival: str | None
    spend_mult: float
    settlement_mult: float
    category_boost: dict[str, float] = field(default_factory=dict)
    suppressed_states: tuple[str, ...] = ()

    @property
    def label(self) -> str:
        return self.festival or self.holiday or (
            "Weekend" if self.is_weekend else "Working day")


def _salary_multiplier(d: date) -> float:
    """Salary credits in India cluster on the 1st, the 7th (PSU/government) and
    the last working day. Spend follows the credit with a one-to-three day lag
    and decays through the month — the classic 'first-week bulge'."""
    dom = d.day
    days_in_month = (d.replace(day=28) + timedelta(days=4)).replace(day=1)
    days_in_month = (days_in_month - timedelta(days=1)).day
    if dom in (1, 2, 3):
        return 1.24 - 0.04 * (dom - 1)
    if dom in (4, 5):
        return 1.12
    if dom in (6, 7, 8):
        return 1.16
    if dom in (9, 10):
        return 1.06
    if dom >= days_in_month - 1:
        return 1.09          # last-working-day credits
    if 11 <= dom <= 20:
        return 0.97
    return 0.92              # the pre-salary trough


def _weekday_multiplier(d: date) -> float:
    """Saturday holds up on consumer spend; Sunday drops on B2B/settlement.
    Monday carries the weekend backlog. Friday is the discretionary peak."""
    return {0: 1.04, 1: 1.00, 2: 0.99, 3: 1.01, 4: 1.07, 5: 1.05, 6: 0.88}[
        d.weekday()]


def _seasonal_multiplier(d: date) -> float:
    """Slow annual wave: post-festive January lull, March fiscal push, May
    travel season, June monsoon softness."""
    month_wave = {1: 0.96, 2: 0.98, 3: 1.05, 4: 1.01, 5: 1.04, 6: 0.99,
                  7: 1.02, 8: 1.01, 9: 1.06, 10: 1.14, 11: 1.10, 12: 1.07}
    return month_wave.get(d.month, 1.0)


def build_calendar(start: date, days: int) -> list[DayContext]:
    """Deterministic per-day context for the whole simulation window."""
    by_day: dict[date, list[tuple[Festival, float]]] = {}
    for f in FESTIVALS_2026:
        for off in range(-f.lead_days, f.tail_days + 1):
            d = f.day + timedelta(days=off)
            if off == 0:
                weight = 1.0
            elif off < 0:
                weight = 0.30 + 0.55 * (1 - abs(off) / (f.lead_days + 1))
            else:
                weight = 0.25 + 0.40 * (1 - off / (f.tail_days + 1))
            by_day.setdefault(d, []).append((f, weight))

    out: list[DayContext] = []
    for i in range(days):
        d = start + timedelta(days=i)
        spend = _weekday_multiplier(d) * _salary_multiplier(d) * \
            _seasonal_multiplier(d)
        settlement = 1.0
        holiday = festival = None
        cat_boost: dict[str, float] = {}

        for f, w in by_day.get(d, []):
            spend *= 1.0 + (f.spend - 1.0) * w
            settlement *= 1.0 + (f.settlement - 1.0) * w
            if w >= 0.9:
                if f.kind == "bank_holiday":
                    holiday = f.name
                else:
                    festival = f.name
            elif festival is None and holiday is None:
                festival = f"{f.name} (build-up)" if w > 0.55 else None
            for c in f.categories:
                cat_boost[c] = cat_boost.get(c, 1.0) * (
                    1.0 + (f.spend - 1.0) * w * 1.9)

        if d.weekday() == 6:
            settlement *= 0.42          # Sunday: no bank settlement window
        elif d.weekday() == 5:
            settlement *= 0.78
        # Second and fourth Saturdays are bank holidays in India.
        if d.weekday() == 5 and (d.day - 1) // 7 in (1, 3):
            settlement *= 0.55

        nxt = d + timedelta(days=1)
        is_month_end = nxt.month != d.month
        is_quarter_end = is_month_end and d.month in (3, 6, 9, 12)
        if is_month_end:
            settlement *= 1.22
        if is_quarter_end:
            settlement *= 1.18

        out.append(DayContext(
            day_index=i, day=d, weekday=d.weekday(),
            is_weekend=d.weekday() >= 5,
            is_salary_window=_salary_multiplier(d) > 1.05,
            is_month_end=is_month_end, is_quarter_end=is_quarter_end,
            holiday=holiday, festival=festival,
            spend_mult=round(spend, 5), settlement_mult=round(settlement, 5),
            category_boost={k: round(v, 4) for k, v in cat_boost.items()},
            suppressed_states=REGIONAL_HOLIDAYS_2026.get(d, ()),
        ))
    return out

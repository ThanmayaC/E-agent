"""Observation detectors — the analytical layer under the daily report.

A report that prints the same twelve sections with today's numbers substituted
in is a template, and reads like one. What a Product Manager actually writes is
*selective*: they look at everything, then say the three or four things that
mattered today and stay quiet about the rest.

That is what this module does. Every detector scans one facet of the day
(products, issuers, apps, categories, geography, failure codes, retries,
disputes, customers, merchants) and emits zero or more :class:`Observation`
objects, each carrying a **materiality** score. The report renders the ranked
top of that list, so a day when an issuer broke reads completely differently
from a day when a campaign landed — without anyone writing either sentence in
advance.

Materiality is deliberately a product of *how unusual* a movement is (a z-score
against the trailing window) and *how much it matters* (the share of volume or
value behind it). A 40% swing on an entity carrying 0.1% of volume is noise; a
2% swing on the largest issuer is a headline.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

import numpy as np
import pandas as pd


@dataclass
class Observation:
    """One thing worth saying about a day, with the evidence behind it."""

    text: str
    materiality: float
    section: str                       # where it belongs in the report
    evidence: dict = field(default_factory=dict)
    kind: str = "observation"          # observation | risk | opportunity

    def evidence_line(self) -> str:
        parts = [f"{k}={_fmt(v)}" for k, v in self.evidence.items()]
        return "; ".join(parts)


def _fmt(v) -> str:
    if isinstance(v, float):
        return f"{v:,.2f}".rstrip("0").rstrip(".") if abs(v) < 1e7 else f"{v:,.0f}"
    if isinstance(v, (int, np.integer)):
        return f"{int(v):,}"
    return str(v)


def zscore(current: float, history: pd.Series) -> float:
    """Robust z-score of today against its own recent history.

    Median/MAD rather than mean/sd: a window containing last week's incident
    should not widen the band so far that today's incident looks normal.
    """
    h = history.dropna()
    if len(h) < 6:
        return 0.0
    med = float(h.median())
    mad = float((h - med).abs().median())
    scale = mad * 1.4826
    if scale < 1e-9:
        scale = float(h.std(ddof=0)) or 1e-9
    return (current - med) / scale


def pct_change(cur: float, prev: float) -> float | None:
    if prev is None or prev == 0 or cur is None:
        return None
    return (cur - prev) / abs(prev) * 100.0


def _arrow(x: float) -> str:
    return "up" if x > 0 else "down"


# ---------------------------------------------------------------------------
# Detectors. Each takes the day's slice plus its trailing history and returns
# observations. They are intentionally independent — adding a new facet of the
# business means adding a detector, not editing a report template.
# ---------------------------------------------------------------------------
def observe_headline(day: pd.Series, hist: pd.DataFrame) -> list[Observation]:
    out: list[Observation] = []
    z_vol = zscore(day["attempts"], hist["attempts"])
    z_sr = zscore(day["success_rate"], hist["success_rate"])
    z_val = zscore(day["value_inr"], hist["value_inr"])

    if abs(z_vol) >= 1.8:
        wow = pct_change(day["attempts"], day.get("attempts_w1"))
        out.append(Observation(
            text=(f"Attempt volume ran {abs(z_vol):.1f} standard deviations "
                  f"{_arrow(z_vol)} its trailing 28-day median at "
                  f"{day['attempts']:,.0f}"
                  + (f", {abs(wow):.1f}% {_arrow(wow)} on the same weekday "
                     f"last week" if wow is not None else "") + "."),
            materiality=abs(z_vol) * 1.6, section="headline",
            evidence={"attempts": day["attempts"],
                      "trailing_median": float(hist["attempts"].median()),
                      "z": round(z_vol, 2)}))

    if abs(z_sr) >= 1.5:
        out.append(Observation(
            text=(f"Success rate closed at {day['success_rate']:.2f}%, "
                  f"{abs(day['success_rate'] - hist['success_rate'].median()):.2f}pp "
                  f"{_arrow(z_sr)} the trailing median — a "
                  f"{abs(z_sr):.1f}-sigma move."),
            materiality=abs(z_sr) * 2.4, section="headline",
            kind="risk" if z_sr < 0 else "observation",
            evidence={"success_rate": day["success_rate"],
                      "trailing_median": float(hist["success_rate"].median()),
                      "z": round(z_sr, 2)}))

    # Value and volume disagreeing is the interesting case: it means the mix
    # moved, not the demand.
    if abs(z_val) >= 1.5 and abs(z_val - z_vol) >= 1.4:
        out.append(Observation(
            text=(f"Settled value moved {_arrow(z_val)} while volume moved "
                  f"{_arrow(z_vol)} — average ticket at "
                  f"₹{day['avg_ticket']:,.0f} against a trailing "
                  f"₹{hist['avg_ticket'].median():,.0f}, so the day's shape is "
                  f"a mix shift rather than a demand shift."),
            materiality=abs(z_val - z_vol) * 1.5, section="headline",
            evidence={"value_inr": day["value_inr"],
                      "avg_ticket": day["avg_ticket"],
                      "trailing_avg_ticket": float(hist["avg_ticket"].median())}))
    return out


def observe_entity(day_rows: pd.DataFrame, hist: pd.DataFrame, *,
                   entity_col: str, label: str, section: str,
                   min_share: float = 0.02, top: int = 3
                   ) -> list[Observation]:
    """Movers within a dimension, scored by surprise × economic weight.

    ``hist`` carries the same dimension over the trailing window, so an
    entity's own normal range is what it is judged against — a bank that
    always sits at 94% is not reported as broken every day.
    """
    if day_rows.empty:
        return []
    total = day_rows["attempts"].sum()
    if total <= 0:
        return []
    out: list[Observation] = []
    for _, r in day_rows.iterrows():
        share = r["attempts"] / total
        if share < min_share:
            continue
        h = hist[hist[entity_col] == r[entity_col]]
        if len(h) < 8:
            continue
        z_sr = zscore(r["success_rate"], h["success_rate"])
        z_vol = zscore(r["attempts"], h["attempts"])
        # Weight surprise by the entity's economic footprint.
        weight = math.sqrt(share)
        if abs(z_sr) >= 2.0:
            gap = r["success_rate"] - float(h["success_rate"].median())
            out.append(Observation(
                text=(f"{label} {r[entity_col]} ran at "
                      f"{r['success_rate']:.2f}% success on "
                      f"{r['attempts']:,.0f} attempts ({share * 100:.1f}% of "
                      f"the day), {abs(gap):.2f}pp {_arrow(gap)} its own "
                      f"28-day median."),
                materiality=abs(z_sr) * weight * 3.0, section=section,
                kind="risk" if gap < 0 else "observation",
                evidence={entity_col: r[entity_col],
                          "attempts": r["attempts"],
                          "success_rate": r["success_rate"],
                          "own_median": round(float(h["success_rate"].median()), 3),
                          "z": round(z_sr, 2)}))
        if abs(z_vol) >= 2.2:
            delta = pct_change(r["attempts"], float(h["attempts"].median()))
            out.append(Observation(
                text=(f"{label} {r[entity_col]} carried "
                      f"{r['attempts']:,.0f} attempts, "
                      f"{abs(delta):.0f}% {_arrow(delta)} its trailing median "
                      f"and {share * 100:.1f}% of the day's volume."),
                materiality=abs(z_vol) * weight * 2.2, section=section,
                evidence={entity_col: r[entity_col],
                          "attempts": r["attempts"],
                          "own_median": float(h["attempts"].median()),
                          "z": round(z_vol, 2)}))
    out.sort(key=lambda o: -o.materiality)
    return out[:top]


def observe_failures(fail_today: pd.DataFrame, fail_hist: pd.DataFrame,
                     attempts: float) -> list[Observation]:
    """Which decline codes moved, and who owns them."""
    if fail_today.empty or attempts <= 0:
        return []
    out: list[Observation] = []
    for _, r in fail_today.iterrows():
        h = fail_hist[fail_hist["failure_code"] == r["failure_code"]]
        if len(h) < 8:
            continue
        rate_today = r["n"] / attempts * 100
        hist_rate = h["rate_pct"]
        z = zscore(rate_today, hist_rate)
        if z < 2.0 or r["n"] < 12:
            continue
        out.append(Observation(
            text=(f"Decline code {r['failure_code']} "
                  f"({r['failure_reason']}) fired {r['n']:,} times — "
                  f"{rate_today:.3f}% of attempts against a trailing "
                  f"{hist_rate.median():.3f}%. Owner: {r['failure_owner']}."),
            materiality=z * math.sqrt(max(rate_today, 0.01)) * 2.6,
            section="failures", kind="risk",
            evidence={"failure_code": r["failure_code"],
                      "count": int(r["n"]),
                      "rate_pct": round(rate_today, 4),
                      "trailing_rate_pct": round(float(hist_rate.median()), 4),
                      "owner": r["failure_owner"], "z": round(z, 2)}))
    out.sort(key=lambda o: -o.materiality)
    return out[:4]


def observe_retries(day: pd.Series, hist: pd.DataFrame) -> list[Observation]:
    """A retry wave is the fingerprint of an availability problem."""
    if day.get("retries", 0) <= 0:
        return []
    z = zscore(day["retry_share"], hist["retry_share"])
    if z < 2.0:
        return []
    rec = day.get("retry_recovery_pct")
    tail = ""
    if rec is not None and not (isinstance(rec, float) and math.isnan(rec)):
        tail = (f" Only {rec:.1f}% of re-presented payments eventually "
                f"succeeded, so the queue was absorbing failures rather than "
                f"clearing them." if rec < 55 else
                f" {rec:.1f}% of re-presented payments recovered, so the "
                f"retry path was doing its job.")
    return [Observation(
        text=(f"Retries reached {day['retries']:,.0f} attempts "
              f"({day['retry_share']:.2f}% of the day, "
              f"{abs(z):.1f} sigma above normal)." + tail),
        materiality=z * 2.8, section="failures",
        kind="risk" if (rec or 100) < 55 else "observation",
        evidence={"retries": day["retries"],
                  "retry_share_pct": day["retry_share"],
                  "recovery_pct": rec, "z": round(z, 2)})]


def observe_adjustments(day: pd.Series, hist: pd.DataFrame
                        ) -> list[Observation]:
    """Refunds, reversals and disputes — money moving backwards."""
    out: list[Observation] = []
    for col, noun, sect in (("refunds", "refunds", "adjustments"),
                            ("reversals", "auto-reversals", "adjustments"),
                            ("chargebacks", "disputes", "adjustments")):
        if col not in day or day[col] <= 0:
            continue
        z = zscore(day[col], hist[col])
        if z < 2.2:
            continue
        out.append(Observation(
            text=(f"{day[col]:,.0f} {noun} were raised, "
                  f"{abs(z):.1f} sigma above the trailing median of "
                  f"{hist[col].median():,.0f}."),
            materiality=z * (2.4 if col == "chargebacks" else 1.7),
            section=sect, kind="risk",
            evidence={col: day[col],
                      "trailing_median": float(hist[col].median()),
                      "z": round(z, 2)}))
    return out


# Event kinds an operations desk owns, as opposed to commercial or demand-side
# ones. A merchant losing an acquirer to a competitor is a Sev-2 to the
# business and still not an outage; calling it one in an operations report is
# how an executive learns to stop trusting the report. A fraud ring, by
# contrast, is squarely operational even though nothing broke.
RELIABILITY_KINDS = frozenset({
    "bank_outage", "psp_degradation", "network_latency", "settlement_delay",
    "maintenance_window", "fraud_spike",
})


def _occurrence_active(inc: dict, day_str: str) -> bool:
    """Is this event actually live today, as opposed to merely spanning today?

    Two cases would otherwise flood every report with the same rows. A
    recurring maintenance window has a start and an end months apart but only
    fires for a day or two each cycle. A ``step`` event — a cap change, a
    corridor launch — never ends at all by construction: it is a permanent
    regime change, so it is context for the first few days and background
    thereafter.
    """
    if not (inc["start_date"] <= day_str <= inc["end_date"]):
        return False
    from datetime import date as _date
    d0 = _date.fromisoformat(inc["start_date"])
    dd = (_date.fromisoformat(day_str) - d0).days
    every = inc.get("recurs_every_days")
    if every:
        return (dd % int(every)) < int(inc.get("duration_days_each") or 1)
    if inc.get("shape") == "step":
        return dd <= 3
    return True


def observe_incidents(incidents: list[dict], day_str: str) -> list[Observation]:
    """Ground-truth operational events genuinely live on the day."""
    out: list[Observation] = []
    for inc in incidents:
        if not _occurrence_active(inc, day_str):
            continue
        sev_weight = {"Sev-1": 9.0, "Sev-2": 5.0, "Sev-3": 2.0}.get(
            inc["severity"], 2.0)
        if inc.get("kind") not in RELIABILITY_KINDS:
            sev_weight *= 0.55
        scope = next((inc[k] for k in ("scope_bank", "scope_psp",
                                       "scope_product", "scope_mcc",
                                       "scope_region") if inc.get(k)),
                     "ecosystem-wide")
        window = ""
        if inc.get("hour_from") is not None:
            window = (f" between {int(inc['hour_from']):02d}:00 and "
                      f"{int(inc['hour_to']):02d}:00")
        out.append(Observation(
            text=(f"**{inc['event_id']}** ({inc['severity']}) — "
                  f"{inc['title']}, scoped to {scope}{window}. "
                  f"{inc['narrative']}"),
            materiality=sev_weight, section="incidents",
            kind="risk" if inc["severity"] != "Sev-3" else "observation",
            evidence={"event_id": inc["event_id"],
                      "kind": inc.get("kind"),
                      "severity": inc["severity"],
                      "window": f"{inc['start_date']} to {inc['end_date']}",
                      "success_impact_pp": inc.get("success_impact_pp"),
                      "volume_impact_pct": inc.get("volume_impact_pct")}))
    out.sort(key=lambda o: -o.materiality)
    return out


def observe_concentration(day_rows: pd.DataFrame, *, entity_col: str,
                          label: str, section: str) -> list[Observation]:
    """Dependence risk — how much of the day rests on a few names."""
    if day_rows.empty:
        return []
    total = day_rows["attempts"].sum()
    if total <= 0:
        return []
    top5 = day_rows.nlargest(5, "attempts")["attempts"].sum() / total * 100
    if top5 < 72:
        return []
    leader = day_rows.nlargest(1, "attempts").iloc[0]
    return [Observation(
        text=(f"The top five {label} carried {top5:.1f}% of the day's "
              f"attempts, with {leader[entity_col]} alone at "
              f"{leader['attempts'] / total * 100:.1f}% — a single-point "
              f"dependency worth watching in capacity and continuity "
              f"planning."),
        materiality=(top5 - 70) * 0.22, section=section, kind="risk",
        evidence={"top5_share_pct": round(top5, 2),
                  "leader": leader[entity_col],
                  "leader_share_pct": round(
                      leader["attempts"] / total * 100, 2)})]


def observe_opportunity(day_rows: pd.DataFrame, hist: pd.DataFrame, *,
                        entity_col: str, label: str, section: str
                        ) -> list[Observation]:
    """Growth worth leaning into, as distinct from growth worth worrying about."""
    if day_rows.empty:
        return []
    out: list[Observation] = []
    for _, r in day_rows.iterrows():
        h = hist[hist[entity_col] == r[entity_col]]
        if len(h) < 14 or r["attempts"] < 40:
            continue
        ordered = h.sort_values("txn_date")
        early = ordered.head(7)["attempts"].mean()
        late = ordered.tail(7)["attempts"].mean()
        growth = pct_change(late, early)
        if growth is None or growth < 25:
            continue
        sr_ok = r["success_rate"] >= float(h["success_rate"].median()) - 0.4
        out.append(Observation(
            text=(f"{label} {r[entity_col]} is compounding — attempts up "
                  f"{growth:.0f}% across the trailing window to "
                  f"{r['attempts']:,.0f} today"
                  + (", with success holding, so the growth is healthy and "
                     "worth funding." if sr_ok else
                     ", but success is slipping as it scales, so the growth "
                     "is outrunning its reliability.")),
            materiality=min(growth / 12.0, 6.0),
            section=section, kind="opportunity" if sr_ok else "risk",
            evidence={entity_col: r[entity_col], "attempts": r["attempts"],
                      "window_growth_pct": round(growth, 1),
                      "success_rate": r["success_rate"]}))
    out.sort(key=lambda o: -o.materiality)
    return out[:2]

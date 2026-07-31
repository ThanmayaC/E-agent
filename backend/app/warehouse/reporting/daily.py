"""Corpus-derived daily operations reports.

These replace the reports the old enterprise generator wrote from a separate,
hand-authored KPI series. Those reports carried the line *"Source:
upi_kpis_month.xlsx"* and were, literally, summaries of numbers that had been
asserted rather than measured — which is why they read like metadata and why
nothing in them could be checked against a transaction.

Every figure below is a SQL aggregate over the raw corpus, every observation is
produced by a detector that scored it against the entity's own recent history,
and every report ends with an evidence appendix a reader can re-derive. If a
sentence appears in one of these reports, the rows that justify it exist.

    python -m app.warehouse.reporting.daily            # write all 206 days
    python -m app.warehouse.reporting.daily --day 150  # one day, to stdout
"""
from __future__ import annotations

import argparse
from datetime import date, datetime, timedelta
from pathlib import Path

import pandas as pd

from app.warehouse.engine import Warehouse, get_warehouse
from app.warehouse.reporting.frames import ReportFrames, load_frames
from app.warehouse.reporting.observe import (
    RELIABILITY_KINDS, Observation, observe_adjustments,
    observe_concentration, observe_entity, observe_failures, observe_headline,
    observe_incidents, observe_opportunity, observe_retries, pct_change,
    zscore,
)

ORG_NAME = "NPCI (Synthetic Demonstration)"
DEPARTMENT = "UPI Products"
TRAILING = 28

# How a detector's section reads in prose.
_SECTION_NOUN = {
    "headline": "the headline numbers", "banks": "issuer performance",
    "psps": "app performance", "products": "the product mix",
    "categories": "merchant categories", "geography": "geography",
    "failures": "the decline profile", "adjustments": "money moving back",
    "incidents": "the operational record",
}


# ---------------------------------------------------------------------------
# Small formatting helpers. The rounding is deliberate: a report that quotes
# eight significant figures is not more accurate, it is less readable, and the
# evidence appendix carries the precise values anyway.
# ---------------------------------------------------------------------------
def _inr(v: float) -> str:
    if v is None or pd.isna(v):
        return "n/a"
    v = float(v)
    if abs(v) >= 1e7:
        return f"₹{v / 1e7:,.2f} Cr"
    if abs(v) >= 1e5:
        return f"₹{v / 1e5:,.2f} L"
    return f"₹{v:,.0f}"


def _delta(cur, prev, unit: str = "%", pp: bool = False) -> str:
    if prev is None or pd.isna(prev) or pd.isna(cur):
        return "—"
    if pp:
        d = cur - prev
        return f"{'+' if d >= 0 else '−'}{abs(d):.2f}pp"
    d = pct_change(cur, prev)
    if d is None:
        return "—"
    return f"{'+' if d >= 0 else '−'}{abs(d):.1f}%"


def _table(headers: list[str], rows: list[list]) -> str:
    head = "| " + " | ".join(headers) + " |"
    rule = "|" + "|".join("---" for _ in headers) + "|"
    body = "\n".join("| " + " | ".join(str(c) for c in r) + " |" for r in rows)
    return f"{head}\n{rule}\n{body}" if rows else "_No rows._"


class DailyReportBuilder:
    """Builds one PM-grade report per day in the corpus."""

    def __init__(self, wh: Warehouse, frames: ReportFrames | None = None):
        self.wh = wh
        self.f = frames or load_frames(wh)
        self._cal = self.f.calendar.set_index("date")

    # ------------------------------------------------------------- slicing
    def _hist(self, df: pd.DataFrame, day: str, col: str = "txn_date"
              ) -> pd.DataFrame:
        """The trailing window *before* today — never including today itself."""
        d0 = str(pd.Timestamp(day) - pd.Timedelta(days=TRAILING))
        return df[(df[col] < day) & (df[col] >= d0[:10])]

    def _day_rows(self, df: pd.DataFrame, day: str) -> pd.DataFrame:
        return df[df["txn_date"] == day]

    # -------------------------------------------------------- observations
    def observations(self, day: str) -> list[Observation]:
        f = self.f
        drow = f.daily[f.daily["txn_date"] == day]
        if drow.empty:
            return []
        cur = drow.iloc[0]
        hist = self._hist(f.daily, day)
        if len(hist) < 6:
            hist = f.daily[f.daily["txn_date"] < day]

        obs: list[Observation] = []
        obs += observe_incidents(f.incidents, day)
        obs += observe_headline(cur, hist)
        obs += observe_entity(self._day_rows(f.by_bank, day),
                              self._hist(f.by_bank, day),
                              entity_col="payer_bank", label="Issuer",
                              section="banks")
        obs += observe_entity(self._day_rows(f.by_psp, day),
                              self._hist(f.by_psp, day),
                              entity_col="payer_psp", label="App",
                              section="psps")
        obs += observe_entity(self._day_rows(f.by_product, day),
                              self._hist(f.by_product, day),
                              entity_col="product_name", label="Product",
                              section="products", min_share=0.005)
        obs += observe_entity(self._day_rows(f.by_category, day),
                              self._hist(f.by_category, day),
                              entity_col="mcc_category", label="Category",
                              section="categories", min_share=0.01)
        obs += observe_entity(self._day_rows(f.by_region, day),
                              self._hist(f.by_region, day),
                              entity_col="region", label="Region",
                              section="geography", min_share=0.03)
        obs += observe_failures(self._day_rows(f.failures, day),
                                self._hist(f.failures, day), cur["attempts"])
        obs += observe_retries(cur, hist)
        obs += observe_adjustments(cur, hist)
        obs += observe_concentration(self._day_rows(f.by_bank, day),
                                     entity_col="payer_bank", label="issuers",
                                     section="banks")
        obs += observe_opportunity(self._day_rows(f.by_product, day),
                                   self._hist(f.by_product, day),
                                   entity_col="product_name", label="Product",
                                   section="products")
        obs.sort(key=lambda o: -o.materiality)
        return obs

    # -------------------------------------------------------------- render
    def render(self, day: str) -> str:
        f = self.f
        cur = f.daily[f.daily["txn_date"] == day].iloc[0]
        hist = self._hist(f.daily, day)
        obs = self.observations(day)
        dt = date.fromisoformat(day)
        cal = self._cal.loc[day] if day in self._cal.index else None

        prev_row = f.daily[f.daily["txn_date"] < day].tail(1)
        prev = prev_row.iloc[0] if not prev_row.empty else None
        month_rows = f.daily[f.daily["txn_date"].str[:7] == day[:7]]
        mtd = month_rows[month_rows["txn_date"] <= day]

        parts: list[str] = []
        parts.append(self._headline(cur, prev, hist, dt, cal, obs))
        parts.append(self._kpi_block(cur, prev, hist, mtd))
        parts.append(self._what_moved(obs))
        parts.append(self._products(day, cur))
        parts.append(self._rails(day))
        parts.append(self._demand(day, cur))
        parts.append(self._failures(day, cur, hist, obs))
        parts.append(self._money_back(cur, hist))
        parts.append(self._customers(day, cur, hist))
        parts.append(self._incidents(obs))
        parts.append(self._risks_opportunities(obs))
        parts.append(self._executive(cur, hist, obs, dt))
        parts.append(self._evidence(day, obs, cur))
        return "\n\n".join(p for p in parts if p)

    # --- sections ---------------------------------------------------------
    def _headline(self, cur, prev, hist, dt: date, cal, obs) -> str:
        wow = _delta(cur["attempts"], cur.get("attempts_w1"))
        dod = _delta(cur["attempts"], prev["attempts"] if prev is not None
                     else None)
        sr_med = float(hist["success_rate"].median()) if len(hist) else \
            cur["success_rate"]
        shape = "in line with" if abs(cur["success_rate"] - sr_med) < 0.25 \
            else ("below" if cur["success_rate"] < sr_med else "above")
        label = ""
        if cal is not None:
            bits = [b for b in (cal.get("festival"), cal.get("holiday"),
                                cal.get("label")) if b and str(b) != "nan"]
            if bits:
                label = f" ({bits[0]})"
        lead = (
            f"The rail took **{cur['attempts']:,.0f} payment attempts** on "
            f"{dt:%A %d %B %Y}{label} and settled "
            f"**{_inr(cur['value_inr'])}** across "
            f"{cur['successes']:,.0f} successful payments. Volume was {dod} "
            f"on yesterday and {wow} on the same weekday last week. Success "
            f"closed at **{cur['success_rate']:.2f}%**, {shape} the trailing "
            f"28-day median of {sr_med:.2f}%.")
        # Incidents get their own section; repeating them verbatim here is
        # how a report starts feeling generated rather than written.
        top = [o for o in obs
               if o.materiality >= 4.0 and o.section != "incidents"][:2]
        if top:
            lead += "\n\n" + " ".join(o.text for o in top)
        return f"## Summary\n\n{lead}"

    def _kpi_block(self, cur, prev, hist, mtd) -> str:
        def row(name, key, fmt, pp=False):
            v = cur[key]
            p = prev[key] if prev is not None else None
            w = cur.get(f"{key}_w1")
            m = mtd[key].mean() if len(mtd) else None
            return [name, fmt(v), _delta(v, p, pp=pp), _delta(v, w, pp=pp),
                    fmt(m) if m is not None else "—"]

        rows = [
            row("Attempts", "attempts", lambda v: f"{v:,.0f}"),
            row("Successful payments", "successes", lambda v: f"{v:,.0f}"),
            row("Success rate", "success_rate", lambda v: f"{v:.2f}%", pp=True),
            row("Settled value", "value_inr", _inr),
            row("Average ticket", "avg_ticket", _inr),
            row("Technical declines", "technical_pct",
                lambda v: f"{v:.3f}%", pp=True),
            row("Business declines", "business_pct",
                lambda v: f"{v:.3f}%", pp=True),
            row("Risk declines", "risk_pct", lambda v: f"{v:.3f}%", pp=True),
            row("Timeout declines", "timeout_pct",
                lambda v: f"{v:.3f}%", pp=True),
            row("Retry share", "retry_share", lambda v: f"{v:.2f}%", pp=True),
            row("Latency p95", "latency_p95", lambda v: f"{v:,.0f} ms"),
            row("Active customers", "customers", lambda v: f"{v:,.0f}"),
            row("Active merchants", "merchants", lambda v: f"{v:,.0f}"),
        ]
        return ("## Key measures\n\n"
                + _table(["Measure", "Today", "vs yesterday", "vs last week",
                          "Month to date"], rows))

    def _what_moved(self, obs) -> str:
        picked = [o for o in obs if o.section in
                  ("headline", "banks", "psps", "products", "categories",
                   "geography") and o.materiality >= 2.2][:6]
        if not picked:
            return ("## What moved\n\nNothing crossed the materiality "
                    "threshold today: every dimension tracked inside its own "
                    "28-day band, so the day is a clean baseline rather than "
                    "an event to explain.")
        lines = "\n".join(f"- {o.text}" for o in picked)
        return f"## What moved\n\n{lines}"

    def _products(self, day: str, cur) -> str:
        d = self._day_rows(self.f.by_product, day).nlargest(8, "attempts")
        h = self._hist(self.f.by_product, day)
        rows = []
        for _, r in d.iterrows():
            own = h[h["product_name"] == r["product_name"]]
            base = float(own["attempts"].median()) if len(own) else None
            rows.append([
                r["product_name"], f"{r['attempts']:,.0f}",
                f"{r['attempts'] / cur['attempts'] * 100:.1f}%",
                f"{r['success_rate']:.2f}%", _inr(r["value_inr"]),
                _delta(r["attempts"], base)])
        return ("## Product performance\n\n"
                + _table(["Product", "Attempts", "Share", "Success",
                          "Settled value", "vs 28d median"], rows))

    def _rails(self, day: str) -> str:
        out = []
        for frame, col, title in ((self.f.by_bank, "payer_bank",
                                   "Issuer performance"),
                                  (self.f.by_psp, "payer_psp",
                                   "App / PSP performance")):
            d = self._day_rows(frame, day).nlargest(6, "attempts")
            h = self._hist(frame, day)
            rows = []
            for _, r in d.iterrows():
                own = h[h[col] == r[col]]
                med = float(own["success_rate"].median()) if len(own) else None
                z = zscore(r["success_rate"], own["success_rate"]) if len(own) \
                    else 0.0
                flag = "⚠ outlier" if abs(z) >= 2.0 else "normal"
                rows.append([r[col], f"{r['attempts']:,.0f}",
                             f"{r['success_rate']:.2f}%",
                             f"{med:.2f}%" if med else "—",
                             _inr(r["value_inr"]), flag])
            out.append(f"### {title}\n\n" + _table(
                [col.replace("payer_", "").title(), "Attempts", "Success",
                 "Own 28d median", "Settled value", "Status"], rows))
        return "## Rail performance\n\n" + "\n\n".join(out)

    def _demand(self, day: str, cur) -> str:
        cat = self._day_rows(self.f.by_category, day).nlargest(6, "attempts")
        crows = [[r["mcc_category"], f"{r['attempts']:,.0f}",
                  f"{r['success_rate']:.2f}%", _inr(r["value_inr"])]
                 for _, r in cat.iterrows()]
        reg = self._day_rows(self.f.by_region, day).nlargest(6, "attempts")
        rrows = [[r["region"], f"{r['attempts']:,.0f}",
                  f"{r['attempts'] / cur['attempts'] * 100:.1f}%",
                  f"{r['success_rate']:.2f}%", _inr(r["value_inr"])]
                 for _, r in reg.iterrows()]
        mer = self._day_rows(self.f.by_merchant, day).nlargest(8, "value_inr")
        mrows = [[r["merchant"], r.get("merchant_tier") or "—",
                  r.get("mcc_category") or "—", f"{r['attempts']:,.0f}",
                  f"{r['success_rate']:.2f}%", _inr(r["value_inr"])]
                 for _, r in mer.iterrows()]
        return ("## Where the demand came from\n\n"
                "### Merchant categories\n\n"
                + _table(["Category", "Attempts", "Success", "Settled value"],
                         crows)
                + "\n\n### Geography\n\n"
                + _table(["Region", "Attempts", "Share", "Success",
                          "Settled value"], rrows)
                + "\n\n### Largest merchants by settled value\n\n"
                + _table(["Merchant", "Tier", "Category", "Attempts",
                          "Success", "Settled value"], mrows))

    def _failures(self, day: str, cur, hist, obs) -> str:
        fd = self._day_rows(self.f.failures, day).nlargest(8, "n")
        fh = self._hist(self.f.failures, day)
        rows = []
        for _, r in fd.iterrows():
            own = fh[fh["failure_code"] == r["failure_code"]]
            med = float(own["rate_pct"].median()) if len(own) else None
            rate = r["n"] / cur["attempts"] * 100
            rows.append([r["failure_code"], r["failure_reason"],
                         r["failure_bucket"], r["failure_owner"],
                         f"{r['n']:,.0f}", f"{rate:.3f}%",
                         f"{med:.3f}%" if med is not None else "—"])
        total_f = cur["attempts"] - cur["successes"] - cur["pending"]
        split = (f"Of {total_f:,.0f} declined attempts, "
                 f"{cur['f_business']:,.0f} were business declines "
                 f"({cur['business_pct']:.3f}% of attempts — balances, PINs "
                 f"and limits), {cur['f_technical']:,.0f} technical "
                 f"({cur['technical_pct']:.3f}%), {cur['f_timeout']:,.0f} "
                 f"timeouts ({cur['timeout_pct']:.3f}%) and "
                 f"{cur['f_risk']:,.0f} risk declines "
                 f"({cur['risk_pct']:.3f}%).")
        rec = cur.get("retry_recovery_pct")
        retry = ""
        if cur["retries"] > 0 and rec is not None and not pd.isna(rec):
            retry = (f"\n\n{cur['retries']:,.0f} attempts were "
                     f"re-presentations of an earlier failure "
                     f"({cur['retry_share']:.2f}% of the day); "
                     f"{rec:.1f}% of them succeeded.")
        notes = [o.text for o in obs if o.section == "failures"]
        note_block = ("\n\n" + "\n".join(f"- {t}" for t in notes)) if notes \
            else ""
        return ("## Failure analysis\n\n" + split + retry + note_block
                + "\n\n" + _table(
                    ["Code", "Reason", "Bucket", "Owner", "Count",
                     "Rate today", "28d median rate"], rows))

    def _money_back(self, cur, hist) -> str:
        rows = [
            ["Refunds", f"{cur['refunds']:,.0f}",
             f"{hist['refunds'].median():,.0f}" if len(hist) else "—"],
            ["Auto-reversals", f"{cur['reversals']:,.0f}",
             f"{hist['reversals'].median():,.0f}" if len(hist) else "—"],
            ["Disputes / chargebacks", f"{cur['chargebacks']:,.0f}",
             f"{hist['chargebacks'].median():,.0f}" if len(hist) else "—"],
            ["Value returned", _inr(cur["adj_value_inr"]),
             _inr(hist["adj_value_inr"].median()) if len(hist) else "—"],
        ]
        return ("## Refunds, reversals and disputes\n\n"
                + _table(["Flow", "Today", "28d median"], rows))

    def _customers(self, day: str, cur, hist) -> str:
        seg = self._day_rows(self.f.by_segment, day).nlargest(8, "attempts")
        rows = [[r["customer_segment"], f"{r['customers']:,.0f}",
                 f"{r['attempts']:,.0f}",
                 f"{r['attempts'] / max(r['customers'], 1):.2f}",
                 f"{r['success_rate']:.2f}%",
                 _inr(r["value_inr"] / max(r["attempts"], 1))]
                for _, r in seg.iterrows()]
        base = float(hist["customers"].median()) if len(hist) else None
        intro = (f"{cur['customers']:,.0f} distinct customers transacted "
                 f"({_delta(cur['customers'], base)} on the 28-day median) "
                 f"at {cur['attempts'] / max(cur['customers'], 1):.2f} "
                 f"attempts each.")
        return ("## Customer behaviour\n\n" + intro + "\n\n"
                + _table(["Segment", "Active customers", "Attempts",
                          "Attempts / customer", "Success", "Avg ticket"],
                         rows))

    def _incidents(self, obs) -> str:
        inc = [o for o in obs if o.section == "incidents"]
        if not inc:
            return ("## Operational events\n\nNo incident, campaign or "
                    "maintenance window overlapped this date in the "
                    "operational record.")
        return ("## Operational events\n\n"
                + "\n".join(f"- {o.text}" for o in inc))

    def _risks_opportunities(self, obs) -> str:
        # Incidents are already enumerated above with their full narrative.
        risks = [o for o in obs
                 if o.kind == "risk" and o.section != "incidents"][:5]
        opps = [o for o in obs if o.kind == "opportunity"][:4]
        out = "## Risks and opportunities\n"
        out += "\n### Risks\n\n" + ("\n".join(f"- {o.text}" for o in risks)
                                    if risks else
                                    "- None material today. No entity, code "
                                    "or flow breached its own 28-day band.")
        out += "\n\n### Opportunities\n\n" + (
            "\n".join(f"- {o.text}" for o in opps) if opps else
            "- No growth signal cleared the threshold today; the compounding "
            "products are tracking their existing curves.")
        return out

    def _executive(self, cur, hist, obs, dt: date) -> str:
        """The paragraph a business head actually reads.

        It is assembled from what the detectors found, so on a quiet day it
        says the day was quiet — which is the honest thing to say and the
        thing a template can never bring itself to do.
        """
        sr_med = float(hist["success_rate"].median()) if len(hist) else \
            cur["success_rate"]
        gap = cur["success_rate"] - sr_med
        material = [o for o in obs if o.materiality >= 3.0]
        # Only a *reliability* event makes it an incident day. A merchant
        # churn wave is a Sev-2 to the business and still not an outage.
        sev = [o for o in obs if o.section == "incidents"
               and o.evidence.get("severity") in ("Sev-1", "Sev-2")
               and o.evidence.get("kind") in RELIABILITY_KINDS]

        if sev:
            ids = ", ".join(o.evidence["event_id"] for o in sev[:2])
            head = (f"{dt:%d %B} was an incident day: {ids} "
                    f"{'were' if len(sev) > 1 else 'was'} live and the rail "
                    f"closed at {cur['success_rate']:.2f}% success against a "
                    f"{sr_med:.2f}% baseline.")
            act = ("Priority is confirming the fix held rather than reading "
                   "the day's demand signal, which the incident contaminates.")
        elif abs(gap) >= 0.4:
            head = (f"Reliability, not demand, is the story of {dt:%d %B}: "
                    f"success came in {abs(gap):.2f}pp "
                    f"{'below' if gap < 0 else 'above'} baseline at "
                    f"{cur['success_rate']:.2f}% on "
                    f"{cur['attempts']:,.0f} attempts.")
            act = ("The decline table below attributes it by code and owner; "
                   "that attribution is where the next action sits."
                   if gap < 0 else
                   "Worth understanding what went right — a sustained gain "
                   "here is worth more than a volume campaign.")
        elif material:
            lead = next((o for o in material if o.section != "incidents"),
                        material[0])
            head = (f"{dt:%d %B} ran on trend at "
                    f"{cur['success_rate']:.2f}% success and "
                    f"{_inr(cur['value_inr'])} settled. The movement worth "
                    f"carrying forward is in {_SECTION_NOUN.get(lead.section, lead.section)}: "
                    f"{lead.text[0].lower() + lead.text[1:]}")
            others = len(material) - 1
            act = (f"{others} further movement{'s' if others != 1 else ''} "
                   f"cleared the materiality threshold and "
                   f"{'are' if others != 1 else 'is'} listed above."
                   if others else
                   "Nothing else in the day cleared the materiality "
                   "threshold.")
        else:
            head = (f"{dt:%d %B} was an unremarkable day, and that is the "
                    f"finding: {cur['attempts']:,.0f} attempts, "
                    f"{cur['success_rate']:.2f}% success, "
                    f"{_inr(cur['value_inr'])} settled, every dimension "
                    f"inside its own 28-day band.")
            act = ("Days like this are the ones to spend on capacity and "
                   "roadmap work, because nothing is competing for the "
                   "operations bandwidth.")
        return f"## Executive observation\n\n{head} {act}"

    def _evidence(self, day: str, obs, cur) -> str:
        """Traceability — the point being that a reader can re-derive this."""
        lines = [
            f"- Corpus window queried: `{day}` plus the {TRAILING} preceding "
            f"days, over `enterprise_data/warehouse/transactions/`.",
            f"- Day totals: attempts={cur['attempts']:,.0f}, "
            f"successes={cur['successes']:,.0f}, "
            f"failed={cur['failures']:,.0f}, pending={cur['pending']:,.0f}, "
            f"settled_value_inr={cur['value_inr']:,.2f}.",
            "- Every rate is computed as a share of attempts on this date; "
            "every '28d median' is that entity's own median over the "
            "preceding 28 days, excluding today.",
        ]
        for o in obs[:10]:
            if o.evidence:
                lines.append(f"- {o.section}: {o.evidence_line()}")
        return ("## Evidence\n\n"
                "Every figure in this report is a SQL aggregate over raw "
                "transaction rows; none of it is read from a precomputed "
                "summary.\n\n" + "\n".join(lines))

    # ------------------------------------------------------------- writing
    def write_all(self, out_dir: Path, *, progress=None) -> list[Path]:
        out_dir = Path(out_dir)
        written: list[Path] = []
        dates = self.f.dates
        for i, day in enumerate(dates, start=1):
            folder = out_dir / f"day_{i:02d}" / "reports"
            folder.mkdir(parents=True, exist_ok=True)
            path = folder / f"RPT-D{i:02d}-daily.md"
            path.write_text(self.document(day, i, len(dates)),
                            encoding="utf-8")
            written.append(path)
            if progress and (i % 25 == 0 or i == len(dates)):
                progress(i, len(dates))
        return written

    def document(self, day: str, index: int, total: int) -> str:
        dt = date.fromisoformat(day)
        rid = f"RPT-D{index:02d}-DAILY"
        stamp = datetime.combine(dt, datetime.min.time()).replace(hour=18,
                                                                  minute=30)
        header = (f"---\n"
                  f"id: {rid}\n"
                  f"type: report\n"
                  f"organization: {ORG_NAME}\n"
                  f"department: {DEPARTMENT}\n"
                  f"timestamp: {stamp.isoformat()}\n"
                  f"source: enterprise_data/warehouse (raw transactions)\n"
                  f"---\n\n")
        title = (f"# {DEPARTMENT} — Daily Operations Report "
                 f"({dt:%A, %d %b %Y})")
        meta = (f"**Report ID:** {rid} · **Day {index} of {total}** · "
                f"**Derived from:** {self.f.daily[self.f.daily['txn_date'] == day].iloc[0]['attempts']:,.0f} "
                f"transaction rows queried live from the warehouse")
        refs = ["enterprise_data/warehouse/transactions",
                f"RPT-D{max(1, index - 1):02d}-DAILY",
                "enterprise_data/warehouse/reference/incidents.parquet"]
        body = self.render(day)
        return (f"{header}{title}\n\n{meta}\n\n{body}\n\n"
                f"Refs: {', '.join(refs)}\n")


def main() -> None:  # pragma: no cover — CLI
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=None, help="enterprise_data directory")
    ap.add_argument("--day", type=int, default=None,
                    help="render a single 1-based day to stdout")
    args = ap.parse_args()

    base = Path(args.root) if args.root else (
        Path(__file__).resolve().parents[4] / "enterprise_data")
    wh = get_warehouse(base / "warehouse")
    if not wh.available:
        raise SystemExit(f"no warehouse corpus under {base / 'warehouse'}")

    print("loading frames from the corpus ...", flush=True)
    b = DailyReportBuilder(wh)
    if args.day:
        day = b.f.dates[args.day - 1]
        print(b.document(day, args.day, len(b.f.dates)))
        return

    def show(done: int, total: int) -> None:
        print(f"  {done}/{total} reports", flush=True)

    paths = b.write_all(base, progress=show)
    print(f"wrote {len(paths)} corpus-derived daily reports")


if __name__ == "__main__":  # pragma: no cover
    main()

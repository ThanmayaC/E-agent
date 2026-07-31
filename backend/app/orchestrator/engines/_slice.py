"""Translate a classified question into a warehouse slice.

The orchestrator speaks in the classifier's vocabulary — a time range, KPI
hints, named entities. The warehouse speaks in :class:`Filters` and target
columns. This is the one place that translation happens, so the Analytics,
Forecast and ML engines all slice the corpus identically for the same question
and can never disagree about what "UPI success rate last month" means.
"""
from __future__ import annotations

from datetime import date, timedelta

from app.warehouse.filters import Filters

# Classifier canonical KPI name → warehouse daily target column.
KPI_TO_TARGET: dict[str, str] = {
    "Success Rate (%)": "success_rate",
    "Technical Declines (%)": "technical_decline_pct",
    "Business Declines (%)": "business_decline_pct",
    "Transaction Volume (Mn)": "attempts",
    "Transaction Value (₹ Cr)": "value_inr",
    "Active Customers (Mn)": "active_customers",
    "Avg Latency (ms)": "p95_latency_ms",
    "Retention (%)": "active_customers",
    "Feature Adoption (%)": "active_merchants",
}

_RELATIVE_SPAN = {"last_ndays": None, "next_ndays": None, "last_week": 7,
                  "this_week": 7, "last_month": 30, "this_month": 30,
                  "next_month": 30, "last_quarter": 91, "this_quarter": 91,
                  "last_nweeks": None, "last_6months": 182}


def pick_target(request) -> str:
    """The metric the question is about; attempts (volume) is the default."""
    for hint in getattr(request, "kpi_hints", ()) or ():
        if hint in KPI_TO_TARGET:
            return KPI_TO_TARGET[hint]
    return "attempts"


def resolve_window(time_range: dict | None, corpus: tuple[str, str]) -> dict:
    """Concrete ISO bounds clamped to the corpus. A forward window has no data
    yet, so it maps to the trailing actuals that frame a forecast, relabelled so
    no answer claims to have read the future."""
    first, last = corpus
    if not first or not last:
        return {"start": first, "end": last, "label": "the available history",
                "forward": False}
    if not time_range:
        return _relative("last_ndays", 30, first, last, "the last 30 days")

    if time_range.get("kind") == "month":
        return _whole_month(time_range, first, last)

    if time_range.get("kind") == "explicit":
        if time_range.get("start_iso"):
            return {"start": max(first, time_range["start_iso"]),
                    "end": min(last, time_range["end_iso"]),
                    "label": time_range.get("label", "the named period"),
                    "forward": False}
        start = _resolve_md(time_range.get("start_md"), first, last, "start")
        end = (_resolve_md(time_range.get("end_md"), first, last, "end")
               if time_range.get("end_md") else last)
        if start and end and start > end:
            start, end = end, start
        return {"start": max(first, start or first),
                "end": min(last, end or last),
                "label": time_range.get("label", "the named period"),
                "forward": False}

    return _relative(time_range.get("token", "last_ndays"),
                     time_range.get("n"), first, last,
                     time_range.get("label"))


def _relative(token: str, n, first: str, last: str, label) -> dict:
    forward = token in ("next_month", "next_ndays")
    if token in ("last_ndays", "next_ndays"):
        days = n or 30
    elif token == "last_nweeks":
        days = (n or 4) * 7
    else:
        days = _RELATIVE_SPAN.get(token, 30) or 30
    try:
        e = date.fromisoformat(last)
        start = max(first, (e - timedelta(days=max(0, days - 1))).isoformat())
    except (ValueError, TypeError):
        start = first
    shown = (f"recent actuals (last {days} days)" if forward
             else label or f"the last {days} days")
    return {"start": start, "end": last, "label": shown, "forward": forward}


def _whole_month(tr: dict, first: str, last: str) -> dict:
    """The full calendar month a question named, clamped to the corpus.

    A month with no year resolves to the most recent occurrence the corpus
    actually covers, so "in May" means the May there is data for rather than a
    year the platform has never seen.
    """
    month = int(tr.get("month") or 1)
    year = tr.get("year")
    if not year:
        year = int(last[:4])
        # Walk back a year if that month has not happened yet in the corpus.
        if date(year, month, 1).isoformat() > last:
            year -= 1
    start = date(year, month, 1)
    end = date(year, month, _days_in(year, month))
    lo, hi = max(first, start.isoformat()), min(last, end.isoformat())
    label = tr.get("label") or start.strftime("%B %Y")
    if lo > hi:
        # The named month lies entirely outside the corpus. Say so rather than
        # silently answering about some other period.
        return {"start": first, "end": last,
                "label": f"{label} (outside the available history "
                         f"{first}..{last})",
                "forward": False, "out_of_range": True}
    partial = lo > start.isoformat() or hi < end.isoformat()
    return {"start": lo, "end": hi,
            "label": f"{label} (partial: {lo}..{hi})" if partial else label,
            "forward": False}


def _resolve_md(md, first: str, last: str, which: str) -> str:
    if not md:
        return ""
    month, day = md
    # Match the (month, day) against the years the corpus spans.
    for y in range(int(last[:4]), int(first[:4]) - 1, -1):
        try:
            cand = date(y, month, min(day, 28)).isoformat()
        except ValueError:
            continue
        if first <= cand <= last:
            return date(y, month, min(day, _days_in(y, month))).isoformat()
    return first if which == "start" else last


def _days_in(y: int, m: int) -> int:
    if m == 12:
        return 31
    return (date(y, m + 1, 1) - timedelta(days=1)).day


def entity_filters(request, analytics) -> dict:
    """Map named entities to Filters fields, resolving product names/families to
    the codes the corpus stores. Only entities the warehouse actually knows are
    applied — an unknown name is dropped, never guessed."""
    out: dict = {}
    ents = getattr(request, "entities", {}) or {}
    banks = ents.get("bank") or []
    psps = ents.get("psp") or []
    merchants = ents.get("merchant") or []
    products = ents.get("product") or []
    if banks:
        out["bank"] = _match_names(analytics, "payer_bank", banks)
    if psps:
        out["psp"] = _match_names(analytics, "payer_psp", psps)
    if merchants:
        m = _match_names(analytics, "merchant_name", merchants)
        if m:
            out["merchant"] = None  # name filtering handled by caller if needed
    if products:
        codes = match_products(analytics, products)
        # A single code stays a scalar so `describe()` and existing consumers
        # read the same as before; two or more become a list, which
        # `Filters.where()` renders as `IN (...)`.
        if codes:
            out["product"] = codes[0] if len(codes) == 1 else codes
    return {k: v for k, v in out.items() if v}


def _match_names(analytics, col: str, wanted: list[str]) -> list[str]:
    try:
        rows = analytics.wh.query(
            f"SELECT DISTINCT {col} AS v FROM txn WHERE {col} IS NOT NULL",
            label=f"slice.match.{col}")
    except Exception:  # noqa: BLE001
        return []
    known = {str(r["v"]).lower(): str(r["v"]) for r in rows}
    hit = []
    for w in wanted:
        v = known.get(str(w).lower())
        if v and v not in hit:
            hit.append(v)
    return hit


def match_products(analytics, wanted: list[str]) -> list[str]:
    """Every product the question named, in the order it named them.

    This used to return on the first match. "Compare UPI AutoPay and UPI Lite"
    therefore resolved to AutoPay alone and the platform answered a question
    about one product as though it were the question asked about two — with no
    warning that half the request had been dropped.
    """
    try:
        prods = analytics.products()
    except Exception:  # noqa: BLE001
        return []
    codes: list[str] = []
    for w in wanted:
        wl = str(w).lower().strip()
        for p in prods:
            name = str(p.get("product_name", "")).lower()
            code = str(p.get("product_code", "")).lower()
            family = str(p.get("product_family", "")).lower()
            # Exact match first, then a contained match so "upi lite" finds
            # "UPI Lite" without also swallowing "UPI Lite Auto Top-Up".
            if wl in (name, code, family):
                got = p.get("product_code")
                if got and got not in codes:
                    codes.append(got)
                break
        else:
            for p in prods:
                if wl and wl in str(p.get("product_name", "")).lower():
                    got = p.get("product_code")
                    if got and got not in codes:
                        codes.append(got)
                    break
    return codes


def build_filters(request, analytics) -> tuple[Filters, dict]:
    """The slice a question resolves to, and the window metadata for the trace."""
    corpus = analytics.corpus_window()
    window = resolve_window(getattr(request, "time_range", None), corpus)
    kw = {"start": window["start"], "end": window["end"]}
    kw.update(entity_filters(request, analytics))
    return Filters(**{k: v for k, v in kw.items() if v}), window


def build_training_filters(request, analytics) -> tuple[Filters, dict]:
    """The slice for a model that must *train* on history: entity filters apply
    (forecast UPI, not everything), but the window is the full corpus unless the
    question explicitly names a past window to restrict to. A forward window
    ("next 14 days") is a horizon, not a training window — it must never shrink
    the data the model learns from."""
    corpus = analytics.corpus_window()
    tr = getattr(request, "time_range", None)
    explicit_past = bool(tr and tr.get("kind") == "explicit")
    if explicit_past:
        window = resolve_window(tr, corpus)
        kw = {"start": window["start"], "end": window["end"]}
    else:
        window = {"start": corpus[0], "end": corpus[1],
                  "label": "the full transaction history", "forward": False}
        kw = {"start": corpus[0], "end": corpus[1]}
    kw.update(entity_filters(request, analytics))
    return Filters(**{k: v for k, v in kw.items() if v}), window


def warehouse_entity_vocab(analytics) -> dict[str, list[str]]:
    """Entity vocabulary read straight from the corpus, so every name the
    classifier recognises is one the warehouse can actually filter on."""
    vocab = {"bank": [], "psp": [], "merchant": [], "product": []}
    if not analytics.available:
        return vocab
    try:
        vocab["bank"] = [str(r["v"]) for r in analytics.wh.query(
            "SELECT DISTINCT payer_bank AS v FROM txn WHERE payer_bank IS NOT NULL")]
        vocab["psp"] = [str(r["v"]) for r in analytics.wh.query(
            "SELECT DISTINCT payer_psp AS v FROM txn WHERE payer_psp IS NOT NULL")]
        prods = analytics.products()
        names = []
        for p in prods:
            names += [p.get("product_name"), p.get("product_code")]
        vocab["product"] = [str(n) for n in names if n]
        vocab["merchant"] = [str(r["v"]) for r in analytics.wh.query(
            "SELECT merchant_name AS v FROM ("
            "  SELECT merchant_name, count(*) c FROM txn "
            "  WHERE merchant_name IS NOT NULL GROUP BY merchant_name "
            "  ORDER BY c DESC LIMIT 80)")]
    except Exception:  # noqa: BLE001
        pass
    return vocab

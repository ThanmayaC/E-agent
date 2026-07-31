"""Analytics Engine — KPIs computed from raw transactions, not documents.

A question about a metric over time — "show UPI trends July 1-20", "how did the
success rate move last month", "compare technical declines week on week" — is
answered by slicing the raw transaction corpus over the window the question
names and deriving the series with SQL. It is never sent to RAG, which is why
the old pipeline answered "no evidence found": a trend is not a document, it is a
computation over millions of payment rows.

The engine computes nothing the platform does not already hold as transactions.
Every figure it emits carries its numbers inside an evidence ``text`` field so
the copilot's validator grounds it, and its ``detail`` reports the real SQL the
warehouse ran, the window it resolved and the rows it scanned — genuine
observability, not a mock.
"""
from __future__ import annotations

from app.orchestrator.base import Engine, EngineRequest, EngineResult
from app.orchestrator.engines import _slice
from app.warehouse.analytics import KPI_META, kpi_label


def _num(v, default: float = 0.0) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return default


class AnalyticsEngine(Engine):
    key = "analytics"
    label = "Analytics Engine"
    categories = ("analytics", "dashboard")

    def __init__(self, analytics=None):
        # TransactionAnalytics over the raw-transaction warehouse.
        self._a = analytics

    def available(self) -> bool:
        return bool(self._a is not None and self._a.available)

    def can_handle(self, request: EngineRequest) -> bool:
        if super().can_handle(request):
            return True
        return bool(request.time_range or request.kpi_hints
                    or request.entities)

    # ------------------------------------------------------------ run
    def run(self, request: EngineRequest) -> EngineResult:
        res = self._result()
        if not self.available():
            res.status = "unavailable"
            res.note = "transaction warehouse holds no data"
            res.ran = False
            return res

        filters, window = _slice.build_filters(request, self._a)
        target = _slice.pick_target(request)
        series = self._a.daily_series(filters)
        where, params = filters.where()
        res.detail = {
            "source": "raw_transactions",
            "window": {"start": window["start"], "end": window["end"],
                       "label": window["label"]},
            "slice": filters.describe(),
            "rows_scanned": len(series),
            "primary_metric": target,
            "sql": (f"SELECT txn_date, {target}, success_rate, attempts, "
                    f"value_inr FROM attempts WHERE {where} "
                    f"GROUP BY txn_date ORDER BY txn_date"),
            "sql_params": params,
        }
        if not series:
            res.status = "empty"
            res.note = f"no transactions in {window['label']} for this slice"
            return res

        # Anchor fact: the window, with settled volume and value.
        total_attempts = sum(_num(r.get("attempts")) for r in series)
        total_value = sum(_num(r.get("value_inr")) for r in series)
        res.add("analytics_window", f"analytics:window:{window['start']}",
                f"{window['label']}: {len(series)} day(s) of transactions",
                {"text": (f"Analytics window {window['label']} "
                          f"({window['start']} to {window['end']}) covers "
                          f"{len(series)} day(s), {int(total_attempts):,} "
                          f"transaction attempts and ₹{int(total_value):,} "
                          f"settled value for slice {filters.describe() or 'all'}."),
                 "start": window["start"], "end": window["end"],
                 "days": len(series)})

        # The KPIs the question named (or the headline three), each as a trend.
        for tgt in self._pick_targets(request, target):
            self._trend_evidence(res, tgt, series, window, filters,
                                 asked_as=_asked_as(request, tgt))

        # "Compare A and B" is not one blended series — it is one series each,
        # side by side. Without this the engine filtered to both products at
        # once and emitted a single merged trend, which cannot answer the
        # question however good the model reading it is.
        self._comparison_evidence(res, request, target, filters, window)

        # "Why did X change" needs more than the aggregate trend — it needs
        # which entities drove it. Root-cause is what "explanation"/"analysis"
        # questions are actually asking for.
        if request.intent in ("explanation", "analysis"):
            self._root_cause_movers(res, target, filters, window,
                                    asked_as=_asked_as(request, target))
        return res

    # Entity kinds a question can compare across, mapped to the Filters field
    # that isolates one of them.
    _COMPARABLE = (("product", "product"), ("bank", "bank"), ("psp", "psp"))

    def _comparison_evidence(self, res: EngineResult, request: EngineRequest,
                             target: str, filters, window: dict) -> None:
        """One metric block per named entity, plus the head-to-head verdict.

        Emitted whenever a question names two or more entities of the same kind
        — not only on `comparison` intent, because "how did AutoPay and Lite do
        in May" classifies as a question and still needs both sides.
        """
        for ent_kind, field in self._COMPARABLE:
            named = (getattr(request, "entities", {}) or {}).get(ent_kind) or []
            if len(named) < 2:
                continue
            resolved = getattr(filters, field, None)
            values = list(resolved) if isinstance(resolved, (list, tuple)) \
                else ([resolved] if resolved else [])
            if len(values) < 2:
                continue

            sides = []
            for value in values:
                one = filters.with_(**{field: value})
                try:
                    summary = self._a.summary(one)
                except Exception:  # noqa: BLE001 - one bad side must not sink the answer
                    continue
                cur = (summary or {}).get("current") or summary or {}
                sides.append({
                    "entity": value,
                    "attempts": _num(cur.get("attempts")),
                    "value_inr": _num(cur.get("value_inr")),
                    "success_rate": _num(cur.get("success_rate")),
                    "avg_ticket_inr": _num(cur.get("avg_ticket_inr")),
                    "active_customers": _num(cur.get("active_customers")),
                })
            if len(sides) < 2:
                continue

            for s in sides:
                res.add(
                    "analytics_comparison_side",
                    f"analytics:compare:{ent_kind}:{s['entity']}:{window['start']}",
                    f"{s['entity']} over {window['label']}",
                    {"name": s["entity"], "dimension": ent_kind,
                     "window": window["label"], **s,
                     "text": (
                         f"{s['entity']} over {window['label']} "
                         f"({window['start']} to {window['end']}): "
                         f"{int(s['attempts']):,} attempts, "
                         f"₹{int(s['value_inr']):,} settled value, "
                         f"{round(s['success_rate'], 2)}% success rate, "
                         f"₹{round(s['avg_ticket_inr'], 2)} average ticket, "
                         f"{int(s['active_customers']):,} active customers.")})

            self._comparison_verdict(res, sides, ent_kind, target, window)
            return  # one comparison dimension per answer is enough

    def _comparison_verdict(self, res: EngineResult, sides: list[dict],
                            ent_kind: str, target: str, window: dict) -> None:
        """The explicit head-to-head, so the answer does not have to do the
        arithmetic itself — and the validator can ground the ratio."""
        metric = target if target in sides[0] else "attempts"
        ranked = sorted(sides, key=lambda s: s.get(metric) or 0.0, reverse=True)
        top, bottom = ranked[0], ranked[-1]
        label = KPI_META.get(metric, {}).get("label", metric)
        lo = bottom.get(metric) or 0.0
        ratio = ((top.get(metric) or 0.0) / lo) if lo else None
        gap = (top.get(metric) or 0.0) - lo

        lines = [f"{s['entity']}: {label} {round(s.get(metric) or 0.0, 2)}, "
                 f"success rate {round(s['success_rate'], 2)}%, "
                 f"average ticket ₹{round(s['avg_ticket_inr'], 2)}"
                 for s in ranked]
        verdict = (f"{top['entity']} leads {bottom['entity']} on {label} over "
                   f"{window['label']} by {round(gap, 2)}"
                   + (f" ({round(ratio, 2)}x)" if ratio else "") + ".")
        best_sr = max(sides, key=lambda s: s["success_rate"])
        res.add(
            "analytics_comparison",
            f"analytics:compare:{ent_kind}:{window['start']}",
            f"Head-to-head across {len(sides)} {ent_kind}(s) over {window['label']}",
            {"dimension": ent_kind, "metric": metric, "window": window["label"],
             "entities": [s["entity"] for s in ranked], "sides": ranked,
             "leader": top["entity"], "laggard": bottom["entity"],
             "gap": round(gap, 2), "ratio": round(ratio, 2) if ratio else None,
             "text": (f"Comparison over {window['label']} "
                      f"({window['start']} to {window['end']}). "
                      + " | ".join(lines) + f" {verdict} "
                      f"Highest success rate: {best_sr['entity']} at "
                      f"{round(best_sr['success_rate'], 2)}%.")})

    _ROOT_CAUSE_DIMS = ("bank", "psp", "product", "mcc_category")

    def _root_cause_movers(self, res: EngineResult, target: str,
                           filters, window: dict,
                           asked_as: str | None = None) -> None:
        """Which entities in each dimension moved the target the most versus
        the equally-long prior period — the breakdown that actually answers
        "why", as opposed to the aggregate trend alone."""
        meta = KPI_META.get(target, {})
        # Name the metric the way the question did, or the model will not
        # recognise this breakdown as an answer to it.
        label = kpi_label(target, asked_as) or target.replace("_", " ")
        unit = meta.get("unit", "")
        growth_key = "value_growth_pct" if target == "value_inr" else "growth_pct"

        movers = []
        for dim in self._ROOT_CAUSE_DIMS:
            try:
                rows = self._a.by_dimension(filters, dim, limit=15,
                                            with_growth=True)
            except ValueError:
                continue
            for r in rows:
                g = r.get(growth_key)
                share = r.get("share_pct")
                if g is None or share is None:
                    continue
                # Percentage-point contribution to the overall change —
                # a small entity swinging wildly matters less than a large
                # one moving modestly.
                impact = g * share / 100.0
                movers.append({"dimension": dim, "name": r["name"],
                              "growth_pct": g, "share_pct": share,
                              "impact": round(impact, 4)})
        if not movers:
            return

        movers.sort(key=lambda m: m["impact"])
        decliners = [m for m in movers if m["impact"] < 0][:4]
        growers = sorted([m for m in movers if m["impact"] > 0],
                         key=lambda m: -m["impact"])[:2]
        top = decliners + growers
        if not top:
            return

        lines = []
        for m in top:
            verb = "fell" if m["growth_pct"] < 0 else "rose"
            lines.append(
                f"{m['name']} ({m['dimension']}) {verb} {abs(m['growth_pct'])}% "
                f"({m['share_pct']}% of current volume, ~{m['impact']:+.2f}pp "
                f"of the total move)")
        res.add(
            "analytics_root_cause",
            f"analytics:rootcause:{target}:{window['start']}",
            f"Top contributors to the {label} change over {window['label']}",
            {"name": f"{label} root cause", "kpi": target,
             "movers": top,
             "text": (f"Root-cause breakdown of {label}{unit and f' ({unit})'} "
                      f"over {window['label']}: the entities that moved it "
                      f"most were " + "; ".join(lines) + ".")})

    def _pick_targets(self, request: EngineRequest, primary: str) -> list[str]:
        targets = []
        for hint in request.kpi_hints or ():
            t = _slice.KPI_TO_TARGET.get(hint)
            if t and t not in targets:
                targets.append(t)
        if not targets:
            targets = ["attempts", "success_rate", "value_inr"]
        elif primary not in targets:
            targets.insert(0, primary)
        return targets

    def _trend_evidence(self, res: EngineResult, target: str,
                        series: list[dict], window: dict, filters,
                        asked_as: str | None = None) -> None:
        meta = KPI_META.get(target, {})
        pts = [(str(r.get("date")), _num(r.get(target)))
               for r in series if r.get(target) is not None]
        if not pts:
            return
        values = [v for _, v in pts]
        first, last = values[0], values[-1]
        lo, hi = min(values), max(values)
        mean = sum(values) / len(values)
        delta = last - first
        pct = (delta / first * 100) if first else 0.0
        higher_good = meta.get("higher", True)
        direction = ("flat" if abs(delta) < 1e-9 * max(1, abs(first))
                     else "up" if delta > 0 else "down")
        improving = (direction == "flat"
                     or (higher_good and direction == "up")
                     or (not higher_good and direction == "down"))
        verdict = ("steady" if direction == "flat"
                   else "improving" if improving else "worsening")
        unit = meta.get("unit", "")
        label = kpi_label(target, asked_as) or target.replace("_", " ")
        res.add(
            "analytics_kpi", f"analytics:{target}:{window['start']}",
            f"{label} {verdict} over {window['label']}: "
            f"{round(first, 3)}→{round(last, 3)}{unit}",
            {"name": label, "unit": unit, "kpi": target,
             "first": round(first, 4), "last": round(last, 4),
             "min": round(lo, 4), "max": round(hi, 4), "mean": round(mean, 4),
             "delta": round(delta, 4), "pct_change": round(pct, 2),
             "direction": direction, "verdict": verdict, "points": len(values),
             "series": [{"date": d, "value": round(v, 3)} for d, v in pts],
             "text": (f"{label} over {window['label']} for slice "
                      f"{filters.describe() or 'the whole platform'}: started at "
                      f"{round(first, 3)}{unit}, ended at {round(last, 3)}{unit} "
                      f"(change {round(delta, 3)}{unit}, {round(pct, 1)}%). "
                      f"Range {round(lo, 3)}–{round(hi, 3)}{unit}, average "
                      f"{round(mean, 3)}{unit} across {len(values)} day(s). "
                      f"Trend is {direction} and {verdict}.")})


def _asked_as(request: EngineRequest, target: str) -> str | None:
    """The phrase the question used for ``target``, if it named one.

    The classifier reports KPI hints as its own canonical names
    ("Transaction Value (₹ Cr)"). Only the hint that actually resolves to this
    target is returned, so a multi-KPI question cannot label one metric's
    evidence with another metric's name.
    """
    for hint in request.kpi_hints or ():
        if _slice.KPI_TO_TARGET.get(hint) == target:
            return hint
    return None

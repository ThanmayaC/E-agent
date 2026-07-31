"""Query Classification — from intent to the engines a question needs.

The copilot's ``IntentClassifier`` answers *what shape* a request is (a
question, an explanation, a forecast). This layer answers the next question:
*which reasoning engines must run to serve it* — Analytics, Knowledge, Machine
Learning, Forecast, Recommendation, Report, or Dashboard — and it detects the
two things that decide how the Analytics engine behaves: a **time range**
("July 1 to July 20", "last 30 days") and the **KPIs** a question names.

A request maps to one *or more* categories. A single category is a clean route;
several is a **hybrid** query, and hybrids are the norm for real executive
questions — "why did transaction value increase?" is analytics (the numbers) +
forecast (the trajectory) + knowledge (the reason) at once. Classifying that as
"RAG" and nothing else is exactly the bug this platform is fixing.

Classification is deterministic — scored keyword and shape evidence, no LLM
call — for the same three reasons intent detection is: routing an answer wrong
is worse than answering plainly, it must work with no provider configured, and
it runs on every message.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

# The engine categories. Closed by design: a category with no engine behind it
# is not a category.
CATEGORIES = ("analytics", "knowledge", "forecast", "ml", "recommendation",
              "report", "dashboard")

# Every intent seeds the categories that answer it. Analytics and Knowledge
# both appear widely on purpose — most enterprise questions want a number *and*
# the story behind it.
INTENT_CATEGORIES: dict[str, tuple[str, ...]] = {
    "question": ("analytics", "knowledge"),
    "analysis": ("analytics", "knowledge", "ml"),
    "explanation": ("analytics", "knowledge", "ml"),
    "comparison": ("analytics",),
    "forecast": ("forecast", "analytics"),
    "scenario": ("forecast", "analytics"),
    "recommendation": ("recommendation", "analytics", "knowledge"),
    "report": ("report", "knowledge"),
    "executive_brief": ("report", "analytics", "recommendation"),
    "meeting_prep": ("report", "analytics", "knowledge"),
    "search": ("knowledge",),
    "decision": ("knowledge", "recommendation"),
    "approval": ("knowledge",),
    "task": ("knowledge",),
    "workflow": (),
}

# Keyword signals that pull a category in regardless of intent — the analytics
# vocabulary of the platform (Phase 5) is the largest, because a KPI question
# must reach SQL/series, never RAG.
CATEGORY_SIGNALS: dict[str, tuple[str, ...]] = {
    "analytics": (
        "trend", "trends", "kpi", "metric", "success rate", "decline",
        "declines", "transaction", "transactions", "volume", "value",
        "growth", "users", "active users", "retention", "conversion",
        "market share", "adoption", "throughput", "latency", "tpm",
        "week over week", "month over month", "compare", "comparison",
        "how many", "how much", "rate", "percentage", "average", "total",
        "bank", "psp", "merchant", "since", "between", "from", "daily"),
    "forecast": (
        "forecast", "predict", "prediction", "projection", "project",
        "next month", "next quarter", "next week", "next 30", "will be",
        "expected", "outlook", "trajectory", "future"),
    "ml": (
        "anomaly", "anomalies", "outlier", "unusual", "spike", "segment",
        "segmentation", "cluster", "churn", "at risk", "at-risk", "risk of",
        "failure", "likely to fail", "classify", "classification",
        "propensity"),
    "knowledge": (
        "why", "reason", "root cause", "rca", "meeting", "minutes",
        "decision", "policy", "sop", "incident", "outage", "email", "report",
        "discussed", "what happened", "after the", "document", "notes"),
    "recommendation": (
        "recommend", "should we", "what should", "advise", "how do we",
        "how can we", "next steps", "action", "improve", "mitigate",
        "best course", "strategy", "prioritise", "prioritize"),
    "report": (
        "report", "brief", "briefing", "summary", "summarise", "summarize",
        "board pack", "executive", "monthly review", "weekly review",
        "generate", "produce"),
    "dashboard": (
        "dashboard", "chart", "graph", "visualise", "visualize", "plot",
        "show me the numbers"),
}

# KPI vocabulary → the canonical KPI name the analytics/forecast engines use.
# The alias on the left is what an executive types; the value is what the cube
# calls it. Order matters — longer, more specific phrases first.
KPI_ALIASES: tuple[tuple[str, str], ...] = (
    ("technical decline", "Technical Declines (%)"),
    ("technical declines", "Technical Declines (%)"),
    ("tech decline", "Technical Declines (%)"),
    ("business decline", "Business Declines (%)"),
    ("success rate", "Success Rate (%)"),
    ("success", "Success Rate (%)"),
    ("transaction value", "Transaction Value (₹ Cr)"),
    ("transaction volume", "Transaction Volume (Mn)"),
    ("txn value", "Transaction Value (₹ Cr)"),
    ("txn volume", "Transaction Volume (Mn)"),
    ("volume", "Transaction Volume (Mn)"),
    ("transactions", "Transaction Volume (Mn)"),
    ("active users", "Active Customers (Mn)"),
    ("active customers", "Active Customers (Mn)"),
    ("customers", "Active Customers (Mn)"),
    ("users", "Active Customers (Mn)"),
    ("latency", "Avg Latency (ms)"),
    ("retention", "Retention (%)"),
    ("adoption", "Feature Adoption (%)"),
    ("market share", "Market Share (%)"),
)

MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
          "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}
# The regexes capture only the three-letter stem, so a label built from the
# match reads "Mar 2026". Answers quote these labels back to the user, so the
# full name is rendered from the month number instead.
MONTH_NAMES = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
               6: "June", 7: "July", 8: "August", 9: "September",
               10: "October", 11: "November", 12: "December"}
_MONTH_RE = "|".join(MONTHS)

# "July 1 to July 20", "July 1 - 20", "from July 1 through July 20"
_RANGE_MONTHDAY = re.compile(
    rf"\b({_MONTH_RE})[a-z]*\s+(\d{{1,2}})\b"
    rf"\s*(?:to|through|thru|until|till|[-–—]|and)\s*"
    rf"(?:({_MONTH_RE})[a-z]*\s+)?(\d{{1,2}})\b", re.I)
# ISO range "2026-07-01 to 2026-07-20"
_RANGE_ISO = re.compile(
    r"\b(\d{4}-\d{2}-\d{2})\s*(?:to|through|until|[-–—]|and)\s*"
    r"(\d{4}-\d{2}-\d{2})\b", re.I)
_SINGLE_MONTHDAY = re.compile(rf"\b(?:since|from|after)\s+({_MONTH_RE})[a-z]*"
                              rf"\s+(\d{{1,2}})\b", re.I)
# A whole named month: "May 2026", "in the month of May", "during May".
# Matched only *after* the day-bearing patterns above, so "July 1 to July 20"
# is still a day range rather than the whole of July. The trailing guard stops
# "May 12" being read as the month of May.
_MONTH_YEAR = re.compile(
    rf"\b(?:in|during|for|throughout)?\s*(?:the\s+)?(?:month\s+of\s+)?"
    rf"({_MONTH_RE})[a-z]*\s+(\d{{4}})\b", re.I)
_MONTH_ONLY = re.compile(
    rf"\b(?:in|during|for|throughout)\s+(?:the\s+)?(?:month\s+of\s+)?"
    rf"({_MONTH_RE})[a-z]*\b(?!\s*\d)", re.I)
_RELATIVE = (
    (re.compile(r"\blast\s+(\d{1,3})\s*days?\b", re.I), "last_ndays"),
    (re.compile(r"\bpast\s+(\d{1,3})\s*days?\b", re.I), "last_ndays"),
    (re.compile(r"\bnext\s+(\d{1,3})\s*days?\b", re.I), "next_ndays"),
    (re.compile(r"\blast\s+quarter\b", re.I), "last_quarter"),
    (re.compile(r"\bthis\s+quarter\b", re.I), "this_quarter"),
    (re.compile(r"\blast\s+month\b", re.I), "last_month"),
    (re.compile(r"\bthis\s+month\b", re.I), "this_month"),
    (re.compile(r"\bnext\s+month\b", re.I), "next_month"),
    (re.compile(r"\blast\s+week\b", re.I), "last_week"),
    (re.compile(r"\bthis\s+week\b", re.I), "this_week"),
    (re.compile(r"\blast\s+(\d{1,2})\s*weeks?\b", re.I), "last_nweeks"),
    (re.compile(r"\blast\s+6\s+months\b", re.I), "last_6months"),
    (re.compile(r"\bsix\s+months?\b", re.I), "last_6months"),
)


@dataclass
class Classification:
    """The engines a request needs and the shape parameters that steer them."""
    intent: str
    categories: tuple[str, ...] = ()
    scores: dict[str, float] = field(default_factory=dict)
    hybrid: bool = False
    primary: str = "knowledge"
    time_range: dict | None = None
    kpi_hints: tuple[str, ...] = ()
    entities: dict[str, list[str]] = field(default_factory=dict)

    def describe(self) -> dict:
        return {"intent": self.intent, "categories": list(self.categories),
                "primary": self.primary, "hybrid": self.hybrid,
                "scores": {k: round(v, 2) for k, v in self.scores.items()},
                "time_range": self.time_range,
                "kpi_hints": list(self.kpi_hints), "entities": self.entities}


class QueryClassifier:
    """Deterministically maps a classified intent + raw message to engine
    categories, a time window, and the KPIs and entities in play."""

    def __init__(self, entity_vocab: dict[str, list[str]] | None = None):
        # {"bank": [...], "psp": [...], "merchant": [...], "product": [...]}
        self._vocab = {k: [v.lower() for v in vs]
                       for k, vs in (entity_vocab or {}).items()}

    def set_vocab(self, entity_vocab: dict[str, list[str]]) -> None:
        self._vocab = {k: [v.lower() for v in vs]
                       for k, vs in (entity_vocab or {}).items()}

    def classify(self, message: str, intent) -> Classification:
        text = f" {str(message).strip().lower()} "
        intent_name = getattr(intent, "intent", str(intent))
        scores: dict[str, float] = {c: 0.0 for c in CATEGORIES}

        # 1. Intent seeds categories (strong prior).
        for i, cat in enumerate(INTENT_CATEGORIES.get(intent_name, ())):
            scores[cat] += 2.0 - i * 0.3

        # 2. Keyword signals sharpen or add categories.
        for cat, signals in CATEGORY_SIGNALS.items():
            for sig in signals:
                if sig in text:
                    scores[cat] += 1.0

        time_range = self._time_range(message)
        kpi_hints = self._kpis(text)
        entities = self._entities(text)

        # 3. Shape overrides make the decisive signals decisive. Each engine's
        #    own vocabulary pulls it in even when another category scored high,
        #    so a forecast or ML question is never swallowed by analytics.
        future = bool(time_range and
                      time_range.get("token") in ("next_month", "next_ndays"))
        has_analytics_kw = any(s in text for s in CATEGORY_SIGNALS["analytics"])
        has_fc_kw = any(s in text for s in CATEGORY_SIGNALS["forecast"])
        has_ml_kw = any(s in text for s in CATEGORY_SIGNALS["ml"])
        has_expl = any(s in text for s in
                       ("why", "root cause", "what happened", "reason",
                        "caused", "driver", "driving"))
        named_entity = bool(entities.get("bank") or entities.get("psp")
                            or entities.get("merchant"))

        # A named KPI or a past window is decisive analytics evidence — this is
        # what turns "show UPI trends July 1-20" toward the KPI series, not RAG
        # (Phase 11). A trend answer also retrieves the reports that explain it.
        if (time_range and not future) or kpi_hints:
            scores["analytics"] += 2.0
            scores["knowledge"] += 1.5   # supporting reports for the trend
        if named_entity:
            scores["analytics"] += 1.0
        # A forecast question (or a forward window) must reach the forecaster.
        if has_fc_kw or future:
            scores["forecast"] += 3.0
        # An ML question (anomaly/segment/churn/failure) must reach the models.
        if has_ml_kw:
            scores["ml"] += 3.0
        # "Why did <metric> change" is a root-cause question: knowledge for the
        # narrative, and the ML models for the drivers (feature importance).
        if has_expl:
            scores["knowledge"] += 2.0
            if kpi_hints or has_analytics_kw:
                scores["ml"] += 2.5

        active = {c: s for c, s in scores.items() if s > 0}
        if not active:
            active = {"knowledge": 1.0}  # a bare question still gets RAG
        ranked = sorted(active.items(), key=lambda kv: -kv[1])
        top = ranked[0][1]
        # Every category that clears an absolute floor OR a share of the top
        # runs — a hybrid answer pulls each engine that is clearly relevant, not
        # only the winner. The primary always runs.
        cut = max(2.0, top * 0.28)
        categories = tuple(c for i, (c, s) in enumerate(ranked)
                           if i == 0 or s >= cut)
        return Classification(
            intent=intent_name, categories=categories, scores=scores,
            hybrid=len(categories) > 1, primary=ranked[0][0],
            time_range=time_range, kpi_hints=kpi_hints, entities=entities)

    # -------------------------------------------------------- time ranges
    def _time_range(self, message: str) -> dict | None:
        m = _RANGE_ISO.search(message)
        if m:
            return {"kind": "explicit", "start_iso": m.group(1),
                    "end_iso": m.group(2),
                    "label": f"{m.group(1)} to {m.group(2)}"}
        m = _RANGE_MONTHDAY.search(message)
        if m:
            start_mon = MONTHS[m.group(1).lower()[:3]]
            end_mon = MONTHS[m.group(3).lower()[:3]] if m.group(3) else start_mon
            return {"kind": "explicit",
                    "start_md": (start_mon, int(m.group(2))),
                    "end_md": (end_mon, int(m.group(4))),
                    "label": f"{m.group(1).title()} {m.group(2)} to "
                             f"{(m.group(3) or m.group(1)).title()} "
                             f"{m.group(4)}"}
        m = _SINGLE_MONTHDAY.search(message)
        if m:
            mon = MONTHS[m.group(1).lower()[:3]]
            return {"kind": "explicit", "start_md": (mon, int(m.group(2))),
                    "end_md": None,
                    "label": f"since {m.group(1).title()} {m.group(2)}"}
        # A whole calendar month. Without this, "in the month of May 2026" fell
        # through to the relative patterns, matched none of them, and silently
        # became the default trailing 30 days — the answer then covered a
        # completely different period than the question asked about and said so
        # only in the fine print.
        m = _MONTH_YEAR.search(message)
        if m:
            mon = MONTHS[m.group(1).lower()[:3]]
            return {"kind": "month", "month": mon, "year": int(m.group(2)),
                    "label": f"{MONTH_NAMES[mon]} {m.group(2)}"}
        m = _MONTH_ONLY.search(message)
        if m:
            mon = MONTHS[m.group(1).lower()[:3]]
            return {"kind": "month", "month": mon, "year": None,
                    "label": MONTH_NAMES[mon]}
        for rx, token in _RELATIVE:
            rm = rx.search(message)
            if rm:
                out = {"kind": "relative", "token": token,
                       "label": rm.group(0).strip()}
                if rm.groups():
                    try:
                        out["n"] = int(rm.group(1))
                    except (ValueError, IndexError):
                        pass
                return out
        return None

    def _kpis(self, text: str) -> tuple[str, ...]:
        found: list[str] = []
        for alias, canonical in KPI_ALIASES:
            if f" {alias} " in text or f" {alias}," in text or \
                    f" {alias}?" in text or text.strip().endswith(alias):
                if canonical not in found:
                    found.append(canonical)
        return tuple(found)

    def _entities(self, text: str) -> dict[str, list[str]]:
        out: dict[str, list[str]] = {}
        for kind, names in self._vocab.items():
            hits = [n for n in names
                    if n and re.search(rf"\b{re.escape(n)}\b", text)]
            if hits:
                out[kind] = sorted(set(hits))
        return out

    @staticmethod
    def vocabulary() -> list[dict]:
        return [{"category": c,
                 "signals": list(CATEGORY_SIGNALS.get(c, ()))[:6]}
                for c in CATEGORIES]

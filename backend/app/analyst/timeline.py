"""Business-timeline translation (V10.0).

End users should never see the platform's internal/technical clock — "Day 18",
"Week 3", "Phase 2", "day_18" — unless they explicitly ask. This module maps a
technical day index onto the business calendar of the corpus and rewrites
technical timeline language into business language ("last 30 days", "previous
quarter", "December 2026", "the most recent executive review period").
"""
from __future__ import annotations

import re
from datetime import date, datetime, timedelta

_MONTHS = ["January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"]


def _to_date(value) -> date | None:
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        for fmt in ("%Y-%m-%d", "%d %b %Y", "%b %Y"):
            try:
                return datetime.strptime(value, fmt).date()
            except ValueError:
                continue
    return None


class BusinessTimeline:
    """Translates the corpus's internal day/week indices into business terms
    anchored on the last day of history (treated as 'today')."""

    def __init__(self, last_date: date | None, total_days: int):
        self.last_date = last_date or date.today()
        self.total_days = max(1, total_days)
        self.day1 = self.last_date - timedelta(days=self.total_days - 1)

    # ---- index -> business language --------------------------------------
    def date_for_day(self, day_index_1based: int) -> date:
        return self.day1 + timedelta(days=max(0, day_index_1based - 1))

    def label_for_day(self, day_index_1based: int) -> str:
        """A business label for a specific technical day, relative to today."""
        d = self.date_for_day(day_index_1based)
        return self.relative(d)

    def relative(self, d: date | None) -> str:
        d = _to_date(d) if not isinstance(d, date) else d
        if not d:
            return "recently"
        delta = (self.last_date - d).days
        if delta <= 0:
            return "today"
        if delta == 1:
            return "yesterday"
        if delta <= 7:
            return "in the last week"
        if delta <= 30:
            return "in the last 30 days"
        if delta <= 90:
            return "in the last quarter"
        return f"{_MONTHS[d.month - 1]} {d.year}"

    def period(self, span: str = "month") -> str:
        """A human name for a rolling window ending today."""
        end = self.last_date
        if span == "day":
            return end.strftime("%d %b %Y")
        if span == "week":
            return "the last 7 days"
        if span == "month":
            return f"{_MONTHS[end.month - 1]} {end.year}"
        if span == "quarter":
            q = (end.month - 1) // 3 + 1
            return f"Q{q} {end.year}"
        if span == "rolling30":
            return "the last 30 days"
        if span == "rolling90":
            return "the last 90 days"
        return "the current period"

    # ---- free-text rewriting --------------------------------------------
    _DAY_RE = re.compile(r"\b[Dd]ay[ _-]?(\d{1,3})\b")
    _WEEK_RE = re.compile(r"\b[Ww]eek[ _-]?(\d{1,3})\b")
    _PHASE_RE = re.compile(r"\b[Pp]hase[ _-]?(\d{1,2})\b")
    _DAYFOLDER_RE = re.compile(r"\bday_(\d{2,3})\b")

    def humanize(self, text: str) -> str:
        """Rewrite technical timeline references in free text into business
        language. Idempotent and safe on text with none."""
        if not text:
            return text

        def day_sub(m):
            return self.label_for_day(int(m.group(1)))

        def week_sub(m):
            wk = int(m.group(1))
            d = self.date_for_day(min(wk * 7, self.total_days))
            return self.relative(d)

        out = self._DAYFOLDER_RE.sub(day_sub, text)
        out = self._DAY_RE.sub(day_sub, out)
        out = self._WEEK_RE.sub(week_sub, out)
        out = self._PHASE_RE.sub("the relevant period", out)
        return out

    @classmethod
    def from_container(cls, container) -> "BusinessTimeline":
        last, total = None, 180
        try:
            eco = container.ecosystem.ecosystem()
            if eco.available and eco.daily_metrics:
                last = _to_date(eco.daily_metrics[-1].get("date"))
                total = len(eco.daily_metrics)
        except Exception:  # noqa: BLE001
            pass
        return cls(last, total)

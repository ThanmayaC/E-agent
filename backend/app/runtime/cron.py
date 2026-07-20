"""Minimal 5-field cron expression support.

``minute hour day-of-month month day-of-week`` with ``*``, ``*/step``,
``a-b``, ``a-b/step``, and comma-separated lists. Day-of-week is 0-6 with
Sunday as 0 (7 is accepted as Sunday too).

Implemented here rather than pulled in as a dependency: the lite profile
installs without a scheduler library, and the enterprise scheduler needs
exactly this much of cron. When day-of-month and day-of-week are both
restricted, the standard cron semantics apply — the job runs when *either*
matches.
"""
from __future__ import annotations

from datetime import datetime, timedelta

FIELD_RANGES = ((0, 59), (0, 23), (1, 31), (1, 12), (0, 6))
FIELD_NAMES = ("minute", "hour", "day-of-month", "month", "day-of-week")
MAX_SEARCH_MINUTES = 60 * 24 * 366 * 2  # two years — beyond this, no match


class CronError(ValueError):
    """Raised for an unparseable cron expression."""


def _parse_field(spec: str, low: int, high: int, name: str) -> set[int]:
    values: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            raise CronError(f"empty {name} field")
        step = 1
        if "/" in part:
            part, _, step_text = part.partition("/")
            try:
                step = int(step_text)
            except ValueError:
                raise CronError(f"invalid step in {name}: {step_text!r}")
            if step < 1:
                raise CronError(f"step must be >= 1 in {name}")
        if part == "*":
            start, end = low, high
        elif "-" in part:
            start_text, _, end_text = part.partition("-")
            try:
                start, end = int(start_text), int(end_text)
            except ValueError:
                raise CronError(f"invalid range in {name}: {part!r}")
        else:
            try:
                start = end = int(part)
            except ValueError:
                raise CronError(f"invalid value in {name}: {part!r}")
        if name == "day-of-week":
            start, end = start % 7, end % 7  # accept 7 as Sunday
            if end < start:
                start, end = low, high  # e.g. 5-7 normalises to the full week
        if start < low or end > high or end < start:
            raise CronError(
                f"{name} out of range: {part!r} (expected {low}-{high})")
        values.update(range(start, end + 1, step))
    return values


class CronSchedule:
    """A parsed cron expression that can answer "when next?"."""

    def __init__(self, expression: str):
        fields = expression.split()
        if len(fields) != 5:
            raise CronError(
                f"cron needs 5 fields (got {len(fields)}): {expression!r}")
        self.expression = expression
        self.minutes, self.hours, self.days, self.months, self.weekdays = (
            _parse_field(field, low, high, name)
            for field, (low, high), name in zip(fields, FIELD_RANGES,
                                                FIELD_NAMES))
        self._dom_restricted = fields[2] != "*"
        self._dow_restricted = fields[4] != "*"

    def matches(self, moment: datetime) -> bool:
        if moment.minute not in self.minutes or moment.hour not in self.hours:
            return False
        if moment.month not in self.months:
            return False
        dom_ok = moment.day in self.days
        dow_ok = (moment.weekday() + 1) % 7 in self.weekdays  # Mon=0 -> Sun=0
        if self._dom_restricted and self._dow_restricted:
            return dom_ok or dow_ok
        return dom_ok and dow_ok

    def next_after(self, moment: datetime) -> datetime | None:
        """The first matching minute strictly after ``moment``."""
        candidate = (moment.replace(second=0, microsecond=0)
                     + timedelta(minutes=1))
        for _ in range(MAX_SEARCH_MINUTES):
            if self.matches(candidate):
                return candidate
            candidate += timedelta(minutes=1)
        return None

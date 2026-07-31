"""Reconciliation — do the published cubes still agree with the corpus?

The platform's central correctness property is that every number on every page
traces back to the same transactions. That held only by convention until now: a
second simulator was writing the analytics cubes from an asserted KPI series,
and nothing noticed that Analytics and Ecosystem were reporting different
success rates for the same day.

This module makes the property checkable. It recomputes the headline series
straight from the corpus and compares it against what the cubes publish,
reporting correlation and worst-day drift per KPI. It is wired into
``python -m app.warehouse.project_cubes --check`` and into the test suite, so a
future change that reintroduces a parallel source fails loudly instead of
quietly disagreeing with itself.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass, field
from pathlib import Path

from app.warehouse.projection import ATTEMPT_TYPES, NATIONAL_SCALE_M_PER_TXN

try:
    import duckdb
    _DUCKDB = True
except ImportError:  # pragma: no cover
    _DUCKDB = False

# A cube is a rounded projection of the corpus, so exact equality is the wrong
# bar. These are the tolerances that still catch a genuinely different source:
# correlation collapses long before drift does, which is why it is the primary
# signal — the old parallel simulator scored r=+0.20 here.
MIN_CORRELATION = 0.99
MAX_MEAN_DRIFT_PP = 0.05


@dataclass
class KpiCheck:
    kpi: str
    correlation: float
    mean_abs_drift: float
    max_abs_drift: float
    worst_day: str
    days: int

    @property
    def ok(self) -> bool:
        return (self.correlation >= MIN_CORRELATION
                and self.mean_abs_drift <= MAX_MEAN_DRIFT_PP)


@dataclass
class ReconcileReport:
    checks: list[KpiCheck] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors and all(c.ok for c in self.checks)

    def render(self) -> str:
        lines = ["Cube <-> corpus reconciliation", "=" * 64]
        for e in self.errors:
            lines.append(f"  ERROR  {e}")
        for c in self.checks:
            flag = "ok  " if c.ok else "FAIL"
            lines.append(
                f"  {flag} {c.kpi:26s} r={c.correlation:+.4f} "
                f"mean|d|={c.mean_abs_drift:.4f} "
                f"max|d|={c.max_abs_drift:.4f} ({c.worst_day}) "
                f"n={c.days}")
        lines.append("=" * 64)
        lines.append("PASS - cubes reconcile with the corpus" if self.ok
                     else "FAIL - cubes disagree with the transactions "
                          "they claim to summarise")
        return "\n".join(lines)


def _corr(a: list[float], b: list[float]) -> float:
    n = len(a)
    if n < 2:
        return 0.0
    ma, mb = sum(a) / n, sum(b) / n
    va = sum((x - ma) ** 2 for x in a)
    vb = sum((x - mb) ** 2 for x in b)
    if va <= 0 or vb <= 0:
        # A constant series cannot be correlated. Treat identical constants as
        # agreement and anything else as disagreement, rather than dividing by
        # zero and reporting a spurious pass.
        return 1.0 if abs(ma - mb) < 1e-9 else 0.0
    cov = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    return cov / (va ** 0.5 * vb ** 0.5)


def reconcile(warehouse_root: str | Path,
              cube_dir: str | Path) -> ReconcileReport:
    report = ReconcileReport()
    cube_path = Path(cube_dir) / "daily_metrics.csv"
    if not _DUCKDB:
        report.errors.append("duckdb unavailable — cannot reconcile")
        return report
    if not cube_path.exists():
        report.errors.append(f"missing cube: {cube_path}")
        return report

    txns = str(Path(warehouse_root) / "transactions" / "*.parquet")
    att = ", ".join(f"'{t}'" for t in ATTEMPT_TYPES)
    con = duckdb.connect()
    try:
        truth = {
            r[0]: r for r in con.execute(f"""
              SELECT txn_date,
                     100.0*sum(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)
                          /count(*)                       AS success_rate,
                     count(*)                             AS attempts,
                     sum(amount_inr)/nullif(count(*),0)   AS avg_ticket
              FROM read_parquet('{txns}')
              WHERE txn_type IN ({att})
              GROUP BY 1 ORDER BY 1""").fetchall()}
    except Exception as exc:  # pragma: no cover - corrupt/absent corpus
        report.errors.append(f"cannot read corpus: {exc}")
        con.close()
        return report
    con.close()

    if not truth:
        report.errors.append("corpus contains no attempt rows")
        return report

    with cube_path.open(encoding="utf-8") as fh:
        published = list(csv.DictReader(fh))

    # (label, cube column, index into the truth row, scale applied to truth)
    specs = [
        ("Success Rate (%)", "success_rate", 1, 1.0),
        ("Attempts (sampled)", "sample_txns", 2, 1.0),
        ("Average Ticket (INR)", "avg_ticket_inr", 3, 1.0),
        ("Volume (M/day)", "volume_millions", 2, NATIONAL_SCALE_M_PER_TXN),
    ]
    for label, column, ix, scale in specs:
        want: list[float] = []
        got: list[float] = []
        worst, worst_day = 0.0, "-"
        for row in published:
            key = str(row.get("date", ""))
            src = truth.get(key)
            if src is None or not row.get(column):
                continue
            expected = float(src[ix]) * scale
            actual = float(row[column])
            want.append(expected)
            got.append(actual)
            drift = abs(expected - actual)
            if drift > worst:
                worst, worst_day = drift, key
        if not want:
            report.errors.append(f"{label}: no comparable days")
            continue
        mean_drift = sum(abs(a - b) for a, b in zip(want, got)) / len(want)
        report.checks.append(KpiCheck(
            kpi=label, correlation=_corr(want, got), mean_abs_drift=mean_drift,
            max_abs_drift=worst, worst_day=worst_day, days=len(want)))
    return report

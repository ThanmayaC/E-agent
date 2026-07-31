"""Rebuild the day-wise analytics cubes from the transaction corpus.

    python -m app.warehouse.project_cubes [--check] [--out DIR]

``--check`` reconciles without writing: it reports, per cube, how far the
published CSV drifts from what the corpus actually says. That is the guard
against the two-truth problem returning — a large drift means something is
publishing numbers the transactions do not support.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from app.warehouse.projection import CubeProjection
from app.warehouse.projection_derived import DerivedProjection


def _default_root() -> Path:
    return Path(__file__).resolve().parents[3] / "enterprise_data"


def main(argv: list[str] | None = None) -> int:
    root = _default_root()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--warehouse", default=str(root / "warehouse"),
                    help="warehouse root holding transactions/ and reference/")
    ap.add_argument("--out", default=str(root / "master" / "analytics"),
                    help="directory to write the projected cubes into")
    ap.add_argument("--workbook",
                    default=str(root / "master" / "upi_kpis_month.xlsx"),
                    help="KPI workbook whose corpus-derivable rows are rewritten")
    ap.add_argument("--skip-workbook", action="store_true",
                    help="project the cubes only, leaving the KPI workbook alone")
    ap.add_argument("--forecasts", action="store_true",
                    help="also rebuild forecasts.csv / forecast_forward.csv "
                         "from the ML pipeline (slower: trains per series)")
    ap.add_argument("--check", action="store_true",
                    help="reconcile against the existing cubes; write nothing")
    args = ap.parse_args(argv)

    if args.check:
        from app.warehouse.reconcile import reconcile
        report = reconcile(args.warehouse, args.out)
        print(report.render())
        return 0 if report.ok else 1

    proj = CubeProjection(args.warehouse, args.out)
    results = proj.build()
    # The derived cubes — weekly evolution, rollups, relationships, findings,
    # storylines and decision tracking — used to come from the old generator's
    # own KPI series. They are projections now too.
    results.update(DerivedProjection(args.warehouse, args.out).build())
    total = sum(r.rows for r in results.values())
    for name, r in sorted(results.items()):
        print(f"  {name:22s} {r.rows:>7,} rows -> {r.path.name}")
    print(f"projected {len(results)} cubes, {total:,} rows from the corpus")

    if args.forecasts:
        from app.core.config import Settings
        from app.core.container import Container
        from app.warehouse.forecast_projection import ForecastProjection
        c = Container(Settings())
        made = ForecastProjection(c.ml_pipeline, c.tx_analytics, args.out).build()
        for name, n in sorted(made.items()):
            print(f"  {name:22s} {n:>7,} rows (learned, not extrapolated)")

    if not args.skip_workbook:
        from app.warehouse.projection import project_kpi_workbook
        book = Path(args.workbook)
        if book.exists():
            written = project_kpi_workbook(args.warehouse, book)
            for kpi, days in sorted(written.items()):
                print(f"  KPI {kpi:34s} {days:>4} days -> {book.name}")
        else:
            print(f"  (skipped KPI workbook — not found: {book})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

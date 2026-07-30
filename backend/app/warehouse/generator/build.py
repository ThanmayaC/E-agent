"""Warehouse build — runs the simulation and lands it on disk.

Layout produced under ``enterprise_data/warehouse``::

    transactions/txns_YYYY-MM-DD.parquet   one file per day, all products
    reference/products.parquet             product catalog
    reference/mcc.parquet                  MCC catalog
    reference/banks.parquet                issuer/beneficiary banks
    reference/psps.parquet                 payment service providers
    reference/cities.parquet               geography
    reference/segments.parquet             customer segments
    reference/customers.parquet            customer master
    reference/merchants.parquet            merchant master
    reference/mandates.parquet             AutoPay mandate registry
    reference/mandate_events.parquet       full mandate lifecycle stream
    reference/incidents.parquet            ground-truth event calendar
    reference/calendar.parquet             per-day calendar context
    MANIFEST.json                          build metadata + row counts

Only raw facts are written. No KPI, no daily rollup, no dashboard table — every
number the platform shows is computed from these files at query time.
"""
from __future__ import annotations

import json
import random
import time
from dataclasses import asdict
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

from app.core.logging import get_logger
from app.warehouse.generator.calendar_in import build_calendar
from app.warehouse.generator.catalog import (
    BANKS, CITIES, FAILURE_CODES, MCCS, PRODUCTS, PSPS, SEGMENTS,
)
from app.warehouse.generator.events import EventPlanner
from app.warehouse.generator.mandates import MandateBook
from app.warehouse.generator.population import Population
from app.warehouse.generator.simulate import TransactionSimulator

logger = get_logger(__name__)

DEFAULT_START = date(2026, 1, 5)
DEFAULT_DAYS = 206
SCHEMA_VERSION = "1.0"


def _write_parquet(df: pd.DataFrame, path: Path) -> None:
    """Parquet via DuckDB — no pyarrow dependency needed."""
    import duckdb
    path.parent.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect()
    try:
        con.register("_df", df)
        con.execute(
            f"COPY _df TO '{path.as_posix()}' "
            f"(FORMAT PARQUET, COMPRESSION ZSTD)")
    finally:
        con.close()


def build_warehouse(out_dir: Path, *, start: date = DEFAULT_START,
                    days: int = DEFAULT_DAYS, seed: int = 20260105,
                    base_daily: int = 11_000, n_customers: int = 80_000,
                    n_merchants: int = 2_400, n_mandates: int = 14_000,
                    progress=None) -> dict:
    """Generate the whole warehouse. Returns the manifest dict."""
    t0 = time.time()
    out_dir = Path(out_dir)
    txn_dir = out_dir / "transactions"
    ref_dir = out_dir / "reference"
    for d in (txn_dir, ref_dir):
        d.mkdir(parents=True, exist_ok=True)
    # A rebuild must not leave yesterday's partitions behind.
    for old in txn_dir.glob("txns_*.parquet"):
        old.unlink()

    rng = np.random.default_rng(seed)
    prng = random.Random(seed)

    calendar = build_calendar(start, days)
    events = EventPlanner(prng, days).plan()
    pop = Population(rng, days, n_customers=n_customers,
                     n_merchants=n_merchants)
    book = MandateBook(rng, pop, days, start, n_mandates=n_mandates)
    sim = TransactionSimulator(rng=rng, pop=pop, book=book, calendar=calendar,
                               events=events, start_date=start,
                               base_daily=base_daily)

    total_rows = 0
    per_day: list[dict] = []
    for d in range(days):
        rows = sim.simulate_day(d)
        day = start + timedelta(days=d)
        if rows:
            df = pd.DataFrame(rows)
            df = _coerce(df)
            _write_parquet(df, txn_dir / f"txns_{day}.parquet")
            total_rows += len(df)
            per_day.append({"date": str(day), "rows": len(df)})
        if progress and (d % 20 == 0 or d == days - 1):
            progress(d + 1, days, total_rows)
        logger.debug("warehouse day %s: %d rows", day, len(rows))

    # ---------------------------------------------------------- reference
    _write_parquet(pd.DataFrame([{
        "product_code": p.code, "product_name": p.name, "family": p.family,
        "owning_team": p.owning_team, "lifecycle": p.lifecycle,
        "payment_types": ",".join(p.payment_types),
        "ticket_median_inr": p.ticket_median, "ticket_cap_inr": p.ticket_cap,
        "merchant_facing": p.merchant_facing,
        "settlement_sensitive": p.settlement_sensitive,
        "description": p.description,
    } for p in PRODUCTS]), ref_dir / "products.parquet")

    _write_parquet(pd.DataFrame([{
        "mcc": m.code, "mcc_name": m.name, "category": m.category,
        "subcategory": m.subcategory, "ticket_multiplier": m.ticket_mult,
        "seasonality": m.seasonality, "risk_index": m.risk,
    } for m in MCCS]), ref_dir / "mcc.parquet")

    _write_parquet(pd.DataFrame(BANKS), ref_dir / "banks.parquet")
    _write_parquet(pd.DataFrame(PSPS), ref_dir / "psps.parquet")
    _write_parquet(pd.DataFrame([{
        "city": c[0], "state": c[1], "region": c[2], "weight": c[3],
        "city_tier": c[4]} for c in CITIES]), ref_dir / "cities.parquet")
    _write_parquet(pd.DataFrame(SEGMENTS), ref_dir / "segments.parquet")
    _write_parquet(pd.DataFrame([{
        "code": f.code, "reason": f.reason, "bucket": f.bucket,
        "retryable": f.retryable, "owner": f.owner}
        for f in FAILURE_CODES]), ref_dir / "failure_codes.parquet")

    _write_parquet(pd.DataFrame(pop.customer_rows(start)),
                   ref_dir / "customers.parquet")
    _write_parquet(pd.DataFrame(pop.merchant_rows(start)),
                   ref_dir / "merchants.parquet")
    _write_parquet(pd.DataFrame(book.registry_rows()),
                   ref_dir / "mandates.parquet")
    _write_parquet(pd.DataFrame(book.events), ref_dir / "mandate_events.parquet")
    _write_parquet(pd.DataFrame([e.to_row(start) for e in events]),
                   ref_dir / "incidents.parquet")
    _write_parquet(pd.DataFrame([{
        "date": str(c.day), "day_index": c.day_index,
        "day_of_week": c.weekday, "is_weekend": c.is_weekend,
        "is_salary_window": c.is_salary_window, "is_month_end": c.is_month_end,
        "is_quarter_end": c.is_quarter_end, "holiday": c.holiday,
        "festival": c.festival, "label": c.label,
        "spend_multiplier": c.spend_mult,
        "settlement_multiplier": c.settlement_mult,
    } for c in calendar]), ref_dir / "calendar.parquet")

    manifest = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "seed": seed,
        "start_date": str(start),
        "end_date": str(start + timedelta(days=days - 1)),
        "days": days,
        "transactions": total_rows,
        "products": len(PRODUCTS),
        "mccs": len(MCCS),
        "banks": len(BANKS),
        "psps": len(PSPS),
        "customers": n_customers,
        "merchants": n_merchants,
        "mandates": n_mandates,
        "mandate_events": len(book.events),
        "incidents": len(events),
        "build_seconds": round(time.time() - t0, 1),
        "per_day": per_day,
    }
    (out_dir / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8")
    logger.info("warehouse built: %s transactions across %s days in %ss",
                total_rows, days, manifest["build_seconds"])
    return manifest


_STRING_COLS = [
    "txn_id", "txn_ts", "txn_date", "calendar_event", "txn_type",
    "product_code", "product_name", "product_family", "payment_type",
    "status", "failure_code", "failure_reason", "failure_bucket",
    "failure_owner", "parent_txn_id", "payer_bank", "payee_bank",
    "payer_psp", "payee_psp", "merchant_id", "merchant_name",
    "merchant_tier", "mcc", "mcc_category", "mcc_subcategory",
    "customer_id", "customer_segment", "device", "channel", "city",
    "state", "region", "mandate_id",
]


def _coerce(df: pd.DataFrame) -> pd.DataFrame:
    """Stable dtypes so every daily parquet file has an identical schema.

    Nullable pandas dtypes matter here: an object column that happens to be
    all-null on one day would otherwise be written as an INTEGER column, and
    the next day's VARCHAR would no longer union with it.
    """
    for c in _STRING_COLS:
        if c in df.columns:
            df[c] = df[c].map(lambda v: None if v is None or (
                isinstance(v, float) and v != v) else str(v)).astype("string")
    for c in ("day_index", "hour", "day_of_week", "week_of_year", "month",
              "quarter", "city_tier", "latency_ms", "switch_ms", "issuer_ms",
              "attempt_no"):
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype(
                "int32")
    for c in ("amount_inr", "risk_score"):
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").astype("float64")
    for c in ("is_weekend", "is_holiday", "is_retry"):
        if c in df.columns:
            df[c] = df[c].astype(bool)
    if "retryable" in df.columns:
        df["retryable"] = df["retryable"].astype("boolean")
    return df


def main() -> None:  # pragma: no cover — CLI entry point
    import argparse
    ap = argparse.ArgumentParser(description="Build the transaction warehouse")
    ap.add_argument("--out", default=None,
                    help="output directory (default: <repo>/enterprise_data/warehouse)")
    ap.add_argument("--start", default=str(DEFAULT_START))
    ap.add_argument("--days", type=int, default=DEFAULT_DAYS)
    ap.add_argument("--seed", type=int, default=20260105)
    ap.add_argument("--base-daily", type=int, default=11_000)
    ap.add_argument("--customers", type=int, default=80_000)
    ap.add_argument("--merchants", type=int, default=2_400)
    ap.add_argument("--mandates", type=int, default=14_000)
    args = ap.parse_args()

    out = Path(args.out) if args.out else (
        Path(__file__).resolve().parents[4] / "enterprise_data" / "warehouse")

    def show(done: int, total: int, rows: int) -> None:
        print(f"  day {done}/{total} — {rows:,} transactions", flush=True)

    y, m, dd = (int(x) for x in args.start.split("-"))
    mf = build_warehouse(out, start=date(y, m, dd), days=args.days,
                         seed=args.seed, base_daily=args.base_daily,
                         n_customers=args.customers,
                         n_merchants=args.merchants,
                         n_mandates=args.mandates, progress=show)
    print(json.dumps({k: v for k, v in mf.items() if k != "per_day"},
                     indent=2))


if __name__ == "__main__":  # pragma: no cover
    main()

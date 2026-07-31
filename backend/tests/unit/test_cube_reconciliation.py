"""The published analytics must agree with the transactions they summarise.

This is a regression guard, not a unit test of arithmetic. The platform shipped
for months with two independent transaction simulators: the warehouse corpus fed
Analytics/Products/ML, while a second sampler reconciled itself to a
hand-authored KPI series and fed Ecosystem/Evolution and the executive KPI
surfaces. Nothing compared them, so nobody noticed that on 2026-01-28 one page
reported 95.17% success and another reported 99.55% for the same day.

These tests fail if a parallel source is ever reintroduced.
"""
from __future__ import annotations

import csv
from pathlib import Path

import pytest

duckdb = pytest.importorskip("duckdb")

from app.warehouse.projection import (  # noqa: E402
    ATTEMPT_TYPES, KPI_FROM_CORPUS, NATIONAL_SCALE_M_PER_TXN, CubeProjection,
)
from app.warehouse.reconcile import MIN_CORRELATION, _corr, reconcile  # noqa: E402

DATA = Path(__file__).resolve().parents[3] / "enterprise_data"
WAREHOUSE = DATA / "warehouse"
CUBES = DATA / "master" / "analytics"

corpus = pytest.mark.skipif(
    not (WAREHOUSE / "transactions").exists(),
    reason="generated corpus not present in this checkout")


# --------------------------------------------------------------- unit-level
def test_corr_matches_known_values():
    assert _corr([1.0, 2.0, 3.0], [2.0, 4.0, 6.0]) == pytest.approx(1.0)
    assert _corr([1.0, 2.0, 3.0], [3.0, 2.0, 1.0]) == pytest.approx(-1.0)


def test_corr_treats_equal_constants_as_agreement():
    # Two flat series carry no covariance. Reporting 0.0 would fail a cube that
    # is in fact identical to the corpus, so equal constants agree and unequal
    # constants do not.
    assert _corr([5.0, 5.0, 5.0], [5.0, 5.0, 5.0]) == pytest.approx(1.0)
    assert _corr([5.0, 5.0, 5.0], [9.0, 9.0, 9.0]) == pytest.approx(0.0)


def test_reconcile_reports_error_when_cube_missing(tmp_path):
    report = reconcile(WAREHOUSE, tmp_path)
    assert not report.ok
    assert any("missing cube" in e for e in report.errors)


# ------------------------------------------------------------- corpus-level
@corpus
def test_published_cubes_reconcile_with_corpus():
    """Every published KPI must trace to the transactions."""
    report = reconcile(WAREHOUSE, CUBES)
    assert report.checks, "no KPIs were compared"
    assert report.ok, "\n" + report.render()


@corpus
def test_projection_is_deterministic(tmp_path):
    """Two runs over an unchanged corpus produce byte-identical cubes."""
    a, b = tmp_path / "a", tmp_path / "b"
    CubeProjection(WAREHOUSE, a).build()
    CubeProjection(WAREHOUSE, b).build()
    for produced in sorted(a.glob("*.csv")):
        assert produced.read_bytes() == (b / produced.name).read_bytes(), \
            f"{produced.name} differs between runs"


@corpus
def test_daily_metrics_internally_consistent():
    """The decline splits and the success rate must add up on every row."""
    with (CUBES / "daily_metrics.csv").open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    assert rows
    for r in rows:
        sr = float(r["success_rate"])
        tech = float(r["technical_decline_pct"])
        biz = float(r["business_decline_pct"])
        pend = float(r["pending_pct"])
        risk = float(r["risk_decline_pct"])
        assert 0.0 <= sr <= 100.0
        # Success + every failure mode is the whole day, allowing for the
        # two-decimal rounding each column carries independently.
        assert sr + tech + biz + risk + pend == pytest.approx(100.0, abs=0.05), \
            f"{r['date']} does not sum to 100: {sr}+{tech}+{biz}+{risk}+{pend}"
        assert 0 <= int(r["peak_hour"]) <= 23
        assert int(r["active_customers_sample"]) > 0


@corpus
def test_archetype_labels_match_the_numbers():
    """An 'incident-affected' day must actually show a depressed success rate."""
    with (CUBES / "daily_metrics.csv").open(encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    flagged = [r for r in rows if r["archetype"] == "Incident-affected day"]
    assert flagged, "corpus contains incidents but no day is labelled for one"
    for r in flagged:
        assert float(r["success_rate"]) < 97.5, \
            f"{r['date']} labelled incident-affected at {r['success_rate']}%"


@corpus
def test_entity_cubes_sum_to_the_daily_total():
    """Per-bank and per-PSP attempts must reconcile to the day's total.

    Each payment has exactly one payer bank and one payer PSP, so these are
    partitions of the same population and any drift means a cube was built from
    a different scan than the spine.
    """
    con = duckdb.connect()
    att = ", ".join(f"'{t}'" for t in ATTEMPT_TYPES)
    total = dict(con.execute(f"""
        SELECT day_index + 1, count(*)
        FROM read_parquet('{WAREHOUSE / 'transactions' / '*.parquet'}')
        WHERE txn_type IN ({att}) GROUP BY 1""").fetchall())
    for cube in ("bank_daily.csv", "psp_daily.csv", "feature_daily.csv"):
        per_day: dict[int, int] = {}
        with (CUBES / cube).open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                per_day[int(row["day"])] = per_day.get(
                    int(row["day"]), 0) + int(row["txns"])
        assert per_day, f"{cube} is empty"
        for day, n in per_day.items():
            assert n == total[day], (
                f"{cube} day {day}: cube={n} corpus={total[day]}")
    con.close()


@corpus
def test_kpi_workbook_rows_track_the_corpus():
    """The workbook rows the corpus owns must correlate with it."""
    openpyxl = pytest.importorskip("openpyxl")
    book = DATA / "master" / "upi_kpis_month.xlsx"
    if not book.exists():
        pytest.skip("KPI workbook not generated")
    ws = openpyxl.load_workbook(book, data_only=True)["Monthly KPIs"]
    published: dict[str, list[float]] = {}
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row and row[0] is not None:
            published[str(row[0])] = [float(v) for v in row[2:] if v is not None]

    con = duckdb.connect()
    rows = con.execute(f"""
        SELECT txn_date, count(*),
               100.0*sum(CASE WHEN status='SUCCESS' THEN 1 ELSE 0 END)/count(*)
        FROM read_parquet('{WAREHOUSE / 'transactions' / '*.parquet'}')
        WHERE txn_type IN ({", ".join(f"'{t}'" for t in ATTEMPT_TYPES)})
        GROUP BY 1 ORDER BY 1""").fetchall()
    con.close()

    checks = {
        "Success Rate (%)": [r[2] for r in rows],
        "UPI Transactions (M/day)": [
            r[1] * NATIONAL_SCALE_M_PER_TXN for r in rows],
    }
    for kpi, truth in checks.items():
        assert kpi in KPI_FROM_CORPUS
        got = published.get(kpi)
        assert got, f"{kpi} missing from workbook"
        n = min(len(got), len(truth))
        r = _corr(got[:n], truth[:n])
        assert r >= MIN_CORRELATION, f"{kpi} correlates {r:+.4f} with the corpus"


@corpus
def test_non_payment_kpis_are_left_alone():
    """Metrics other subsystems own must not be fabricated from payments."""
    for kpi in ("Customer Complaints", "Fraud Alerts", "Merchant Adoption (M)",
                "Risk Score", "Settlement Success (%)"):
        assert kpi not in KPI_FROM_CORPUS, (
            f"{kpi} is not derivable from payment rows and must not be "
            f"projected from them")

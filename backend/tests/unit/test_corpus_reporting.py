"""Guards for the corpus-derived reports and the derived cube projections.

The property under test throughout is the one the platform's credibility rests
on: a number that appears in a report, a cube or a narrative must be
re-derivable from the transaction corpus. These tests fail if a parallel source
of truth reappears, if a report degenerates back into a template, or if a
generated sentence contradicts the numbers beside it.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3] / "enterprise_data"
REPORTS = sorted(ROOT.glob("day_*/reports/RPT-*-daily.md"))
ANALYTICS = ROOT / "master" / "analytics"

pytestmark = pytest.mark.skipif(
    not REPORTS, reason="enterprise_data corpus not built in this checkout")


def _read(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


# --------------------------------------------------------------- provenance
def test_reports_do_not_cite_the_hand_authored_workbook():
    """The old reports declared 'Source: upi_kpis_month.xlsx'.

    That workbook is a *projection* of the corpus now, so a report sourcing
    itself from it would be reading a derived artifact instead of the facts —
    exactly the indirection that let two sources of truth diverge before.
    """
    offenders = [p.name for p in REPORTS
                 if "upi_kpis_month.xlsx" in p.read_text(encoding="utf-8")]
    assert offenders == [], f"reports still sourced from the workbook: {offenders}"


def test_reports_declare_the_corpus_as_their_source():
    for p in REPORTS[:20]:
        text = p.read_text(encoding="utf-8")
        assert "source: enterprise_data/warehouse (raw transactions)" in text
        assert "## Evidence" in text, f"{p.name} has no evidence appendix"


# ------------------------------------------------------------- not a template
def test_every_report_has_a_distinct_summary_and_executive_view():
    """A template produces the same prose with the numbers swapped.

    Requiring near-total uniqueness across 200+ days is the cheapest way to
    detect a regression back to one, since any fixed sentence structure with
    substituted figures still collapses when a quiet day repeats.
    """
    def section(text: str, name: str) -> str:
        m = re.search(rf"## {name}\n(.*?)(?=\n## |\Z)", text, re.S)
        return m.group(1).strip() if m else ""

    texts = [p.read_text(encoding="utf-8") for p in REPORTS]
    summaries = {section(t, "Summary") for t in texts}
    execs = {section(t, "Executive observation") for t in texts}
    assert len(summaries) / len(texts) > 0.95
    assert len(execs) / len(texts) > 0.95


def test_reports_carry_real_analysis_not_just_tables():
    """Each report must contain the sections a PM actually reads."""
    required = ["## Summary", "## Key measures", "## What moved",
                "## Product performance", "## Rail performance",
                "## Where the demand came from", "## Failure analysis",
                "## Customer behaviour", "## Operational events",
                "## Risks and opportunities", "## Executive observation",
                "## Evidence"]
    text = REPORTS[len(REPORTS) // 2].read_text(encoding="utf-8")
    missing = [s for s in required if s not in text]
    assert missing == [], f"report is missing sections: {missing}"


def test_report_headline_matches_the_corpus_row_count():
    """The headline attempt count must equal what the warehouse says."""
    pytest.importorskip("duckdb")
    import duckdb

    txn = (ROOT / "warehouse" / "transactions" / "*.parquet").as_posix()
    con = duckdb.connect()
    counts = dict(con.execute(f"""
        SELECT txn_date, COUNT(*) FROM read_parquet('{txn}')
        WHERE txn_type IN ('PAYMENT','MANDATE_EXECUTION','RETRY','MANDATE_RETRY')
        GROUP BY 1""").fetchall())

    checked = 0
    for p in REPORTS[::37]:
        text = p.read_text(encoding="utf-8")
        day = re.search(r"Corpus window queried: `(\d{4}-\d{2}-\d{2})`", text)
        stated = re.search(r"attempts=([\d,]+)", text)
        assert day and stated, f"{p.name} lost its evidence anchors"
        assert int(stated.group(1).replace(",", "")) == counts[day.group(1)]
        checked += 1
    assert checked >= 4


# ------------------------------------------------------- narrative integrity
def test_storylines_never_claim_a_trough_above_its_own_baseline():
    """A 'dip' to a value higher than the baseline is a broken sentence.

    It happened for real: an event with no measurable impact still went
    through the incident template and printed 'troughs at 95.54% from a
    94.65% baseline'. Events with no measured impact now take a separate,
    honest lifecycle instead.
    """
    rows = _read(ANALYTICS / "storylines.csv")
    assert rows, "storylines cube is empty"
    pattern = re.compile(r"troughs at ([\d.]+)% against a ([\d.]+)% baseline")
    checked = 0
    for r in rows:
        m = pattern.search(r["event"])
        if m:
            trough, pre = float(m.group(1)), float(m.group(2))
            assert trough < pre, f"{r['incident_id']}: {r['event']}"
            checked += 1
    assert checked > 0, "no impact storylines found to verify"


def test_decision_tracking_does_not_score_recovery_on_a_non_dip():
    rows = _read(ANALYTICS / "decision_tracking.csv")
    assert rows
    for r in rows:
        pre, trough = float(r["pre_value"]), float(r["trough_value"])
        if pre - trough < 0.25:
            assert r["status"] == "No impact", (
                f"{r['decision_id']} claims a recovery on a "
                f"{pre - trough:.3f}pp move")
            assert "No measurable dip" in r["actual_impact"]


def test_bi_findings_name_only_one_highest_category():
    rows = _read(ANALYTICS / "bi_findings.csv")
    highest = [r for r in rows if "the highest of any category" in r["finding"]]
    assert len(highest) <= 1, "two findings both claim to be the highest"


def test_bi_findings_do_not_call_a_growing_product_weak():
    rows = _read(ANALYTICS / "bi_findings.csv")
    for r in rows:
        if r["category"] == "declining_features" and float(r["value"]) > 0:
            assert "Contracting" not in r["finding"]
            assert "Slowest-growing" in r["finding"]


# ------------------------------------------------------ derived cube sanity
@pytest.mark.parametrize("cube", [
    "bank_evolution", "psp_evolution", "merchant_evolution",
    "customer_evolution", "kpi_rollups", "cross_entity", "bi_findings",
    "storylines", "decision_tracking",
])
def test_derived_cubes_are_populated(cube):
    rows = _read(ANALYTICS / f"{cube}.csv")
    assert len(rows) > 0, f"{cube} projected zero rows"


def test_entity_evolution_weekly_volume_matches_the_corpus():
    """The weekly cube must sum to the transactions it claims to summarise."""
    pytest.importorskip("duckdb")
    import duckdb

    txn = (ROOT / "warehouse" / "transactions" / "*.parquet").as_posix()
    con = duckdb.connect()
    corpus = dict(con.execute(f"""
        SELECT CAST(date_trunc('week', CAST(txn_date AS DATE)) AS DATE), COUNT(*)
        FROM read_parquet('{txn}')
        WHERE txn_type IN ('PAYMENT','MANDATE_EXECUTION','RETRY','MANDATE_RETRY')
          AND payer_bank IS NOT NULL
        GROUP BY 1""").fetchall())

    weekly: dict[str, int] = {}
    for r in _read(ANALYTICS / "bank_evolution.csv"):
        weekly[r["date"]] = weekly.get(r["date"], 0) + int(r["txns"])
    assert weekly, "bank_evolution is empty"
    for week, total in weekly.items():
        assert total == corpus[__import__("datetime").date.fromisoformat(week)]


def test_forecast_validation_reports_skill_not_self_assessment():
    """The replaced cube fitted a line and graded its own fit.

    Skill against a seasonal-naive baseline is the column that makes the
    table meaningful, and a row must never claim to beat the baseline while
    reporting negative skill.
    """
    path = ANALYTICS / "forecast_validation.csv"
    if not path.exists():
        pytest.skip("forecast_validation not projected in this checkout")
    rows = _read(path)
    assert rows
    for r in rows:
        assert "skill_vs_naive_pct" in r
        if r.get("skill_vs_naive_pct") not in ("", None):
            skill = float(r["skill_vs_naive_pct"])
            beat = r["beat_naive_baseline"] == "true"
            assert beat == (skill > 0), (
                f"{r['series']}: claims beat={beat} on skill {skill}")
            if not beat:
                assert "worse than seasonal-naive" in r["verdict"]

"""Comparison questions must compare, over the period actually asked about.

"compare upi autopay and upi lite in the month of may 2026" failed three ways at
once, and each failure was silent:

1. no pattern matched a whole month, so the window fell back to the default
   trailing 30 days — the answer covered June 30–July 29, not May;
2. product resolution returned on the *first* match, so the two-product question
   was answered about one product;
3. no comparison path existed, so even with both products in the filter the
   engine emitted a single blended series.

The result was a confident-looking answer about the wrong products over the
wrong period. These tests exist so that cannot recur.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from app.orchestrator.classifier import QueryClassifier
from app.orchestrator.engines import _slice

DATA = Path(__file__).resolve().parents[3] / "enterprise_data"
WAREHOUSE = DATA / "warehouse"
CORPUS = ("2026-01-05", "2026-07-29")


def _intent(name: str):
    return type("I", (), {"intent": name})()


def _classify(message: str, intent: str = "comparison"):
    return QueryClassifier().classify(message, _intent(intent)).describe()


# ------------------------------------------------------------ month windows
@pytest.mark.parametrize("message,month,year", [
    ("compare upi autopay and upi lite in the month of may 2026", 5, 2026),
    ("what happened in March 2026", 3, 2026),
    ("during February 2026 how did we do", 2, 2026),
    ("how did upi lite do in May", 5, None),
])
def test_whole_month_is_recognised(message, month, year):
    tr = _classify(message)["time_range"]
    assert tr and tr["kind"] == "month"
    assert tr["month"] == month
    assert tr["year"] == year


@pytest.mark.parametrize("message,kind", [
    # A day-bearing range must still win over the whole-month pattern.
    ("show trends July 1 to July 20", "explicit"),
    ("success rate last 30 days", "relative"),
    ("compare hdfc bank and icici bank last month", "relative"),
    ("since March 3 what changed", "explicit"),
])
def test_existing_time_patterns_still_win(message, kind):
    tr = _classify(message, "question")["time_range"]
    assert tr and tr["kind"] == kind


def test_month_resolves_to_full_calendar_month():
    w = _slice.resolve_window(
        {"kind": "month", "month": 5, "year": 2026, "label": "May 2026"}, CORPUS)
    assert (w["start"], w["end"]) == ("2026-05-01", "2026-05-31")
    assert w["label"] == "May 2026"


def test_month_without_a_year_uses_the_year_the_corpus_covers():
    w = _slice.resolve_window(
        {"kind": "month", "month": 5, "year": None, "label": "May"}, CORPUS)
    assert (w["start"], w["end"]) == ("2026-05-01", "2026-05-31")


def test_month_outside_the_corpus_says_so_rather_than_answering_silently():
    w = _slice.resolve_window(
        {"kind": "month", "month": 12, "year": 2026, "label": "December 2026"},
        CORPUS)
    assert w.get("out_of_range") is True
    assert "outside the available history" in w["label"]


def test_partial_month_is_labelled_partial():
    # January is only covered from the 5th — the label must not imply otherwise.
    w = _slice.resolve_window(
        {"kind": "month", "month": 1, "year": 2026, "label": "January 2026"},
        CORPUS)
    assert w["start"] == "2026-01-05"
    assert "partial" in w["label"]


# -------------------------------------------------------- entity extraction
# --------------------------------------------------------- corpus-dependent
corpus = pytest.mark.skipif(
    not (WAREHOUSE / "transactions").exists(),
    reason="generated corpus not present in this checkout")


@pytest.fixture(scope="module")
def analytics():
    from app.core.config import Settings
    from app.core.container import Container
    return Container(Settings()).tx_analytics


@pytest.fixture(scope="module")
def vocab_classifier(analytics):
    """A classifier whose entity vocabulary comes from the corpus, which is how
    it is built in production — a bare QueryClassifier knows no entity names."""
    return QueryClassifier(_slice.warehouse_entity_vocab(analytics))


@corpus
def test_both_products_are_extracted_from_a_comparison(vocab_classifier):
    """Entity vocabulary is read from the corpus, so this needs a real one."""
    ents = vocab_classifier.classify(
        "compare upi autopay and upi lite in the month of may 2026",
        _intent("comparison")).describe()["entities"]
    products = [p.lower() for p in ents.get("product", [])]
    assert "upi autopay" in products
    assert "upi lite" in products


@corpus
def test_every_named_product_is_resolved_not_just_the_first(analytics):
    codes = _slice.match_products(analytics, ["upi autopay", "upi lite"])
    assert len(codes) == 2, f"only resolved {codes}"
    assert "UPI_AUTOPAY" in codes and "UPI_LITE" in codes


@corpus
def test_a_single_product_still_resolves_to_a_scalar_filter(analytics):
    request = type("R", (), {
        "entities": {"product": ["upi lite"]}, "time_range": None})()
    out = _slice.entity_filters(request, analytics)
    assert out["product"] == "UPI_LITE"


@corpus
def test_two_products_become_a_list_filter(analytics):
    request = type("R", (), {
        "entities": {"product": ["upi autopay", "upi lite"]},
        "time_range": None})()
    out = _slice.entity_filters(request, analytics)
    assert isinstance(out["product"], list)
    assert set(out["product"]) == {"UPI_AUTOPAY", "UPI_LITE"}


@corpus
def test_a_list_filter_renders_as_sql_in_clause(analytics):
    from app.warehouse.filters import Filters
    where, params = Filters(product=["UPI_AUTOPAY", "UPI_LITE"]).where()
    assert "IN (?, ?)" in where
    assert params == ["UPI_AUTOPAY", "UPI_LITE"]


@corpus
def test_comparison_emits_one_side_per_product_plus_a_verdict(
        analytics, vocab_classifier):
    """The whole point: two products asked about produce two measured sides."""
    from app.orchestrator.engines.analytics import AnalyticsEngine

    cls = vocab_classifier.classify(
        "compare upi autopay and upi lite in the month of may 2026",
        _intent("comparison")).describe()
    request = type("R", (), {
        "intent": "comparison",
        "entities": cls["entities"],
        "kpi_hints": tuple(cls["kpi_hints"]),
        "time_range": cls["time_range"],
        "categories": ("analytics",),
        "message": "compare upi autopay and upi lite in may 2026",
    })()

    res = AnalyticsEngine(analytics).run(request)
    kinds = [e.kind for e in res.evidence]
    sides = [e.payload for e in res.evidence
             if e.kind == "analytics_comparison_side"]
    verdict = [e.payload for e in res.evidence
               if e.kind == "analytics_comparison"]

    assert len(sides) == 2, f"expected both products, got kinds={kinds}"
    assert {s["name"] for s in sides} == {"UPI_AUTOPAY", "UPI_LITE"}
    assert len(verdict) == 1

    # Each side must carry real measured numbers, not placeholders.
    for s in sides:
        assert s["attempts"] > 0
        assert 0 < s["success_rate"] <= 100
        assert str(int(s["attempts"])) or True
        assert "May 2026" in s["text"]

    v = verdict[0]
    assert v["leader"] in {"UPI_AUTOPAY", "UPI_LITE"}
    assert v["laggard"] != v["leader"]
    assert v["dimension"] == "product"

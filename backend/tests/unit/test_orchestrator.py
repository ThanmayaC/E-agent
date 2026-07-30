"""Enterprise AI Orchestrator (V11) — classification, engines, routing.

The orchestrator's job is to stop sending every question to RAG. These tests
pin the behaviours that matter: a KPI-over-time question routes to the
analytics engine and comes back with a real windowed trend (the "no evidence
found" bug), a forecast question reaches the forecaster, an ML question reaches
the models, a root-cause question fans out to several engines, and every engine
failure degrades to an honest status rather than breaking the answer.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from app.copilot.evidence import Evidence
from app.orchestrator.base import Engine, EngineRequest
from app.orchestrator.classifier import QueryClassifier
from app.orchestrator.engines.analytics import AnalyticsEngine
from app.orchestrator.engines.knowledge import _is_data_dump
from app.orchestrator.orchestrator import EnterpriseOrchestrator
from app.orchestrator.router import EngineRouter
from app.warehouse import TransactionAnalytics, get_warehouse

_REPO_ROOT = Path(__file__).resolve().parents[3]
_WAREHOUSE_ROOT = _REPO_ROOT / "enterprise_data" / "warehouse"


@dataclass
class _Intent:
    intent: str = "question"
    subject: str = ""


# --------------------------------------------------------------- classifier
def _cls(vocab=None):
    return QueryClassifier(vocab or {"bank": ["ICICI Bank", "HDFC Bank"]})


def test_time_range_question_routes_to_analytics_not_rag():
    c = _cls()
    r = c.classify("Show UPI trends from July 1 to July 20", _Intent())
    assert "analytics" in r.categories
    assert r.primary == "analytics"
    assert r.time_range and r.time_range["kind"] == "explicit"
    assert r.time_range["start_md"] == (7, 1)
    assert r.time_range["end_md"] == (7, 20)


def test_forecast_question_reaches_forecast_engine():
    c = _cls()
    r = c.classify("Predict next month's transaction volume", _Intent("forecast"))
    assert "forecast" in r.categories
    assert "Transaction Volume (Mn)" in r.kpi_hints


def test_ml_question_reaches_ml_engine():
    c = _cls()
    r = c.classify("Which merchants are at risk of churn?", _Intent())
    assert "ml" in r.categories


def test_root_cause_is_hybrid():
    c = _cls()
    r = c.classify("Why are technical declines increasing at ICICI Bank?",
                   _Intent("explanation"))
    assert "analytics" in r.categories
    assert "knowledge" in r.categories
    assert "ml" in r.categories
    assert r.hybrid is True
    assert r.entities.get("bank") == ["icici bank"]


def test_relative_and_iso_ranges_parse():
    c = _cls()
    assert c.classify("success rate last 30 days", _Intent()).time_range[
        "token"] == "last_ndays"
    iso = c.classify("declines between 2026-07-01 and 2026-07-20", _Intent())
    assert iso.time_range["start_iso"] == "2026-07-01"


def test_pure_lookup_does_not_force_ml_or_forecast():
    c = _cls()
    r = c.classify("How many active users do we have?", _Intent())
    assert "ml" not in r.categories
    assert "forecast" not in r.categories


# --------------------------------------------------------------- analytics
# These run against the real transaction warehouse (enterprise_data/warehouse)
# rather than a fake ecosystem double: the AnalyticsEngine was rewired to
# read TransactionAnalytics over raw transactions, so the only honest fixture
# is the actual corpus.
def _analytics() -> TransactionAnalytics:
    wh = get_warehouse(str(_WAREHOUSE_ROOT))
    assert wh.available, f"warehouse not found at {_WAREHOUSE_ROOT}"
    return TransactionAnalytics(wh)


def test_analytics_engine_computes_windowed_trend():
    eng = AnalyticsEngine(analytics=_analytics())
    req = EngineRequest(
        message="show trends July 1 to July 20", intent="question",
        categories=("analytics",),
        time_range={"kind": "explicit", "start_md": (7, 1),
                    "end_md": (7, 20), "label": "July 1 to July 20"})
    res = eng.timed(req)
    assert res.status == "ok"
    kinds = {e.kind for e in res.evidence}
    assert "analytics_kpi" in kinds
    # The real SQL run against the warehouse is reported for observability.
    assert "SELECT" in res.detail["sql"]
    assert res.detail["window"]["start"] == "2026-07-01"
    assert res.detail["window"]["end"] == "2026-07-20"
    sr = next(e for e in res.evidence
              if e.payload.get("kpi") == "success_rate")
    assert sr.payload["direction"] in ("up", "down", "flat")
    assert sr.payload["verdict"] in ("improving", "worsening", "steady")
    # And its numbers live in text, so the copilot validator can ground them.
    assert "%" in sr.payload["text"]


def test_analytics_engine_unavailable_without_data():
    eng = AnalyticsEngine(analytics=None)
    res = eng.timed(EngineRequest(message="trends", intent="question",
                                  categories=("analytics",)))
    assert res.status == "unavailable"
    assert res.ran is False


def test_analytics_grounds_every_daily_value_in_text():
    # A day-by-day narration must not be rejected: even though the aggregate
    # text only carries first/last/min/max/mean, every per-day value in the
    # structured ``series`` must still be groundable by Evidence.numbers().
    eng = AnalyticsEngine(analytics=_analytics())
    req = EngineRequest(
        message="trends", intent="question", categories=("analytics",),
        time_range={"kind": "explicit", "start_md": (7, 1),
                    "end_md": (7, 20), "label": "July 1 to July 20"})
    res = eng.run(req)
    sr = next(e for e in res.evidence
              if e.payload.get("kpi") == "success_rate")
    assert len(sr.payload["series"]) == 20
    ev = Evidence()
    ev.add(sr.kind, sr.id, sr.summary, sr.payload)
    known = ev.numbers()
    mid = next(p for p in sr.payload["series"] if p["date"] == "2026-07-10")
    assert round(mid["value"], 4) in known


# ------------------------------------------------------ data-dump filter
def test_data_dump_detected_and_narrative_kept():
    dump = ("Feature | squad | 01-Jul | 02-Jul | 03-Jul | 04-Jul | 05-Jul | "
            "06-Jul | 07-Jul | 08-Jul")
    assert _is_data_dump(dump) is True
    narrative = ("The Autopay incident on 2026-07-14 reduced success rate; "
                 "the RCA recommends a callback timeout increase.")
    assert _is_data_dump(narrative) is False


# ------------------------------------------------- evidence KPI grounding
def test_kpi_names_include_analytics_and_executive_kinds():
    ev = Evidence()
    ev.add("kpi", "k1", "x", {"name": "Total Transactions"})
    ev.add("executive_kpi", "k2", "x", {"name": "UPI Transactions (M/day)"})
    ev.add("analytics_kpi", "k3", "x", {"name": "Success Rate (%)"})
    names = ev.kpi_names()
    assert "upi transactions (m/day)" in names
    assert "success rate (%)" in names
    assert "total transactions" in names


# ------------------------------------------------------------ router/graph
class _Fake(Engine):
    def __init__(self, key, cats, boom=False, items=1):
        self.key = key
        self.label = key.title()
        self.categories = cats
        self._boom = boom
        self._items = items

    def run(self, request):
        if self._boom:
            raise RuntimeError("engine exploded")
        res = self._result()
        for i in range(self._items):
            res.add(self.key, f"{self.key}:{i}", f"{self.key} fact {i}",
                    {"text": f"{self.key} value {i}"})
        res.detail = {"ran": self.key}
        return res


def test_router_selects_only_relevant_engines():
    router = EngineRouter([_Fake("analytics", ("analytics",)),
                           _Fake("ml", ("ml",))], parallel=False)
    req = EngineRequest(message="q", intent="question",
                        categories=("analytics",))
    chosen = [e.key for e in router.select(req)]
    assert chosen == ["analytics"]


def test_router_falls_back_to_knowledge_when_nothing_matches():
    router = EngineRouter([_Fake("analytics", ("analytics",)),
                           _Fake("knowledge", ("knowledge",))], parallel=False)
    req = EngineRequest(message="q", intent="question", categories=("report",))
    assert [e.key for e in router.select(req)] == ["knowledge"]


def test_engine_error_becomes_status_not_exception():
    res = _Fake("ml", ("ml",), boom=True).timed(
        EngineRequest(message="q", intent="question", categories=("ml",)))
    assert res.status == "error"
    assert "exploded" in res.note


def test_orchestrator_merges_evidence_and_builds_graph():
    engines = [_Fake("analytics", ("analytics",), items=2),
               _Fake("knowledge", ("knowledge",), items=1),
               _Fake("ml", ("ml",), items=1)]
    router = EngineRouter(engines, parallel=True)
    orch = EnterpriseOrchestrator(_cls(), router)
    result = orch.run("Why are declines rising?", _Intent("explanation"))
    d = result.describe()
    assert d["evidence_added"] >= 2
    # The execution graph names the classify → route → engines → merge path.
    nodes = [n["node"] for n in d["graph"]]
    assert nodes[0] == "classify"
    assert "merge" == nodes[-1]
    assert any(n.startswith("engine:") for n in nodes)
    assert "analytics" in d["engines_run"]

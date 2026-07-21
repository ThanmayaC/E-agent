"""V2.4 Decision Intelligence: the Brain deciding, not just informing.

Unit tests drive the layer with fakes; the API tests boot the real app and
prove the executive surface answers. The layer must reuse what exists —
execution goes through the Decision Engine, memory through the
KnowledgeStore, and the Decision Graph is the Enterprise Knowledge Graph.
"""
from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone

import pytest

from app.knowledge.graph import EnterpriseKnowledgeGraph
from app.runtime.events import EventBus
from app.runtime.intelligence import DecisionIntelligence
from app.runtime.store import RuntimeStore


# ---------------------------------------------------------------- fakes
class FakeEngine:
    def __init__(self):
        self.decided = []

    def decide(self, recommendation, project_id="", action_kind="create_task",
               source=""):
        self.decided.append({"recommendation": recommendation,
                             "project_id": project_id, "source": source})
        return {"decision_id": f"dec_{len(self.decided)}",
                "queued_action_id": f"act_{len(self.decided)}"}

    def stats(self):
        return {"total": len(self.decided)}


class FakeKnowledge:
    def __init__(self):
        self.recorded_decisions = []
        self.learning_events = []
        self.meeting_decisions = []

    def record_decision(self, decision, context="", project_id="", source=""):
        self.recorded_decisions.append(decision)

    def record_learning_event(self, event, source="", project_id="",
                              details=None):
        self.learning_events.append(event)

    def decisions(self, limit=20):
        return self.meeting_decisions[:limit]


class FakeTasks:
    def __init__(self, items=None):
        self.items = items or []

    def tasks(self, status="", limit=100):
        return self.items[:limit]


class FakeDocuments:
    def __init__(self, docs=None):
        self.docs = docs or []

    def documents(self, category="", source="", limit=50):
        return [d for d in self.docs
                if not category or d.get("category") == category][:limit]


class FakePortfolio:
    def __init__(self, risks=None, projects=None):
        self._risks = risks or []
        self._projects = projects or []

    def overview(self):
        return {"risks": self._risks, "projects": self._projects,
                "opportunities": [], "historical_comparison": []}


@pytest.fixture
def layer(tmp_path):
    store = RuntimeStore(tmp_path / "runtime")
    bus = EventBus()
    engine = FakeEngine()
    knowledge = FakeKnowledge()
    graph = EnterpriseKnowledgeGraph(tmp_path)
    intelligence = DecisionIntelligence(
        store, bus, engine=engine, knowledge=knowledge, graph=graph,
        portfolio=FakePortfolio(), tasks=FakeTasks(),
        documents=FakeDocuments(), enabled=True, ttl_days=14)
    intelligence.test_bus = bus
    intelligence.test_engine = engine
    intelligence.test_knowledge = knowledge
    intelligence.test_graph = graph
    intelligence.test_store = store
    return intelligence


# ------------------------------------------------------------- lifecycle
def test_a_proposed_decision_carries_the_full_lifecycle_record(layer):
    record = layer.propose(
        "Investigate Merchant X", kind="investigation",
        reasoning="Revenue declining across three reports", priority=2,
        evidence_ids=["ev1", "ev2"], affected_products=["Payments"],
        affected_teams=["operations"], expected_impact="Recover revenue",
        owner="coo", project_id="p1")

    for field in ("decision_id", "priority", "confidence", "reasoning",
                  "evidence_ids", "affected_products", "affected_teams",
                  "expected_impact", "owner", "status", "dependencies",
                  "created_by", "created_at", "history"):
        assert field in record, f"lifecycle field {field} missing"
    assert record["status"] == "proposed"
    assert record["history"][0]["status"] == "proposed"
    assert record["confidence"] == 0.7  # 0.5 + 0.1 * 2 pieces of evidence


def test_an_equivalent_open_decision_is_never_proposed_twice(layer):
    assert layer.propose("Investigate Merchant X",
                         kind="investigation") is not None
    assert layer.propose("Investigate Merchant X",
                         kind="investigation") is None


def test_approval_executes_through_the_existing_decision_engine(layer):
    record = layer.propose("Escalate settlement failures", kind="escalation",
                           priority=1, evidence_ids=["ev1"])
    approved = layer.set_status(record["decision_id"], "approved", by="ceo")

    assert approved["status"] == "approved"
    assert layer.test_engine.decided, "the Decision Engine never saw it"
    linked = layer.get(record["decision_id"])
    assert linked["engine_decision_id"], "the two trails are not linked"
    assert linked["queued_action_id"]

    # The queue executes the action → the decision reaches its terminal state.
    layer.test_bus.publish("ActionExecuted",
                           {"action_id": linked["queued_action_id"]})
    assert layer.get(record["decision_id"])["status"] == "executed"


def test_every_transition_is_remembered_by_the_brain(layer):
    record = layer.propose("Recommend SOP review", kind="sop_review")
    layer.set_status(record["decision_id"], "rejected", by="coo",
                     note="Not this quarter")

    assert "Recommend SOP review" in layer.test_knowledge.recorded_decisions
    assert "decision_created" in layer.test_knowledge.learning_events
    assert "decision_rejected" in layer.test_knowledge.learning_events


def test_rejecting_an_unknown_status_is_refused(layer):
    record = layer.propose("Anything", kind="review")
    with pytest.raises(ValueError):
        layer.set_status(record["decision_id"], "vetoed")


def test_a_decided_decision_cannot_be_edited(layer):
    record = layer.propose("Investigate the anomaly", kind="investigation")
    layer.set_status(record["decision_id"], "approved")
    with pytest.raises(ValueError):
        layer.modify(record["decision_id"], action="Something else")


def test_editing_a_proposal_marks_it_modified_with_history(layer):
    record = layer.propose("Investigate the anomaly", kind="investigation")
    updated = layer.modify(record["decision_id"], by="coo", priority=1,
                           owner="ops-lead")
    assert updated["status"] == "modified"
    assert updated["priority"] == 1
    assert updated["owner"] == "ops-lead"
    assert updated["history"][-1]["status"] == "modified"


# -------------------------------------------------------- decision graph
def test_decisions_become_nodes_in_the_enterprise_graph(layer):
    record = layer.propose("Fix churn in Payments", kind="mitigation",
                           affected_products=["Payments"])
    node = layer.test_graph.neighbors(f"decision:{record['decision_id']}")
    assert node["node"] is not None, "the decision never reached the graph"
    assert node["node"]["kind"] == "decision"
    kinds = {r["kind"] for r in node["relations"]}
    assert "affects" in kinds, "the affects → product edge is missing"


# --------------------------------------------------------------- ranking
def test_ranking_puts_urgent_evidenced_decisions_first(layer):
    low = layer.propose("Tidy the wiki", kind="knowledge", priority=6)
    high = layer.propose("Escalate the settlement failure spike",
                         kind="escalation", priority=1,
                         evidence_ids=["e1", "e2", "e3"],
                         strategic_weight=0.9)
    ranked = layer.rank(5)
    assert ranked[0]["decision_id"] == high["decision_id"]
    assert ranked[-1]["decision_id"] == low["decision_id"]
    assert set(ranked[0]["factors"]) == {"impact", "urgency", "confidence",
                                         "evidence", "history", "risk",
                                         "strategic"}


def test_history_teaches_the_ranker_without_retraining(layer):
    # Two rejected escalations lower the historical factor for the kind.
    for i in range(2):
        r = layer.propose(f"Escalate incident {i}", kind="escalation")
        layer.set_status(r["decision_id"], "rejected")
    fresh = layer.propose("Escalate incident new", kind="escalation")
    ranked = {r["decision_id"]: r for r in layer.rank(10)}
    assert ranked[fresh["decision_id"]]["factors"]["history"] < 0.5


# --------------------------------------------------- proactive detection
def test_repeated_rcas_recommend_an_sop_review(tmp_path):
    store = RuntimeStore(tmp_path / "rt")
    docs = FakeDocuments([
        {"category": "rca", "title": "RCA: Settlement failures in March",
         "document_id": "d1"},
        {"category": "rca", "title": "Settlement failures RCA (repeat)",
         "document_id": "d2"},
    ])
    layer = DecisionIntelligence(store, EventBus(), engine=None,
                                 knowledge=None, documents=docs)
    outcome = layer.observe()
    assert outcome["repeated_rcas"]["signals"] == 1
    kinds = {d["kind"] for d in layer.decisions()}
    assert "sop_review" in kinds


def test_meeting_decisions_without_tasks_get_follow_ups(tmp_path):
    store = RuntimeStore(tmp_path / "rt")
    knowledge = FakeKnowledge()
    knowledge.meeting_decisions = [
        {"decision": "Expand to the Gulf market", "context": "Q3 board"}]
    layer = DecisionIntelligence(store, EventBus(), engine=None,
                                 knowledge=knowledge, tasks=FakeTasks([]))
    layer.observe()
    actions = [d["action"] for d in layer.decisions()]
    assert any("Expand to the Gulf market" in a for a in actions)


def test_overdue_action_items_are_chased(tmp_path):
    store = RuntimeStore(tmp_path / "rt")
    yesterday = (datetime.now(timezone.utc) - timedelta(days=1)).date()
    tasks = FakeTasks([{"title": "Send the audit response",
                        "status": "pending",
                        "due_date": yesterday.isoformat()}])
    layer = DecisionIntelligence(store, EventBus(), engine=None,
                                 knowledge=None, tasks=tasks)
    outcome = layer.observe()
    assert outcome["missed_action_items"]["signals"] == 1


def test_live_events_become_candidate_decisions(layer):
    layer.test_bus.publish("RiskIncreased",
                           {"count": 9, "previous": 3, "increase": 6,
                            "top_risk": "Settlement failures increasing"})
    kinds = {d["kind"] for d in layer.decisions()}
    assert "escalation" in kinds


def test_stale_proposals_expire(tmp_path):
    store = RuntimeStore(tmp_path / "rt")
    layer = DecisionIntelligence(store, EventBus(), engine=None,
                                 knowledge=None, ttl_days=14)
    record = layer.propose("Old idea nobody answered", kind="review")
    with store.mutate("decision_records") as records:
        records[0]["created_at"] = (
            datetime.now(timezone.utc) - timedelta(days=30)).isoformat()
    layer.observe()
    assert layer.get(record["decision_id"])["status"] == "expired"


def test_the_sweep_survives_a_failing_detector(tmp_path):
    class ExplodingDocuments:
        def documents(self, **kwargs):
            raise RuntimeError("source offline")
    layer = DecisionIntelligence(RuntimeStore(tmp_path / "rt"), EventBus(),
                                 engine=None, knowledge=None,
                                 documents=ExplodingDocuments())
    outcome = layer.observe()
    assert outcome["repeated_rcas"] == {"error": "detector failed"}
    assert "expired" in outcome, "the sweep stopped at the failure"


def test_disabled_layer_neither_observes_nor_proposes(tmp_path):
    layer = DecisionIntelligence(RuntimeStore(tmp_path / "rt"), EventBus(),
                                 engine=None, knowledge=None, enabled=False)
    assert layer.observe() == {"skipped": "decision intelligence disabled"}


# ------------------------------------------------------ reports and brief
def test_the_daily_report_measures_decision_effectiveness(layer):
    a = layer.propose("Approve me", kind="escalation", evidence_ids=["e"])
    layer.set_status(a["decision_id"], "approved")
    layer.test_bus.publish(
        "ActionExecuted",
        {"action_id": layer.get(a["decision_id"])["queued_action_id"]})
    b = layer.propose("Reject me", kind="review")
    layer.set_status(b["decision_id"], "rejected")

    report = layer.report("daily")
    assert report["by_status"]["executed"] == 1
    assert report["by_status"]["rejected"] == 1
    assert report["effectiveness"]["execution_rate"] == 0.5
    assert "escalation" in report["effectiveness"]["success_by_kind"]
    with pytest.raises(ValueError):
        layer.report("hourly")


def test_the_brief_leads_with_what_requires_attention(layer):
    layer.propose("Escalate the outage", kind="escalation", priority=1)
    brief = layer.brief()
    for section in ("top_decisions", "recommended_actions", "critical_risks",
                    "pending_approvals", "recent_changes", "stats"):
        assert section in brief
    assert brief["top_decisions"], "the top decision is missing"
    assert brief["recommended_actions"][0]["action"] == "Escalate the outage"


# ------------------------------------------------------------ API surface
@pytest.fixture(scope="module")
def client(tmp_path_factory):
    os.environ["EDIP_DATA_DIR"] = str(tmp_path_factory.mktemp("v24_data"))
    os.environ["EDIP_LLM_PROVIDER"] = "mock"
    from app.core import config, container
    config.get_settings.cache_clear()
    container.get_container.cache_clear()
    from fastapi.testclient import TestClient
    from app.main import create_app
    with TestClient(create_app()) as c:
        yield c
    config.get_settings.cache_clear()
    container.get_container.cache_clear()


def test_every_intelligence_endpoint_answers(client):
    for path in ("/api/v1/runtime/intelligence",
                 "/api/v1/runtime/intelligence/decisions",
                 "/api/v1/runtime/intelligence/recommendations",
                 "/api/v1/runtime/intelligence/signals",
                 "/api/v1/runtime/intelligence/brief",
                 "/api/v1/runtime/intelligence/reports/daily",
                 "/api/v1/runtime/intelligence/reports/weekly",
                 "/api/v1/runtime/intelligence/reports/monthly"):
        assert client.get(path).status_code == 200, path


def test_the_decision_lifecycle_over_the_api(client):
    created = client.post("/api/v1/runtime/intelligence/decisions", json={
        "action": "Investigate Merchant X's revenue decline",
        "kind": "investigation", "priority": 2,
        "reasoning": "Three consecutive weekly declines",
        "evidence_ids": ["ev1"], "affected_teams": ["operations"],
    })
    assert created.status_code == 201
    decision_id = created.json()["decision_id"]

    # Duplicates are refused while the decision is open.
    assert client.post("/api/v1/runtime/intelligence/decisions", json={
        "action": "Investigate Merchant X's revenue decline",
        "kind": "investigation"}).status_code == 409

    approved = client.patch(
        f"/api/v1/runtime/intelligence/decisions/{decision_id}",
        json={"status": "approved", "by": "executive"}).json()
    assert approved["status"] == "approved"
    assert approved["history"][-1]["by"] == "executive"
    # The PATCH response itself must carry the linkage — not only a later GET.
    assert approved["engine_decision_id"], \
        "approval did not reach the Decision Engine"
    assert approved["queued_action_id"]

    fetched = client.get(
        f"/api/v1/runtime/intelligence/decisions/{decision_id}").json()
    assert fetched["engine_decision_id"] == approved["engine_decision_id"]


def test_the_runtime_status_reports_the_new_layer(client):
    body = client.get("/api/v1/runtime").json()
    assert body["decision_intelligence"]["enabled"] is True


def test_the_observation_sweep_runs_on_demand(client):
    body = client.post("/api/v1/runtime/intelligence/observe")
    assert body.status_code == 200
    assert "expired" in body.json()

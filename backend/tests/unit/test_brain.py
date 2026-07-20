"""Enterprise Brain — continuous learning, versioning, memory sync,
enterprise context, and runtime startup."""
from __future__ import annotations

import pytest

from app.brain import EnterpriseBrain, EnterpriseContextBuilder
from app.knowledge.engine import KnowledgeEngine
from app.knowledge.graph import EnterpriseKnowledgeGraph
from app.knowledge.store import KnowledgeStore
from app.memory.manager import MemoryManager
from app.memory.sync import MemorySynchronizer
from app.repositories.artifact_store import ArtifactStore

PID = "proj_test01"

ARTIFACTS = {
    "profiles": [{"name": "transactions", "entity": "Transaction",
                  "dataset_id": "txns_ab12cd", "row_count": 400,
                  "column_count": 6, "confidence": 0.9}],
    "semantic_layer": [
        {"column": "Cust_ID", "canonical_name": "customer_id",
         "concept": "Customer", "confidence": 0.92},
        {"column": "mystery_col", "canonical_name": "unknown_thing",
         "concept": "Unknown", "confidence": 0.30},  # below learn threshold
    ],
    "kpis": [{"name": "Total Revenue", "expression": "SUM(Txn_Value)",
              "unit": "USD", "confidence": 0.9, "concept": "Revenue"}],
    "relationships": [{"from_dataset": "txns_ab12cd", "to_dataset": "cust_x1",
                       "from_column": "Cust_ID", "to_column": "customer_no",
                       "confidence": 0.85}],
    "ai_report": {
        "status": "ok",
        "key_insights": [
            {"title": "Revenue grew 12% month over month",
             "statement_type": "fact", "verification": "evidence_verified",
             "confidence": 0.9, "evidence_ids": ["kpi:total_revenue"]},
            {"title": "Unverified speculation", "statement_type": "hypothesis",
             "verification": "unsupported", "evidence_ids": []},
        ],
        "recommendations": [{"action": "Investigate failed transactions",
                             "priority": 1, "evidence_ids": ["sig:failures"]}],
        "priority_actions": ["Investigate failed transactions"],
        "risks": [{"risk": "Failure rate is rising", "severity": "high"},
                  {"risk": "Minor gap", "severity": "low"}],
        "opportunities": [{"opportunity": "North region growth",
                           "impact": "high"}],
    },
    "understanding": {"questions": [
        {"question": "Which column is revenue?", "answer": "Txn_Value",
         "answered": True, "signature": "sig-rev"}]},
    "business_context": {"kpis": [{"id": "kpi:total_revenue",
                                   "name": "Total Revenue"}],
                         "executive_metrics": {"health_score": 71.0}},
}


@pytest.fixture()
def brain(tmp_path):
    store = ArtifactStore(tmp_path / "projects")
    knowledge = KnowledgeStore(tmp_path / "knowledge")
    graph = EnterpriseKnowledgeGraph(tmp_path / "knowledge")
    engine = KnowledgeEngine(knowledge, graph)
    memory = MemoryManager(store, knowledge)
    b = EnterpriseBrain(
        store=store, memory=memory, knowledge=knowledge, graph=graph,
        engine=engine, synchronizer=MemorySynchronizer(memory),
        context_builder=EnterpriseContextBuilder(store, knowledge, graph))
    store.save(PID, "state", {"project_id": PID, "name": "Fintech P1",
                              "status": "ready"})
    for name, payload in ARTIFACTS.items():
        store.save(PID, name, payload)
    return b


# ------------------------------------------------------------------ startup
def test_startup_marks_brain_ready(brain):
    status = brain.startup()
    assert brain.state == "ready"
    assert status["state"] == "ready"
    assert all(c["ok"] for c in status["checks"].values())
    assert set(status["checks"]) >= {"knowledge_store", "knowledge_graph",
                                     "learning_history", "business_rules",
                                     "clarifications", "memory"}


# ---------------------------------------------------------------- learning
def test_learning_pipeline_builds_knowledge_and_graph(brain):
    summary = brain.learn_after_analysis(PID)
    k = brain.knowledge

    # terminology from KPIs; entity from dataset; alias from semantics
    assert k.resolve_term("Total Revenue") is not None
    assert k.resolve_schema_alias("Cust_ID") == "customer_id"
    assert k.resolve_schema_alias("mystery_col") is None  # low confidence
    # only evidence-verified insights become knowledge
    insights = [i["insight"] for i in k.insights(10)]
    assert "Revenue grew 12% month over month" in insights
    assert not any("speculation" in i.lower() for i in insights)
    assert any(r["action"] == "Investigate failed transactions"
               for r in k.recommendations(10))
    # graph grew: project, dataset, concept, kpi, report, insight nodes
    stats = brain.graph.stats()
    assert stats["node_count"] >= 6
    assert stats["edge_count"] >= 5
    assert summary["knowledge"]["kpis"] == 1
    # learning memory recorded the pipeline execution
    events = k.learning_history(10)
    assert events and events[-1]["event"] == "continuous_learning_pipeline"
    assert events[-1]["project_id"] == PID


def test_learning_is_idempotent(brain):
    first = brain.learn_after_analysis(PID)
    before = brain.knowledge.stats()
    second = brain.learn_after_analysis(PID)
    after = brain.knowledge.stats()
    # re-learning the same analysis adds no duplicate knowledge
    for section in ("terminology", "schema_aliases", "insights",
                    "recommendations", "strategic_insights"):
        assert after[section] == before[section], section
    assert second["knowledge"]["aliases"] == 0  # already known
    assert first["knowledge"]["aliases"] == 1


# -------------------------------------------------------------- versioning
def test_knowledge_versioning_preserves_history(brain):
    k = brain.knowledge
    k.add_term("GMV", "Gross merchandise value", ["gross_value"],
               added_by="user", project_id=PID)
    k.add_term("GMV", "Gross merchandise value", ["gmv_total"],
               added_by="user", project_id="proj_other")
    versions = k.versions("term:gmv")
    assert [v["version"] for v in versions] == [1, 2]
    assert versions[0]["action"] == "created"
    assert versions[1]["action"] == "updated"
    assert "previous" in versions[1]          # history preserved, not lost
    assert versions[1]["project_id"] == "proj_other"
    assert all(v["recorded_at"] and v["source"] for v in versions)
    # aliases merged, never overwritten
    assert set(k.resolve_term("GMV")["aliases"]) == {"gross_value", "gmv_total"}
    # journal is queryable as history
    assert any(h["key"] == "term:gmv" for h in k.history(50))


# ------------------------------------------------------- clarification reuse
def test_clarifications_are_never_asked_twice(brain):
    k = brain.knowledge
    k.remember_clarification("Which column represents revenue?", "Txn_Value",
                             signature="sig-abc", project_id=PID)
    recalled = k.find_clarification("Which column represents revenue?",
                                    signature="sig-abc")
    assert recalled and recalled["answer"] == "Txn_Value"
    # similar wording still recalls the same answer
    similar = k.find_clarification("Which column represents the revenue?")
    assert similar and similar["answer"] == "Txn_Value"


# --------------------------------------------------------------- memory sync
def test_memory_sync_feeds_strategic_memory(brain):
    result = brain.synchronizer.sync_after_analysis(PID, ARTIFACTS)
    assert result["strategic_insights_added"] == 2  # high risk + high opp
    texts = [s["insight"] for s in brain.memory.strategic_memory(10)]
    assert any("Failure rate is rising" in t for t in texts)
    assert any("North region growth" in t for t in texts)
    assert not any("Minor gap" in t for t in texts)  # low severity excluded
    # idempotent
    again = brain.synchronizer.sync_after_analysis(PID, ARTIFACTS)
    assert again["strategic_insights_added"] == 0
    stats = brain.synchronizer.stats()
    assert stats["strategic_memory"] == 2


# --------------------------------------------------------- enterprise context
def test_enterprise_context_unifies_brain_output(brain):
    brain.learn_after_analysis(PID)
    context = brain.build_enterprise_context(PID)
    # superset of the business context: facts and evidence ids intact
    assert context["kpis"][0]["id"] == "kpi:total_revenue"
    assert context["executive_metrics"]["health_score"] == 71.0
    ent = context["enterprise"]
    assert "Fintech P1" in ent["business_objective"]
    assert ent["knowledge"]["terminology"]  # learned KPI terminology
    assert ent["memory"]["verified_insights"]
    assert ent["knowledge_graph"]["stats"]["node_count"] > 0
    # persisted as an artifact for the API
    assert brain.store.load(PID, "enterprise_context")["enterprise"]


def test_prompt_engine_consumes_only_enterprise_context(brain):
    from app.agents.prompt_generator import PromptGenerationAgent
    brain.learn_after_analysis(PID)
    context = brain.build_enterprise_context(PID)
    agent = PromptGenerationAgent(knowledge=brain.knowledge)
    prompt = agent.report_prompt(context)
    # the unified context is the single source — no duplicate knowledge block
    assert prompt.user.count("ENTERPRISE") == 1
    assert "Fintech P1" in prompt.user           # objective flows into prompt
    assert "business_objective" in prompt.user

"""Enterprise AI Operating Layer (Version 2.2) — registries, evaluation,
governance, memory lifecycle, workflow registry, and observability.

These are the operational layers *around* the Enterprise Brain. The tests
assert two things above all: that each layer is a catalogue/authority over
implementations that already exist (not a reimplementation), and that
disabling a layer returns the platform to V2.1 behaviour.
"""
from __future__ import annotations

import pytest

from app.agents.base import AgentRequest, AgentResult
from app.agents.registry import AgentDescriptor, AgentRegistry
from app.evaluation import EvaluationInput, EvaluationPipeline
from app.evaluation.evaluators import build_evaluators
from app.governance import GovernanceLayer, KnowledgeAccessPolicy, Role
from app.memory.lifecycle import MemoryLifecycle
from app.prompts.registry import (
    PromptNotFound, PromptRegistry, PromptTemplate, PromptVariablesMissing,
)
from app.tools.registry import ToolPermissionDenied, ToolRegistry, ToolSpec
from app.tools.base import Tool
from app.workflows.registry import WorkflowRegistry, WorkflowSpec


# =====================================================================
#  Agent Registry
# =====================================================================
class _StubAgent:
    name = "stub"
    role = "does a stubbed thing"

    def run(self, request: AgentRequest) -> AgentResult:
        return AgentResult(status="ok", output={"echo": request.goal})

    def describe(self) -> dict:
        return {"name": self.name, "role": self.role}


def test_agent_registry_keeps_the_v1_contract():
    registry = AgentRegistry()
    agent = _StubAgent()
    registry.register(agent)
    assert registry.get("stub") is agent               # V1 get() unchanged
    assert any(d["name"] == "Stub" or d["id"] == "stub"
               for d in registry.describe())


def test_agent_registry_discovers_by_capability():
    registry = AgentRegistry()
    registry.register_capability(AgentDescriptor(
        agent_id="rca", name="RCA", capabilities=("summarize", "analyze"),
        brain_role="feeds", runner=lambda r: AgentResult("ok")))
    registry.register_capability(AgentDescriptor(
        agent_id="forecast", name="Forecast", capabilities=("forecast",),
        brain_role="feeds"))
    assert [d.agent_id for d in registry.find(capability="summarize")] == ["rca"]
    assert {d.agent_id for d in registry.find(brain_role="feeds")} == {"rca",
                                                                       "forecast"}


def test_agent_registry_executes_and_tracks_health():
    registry = AgentRegistry()
    registry.register_capability(AgentDescriptor(
        agent_id="ok", name="OK", capabilities=("summarize",),
        execution_policy="automatic",
        runner=lambda r: AgentResult(status="ok", output="done")))
    result = registry.execute("ok", AgentRequest(goal="go"), reason="automatic")
    assert result.status == "ok"
    assert registry.health("ok").state == "healthy"


def test_agent_registry_degrades_a_failing_agent():
    registry = AgentRegistry()

    def boom(_request):
        raise RuntimeError("kaboom")

    registry.register_capability(AgentDescriptor(
        agent_id="bad", name="Bad", capabilities=("analyze",), runner=boom))
    for _ in range(3):
        assert registry.execute("bad", AgentRequest(goal="x")).status == "failed"
    assert registry.health("bad").state == "unavailable"
    assert "bad" in registry.status()["degraded"]


def test_agent_execution_policy_forbids_automatic_on_demand_runs():
    registry = AgentRegistry()
    registry.register_capability(AgentDescriptor(
        agent_id="manual", name="Manual", capabilities=("analyze",),
        execution_policy="on_demand", runner=lambda r: AgentResult("ok")))
    auto = registry.execute("manual", AgentRequest(goal="x"), reason="automatic")
    assert auto.status == "unavailable"
    assert registry.execute("manual", AgentRequest(goal="x"),
                            reason="manual").status == "ok"


def test_a_catalogue_entry_without_a_runner_is_not_a_fault():
    registry = AgentRegistry()
    registry.register_capability(AgentDescriptor(
        agent_id="declared", name="Declared", capabilities=("analyze",)))
    assert registry.health("declared").state == "catalogue"
    assert registry.status()["degraded"] == []
    assert "declared" in registry.status()["catalogue_only"]


def test_agent_registry_rejects_unknown_policies():
    with pytest.raises(ValueError, match="execution policy"):
        AgentDescriptor(agent_id="x", name="X", execution_policy="whenever")
    with pytest.raises(ValueError, match="capabilities"):
        AgentDescriptor(agent_id="x", name="X", capabilities=("teleport",))


# =====================================================================
#  Tool Registry
# =====================================================================
class _EchoTool(Tool):
    name = "echo"
    description = "echoes"

    def run(self, *, text: str) -> str:
        return text


def test_tool_registry_keeps_the_v1_contract():
    registry = ToolRegistry()
    registry.register(_EchoTool())
    assert registry.run("echo", text="hi") == "hi"    # V1 run() unchanged


def test_tool_registry_validates_declared_inputs():
    registry = ToolRegistry()
    registry.register(_EchoTool(), ToolSpec(
        tool_id="echo", capability="read", inputs={"text": "string"},
        required=("text",), permissions=("read_project",)))
    from app.tools.registry import ToolInputInvalid
    with pytest.raises(ToolInputInvalid, match="missing required"):
        registry.run("echo")
    with pytest.raises(ToolInputInvalid, match="unknown input"):
        registry.run("echo", text="hi", bogus=1)


def test_tool_registry_finds_by_capability_and_agent():
    registry = ToolRegistry()
    registry.register(_EchoTool(), ToolSpec(
        tool_id="echo", capability="read", supported_agents=("report_agent",),
        inputs={"text": "string"}, permissions=("read_project",)))
    assert [s.tool_id for s in registry.find(capability="read")] == ["echo"]
    assert registry.find(agent_id="report_agent")
    assert registry.find(agent_id="other") == []


def test_tool_registry_records_execution_status():
    registry = ToolRegistry()
    registry.register(_EchoTool(), ToolSpec(
        tool_id="echo", capability="read", inputs={"text": "string"},
        permissions=("read_project",)))
    registry.run("echo", text="hi")
    status = registry.status_of("echo")
    assert status.calls == 1 and status.status == "ready"


def test_tool_registry_enforces_governance():
    governance = GovernanceLayer(default_role="manager")   # cannot write
    registry = ToolRegistry(governance=governance)
    registry.register(_EchoTool(), ToolSpec(
        tool_id="echo", capability="draft", inputs={"text": "string"},
        permissions=("draft_external",)))
    with pytest.raises(ToolPermissionDenied):
        registry.run_as("communication_agent", "echo", text="hi")


# =====================================================================
#  Prompt Registry
# =====================================================================
def test_prompt_registry_loads_every_domain():
    registry = PromptRegistry()
    status = registry.status()
    assert status["total"] >= 12
    # The constitutional prompt must be present and governed.
    narrator = registry.get("reports.evidence_narrator")
    assert narrator.governed and "EVIDENCE CONTRACT" in narrator.template


def test_prompt_rendering_requires_declared_variables():
    registry = PromptRegistry(load_defaults=False)
    registry.register(PromptTemplate(
        prompt_id="reports.demo", domain="reports",
        template="Hello {name}, your score is {score}."))
    assert registry.render("reports.demo", name="Al", score=9) \
        == "Hello Al, your score is 9."
    with pytest.raises(PromptVariablesMissing):
        registry.render("reports.demo", name="Al")


def test_prompt_variables_are_derived_from_the_template():
    template = PromptTemplate(prompt_id="copilot.x", domain="copilot",
                              template="A {one} and {two}.")
    assert set(template.variables) == {"one", "two"}


def test_prompt_registry_versions_do_not_overwrite():
    registry = PromptRegistry(load_defaults=False)
    registry.register(PromptTemplate(prompt_id="rca.x", domain="rca",
                                     template="v1", version=1))
    registry.register(PromptTemplate(prompt_id="rca.x", domain="rca",
                                     template="v2", version=2))
    assert registry.get("rca.x").version == 2
    assert registry.get("rca.x", version=1).template == "v1"
    assert len(registry.versions("rca.x")) == 2


def test_prompt_registry_rejects_a_silent_rewrite():
    registry = PromptRegistry(load_defaults=False)
    registry.register(PromptTemplate(prompt_id="sop.x", domain="sop",
                                     template="original", version=1))
    with pytest.raises(ValueError, match="already exists"):
        registry.register(PromptTemplate(prompt_id="sop.x", domain="sop",
                                         template="changed", version=1))


def test_unknown_prompt_raises():
    with pytest.raises(PromptNotFound):
        PromptRegistry().get("nonexistent.prompt")


def test_no_prompt_remains_embedded_in_the_prompt_agent():
    """The V2.2 contract: prompts come from the registry, not the module."""
    from app.agents.prompt_generator import PromptGenerationAgent
    agent = PromptGenerationAgent()
    prompt = agent.report_prompt({"kpis": [{"id": "k"}], "signals": [],
                                  "schema": []})
    # The system prompt must be the one the registry owns, verbatim.
    assert prompt.system == agent.prompts.render("reports.evidence_narrator")


# =====================================================================
#  Evaluation
# =====================================================================
@pytest.fixture()
def evidence():
    return [{"id": "kpi:rev", "kind": "kpi", "name": "Revenue", "value": 120000},
            {"id": "sig:up", "kind": "signal", "detail": "revenue up 12.0% QoQ"},
            {"id": "quality:overall", "kind": "quality", "score": 0.9}]


def test_good_report_is_accepted(evidence):
    pipeline = EvaluationPipeline()
    good = {"executive_summary": "Revenue reached 120000, up 12.0% QoQ.",
            "key_insights": [{"title": "Growth",
                              "evidence_ids": ["kpi:rev", "sig:up"]}],
            "recommendations": [{"action": "Sustain the plan",
                                 "evidence_ids": ["sig:up"]}],
            "confidence": 0.7}
    result = pipeline.evaluate(EvaluationInput(
        kind="report", output=good, evidence=evidence,
        produced_by="report_agent"))
    assert result.accepted, result.reasons()


def test_invented_numbers_and_citations_are_caught(evidence):
    pipeline = EvaluationPipeline()
    bad = {"executive_summary": "Revenue hit 987654 last quarter.",
           "key_insights": [{"title": "X", "evidence_ids": ["kpi:ghost"]}],
           "recommendations": [{"action": "act", "evidence_ids": []}],
           "confidence": 0.99}
    result = pipeline.evaluate(EvaluationInput(
        kind="report", output=bad, evidence=evidence))
    assert not result.accepted
    failed = {r.evaluator for r in result.failures}
    assert "grounding" in failed and "citation" in failed


def test_overconfidence_is_flagged(evidence):
    pipeline = EvaluationPipeline()
    out = {"answer": "Revenue is 120000.", "evidence_ids": ["kpi:rev"],
           "confidence": 0.99}
    result = pipeline.evaluate(EvaluationInput(
        kind="answer", output=out, evidence=[evidence[0]]))
    assert any(r.evaluator == "confidence_estimation" and not r.passed
               for r in result.results)


def test_policy_violation_rejects(evidence):
    pipeline = EvaluationPipeline()
    out = {"answer": "Revenue fell because customers churned.",
           "evidence_ids": ["kpi:rev"], "confidence": 0.5}
    result = pipeline.evaluate(EvaluationInput(
        kind="answer", output=out, evidence=evidence,
        business_rules=["Never attribute revenue change to churn"]))
    assert result.decision == "reject"
    assert any(r.evaluator == "policy_compliance" for r in result.failures)


def test_duplicate_output_is_rejected(evidence):
    pipeline = EvaluationPipeline()
    text = ("Revenue reached 120000 this quarter, an increase driven by the "
            "north region and sustained transaction volume across segments.")
    result = pipeline.evaluate(EvaluationInput(
        kind="summary", output=text, evidence=evidence,
        prior_outputs=[text]))
    assert result.decision == "reject"
    assert any(r.evaluator == "duplicate_detection" for r in result.failures)


def test_disabling_evaluation_accepts_everything(evidence):
    pipeline = EvaluationPipeline(enabled=False)
    bad = {"executive_summary": "invented 987654", "confidence": 0.99}
    result = pipeline.evaluate(EvaluationInput(kind="report", output=bad,
                                               evidence=[]))
    assert result.accepted and result.results == []


def test_a_broken_evaluator_never_fails_the_pipeline(evidence):
    class Broken:
        name = "broken"
        enabled = True

        def applies_to(self, request):
            return True

        def evaluate(self, request):
            raise RuntimeError("evaluator bug")

    pipeline = EvaluationPipeline(evaluators=[*build_evaluators(), Broken()])
    result = pipeline.evaluate(EvaluationInput(
        kind="answer", output={"answer": "Revenue is 120000",
                               "evidence_ids": ["kpi:rev"], "confidence": 0.6},
        evidence=evidence))
    # The broken evaluator is recorded but does not crash the panel.
    assert any(r.evaluator == "broken" for r in result.results)


# =====================================================================
#  Governance
# =====================================================================
def test_rbac_grants_and_denies_by_role():
    g = GovernanceLayer()
    g.assign("exec1", "executive")
    g.assign("admin1", "administrator")
    assert g.check_permission("exec1", "approve_actions").allowed
    assert not g.check_permission("exec1", "manage_connectors").allowed
    assert g.check_permission("admin1", "manage_connectors").allowed
    # Administrators operate, but are not automatically approvers.
    assert not g.check_permission("admin1", "approve_actions").allowed


def test_governance_fails_closed_on_unknown_role():
    g = GovernanceLayer(default_role="nonexistent")
    assert not g.check_permission("someone", "read_project").allowed


def test_disabling_governance_opens_every_gate():
    g = GovernanceLayer(enabled=False, default_role="manager")
    assert g.check_permission("anyone", "manage_policies").allowed


def test_governance_audits_and_logs_model_usage():
    g = GovernanceLayer()
    g.assign("u", "analyst")
    g.record_model_usage("ollama", "llama3",
                         prompt_id="reports.evidence_narrator",
                         tokens_in=1000, tokens_out=200)
    assert g.audit_log(action="role_assigned")
    summary = g.model_usage_summary()
    assert summary["calls"] == 1 and summary["tokens_total"] == 1200


def test_knowledge_access_policy_restricts_scope():
    g = GovernanceLayer()
    g.assign("u", "analyst")
    g.set_knowledge_policy(KnowledgeAccessPolicy(
        role="analyst", scopes=("team",)))
    assert g.check_knowledge("u", scope="team").allowed
    assert not g.check_knowledge("u", scope="restricted").allowed


def test_retention_expiry_is_computed_not_enforced():
    g = GovernanceLayer()
    assert g.is_expired("sync_runs", "2000-01-01T00:00:00+00:00")
    assert not g.is_expired("reports", "2000-01-01T00:00:00+00:00")  # never


def test_role_rejects_unknown_permissions():
    with pytest.raises(ValueError, match="unknown permissions"):
        Role(name="bad", permissions=("fly",))


# =====================================================================
#  Memory Lifecycle
# =====================================================================
class _FakeKnowledge:
    def insights(self, limit=200):
        return [{"recorded_at": "2020-01-01T00:00:00+00:00"}]

    def decisions(self, limit=200):
        return [{"recorded_at": "2020-01-01T00:00:00+00:00"}]

    def record_learning_event(self, *a, **k):
        self.logged = True


def test_memory_lifecycle_reports_freshness():
    lifecycle = MemoryLifecycle(knowledge=_FakeKnowledge())
    freshness = {f.knowledge_class: f for f in lifecycle.freshness()}
    # Insights from 2020 are unambiguously stale.
    assert freshness["insights"].state == "stale"


def test_memory_lifecycle_archives_without_deleting():
    knowledge = _FakeKnowledge()
    lifecycle = MemoryLifecycle(knowledge=knowledge)
    event = lifecycle.archive("doc:1", "document", reason="superseded")
    assert event.event == "archived"
    assert getattr(knowledge, "logged", False)
    assert lifecycle.events()[0]["subject"] == "doc:1"


def test_memory_lifecycle_degrades_without_components():
    lifecycle = MemoryLifecycle()   # nothing wired
    assert lifecycle.status()["total_items"] == 0
    assert lifecycle.document_versions() == []


# =====================================================================
#  Workflow Registry
# =====================================================================
class _FakeEngine:
    def __init__(self):
        self.ran = []

    def definition(self, name):
        return type("D", (), {"available": True})() if name == "known" else None

    def run(self, name, project_id):
        self.ran.append((name, project_id))
        return {"workflow": name, "status": "completed"}

    def recent_runs(self, n):
        return [{"status": "completed"}]


def test_workflow_registry_delegates_to_the_engine():
    engine = _FakeEngine()
    registry = WorkflowRegistry(engine=engine)
    registry.register(WorkflowSpec(
        workflow_id="brief", name="Brief", workflow="known",
        trigger="scheduled"))
    result = registry.execute("brief")
    assert result["status"] == "completed"
    assert engine.ran == [("known", "")]


def test_workflow_registry_reports_unavailable_without_pretending():
    engine = _FakeEngine()
    registry = WorkflowRegistry(engine=engine)
    registry.register(WorkflowSpec(
        workflow_id="ghost", name="Ghost", workflow="missing",
        trigger="manual"))
    assert registry.execute("ghost")["status"] == "unavailable"


def test_workflow_spec_validates_triggers():
    with pytest.raises(ValueError, match="trigger"):
        WorkflowSpec(workflow_id="x", name="X", trigger="whenever")
    with pytest.raises(ValueError, match="event"):
        WorkflowSpec(workflow_id="x", name="X", trigger="event")


def test_workflow_registry_discovers_by_trigger_and_tag():
    registry = WorkflowRegistry(engine=_FakeEngine())
    registry.register(WorkflowSpec(workflow_id="a", name="A",
                                   trigger="event", event="DocumentsUpdated",
                                   tags=("documents",)))
    registry.register(WorkflowSpec(workflow_id="b", name="B",
                                   trigger="scheduled", tags=("daily",)))
    assert [s.workflow_id for s in registry.find(trigger="event")] == ["a"]
    assert [s.workflow_id for s in registry.find(tag="daily")] == ["b"]


# =====================================================================
#  Observability
# =====================================================================
def test_observability_composes_available_sections():
    from app.observability import LatencyTracker, ObservabilityDashboard
    dash = ObservabilityDashboard(
        evaluation=EvaluationPipeline(), governance=GovernanceLayer(),
        latency=LatencyTracker())
    snapshot = dash.snapshot()
    assert snapshot["sections"]["evaluation_metrics"]["available"]
    assert not snapshot["sections"]["agent_health"]["available"]
    assert snapshot["verdict"]["state"] in ("healthy", "degraded", "unhealthy",
                                            "unknown")


def test_observability_latency_measures():
    from app.observability import LatencyTracker
    tracker = LatencyTracker()
    with tracker.measure("op"):
        pass
    assert tracker.summary()["op"]["samples"] == 1


def test_a_failing_section_does_not_break_the_dashboard():
    from app.observability import ObservabilityDashboard

    class Boom:
        def status(self):
            raise RuntimeError("layer down")

    dash = ObservabilityDashboard(agents=Boom())
    section = dash.agent_health()
    assert not section["available"] and "layer down" in section["reason"]

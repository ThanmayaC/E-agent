"""The enterprise agent catalogue — the SDS's named capabilities, mapped onto
the implementations that already exist.

This module implements **nothing**. Every capability the V2.2 SDS names is
already built:

    Executive Brief Agent      → DailyBriefGenerator + ExecutiveBriefGenerator
    Meeting Intelligence Agent → workflow ``meeting_summarization``
    RCA Agent                  → workflow ``rca_summarization``
    SOP Agent                  → workflow ``sop_change_detection``
    Report Agent               → the analysis orchestrator (``full_analysis``)
    Analytics Agent            → the Intelligence Engine, via BusinessAnalyst
    Recommendation Agent       → the Decision Engine + Product recommendations
    Forecast Agent             → the Forecasting module, via the analysis graph
    Communication Agent        → workflows ``email_drafting`` / ``teams_*``
    Risk Detection Agent       → workflow ``monitoring`` + growth risk sweeps
    Document Intelligence Agent→ the Document Intelligence pipeline

What was missing was not the capability — it was one place that says what
each one accepts, produces, needs, and is allowed to do, and one way for the
Runtime to find and run it. That is what this file adds, and why it is a
catalogue rather than a package of new agents.

Each descriptor's ``runner`` adapts an ``AgentRequest`` onto the existing
implementation. The adapters are deliberately thin: if one starts making
decisions, the logic has moved to the wrong layer.
"""
from __future__ import annotations

from typing import Any, Callable

from app.agents.base import AgentRequest, AgentResult
from app.agents.registry import AgentDescriptor
from app.core.logging import get_logger

logger = get_logger(__name__)


def _workflow_runner(workflows, workflow_name: str) -> Callable[[AgentRequest],
                                                                AgentResult]:
    """Adapt a registered workflow to the agent contract."""
    def run(request: AgentRequest) -> AgentResult:
        outcome = workflows.run(workflow_name, request.project_id)
        status = outcome.get("status", "completed")
        return AgentResult(
            status="ok" if status in ("completed", "ok") else "failed",
            output=outcome, confidence=1.0)
    return run


def _callable_runner(fn: Callable[..., Any], *,
                     pass_project: bool = False) -> Callable[[AgentRequest],
                                                             AgentResult]:
    """Adapt a plain layer method to the agent contract."""
    def run(request: AgentRequest) -> AgentResult:
        output = (fn(request.project_id) if pass_project
                  else fn(**request.payload))
        return AgentResult(status="ok", output=output, confidence=1.0)
    return run


def build_catalogue(*, workflows=None, brief=None, product=None,
                    documents=None, decisions=None,
                    orchestrator=None) -> list[AgentDescriptor]:
    """Every enterprise capability, described once.

    Components are injected; a component that is absent in this deployment
    yields a descriptor with no runner — it stays visible in the catalogue as
    a capability the platform *has* but cannot run here, which is more honest
    than hiding it.
    """
    catalogue: list[AgentDescriptor] = []

    # ---------------------------------------------------------- reporting
    catalogue.append(AgentDescriptor(
        agent_id="report_agent", name="Report Agent",
        description="Runs the full analysis and writes the executive report.",
        capabilities=("analyze", "generate_report"),
        inputs=("project_id",), outputs=("report", "evidence", "statements"),
        required_tools=("artifact_lookup", "report_markdown"),
        execution_policy="on_demand", approval_policy="review",
        brain_role="feeds", tags=("core", "reporting"),
        implementation="app.workflows.analysis / app.orchestration.graph",
        runner=(_workflow_runner(workflows, "full_analysis")
                if workflows is not None else None)))

    catalogue.append(AgentDescriptor(
        agent_id="executive_brief_agent", name="Executive Brief Agent",
        description="Generates the daily executive brief from what the Brain "
                    "already knows.",
        capabilities=("summarize", "generate_brief"),
        inputs=("date",), outputs=("brief",),
        execution_policy="automatic", approval_policy="none",
        brain_role="consumes", tags=("executive", "daily"),
        implementation="app.manager.DailyBriefGenerator",
        runner=(_callable_runner(brief.generate) if brief is not None else None)))

    catalogue.append(AgentDescriptor(
        agent_id="board_brief_agent", name="Board Brief Agent",
        description="Generates board briefs, monthly reviews, and quarterly "
                    "strategy packs from product intelligence.",
        capabilities=("summarize", "generate_brief"),
        inputs=("kind",), outputs=("brief",),
        execution_policy="scheduled_only", approval_policy="review",
        brain_role="consumes", tags=("executive", "product"),
        implementation="app.product.briefs.ExecutiveBriefGenerator",
        runner=(_callable_runner(product.briefs.generate)
                if product is not None and hasattr(product, "briefs") else None)))

    # ---------------------------------------------------------- documents
    catalogue.append(AgentDescriptor(
        agent_id="document_intelligence_agent",
        name="Document Intelligence Agent",
        description="Parses, chunks, embeds, and versions every document the "
                    "connectors detect.",
        capabilities=("process_document",),
        inputs=("knowledge_package", "sync_delta"),
        outputs=("document", "chunks", "version"),
        execution_policy="automatic", approval_policy="none",
        brain_role="feeds", tags=("documents", "ingestion"),
        implementation="app.documents.pipeline.DocumentIntelligence",
        runner=(_callable_runner(documents.process_sync)
                if documents is not None else None)))

    catalogue.append(AgentDescriptor(
        agent_id="meeting_intelligence_agent",
        name="Meeting Intelligence Agent",
        description="Summarizes meeting notes into decisions, topics, and "
                    "open questions.",
        capabilities=("summarize", "extract_actions"),
        inputs=("meeting_document",),
        outputs=("summary", "decisions", "open_questions"),
        execution_policy="automatic", approval_policy="none",
        brain_role="feeds", tags=("meetings", "documents"),
        implementation="app.workflows.library:_run_meeting_summarization",
        runner=(_workflow_runner(workflows, "meeting_summarization")
                if workflows is not None else None)))

    catalogue.append(AgentDescriptor(
        agent_id="action_item_agent", name="Action Item Agent",
        description="Extracts action items from meeting notes into executive "
                    "tasks.",
        capabilities=("extract_actions",),
        inputs=("meeting_document",), outputs=("tasks",),
        execution_policy="automatic", approval_policy="none",
        brain_role="automates", tags=("meetings", "tasks"),
        implementation="app.workflows.library:_run_action_item_extraction",
        runner=(_workflow_runner(workflows, "action_item_extraction")
                if workflows is not None else None)))

    catalogue.append(AgentDescriptor(
        agent_id="rca_agent", name="RCA Agent",
        description="Summarizes new and updated RCA documents into "
                    "organizational knowledge.",
        capabilities=("summarize", "analyze"),
        inputs=("rca_document",), outputs=("summary", "knowledge"),
        execution_policy="automatic", approval_policy="none",
        brain_role="feeds", tags=("rca", "documents"),
        implementation="app.workflows.library:_run_rca_summarization",
        runner=(_workflow_runner(workflows, "rca_summarization")
                if workflows is not None else None)))

    catalogue.append(AgentDescriptor(
        agent_id="sop_agent", name="SOP Agent",
        description="Detects SOP changes and opens review tasks.",
        capabilities=("detect_change", "summarize"),
        inputs=("sop_document",), outputs=("changes", "tasks"),
        execution_policy="automatic", approval_policy="none",
        brain_role="automates", tags=("sop", "documents"),
        implementation="app.workflows.library:_run_sop_change_detection",
        runner=(_workflow_runner(workflows, "sop_change_detection")
                if workflows is not None else None)))

    # ---------------------------------------------------------- analytics
    catalogue.append(AgentDescriptor(
        agent_id="analytics_agent", name="Analytics Agent",
        description="Deterministic analytics over connected data: profiling, "
                    "semantics, relationships, KPIs, quality, signals.",
        capabilities=("analyze",),
        inputs=("project_id",), outputs=("kpis", "signals", "quality"),
        required_tools=("analytics_sql",),
        execution_policy="on_demand", approval_policy="none",
        brain_role="feeds", tags=("analytics", "core"),
        implementation="app.intelligence.engine.IntelligenceEngine"))

    catalogue.append(AgentDescriptor(
        agent_id="forecast_agent", name="Forecast Agent",
        description="Produces validated KPI forecasts with confidence and "
                    "explicit limitations.",
        capabilities=("forecast",),
        inputs=("project_id", "kpi_id"), outputs=("forecast", "confidence"),
        execution_policy="on_demand", approval_policy="none",
        brain_role="feeds", tags=("forecasting", "ml"),
        implementation="app.intelligence.forecasting"))

    catalogue.append(AgentDescriptor(
        agent_id="recommendation_agent", name="Recommendation Agent",
        description="Turns evidence into routed recommendations — executed, "
                    "queued for approval, or escalated by confidence.",
        capabilities=("recommend",),
        inputs=("evidence", "context"), outputs=("recommendations", "actions"),
        execution_policy="automatic", approval_policy="required",
        brain_role="automates", tags=("decisions",),
        implementation="app.runtime.decisions.DecisionEngine",
        runner=(_callable_runner(decisions.decide_many)
                if decisions is not None
                and hasattr(decisions, "decide_many") else None)))

    catalogue.append(AgentDescriptor(
        agent_id="risk_detection_agent", name="Risk Detection Agent",
        description="Monitors KPIs, anomalies, and growth signals and raises "
                    "risks before they become incidents.",
        capabilities=("detect_risk",),
        inputs=("kpis", "signals"), outputs=("risks", "alerts"),
        execution_policy="automatic", approval_policy="none",
        brain_role="consumes", tags=("monitoring", "risk"),
        implementation="app.workflows.autonomous:monitoring",
        runner=(_workflow_runner(workflows, "monitoring")
                if workflows is not None else None)))

    # ------------------------------------------------------ communication
    catalogue.append(AgentDescriptor(
        agent_id="communication_agent", name="Communication Agent",
        description="Drafts executive email and Teams updates. Drafts only — "
                    "nothing leaves the platform without approval.",
        capabilities=("draft_communication",),
        inputs=("recipients", "context"), outputs=("draft",),
        required_tools=("email_draft",),
        execution_policy="scheduled_only", approval_policy="required",
        brain_role="automates", tags=("communication", "drafting"),
        implementation="app.workflows.library:_run_email_drafting",
        runner=(_workflow_runner(workflows, "email_drafting")
                if workflows is not None else None)))

    return catalogue


def register_catalogue(registry, **components) -> int:
    """Register every catalogued capability. Returns how many are executable
    in this deployment."""
    executable = 0
    for descriptor in build_catalogue(**components):
        registry.register_capability(descriptor)
        executable += bool(descriptor.executable)
    logger.info("Agent catalogue registered (%d executable)", executable)
    return executable

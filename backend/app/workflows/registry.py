"""Autonomous Workflow Registry (Version 2.2).

The Workflow Engine already runs workflows and records every run. What it
could not tell you is what a workflow *is*: what triggers it, which agents and
tools it uses, what it produces, whether its output needs approval, and on
what schedule it runs. That knowledge was spread across the scheduler's job
definitions, the engine's registrations, and the container's wiring.

This registry declares it in one place, as data. The Runtime executes
workflows **from the registry**, and adding a workflow becomes a declaration
rather than an edit in three files.

It is a registry, **not a second orchestration engine**: every ``execute``
delegates to the existing ``WorkflowEngine``, which still owns running steps,
recording runs, and announcing completion. If this module ever grows a step
loop, the architecture has gone wrong.
"""
from __future__ import annotations

import threading
from dataclasses import dataclass
from typing import Any

from app.core.logging import get_logger

logger = get_logger(__name__)

# How a workflow starts.
TRIGGERS = ("scheduled", "event", "manual", "startup")

# What must happen to its output before it has an effect.
APPROVAL_POLICIES = ("none", "review", "required")


@dataclass
class WorkflowSpec:
    """A declared autonomous workflow.

    ``workflow`` names the definition registered on the Workflow Engine; this
    spec describes it rather than reimplementing it. A spec whose workflow is
    not registered in this deployment stays visible and reports itself
    unavailable — the catalogue tells the truth about what the platform can
    do, not what it wishes it could.
    """
    workflow_id: str
    name: str
    description: str = ""
    trigger: str = "scheduled"
    schedule: str = ""                       # cron or interval description
    event: str = ""                          # for trigger="event"
    inputs: tuple[str, ...] = ()
    outputs: tuple[str, ...] = ()
    agents: tuple[str, ...] = ()             # agent ids from the Agent Registry
    tools: tuple[str, ...] = ()              # tool ids from the Tool Registry
    approval_policy: str = "none"
    workflow: str = ""                       # engine definition name
    tags: tuple[str, ...] = ()
    enabled: bool = True

    def __post_init__(self) -> None:
        if self.trigger not in TRIGGERS:
            raise ValueError(
                f"Workflow {self.workflow_id}: unknown trigger "
                f"{self.trigger!r}")
        if self.approval_policy not in APPROVAL_POLICIES:
            raise ValueError(
                f"Workflow {self.workflow_id}: unknown approval policy "
                f"{self.approval_policy!r}")
        if self.trigger == "event" and not self.event:
            raise ValueError(
                f"Workflow {self.workflow_id}: an event trigger needs an event")
        if not self.workflow:
            self.workflow = self.workflow_id

    def describe(self) -> dict:
        return {"id": self.workflow_id, "name": self.name,
                "description": self.description, "trigger": self.trigger,
                "schedule": self.schedule, "event": self.event,
                "inputs": list(self.inputs), "outputs": list(self.outputs),
                "agents": list(self.agents), "tools": list(self.tools),
                "approval_policy": self.approval_policy,
                "workflow": self.workflow, "tags": list(self.tags),
                "enabled": self.enabled}


class WorkflowRegistry:
    """Every declared autonomous workflow, and the engine that runs them."""

    def __init__(self, engine=None, agents=None):
        self._specs: dict[str, WorkflowSpec] = {}
        self._engine = engine
        self._agents = agents
        self._lock = threading.RLock()

    def attach_engine(self, engine) -> None:
        self._engine = engine

    # ------------------------------------------------------- registration
    def register(self, spec: WorkflowSpec) -> WorkflowSpec:
        with self._lock:
            self._specs[spec.workflow_id] = spec
        return spec

    def register_all(self, specs: list[WorkflowSpec]) -> int:
        for spec in specs:
            self.register(spec)
        return len(specs)

    # ----------------------------------------------------------- discovery
    def get(self, workflow_id: str) -> WorkflowSpec:
        with self._lock:
            if workflow_id not in self._specs:
                raise KeyError(f"Unknown workflow: {workflow_id}")
            return self._specs[workflow_id]

    def find(self, trigger: str = "", agent: str = "", tag: str = "",
             enabled_only: bool = False) -> list[WorkflowSpec]:
        with self._lock:
            found = list(self._specs.values())
        if trigger:
            found = [s for s in found if s.trigger == trigger]
        if agent:
            found = [s for s in found if agent in s.agents]
        if tag:
            found = [s for s in found if tag in s.tags]
        if enabled_only:
            found = [s for s in found if s.enabled]
        return found

    def available(self, spec: WorkflowSpec) -> bool:
        """Whether the engine can actually run this workflow here."""
        if self._engine is None:
            return False
        definition = self._engine.definition(spec.workflow)
        return definition is not None and definition.available

    # ----------------------------------------------------------- execution
    def execute(self, workflow_id: str, project_id: str = "") -> dict:
        """Run a declared workflow through the existing Workflow Engine."""
        spec = self.get(workflow_id)
        if not spec.enabled:
            return {"workflow": workflow_id, "status": "skipped",
                    "reason": "workflow is disabled"}
        if self._engine is None:
            raise RuntimeError(
                "No Workflow Engine attached — the registry declares "
                "workflows, it does not run them")
        if not self.available(spec):
            return {"workflow": workflow_id, "status": "unavailable",
                    "reason": f"'{spec.workflow}' is not registered or not "
                              f"executable in this deployment"}
        return self._engine.run(spec.workflow, project_id)

    # --------------------------------------------------------- inspection
    def describe(self) -> list[dict]:
        with self._lock:
            specs = list(self._specs.values())
        return [{**s.describe(), "available": self.available(s)}
                for s in sorted(specs, key=lambda s: s.workflow_id)]

    def status(self) -> dict[str, Any]:
        specs = self.describe()
        by_trigger: dict[str, int] = {}
        for s in specs:
            by_trigger[s["trigger"]] = by_trigger.get(s["trigger"], 0) + 1
        runs, failures = 0, 0
        if self._engine is not None and hasattr(self._engine, "recent_runs"):
            try:
                recent = self._engine.recent_runs(200)
                runs = len(recent)
                failures = sum(1 for r in recent
                               if r.get("status") == "failed")
            except Exception:  # noqa: BLE001 — statistics never break a status
                logger.exception("Workflow run statistics failed")
        return {
            "total": len(specs),
            "enabled": sum(1 for s in specs if s["enabled"]),
            "available": sum(1 for s in specs if s["available"]),
            "by_trigger": by_trigger,
            "requiring_approval": sum(1 for s in specs
                                      if s["approval_policy"] != "none"),
            "runs": runs, "failures": failures,
            "success_rate": (round((runs - failures) / runs, 3)
                             if runs else None),
        }


def build_default_specs(settings=None) -> list[WorkflowSpec]:
    """The V2.2 workflow catalogue, declared over what already runs.

    Every entry names a workflow the engine already has. Schedules mirror the
    scheduler's existing job configuration rather than introducing a second
    source of truth for cadence — the scheduler still owns when things run.
    """
    def cron(attr: str, default: str) -> str:
        return str(getattr(settings, attr, default)) if settings else default

    return [
        WorkflowSpec(
            workflow_id="daily_executive_brief", name="Daily Executive Brief",
            description="Assemble and deliver the executive's daily brief.",
            trigger="scheduled",
            schedule=cron("autonomy_daily_cycle_cron", "0 6 * * *"),
            inputs=("date",), outputs=("brief", "notifications"),
            agents=("executive_brief_agent",), workflow="daily_cycle",
            approval_policy="none", tags=("executive", "daily")),
        WorkflowSpec(
            workflow_id="weekly_kpi_report", name="Weekly KPI Report",
            description="Refresh KPI analysis and publish the weekly report.",
            trigger="scheduled", schedule=cron("product_brief_cron",
                                               "0 7 * * 1"),
            inputs=("project_id",), outputs=("report",),
            agents=("analytics_agent", "report_agent"),
            tools=("analytics_sql", "report_markdown"),
            workflow="full_analysis", approval_policy="review",
            tags=("reporting", "weekly")),
        WorkflowSpec(
            workflow_id="monthly_product_review",
            name="Monthly Product Review",
            description="Generate the monthly product review brief.",
            trigger="scheduled", schedule="0 7 1 * *",
            inputs=("kind",), outputs=("brief",),
            agents=("board_brief_agent",), workflow="monthly_review",
            approval_policy="review", tags=("product", "monthly")),
        WorkflowSpec(
            workflow_id="meeting_processing", name="Meeting Processing",
            description="Summarize new meeting notes and extract action items.",
            trigger="event", event="DocumentsUpdated",
            inputs=("meeting_document",),
            outputs=("summary", "tasks"),
            agents=("meeting_intelligence_agent", "action_item_agent"),
            workflow="meeting_summarization", approval_policy="none",
            tags=("meetings", "documents")),
        WorkflowSpec(
            workflow_id="rca_processing", name="RCA Processing",
            description="Summarize new and updated RCA documents.",
            trigger="event", event="DocumentsUpdated",
            inputs=("rca_document",), outputs=("summary", "knowledge"),
            agents=("rca_agent",), workflow="rca_summarization",
            approval_policy="none", tags=("rca", "documents")),
        WorkflowSpec(
            workflow_id="sop_change_detection", name="SOP Change Detection",
            description="Detect SOP changes and open review tasks.",
            trigger="event", event="DocumentsUpdated",
            inputs=("sop_document",), outputs=("changes", "tasks"),
            agents=("sop_agent",), workflow="sop_change_detection",
            approval_policy="none", tags=("sop", "documents")),
        WorkflowSpec(
            workflow_id="risk_monitoring", name="Risk Monitoring",
            description="Monitor KPIs and signals; raise risks and alerts.",
            trigger="scheduled",
            schedule=cron("autonomy_monitoring_cron", "0 * * * *"),
            inputs=("kpis", "signals"), outputs=("risks", "alerts"),
            agents=("risk_detection_agent",), workflow="monitoring",
            approval_policy="none", tags=("monitoring", "risk")),
        WorkflowSpec(
            workflow_id="email_draft", name="Email Draft Workflow",
            description="Draft the daily executive status email for approval.",
            trigger="scheduled", schedule=cron("v2_email_draft_cron",
                                               "30 6 * * *"),
            inputs=("recipients",), outputs=("draft",),
            agents=("communication_agent",), tools=("email",),
            workflow="email_drafting", approval_policy="required",
            tags=("communication", "drafting")),
        WorkflowSpec(
            workflow_id="presentation_draft", name="Presentation Workflow",
            description="Draft the weekly portfolio review presentation.",
            trigger="scheduled", schedule=cron("v2_presentation_cron",
                                               "0 7 * * 1"),
            inputs=("portfolio",), outputs=("slides",),
            tools=("powerpoint_generator",),
            workflow="presentation_drafting", approval_policy="review",
            tags=("communication", "drafting")),
        WorkflowSpec(
            workflow_id="knowledge_refresh", name="Knowledge Refresh",
            description="Synchronize connected sources and refresh the Brain.",
            trigger="scheduled", schedule="every 15 minutes",
            inputs=(), outputs=("knowledge",),
            agents=("document_intelligence_agent",),
            workflow="background_intelligence", approval_policy="none",
            tags=("knowledge", "ingestion")),
    ]

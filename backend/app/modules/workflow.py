"""Workflow Module (SDS §2.8) — status: implemented.

Named, registered units of autonomous work with persisted run history.
Two shapes share one engine:

- single-runner workflows wrap one callable (``full_analysis`` — the
  analysis graph);
- autonomous workflows are ordered step chains the engine executes without
  a user: ``daily_cycle`` (refresh portfolio → analyse new data → update the
  Enterprise Brain → daily brief → tasks → recommendations → queue
  communications), ``background_intelligence``, and ``monitoring``.

Approval flows are handled at two levels: the analysis graph's confidence
gate (LangGraph interrupt/resume) inside a run, and the Action Queue's
approval layer for anything a workflow wants to do to the outside world.
"""
from app.workflows.analysis import AnalysisWorkflow
from app.workflows.autonomous import (
    AutonomousContext, build_autonomous_workflows,
)
from app.workflows.engine import (
    PLANNED_WORKFLOWS, WorkflowDefinition, WorkflowEngine, WorkflowStep,
)

__all__ = ["AnalysisWorkflow", "AutonomousContext", "PLANNED_WORKFLOWS",
           "WorkflowDefinition", "WorkflowEngine", "WorkflowStep",
           "build_autonomous_workflows"]

"""Platform introspection, workflow, and control-plane APIs.

Exposes the agent registry, tool registry, connector catalogue, workflow
definitions, runs, and schedules — powering the Workflow Monitoring UI —
plus the Evidence Ledger's governance surface (analysis runs and their node
events, evidence records, AI statements with citations, the model registry).
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from app.api.deps import container, require_project
from app.core.container import Container

router = APIRouter(tags=["platform"])


@router.get("/platform/agents")
def agents(c: Container = Depends(container)):
    return c.agents.describe()


@router.get("/platform/tools")
def tools(c: Container = Depends(container)):
    return c.tools.describe()


@router.get("/platform/connectors")
def connectors(c: Container = Depends(container)):
    return c.connectors.describe()


@router.get("/platform/workflows")
def workflows(c: Container = Depends(container)):
    return c.workflows.describe()


@router.get("/projects/{project_id}/workflow-runs")
def workflow_runs(project_id: str, c: Container = Depends(container)):
    require_project(c, project_id)
    return c.workflows.runs(project_id)


@router.get("/projects/{project_id}/workflow-schedules")
def workflow_schedules(project_id: str, c: Container = Depends(container)):
    require_project(c, project_id)
    return c.workflows.schedules(project_id)


# ------------------------------------------- Evidence Ledger (control plane)
@router.get("/projects/{project_id}/runs")
def analysis_runs(project_id: str, c: Container = Depends(container)):
    """LangGraph analysis runs recorded in the control plane (newest first)."""
    require_project(c, project_id)
    return c.ledger.runs(project_id)


@router.get("/projects/{project_id}/runs/{run_id}/events")
def run_events(project_id: str, run_id: str, c: Container = Depends(container)):
    """The run's full node-event stream — the durable trace behind the
    Run Graph console."""
    require_project(c, project_id)
    return c.ledger.run_events(run_id)


@router.get("/projects/{project_id}/evidence-ledger")
def evidence_ledger(project_id: str, run_id: str | None = None,
                    kind: str | None = None, c: Container = Depends(container)):
    require_project(c, project_id)
    return c.ledger.evidence(project_id, run_id=run_id, kind=kind)


@router.get("/projects/{project_id}/statements")
def statements(project_id: str, run_id: str | None = None,
               c: Container = Depends(container)):
    """Every AI statement with its type, verification verdict, and cited
    evidence ids — statements × citations × evidence, one join away."""
    require_project(c, project_id)
    return c.ledger.statements(project_id, run_id=run_id)


@router.get("/projects/{project_id}/models")
def models(project_id: str, c: Container = Depends(container)):
    """Model registry: every admitted model with metrics + selection trace."""
    require_project(c, project_id)
    return c.ledger.models(project_id)


class Schedule(BaseModel):
    workflow: str
    cadence: str  # daily | weekly | monthly


@router.post("/projects/{project_id}/workflow-schedules", status_code=201)
def add_schedule(project_id: str, body: Schedule, c: Container = Depends(container)):
    require_project(c, project_id)
    if body.cadence not in ("daily", "weekly", "monthly"):
        raise HTTPException(422, "cadence must be daily, weekly, or monthly")
    return c.workflows.schedule(project_id, body.workflow, body.cadence)

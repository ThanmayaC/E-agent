"""Enterprise AI Operating Layer APIs (Version 2.2) — Admin only.

The Agent Registry, Tool Registry, Prompt Registry, Evaluation pipeline,
Governance layer, Memory Lifecycle, Autonomous Workflow Registry, and the
Observability dashboard. Read-and-operate surfaces for administrators; the
Executive Workspace never touches any of them.

Every route reads a registry that already exists in the container — these
endpoints expose the operating layer, they do not implement it.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel

from app.agents.base import AgentRequest
from app.api.deps import container
from app.core.container import Container

router = APIRouter(prefix="/ops", tags=["ai operating layer"])


# =====================================================================
#  Agent Registry
# =====================================================================
@router.get("/agents")
def agents(capability: str = "", brain_role: str = "",
           c: Container = Depends(container)):
    """Every registered autonomous capability, with health."""
    found = c.agents.find(capability=capability, brain_role=brain_role)
    ids = {d.agent_id for d in found}
    return {"agents": [a for a in c.agents.describe() if a["id"] in ids],
            "status": c.agents.status()}


@router.get("/agents/{agent_id}")
def agent(agent_id: str, c: Container = Depends(container)):
    try:
        return {**c.agents.descriptor(agent_id).describe(),
                "health": c.agents.health(agent_id).describe()}
    except KeyError:
        raise HTTPException(status_code=404, detail="Agent not found")


class AgentRun(BaseModel):
    goal: str = ""
    project_id: str = ""
    payload: dict = {}


@router.post("/agents/{agent_id}/run")
def run_agent(agent_id: str, body: AgentRun,
              c: Container = Depends(container)):
    """Execute an agent through the registry. Governed by its execution
    policy — an ``on_demand`` agent refuses an automatic reason."""
    if not c.agents.has(agent_id):
        raise HTTPException(status_code=404, detail="Agent not found")
    result = c.agents.execute(
        agent_id, AgentRequest(goal=body.goal, project_id=body.project_id,
                               payload=body.payload), reason="manual")
    return {"agent": agent_id, "status": result.status,
            "confidence": result.confidence,
            "output": result.output if isinstance(result.output, (dict, list, str))
            else str(result.output)}


# =====================================================================
#  Tool Registry
# =====================================================================
@router.get("/tools")
def tools(capability: str = "", c: Container = Depends(container)):
    found = {s.tool_id for s in c.tools.find(capability=capability)} \
        if capability else None
    described = c.tools.describe()
    if found is not None:
        described = [t for t in described if t["id"] in found]
    return {"tools": described, "status": c.tools.status()}


# =====================================================================
#  Prompt Registry
# =====================================================================
@router.get("/prompts")
def prompts(domain: str = "", c: Container = Depends(container)):
    described = c.prompts.describe()
    if domain:
        described = [p for p in described if p["domain"] == domain]
    return {"prompts": described, "status": c.prompts.status()}


@router.get("/prompts/{prompt_id}")
def prompt(prompt_id: str, c: Container = Depends(container)):
    try:
        template = c.prompts.get(prompt_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return {**template.describe(),
            "template": template.template,
            "versions": [t.version for t in c.prompts.versions(prompt_id)],
            "history": c.prompts.history(prompt_id, limit=20)}


# =====================================================================
#  Evaluation
# =====================================================================
@router.get("/evaluation")
def evaluation(c: Container = Depends(container)):
    return {"status": c.evaluation.status(),
            "evaluators": c.evaluation.describe()}


@router.get("/evaluation/history")
def evaluation_history(decision: str = "", limit: int = Query(50, ge=1, le=200),
                       c: Container = Depends(container)):
    return {"history": c.evaluation.history(limit=limit, decision=decision)}


# =====================================================================
#  Governance
# =====================================================================
@router.get("/governance")
def governance(c: Container = Depends(container)):
    return c.governance.status()


@router.get("/governance/audit")
def audit_log(action: str = "", actor: str = "",
              limit: int = Query(100, ge=1, le=500),
              c: Container = Depends(container)):
    return {"audit": c.governance.audit_log(action=action, actor=actor,
                                            limit=limit)}


@router.get("/governance/model-usage")
def model_usage(limit: int = Query(100, ge=1, le=500),
                c: Container = Depends(container)):
    return {"usage": c.governance.model_usage(limit=limit),
            "summary": c.governance.model_usage_summary()}


class RoleAssignment(BaseModel):
    principal: str
    role: str


@router.post("/governance/assign")
def assign_role(body: RoleAssignment, c: Container = Depends(container)):
    """Assign a principal to a role. Audited."""
    try:
        c.governance.assign(body.principal, body.role, actor="admin_api")
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    return {"principal": body.principal, "role": body.role,
            "permissions": list(c.governance.role_of(body.principal).permissions)}


# =====================================================================
#  Memory Lifecycle
# =====================================================================
@router.get("/memory/lifecycle")
def memory_lifecycle(c: Container = Depends(container)):
    return c.memory_lifecycle.status()


@router.get("/memory/freshness")
def memory_freshness(c: Container = Depends(container)):
    return {"freshness": [f.describe() for f in c.memory_lifecycle.freshness()]}


@router.get("/memory/evolution")
def memory_evolution(hours: int = Query(168, ge=1, le=24 * 90),
                     c: Container = Depends(container)):
    return c.memory_lifecycle.relationship_evolution(since_hours=hours)


# =====================================================================
#  Autonomous Workflow Registry
# =====================================================================
@router.get("/workflows")
def workflows(trigger: str = "", tag: str = "",
              c: Container = Depends(container)):
    described = c.workflow_registry.describe()
    if trigger:
        described = [w for w in described if w["trigger"] == trigger]
    if tag:
        described = [w for w in described if tag in w["tags"]]
    return {"workflows": described, "status": c.workflow_registry.status()}


@router.post("/workflows/{workflow_id}/run")
def run_workflow(workflow_id: str, project_id: str = "",
                 c: Container = Depends(container)):
    try:
        return c.workflow_registry.execute(workflow_id, project_id=project_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Workflow not found")


# =====================================================================
#  Observability
# =====================================================================
@router.get("/observability")
def observability(c: Container = Depends(container)):
    """The whole operational dashboard in one call. Admin-only; nothing here
    touches the Executive Workspace."""
    return c.observability.snapshot()


@router.get("/observability/{section}")
def observability_section(section: str, c: Container = Depends(container)):
    reader = getattr(c.observability, section, None)
    if reader is None or not callable(reader):
        raise HTTPException(
            status_code=404,
            detail=f"Unknown observability section: {section}")
    return reader()

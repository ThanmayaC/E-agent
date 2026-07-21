"""Runtime Dashboard APIs — the autonomous execution layer's surface.

Everything the platform does on its own is observable here: the scheduler
and its jobs, the event stream, the action queue and its approval layer, the
goals it is working toward, the plans it is executing, and every execution
it has recorded. APIs only — no business logic lives in this module.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

from app.api.deps import container
from app.core.container import Container

router = APIRouter(tags=["runtime"])


# ------------------------------------------------------------------ status
@router.get("/runtime")
def runtime_status(c: Container = Depends(container)):
    """Is the agent autonomous right now, and what is it carrying?"""
    return c.runtime.status()


@router.get("/runtime/activity")
def runtime_activity(limit: int = Query(20, ge=1, le=100),
                     c: Container = Depends(container)):
    """Autonomous Activities: what the agent did while nobody watched."""
    return c.runtime.activity(limit)


# -------------------------------------------------------------- scheduler
@router.get("/runtime/scheduler")
def scheduler(c: Container = Depends(container)):
    return c.runtime.scheduler.status()


@router.post("/runtime/scheduler/start")
def start_scheduler(c: Container = Depends(container)):
    """Start the heartbeat (idempotent) — runs startup jobs, then ticks."""
    return c.runtime.start()


@router.post("/runtime/scheduler/stop")
def stop_scheduler(c: Container = Depends(container)):
    """Stop the heartbeat. Queued work and state survive; nothing new runs."""
    c.runtime.stop()
    return c.runtime.status()


# ------------------------------------------------------------------- jobs
@router.get("/runtime/jobs")
def jobs(c: Container = Depends(container)):
    return c.runtime.scheduler.describe()


@router.post("/runtime/jobs/{name}/run")
def run_job(name: str, c: Container = Depends(container)):
    """Run a job now, outside its schedule."""
    try:
        return c.runtime.scheduler.run_job(name, reason="manual")
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Unknown job: {name}")


class JobEnabled(BaseModel):
    enabled: bool


@router.patch("/runtime/jobs/{name}")
def set_job_enabled(name: str, body: JobEnabled,
                    c: Container = Depends(container)):
    try:
        return c.runtime.scheduler.enable(name, body.enabled)
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Unknown job: {name}")


# ----------------------------------------------------------------- events
@router.get("/runtime/events")
def events(kind: str = "", project_id: str = "",
           limit: int = Query(50, ge=1, le=200),
           c: Container = Depends(container)):
    return {"events": c.runtime.bus.history(limit, kind=kind,
                                            project_id=project_id),
            "stats": c.runtime.bus.stats(),
            "subscriptions": c.runtime.bus.subscribers()}


# ------------------------------------------------------------- executions
@router.get("/runtime/executions")
def executions(job: str = "", limit: int = Query(50, ge=1, le=200),
               c: Container = Depends(container)):
    return c.runtime.scheduler.executions(limit, job=job)


# ------------------------------------------------ actions / queue / approvals
@router.get("/runtime/actions")
def actions(status: str = "", kind: str = "", project_id: str = "",
            limit: int = Query(100, ge=1, le=500),
            c: Container = Depends(container)):
    return {"actions": c.runtime.queue.actions(status=status, kind=kind,
                                               project_id=project_id,
                                               limit=limit),
            "stats": c.runtime.queue.stats()}


@router.get("/runtime/queue")
def queue(c: Container = Depends(container)):
    """The execution centre: what is waiting, on whom, and under what policy."""
    return {"stats": c.runtime.queue.stats(),
            "policy": c.runtime.queue.policy(),
            "pending_approval": c.runtime.queue.pending_approvals(),
            "in_flight": c.runtime.queue.actions(status="approved", limit=50),
            "recent": c.runtime.queue.recent(20)}


class ActionSubmit(BaseModel):
    kind: str
    title: str
    detail: str = ""
    payload: dict = Field(default_factory=dict)
    priority: int = Field(5, ge=1, le=9)
    project_id: str = ""


@router.post("/runtime/actions", status_code=201)
def submit_action(body: ActionSubmit, c: Container = Depends(container)):
    try:
        action = c.runtime.queue.submit(
            body.kind, body.title, payload=body.payload, detail=body.detail,
            priority=body.priority, project_id=body.project_id,
            source="manager", source_ref="")
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    if action is None:
        raise HTTPException(status_code=409,
                            detail="An equivalent action is already queued")
    return action


class Approval(BaseModel):
    by: str = ""
    reason: str = ""


@router.post("/runtime/actions/{action_id}/approve")
def approve_action(action_id: str, body: Approval,
                   c: Container = Depends(container)):
    """Approve a queued action; the next queue drain executes it."""
    try:
        return c.runtime.queue.approve(action_id, by=body.by)
    except KeyError:
        raise HTTPException(status_code=404, detail="Action not found")
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


@router.post("/runtime/actions/{action_id}/reject")
def reject_action(action_id: str, body: Approval,
                  c: Container = Depends(container)):
    try:
        return c.runtime.queue.reject(action_id, by=body.by,
                                      reason=body.reason)
    except KeyError:
        raise HTTPException(status_code=404, detail="Action not found")
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


class ActionEdit(BaseModel):
    title: str = ""
    detail: str = ""
    payload: dict = Field(default_factory=dict)
    by: str = ""


@router.patch("/runtime/actions/{action_id}")
def edit_action(action_id: str, body: ActionEdit,
                c: Container = Depends(container)):
    """Edit a queued action before it executes (V2 Approval Engine): the
    manager rewrites a draft instead of only approving or rejecting it."""
    try:
        return c.runtime.queue.edit(action_id, title=body.title,
                                    detail=body.detail, payload=body.payload,
                                    by=body.by)
    except KeyError:
        raise HTTPException(status_code=404, detail="Action not found")
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


@router.post("/runtime/actions/{action_id}/execute")
def execute_action(action_id: str, c: Container = Depends(container)):
    """Execute an approved action immediately instead of waiting for the
    next drain."""
    try:
        return c.runtime.queue.execute(action_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Action not found")
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(status_code=422, detail=str(exc))


@router.post("/runtime/actions/{action_id}/retry")
def retry_action(action_id: str, c: Container = Depends(container)):
    try:
        return c.runtime.queue.retry(action_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Action not found")
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


# ------------------------------------------------------------------ goals
class KPI(BaseModel):
    name: str
    target: float
    direction: str = "increase"        # increase | decrease | maintain
    metric: str = ""                   # platform metric that measures it
    baseline: float | None = None
    current: float | None = None
    unit: str = ""


class GoalCreate(BaseModel):
    objective: str
    detail: str = ""
    kpis: list[KPI] = Field(default_factory=list)
    deadline: str = ""                 # ISO date
    owner: str = ""
    horizon: str = "quarter"
    project_id: str = ""


@router.get("/runtime/goals")
def goals(status: str = "", c: Container = Depends(container)):
    return {"goals": c.runtime.goals.goals(status=status),
            "progress": c.runtime.goals.progress_report()}


@router.post("/runtime/goals", status_code=201)
def create_goal(body: GoalCreate, c: Container = Depends(container)):
    """Define an objective. The platform plans it and starts working toward
    it immediately — the plan is created by the GoalCreated event."""
    try:
        return c.runtime.goals.create(
            body.objective, kpis=[k.model_dump() for k in body.kpis],
            deadline=body.deadline, owner=body.owner, horizon=body.horizon,
            project_id=body.project_id, detail=body.detail)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


@router.get("/runtime/goals/{goal_id}")
def goal(goal_id: str, c: Container = Depends(container)):
    found = c.runtime.goals.get(goal_id)
    if found is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    return {"goal": found, "plan": c.runtime.planning.plan_for(goal_id)}


class GoalStatus(BaseModel):
    status: str


@router.patch("/runtime/goals/{goal_id}")
def set_goal_status(goal_id: str, body: GoalStatus,
                    c: Container = Depends(container)):
    try:
        updated = c.runtime.goals.set_status(goal_id, body.status)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    if updated is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    return updated


class Measurement(BaseModel):
    kpi: str
    value: float


@router.post("/runtime/goals/{goal_id}/measure")
def measure_goal(goal_id: str, body: Measurement,
                 c: Container = Depends(container)):
    updated = c.runtime.goals.record_measurement(goal_id, body.kpi, body.value)
    if updated is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    return updated


@router.get("/runtime/metrics")
def metrics(c: Container = Depends(container)):
    """The metric names a KPI can point at, with their current values."""
    return c.runtime.background.metrics_snapshot()


# ------------------------------------------------------------------ plans
@router.get("/runtime/plans")
def plans(status: str = "", goal_id: str = "",
          c: Container = Depends(container)):
    return {"plans": c.runtime.planning.plans(status=status, goal_id=goal_id),
            "stats": c.runtime.planning.stats()}


@router.post("/runtime/plans/{plan_id}/advance")
def advance_plan(plan_id: str, c: Container = Depends(container)):
    return c.runtime.planning.advance(plan_id)


class Replan(BaseModel):
    reason: str = "requested by the manager"


@router.post("/runtime/plans/{plan_id}/replan")
def replan(plan_id: str, body: Replan, c: Container = Depends(container)):
    successor = c.runtime.planning.replan(plan_id, body.reason)
    if successor is None:
        raise HTTPException(status_code=404, detail="Plan not found")
    return successor


# --------------------------------------------------------------- decisions
@router.get("/runtime/decisions")
def decisions(status: str = "", project_id: str = "",
              c: Container = Depends(container)):
    """Every autonomous decision with its full pipeline trace."""
    return {"decisions": c.runtime.decisions.decisions(status=status,
                                                       project_id=project_id),
            "stats": c.runtime.decisions.stats()}


# ----------------------------------------- V2.4: Decision Intelligence
@router.get("/runtime/intelligence")
def decision_intelligence(c: Container = Depends(container)):
    """What the Brain is deciding about: counts, statuses, last sweep."""
    return c.runtime.intelligence.status()


@router.post("/runtime/intelligence/observe")
def observe_now(c: Container = Depends(container)):
    """Run the proactive detection sweep now, outside its schedule."""
    return c.runtime.intelligence.observe()


@router.get("/runtime/intelligence/decisions")
def intelligence_decisions(status: str = "", kind: str = "",
                           limit: int = Query(50, ge=1, le=200),
                           c: Container = Depends(container)):
    """Every organizational decision with its full lifecycle history."""
    return {"decisions": c.runtime.intelligence.decisions(
                status=status, kind=kind, limit=limit),
            "stats": c.runtime.intelligence.stats()}


@router.get("/runtime/intelligence/recommendations")
def intelligence_recommendations(limit: int = Query(5, ge=1, le=25),
                                 c: Container = Depends(container)):
    """The highest-value open decisions, ranked, with factor breakdowns."""
    return {"recommendations": c.runtime.intelligence.rank(limit)}


@router.get("/runtime/intelligence/signals")
def intelligence_signals(kind: str = "", limit: int = Query(50, ge=1, le=200),
                         c: Container = Depends(container)):
    """The significant observations that produced candidate decisions."""
    return {"signals": c.runtime.intelligence.signals(kind=kind, limit=limit)}


@router.get("/runtime/intelligence/brief")
def intelligence_brief(c: Container = Depends(container)):
    """The executive workspace brief: what requires attention right now."""
    return c.runtime.intelligence.brief(queue=c.runtime.queue)


@router.get("/runtime/intelligence/reports/{period}")
def intelligence_report(period: str, c: Container = Depends(container)):
    """Decision reports: daily, weekly, or monthly."""
    try:
        return c.runtime.intelligence.report(period)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


class DecisionPropose(BaseModel):
    action: str
    kind: str = "recommendation"
    reasoning: str = ""
    priority: int = Field(3, ge=1, le=9)
    confidence: float | None = Field(None, ge=0, le=1)
    evidence_ids: list[str] = Field(default_factory=list)
    affected_products: list[str] = Field(default_factory=list)
    affected_teams: list[str] = Field(default_factory=list)
    expected_impact: str = ""
    owner: str = ""
    dependencies: list[str] = Field(default_factory=list)
    project_id: str = ""


@router.post("/runtime/intelligence/decisions", status_code=201)
def propose_decision(body: DecisionPropose,
                     c: Container = Depends(container)):
    """Propose a decision manually — same lifecycle as a detected one."""
    try:
        record = c.runtime.intelligence.propose(
            body.action, kind=body.kind, reasoning=body.reasoning,
            priority=body.priority, confidence=body.confidence,
            evidence_ids=body.evidence_ids,
            affected_products=body.affected_products,
            affected_teams=body.affected_teams,
            expected_impact=body.expected_impact, owner=body.owner,
            dependencies=body.dependencies, project_id=body.project_id,
            created_by="manager")
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    if record is None:
        raise HTTPException(status_code=409,
                            detail="An equivalent decision is already open")
    return record


class DecisionStatus(BaseModel):
    status: str
    by: str = ""
    note: str = ""


@router.get("/runtime/intelligence/decisions/{decision_id}")
def get_intelligence_decision(decision_id: str,
                              c: Container = Depends(container)):
    record = c.runtime.intelligence.get(decision_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Decision not found")
    return record


@router.patch("/runtime/intelligence/decisions/{decision_id}")
def set_intelligence_decision_status(decision_id: str, body: DecisionStatus,
                                     c: Container = Depends(container)):
    """Approve, reject, cancel, or otherwise move a decision. Approval
    executes it through the existing Decision Engine and Action Queue."""
    try:
        updated = c.runtime.intelligence.set_status(
            decision_id, body.status, by=body.by, note=body.note)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    if updated is None:
        raise HTTPException(status_code=404, detail="Decision not found")
    return updated


# ---------------------------------------------------------------- triggers
class TriggerCreate(BaseModel):
    name: str
    event: str
    action: str
    conditions: list[dict] = Field(default_factory=list)
    params: dict = Field(default_factory=dict)
    description: str = ""
    enabled: bool = True


@router.get("/runtime/triggers")
def triggers(event: str = "", c: Container = Depends(container)):
    return {"rules": c.runtime.triggers.rules(event=event),
            "stats": c.runtime.triggers.stats()}


@router.post("/runtime/triggers", status_code=201)
def create_trigger(body: TriggerCreate, c: Container = Depends(container)):
    try:
        return c.runtime.triggers.add_rule(
            body.name, body.event, body.action, conditions=body.conditions,
            params=body.params, description=body.description,
            enabled=body.enabled)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


class TriggerEnabled(BaseModel):
    enabled: bool


@router.patch("/runtime/triggers/{rule_id}")
def set_trigger_enabled(rule_id: str, body: TriggerEnabled,
                        c: Container = Depends(container)):
    updated = c.runtime.triggers.set_enabled(rule_id, body.enabled)
    if updated is None:
        raise HTTPException(status_code=404, detail="Trigger rule not found")
    return updated


@router.delete("/runtime/triggers/{rule_id}", status_code=204)
def delete_trigger(rule_id: str, c: Container = Depends(container)):
    if not c.runtime.triggers.delete_rule(rule_id):
        raise HTTPException(status_code=404, detail="Trigger rule not found")

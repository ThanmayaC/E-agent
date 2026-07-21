"""Executive Workspace APIs (Manager Module).

The business-facing surface: dashboard, workspace, daily brief, tasks,
decisions, notifications, report reviews, and portfolio. No technical
internals (knowledge graph, memory, embeddings, prompts, LangGraph) are
exposed here.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel

from app.api.deps import container
from app.core.container import Container

router = APIRouter(tags=["manager"])


# ------------------------------------------------------------- workspace
@router.get("/manager/dashboard")
def dashboard(c: Container = Depends(container)):
    """Executive dashboard: business health, operational status, portfolio
    summary, recommended actions, automation status."""
    return c.manager.dashboard()


@router.get("/manager/workspace")
def workspace(c: Container = Depends(container)):
    """The full Manager Workspace payload (every executive panel)."""
    return c.manager.workspace()


@router.get("/manager/overnight")
def overnight(hours: int = Query(16, ge=1, le=72),
              c: Container = Depends(container)):
    """Overnight Summary (V2): what the platform did autonomously — workflow
    runs, executed actions, drafts awaiting approval, reports, notifications."""
    return c.manager.overnight_summary(hours=hours)


@router.get("/manager/daily-brief")
def daily_brief(regenerate: bool = False, c: Container = Depends(container)):
    """Today's executive brief (auto-generated; regenerate on demand)."""
    return c.daily_brief.generate() if regenerate else c.daily_brief.today()


@router.get("/manager/daily-brief/history")
def daily_brief_history(limit: int = Query(14, ge=1, le=60),
                        c: Container = Depends(container)):
    return c.daily_brief.history(limit)


# ------------------------------------------------------------------ tasks
class TaskCreate(BaseModel):
    title: str
    detail: str = ""
    priority: int | None = None
    due_date: str = ""
    owner: str = ""
    project_id: str = ""


class TaskStatus(BaseModel):
    status: str


@router.get("/manager/tasks")
def tasks(status: str = "", c: Container = Depends(container)):
    return {"tasks": c.exec_tasks.tasks(status=status),
            "stats": c.exec_tasks.stats()}


@router.post("/manager/tasks", status_code=201)
def create_task(body: TaskCreate, c: Container = Depends(container)):
    task = c.exec_tasks.create(body.title, detail=body.detail,
                               priority=body.priority,
                               due_date=body.due_date, owner=body.owner,
                               project_id=body.project_id)
    if task is None:
        raise HTTPException(status_code=409, detail="Equivalent task exists")
    return task


@router.patch("/manager/tasks/{task_id}")
def update_task(task_id: str, body: TaskStatus,
                c: Container = Depends(container)):
    try:
        task = c.exec_tasks.update_status(task_id, body.status)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


# -------------------------------------------------------------- decisions
class DecisionCreate(BaseModel):
    decision: str
    owner: str = ""
    impact: str = ""
    context: str = ""
    project_id: str = ""
    evidence_ids: list[str] = []


class DecisionUpdate(BaseModel):
    status: str = ""
    owner: str = ""
    impact: str = ""
    by: str = ""


@router.get("/manager/decisions")
def decisions(status: str = "", c: Container = Depends(container)):
    return {"decisions": c.decisions.decisions(status=status),
            "stats": c.decisions.stats()}


@router.post("/manager/decisions", status_code=201)
def record_decision(body: DecisionCreate, c: Container = Depends(container)):
    try:
        return c.decisions.record(body.decision, owner=body.owner,
                                  impact=body.impact, context=body.context,
                                  project_id=body.project_id,
                                  evidence_ids=body.evidence_ids)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


@router.patch("/manager/decisions/{decision_id}")
def update_decision(decision_id: str, body: DecisionUpdate,
                    c: Container = Depends(container)):
    try:
        decision = c.decisions.update(decision_id, status=body.status,
                                      owner=body.owner, impact=body.impact,
                                      by=body.by)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    if decision is None:
        raise HTTPException(status_code=404, detail="Decision not found")
    return decision


# ---------------------------------------------------------- notifications
@router.get("/manager/notifications")
def notifications(unread: bool = False, limit: int = Query(30, ge=1, le=200),
                  c: Container = Depends(container)):
    return {"notifications": c.notifications.recent(limit,
                                                    unread_only=unread),
            "stats": c.notifications.stats()}


@router.post("/manager/notifications/{notification_id}/read")
def mark_read(notification_id: str, c: Container = Depends(container)):
    if not c.notifications.mark_read(notification_id):
        raise HTTPException(status_code=404, detail="Notification not found")
    return {"status": "read"}


@router.post("/manager/notifications/read-all")
def mark_all_read(c: Container = Depends(container)):
    return {"marked_read": c.notifications.mark_all_read()}


# ---------------------------------------------------------- report reviews
class ReviewStatus(BaseModel):
    status: str
    by: str = ""
    note: str = ""


@router.get("/manager/reports")
def report_reviews(status: str = "", c: Container = Depends(container)):
    """Report Review Center: every report with its review status."""
    return {"reviews": c.reviews.reviews(status=status),
            "stats": c.reviews.stats()}


@router.post("/manager/reports/{review_id}/status")
def set_review_status(review_id: str, body: ReviewStatus,
                      c: Container = Depends(container)):
    try:
        return c.reviews.set_status(review_id, body.status, by=body.by,
                                    note=body.note)
    except KeyError:
        raise HTTPException(status_code=404, detail="Review not found")
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


# --------------------------------------------------------------- portfolio
@router.get("/manager/portfolio")
def portfolio(c: Container = Depends(container)):
    return c.portfolio.overview()


# ------------------------------------------------ organization and search
@router.get("/manager/organization")
def organization(c: Container = Depends(container)):
    """Organization Overview for the executive: business entity counts,
    connected systems, knowledge freshness, recent synchronizations."""
    return c.manager.organization()


@router.get("/manager/search")
def search(q: str = Query(..., min_length=1),
           limit: int = Query(20, ge=1, le=100),
           c: Container = Depends(container)):
    """One question across everything the organization knows."""
    return c.manager.search(q, limit=limit)


# ---------------------------------------------------------------- products
@router.get("/manager/products")
def products(c: Container = Depends(container)):
    """The executive product view: portfolio position, products needing
    attention, growth opportunities, and recommended strategy."""
    return c.manager.products()


@router.get("/manager/product-reviews")
def product_reviews(limit: int = Query(5, ge=1, le=50),
                    c: Container = Depends(container)):
    """Executive Reviews: the latest product review per product."""
    return {"reviews": c.manager.product_reviews(limit=limit)}


# -------------------------------------------------- automation preparation
@router.get("/manager/integrations")
def integrations(c: Container = Depends(container)):
    """Future integration slots (email, calendar, meetings, messaging,
    documents, tasks) — interfaces prepared, providers arrive in V2."""
    return c.providers.describe()


# ------------------------------------------------ Outlook / Teams (read-only)
# Reading email and Teams is another enterprise knowledge source. These
# surfaces never send or post — outbound stays behind the Action Queue's
# approval layer. When a channel is not configured they answer with a clear
# reason and an empty result, exactly as the platform degrades everywhere else.
def _read_provider(c: Container, kind: str):
    """The registered adapter for a provider kind, unwrapped past the
    'available' gate the registry applies to *outbound* use — reading has its
    own availability, so the adapter itself decides."""
    provider = c.providers._providers.get(kind)  # noqa: SLF001 — read view
    if provider is None:
        raise HTTPException(status_code=404,
                            detail=f"no {kind} provider registered")
    return provider


@router.get("/manager/outlook/messages")
def outlook_messages(folder: str = Query("inbox"),
                     top: int = Query(25, ge=1, le=100),
                     c: Container = Depends(container)):
    """Recent Outlook messages (read-only)."""
    provider = _read_provider(c, "email")
    if not getattr(provider, "available", False):
        return {"available": False, "messages": [],
                "reason": provider.unavailable_reason}
    return {"available": True,
            "messages": provider.read_messages(folder=folder, top=top)}


@router.get("/manager/outlook/search")
def outlook_search(q: str = Query(..., min_length=2),
                   top: int = Query(25, ge=1, le=100),
                   c: Container = Depends(container)):
    """Search historical Outlook email (read-only)."""
    provider = _read_provider(c, "email")
    if not getattr(provider, "available", False):
        return {"available": False, "messages": [],
                "reason": provider.unavailable_reason}
    return {"available": True,
            "messages": provider.search_messages(q, top=top)}


@router.get("/manager/teams/channels")
def teams_channels(team_id: str = Query(...),
                   c: Container = Depends(container)):
    """List a team's Teams channels (read-only)."""
    provider = _read_provider(c, "messaging")
    if not getattr(provider, "read_available", False):
        return {"available": False, "channels": [],
                "reason": provider.read_unavailable_reason}
    return {"available": True,
            "channels": provider.read_channels(team_id)}


@router.get("/manager/teams/messages")
def teams_messages(team_id: str = Query(...), channel_id: str = Query(...),
                   top: int = Query(25, ge=1, le=50),
                   c: Container = Depends(container)):
    """Read recent messages in a Teams channel (read-only)."""
    provider = _read_provider(c, "messaging")
    if not getattr(provider, "read_available", False):
        return {"available": False, "messages": [],
                "reason": provider.read_unavailable_reason}
    return {"available": True,
            "messages": provider.read_messages(team_id, channel_id, top=top)}

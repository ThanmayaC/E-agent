"""Enterprise Brain APIs — status, statistics, memory, learning, and the
unified Enterprise Context.

The Brain is deterministic organizational intelligence (Knowledge + Memory +
Graph + Learning); these endpoints expose its state to the dashboard and to
governance consumers. All read-only.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query

from app.api.deps import container, require_project
from app.core.container import Container

router = APIRouter(tags=["brain"])

# knowledge sections that constitute organizational memory
MEMORY_SECTIONS = ("decisions", "report_history", "strategic_insights",
                   "insights", "recommendations", "clarifications",
                   "learning_events")


@router.get("/brain/status")
def brain_status(c: Container = Depends(container)):
    """Runtime state of the Enterprise Brain (READY after startup checks)."""
    if c.brain is None:
        return {"state": "disabled",
                "detail": "EDIP_BRAIN_ENABLED is false"}
    return c.brain.status()


@router.get("/brain/statistics")
def brain_statistics(c: Container = Depends(container)):
    """Knowledge, memory, graph, learning, and clarification statistics."""
    if c.brain is None:
        return {"state": "disabled"}
    return c.brain.statistics()


@router.get("/learning/history")
def learning_history(limit: int = Query(50, ge=1, le=500),
                     c: Container = Depends(container)):
    """Continuous-learning events, newest last: what was learned, from
    where, and when."""
    return c.knowledge.learning_history(limit)


@router.get("/memory/search")
def memory_search(q: str = Query(..., min_length=2),
                  limit: int = Query(20, ge=1, le=100),
                  c: Container = Depends(container)):
    """Keyword search across organizational memory (decisions, reports,
    strategic insights, verified insights, recommendations,
    clarifications, learning events)."""
    hits = c.knowledge.search(q, limit=100)
    memory_hits = [h for h in hits if h.get("section") in MEMORY_SECTIONS]
    return memory_hits[:limit]


@router.get("/projects/{project_id}/enterprise-context")
def enterprise_context(project_id: str, c: Container = Depends(container)):
    """The unified Enterprise Context (facts + organizational knowledge,
    memory, and graph) — the only input the Prompt Engine consumes."""
    require_project(c, project_id)
    context = c.store.load(project_id, "enterprise_context")
    if context:
        return context
    if c.brain is None:
        raise HTTPException(status_code=404, detail=(
            "No enterprise context exists and the Enterprise Brain is "
            "disabled"))
    return c.brain.build_enterprise_context(project_id)

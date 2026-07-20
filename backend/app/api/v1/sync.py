"""Enterprise Knowledge Synchronization APIs.

The data-source registry, synchronization control, the organizational model,
and unified enterprise search. APIs only — no business logic in this module.

Nothing here can read or return a credential: sources hold auth by reference
(an environment variable name), and the registry's own contract refuses secret
values, so there is no code path from this router to a stored secret.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

from app.api.deps import container
from app.core.container import Container

router = APIRouter(tags=["synchronization"])


def _sync(c: Container):
    if c.sync is None:
        raise HTTPException(status_code=503,
                            detail="The synchronization layer is disabled")
    return c.sync


# ---------------------------------------------------------------- sources
class AuthRef(BaseModel):
    """Authentication by reference. The platform never stores credentials:
    ``ref`` names an environment variable that holds the secret."""
    kind: str = "none"     # none | env
    ref: str = ""


class SourceCreate(BaseModel):
    name: str
    kind: str
    location: str = ""     # path, base URL — never a credentialed URL
    auth: AuthRef = Field(default_factory=AuthRef)
    cadence: str = "hourly"
    description: str = ""
    options: dict = Field(default_factory=dict)
    project_id: str = ""


@router.get("/sources")
def sources(kind: str = "", health: str = "",
            c: Container = Depends(container)):
    """Every configured enterprise data source (credentials never included)."""
    layer = _sync(c)
    return {"sources": layer.registry.sources(kind=kind, health=health),
            "catalogue": layer.registry.kinds()}


@router.post("/sources", status_code=201)
def register_source(body: SourceCreate, c: Container = Depends(container)):
    """Connect an enterprise system. Interface-only kinds (SharePoint,
    Outlook, Teams) may be registered — they appear as awaiting their Version 2
    provider and are never synchronized."""
    try:
        return _sync(c).registry.register(
            body.name, body.kind, location=body.location,
            auth=body.auth.model_dump(), cadence=body.cadence,
            description=body.description, options=body.options,
            project_id=body.project_id)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


@router.get("/sources/status")
def sources_status(c: Container = Depends(container)):
    """Connected Systems: what is attached, healthy, and how fresh."""
    layer = _sync(c)
    return {**layer.registry.status(),
            "freshness": layer.pipeline.freshness(),
            "synchronization": layer.engine.stats()}


@router.post("/sources/sync")
def sync_sources(source_id: str = "", full: bool = False,
                 c: Container = Depends(container)):
    """Manual refresh. Without ``source_id`` every due source synchronizes and
    organizational knowledge refreshes; ``full=true`` forces a complete
    re-read instead of a delta."""
    layer = _sync(c)
    if source_id and layer.registry.get(source_id) is None:
        raise HTTPException(status_code=404, detail="Source not found")
    return layer.pipeline.refresh(source_id=source_id, trigger="manual",
                                  force_full=full).describe()


@router.get("/sources/{source_id}")
def source(source_id: str, c: Container = Depends(container)):
    layer = _sync(c)
    found = layer.registry.get(source_id)
    if found is None:
        raise HTTPException(status_code=404, detail="Source not found")
    return {"source": found, "runs": layer.engine.runs(source_id, limit=20)}


class SourceUpdate(BaseModel):
    enabled: bool | None = None
    cadence: str | None = None


@router.patch("/sources/{source_id}")
def update_source(source_id: str, body: SourceUpdate,
                  c: Container = Depends(container)):
    layer = _sync(c)
    if layer.registry.get(source_id) is None:
        raise HTTPException(status_code=404, detail="Source not found")
    try:
        updated = None
        if body.cadence is not None:
            updated = layer.registry.set_cadence(source_id, body.cadence)
        if body.enabled is not None:
            updated = layer.registry.set_enabled(source_id, body.enabled)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    return updated or layer.registry.get(source_id)


@router.post("/sources/{source_id}/health")
def check_source_health(source_id: str, c: Container = Depends(container)):
    layer = _sync(c)
    if layer.registry.get(source_id) is None:
        raise HTTPException(status_code=404, detail="Source not found")
    return layer.registry.check_health(source_id)


@router.delete("/sources/{source_id}", status_code=204)
def remove_source(source_id: str, c: Container = Depends(container)):
    if not _sync(c).registry.remove(source_id):
        raise HTTPException(status_code=404, detail="Source not found")


# ----------------------------------------------------------------- search
@router.get("/search")
def search(q: str = Query(..., min_length=1),
           surfaces: str = "", limit: int = Query(30, ge=1, le=100),
           c: Container = Depends(container)):
    """Unified enterprise search across every surface the platform holds."""
    wanted = [s.strip() for s in surfaces.split(",") if s.strip()]
    return _sync(c).search.search(q, surfaces=wanted or None, limit=limit)


@router.get("/search/enterprise")
def search_enterprise(q: str = Query(..., min_length=1),
                      limit: int = Query(30, ge=1, le=100),
                      c: Container = Depends(container)):
    """Enterprise search with its surface catalogue — one query, everything
    the organization knows."""
    layer = _sync(c)
    return {**layer.search.search(q, limit=limit),
            "surfaces": layer.search.surfaces()}


# ----------------------------------------------------------- organization
@router.get("/organization")
def organization(c: Container = Depends(container)):
    """Organization Overview: what the enterprise contains, what is connected,
    how fresh its knowledge is. Business framing only."""
    return _sync(c).overview()


@router.get("/organization/entities")
def entities(kind: str = "", owner: str = "", q: str = "",
             project_id: str = "", limit: int = Query(200, ge=1, le=1000),
             c: Container = Depends(container)):
    """Enterprise entities with identity, ownership, and provenance."""
    layer = _sync(c)
    return {"entities": layer.organization.entities(
                kind=kind, owner=owner, query=q, project_id=project_id,
                limit=limit),
            "counts": layer.organization.counts(),
            "kinds": list(layer.organization.counts())}


@router.get("/organization/entities/{entity_id:path}")
def entity(entity_id: str, c: Container = Depends(container)):
    """One entity with its history and everything it is wired to."""
    layer = _sync(c)
    found = layer.organization.get(entity_id)
    if found is None:
        raise HTTPException(status_code=404, detail="Entity not found")
    return {"entity": found,
            "history": found["history"],
            "related": layer.relationships.neighbourhood(entity_id)["related"]}


@router.get("/organization/relationships")
def relationships(kind: str = "", entity_id: str = "",
                  min_confidence: float = Query(0.0, ge=0.0, le=1.0),
                  limit: int = Query(200, ge=1, le=1000),
                  c: Container = Depends(container)):
    """How the organization is wired, with the evidence for each link."""
    layer = _sync(c)
    return {"relationships": layer.relationships.relationships(
                kind=kind, entity_id=entity_id, min_confidence=min_confidence,
                limit=limit),
            "stats": layer.relationships.stats()}


@router.get("/organization/refreshes")
def refreshes(limit: int = Query(20, ge=1, le=100),
              c: Container = Depends(container)):
    """The Knowledge Refresh Pipeline's history, stage by stage."""
    layer = _sync(c)
    return {"refreshes": layer.pipeline.events(limit),
            "freshness": layer.pipeline.freshness()}

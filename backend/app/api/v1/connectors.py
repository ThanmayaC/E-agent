"""Enterprise Data Sources — the administration API for the Connector
Framework.

Administrators register, edit, enable, test, and manually synchronize
enterprise data sources here. Managers never see this router: the Executive
Workspace receives fresh reports, insights, summaries, approvals, and
notifications, and is never asked to configure a connector or know that one
exists.

Nothing here can read or return a credential. A source holds auth by
reference (an environment variable name), the service refuses secret values
on the way in, and ``describe()`` is the only view on the way out — so there
is no code path from this router to a stored secret.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

from app.api.deps import container
from app.connectors.registry import ConnectorNotRegistered
from app.core.container import Container

router = APIRouter(prefix="/connectors", tags=["enterprise data sources"])


def _framework(c: Container):
    framework = getattr(c, "connector_framework", None)
    if framework is None:
        raise HTTPException(
            status_code=503,
            detail="The Enterprise Connector Framework is disabled")
    return framework


def _service(c: Container):
    return _framework(c).service


def _require(service, connector_id: str) -> dict:
    record = service.get(connector_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Data source not found")
    return record


# --------------------------------------------------- the other source registry
# The platform has two registries that both hold enterprise data sources: this
# framework's own store, and the older Synchronization Layer's
# ``DataSourceRegistry`` (which is what the enterprise-demo bootstrap and every
# document folder register into). They are deliberately not merged in storage —
# the sync layer owns its ingestion path and re-registering its folders here
# would ingest every document twice. But an administrator asking "what data
# sources does this platform have?" must be told about all of them, so the
# *read* side reports both, each tagged with where it came from.

def _sync_registry(c: Container):
    sync = getattr(c, "sync", None)
    return getattr(sync, "registry", None) if sync is not None else None


def _as_source_record(source: dict) -> dict:
    """Present a Synchronization Layer source in the shape this API's clients
    already consume, without pretending it is a connector — ``read_only``
    says the connector actions (test/discover/sync/delete) do not apply."""
    return {
        "connector_id": source.get("source_id", ""),
        "name": source.get("name", ""),
        "kind": source.get("kind", ""),
        "location": source.get("location", ""),
        "description": source.get("description", ""),
        "cadence": source.get("cadence", ""),
        "enabled": source.get("enabled", True),
        "health": source.get("health", "unknown"),
        "health_detail": source.get("health_detail", ""),
        "last_synced_at": source.get("last_synced_at", ""),
        "last_sync_status": source.get("last_sync_status", ""),
        "items_total": source.get("records_total", 0),
        "origin": "sync_layer",
        "read_only": True,
    }


def _merged_status(c: Container) -> dict:
    """Data-source totals across both registries.

    A count that ignores half the platform's sources is worse than no count:
    it reads as "nothing is connected" while the Brain is answering questions
    from 70 ingested folders.
    """
    service = _service(c)
    status = dict(service.status())
    status["by_origin"] = {"connector_framework": status["total"]}

    registry = _sync_registry(c)
    if registry is None:
        return status

    sync_sources = registry.sources()
    sync_status = registry.status()
    status["by_origin"]["sync_layer"] = len(sync_sources)
    status["total"] += len(sync_sources)
    status["enabled"] += sum(1 for s in sync_sources if s.get("enabled"))
    status["healthy"] += sync_status.get("connected", 0)
    status["needs_attention"] += sync_status.get("needs_attention", 0)
    status["items_total"] += sync_status.get("records_total", 0)
    for bucket, counts in (("by_health", sync_status.get("by_health", {})),
                           ("by_kind", sync_status.get("by_kind", {}))):
        merged = dict(status.get(bucket, {}))
        for key, value in counts.items():
            merged[key] = merged.get(key, 0) + value
        status[bucket] = merged
    last = [t for t in (status.get("last_sync_at"),
                        sync_status.get("last_sync_at")) if t]
    status["last_sync_at"] = max(last) if last else ""
    return status


# ------------------------------------------------------------- catalogue
@router.get("")
def overview(c: Container = Depends(container)):
    """Everything the Admin console needs on one call: what is connected,
    how healthy it is, and what else could be connected.

    Counts span both source registries — see ``_merged_status``."""
    status = _framework(c).status()
    return {**status, "sources": _merged_status(c)}


@router.get("/catalogue")
def catalogue(c: Container = Depends(container)):
    """Connector kinds: available now, unavailable here, and planned."""
    return {"catalogue": _framework(c).registry.describe()}


# ------------------------------------------------------------ registration
class AuthRef(BaseModel):
    """Authentication by reference — ``ref`` names an environment variable
    that holds the secret. The platform never stores credentials."""
    kind: str = "none"      # none | env
    ref: str = ""


class SourceCreate(BaseModel):
    name: str
    kind: str                       # folder | excel | csv | postgresql | ...
    location: str = ""              # path or host — never a credentialed URL
    auth: AuthRef = Field(default_factory=AuthRef)
    cadence: str = "hourly"         # startup | 15m | hourly | daily | weekly | manual
    description: str = ""
    options: dict = Field(default_factory=dict)
    project_id: str = ""
    enabled: bool = True


class SourceUpdate(BaseModel):
    name: str | None = None
    location: str | None = None
    cadence: str | None = None
    enabled: bool | None = None
    description: str | None = None
    options: dict | None = None
    project_id: str | None = None


@router.get("/sources")
def sources(kind: str = "", health: str = "",
            c: Container = Depends(container)):
    """Every configured enterprise data source (credentials never included).

    Includes the Synchronization Layer's sources, tagged ``origin`` and
    ``read_only`` — they are real, ingesting sources, they simply are not
    administered through this framework's actions."""
    service = _service(c)
    own = [{**s, "origin": "connector_framework", "read_only": False}
           for s in service.sources(kind=kind, health=health)]

    registry = _sync_registry(c)
    if registry is None:
        return {"sources": own, "status": _merged_status(c)}

    merged = own + [_as_source_record(s)
                    for s in registry.sources(kind=kind, health=health)]
    return {"sources": merged, "status": _merged_status(c)}


@router.post("/sources", status_code=201)
def register_source(body: SourceCreate, c: Container = Depends(container)):
    """Connect an enterprise data source. Validated on the way in: a
    misconfiguration is refused here, not discovered at 03:00."""
    try:
        return _service(c).register(
            body.name, body.kind, location=body.location,
            auth=body.auth.model_dump(), cadence=body.cadence,
            description=body.description, options=body.options,
            project_id=body.project_id, enabled=body.enabled)
    except ConnectorNotRegistered as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


@router.get("/sources/{connector_id}")
def source(connector_id: str, c: Container = Depends(container)):
    """One source with its recent runs and failures."""
    service = _service(c)
    record = _require(service, connector_id)
    return {"source": record,
            "runs": service.runs(connector_id, limit=20),
            "failures": service.failures(connector_id, limit=20),
            "packages": service.packages(connector_id, limit=50)}


@router.patch("/sources/{connector_id}")
def update_source(connector_id: str, body: SourceUpdate,
                  c: Container = Depends(container)):
    """Edit a source. Changes take effect on the next synchronization."""
    service = _service(c)
    _require(service, connector_id)
    fields = {k: v for k, v in body.model_dump().items() if v is not None}
    if not fields:
        return service.get(connector_id)
    try:
        return service.update(connector_id, **fields)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


@router.delete("/sources/{connector_id}", status_code=204)
def remove_source(connector_id: str, c: Container = Depends(container)):
    """Disconnect a source. Knowledge already ingested from it is kept —
    deleting organizational knowledge is a separate, audited decision."""
    if not _service(c).remove(connector_id):
        raise HTTPException(status_code=404, detail="Data source not found")


# ---------------------------------------------------------------- actions
@router.post("/sources/{connector_id}/test")
def test_connection(connector_id: str, c: Container = Depends(container)):
    """Test connection. Always answers — a failure is a result, not a 500."""
    service = _service(c)
    _require(service, connector_id)
    return service.test_connection(connector_id)


@router.post("/sources/{connector_id}/discover")
def discover(connector_id: str, c: Container = Depends(container)):
    """What the source holds: files, sheets, tables. Metadata only."""
    service = _service(c)
    _require(service, connector_id)
    return service.discover(connector_id)


@router.post("/sources/{connector_id}/health")
def check_health(connector_id: str, c: Container = Depends(container)):
    service = _service(c)
    _require(service, connector_id)
    return service.check_health(connector_id)


@router.post("/sources/{connector_id}/sync")
def sync_source(connector_id: str, full: bool = False,
                c: Container = Depends(container)):
    """Manual synchronization of one source. ``full=true`` forces a complete
    re-read instead of an incremental one."""
    service = _service(c)
    _require(service, connector_id)
    return service.sync_one(connector_id, full=full, trigger="manual")


@router.post("/sync")
def sync_all(full: bool = False, c: Container = Depends(container)):
    """Manual synchronization of every enabled source."""
    return _service(c).sync_all(full=full)


# ---------------------------------------------------------------- history
@router.get("/runs")
def runs(connector_id: str = "", limit: int = Query(50, ge=1, le=200),
         c: Container = Depends(container)):
    """Synchronization history, newest first."""
    return {"runs": _service(c).runs(connector_id, limit=limit)}


@router.get("/failures")
def failures(connector_id: str = "", limit: int = Query(50, ge=1, le=200),
             c: Container = Depends(container)):
    """Every recorded failure, with the error and the attempt count."""
    return {"failures": _service(c).failures(connector_id, limit=limit)}


@router.get("/packages")
def packages(connector_id: str = "", limit: int = Query(100, ge=1, le=500),
             c: Container = Depends(container)):
    """The Knowledge Package catalogue: what the connectors have produced.
    Metadata and checksums only — content lives in the document store."""
    return {"packages": _service(c).packages(connector_id, limit=limit)}

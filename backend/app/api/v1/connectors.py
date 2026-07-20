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


# ------------------------------------------------------------- catalogue
@router.get("")
def overview(c: Container = Depends(container)):
    """Everything the Admin console needs on one call: what is connected,
    how healthy it is, and what else could be connected."""
    return _framework(c).status()


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
    """Every configured enterprise data source (credentials never included)."""
    service = _service(c)
    return {"sources": service.sources(kind=kind, health=health),
            "status": service.status()}


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

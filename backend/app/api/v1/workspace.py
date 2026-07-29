"""Enterprise AI Workspace APIs (V9.0).

The AI-first surface: universal file upload + AI understanding, unified
enterprise search, artifact generation & download, the conversational home feed,
pins / saved items, and the AI-sidebar context. All read-only over the existing
platform except uploads, artifacts and pins, which write only inside the
workspace directory. Every endpoint degrades gracefully when a layer is absent.
"""
from __future__ import annotations

from fastapi import (APIRouter, Depends, HTTPException, Query, UploadFile)
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from app.api.deps import container
from app.core.container import Container

router = APIRouter(tags=["workspace"])


def _ws(c: Container):
    ws = getattr(c, "workspace", None)
    if ws is None:
        raise HTTPException(503, "The AI Workspace is not available")
    return ws


@router.get("/workspace")
def workspace_status(c: Container = Depends(container)):
    """Is the workspace live; supported file types and artifact kinds."""
    return _ws(c).status()


@router.get("/workspace/home")
def workspace_home(c: Container = Depends(container)):
    """The conversational home feed: recent chats, files, reports,
    suggestions, recommendations, pins and artifacts."""
    return _ws(c).home()


# --------------------------------------------------------------- file upload
@router.post("/workspace/upload")
async def workspace_upload(files: list[UploadFile],
                           c: Container = Depends(container)):
    """Upload one or many files (drag-drop / folder). Each is understood
    automatically: type, text, tables, entities, dates, KPIs, summary, tags,
    recommendations, and Knowledge-Graph links."""
    ws = _ws(c)
    max_bytes = c.settings.max_upload_mb * 1024 * 1024
    results, errors = [], []
    for f in files:
        name = f.filename or "upload"
        if not ws.accepts(name):
            errors.append({"file": name, "error": "unsupported type"})
            continue
        content = await f.read()
        if len(content) > max_bytes:
            errors.append({"file": name,
                           "error": f"exceeds {c.settings.max_upload_mb} MB"})
            continue
        results.append(ws.save_upload(name, content))
    return {"understood": results, "errors": errors,
            "count": len(results)}


@router.get("/workspace/files")
def workspace_files(c: Container = Depends(container)):
    return {"files": _ws(c).list_files()}


@router.get("/workspace/files/{fid}")
def workspace_file(fid: str, c: Container = Depends(container)):
    return _ws(c).get_file(fid)


@router.delete("/workspace/files/{fid}")
def workspace_delete_file(fid: str, c: Container = Depends(container)):
    return _ws(c).delete_file(fid)


@router.post("/workspace/files/{fid}/understand")
def workspace_reunderstand(fid: str, c: Container = Depends(container)):
    return _ws(c).understand(fid)


# ------------------------------------------------------------------- search
@router.get("/workspace/search")
def workspace_search(q: str = "", limit: int = Query(40, ge=1, le=100),
                     c: Container = Depends(container)):
    """Unified enterprise search across every surface."""
    return _ws(c).search(q, limit)


# ---------------------------------------------------------------- artifacts
class ArtifactRequest(BaseModel):
    kind: str = Field("executive_report")
    title: str = ""
    prompt: str = ""
    fmt: str = ""
    sections: list[dict] | None = None


@router.post("/workspace/artifacts")
def workspace_generate_artifact(body: ArtifactRequest,
                                c: Container = Depends(container)):
    """Generate a downloadable artifact (PowerPoint/Excel/Word/PDF/email/
    executive report/RCA/minutes/action items/roadmap/business case)."""
    return _ws(c).generate_artifact(body.kind, title=body.title,
                                    prompt=body.prompt, sections=body.sections,
                                    fmt=body.fmt)


@router.get("/workspace/artifacts")
def workspace_list_artifacts(c: Container = Depends(container)):
    return {"artifacts": _ws(c).list_artifacts()}


@router.get("/workspace/artifacts/{name}")
def workspace_download_artifact(name: str, c: Container = Depends(container)):
    path = _ws(c).artifact_path(name)
    if not path:
        raise HTTPException(404, "artifact not found")
    return FileResponse(str(path), filename=path.name)


# --------------------------------------------------------------- pins/saved
class PinRequest(BaseModel):
    bucket: str = "pins"
    item: dict


@router.get("/workspace/pins")
def workspace_pins(c: Container = Depends(container)):
    return _ws(c).pins()


@router.post("/workspace/pins", status_code=201)
def workspace_add_pin(body: PinRequest, c: Container = Depends(container)):
    return _ws(c).add_pin(body.bucket, body.item)


@router.delete("/workspace/pins/{bucket}/{item_id}")
def workspace_remove_pin(bucket: str, item_id: str,
                         c: Container = Depends(container)):
    return _ws(c).remove_pin(bucket, item_id)


# ----------------------------------------------------------------- context
@router.get("/workspace/context")
def workspace_context(page: str = "", c: Container = Depends(container)):
    """What the AI sidebar knows about the user's current situation."""
    return _ws(c).context(page)

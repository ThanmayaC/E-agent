"""Project lifecycle: create, upload, analyze, status."""
from __future__ import annotations

import re
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, UploadFile
from pydantic import BaseModel

from app.api.deps import container, require_project
from app.core.container import Container
from app.domain.entities import ProjectState

router = APIRouter(tags=["projects"])


class CreateProject(BaseModel):
    name: str


@router.post("/projects", status_code=201)
def create_project(body: CreateProject, c: Container = Depends(container)):
    project_id = re.sub(r"[^0-9a-z]+", "-", body.name.lower()).strip("-")[:40] or "project"
    project_id = f"{project_id}-{uuid.uuid4().hex[:6]}"
    state = ProjectState(project_id=project_id, name=body.name,
                         created_at=datetime.now(timezone.utc))
    c.store.save(project_id, "state", state)
    return state


@router.get("/projects")
def list_projects(c: Container = Depends(container)):
    """Every project the user owns. States written by older builds can be
    missing their identity fields; they are backfilled from the directory id
    so such a project still renders — and stays deletable — in the UI."""
    projects = []
    for pid in c.store.list_projects():
        state = c.store.load(pid, "state")
        if not isinstance(state, dict) or not state:
            continue
        state.setdefault("project_id", pid)
        state.setdefault("name", pid)
        # no creation timestamp survived: fall back to when the report landed
        if not state.get("created_at"):
            state["created_at"] = state.get("report_generated_at")
        projects.append(state)
    projects.sort(key=lambda s: s.get("created_at") or "", reverse=True)
    return projects


@router.get("/projects/{project_id}")
def get_project(project_id: str, c: Container = Depends(container)):
    require_project(c, project_id)
    return c.store.load(project_id, "state")


@router.delete("/projects/{project_id}")
def delete_project(project_id: str, c: Container = Depends(container)):
    """Delete the project and everything it owns: metadata, uploaded files,
    generated datasets, cached analytics, reports, embeddings, knowledge
    graph, and workflow artifacts. Organization-wide knowledge (terms, rules,
    answered clarifications) is intentionally retained."""
    require_project(c, project_id)
    try:
        c.store.delete_project(project_id)
    except OSError as exc:
        raise HTTPException(
            409, f"Project files are in use and could not be deleted: {exc}")
    # control plane: purge everything the project owns; the audit log keeps
    # the record that it was deleted (never erased)
    c.ledger.purge_project(project_id)
    c.ledger.audit("project.deleted", project_id)
    return {"status": "deleted", "project_id": project_id}


@router.post("/projects/{project_id}/files")
async def upload_files(project_id: str, files: list[UploadFile],
                       c: Container = Depends(container)):
    require_project(c, project_id)
    saved = []
    max_bytes = c.settings.max_upload_mb * 1024 * 1024
    for f in files:
        # A file is acceptable when an AVAILABLE connector can ingest it.
        if not c.connectors.accepts(f.filename or ""):
            supported = ", ".join(c.connectors.supported_extensions())
            raise HTTPException(
                415, f"No connector available for: {f.filename}. Supported: {supported}")
        content = await f.read()
        if len(content) > max_bytes:
            raise HTTPException(413, f"{f.filename} exceeds {c.settings.max_upload_mb} MB limit")
        safe_name = re.sub(r"[^0-9a-zA-Z._ -]", "_", f.filename or "upload.xlsx")
        (c.store.uploads_dir(project_id) / safe_name).write_bytes(content)
        saved.append(safe_name)
    return {"uploaded": saved}


@router.post("/projects/{project_id}/analyze", status_code=202)
def analyze(project_id: str, tasks: BackgroundTasks, c: Container = Depends(container)):
    require_project(c, project_id)
    if not any(c.store.uploads_dir(project_id).iterdir()):
        raise HTTPException(400, "Upload at least one data source first")
    if c.settings.use_celery:
        from app.workers.tasks import run_pipeline
        run_pipeline.delay(project_id)
    else:
        tasks.add_task(c.workflows.run, "full_analysis", project_id)
    return {"status": "analyzing", "project_id": project_id}


@router.get("/projects/{project_id}/status")
def status(project_id: str, c: Container = Depends(container)):
    require_project(c, project_id)
    state = c.store.load(project_id, "state")
    return {"status": state.get("status"), "stages": state.get("stages", [])}


@router.get("/projects/{project_id}/clarifications")
def clarifications(project_id: str, c: Container = Depends(container)):
    """Understanding assessment: overall confidence, per-inference scores, and
    the clarification questions the platform needs answered before it will
    reason. Populated once analysis reaches the confidence-assessment stage."""
    require_project(c, project_id)
    understanding = c.store.load(project_id, "understanding")
    if understanding is None:
        raise HTTPException(404, "No understanding assessment yet — run /analyze first")
    return understanding


class ClarificationAnswer(BaseModel):
    question_id: str
    answer: str


class ClarificationAnswers(BaseModel):
    answers: list[ClarificationAnswer]


@router.post("/projects/{project_id}/clarifications", status_code=202)
def answer_clarifications(project_id: str, body: ClarificationAnswers,
                          tasks: BackgroundTasks, c: Container = Depends(container)):
    """Record clarification answers into enterprise knowledge (so an equivalent
    schema is never asked again) and resume the analysis. The re-run recalls
    these answers, clears the ambiguity, and proceeds to LLM reasoning."""
    require_project(c, project_id)
    understanding = c.store.load(project_id, "understanding")
    if understanding is None:
        raise HTTPException(404, "No clarification questions are pending for this project")
    by_id = {q["id"]: q for q in understanding.get("questions", [])}
    matched = {a.question_id: a.answer.strip() for a in body.answers
               if a.question_id in by_id and a.answer.strip()}
    if not matched:
        raise HTTPException(422, "No answers matched the pending clarification questions")

    # LangGraph orchestrator: the run is checkpointed at the confidence gate —
    # resume it in place; the gate node records the answers into enterprise
    # knowledge and the run continues from that exact node.
    awaiting = c.awaiting_run(project_id)
    if awaiting:
        tasks.add_task(c.orchestrator.resume, project_id, awaiting, matched)
        return {"status": "analyzing", "project_id": project_id,
                "answers_recorded": len(matched), "resumed_run": awaiting}

    # Legacy workflow: record the answers into enterprise knowledge here and
    # re-run — the fresh run recalls them and clears the ambiguity.
    canonical_by_kind = {"revenue_ambiguity": "Revenue",
                         "identifier_ambiguity": "Primary Identifier",
                         "time_ambiguity": "Reporting Period"}
    recorded = 0
    for question_id, answer in matched.items():
        q = by_id[question_id]
        # when the answer picks a candidate column, that becomes a permanent
        # schema alias — future datasets resolve it without asking
        aliases = [answer] if answer in q.get("candidates", []) else []
        canonical = canonical_by_kind.get(q.get("kind", ""))
        if aliases and canonical:
            c.knowledge.add_schema_alias(answer, canonical)
        c.knowledge.remember_clarification(
            question=q["question"], answer=answer,
            signature=q.get("signature", ""), project_id=project_id,
            kind=q.get("kind", ""), dataset=q.get("dataset", ""),
            confidence_before=understanding.get("confidence"),
            aliases=aliases)
        recorded += 1

    if c.settings.use_celery:
        from app.workers.tasks import run_pipeline
        run_pipeline.delay(project_id)
    else:
        tasks.add_task(c.workflows.run, "full_analysis", project_id)
    return {"status": "analyzing", "project_id": project_id, "answers_recorded": recorded}

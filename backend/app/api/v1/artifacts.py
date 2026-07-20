"""Read APIs for every pipeline artifact + analytics queries + copilot."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel

from app.api.deps import container, require_project
from app.core.container import Container
from app.intelligence.analytics.engine import AnalyticsEngine

router = APIRouter(tags=["artifacts"])


def _artifact(c: Container, project_id: str, name: str, default=None):
    require_project(c, project_id)
    data = c.store.load(project_id, name, default)
    if data is None:
        raise HTTPException(404, f"Artifact '{name}' not ready — run /analyze first")
    return data


@router.get("/projects/{project_id}/datasets")
def datasets(project_id: str, c: Container = Depends(container)):
    return _artifact(c, project_id, "profiles", [])


@router.get("/projects/{project_id}/datasets/{dataset_id}/preview")
def preview(project_id: str, dataset_id: str, limit: int = Query(50, le=500),
            c: Container = Depends(container)):
    require_project(c, project_id)
    engine = AnalyticsEngine(c.store.duckdb_path(project_id))
    try:
        return engine.preview(dataset_id, limit)
    except Exception as exc:
        raise HTTPException(404, f"Dataset not found: {exc}")


@router.get("/projects/{project_id}/semantics")
def semantics(project_id: str, c: Container = Depends(container)):
    return _artifact(c, project_id, "semantic_layer", [])


@router.get("/projects/{project_id}/relationships")
def relationships(project_id: str, c: Container = Depends(container)):
    return _artifact(c, project_id, "relationships", [])


@router.get("/projects/{project_id}/graph")
def graph(project_id: str, c: Container = Depends(container)):
    return _artifact(c, project_id, "graph")


@router.get("/projects/{project_id}/kpis")
def kpis(project_id: str, c: Container = Depends(container)):
    return _artifact(c, project_id, "kpis", [])


@router.get("/projects/{project_id}/signals")
def signals(project_id: str, c: Container = Depends(container)):
    """Deterministic statistical signals (facts only)."""
    return _artifact(c, project_id, "signals", [])


@router.get("/projects/{project_id}/ai-report")
def ai_report(project_id: str, c: Container = Depends(container)):
    """Full structured output of the AI reasoning pipeline."""
    return _artifact(c, project_id, "ai_report")


@router.get("/projects/{project_id}/insights")
def insights(project_id: str, c: Container = Depends(container)):
    """AI-generated insights (LLM reasoning over the business context).
    Every statement carries statement_type, evidence_ids, and its
    deterministic verification result."""
    ai = _artifact(c, project_id, "ai_report")
    return {"status": ai.get("status"), "error": ai.get("error", ""),
            "provider": ai.get("provider", ""), "model": ai.get("model", ""),
            "key_insights": ai.get("key_insights", []),
            "root_causes": ai.get("root_causes", []),
            "risks": ai.get("risks", []),
            "opportunities": ai.get("opportunities", []),
            "data_limitations": ai.get("data_limitations", [])}


def _index_evidence(node, index: dict) -> None:
    if isinstance(node, dict):
        if isinstance(node.get("id"), str) and node["id"]:
            index.setdefault(node["id"], node)
        for v in node.values():
            _index_evidence(v, index)
    elif isinstance(node, list):
        for v in node:
            _index_evidence(v, index)


@router.get("/projects/{project_id}/report/audit")
def report_audit(project_id: str, c: Container = Depends(container)):
    """Auditability: every generated statement with its statement type,
    verification result, confidence, cited evidence RESOLVED to the actual
    deterministic evidence items, and the missing evidence (for hypotheses)."""
    ai = _artifact(c, project_id, "ai_report")
    ctx = _artifact(c, project_id, "business_context")
    index: dict = {}
    _index_evidence(ctx, index)

    def entries(items, statement_key):
        out = []
        for it in items or []:
            if not isinstance(it, dict):
                continue
            ids = it.get("evidence_ids") or []
            out.append({
                "statement": it.get(statement_key, ""),
                "detail": it.get("detail") or it.get("possible_cause")
                or it.get("evidence") or "",
                "statement_type": it.get("statement_type"),
                "verification": it.get("verification", "unverified"),
                "confidence": it.get("confidence"),
                "evidence_ids": ids,
                "rejected_evidence_ids": it.get("rejected_evidence_ids", []),
                "evidence": [index[e] for e in ids if e in index],
                "supporting_metrics": it.get("supporting_metrics", []),
                "missing_evidence": it.get("missing_evidence", ""),
            })
        return out

    return {
        "status": ai.get("status"),
        "insights": entries(ai.get("key_insights"), "title"),
        "root_cause_hypotheses": entries(ai.get("root_causes"), "problem"),
        "risks": entries(ai.get("risks"), "risk"),
        "opportunities": entries(ai.get("opportunities"), "opportunity"),
        "recommendations": entries(ai.get("recommendations"), "action"),
        "data_limitations": ctx.get("data_limitations", {}),
    }


@router.get("/projects/{project_id}/predictions")
def predictions(project_id: str, c: Container = Depends(container)):
    return _artifact(c, project_id, "forecasts", [])


@router.get("/projects/{project_id}/recommendations")
def recommendations(project_id: str, c: Container = Depends(container)):
    """Recommendations: rule-derived deterministic ones (each citing the
    finding that triggered it) plus evidence-grounded AI ones."""
    ai = _artifact(c, project_id, "ai_report")
    report = c.store.load(project_id, "report") or {}
    return {"status": ai.get("status"), "error": ai.get("error", ""),
            "provider": ai.get("provider", ""), "model": ai.get("model", ""),
            "recommendations": ai.get("recommendations", []),
            "deterministic_recommendations":
                report.get("deterministic_recommendations", []),
            "priority_actions": ai.get("priority_actions", [])}


@router.get("/projects/{project_id}/context")
def business_context(project_id: str, c: Container = Depends(container)):
    """The compact business-context JSON sent to the LLM (transparency)."""
    return _artifact(c, project_id, "business_context")


@router.get("/projects/{project_id}/quality")
def quality(project_id: str, c: Container = Depends(container)):
    return _artifact(c, project_id, "quality")


@router.get("/projects/{project_id}/breakdowns")
def breakdowns(project_id: str, c: Container = Depends(container)):
    return _artifact(c, project_id, "breakdowns", [])


@router.get("/projects/{project_id}/report")
def report(project_id: str, c: Container = Depends(container)):
    return _artifact(c, project_id, "report")


@router.get("/projects/{project_id}/report/markdown")
def report_markdown(project_id: str, c: Container = Depends(container)):
    from app.reports.markdown import render_markdown
    data = _artifact(c, project_id, "report")
    return {"markdown": render_markdown(data)}


class Ask(BaseModel):
    question: str


@router.post("/projects/{project_id}/copilot/chat")
def copilot_chat(project_id: str, body: Ask, c: Container = Depends(container)):
    require_project(c, project_id)
    if not body.question.strip():
        raise HTTPException(422, "Question must not be empty")
    return c.copilot.ask(project_id, body.question.strip())


class SQLQuery(BaseModel):
    sql: str


@router.post("/projects/{project_id}/query")
def run_query(project_id: str, body: SQLQuery, c: Container = Depends(container)):
    require_project(c, project_id)
    sql = body.sql.strip().rstrip(";")
    if not sql.lower().startswith(("select", "with")):
        raise HTTPException(422, "Only read-only SELECT queries are allowed")
    engine = AnalyticsEngine(c.store.duckdb_path(project_id))
    try:
        return engine.query(sql)
    except Exception as exc:
        raise HTTPException(400, f"Query failed: {exc}")

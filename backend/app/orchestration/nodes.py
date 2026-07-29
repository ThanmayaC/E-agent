"""Deterministic graph nodes.

Each node wraps existing Intelligence Engine capabilities (kept intact —
ADR-001), records its lifecycle in the Evidence Ledger, and keeps the v1
stage stream (`ProjectState.stages`) updated so the existing UI works
unchanged whichever orchestrator is active.

Nodes contain NO analytics of their own and NO narrative — they sequence,
persist, and translate between graph state and the engines.
"""
from __future__ import annotations

import threading
from datetime import datetime, timezone

import numpy as np
from langgraph.types import interrupt
from pydantic import BaseModel

from app.core.logging import get_logger
from app.domain.entities import (
    AIReport, ProjectState, UnderstandingAssessment, WorkbookInfo,
)
from app.domain.enums import PipelineStage, StageStatus
from app.evidence.extract import extract_evidence
from app.intelligence.confidence.assessor import report_confidence
from app.intelligence.recommendations import RecommendationEngine
from app.orchestration.clarifications import record_answers
from app.orchestration.state import FRAMES, AnalysisState
from app.reports.generator import ReportAssembler

logger = get_logger(__name__)

_STATE_LOCK = threading.Lock()


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _native(obj):
    """Checkpointed state must be serializable: the deterministic engines
    leave numpy scalars inside dict/list fields (tolerated by the legacy JSON
    path), which the checkpointer's msgpack encoder rejects. Convert them to
    Python natives at the graph boundary — inside pydantic models too."""
    if isinstance(obj, np.generic):
        return obj.item()
    if isinstance(obj, dict):
        return {k: _native(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_native(v) for v in obj]
    if isinstance(obj, BaseModel):
        for name in obj.__class__.model_fields:
            v = getattr(obj, name)
            if isinstance(v, (dict, list, tuple, np.generic, BaseModel)):
                object.__setattr__(obj, name, _native(v))
        return obj
    return obj


class NodeContext:
    """Shared dependencies every node closes over (bound by the graph builder)."""

    def __init__(self, settings, store, intelligence, report_writer,
                 knowledge, ledger, brain=None, manager=None):
        self.settings = settings
        self.store = store
        self.intelligence = intelligence
        self.report_writer = report_writer
        self.knowledge = knowledge
        self.ledger = ledger
        self.brain = brain      # EnterpriseBrain (None => learning disabled)
        self.manager = manager  # ManagerWorkspace (None => no exec refresh)

    # -------------------------------------------------- v1 stage streaming
    def mark_stages(self, project_id: str, stages: list[PipelineStage],
                    status: StageStatus, detail: str = "") -> None:
        """Read-modify-write of the legacy ProjectState stage list. Locked:
        parallel branches update the same JSON artifact."""
        with _STATE_LOCK:
            raw = self.store.load(project_id, "state")
            if not raw:
                return
            try:
                state = ProjectState(**raw)
            except Exception:
                return
            for run in state.stages:
                if run.stage in stages:
                    if status == StageStatus.RUNNING:
                        run.started_at = _now()
                    else:
                        run.finished_at = run.finished_at or _now()
                    run.status = status
                    if detail:
                        run.detail = detail[:300]
            self.store.save(project_id, "state", state)

    def set_project_status(self, project_id: str, status: str, **fields) -> None:
        with _STATE_LOCK:
            raw = self.store.load(project_id, "state") or {}
            raw["status"] = status
            raw.update({k: v for k, v in fields.items() if v is not None})
            self.store.save(project_id, "state", raw)

    # ------------------------------------------------------- node wrapper
    def staged(self, node_name: str, stages: list[PipelineStage]):
        """Decorator: ledger events + v1 stage markers + failure accounting."""
        def wrap(fn):
            def run(state: AnalysisState) -> dict:
                pid, rid = state["project_id"], state["run_id"]
                self.ledger.record_event(rid, node_name, "started")
                self.mark_stages(pid, stages, StageStatus.RUNNING)
                try:
                    out = fn(state)
                except Exception as exc:
                    self.mark_stages(pid, stages, StageStatus.FAILED, str(exc))
                    self.ledger.record_event(rid, node_name, "failed",
                                             {"error": str(exc)[:500]})
                    raise
                self.mark_stages(pid, stages, StageStatus.COMPLETED)
                self.ledger.record_event(rid, node_name, "completed")
                return _native(out)
            run.__name__ = node_name
            return run
        return wrap


# --------------------------------------------------------------------- nodes
def build_nodes(ctx: NodeContext) -> dict:
    engine = ctx.intelligence
    s = ctx.settings

    @ctx.staged("ingest", [PipelineStage.FILE_DISCOVERY,
                           PipelineStage.WORKSHEET_DISCOVERY,
                           PipelineStage.DEDUPLICATION,
                           PipelineStage.SCHEMA_DISCOVERY,
                           PipelineStage.COLUMN_PROFILING,
                           PipelineStage.TIME_SERIES_DETECTION])
    def ingest(state: AnalysisState) -> dict:
        pid = state["project_id"]
        extracts = engine.ingest(pid)
        files = [e.info for e in extracts]
        with _STATE_LOCK:
            raw = ctx.store.load(pid, "state") or {}
            raw["files"] = [f.model_dump() for f in files]
            ctx.store.save(pid, "state", raw)
        tables = [t for e in extracts for t in e.tables]
        if not tables:
            raise ValueError("No readable tables found in uploaded sources")
        merged, lineage = engine.deduplicate(pid, tables)
        profiles, frames = engine.profile(merged, lineage)
        engine.timeseries(profiles, frames)
        FRAMES.put(state["run_id"], frames)
        return {"profiles": profiles}

    @ctx.staged("understanding", [PipelineStage.BUSINESS_MEANING,
                                  PipelineStage.SEMANTIC_LAYER,
                                  PipelineStage.RELATIONSHIP_DETECTION])
    def understanding(state: AnalysisState) -> dict:
        pid = state["project_id"]
        frames = FRAMES.get(state["run_id"])
        mappings = engine.semantics(pid, state["profiles"])
        relationships = engine.relationships(pid, state["profiles"], frames)
        return {"mappings": mappings, "relationships": relationships}

    @ctx.staged("quality", [PipelineStage.DATA_QUALITY])
    def quality(state: AnalysisState) -> dict:
        frames = FRAMES.get(state["run_id"])
        report = engine.quality(state["project_id"], state["profiles"], frames)
        return {"quality": report}

    @ctx.staged("quant", [PipelineStage.KPI_DISCOVERY, PipelineStage.ANALYTICS,
                          PipelineStage.SIGNALS, PipelineStage.PREDICTIONS])
    def quant(state: AnalysisState) -> dict:
        pid = state["project_id"]
        frames = FRAMES.get(state["run_id"])
        kpis = engine.kpis(state["profiles"], frames)
        breakdowns = engine.warehouse(pid, state["profiles"], frames)
        signals = engine.signals(pid, kpis, breakdowns)
        forecasts = engine.forecasts(pid, kpis)
        # What the data can actually support — computed here, while the period
        # coverage from KPI discovery is still in hand, and carried through the
        # run so the context builder and the report both gate on the same facts.
        feasibility = engine.feasibility(state["profiles"], kpis)
        return {"kpis": kpis, "breakdowns": breakdowns,
                "signals": signals, "forecasts": forecasts,
                "feasibility": feasibility}

    @ctx.staged("graph_build", [PipelineStage.KNOWLEDGE_GRAPH])
    def graph_build(state: AnalysisState) -> dict:
        engine.knowledge_graph(state["project_id"], state["profiles"],
                               state["relationships"], state["kpis"],
                               state["signals"])
        return {}

    @ctx.staged("index", [PipelineStage.EMBEDDINGS])
    def index(state: AnalysisState) -> dict:
        engine.embed(state["project_id"], state["profiles"], state["mappings"],
                     state["kpis"], state["signals"], state["relationships"])
        return {}

    def confidence_gate(state: AnalysisState) -> dict:
        """Score understanding; pause on any genuinely unanswered ambiguity.
        interrupt() re-executes this node on resume — assessment is
        deterministic, answers land in enterprise knowledge, recall clears
        the questions, and the run proceeds from this exact node."""
        pid, rid = state["project_id"], state["run_id"]
        ctx.ledger.record_event(rid, "confidence_gate", "started")
        ctx.mark_stages(pid, [PipelineStage.CONFIDENCE_ASSESSMENT],
                        StageStatus.RUNNING)
        assessment: UnderstandingAssessment = engine.assess(
            state["profiles"], state["kpis"], state["relationships"],
            state["quality"])
        for q in assessment.questions:  # recall org-wide answers — never re-ask
            known = ctx.knowledge.find_clarification(q.question, q.signature)
            if known and known.get("answer"):
                q.answer = known["answer"]
                q.answered = True
        ctx.store.save(pid, "understanding", assessment)

        while [q for q in assessment.questions if not q.answered]:
            unanswered = [q for q in assessment.questions if not q.answered]
            payload = {"kind": "clarification",
                       "confidence": assessment.confidence,
                       "threshold": assessment.threshold,
                       "questions": [q.model_dump() for q in unanswered]}
            ctx.ledger.record_event(rid, "confidence_gate", "interrupt", payload)
            ctx.set_project_status(pid, "awaiting_clarification")
            answers = interrupt(payload)  # ── human input, resumed via API ──
            ctx.set_project_status(pid, "analyzing")
            recorded = record_answers(ctx.knowledge, pid, assessment,
                                      answers if isinstance(answers, dict) else {})
            ctx.ledger.record_event(rid, "confidence_gate", "resumed",
                                    {"answers_recorded": recorded})
            if not recorded:  # nothing usable came back — ask again
                continue
            ctx.store.save(pid, "understanding", assessment)

        ctx.mark_stages(pid, [PipelineStage.CONFIDENCE_ASSESSMENT],
                        StageStatus.COMPLETED)
        ctx.ledger.record_event(rid, "confidence_gate", "completed",
                                {"confidence": assessment.confidence})
        return {"understanding": _native(assessment)}

    @ctx.staged("context", [PipelineStage.BUSINESS_CONTEXT])
    def context(state: AnalysisState) -> dict:
        pid, rid = state["project_id"], state["run_id"]
        assessment = state["understanding"]
        business_context = engine.business_context(
            pid, state.get("project_name") or pid, state["profiles"],
            state["relationships"], state["kpis"], state["signals"],
            state["forecasts"], state["quality"],
            understanding=_understanding_context(ctx, assessment),
            feasibility=state.get("feasibility"))
        ml_results = state.get("ml_results") or []
        if ml_results:
            business_context["ml_predictions"] = ml_results
            ctx.store.save(pid, "business_context", business_context)
        records = extract_evidence(business_context)
        written = ctx.ledger.record_evidence(pid, rid, records)
        ctx.ledger.record_event(rid, "context", "evidence_recorded",
                                {"records": written})
        # Enterprise Context: the unified superset (facts + organizational
        # knowledge/memory/graph) the Prompt Engine consumes. Falls back to
        # the bare business context when the Brain is disabled.
        enterprise_context = business_context
        if ctx.brain is not None:
            try:
                enterprise_context = ctx.brain.build_enterprise_context(
                    pid, business_context)
            except Exception:  # noqa: BLE001 — enrichment must never fail a run
                logger.exception("Enterprise context build failed for %s", pid)
        return {"business_context": business_context,
                "enterprise_context": enterprise_context}

    @ctx.staged("assembler", [PipelineStage.REPORT])
    def assembler(state: AnalysisState) -> dict:
        pid, rid = state["project_id"], state["run_id"]
        business_context = state["business_context"]
        ai_report = state.get("ai_report") or {}
        ai = AIReport(**ai_report) if ai_report else AIReport(
            status="unavailable", error="AI reasoning did not run")
        det_recs = RecommendationEngine().derive(
            state["quality"], state["forecasts"], state["signals"],
            business_context.get("data_limitations", {}))
        confidence = report_confidence(state["understanding"], state["forecasts"])
        previous = ctx.store.load(pid, "report") or {}
        version = int((previous.get("meta") or {}).get("report_version", 0)) + 1
        raw_state = ctx.store.load(pid, "state") or {}
        files = [WorkbookInfo(**f) for f in raw_state.get("files") or []
                 if isinstance(f, dict)]
        report = ReportAssembler().assemble(
            state.get("project_name") or pid, files, state["profiles"],
            state["relationships"], state["kpis"], state["signals"],
            state["forecasts"], state["quality"],
            health_score=business_context["executive_metrics"]["health_score"],
            ai=ai, business_context=business_context,
            deterministic_recommendations=det_recs,
            report_confidence=confidence, report_version=version)
        ctx.store.save(pid, "report", report)
        ctx.store.save(pid, "profiles", state["profiles"])
        ctx.ledger.record_statements(pid, rid, ai_report)
        ctx.ledger.record_deterministic_recommendations(pid, rid, det_recs)
        ctx.ledger.record_report(pid, rid, version, confidence.get("overall"),
                                 {"health_score": business_context[
                                     "executive_metrics"]["health_score"]})
        ctx.set_project_status(pid, "analyzing",
                               report_generated_at=_now().isoformat(),
                               report_version=version,
                               report_confidence=confidence.get("overall"))
        return {"report_version": version}

    def learning(state: AnalysisState) -> dict:
        """Continuous Learning Pipeline (Enterprise Brain): after the report
        is assembled, module outputs become versioned organizational
        knowledge, memory feeds the Knowledge Engine, the project graph
        merges into the enterprise graph, and the Enterprise Context is
        rebuilt. Learning degrades — it never fails the run."""
        pid, rid = state["project_id"], state["run_id"]
        summary = {}
        if ctx.brain is not None:
            ctx.ledger.record_event(rid, "learning", "started")
            try:
                summary = ctx.brain.learn_after_analysis(pid)
                ctx.ledger.record_event(rid, "learning", "completed", summary)
            except Exception as exc:  # noqa: BLE001
                logger.exception("Continuous learning failed for %s", pid)
                ctx.ledger.record_event(rid, "learning", "failed",
                                        {"error": str(exc)[:300]})
        if ctx.manager is not None:
            try:  # executive workspace refresh — best-effort, never fails a run
                refreshed = ctx.manager.refresh_after_analysis(pid)
                ctx.ledger.record_event(rid, "learning",
                                        "workspace_refreshed", refreshed)
            except Exception:  # noqa: BLE001
                logger.exception("Workspace refresh failed for %s", pid)
        return {"learning": _native(summary)} if summary else {}

    return {"ingest": ingest, "understanding": understanding,
            "quality": quality, "quant": quant, "graph_build": graph_build,
            "index": index, "confidence_gate": confidence_gate,
            "context": context, "assembler": assembler, "learning": learning}


def _understanding_context(ctx: NodeContext,
                           understanding: UnderstandingAssessment) -> dict:
    """Compact understanding facts for the business context (same contract as
    the legacy workflow — the model reasons confidence-aware, in the
    organization's own terms)."""
    return {
        "confidence": understanding.confidence,
        "confidence_by_category": understanding.categories,
        "confidence_explanation": understanding.explanation,
        "threshold": understanding.threshold,
        "schema_signature": understanding.schema_signature,
        "inferences": [i.model_dump() for i in understanding.inferences],
        "clarifications": [
            {"question": q.question, "answer": q.answer}
            for q in understanding.questions if q.answered and q.answer
        ],
        "business_rules": [
            r.get("rule") for r in
            ctx.knowledge.context_for_reasoning().get("business_rules", [])
        ],
    }

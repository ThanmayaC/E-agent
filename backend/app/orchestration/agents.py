"""Agent nodes: Supervisor, Planner, ML, Report, Verifier.

Disposition per ADR-002: an agent exists only where judgement lives.
- Supervisor: rules-first run owner (entry validation, pass control, close).
- Planner: emits a typed, stored ExecutionPlan (rules-first; the configured
  LLM may annotate rationale but never changes the plan's structure).
- ML agent: executes the Model Selection Framework — gates → priors →
  champion/challenger — and emits ml_prediction evidence with explanations.
- Report agent: the existing ReportWriterAgent (LLM narration over evidence).
- Verifier: deterministic, never an LLM (ADR-004) — statistics over the
  verification verdicts the reasoning engine stamped on every statement.
"""
from __future__ import annotations

from datetime import UTC

from app.core.logging import get_logger
from app.domain.entities import ProjectState, StageRun
from app.domain.enums import PipelineStage, StageStatus
from app.orchestration.nodes import NodeContext
from app.orchestration.state import AnalysisState

logger = get_logger(__name__)

# sections whose statements the verifier audits
VERIFIED_SECTIONS = ("key_insights", "root_causes", "risks",
                     "opportunities", "recommendations")


def build_agents(ctx: NodeContext) -> dict:
    s = ctx.settings

    def supervisor_entry(state: AnalysisState) -> dict:
        """Owns the run: validates the request, resets the v1 stage stream,
        opens the pass counter."""
        pid, rid = state["project_id"], state["run_id"]
        ctx.ledger.record_event(rid, "supervisor", "run_opened",
                                {"pass": state.get("passes", 0) + 1})
        raw = ctx.store.load(pid, "state") or {}
        name = raw.get("name", pid)
        project = ProjectState(**{**raw, "status": "analyzing",
                                  "stages": []}) if raw else ProjectState(
            project_id=pid, name=name, created_at=_utcnow())
        project.status = "analyzing"
        project.stages = [StageRun(stage=st) for st in PipelineStage]
        ctx.store.save(pid, "state", project)
        if not any(ctx.store.uploads_dir(pid).iterdir()):
            raise ValueError("No uploaded sources to analyze")
        return {"project_name": name, "passes": state.get("passes", 0) + 1,
                "repair_attempts": 0}

    def planner(state: AnalysisState) -> dict:
        """Typed ExecutionPlan: which subgraphs run, ML candidacy, budgets.
        Stored on the project — auditable and diffable across runs."""
        rid = state["run_id"]
        plan = {
            "steps": ["ingest", "understanding", "quality", "quant",
                      "graph_build", "index", "confidence_gate", "ml",
                      "context", "report", "verifier", "assembler"],
            "ml": {"enabled": bool(s.ml_enabled),
                   "mode": "auto",   # candidates decided by meta-feature gates
                   "beat_margin": s.ml_min_beat_margin},
            "budgets": {"max_passes": s.max_passes,
                        "max_repairs": s.max_repair_attempts},
            "pass": state.get("passes", 1),
        }
        ctx.store.save(state["project_id"], "plan", plan)
        ctx.ledger.record_event(rid, "planner", "plan_emitted", plan)
        return {"plan": plan}

    def ml_agent(state: AnalysisState) -> dict:
        """Model Selection Framework over the discovered KPI series. Never
        hardcoded: eligibility gates → priors → rolling-origin
        champion/challenger vs the deterministic baseline. 'No model
        admitted' is a normal, recorded outcome."""
        from app.ml.selection import ModelSelectionFramework  # lazy: sklearn
        pid, rid = state["project_id"], state["run_id"]
        plan_ml = (state.get("plan") or {}).get("ml") or {}
        if not plan_ml.get("enabled", True):
            ctx.ledger.record_event(rid, "ml", "skipped", {"reason": "disabled"})
            return {"ml_results": [], "ml_selection": []}
        ctx.ledger.record_event(rid, "ml", "started")
        framework = ModelSelectionFramework(
            beat_margin=float(plan_ml.get("beat_margin", 0.05)))
        results, traces = [], []
        for kpi in state.get("kpis") or []:
            outcome = framework.run_for_kpi(kpi)
            traces.append(outcome.trace)
            if outcome.model_name:
                version = ctx.ledger.register_model(
                    pid, rid, name=outcome.model_name, family=outcome.family,
                    task="kpi_forecast", metrics=outcome.metrics,
                    selection_trace=outcome.trace)
                for pred in outcome.predictions:
                    pred["model_version"] = f"{outcome.model_name}@{version}"
                results.extend(outcome.predictions)
        # entity-level tasks (churn/growth/segmentation) — discovered by the
        # tabular framework's gates, guarded so a failure degrades to a
        # trace event, never fails the run
        try:
            tab_traces, tab_results = _tabular_tasks(ctx, pid, rid,
                                                     plan_ml)
            traces.extend(tab_traces)
            results.extend(tab_results)
        except Exception as exc:
            ctx.ledger.record_event(rid, "ml", "tabular_failed",
                                    {"error": str(exc)[:300]})
        ctx.store.save(pid, "ml_selection", traces)
        if results:
            ctx.ledger.record_evidence(pid, rid, [
                {"evidence_id": p["id"], "kind": "ml_prediction",
                 "producer": "ml.inference", "payload": p,
                 "content_hash": _hash(p)} for p in results])
        ctx.ledger.record_event(
            rid, "ml", "completed",
            {"kpis_evaluated": len(traces),
             "models_admitted": len({p.get("model_version") for p in results}),
             "predictions": len(results)})
        return {"ml_results": results, "ml_selection": traces}

    def report_agent(state: AnalysisState) -> dict:
        pid, rid = state["project_id"], state["run_id"]
        ctx.ledger.record_event(rid, "report", "started",
                                {"repair_attempt": state.get("repair_attempts", 0)})
        ctx.mark_stages(pid, [PipelineStage.AI_REASONING], StageStatus.RUNNING)
        # The Prompt Engine consumes the unified Enterprise Context (facts +
        # organizational knowledge/memory); bare business context is the
        # fallback when the Brain is disabled.
        ai_report = ctx.report_writer.write(
            pid, state.get("enterprise_context") or state["business_context"])
        ctx.store.save(pid, "ai_report", ai_report)
        ctx.mark_stages(pid, [PipelineStage.AI_REASONING], StageStatus.COMPLETED)
        ctx.ledger.record_event(rid, "report", "completed",
                                {"status": ai_report.status,
                                 "provider": ai_report.provider})
        return {"ai_report": ai_report.model_dump()}

    def verifier(state: AnalysisState) -> dict:
        """Deterministic verification statistics. The reasoning engine already
        stamped every statement (citations resolved against supplied evidence,
        unsupported facts downgraded to hypotheses); this node turns those
        verdicts into the run's quality metric and the repair-loop signal."""
        rid = state["run_id"]
        ai = state.get("ai_report") or {}
        total = verified = 0
        for section in VERIFIED_SECTIONS:
            for item in ai.get(section) or []:
                if not isinstance(item, dict):
                    continue
                total += 1
                if item.get("verification") == "evidence_verified":
                    verified += 1
        fail_rate = 0.0 if total == 0 else round(1 - verified / total, 3)
        verdict = {"statements": total, "verified": verified,
                   "fail_rate": fail_rate,
                   "ai_status": ai.get("status", "unavailable"),
                   "repair_attempts": state.get("repair_attempts", 0)}
        ctx.ledger.record_event(rid, "verifier", "completed", verdict)
        return {"verification": verdict}

    def supervisor_exit(state: AnalysisState) -> dict:
        pid, rid = state["project_id"], state["run_id"]
        verdict = state.get("verification") or {}
        ctx.ledger.record_event(rid, "supervisor", "run_accepted", {
            "pass": state.get("passes", 1),
            "verification_fail_rate": verdict.get("fail_rate"),
            "report_version": state.get("report_version")})
        ctx.set_project_status(pid, "ready")
        return {}

    return {"supervisor_entry": supervisor_entry, "planner": planner,
            "ml": ml_agent, "report": report_agent, "verifier": verifier,
            "supervisor_exit": supervisor_exit}


MAX_TABULAR_TABLES = 5
MAX_TABULAR_ROWS = 50_000


def _tabular_tasks(ctx: NodeContext, pid: str, rid: str,
                   plan_ml: dict) -> tuple[list, list]:
    """Run the tabular Training Pipeline over the project's warehouse tables.
    Tasks are discovered (never assumed); the pipeline registers admitted
    models (registry + ledger) and inference produces ml_prediction evidence
    with model_version + explanation attached."""
    import duckdb  # lazy, like the selection framework

    from app.ml.pipelines import InferencePipeline, TrainingPipeline
    db = ctx.store.duckdb_path(pid)
    if not db.exists():
        return [], []
    training = TrainingPipeline(
        ctx.store.project_dir(pid), ledger=ctx.ledger, project_id=pid,
        run_id=rid, beat_margin=float(plan_ml.get("beat_margin", 0.05)),
        mlflow_uri=getattr(ctx.settings, "mlflow_uri", ""))
    inference = InferencePipeline(ctx.store.project_dir(pid))
    traces, results = [], []
    con = duckdb.connect(str(db), read_only=True)
    try:
        tables = [r[0] for r in con.execute("SHOW TABLES").fetchall()]
        for table in tables[:MAX_TABULAR_TABLES]:
            df = con.execute(
                f'SELECT * FROM "{table}" LIMIT {MAX_TABULAR_ROWS}').fetchdf()
            for tr in training.run_discovered(df):
                tr.trace["dataset_id"] = table
                traces.append(tr.trace)
                if tr.registered is not None:
                    results.append(
                        inference.run(tr.registered.name, df)["evidence"])
    finally:
        con.close()
    return traces, results


def route_after_verifier(settings):
    """Repair loop: an LLM report with a high unverified-statement rate is
    regenerated (bounded). Deterministic failures (no provider) never loop —
    there is nothing a retry would change."""
    def route(state: AnalysisState) -> str:
        v = state.get("verification") or {}
        if (v.get("ai_status") == "ok"
                and v.get("fail_rate", 0.0) > settings.verification_repair_threshold
                and state.get("repair_attempts", 0) < settings.max_repair_attempts):
            return "repair"
        return "assemble"
    return route


def _utcnow():
    from datetime import datetime
    return datetime.now(UTC)


def _hash(payload: dict) -> str:
    from app.evidence.extract import content_hash
    return content_hash(payload)

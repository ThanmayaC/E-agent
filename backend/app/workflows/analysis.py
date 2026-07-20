"""Full-analysis workflow.

Orchestrates the platform's core loop for one project:

    connectors → facts (Intelligence Engine) → executive narrative
    (Report Writer Agent) → assembled report.

The workflow owns sequencing, stage-status streaming, and persistence of the
run state. It contains NO analytics (Intelligence Engine) and NO narrative
generation (Report Writer Agent) of its own.
"""
from __future__ import annotations

from datetime import datetime, timezone

from app.agents.report_writer import ReportWriterAgent
from app.core.logging import get_logger
from app.domain.entities import ProjectState, StageRun, UnderstandingAssessment
from app.domain.enums import PipelineStage, StageStatus
from app.intelligence.confidence.assessor import report_confidence
from app.intelligence.engine import IntelligenceEngine
from app.intelligence.recommendations import RecommendationEngine
from app.knowledge.store import KnowledgeStore
from app.repositories.artifact_store import ArtifactStore
from app.reports.generator import ReportAssembler

logger = get_logger(__name__)


class AnalysisWorkflow:
    def __init__(self, store: ArtifactStore, intelligence: IntelligenceEngine,
                 report_writer: ReportWriterAgent, knowledge: KnowledgeStore,
                 brain=None, manager=None):
        self.store = store
        self.intelligence = intelligence
        self.report_writer = report_writer
        self.knowledge = knowledge
        self.brain = brain      # EnterpriseBrain (None => learning disabled)
        self.manager = manager  # ManagerWorkspace (None => no exec refresh)

    # -------------------------------------------------------------- entry
    def run(self, project_id: str) -> None:
        state_raw = self.store.load(project_id, "state")
        state = None
        if state_raw:
            try:
                state = ProjectState(**state_raw)
            except Exception:  # stale state from an older pipeline version
                state = ProjectState(
                    project_id=project_id,
                    name=state_raw.get("name", project_id),
                    created_at=state_raw.get("created_at") or datetime.now(timezone.utc),
                )
        if state is None:
            state = ProjectState(project_id=project_id, name=project_id,
                                 created_at=datetime.now(timezone.utc))
        state.status = "analyzing"
        state.stages = [StageRun(stage=s) for s in PipelineStage]
        self._save_state(state)

        try:
            self._execute(project_id, state)
            # _execute pauses (awaiting_clarification) when understanding
            # confidence is below threshold; never override that into "ready".
            if state.status != "awaiting_clarification":
                state.status = "ready"
        except Exception:
            logger.exception("Analysis workflow failed for %s", project_id)
            state.status = "failed"
        self._save_state(state)

    # ----------------------------------------------------------- workflow
    def _execute(self, project_id: str, state: ProjectState) -> None:
        mark = self._marker(state)
        engine = self.intelligence

        # 1-2. source + table discovery (any connector: Excel, CSV, PDF, ...)
        with mark(PipelineStage.FILE_DISCOVERY), mark(PipelineStage.WORKSHEET_DISCOVERY):
            extracts = engine.ingest(project_id)
            state.files = [e.info for e in extracts]
            tables = [t for e in extracts for t in e.tables]
            if not tables:
                raise ValueError("No readable tables found in uploaded sources")

        # dedup / partition merge
        with mark(PipelineStage.DEDUPLICATION):
            merged, lineage = engine.deduplicate(project_id, tables)

        # 3-4. schema discovery + profiling
        with mark(PipelineStage.SCHEMA_DISCOVERY), mark(PipelineStage.COLUMN_PROFILING):
            profiles, frames = engine.profile(merged, lineage)

        # 5. business meaning + semantic layer
        with mark(PipelineStage.BUSINESS_MEANING), mark(PipelineStage.SEMANTIC_LAYER):
            mappings = engine.semantics(project_id, profiles)

        # 6. relationships
        with mark(PipelineStage.RELATIONSHIP_DETECTION):
            relationships = engine.relationships(project_id, profiles, frames)

        # 7. time series
        with mark(PipelineStage.TIME_SERIES_DETECTION):
            engine.timeseries(profiles, frames)

        # 8. KPIs
        with mark(PipelineStage.KPI_DISCOVERY):
            kpis = engine.kpis(profiles, frames)

        # 9. quality
        with mark(PipelineStage.DATA_QUALITY):
            quality = engine.quality(project_id, profiles, frames)

        # 10. analytics warehouse
        with mark(PipelineStage.ANALYTICS):
            breakdowns = engine.warehouse(project_id, profiles, frames)

        # 11. deterministic statistical signals (facts only — no narrative)
        with mark(PipelineStage.SIGNALS):
            signals = engine.signals(project_id, kpis, breakdowns)

        # 12. forecasts
        with mark(PipelineStage.PREDICTIONS):
            forecasts = engine.forecasts(project_id, kpis)

        # 13. knowledge graph
        with mark(PipelineStage.KNOWLEDGE_GRAPH):
            engine.knowledge_graph(project_id, profiles, relationships, kpis, signals)

        # 14. embeddings + vector store
        with mark(PipelineStage.EMBEDDINGS):
            engine.embed(project_id, profiles, mappings, kpis, signals, relationships)

        # 15. confidence gate — understand the data before reasoning over it.
        # Below-threshold understanding pauses the pipeline with clarification
        # questions instead of letting the model guess. All deterministic
        # artifacts above remain available to the UI while paused.
        with mark(PipelineStage.CONFIDENCE_ASSESSMENT):
            understanding = self._recall_answers(
                engine.assess(profiles, kpis, relationships, quality))
            self.store.save(project_id, "understanding", understanding)
            # Questions are only generated for REAL ambiguities (two revenue
            # candidates, competing identifiers, multiple reporting dates, an
            # unidentifiable dataset). Reasoning past any of them is guessing,
            # whatever the overall score says — so any unanswered question
            # pauses. Answered ones (user or recalled knowledge) never do.
            unanswered = [q for q in understanding.questions if not q.answered]
            if unanswered:
                state.status = "awaiting_clarification"
                logger.info(
                    "Pausing %s for clarification: confidence %.2f, "
                    "%d question(s) unanswered",
                    project_id, understanding.confidence, len(unanswered))
                return  # DO NOT GUESS — wait for the user's answers

        # 16. business context (compact facts JSON — the only thing agents see)
        with mark(PipelineStage.BUSINESS_CONTEXT):
            business_context = engine.business_context(
                project_id, state.name, profiles, relationships, kpis, signals,
                forecasts, quality,
                understanding=self._understanding_context(understanding))

        # 16.5. Enterprise Context — the unified superset (facts + org
        # knowledge/memory/graph) the Prompt Engine consumes. Enrichment
        # never fails the run; the bare business context is the fallback.
        reasoning_context = business_context
        if self.brain is not None:
            try:
                reasoning_context = self.brain.build_enterprise_context(
                    project_id, business_context)
            except Exception:
                logger.exception("Enterprise context build failed for %s",
                                 project_id)

        # 17. executive narrative: Report Writer Agent → reasoning model
        with mark(PipelineStage.AI_REASONING):
            ai_report = self.report_writer.write(project_id, reasoning_context)
            self.store.save(project_id, "ai_report", ai_report)

        # 18. fixed-structure executive report (facts + AI narrative), plus
        # rule-derived recommendations and the deterministic confidence model
        with mark(PipelineStage.REPORT):
            det_recs = RecommendationEngine().derive(
                quality, forecasts, signals,
                business_context.get("data_limitations", {}))
            confidence = report_confidence(understanding, forecasts)
            previous = self.store.load(project_id, "report") or {}
            version = int((previous.get("meta") or {}).get("report_version", 0)) + 1
            report = ReportAssembler().assemble(
                state.name, state.files, profiles, relationships, kpis, signals,
                forecasts, quality,
                health_score=business_context["executive_metrics"]["health_score"],
                ai=ai_report, business_context=business_context,
                deterministic_recommendations=det_recs,
                report_confidence=confidence, report_version=version)
            self.store.save(project_id, "report", report)
            state.report_generated_at = datetime.now(timezone.utc)
            state.report_version = version
            state.report_confidence = confidence["overall"]

        self.store.save(project_id, "profiles", profiles)

        # 19. Continuous Learning Pipeline (Enterprise Brain) — module
        # outputs become versioned organizational knowledge, memory syncs,
        # the enterprise graph grows, the Enterprise Context is refreshed.
        # Learning degrades — it never fails a successful analysis.
        if self.brain is not None:
            try:
                self.brain.learn_after_analysis(project_id)
            except Exception:
                logger.exception("Continuous learning failed for %s",
                                 project_id)

        # 20. Executive workspace refresh (Manager Module) — reviews, tasks,
        # notifications, daily brief. Best-effort, never fails the run.
        if self.manager is not None:
            try:
                self.manager.refresh_after_analysis(project_id)
            except Exception:
                logger.exception("Workspace refresh failed for %s",
                                 project_id)

    # -------------------------------------------------------- clarification
    def _recall_answers(self, understanding: UnderstandingAssessment
                        ) -> UnderstandingAssessment:
        """Fill in any clarification the organization already answered for an
        equivalent schema, so it is never asked twice."""
        for q in understanding.questions:
            known = self.knowledge.find_clarification(q.question, q.signature)
            if known and known.get("answer"):
                q.answer = known["answer"]
                q.answered = True
        return understanding

    def _understanding_context(self, understanding: UnderstandingAssessment) -> dict:
        """Compact understanding facts for the business context: overall and
        per-category confidence, per-inference scores, answered clarifications,
        and the organization's business rules — so the model reasons
        confidence-aware and in the organization's own terms."""
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
                self.knowledge.context_for_reasoning().get("business_rules", [])
            ],
        }

    # ------------------------------------------------------------ helpers
    def _marker(self, state: ProjectState):
        workflow = self

        class _Mark:
            def __init__(self, stage: PipelineStage):
                self.stage = stage

            def __enter__(self):
                run = next(r for r in state.stages if r.stage == self.stage)
                run.status = StageStatus.RUNNING
                run.started_at = datetime.now(timezone.utc)
                workflow._save_state(state)
                return self

            def __exit__(self, exc_type, exc, tb):
                run = next(r for r in state.stages if r.stage == self.stage)
                run.finished_at = datetime.now(timezone.utc)
                run.status = StageStatus.FAILED if exc_type else StageStatus.COMPLETED
                if exc:
                    run.detail = str(exc)[:300]
                workflow._save_state(state)
                return False

        return _Mark

    def _save_state(self, state: ProjectState) -> None:
        self.store.save(state.project_id, "state", state)

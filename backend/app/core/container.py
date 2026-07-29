"""Dependency-injection container: builds and caches singletons from Settings.

The application depends only on abstractions (BaseLLMProvider, Embedder,
VectorStore, DataConnector, Tool, BaseAgent); which concrete implementation
runs is decided here, from configuration alone.

Layering (top depends on bottom, never the reverse):

    API / Workers
    Autonomy Runtime (scheduler, event bus, queue, goals, planning)
    Workflow Engine  →  Agents  →  Tools
    Memory  →  Knowledge
    Intelligence Engine (connectors + analytics: facts only)
    LLM provider abstraction
"""
from __future__ import annotations

from functools import lru_cache

from app.agents.catalogue import register_catalogue
from app.agents.registry import AgentRegistry
from app.agents.copilot import CopilotAgent
from app.agents.prompt_generator import PromptGenerationAgent
from app.agents.reasoning import AIReasoningEngine
from app.agents.report_writer import ReportWriterAgent
from app.agents.specialists import (
    BusinessAnalystAgent, ManagerAgent, PlannerAgent, PortfolioAgent, SchemaAnalystAgent,
)
from app.brain import EnterpriseBrain, EnterpriseContextBuilder
from app.communication import NotificationCenter, ProviderRegistry
from app.connectors import EnterpriseConnectorFramework
from app.copilot.copilot_runtime import CopilotLayer
from app.core.config import Settings, get_settings
from app.core.logging import get_logger
from app.evaluation import EvaluationPipeline
from app.evidence.ledger import EvidenceLedger
from app.governance import GovernanceLayer
from app.intelligence.connectors import build_registry as build_connectors
from app.intelligence.embeddings.embedder import Embedder, create_embedder
from app.intelligence.embeddings.vector_store import VectorStore, create_vector_store
from app.intelligence.engine import IntelligenceEngine
from app.knowledge.engine import KnowledgeEngine
from app.knowledge.graph import EnterpriseKnowledgeGraph
from app.knowledge.store import KnowledgeStore
from app.llm.provider_factory import create_fallback_provider, create_provider
from app.manager import (
    DailyBriefGenerator, DecisionCenter, ExecutiveTaskManager, ManagerStore,
    ManagerWorkspace, PortfolioWorkspace, ReportReviewCenter,
)
from app.memory.lifecycle import MemoryLifecycle
from app.memory.manager import MemoryManager
from app.memory.sync import MemorySynchronizer
from app.observability import LatencyTracker, ObservabilityDashboard
from app.product.product_runtime import ProductIntelligenceLayer
from app.prompts.registry import PromptRegistry
from app.repositories.artifact_store import ArtifactStore
from app.runtime.runtime import AutonomyRuntime
from app.sync.sync_runtime import SynchronizationLayer
from app.tools.registry import ToolRegistry
from app.tools.builtin import (
    AnalyticsSQLTool, ArtifactLookupTool, KnowledgeSearchTool, ReportMarkdownTool,
    VectorSearchTool,
)
from app.tools.planned import CalendarTool, EmailTool, PDFExportTool, PowerPointTool
from app.tools.specs import spec_for
from app.workflows.analysis import AnalysisWorkflow
from app.workflows.engine import PLANNED_WORKFLOWS, WorkflowDefinition, WorkflowEngine
from app.workflows.registry import WorkflowRegistry, build_default_specs

logger = get_logger(__name__)


class Container:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.store = ArtifactStore(settings.projects_dir)

        # ------------------------------------------- control plane (ledger)
        # Always on: runs, evidence, statements, citations, models, audit.
        # SQLite in the lite profile, PostgreSQL via EDIP_DATABASE_URL.
        self.ledger = EvidenceLedger(settings.control_db_url)

        # ------------------------------------------------ knowledge/memory
        self.knowledge = KnowledgeStore(settings.knowledge_dir)
        self.enterprise_graph = EnterpriseKnowledgeGraph(
            settings.knowledge_dir, neo4j_uri=settings.neo4j_uri,
            neo4j_user=settings.neo4j_user,
            neo4j_password=settings.neo4j_password)
        self.knowledge_engine = KnowledgeEngine(self.knowledge,
                                                self.enterprise_graph)
        self.memory = MemoryManager(self.store, self.knowledge)

        # -------------------------------------------- intelligence (facts)
        self.embedder: Embedder = create_embedder(settings.embedding_model, settings.embedding_dim)
        self.connectors = build_connectors(header_scan_rows=settings.header_scan_rows)
        self.intelligence = IntelligenceEngine(settings, self.store, self.embedder,
                                               self.connectors)

        # ------------------- V2.2: Enterprise AI Operating Layer (policy)
        # Governance and the Prompt Registry are built FIRST: the tool
        # registry asks governance before every call, and the prompt agent
        # renders from the registry rather than embedding prompts.
        self.governance = GovernanceLayer(
            ledger=self.ledger, enabled=settings.governance_enabled,
            default_role=settings.governance_default_role)
        self.prompts = PromptRegistry(settings.prompts_dir)

        # ------------------------------------------------------ LLM layer
        # Built here (before reasoning) so every LLM call can be recorded —
        # governance.record_model_usage() for the Admin console's usage
        # metrics, latency for the processing-latency dashboard.
        self.latency = LatencyTracker()
        self.llm_provider = create_provider(settings)  # None => AI unavailable
        self.prompt_agent = PromptGenerationAgent(knowledge=self.knowledge,
                                                  prompts=self.prompts)
        self.reasoning = AIReasoningEngine(self.llm_provider, self.prompt_agent,
                                           fallback=create_fallback_provider(settings),
                                           governance=self.governance,
                                           latency=self.latency)

        # ----------------------------------------------------------- tools
        # V2.2: each tool registers with its declared spec — capability,
        # permissions, and input/output schema — so agents request
        # capabilities and Governance can reason about them.
        self.tools = ToolRegistry(governance=self.governance)
        for tool in (VectorSearchTool(self.embedder, self.vector_store_for),
                     ArtifactLookupTool(self.store),
                     AnalyticsSQLTool(self.store),
                     KnowledgeSearchTool(self.knowledge),
                     ReportMarkdownTool(self.store),
                     PowerPointTool(), PDFExportTool(), EmailTool(),
                     CalendarTool()):
            self.tools.register(tool, spec_for(tool.name))

        # ---------------------------------------------------------- agents
        self.report_writer = ReportWriterAgent(self.tools, self.memory, self.reasoning)
        self.copilot = CopilotAgent(self.tools, self.memory, self.reasoning)
        self.agents = AgentRegistry(tools=self.tools)
        self.agents.register(self.prompt_agent)
        self.agents.register(self.report_writer)
        self.agents.register(self.copilot)
        self.agents.register(SchemaAnalystAgent(self.tools, self.memory))
        self.agents.register(BusinessAnalystAgent(self.tools, self.memory))
        self.agents.register(PortfolioAgent(self.tools, self.memory))
        self.agents.register(ManagerAgent(self.tools, self.memory))
        self.agents.register(PlannerAgent(self.tools, self.memory))

        # ------------------------------------------------ Enterprise Brain
        # The continuously learning organizational intelligence layer: the
        # Knowledge Engine, memory synchronization, the enterprise knowledge
        # graph, and the Enterprise Context Builder — loaded and verified at
        # startup, fed automatically after every successful analysis.
        self.brain = None
        if settings.brain_enabled:
            self.brain = EnterpriseBrain(
                store=self.store, memory=self.memory,
                knowledge=self.knowledge, graph=self.enterprise_graph,
                engine=self.knowledge_engine,
                synchronizer=MemorySynchronizer(self.memory),
                context_builder=EnterpriseContextBuilder(
                    self.store, self.knowledge, self.enterprise_graph))
            self.brain.startup()

        # -------------------------------------- Executive Workspace (Manager)
        # The primary interface between the Enterprise Brain and enterprise
        # users: tasks, decisions, report reviews, portfolio, daily brief,
        # internal notifications, and the V2 provider interfaces.
        self.manager_store = ManagerStore(settings.data_dir / "manager")
        self.notifications = NotificationCenter(settings.data_dir / "manager")
        # V2 Communication Layer: Outlook, Teams, and SharePoint adapters
        # register unconditionally and report their own availability —
        # unconfigured channels leave approved communications waiting in the
        # queue, exactly as V1 behaved.
        self.providers = ProviderRegistry()
        from app.communication.adapters import build_default_adapters
        for adapter in build_default_adapters():
            self.providers.register(adapter)
        self.exec_tasks = ExecutiveTaskManager(self.manager_store)
        self.decisions = DecisionCenter(self.manager_store, self.knowledge)
        self.reviews = ReportReviewCenter(self.manager_store,
                                          self.notifications)
        self.portfolio = PortfolioWorkspace(self.store, self.knowledge)
        self.daily_brief = DailyBriefGenerator(
            self.manager_store, self.knowledge, self.notifications,
            self.exec_tasks, self.portfolio)
        self.manager = ManagerWorkspace(
            self.store, self.knowledge, self.exec_tasks, self.decisions,
            self.reviews, self.notifications, self.portfolio,
            self.daily_brief, brain=self.brain)
        self.manager.startup_refresh()

        # ------------------------------------------------------- workflows
        # Strangler flag (v3 Phase C): the LangGraph analysis graph is the
        # default orchestrator; the v2 imperative workflow remains selectable
        # (EDIP_ORCHESTRATOR=legacy) and is the automatic fallback when the
        # langgraph library is not installed (lite profile unchanged).
        self.legacy_workflow = AnalysisWorkflow(self.store, self.intelligence,
                                                self.report_writer, self.knowledge,
                                                brain=self.brain,
                                                manager=self.manager)
        self.langgraph = None
        if settings.orchestrator == "langgraph":
            try:
                from app.orchestration.graph import LangGraphOrchestrator
                from app.orchestration.nodes import NodeContext
                self.langgraph = LangGraphOrchestrator(NodeContext(
                    settings, self.store, self.intelligence,
                    self.report_writer, self.knowledge, self.ledger,
                    brain=self.brain, manager=self.manager))
            except ImportError as exc:
                logger.warning("langgraph unavailable (%s) — using the legacy "
                               "imperative workflow", exc)
        self.orchestrator = self.langgraph or self.legacy_workflow
        self.workflows = WorkflowEngine(
            self.store, on_failure=self.manager.notify_workflow_failure)
        self.manager.workflow_engine = self.workflows  # automation status view
        self.workflows.register(WorkflowDefinition(
            "full_analysis",
            "Ingest every uploaded source, build facts, and write the executive report",
            runner=self.orchestrator.run, tags=["analysis"]))
        for planned_wf in PLANNED_WORKFLOWS:
            self.workflows.register(planned_wf)

        # ------------------- Enterprise Knowledge Synchronization Layer
        # Keeps the Enterprise Brain learning from the enterprise itself:
        # the data-source registry, incremental synchronization, the
        # organizational model, the relationship engine, the knowledge
        # refresh pipeline, and unified enterprise search. Built here;
        # its jobs are registered on the scheduler by the runtime below.
        self.sync = SynchronizationLayer(
            settings=settings, store=self.store, knowledge=self.knowledge,
            connectors=self.connectors, embedder=self.embedder,
            vector_store_for=self.vector_store_for, brain=self.brain,
            tasks=self.exec_tasks, portfolio=self.portfolio,
            graph=self.enterprise_graph, latency=self.latency)
        self.manager.sync = self.sync  # organization panels in the workspace

        # ------------------ Enterprise Connector Framework (V2.1)
        # The uniform way enterprise knowledge gets IN: an administrator
        # configures a data source once, the Runtime keeps it synchronized,
        # and every change becomes a Knowledge Package that flows through
        # Document Intelligence into the Brain. It owns no clock and no
        # pipeline — it registers on the scheduler built below and hands
        # packages to the document pipeline built above.
        self.connector_framework = EnterpriseConnectorFramework(
            settings=settings, documents=self.sync.documents,
            knowledge=self.knowledge)

        # ------------- Product Intelligence & Strategic Decision Layer
        # The Enterprise Product Manager, sitting ABOVE the Brain: the
        # product catalogue, health, growth intelligence, strategy, KPI
        # monitoring, scenarios, portfolio intelligence, and executive
        # briefs. It computes no analytics of its own — every judgement is
        # derived from evidence the Brain and the intelligence engines
        # already produced. Its jobs are registered by the runtime below.
        self.product = ProductIntelligenceLayer(
            settings=settings, store=self.store, knowledge=self.knowledge,
            sync=self.sync, tasks=self.exec_tasks,
            notifications=self.notifications, reviews_center=self.reviews)
        self.manager.product = self.product  # product panels in the workspace

        # ------------------------------- Enterprise Copilot Layer
        # The executive's primary interaction point: understands intent,
        # orchestrates the modules that already hold the answer, and has the
        # reasoning model narrate their evidence. It calculates nothing —
        # the LLM router reuses the providers built above, and every fact
        # comes from a module through its public interface.
        self.copilot_layer = CopilotLayer(
            settings=settings, store=self.store, knowledge=self.knowledge,
            prompt_agent=self.prompt_agent, provider=self.llm_provider,
            fallback=create_fallback_provider(settings), manager=self.manager,
            portfolio=self.portfolio, brain=self.brain, sync=self.sync,
            product=self.product, governance=self.governance,
            latency=self.latency)
        self.manager.copilot_layer = self.copilot_layer

        # ------------------------------------------- autonomous execution
        # The heartbeat: scheduler, event bus, triggers, goals, planning,
        # decisions, and the action queue. Built here (its state and APIs
        # are always readable) but never started here — `start()` is the
        # application's call, so importing the app or building the
        # container never spawns a thread or executes autonomous work.
        self.runtime = AutonomyRuntime(
            settings=settings, store=self.store, knowledge=self.knowledge,
            memory=self.memory, manager=self.manager,
            portfolio=self.portfolio, tasks=self.exec_tasks,
            notifications=self.notifications, brief=self.daily_brief,
            workflows=self.workflows, orchestrator=self.orchestrator,
            brain=self.brain, sync=self.sync if settings.sync_enabled else None,
            product=self.product if settings.product_enabled else None,
            copilot=self.copilot_layer if settings.copilot_enabled else None,
            connectors=(self.connector_framework
                        if settings.connectors_enabled else None),
            providers=self.providers, reasoning=self.reasoning)
        self.manager.runtime = self.runtime  # autonomy panels in the workspace

        # ------------------ V2.2: Enterprise AI Operating Layer (assembly)
        # Everything below composes layers that already exist. Built last
        # because each one catalogues or observes the components above it —
        # and built here rather than inside those components so no module
        # gains a dependency on the operating layer to function.

        # The agent catalogue: the SDS's named capabilities, mapped onto the
        # workflows, layers, and pipelines that already implement them.
        # Nothing is reimplemented; a capability whose implementation is
        # disabled here registers without a runner and reports itself so.
        register_catalogue(
            self.agents, workflows=self.workflows, brief=self.daily_brief,
            product=self.product, documents=self.sync.documents,
            decisions=self.runtime.decisions, orchestrator=self.orchestrator)

        # Declared autonomous workflows, executed through the existing
        # Workflow Engine — a registry, never a second orchestrator.
        self.workflow_registry = WorkflowRegistry(engine=self.workflows,
                                                  agents=self.agents)
        self.workflow_registry.register_all(build_default_specs(settings))

        # The evaluation panel. Optional: disabling it returns the platform
        # to V2.1 behaviour, since the V1 guards remain underneath.
        self.evaluation = EvaluationPipeline(
            enabled=settings.evaluation_enabled)
        self.evaluation.attach_bus(self.runtime.bus)

        # The Brain's lifecycle view: freshness, versions, history, expiry.
        self.memory_lifecycle = MemoryLifecycle(
            knowledge=self.knowledge, documents=self.sync.documents,
            organization=self.sync.organization,
            relationships=self.sync.relationships, governance=self.governance)

        # ------------------ V3.1: Executive Intelligence layer
        # Reads the ingested synthetic enterprise (KPI workbook, decisions,
        # incidents, RCAs, SOPs, reports, master data) and reasons over it to
        # produce the executive brief, priorities, recommendations, KPI
        # intelligence, and ranked decisions. Adds no data and changes no Brain
        # architecture; if the enterprise has not been generated it runs empty
        # and every existing surface behaves exactly as before.
        from app.executive import (
            EcosystemIntelligence, EcosystemReader, EnterpriseReader,
            EvolutionIntelligence, ExecutiveIntelligence)
        self.executive = ExecutiveIntelligence(
            EnterpriseReader(settings.enterprise_data_dir))
        # V7.0: ecosystem analytics over the sampled ledger + aggregate cubes.
        _eco_reader = EcosystemReader(settings.enterprise_data_dir)
        self.ecosystem = EcosystemIntelligence(_eco_reader)
        # V8.0: six-month evolution — entity lifecycle, multi-granularity trends,
        # forecast validation, decision tracking, storylines + executive Q&A.
        # Shares the ecosystem reader (one cache over the same cube directory).
        self.evolution = EvolutionIntelligence(_eco_reader)

        # Phase 2 #12: email intelligence. Emails from any configured provider
        # (Gmail/Outlook) become searchable enterprise knowledge — categorised
        # and linked to the same business entities the rest of the Brain uses.
        # The vocabulary is best-effort (the analyzer still extracts ids and
        # actions without it), so a missing/unbuilt ecosystem never blocks it.
        from app.communication.email_intelligence import EmailIntelligence

        def _entity_vocab() -> list[str]:
            names: list[str] = []
            for accessor in (self.ecosystem.compare_banks,
                             self.ecosystem.compare_psps):
                try:
                    for row in accessor():
                        name = row.get("name") or row.get("bank") or \
                            row.get("psp") or ""
                        if name:
                            names.append(name)
                except Exception:  # noqa: BLE001 — vocab is optional
                    pass
            return names

        self.email_intelligence = EmailIntelligence(vocabulary=_entity_vocab())

        # V9.0: the AI-first Enterprise Workspace — universal file understanding,
        # unified search, artifact generation, home feed and pins. Orchestrates
        # the layers above; adds no new intelligence. Built last so every layer
        # it federates (copilot/executive/ecosystem/evolution/graph) exists.
        from app.workspace import Workspace
        self.workspace = Workspace(self, settings.data_dir / "workspace")

        # V10.0: Layer-2 machine learning (scikit-learn) — forecasting, anomaly
        # detection, segmentation, churn & failure prediction, each prediction
        # tagged model+version+confidence+features. Trained on the cubes.
        from app.ml_models import MLService
        self.ml = MLService(self)
        # V10.0: the multi-layer analyst — insight engine (deterministic + ML +
        # graph + evidence), continuous-learning feedback store, and the
        # retrieval/semantic cache. Kept in its own app/analyst package.
        from app.analyst import InsightEngine, LearningStore
        self.learning_store = LearningStore(settings.data_dir / "learning")
        self.insight_engine = InsightEngine(self)
        # The manager workspace and daily brief draw on it so the existing
        # Executive Dashboard lights up with real enterprise intelligence.
        self.manager.executive = self.executive
        self.daily_brief.executive = self.executive
        # The Copilot reasons over it: the executive summary is always in the
        # business context, and the executive facts are admissible evidence so
        # the validator grounds the figures the model quotes — success-criteria
        # questions are answered by reasoning, not document retrieval alone.
        self.copilot_layer.context._executive = self.executive
        self.copilot_layer.evidence._executive = self.executive

        # Admin-only observability, composed from every layer's own status.
        # self.latency was built earlier, alongside the LLM layer, so every
        # reasoning/copilot call could be timed from the start.
        self.observability = ObservabilityDashboard(
            agents=self.agents, tools=self.tools, prompts=self.prompts,
            evaluation=self.evaluation, governance=self.governance,
            connectors=self.connector_framework, runtime=self.runtime,
            lifecycle=self.memory_lifecycle,
            workflows=self.workflow_registry, brain=self.brain,
            latency=self.latency)

    def awaiting_run(self, project_id: str) -> str | None:
        """run_id of the project's interrupted LangGraph run (paused at the
        confidence gate), if any — the clarification API resumes it in place
        instead of re-running the pipeline."""
        if self.langgraph is None:
            return None
        runs = self.ledger.runs(project_id)
        if runs and runs[0]["status"] == "awaiting_clarification":
            return runs[0]["run_id"]
        return None

    def vector_store_for(self, project_id: str) -> VectorStore:
        return create_vector_store(
            self.settings.vector_backend,
            path=self.store.vectors_path(project_id),
            pg_url=self.settings.pgvector_url,
            dim=self.embedder.dim,
            collection=project_id,
        )


@lru_cache
def get_container() -> Container:
    return Container(get_settings())

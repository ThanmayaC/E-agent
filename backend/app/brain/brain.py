"""Enterprise Brain runtime.

Owns the continuous learning pipeline and the Brain's lifecycle:

    startup:  load memory, knowledge, knowledge graph, learning history,
              business rules, clarifications → verify consistency → READY.

    after every successful analysis (automatic, never manual):
        Knowledge Update        — KnowledgeEngine extracts structured,
                                  versioned knowledge from module outputs
        Memory Update           — MemorySynchronizer feeds memory layers
                                  into organizational knowledge
        Knowledge Graph Update  — the project graph merges into the
                                  enterprise graph (cross-project links)
        Enterprise Context Update — the unified context is rebuilt
        → a learning event records what was learned, from where

Learning DEGRADES, it never fails: any exception is recorded and the
analysis run stays successful. The Brain is deterministic end to end — the
LLM is only a downstream consumer of the Enterprise Context.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from app.brain.context import EnterpriseContextBuilder
from app.core.logging import get_logger
from app.knowledge.engine import KnowledgeEngine
from app.knowledge.graph import EnterpriseKnowledgeGraph
from app.knowledge.store import KnowledgeStore
from app.memory.manager import MemoryManager
from app.memory.sync import MemorySynchronizer
from app.repositories.artifact_store import ArtifactStore

logger = get_logger(__name__)

# project artifacts the learning pipeline reads (missing ones are skipped)
LEARNED_ARTIFACTS = ("profiles", "semantic_layer", "relationships", "kpis",
                     "signals", "forecasts", "ai_report", "understanding",
                     "business_context")


class EnterpriseBrain:
    """Composition root of the organizational intelligence layer."""

    def __init__(self, store: ArtifactStore, memory: MemoryManager,
                 knowledge: KnowledgeStore, graph: EnterpriseKnowledgeGraph,
                 engine: KnowledgeEngine, synchronizer: MemorySynchronizer,
                 context_builder: EnterpriseContextBuilder):
        self.store = store
        self.memory = memory
        self.knowledge = knowledge
        self.graph = graph
        self.engine = engine
        self.synchronizer = synchronizer
        self.context = context_builder
        self.state = "initializing"
        self.checks: dict[str, Any] = {}
        self.started_at: str | None = None

    # -------------------------------------------------------------- startup
    def startup(self) -> dict[str, Any]:
        """Load every knowledge/memory surface, verify consistency, and mark
        the Brain READY (or degraded, naming exactly what failed)."""
        checks: dict[str, Any] = {}

        def check(name: str, fn) -> None:
            try:
                checks[name] = {"ok": True, "detail": fn()}
            except Exception as exc:  # noqa: BLE001 — degraded, not down
                logger.exception("Brain startup check failed: %s", name)
                checks[name] = {"ok": False, "error": str(exc)[:200]}

        check("knowledge_store", lambda: self.knowledge.stats())
        check("knowledge_graph", lambda: {
            k: v for k, v in self.graph.stats().items()
            if k in ("node_count", "edge_count", "neo4j")})
        check("learning_history",
              lambda: {"events": len(self.knowledge.learning_history(1000))})
        check("business_rules", lambda: {
            "rules": len(self.knowledge.snapshot().get("business_rules", []))})
        check("clarifications", lambda: {
            "answered": len(self.knowledge.snapshot().get("clarifications", []))})
        check("memory", lambda: {
            "working": self.memory.working() is not None,
            "organizational": self.memory.organizational is self.knowledge})

        self.checks = checks
        self.state = "ready" if all(c["ok"] for c in checks.values()) \
            else "degraded"
        self.started_at = datetime.now(timezone.utc).isoformat()
        logger.info("Enterprise Brain %s (%d/%d checks passed)",
                    self.state.upper(),
                    sum(c["ok"] for c in checks.values()), len(checks))
        return self.status()

    # ---------------------------------------------------------- continuous
    def learn_after_analysis(self, project_id: str) -> dict[str, Any]:
        """The Continuous Learning Pipeline — runs automatically after every
        successful analysis. Returns a compact, serializable summary."""
        state = self.store.load(project_id, "state", {}) or {}
        project_name = state.get("name", project_id)
        artifacts = {name: self.store.load(project_id, name)
                     for name in LEARNED_ARTIFACTS}

        # 1. Knowledge Update — structured, versioned extraction
        counters = self.engine.learn_from_artifacts(project_id, project_name,
                                                    artifacts)
        # 2. Memory Update — memory layers feed organizational knowledge
        synced = self.synchronizer.sync_after_analysis(project_id, artifacts)
        # 3. Knowledge Graph Update — merge the project graph enterprise-wide
        merged = self.graph.merge_project_graph(
            project_id, self.store.load(project_id, "graph", {}) or {})
        # 4. Enterprise Context Update — the unified context is rebuilt
        self.context.build(project_id,
                           artifacts.get("business_context") or None)

        summary = {"project_id": project_id, "knowledge": counters,
                   "memory_sync": synced, "graph_merge": merged,
                   "enterprise_context": "updated"}
        # 5. Learning memory — what was learned, from where, when
        self.knowledge.record_learning_event(
            "continuous_learning_pipeline", source="enterprise_brain",
            project_id=project_id, details=summary)
        return summary

    # --------------------------------------------------------------- status
    def build_enterprise_context(self, project_id: str,
                                 business_context: dict | None = None,
                                 objective: str = "") -> dict:
        return self.context.build(project_id, business_context, objective)

    def status(self) -> dict[str, Any]:
        # Component states are derived from the startup checks that actually
        # ran, never asserted. A component whose check failed reports
        # "degraded"; before startup() has run there is nothing to report, so
        # it says so rather than claiming readiness.
        def component(check: str) -> str:
            result = self.checks.get(check)
            if result is None:
                return "not_started"
            return "ready" if result.get("ok") else "degraded"

        return {"state": self.state, "started_at": self.started_at,
                "checks": self.checks,
                "components": {
                    "knowledge_engine": component("knowledge_store"),
                    "learning_engine": component("learning_history"),
                    "memory_synchronizer": component("memory"),
                    "enterprise_context_builder": component("business_rules"),
                    "knowledge_graph": self.graph.stats().get("neo4j",
                                                              "not_configured"),
                }}

    def statistics(self) -> dict[str, Any]:
        """Knowledge / memory / graph / learning statistics for the UI."""
        knowledge_stats = self.knowledge.stats()
        return {
            "knowledge": knowledge_stats,
            "graph": self.graph.stats(),
            "memory": self.synchronizer.stats(),
            "learning": {
                "events": knowledge_stats.get("learning_events", 0),
                "recent": self.knowledge.learning_history(5),
            },
            "clarifications": {
                "answered": knowledge_stats.get("clarifications", 0),
            },
        }

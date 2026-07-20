"""Enterprise Context Builder.

Combines everything the platform knows into ONE unified Enterprise Context:

    current analysis facts (business context: KPIs, signals, forecasts,
    schema, quality, ML predictions, evidence ids, limitations)
  + organizational knowledge (terminology, business rules, clarifications)
  + organizational memory (decisions, report history, strategic insights,
    verified insights, open recommendations)
  + enterprise knowledge graph (scale + cross-project links)
  + the business objective

The result is a strict superset of the per-project business context, so
every existing evidence id, verifier check, and report-assembler consumer
keeps working unchanged — the organizational layers ride along under the
``enterprise`` key. This context is the ONLY thing the Prompt Engine may
consume; no raw Excel, CSV, DataFrames, SQL rows, or documents ever reach a
prompt.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from app.core.logging import get_logger
from app.knowledge.graph import EnterpriseKnowledgeGraph
from app.knowledge.store import KnowledgeStore
from app.repositories.artifact_store import ArtifactStore

logger = get_logger(__name__)

MAX_MEMORY_ITEMS = 8


class EnterpriseContextBuilder:
    """Builds and persists the unified Enterprise Context for one project."""

    def __init__(self, store: ArtifactStore, knowledge: KnowledgeStore,
                 graph: EnterpriseKnowledgeGraph):
        self.store = store
        self.knowledge = knowledge
        self.graph = graph

    def build(self, project_id: str, business_context: dict | None = None,
              objective: str = "") -> dict[str, Any]:
        """Assemble the Enterprise Context and persist it as the
        ``enterprise_context`` artifact. ``business_context`` may be passed
        by the running pipeline (fresh facts) or loaded from the store."""
        bc = business_context if business_context is not None else \
            (self.store.load(project_id, "business_context", {}) or {})
        state = self.store.load(project_id, "state", {}) or {}
        name = state.get("name", project_id)

        enterprise = {
            "business_objective": objective or state.get("objective") or (
                f"Understand, monitor, and improve the business represented "
                f"by project '{name}'"),
            "knowledge": self.knowledge.context_for_reasoning(),
            "memory": {
                "recent_decisions": self.knowledge.decisions(MAX_MEMORY_ITEMS),
                "report_history": self.knowledge.report_history(MAX_MEMORY_ITEMS),
                "strategic_insights": self.knowledge.strategic_insights(MAX_MEMORY_ITEMS),
                "verified_insights": self.knowledge.insights(MAX_MEMORY_ITEMS),
                "open_recommendations": self.knowledge.recommendations(MAX_MEMORY_ITEMS),
            },
            "knowledge_graph": {
                "stats": {k: v for k, v in self.graph.stats().items()
                          if k in ("node_count", "edge_count", "node_kinds")},
                "related_projects": self.graph.related_projects(project_id),
            },
            "generated_at": datetime.now(timezone.utc).isoformat(),
        }
        context = {**bc, "enterprise": enterprise}
        self.store.save(project_id, "enterprise_context", context)
        return context

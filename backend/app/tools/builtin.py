"""Built-in tools wrapping existing platform capabilities."""
from __future__ import annotations

from typing import Any, Callable

from app.intelligence.analytics.engine import AnalyticsEngine
from app.intelligence.embeddings.embedder import Embedder
from app.knowledge.store import KnowledgeStore
from app.repositories.artifact_store import ArtifactStore
from app.tools.base import Tool


class VectorSearchTool(Tool):
    """Semantic search over a project's analytics documents."""

    name = "vector_search"
    description = "Semantic search over schema, KPIs, signals, and relationships of a project"

    def __init__(self, embedder: Embedder, vector_store_factory: Callable):
        self._embedder = embedder
        self._vs_factory = vector_store_factory

    def run(self, *, project_id: str, query: str, top_k: int = 8) -> list[dict]:
        qvec = self._embedder.embed([query])[0]
        return self._vs_factory(project_id).search(qvec, top_k=top_k)


class ArtifactLookupTool(Tool):
    """Fetch any analytical artifact (kpis, signals, forecasts, quality, ...)."""

    name = "artifact_lookup"
    description = "Load a project's analytical facts: kpis, signals, forecasts, quality, business_context, relationships"

    def __init__(self, store: ArtifactStore):
        self._store = store

    def run(self, *, project_id: str, artifact: str, default: Any = None) -> Any:
        return self._store.load(project_id, artifact, default)


class AnalyticsSQLTool(Tool):
    """Read-only SQL over the project's DuckDB analytics warehouse."""

    name = "analytics_sql"
    description = "Run a read-only SELECT against the project analytics warehouse"

    def __init__(self, store: ArtifactStore):
        self._store = store

    def run(self, *, project_id: str, sql: str) -> Any:
        stmt = sql.strip().rstrip(";")
        if not stmt.lower().startswith(("select", "with")):
            raise ValueError("Only read-only SELECT queries are allowed")
        return AnalyticsEngine(self._store.duckdb_path(project_id)).query(stmt)


class KnowledgeSearchTool(Tool):
    """Search the enterprise knowledge store."""

    name = "knowledge_search"
    description = "Search enterprise terminology, rules, clarifications, and decision history"

    def __init__(self, knowledge: KnowledgeStore):
        self._knowledge = knowledge

    def run(self, *, query: str, limit: int = 10) -> list[dict]:
        return self._knowledge.search(query, limit)


class ReportMarkdownTool(Tool):
    """Render a project's executive report as markdown."""

    name = "report_markdown"
    description = "Render the assembled executive report of a project as markdown"

    def __init__(self, store: ArtifactStore):
        self._store = store

    def run(self, *, project_id: str) -> str:
        from app.reports.markdown import render_markdown
        report = self._store.load(project_id, "report")
        if report is None:
            raise ValueError("Report not generated yet — run the analysis workflow first")
        return render_markdown(report)

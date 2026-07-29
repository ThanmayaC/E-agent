"""Synchronization Layer — composition root and runtime integration.

Assembles the registry, reader, sync engine, organizational model,
relationship engine, refresh pipeline, and enterprise search, then hands the
autonomy runtime a set of jobs. The heartbeat already exists; this layer does
not build a second one — it registers on the first.

Jobs:

    startup_organization  build the organizational model from what the
                          platform already holds (startup, once)
    source_health         keep Connected Systems honest (interval)
    knowledge_refresh     synchronize every due source and refresh knowledge
                          (interval — the layer's heartbeat)
    refresh_on_import     a dataset landed: refresh now, do not wait for the
                          cadence (event)
    organization_sweep    re-observe platform entities and cross-domain links
                          (cron, nightly)
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.sync.engine import SynchronizationEngine
from app.sync.organization import OrganizationalModel
from app.sync.pipeline import KnowledgeRefreshPipeline
from app.sync.reader import SourceReader
from app.sync.registry import DataSourceRegistry
from app.sync.relationships import RelationshipEngine
from app.sync.search import EnterpriseSearch
from app.sync.store import SyncStore

logger = get_logger(__name__)


class SynchronizationLayer:
    """The Enterprise Knowledge Synchronization Layer, assembled."""

    def __init__(self, settings, store, knowledge, connectors, embedder=None,
                 vector_store_for=None, brain=None, tasks=None,
                 portfolio=None, graph=None, latency=None):
        self.settings = settings
        self.store = SyncStore(settings.sync_dir)
        self.registry = DataSourceRegistry(self.store)
        self.reader = SourceReader(connectors)
        self.engine = SynchronizationEngine(self.store, self.registry,
                                            self.reader)
        self.organization = OrganizationalModel(self.store, graph=graph,
                                                knowledge=knowledge)
        self.relationships = RelationshipEngine(self.store, self.organization,
                                                graph=graph)
        # Document Intelligence (V2): parses, chunks, embeds, and versions
        # documents the sync detected. Optional — a deployment can disable it
        # and document sources degrade to catalog-only sync.
        self.documents = None
        if getattr(settings, "documents_enabled", True):
            from app.documents import (
                DocumentIntelligence, DocumentParser, DocumentStore,
            )
            self.documents = DocumentIntelligence(
                store=DocumentStore(settings.data_dir / "documents"),
                parser=DocumentParser(
                    ocr_enabled=getattr(settings, "document_ocr_enabled", True)),
                chunk_chars=getattr(settings, "document_chunk_chars", 1600),
                chunk_overlap=getattr(settings, "document_chunk_overlap", 200),
                embedder=embedder, vector_store_for=vector_store_for,
                knowledge=knowledge, organization=self.organization,
                graph_client_for=self._graph_client_for, latency=latency,
                embedding_model=getattr(settings, "embedding_model", ""))
        self.pipeline = KnowledgeRefreshPipeline(
            self.store, self.engine, self.registry, self.organization,
            self.relationships, knowledge, brain=brain, artifacts=store,
            embedder=embedder, vector_store_for=vector_store_for,
            documents=self.documents)
        self.search = EnterpriseSearch(
            knowledge, store, self.organization, self.relationships,
            tasks=tasks, portfolio=portfolio, embedder=embedder,
            vector_store_for=vector_store_for, documents=self.documents)
        self._artifacts = store
        self._knowledge = knowledge
        self._bus = None

    # ------------------------------------------------------------ wiring
    def attach_bus(self, bus) -> None:
        """Announce on the enterprise event bus. Called by the autonomy
        runtime, which owns the bus — the sync layer is built before it."""
        self._bus = bus
        components = [self.registry, self.engine, self.organization,
                      self.relationships, self.pipeline]
        if self.documents is not None:
            components.append(self.documents)
        for component in components:
            component.attach_bus(bus)

    def _graph_client_for(self, source: dict):
        """A GraphClient for a registered Microsoft 365 source, resolving its
        credential by reference at call time (never stored)."""
        from app.communication.graph import GraphClient
        return GraphClient(self.registry.auth_for(source)
                           .require(source["name"]))

    def register_jobs(self, scheduler, JobDefinition, RetryPolicy) -> None:
        """Register synchronization work on the existing Enterprise
        Scheduler. The classes are passed in rather than imported so this
        layer never depends on the runtime package."""
        settings = self.settings
        retry = RetryPolicy(attempts=2, backoff_seconds=5.0)

        scheduler.register(JobDefinition(
            "startup_organization",
            "Build the organizational model from what the platform knows",
            "startup", self.build_organization, retry=retry,
            tags=["startup", "organization"]))
        scheduler.register(JobDefinition(
            "source_health", "Check every connected system's health",
            "interval", self.registry.check_all,
            interval_seconds=settings.sync_health_interval_seconds,
            retry=retry, tags=["sync", "health"]))
        scheduler.register(JobDefinition(
            "knowledge_refresh",
            "Synchronize due sources and refresh organizational knowledge",
            "interval", self.refresh,
            interval_seconds=settings.sync_refresh_interval_seconds,
            depends_on=["source_health"], retry=RetryPolicy(attempts=1),
            tags=["sync", "knowledge"]))
        scheduler.register(JobDefinition(
            "refresh_on_import",
            "Refresh organizational knowledge when new data lands",
            "event", self.refresh, event="DatasetImported", retry=retry,
            tags=["sync", "event"]))
        scheduler.register(JobDefinition(
            "organization_sweep",
            "Re-observe platform entities and cross-domain links",
            "cron", self.sweep_organization, cron=settings.sync_sweep_cron,
            retry=retry, tags=["organization", "nightly"]))

    # -------------------------------------------------------------- jobs
    def refresh(self, source_id: str = "", trigger: str = "scheduled") -> dict:
        """The layer's heartbeat: sync what is due, learn what changed."""
        return self.pipeline.refresh(source_id=source_id,
                                     trigger=trigger).describe()

    def build_organization(self) -> dict:
        """Construct the organizational model from what the platform already
        holds — projects, reports, KPIs, business rules, and every project's
        semantic layer. Idempotent: it observes, it does not rebuild."""
        counts = self.organization.observe_platform_entities(
            self._artifacts, self._knowledge)
        for pid in self._artifacts.list_projects():
            state = self._artifacts.load(pid, "state") or {}
            semantics = self._artifacts.load(pid, "semantic_layer", {}) or {}
            if semantics:
                found = self.organization.observe_from_semantics(
                    pid, state.get("name", pid), semantics)
                counts["semantic_entities"] = (
                    counts.get("semantic_entities", 0) + found["discovered"])
        counts.update(self.relationships.detect_dependencies(self._artifacts))
        return counts

    def sweep_organization(self) -> dict:
        outcome = self.build_organization()
        outcome.update(self.relationships.detect_cross_domain())
        return outcome

    # ------------------------------------------------------------- status
    def status(self) -> dict[str, Any]:
        """Runtime status for the synchronization layer."""
        return {
            "sources": self.registry.status(),
            "synchronization": self.engine.stats(),
            "organization": self.organization.counts(),
            "relationships": self.relationships.stats(),
            "freshness": self.pipeline.freshness(),
            "documents": (self.documents.status() if self.documents is not None
                          else {"enabled": False}),
        }

    def overview(self) -> dict[str, Any]:
        """Organization Overview for the Executive Workspace — business
        framing only: what the organization contains, what is connected, how
        fresh it is. No sync mechanics, no fingerprints, no vectors."""
        sources = self.registry.status()
        organization = self.organization.overview()
        freshness = self.pipeline.freshness()
        return {
            "entities_total": organization["entities_total"],
            "by_kind": organization["by_kind"],
            "owned": organization["owned"],
            "unowned": organization["unowned"],
            "connected_systems": {
                "total": sources["total"],
                "connected": sources["connected"],
                "needs_attention": sources["needs_attention"],
                "awaiting_integration": sources["awaiting_integration"],
                "systems": [
                    {"name": s["name"], "type": s["title"],
                     "status": _business_health(s),
                     "last_synced_at": s["last_synced_at"],
                     "records": s["records_total"]}
                    for s in self.registry.sources()],
            },
            "knowledge_freshness": {
                "status": ("current" if freshness["is_fresh"]
                           else "needs attention"),
                "last_updated_at": freshness["last_refresh_at"],
                "systems_needing_attention": freshness["sources_stale"],
            },
            "recent_synchronizations": [
                {"system": r["source"], "at": r["finished_at"],
                 "outcome": ("updated" if r["status"] == "completed"
                             else r["status"]),
                 "records_changed": r.get("changed_records", 0)}
                for r in self.engine.runs(limit=8)],
            "relationships_total": self.relationships.stats()["total"],
            "recently_discovered": organization["recently_discovered"][:5],
        }


def _business_health(source: dict) -> str:
    """Health in business language — an executive reads "connected", not
    "unconfigured"."""
    return {
        "healthy": "connected",
        "degraded": "having trouble",
        "unreachable": "not responding",
        "unconfigured": "needs credentials",
        "awaiting_integration": "available in Version 2",
        "unknown": "not yet synchronized",
    }.get(source["health"], source["health"])

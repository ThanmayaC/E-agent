"""Enterprise Connector Framework — composition root and runtime integration.

Assembles the connector registry, the configuration store, and the Enterprise
Sync Service, wires the ingestion handler to the pipeline that already exists,
and hands the autonomy runtime a set of jobs.

The framework does not own a clock, a queue, a bus, or a document pipeline. It
registers on the Enterprise Scheduler, publishes on the enterprise Event Bus,
and hands packages to Document Intelligence — every one of which was already
built. What it adds is the one thing that was missing: a uniform contract for
*getting* enterprise knowledge in, so that adding SharePoint later touches one
new file and nothing else.

Jobs registered on the existing scheduler:

    connector_health      every source's own health assessment (interval)
    connector_sync        synchronize every due source (interval — the
                          framework's heartbeat)
    connector_sync_boot   first synchronization after startup, once
    connector_full_sweep  nightly full re-read, so a missed delta self-heals
                          (cron)
"""
from __future__ import annotations

from typing import Any

from app.connectors.package import KnowledgePackage
from app.connectors.registry import ConnectorRegistry, build_registry
from app.connectors.service import EnterpriseSyncService
from app.connectors.store import ConnectorStore
from app.core.logging import get_logger

logger = get_logger(__name__)

# A folder source says what kind of documents it holds; Document Intelligence
# already categorizes by source kind, so this maps the connector's option onto
# the vocabulary that store already uses rather than inventing a second one.
CATEGORY_SOURCE_KINDS = {
    "sop": "sop_repository", "rca": "rca_repository",
    "policy": "policy_repository", "meeting": "meeting_notes",
    "product_document": "product_documents", "document": "document_folder",
}


class EnterpriseConnectorFramework:
    """The Enterprise Connector Framework, assembled."""

    def __init__(self, settings, documents=None, knowledge=None,
                 registry: ConnectorRegistry | None = None):
        self.settings = settings
        self.store = ConnectorStore(settings.connectors_dir)
        self.registry = registry or build_registry()
        self.documents = documents      # DocumentIntelligence, or None
        self._knowledge = knowledge
        self.service = EnterpriseSyncService(self.store, self.registry)
        self.service.set_ingestion_handler(self.ingest)

    # ------------------------------------------------------------- wiring
    def attach_bus(self, bus) -> None:
        """Announce on the enterprise event bus, which the runtime owns."""
        self.service.attach_bus(bus)

    def register_jobs(self, scheduler, JobDefinition, RetryPolicy) -> None:
        """Register connector work on the existing Enterprise Scheduler.

        The classes are passed in rather than imported so this package never
        depends on the runtime package — the same contract the synchronization
        layer already follows.
        """
        settings = self.settings
        retry = RetryPolicy(attempts=2, backoff_seconds=5.0)

        scheduler.register(JobDefinition(
            "connector_health", "Assess every enterprise data source",
            "interval", self.service.check_all,
            interval_seconds=settings.connector_health_interval_seconds,
            retry=retry, tags=["connectors", "health"]))
        scheduler.register(JobDefinition(
            "connector_sync",
            "Synchronize every due enterprise data source",
            "interval", self.service.sync_due,
            interval_seconds=settings.connector_sync_interval_seconds,
            depends_on=["connector_health"], retry=RetryPolicy(attempts=1),
            tags=["connectors", "sync"]))
        scheduler.register(JobDefinition(
            "connector_sync_boot",
            "First synchronization of connected data sources after startup",
            "startup", self.service.sync_due, retry=RetryPolicy(attempts=1),
            tags=["connectors", "startup"]))
        scheduler.register(JobDefinition(
            "connector_full_sweep",
            "Full re-read of every source, so a missed change self-heals",
            "cron", lambda: self.service.sync_all(full=True),
            cron=settings.connector_sweep_cron, retry=retry,
            tags=["connectors", "nightly"]))

    # ---------------------------------------------------------- ingestion
    def ingest(self, record: dict, packages: list[KnowledgePackage],
               removed: list[str]) -> dict[str, Any]:
        """Route one source's packages into the pipeline that already exists.

            document packages → Document Intelligence → embeddings → Brain
            table packages    → the package catalogue and the event bus

        Table packages carry structure, not content: the analytics layers read
        their own data through the Intelligence Engine, so pushing rows into
        the document pipeline would duplicate a path that already works.
        """
        documents = [p for p in packages if p.family == "document"]
        tables = [p for p in packages if p.family == "table"]
        counts: dict[str, Any] = {"documents": 0, "tables": len(tables),
                                  "removed": len(removed)}

        if documents and self.documents is not None:
            outcome = self.documents.process_sync(
                self._document_source(record),
                [_PackageDelta(documents, removed)])
            counts["documents"] = outcome.get("ingested", 0) + outcome.get(
                "updated", 0)
            counts["document_pipeline"] = outcome
        elif documents:
            counts["documents"] = len(documents)
            counts["note"] = "Document Intelligence is disabled in this deployment"

        if tables:
            counts["schemas"] = self._record_schemas(record, tables)
        return counts

    def _document_source(self, record: dict) -> dict:
        """The source shape Document Intelligence consumes, with the category
        the administrator configured."""
        category = (record.get("options") or {}).get("category", "document")
        return {"name": record["name"],
                "kind": CATEGORY_SOURCE_KINDS.get(category, "document_folder"),
                "connector_id": record["connector_id"]}

    def _record_schemas(self, record: dict,
                        tables: list[KnowledgePackage]) -> int:
        """Note discovered schemas as organizational knowledge.

        Structure only — a table's name, columns, and types are things the
        organization knows about itself, and the Brain already stores facts of
        exactly this shape.
        """
        if self._knowledge is None:
            return 0
        noted = 0
        for package in tables:
            metadata = package.structured_metadata
            columns = metadata.get("columns") or []
            if not columns:
                # Workbook packages nest their schema per sheet.
                columns = [c for sheet in
                           (metadata.get("tables_by_sheet") or {}).values()
                           for table in sheet for c in table.get("schema", [])]
            if not columns:
                continue
            try:
                self._knowledge.record_learning_event(
                    f"{record['name']} provides '{package.title}' with "
                    f"{len(columns)} columns "
                    f"({', '.join(str(c['name']) for c in columns[:8])}"
                    f"{'…' if len(columns) > 8 else ''})",
                    source=f"connector:{record['kind']}",
                    project_id=record.get("project_id", ""),
                    details={"connector_id": record["connector_id"],
                             "item": package.item_id,
                             "columns": len(columns)})
                noted += 1
            except Exception:  # noqa: BLE001 — knowledge is a consumer, not a gate
                logger.exception("Recording schema knowledge failed for %s",
                                 package.title)
        return noted

    # ------------------------------------------------------------- status
    def status(self) -> dict[str, Any]:
        """Runtime status of the connector framework."""
        return {"enabled": True,
                "sources": self.service.status(),
                "catalogue": self.registry.describe(),
                "kinds": self.registry.kinds(),
                "documents_pipeline": self.documents is not None}


class _PackageDelta:
    """Adapts KnowledgePackages to the sync-delta shape Document Intelligence
    already consumes.

    The document pipeline was built against the Synchronization Engine's
    deltas and is not modified by this framework: packages adapt to it. That
    keeps V2.1 additive — the V2 document path behaves exactly as before.
    """

    table = "documents"

    def __init__(self, packages: list[KnowledgePackage], removed: list[str]):
        self.added = [{"key": p.key, "table": "documents",
                       "record": p.as_document_record()} for p in packages]
        self.changed: list[dict] = []
        # The pipeline splits a "documents:<id>" key on the first colon.
        self.removed = [f"documents:{key}" for key in removed]
        self.unchanged = 0
        self.columns: list[str] = []
        self.truncated = False

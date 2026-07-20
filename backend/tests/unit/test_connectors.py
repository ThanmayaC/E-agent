"""Enterprise Connector Framework (V2.1) — the lifecycle contract, the
registry, the four shipped connectors, and the Enterprise Sync Service.

Connectors are driven against real files on disk rather than mocks:
incremental synchronization is a claim about what happens when a folder
actually changes, and a fake source cannot falsify it.
"""
from __future__ import annotations

import pandas as pd
import pytest

from app.connectors.base import (
    ConnectionFailed, ConnectorConfig, ConnectorNotConfigured,
    EnterpriseConnector, SyncCursor,
)
from app.connectors.csv import CSVConnector
from app.connectors.excel import ExcelConnector
from app.connectors.folder import FolderConnector
from app.connectors.framework import EnterpriseConnectorFramework
from app.connectors.package import KnowledgePackage
from app.connectors.postgres import PostgreSQLConnector
from app.connectors.registry import (
    ConnectorNotRegistered, ConnectorRegistry, build_registry,
)
from app.connectors.service import EnterpriseSyncService
from app.connectors.store import ConnectorStore


# --------------------------------------------------------------- fixtures
@pytest.fixture()
def documents_dir(tmp_path):
    root = tmp_path / "enterprise_docs"
    root.mkdir()
    (root / "refund_policy.md").write_text(
        "# Refund policy\nRefunds are issued within 30 days.", encoding="utf-8")
    (root / "standup.txt").write_text("Standup: V2.1 ships Friday.",
                                      encoding="utf-8")
    (root / "ignore.bin").write_bytes(b"\x00\x01\x02")  # unsupported: ignored
    return root


@pytest.fixture()
def csv_dir(tmp_path):
    root = tmp_path / "finance"
    root.mkdir()
    pd.DataFrame({"invoice_id": [1, 2, 3],
                  "customer": ["North", "South", "East"],
                  "amount": [120.5, 90.0, 310.25]}).to_csv(
        root / "invoices.csv", index=False)
    return root


@pytest.fixture()
def workbook(tmp_path):
    path = tmp_path / "kpis.xlsx"
    with pd.ExcelWriter(path) as writer:
        pd.DataFrame({"month": ["Jan", "Feb"], "revenue": [100, 120]}).to_excel(
            writer, sheet_name="Revenue", index=False)
        pd.DataFrame({"region": ["North", "South"], "headcount": [12, 9]}).to_excel(
            writer, sheet_name="People", index=False)
    return path


@pytest.fixture()
def service(tmp_path):
    return EnterpriseSyncService(ConnectorStore(tmp_path / "connectors"),
                                 build_registry())


def config_for(kind: str, location, **options) -> ConnectorConfig:
    return ConnectorConfig(connector_id=f"conn_{kind}", name=f"{kind} source",
                           kind=kind, location=str(location), options=options)


# ---------------------------------------------------------------- registry
def test_registry_loads_the_shipped_connectors():
    registry = build_registry()
    assert set(registry.kinds()) == {"folder", "excel", "csv", "postgresql"}


def test_registry_reports_planned_connectors_instead_of_pretending():
    registry = build_registry()
    with pytest.raises(ConnectorNotRegistered, match="planned"):
        registry.get("sharepoint")


def test_registry_loads_a_connector_from_a_dotted_path():
    """A deployment adds its own connector without touching the framework."""
    registry = ConnectorRegistry()
    assert registry.load("folder", "app.connectors.folder:FolderConnector")
    assert registry.has("folder")


def test_a_bad_dotted_path_degrades_one_kind_not_the_catalogue():
    registry = ConnectorRegistry()
    assert not registry.load("ghost", "app.connectors.nope:Missing")
    assert registry.load("csv", "app.connectors.csv:CSVConnector")
    assert registry.kinds() == ["csv"]
    entry = next(e for e in registry.describe() if e["kind"] == "ghost")
    assert not entry["available"] and entry["unavailable_reason"]


# --------------------------------------------------------------- interface
def test_every_shipped_connector_implements_the_lifecycle():
    lifecycle = ("initialize", "connect", "test_connection", "discover",
                 "sync", "incremental_sync", "fetch_metadata",
                 "fetch_content", "health", "disconnect")
    for connector_class in (FolderConnector, ExcelConnector, CSVConnector,
                            PostgreSQLConnector):
        assert issubclass(connector_class, EnterpriseConnector)
        for method in lifecycle:
            assert callable(getattr(connector_class, method)), \
                f"{connector_class.__name__} is missing {method}()"


def test_a_connector_without_configuration_refuses_to_initialize():
    connector = FolderConnector(ConnectorConfig(
        connector_id="c1", name="nowhere", kind="folder"))
    with pytest.raises(ConnectorNotConfigured):
        connector.initialize()


def test_test_connection_answers_instead_of_raising(tmp_path):
    connector = FolderConnector(config_for("folder", tmp_path / "missing"))
    result = connector.test_connection()
    assert not result.ok and "does not exist" in result.detail


# -------------------------------------------------- unified knowledge package
def test_every_connector_produces_the_same_shape(documents_dir, csv_dir,
                                                 workbook):
    produced = []
    for connector in (FolderConnector(config_for("folder", documents_dir)),
                      CSVConnector(config_for("csv", csv_dir)),
                      ExcelConnector(config_for("excel", workbook))):
        outcome = connector.sync()
        assert outcome.packages
        produced.extend(outcome.packages)

    for package in produced:
        assert isinstance(package, KnowledgePackage)
        assert package.source_id and package.connector_type and package.title
        assert package.checksum and package.version >= 1
        assert package.modified_date
        described = package.describe()
        assert "raw_content" not in described  # content never persists


def test_package_identity_is_stable_across_syncs(documents_dir):
    connector = FolderConnector(config_for("folder", documents_dir))
    first = connector.sync()
    keys = {p.key for p in first.packages}
    (documents_dir / "refund_policy.md").write_text("# Refund policy\n45 days.",
                                                    encoding="utf-8")
    second = connector.incremental_sync(first.cursor)
    assert {p.key for p in second.packages} <= keys  # a change, not a new doc


# --------------------------------------------------------- folder connector
def test_folder_connector_detects_new_updated_and_deleted(documents_dir):
    connector = FolderConnector(config_for("folder", documents_dir))
    first = connector.sync()
    assert len(first.packages) == 2          # the .bin file is not a document
    assert first.mode == "full"

    unchanged = connector.incremental_sync(first.cursor)
    assert unchanged.packages == [] and unchanged.unchanged == 2

    (documents_dir / "refund_policy.md").write_text("# Refund policy\n45 days.",
                                                    encoding="utf-8")
    (documents_dir / "standup.txt").unlink()
    (documents_dir / "new_sop.md").write_text("# SOP\nStep one.", encoding="utf-8")

    delta = connector.incremental_sync(unchanged.cursor)
    assert {p.item_id for p in delta.packages} == {"refund_policy.md",
                                                   "new_sop.md"}
    assert delta.removed == ["standup.txt"]
    assert delta.mode == "incremental"


def test_folder_connector_change_detection_survives_a_touch(documents_dir):
    """Content hash, not mtime: a touched-but-identical file is unchanged."""
    connector = FolderConnector(config_for("folder", documents_dir))
    first = connector.sync()
    path = documents_dir / "standup.txt"
    path.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    assert connector.incremental_sync(first.cursor).packages == []


def test_folder_connector_reads_metadata_and_content(documents_dir):
    connector = FolderConnector(config_for("folder", documents_dir))
    metadata = connector.fetch_metadata("standup.txt")
    assert metadata["extension"] == ".txt" and metadata["checksum"]
    assert b"Standup" in connector.fetch_content("standup.txt")


def test_folder_connector_refuses_to_escape_its_folder(documents_dir):
    connector = FolderConnector(config_for("folder", documents_dir))
    with pytest.raises(ConnectionFailed, match="outside the monitored folder"):
        connector.fetch_content("../../../etc/passwd")


# ---------------------------------------------------- excel/csv connectors
def test_excel_connector_extracts_workbook_structure(workbook):
    connector = ExcelConnector(config_for("excel", workbook))
    metadata = connector.fetch_metadata(workbook.name)
    assert metadata["sheet_count"] == 2
    assert set(metadata["sheets"]) == {"Revenue", "People"}
    revenue = metadata["tables_by_sheet"]["Revenue"][0]
    assert revenue["rows"] == 2 and revenue["columns"] == 2
    types = {c["name"]: c["type"] for c in revenue["schema"]}
    assert types["month"] == "text" and types["revenue"] == "integer"
    assert metadata["modified_at"]


def test_csv_connector_extracts_schema_and_types(csv_dir):
    connector = CSVConnector(config_for("csv", csv_dir))
    outcome = connector.sync()
    assert len(outcome.packages) == 1
    package = outcome.packages[0]
    assert package.family == "table" and package.file_type == ".csv"
    table = package.structured_metadata["tables_by_sheet"]["csv"][0]
    types = {c["name"]: c["type"] for c in table["schema"]}
    assert types == {"invoice_id": "integer", "customer": "text",
                     "amount": "decimal"}


def test_tabular_connectors_do_no_analytics(csv_dir):
    """V2.1 extracts structure only — profiling stays downstream."""
    package = CSVConnector(config_for("csv", csv_dir)).sync().packages[0]
    schema = package.structured_metadata["tables_by_sheet"]["csv"][0]["schema"]
    forbidden = {"mean", "median", "std", "outliers", "correlation", "kpi"}
    assert not forbidden & set(schema[0])


# ------------------------------------------------------ postgres connector
def test_postgres_connector_requires_a_credential_reference():
    connector = PostgreSQLConnector(ConnectorConfig(
        connector_id="pg", name="warehouse", kind="postgresql"))
    with pytest.raises(ConnectorNotConfigured, match="connection URL"):
        connector.initialize()


def test_postgres_connector_rejects_a_non_postgres_url(monkeypatch):
    monkeypatch.setenv("EDIP_TEST_DB", "mysql://host/db")
    connector = PostgreSQLConnector(ConnectorConfig(
        connector_id="pg", name="warehouse", kind="postgresql",
        auth_kind="env", auth_ref="EDIP_TEST_DB"))
    connector.initialize()
    result = connector.test_connection()
    assert not result.ok and "PostgreSQL URL" in result.detail


def test_database_connector_reads_schema_from_sqlite(tmp_path, monkeypatch):
    """The generic DatabaseConnector is engine-agnostic by construction, so
    SQLite exercises the same discovery path PostgreSQL takes."""
    from sqlalchemy import create_engine, text

    from app.connectors.database import DatabaseConnector

    db_path = tmp_path / "erp.db"
    engine = create_engine(f"sqlite:///{db_path.as_posix()}")
    with engine.begin() as connection:
        connection.execute(text(
            "CREATE TABLE orders (id INTEGER PRIMARY KEY, customer TEXT NOT NULL, "
            "updated_at TEXT)"))
        connection.execute(text(
            "INSERT INTO orders VALUES (1, 'North', '2026-01-01')"))
    engine.dispose()

    monkeypatch.setenv("EDIP_TEST_SQLITE", f"sqlite:///{db_path.as_posix()}")
    connector = DatabaseConnector(ConnectorConfig(
        connector_id="db", name="erp", kind="database", auth_kind="env",
        auth_ref="EDIP_TEST_SQLITE", options={"watermark_column": "updated_at"}))
    connector.initialize()

    assert connector.test_connection().ok
    discovery = connector.discover()
    assert [i.name for i in discovery.items] == ["orders"]

    metadata = connector.fetch_metadata("orders")
    assert metadata["column_count"] == 3
    assert metadata["primary_key"] == ["id"]
    assert {c["name"] for c in metadata["columns"]} == {"id", "customer",
                                                        "updated_at"}

    outcome = connector.sync()
    assert len(outcome.packages) == 1
    assert outcome.packages[0].family == "table"

    unchanged = connector.incremental_sync(outcome.cursor)
    assert unchanged.unchanged == 1 and not unchanged.packages
    connector.disconnect()


def test_database_errors_never_leak_the_credential(monkeypatch):
    from app.connectors.database import _safe

    monkeypatch.setenv("EDIP_TEST_DB", "postgresql://user:hunter2@db/prod")
    message = _safe(RuntimeError("could not connect to "
                                 "postgresql://user:hunter2@db/prod"),
                    "EDIP_TEST_DB")
    assert "hunter2" not in message and "$EDIP_TEST_DB" in message


# --------------------------------------------------- enterprise sync service
def test_service_registers_and_synchronizes_a_source(service, documents_dir):
    source = service.register("Ops folder", "folder", location=str(documents_dir))
    assert source["health"] == "unknown" and source["sync_state"] == "never_synced"

    first = service.sync_one(source["connector_id"])
    assert first["status"] == "completed" and first["packages"] == 2

    stored = service.get(source["connector_id"])
    assert stored["sync_state"] == "synced" and stored["health"] == "healthy"
    assert stored["items_total"] == 2 and stored["next_sync_at"]

    second = service.sync_one(source["connector_id"])
    assert second["mode"] == "incremental" and second["packages"] == 0


def test_service_refuses_a_duplicate_name(service, documents_dir):
    service.register("Ops", "folder", location=str(documents_dir))
    with pytest.raises(ValueError, match="already exists"):
        service.register("Ops", "folder", location=str(documents_dir))


def test_service_refuses_credentials_in_configuration(service):
    with pytest.raises(ValueError, match="credentials"):
        service.register("bad", "folder",
                         location="postgresql://user:pw@host/db")
    with pytest.raises(ValueError, match="reference"):
        service.register("bad", "folder", location="/data",
                        auth={"kind": "env", "password": "hunter2"})


def test_service_never_returns_a_secret(service, monkeypatch, tmp_path):
    monkeypatch.setenv("EDIP_TEST_DB", "postgresql://user:hunter2@db/prod")
    source = service.register("Warehouse", "postgresql", location="db.internal",
                              auth={"kind": "env", "ref": "EDIP_TEST_DB"})
    assert "hunter2" not in str(source)
    assert source["auth"] == {"kind": "env", "ref": "EDIP_TEST_DB",
                              "configured": True}


def test_service_records_failures_and_degrades_the_source(service, tmp_path):
    source = service.register("Missing folder", "folder",
                              location=str(tmp_path / "gone"))
    run = service.sync_one(source["connector_id"])
    assert run["status"] == "failed" and "does not exist" in run["error"]

    stored = service.get(source["connector_id"])
    assert stored["consecutive_failures"] == 1 and stored["health"] == "degraded"
    assert service.failures(source["connector_id"])[0]["error"]

    for _ in range(2):
        service.sync_one(source["connector_id"])
    assert service.get(source["connector_id"])["health"] == "unreachable"


def test_one_broken_source_never_stops_the_others(service, documents_dir,
                                                  tmp_path):
    service.register("Broken", "folder", location=str(tmp_path / "gone"))
    service.register("Working", "folder", location=str(documents_dir))
    summary = service.sync_all()
    assert summary["completed"] == 1 and summary["failed"] == 1
    assert summary["with_changes"] == ["Working"]


def test_a_disabled_source_is_skipped(service, documents_dir):
    source = service.register("Ops", "folder", location=str(documents_dir),
                              enabled=False)
    assert service.sync_one(source["connector_id"])["status"] == "skipped"
    assert service.due() == []


def test_manual_cadence_is_never_due(service, documents_dir):
    service.register("Ops", "folder", location=str(documents_dir),
                     cadence="manual")
    assert service.due() == []


def test_service_tests_connections_and_discovers(service, documents_dir):
    source = service.register("Ops", "folder", location=str(documents_dir))
    result = service.test_connection(source["connector_id"])
    assert result["ok"]
    assert service.get(source["connector_id"])["health"] == "healthy"
    assert service.discover(source["connector_id"])["count"] == 2


def test_removing_a_source_clears_its_sync_state(service, documents_dir):
    source = service.register("Ops", "folder", location=str(documents_dir))
    service.sync_one(source["connector_id"])
    assert service.remove(source["connector_id"])
    assert service.get(source["connector_id"]) is None
    assert not service.remove(source["connector_id"])


def test_editing_a_source_rebuilds_it(service, documents_dir, tmp_path):
    other = tmp_path / "other"
    other.mkdir()
    (other / "note.md").write_text("# Note", encoding="utf-8")
    source = service.register("Ops", "folder", location=str(documents_dir))
    service.sync_one(source["connector_id"])
    service.update(source["connector_id"], location=str(other))
    assert service.connector(source["connector_id"]).config.location == str(other)


def test_events_are_published_for_every_outcome(service, documents_dir,
                                                tmp_path):
    published = []

    class Bus:
        def publish(self, kind, payload, **kwargs):
            published.append(kind)

    service.attach_bus(Bus())
    ok = service.register("Ops", "folder", location=str(documents_dir))
    bad = service.register("Gone", "folder", location=str(tmp_path / "gone"))
    service.sync_one(ok["connector_id"])
    service.sync_one(bad["connector_id"])

    assert "ConnectorRegistered" in published
    assert "ConnectorSyncCompleted" in published
    assert "KnowledgePackagesProduced" in published
    assert "ConnectorSyncFailed" in published


def test_event_kinds_are_declared_on_the_bus():
    """The bus rejects unknown event names, so the framework's vocabulary
    must actually be part of the contract."""
    from app.runtime.events import EVENT_KINDS
    for kind in ("ConnectorRegistered", "ConnectorSyncStarted",
                 "ConnectorSyncCompleted", "ConnectorSyncFailed",
                 "ConnectorHealthChanged", "KnowledgePackagesProduced"):
        assert kind in EVENT_KINDS


# ------------------------------------------------------------- framework
def test_framework_registers_jobs_on_the_existing_scheduler(tmp_path):
    """The framework must not build a second scheduler — it registers on the
    one the runtime already owns."""
    from app.core.config import Settings
    from app.runtime.events import EventBus
    from app.runtime.scheduler import (
        EnterpriseScheduler, JobDefinition, RetryPolicy,
    )

    settings = Settings(data_dir=tmp_path)
    framework = EnterpriseConnectorFramework(settings)
    scheduler = EnterpriseScheduler(EventBus())
    framework.register_jobs(scheduler, JobDefinition, RetryPolicy)

    jobs = {j["name"]: j for j in scheduler.describe()}
    assert set(jobs) == {"connector_health", "connector_sync",
                         "connector_sync_boot", "connector_full_sweep"}
    assert jobs["connector_sync"]["kind"] == "interval"
    assert jobs["connector_sync_boot"]["kind"] == "startup"
    assert jobs["connector_full_sweep"]["kind"] == "cron"


def test_framework_ingests_documents_through_document_intelligence(
        tmp_path, documents_dir):
    """Packages must flow into the pipeline that already exists, unchanged."""
    from app.core.config import Settings
    from app.documents import DocumentIntelligence, DocumentParser, DocumentStore
    from app.knowledge.store import KnowledgeStore

    settings = Settings(data_dir=tmp_path)
    documents = DocumentIntelligence(
        store=DocumentStore(tmp_path / "documents"),
        parser=DocumentParser(ocr_enabled=False))
    framework = EnterpriseConnectorFramework(
        settings, documents=documents,
        knowledge=KnowledgeStore(tmp_path / "knowledge"))

    source = framework.service.register("Ops folder", "folder",
                                        location=str(documents_dir))
    run = framework.service.sync_one(source["connector_id"])
    assert run["status"] == "completed"
    assert run["ingested"]["documents"] == 2

    stored = documents.status()
    assert stored["documents"] >= 2


def test_framework_records_table_schemas_as_knowledge(tmp_path, csv_dir):
    from app.core.config import Settings
    from app.knowledge.store import KnowledgeStore

    knowledge = KnowledgeStore(tmp_path / "knowledge")
    framework = EnterpriseConnectorFramework(Settings(data_dir=tmp_path),
                                             knowledge=knowledge)
    source = framework.service.register("Finance", "csv", location=str(csv_dir))
    run = framework.service.sync_one(source["connector_id"])

    assert run["ingested"]["schemas"] == 1
    learned = knowledge.learning_history()
    assert any("invoices" in event["event"] for event in learned)


def test_framework_status_reports_the_catalogue(tmp_path):
    from app.core.config import Settings
    framework = EnterpriseConnectorFramework(Settings(data_dir=tmp_path))
    status = framework.status()
    assert status["enabled"]
    assert set(status["kinds"]) == {"folder", "excel", "csv", "postgresql"}
    assert any(e["kind"] == "sharepoint" and not e["available"]
               for e in status["catalogue"])


# ------------------------------------------------------------ cursor/state
def test_a_cursor_round_trips_through_persistence():
    cursor = SyncCursor(version=3, watermark="2026-01-01",
                        fingerprints={"a": "x"}, extra={"watermarks": {"t": "1"}})
    assert SyncCursor.from_dict(cursor.to_dict()).to_dict() == cursor.to_dict()


def test_a_failed_sync_preserves_the_last_good_cursor(service, documents_dir):
    source = service.register("Ops", "folder", location=str(documents_dir))
    service.sync_one(source["connector_id"])
    good = dict(service._store.cursor(source["connector_id"]))

    service.update(source["connector_id"], location=str(documents_dir / "gone"))
    assert service.sync_one(source["connector_id"])["status"] == "failed"
    assert service._store.cursor(source["connector_id"]) == good

"""Enterprise Connector Framework (Version 2.1).

The platform's uniform way of getting organizational knowledge *in*. An
administrator configures a data source once; the Runtime keeps it
synchronized forever; every document, spreadsheet, report, and table that
lands in it becomes organizational knowledge automatically. Managers never
upload anything.

    base        EnterpriseConnector — the lifecycle contract every source
                implements: initialize, connect, test_connection, discover,
                sync, incremental_sync, fetch_metadata, fetch_content,
                health, disconnect
    package     KnowledgePackage — the one normalized shape every connector
                produces, and the only thing downstream ever sees
    registry    ConnectorRegistry — the catalogue, with dynamic loading, so a
                new connector needs no framework change
    store       configurations, cursors, run history, package catalogue
    service     EnterpriseSyncService — scheduling, change detection,
                ingestion, retries, history, events. One engine, every
                connector.
    framework   EnterpriseConnectorFramework — the composition root, wired
                into the existing Scheduler, Event Bus, and Document
                Intelligence pipeline

Connectors shipped in V2.1: folder, excel, csv, postgresql. The rest of the
catalogue (SharePoint, Outlook, Teams, OneDrive, SQL Server, Oracle, REST) is
declared as planned and arrives as one module each.

Not to be confused with ``app/intelligence/connectors``, which holds *format*
connectors — one file in, tabular extracts out. Source connectors use those
for content extraction; they do not replace them.
"""
from app.connectors.base import (
    CAPABILITIES, ConnectionFailed, ConnectionTest, ConnectorConfig,
    ConnectorError, ConnectorHealth, ConnectorNotConfigured,
    ConnectorUnavailable, Discovery, DiscoveredItem, EnterpriseConnector,
    SyncCursor, SyncFailed, SyncOutcome,
)
from app.connectors.csv import CSVConnector
from app.connectors.database import DatabaseConnector
from app.connectors.excel import ExcelConnector
from app.connectors.folder import FolderConnector
from app.connectors.framework import EnterpriseConnectorFramework
from app.connectors.package import PACKAGE_FAMILIES, KnowledgePackage
from app.connectors.postgres import PostgreSQLConnector
from app.connectors.registry import (
    CONNECTOR_PATHS, PLANNED_CONNECTORS, ConnectorNotRegistered,
    ConnectorRegistry, build_registry,
)
from app.connectors.service import EnterpriseSyncService
from app.connectors.store import ConnectorStore
from app.connectors.tabular import TabularRepositoryConnector

__all__ = [
    "CAPABILITIES", "CONNECTOR_PATHS", "CSVConnector", "ConnectionFailed",
    "ConnectionTest", "ConnectorConfig", "ConnectorError", "ConnectorHealth",
    "ConnectorNotConfigured", "ConnectorNotRegistered", "ConnectorRegistry",
    "ConnectorStore", "ConnectorUnavailable", "DatabaseConnector",
    "DiscoveredItem", "Discovery", "EnterpriseConnector",
    "EnterpriseConnectorFramework", "EnterpriseSyncService", "ExcelConnector",
    "FolderConnector", "KnowledgePackage", "PACKAGE_FAMILIES",
    "PLANNED_CONNECTORS", "PostgreSQLConnector", "SyncCursor", "SyncFailed",
    "SyncOutcome", "TabularRepositoryConnector", "build_registry",
]

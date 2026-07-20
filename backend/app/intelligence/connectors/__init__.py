"""Enterprise data-source connectors.

``build_registry`` assembles the default connector catalogue; new sources
(message queues, warehouses, SaaS APIs, ...) are added here without touching
any other layer.
"""
from __future__ import annotations

from app.intelligence.connectors.base import (
    ConnectorNotAvailable, ConnectorRegistry, DataConnector, ExtractedTable, SourceExtract,
)
from app.intelligence.connectors.csv import CSVConnector
from app.intelligence.connectors.excel import ExcelConnector
from app.intelligence.connectors.pdf import PDFConnector
from app.intelligence.connectors.rest_api import APIConnector
from app.intelligence.connectors.sql import SQLConnector
from app.intelligence.connectors.word import WordConnector

__all__ = [
    "ConnectorNotAvailable", "ConnectorRegistry", "DataConnector",
    "ExtractedTable", "SourceExtract", "build_registry",
]


def build_registry(header_scan_rows: int = 15) -> ConnectorRegistry:
    registry = ConnectorRegistry()
    # Descriptor-based connectors first: their extensions are more specific
    # (.sqlsource.json / .apisource.json) than plain suffix matching.
    registry.register(SQLConnector())
    registry.register(APIConnector())
    registry.register(ExcelConnector(header_scan_rows=header_scan_rows))
    registry.register(CSVConnector())
    registry.register(PDFConnector())
    registry.register(WordConnector())
    return registry

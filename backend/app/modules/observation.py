"""Observation Module (SDS §2.1).

Enterprise data acquisition: Excel, CSV, PDF, Word, SQL, REST API — via the
connector registry. Acquisition only; no business decisions are made here.
New enterprise sources are new ``DataConnector`` implementations.
"""
from app.intelligence.connectors import ConnectorRegistry, ExtractedTable, SourceExtract, build_registry
from app.intelligence.connectors.base import DataConnector

__all__ = ["ConnectorRegistry", "DataConnector", "ExtractedTable",
           "SourceExtract", "build_registry"]

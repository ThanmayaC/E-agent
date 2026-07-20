"""Connector abstraction — every enterprise data source enters through here.

A connector turns one source (file, database, API endpoint, ...) into a list
of tabular extracts plus source metadata. Downstream intelligence (profiling,
semantics, KPIs, ...) never knows or cares which connector produced a table:
Excel is just one connector among many, not the core product.

Connectors that need an optional dependency or configuration report
``available = False`` and explain what is missing instead of crashing.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path

import pandas as pd

from app.domain.entities import WorkbookInfo


@dataclass
class ExtractedTable:
    """One tabular dataset extracted from any source."""
    name: str
    source_file: str
    source_sheet: str
    header_row: int
    df: pd.DataFrame
    region: str = ""


@dataclass
class SourceExtract:
    """Everything a connector produced from a single source."""
    info: WorkbookInfo
    tables: list[ExtractedTable] = field(default_factory=list)


class ConnectorNotAvailable(RuntimeError):
    """Raised when a registered connector cannot run in this deployment."""


# --------------------------------------------------------------- utilities
def clean_frame(df: pd.DataFrame) -> pd.DataFrame:
    """Drop empty rows/columns and de-duplicate column names (a, a -> a, a_2)."""
    df = df.dropna(axis=0, how="all").dropna(axis=1, how="all")
    seen: dict[str, int] = {}
    cols = []
    for c in df.columns.astype(str):
        key = c.strip() or "column"
        seen[key] = seen.get(key, 0) + 1
        cols.append(key if seen[key] == 1 else f"{key}_{seen[key]}")
    df.columns = cols
    return df.reset_index(drop=True)


def slug(text: str) -> str:
    import re
    s = re.sub(r"[^0-9a-zA-Z]+", "_", text.strip().lower()).strip("_")
    return s or "table"


class DataConnector(ABC):
    """Base class for all enterprise data-source connectors."""

    name: str = "connector"
    description: str = ""
    extensions: tuple[str, ...] = ()  # file extensions this connector handles

    @property
    def available(self) -> bool:
        """Whether the connector can run here (deps installed, configured)."""
        return True

    @property
    def unavailable_reason(self) -> str:
        return ""

    def can_handle(self, path: Path) -> bool:
        return path.suffix.lower() in self.extensions

    @abstractmethod
    def extract(self, path: Path) -> SourceExtract:
        """Read the source and return tabular extracts. Must not require any
        user-supplied schema."""


class ConnectorRegistry:
    """Registry of every known connector, available or planned.

    The ingestion stage asks the registry which connector handles a file; the
    API layer asks it which extensions may be uploaded.
    """

    def __init__(self) -> None:
        self._connectors: list[DataConnector] = []

    def register(self, connector: DataConnector) -> None:
        self._connectors.append(connector)

    def all(self) -> list[DataConnector]:
        return list(self._connectors)

    def for_file(self, path: Path) -> DataConnector:
        for c in self._connectors:
            if c.can_handle(path):
                if not c.available:
                    raise ConnectorNotAvailable(
                        f"Connector '{c.name}' handles {path.suffix} but is not "
                        f"available: {c.unavailable_reason}")
                return c
        raise ConnectorNotAvailable(f"No connector registered for {path.suffix}")

    def accepts(self, filename: str) -> bool:
        """Whether any available connector can ingest this file name."""
        return any(c.available and c.can_handle(Path(filename)) for c in self._connectors)

    def supported_extensions(self) -> list[str]:
        """Extensions handled by connectors that can actually run here."""
        return sorted({e for c in self._connectors if c.available for e in c.extensions})

    def describe(self) -> list[dict]:
        """Connector catalogue for the API/UI (Knowledge Explorer)."""
        return [{
            "name": c.name,
            "description": c.description,
            "extensions": list(c.extensions),
            "available": c.available,
            "unavailable_reason": c.unavailable_reason,
        } for c in self._connectors]

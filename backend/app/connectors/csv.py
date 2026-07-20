"""CSV Connector — delimited-file repositories, same behaviour as Excel.

A CSV file is a workbook with one sheet and one table, so this connector is
the Excel connector's structure minus the sheet dimension: separator
detection, column schema, inferred types, row count, last modified. No
analytics, for the same reason as Excel — those layers are downstream and
stay there.

Reading is delegated to the Intelligence Engine's CSV format connector, which
already sniffs separators and cleans frames.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from app.connectors.base import ConnectorConfig
from app.connectors.tabular import (
    SCHEMA_SAMPLE_ROWS, TabularRepositoryConnector, schema_of,
)


class CSVConnector(TabularRepositoryConnector):
    """A delimited file, or a repository of them."""

    kind = "csv"
    title = "CSV"
    description = ("CSV/TSV files and repositories: column schema, inferred "
                   "types, row counts, last modified.")
    extensions = (".csv", ".tsv")

    def __init__(self, config: ConnectorConfig):
        super().__init__(config)
        self._reader = None

    def _format_connector(self):
        if self._reader is None:
            from app.intelligence.connectors.csv import (
                CSVConnector as CSVFormatConnector,
            )
            self._reader = CSVFormatConnector()
        return self._reader

    def describe_file(self, path: Path) -> dict[str, Any]:
        extract = self._format_connector().extract(path)
        table = extract.tables[0]
        frame = table.df
        return {
            "file": path.name,
            "delimiter": "\t" if path.suffix.lower() == ".tsv" else "sniffed",
            "sheets": [table.source_sheet],
            "sheet_count": 1,
            "tables_total": 1,
            "tables_by_sheet": {table.source_sheet: [{
                "table": table.name,
                "header_row": table.header_row,
                "rows": int(len(frame)),
                "columns": int(len(frame.columns)),
                "schema": schema_of(frame.head(SCHEMA_SAMPLE_ROWS)),
            }]},
            "rows_total": int(len(frame)),
        }

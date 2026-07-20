"""Excel Connector — workbook understanding, without analytics.

Extracts what a workbook *is*: its sheets, the tables inside each sheet, each
table's column schema and inferred types, its row count, and when the file
last changed. It computes nothing about the numbers — KPIs, quality, and
forecasting are downstream layers that already exist and stay downstream.

Table detection is not re-implemented here. The Intelligence Engine's Excel
format connector already finds data regions inside messy sheets (merged
cells, blank bands, several tables per sheet, hidden sheets), so this
connector calls it and describes what came back. One implementation of "where
does the table start" is enough.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from app.connectors.base import ConnectorConfig
from app.connectors.tabular import (
    SCHEMA_SAMPLE_ROWS, TabularRepositoryConnector, schema_of,
)
from app.core.logging import get_logger

logger = get_logger(__name__)


class ExcelConnector(TabularRepositoryConnector):
    """An Excel workbook, or a repository of workbooks."""

    kind = "excel"
    title = "Excel"
    description = ("Excel workbooks and workbook repositories: sheets, "
                   "detected tables, column schema and types, last modified.")
    extensions = (".xlsx", ".xlsm", ".xls")

    def __init__(self, config: ConnectorConfig):
        super().__init__(config)
        self._reader = None  # the format connector, built lazily

    def _format_connector(self):
        """The Intelligence Engine's Excel reader, which already knows how to
        find tables in a sheet."""
        if self._reader is None:
            from app.intelligence.connectors.excel import (
                ExcelConnector as ExcelFormatConnector,
            )
            self._reader = ExcelFormatConnector(
                header_scan_rows=int(self.config.options.get(
                    "header_scan_rows", 15)))
        return self._reader

    def describe_file(self, path: Path) -> dict[str, Any]:
        """Workbook metadata: sheets, tables, schema, column types."""
        extract = self._format_connector().extract(path)
        info = extract.info

        by_sheet: dict[str, list[dict]] = {}
        for table in extract.tables:
            frame = table.df.head(SCHEMA_SAMPLE_ROWS)
            by_sheet.setdefault(table.source_sheet, []).append({
                "table": table.name,
                "header_row": table.header_row,
                "rows": int(len(table.df)),
                "columns": int(len(table.df.columns)),
                "schema": schema_of(frame),
            })

        # WorkbookInfo reports counts, not names; the sheets that actually
        # yielded tables are the ones the extract knows by name.
        return {
            "workbook": path.name,
            "sheets": list(by_sheet),
            "sheet_count": int(info.sheet_count),
            "hidden_sheets": list(info.hidden_sheets),
            "named_ranges": list(info.named_ranges),
            "merged_regions": int(info.merged_cell_regions),
            "charts": int(info.charts),
            "tables_total": len(extract.tables),
            "tables_by_sheet": by_sheet,
            "rows_total": sum(int(len(t.df)) for t in extract.tables),
        }

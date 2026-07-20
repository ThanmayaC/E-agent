"""Excel connector — automatic workbook understanding.

Discovers workbooks → sheets (incl. hidden) → data regions → headers → tables,
handling merged cells, blank areas, named ranges, and inconsistent layouts.
No schema is ever supplied by the user.

Excel is ONE connector inside the Intelligence Engine, not the core product.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet

from app.core.logging import get_logger
from app.domain.entities import WorkbookInfo
from app.intelligence.connectors.base import (
    DataConnector, ExtractedTable, SourceExtract, clean_frame, slug,
)

logger = get_logger(__name__)

# Backwards-compatible alias: extract types now live in connectors.base and
# are connector-neutral.
WorkbookExtract = SourceExtract
__all__ = ["ExcelConnector", "ExtractedTable", "WorkbookExtract"]


class ExcelConnector(DataConnector):
    """Reads any workbook without a predefined schema."""

    name = "excel"
    description = "Excel workbooks: sheets, hidden sheets, merged cells, multi-table regions"
    extensions = (".xlsx", ".xlsm", ".xls")

    def __init__(self, header_scan_rows: int = 15):
        self.header_scan_rows = header_scan_rows

    # ------------------------------------------------------------- public
    def extract(self, path: Path) -> SourceExtract:
        return self._read_workbook(path)

    # ------------------------------------------------------------ xlsx
    def _read_workbook(self, path: Path) -> SourceExtract:
        wb = load_workbook(path, read_only=False, data_only=True)
        hidden = [ws.title for ws in wb.worksheets if ws.sheet_state != "visible"]
        named_ranges = list(wb.defined_names.keys()) if wb.defined_names else []
        merged_regions = sum(len(ws.merged_cells.ranges) for ws in wb.worksheets)
        charts = sum(len(getattr(ws, "_charts", [])) for ws in wb.worksheets)

        tables: list[ExtractedTable] = []
        for ws in wb.worksheets:
            try:
                tables.extend(self._extract_sheet(ws, path.name))
            except Exception as exc:  # a corrupt sheet must not sink the workbook
                logger.warning("Sheet %s of %s unreadable: %s", ws.title, path.name, exc)

        info = WorkbookInfo(
            file_name=path.name,
            file_size=path.stat().st_size,
            sheet_count=len(wb.worksheets),
            hidden_sheets=hidden,
            named_ranges=named_ranges,
            merged_cell_regions=merged_regions,
            charts=charts,
            tables_found=len(tables),
        )
        wb.close()
        return WorkbookExtract(info=info, tables=tables)

    def _extract_sheet(self, ws: Worksheet, file_name: str) -> list[ExtractedTable]:
        self._unmerge(ws)
        rows = list(ws.iter_rows(values_only=True))
        if not rows:
            return []
        blocks = self._split_blocks(rows)
        tables: list[ExtractedTable] = []
        for idx, (start, block) in enumerate(blocks):
            df, header_row = self._block_to_frame(block)
            if df is None or df.empty or df.shape[1] < 2:
                continue
            suffix = f"_{idx + 1}" if len(blocks) > 1 else ""
            tables.append(ExtractedTable(
                name=slug(f"{Path(file_name).stem}_{ws.title}{suffix}"),
                source_file=file_name,
                source_sheet=ws.title,
                header_row=start + header_row,
                df=df,
                region=f"rows {start + 1}-{start + len(block)}",
            ))
        return tables

    # --------------------------------------------------------- mechanics
    @staticmethod
    def _unmerge(ws: Worksheet) -> None:
        """Fill merged regions with the top-left value so no data is lost."""
        for rng in list(ws.merged_cells.ranges):
            value = ws.cell(rng.min_row, rng.min_col).value
            ws.unmerge_cells(str(rng))
            for row in ws.iter_rows(rng.min_row, rng.max_row, rng.min_col, rng.max_col):
                for cell in row:
                    cell.value = value

    @staticmethod
    def _split_blocks(rows: list[tuple]) -> list[tuple[int, list[tuple]]]:
        """Split sheet rows into contiguous data blocks separated by >=2 blank rows."""
        blocks, current, start, blanks = [], [], 0, 0
        for i, row in enumerate(rows):
            empty = all(v is None or (isinstance(v, str) and not v.strip()) for v in row)
            if empty:
                blanks += 1
                if blanks >= 2 and current:
                    blocks.append((start, current))
                    current = []
                continue
            if not current:
                start = i
            blanks = 0
            current.append(row)
        if current:
            blocks.append((start, current))
        return blocks

    def _block_to_frame(self, block: list[tuple]) -> tuple[pd.DataFrame | None, int]:
        header_idx = self._find_header(block)
        if header_idx is None:
            return None, 0
        header = [self._header_name(v, j) for j, v in enumerate(block[header_idx])]
        body = block[header_idx + 1:]
        if not body:
            return None, header_idx
        df = pd.DataFrame(body, columns=header)
        df = clean_frame(df)
        return df, header_idx

    def _find_header(self, block: list[tuple]) -> int | None:
        """Header = the first row within the scan window that is mostly text and
        is followed by rows whose types differ (data)."""
        best, best_score = None, 0.0
        limit = min(self.header_scan_rows, len(block) - 1)
        for i in range(max(limit, 1)):
            row = block[i]
            cells = [v for v in row if v is not None]
            if not cells:
                continue
            text_ratio = sum(isinstance(v, str) for v in cells) / len(cells)
            fill_ratio = len(cells) / len(row)
            uniq_ratio = len({str(v).strip().lower() for v in cells}) / len(cells)
            score = text_ratio * 0.5 + fill_ratio * 0.3 + uniq_ratio * 0.2
            if score > best_score and text_ratio >= 0.5:
                best, best_score = i, score
        return best if best is not None else (0 if len(block) > 1 else None)

    @staticmethod
    def _header_name(value, position: int) -> str:
        if value is None or (isinstance(value, str) and not value.strip()):
            return f"column_{position + 1}"
        return str(value).strip()



"""PDF connector — extracts tables from PDF reports.

Requires the optional dependency ``pdfplumber``; when it is not installed the
connector registers as unavailable and explains what to install.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from app.domain.entities import WorkbookInfo
from app.intelligence.connectors.base import (
    DataConnector, ExtractedTable, SourceExtract, clean_frame, slug,
)

try:
    import pdfplumber  # type: ignore
    _PDF_OK = True
except ImportError:
    _PDF_OK = False


class PDFConnector(DataConnector):
    name = "pdf"
    description = "PDF documents: table extraction from report pages"
    extensions = (".pdf",)

    @property
    def available(self) -> bool:
        return _PDF_OK

    @property
    def unavailable_reason(self) -> str:
        return "" if _PDF_OK else "install optional dependency: pip install pdfplumber"

    def extract(self, path: Path) -> SourceExtract:
        tables: list[ExtractedTable] = []
        with pdfplumber.open(path) as pdf:
            page_count = len(pdf.pages)
            for page_no, page in enumerate(pdf.pages, start=1):
                for idx, rows in enumerate(page.extract_tables() or []):
                    df = self._rows_to_frame(rows)
                    if df is None:
                        continue
                    tables.append(ExtractedTable(
                        name=slug(f"{path.stem}_p{page_no}_{idx + 1}"),
                        source_file=path.name,
                        source_sheet=f"page {page_no}",
                        header_row=0, df=df,
                        region=f"page {page_no} table {idx + 1}",
                    ))
        info = WorkbookInfo(file_name=path.name, file_size=path.stat().st_size,
                            sheet_count=page_count, tables_found=len(tables))
        return SourceExtract(info=info, tables=tables)

    @staticmethod
    def _rows_to_frame(rows: list[list]) -> pd.DataFrame | None:
        if not rows or len(rows) < 2:
            return None
        header = [str(h or f"column_{i + 1}").strip() for i, h in enumerate(rows[0])]
        df = clean_frame(pd.DataFrame(rows[1:], columns=header))
        return None if df.empty or df.shape[1] < 2 else df

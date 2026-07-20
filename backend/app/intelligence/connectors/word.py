"""Word connector — extracts tables from .docx documents.

Requires the optional dependency ``python-docx``; when it is not installed
the connector registers as unavailable and explains what to install.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from app.domain.entities import WorkbookInfo
from app.intelligence.connectors.base import (
    DataConnector, ExtractedTable, SourceExtract, clean_frame, slug,
)

try:
    import docx  # type: ignore
    _DOCX_OK = True
except ImportError:
    _DOCX_OK = False


class WordConnector(DataConnector):
    name = "word"
    description = "Word documents (.docx): embedded table extraction"
    extensions = (".docx",)

    @property
    def available(self) -> bool:
        return _DOCX_OK

    @property
    def unavailable_reason(self) -> str:
        return "" if _DOCX_OK else "install optional dependency: pip install python-docx"

    def extract(self, path: Path) -> SourceExtract:
        document = docx.Document(str(path))
        tables: list[ExtractedTable] = []
        for idx, tbl in enumerate(document.tables, start=1):
            rows = [[cell.text.strip() for cell in row.cells] for row in tbl.rows]
            if len(rows) < 2:
                continue
            df = clean_frame(pd.DataFrame(rows[1:], columns=rows[0]))
            if df.empty or df.shape[1] < 2:
                continue
            tables.append(ExtractedTable(
                name=slug(f"{path.stem}_table_{idx}"),
                source_file=path.name, source_sheet=f"table {idx}",
                header_row=0, df=df,
            ))
        info = WorkbookInfo(file_name=path.name, file_size=path.stat().st_size,
                            sheet_count=1, tables_found=len(tables))
        return SourceExtract(info=info, tables=tables)

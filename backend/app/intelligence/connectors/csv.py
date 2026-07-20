"""CSV / TSV connector."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from app.domain.entities import WorkbookInfo
from app.intelligence.connectors.base import (
    DataConnector, ExtractedTable, SourceExtract, clean_frame, slug,
)


class CSVConnector(DataConnector):
    name = "csv"
    description = "Delimited text files (.csv/.tsv) with automatic separator detection"
    extensions = (".csv", ".tsv")

    def extract(self, path: Path) -> SourceExtract:
        sep = "\t" if path.suffix.lower() == ".tsv" else None  # None => sniff
        df = pd.read_csv(path, sep=sep, engine="python")
        df = clean_frame(df)
        info = WorkbookInfo(
            file_name=path.name, file_size=path.stat().st_size,
            sheet_count=1, tables_found=1,
        )
        table = ExtractedTable(
            name=slug(path.stem), source_file=path.name,
            source_sheet="csv", header_row=0, df=df,
        )
        return SourceExtract(info=info, tables=[table])

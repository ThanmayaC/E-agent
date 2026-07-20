"""SQL connector — reads tables from any SQLAlchemy-supported database.

Sources are described by a ``*.sqlsource.json`` descriptor uploaded to the
project (never credentials hardcoded in code):

    {"url": "postgresql://user:pass@host/db", "tables": ["orders", "customers"]}

If ``tables`` is omitted, every table visible to the connection is read.
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from app.domain.entities import WorkbookInfo
from app.intelligence.connectors.base import (
    DataConnector, ExtractedTable, SourceExtract, clean_frame, slug,
)


class SQLConnector(DataConnector):
    name = "sql"
    description = "SQL databases via a .sqlsource.json descriptor (SQLAlchemy URL + tables)"
    extensions = (".sqlsource.json",)

    def __init__(self, max_rows: int = 200_000):
        self.max_rows = max_rows

    def can_handle(self, path: Path) -> bool:
        return path.name.lower().endswith(self.extensions)

    def extract(self, path: Path) -> SourceExtract:
        from sqlalchemy import create_engine, inspect, text

        spec = json.loads(path.read_text(encoding="utf-8"))
        engine = create_engine(spec["url"])
        tables: list[ExtractedTable] = []
        with engine.connect() as conn:
            names = spec.get("tables") or inspect(engine).get_table_names()
            for table_name in names:
                df = pd.read_sql(
                    text(f'SELECT * FROM "{table_name}" LIMIT {self.max_rows}'), conn)  # noqa: S608
                df = clean_frame(df)
                if df.empty:
                    continue
                tables.append(ExtractedTable(
                    name=slug(table_name), source_file=path.name,
                    source_sheet=table_name, header_row=0, df=df,
                ))
        info = WorkbookInfo(file_name=path.name, file_size=path.stat().st_size,
                            sheet_count=len(tables), tables_found=len(tables))
        return SourceExtract(info=info, tables=tables)

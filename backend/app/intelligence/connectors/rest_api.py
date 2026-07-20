"""REST API connector — pulls tabular records from JSON endpoints.

Sources are described by a ``*.apisource.json`` descriptor uploaded to the
project:

    {"url": "https://api.example.com/v1/orders",
     "headers": {"Authorization": "Bearer ..."},
     "records_path": "data.items",       # optional dotted path to the list
     "name": "orders"}                   # optional dataset name
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import httpx
import pandas as pd

from app.domain.entities import WorkbookInfo
from app.intelligence.connectors.base import (
    DataConnector, ExtractedTable, SourceExtract, clean_frame, slug,
)


class APIConnector(DataConnector):
    name = "api"
    description = "REST APIs via an .apisource.json descriptor (JSON records to table)"
    extensions = (".apisource.json",)

    def __init__(self, timeout_s: float = 60.0):
        self.timeout_s = timeout_s

    def can_handle(self, path: Path) -> bool:
        return path.name.lower().endswith(self.extensions)

    def extract(self, path: Path) -> SourceExtract:
        spec = json.loads(path.read_text(encoding="utf-8"))
        response = httpx.get(spec["url"], headers=spec.get("headers") or {},
                             timeout=self.timeout_s)
        response.raise_for_status()
        records = self._dig(response.json(), spec.get("records_path", ""))
        if isinstance(records, dict):
            records = [records]
        if not isinstance(records, list):
            raise ValueError(f"API response is not a record list ({type(records).__name__})")
        df = clean_frame(pd.json_normalize(records))
        table = ExtractedTable(
            name=slug(spec.get("name") or path.stem), source_file=path.name,
            source_sheet=spec["url"], header_row=0, df=df,
        )
        info = WorkbookInfo(file_name=path.name, file_size=path.stat().st_size,
                            sheet_count=1, tables_found=1)
        return SourceExtract(info=info, tables=[table])

    @staticmethod
    def _dig(payload: Any, dotted: str) -> Any:
        for key in [k for k in dotted.split(".") if k]:
            payload = payload[key]
        return payload

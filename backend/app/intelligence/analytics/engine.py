"""Analytics engine on DuckDB.

Every merged dataset is registered as a DuckDB table (per project) so the
copilot and dashboard can run aggregations, group-bys, and time rollups.
"""
from __future__ import annotations

from pathlib import Path

import duckdb
import pandas as pd

from app.core.logging import get_logger
from app.domain.entities import TableProfile
from app.domain.enums import ColumnRole

logger = get_logger(__name__)


class AnalyticsEngine:
    def __init__(self, db_path: Path):
        self.db_path = db_path

    # ------------------------------------------------------------ loading
    def load(self, frames: dict[str, pd.DataFrame]) -> None:
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        con = duckdb.connect(str(self.db_path))
        try:
            for dataset_id, df in frames.items():
                con.register("df_tmp", df)
                con.execute(f'CREATE OR REPLACE TABLE "{dataset_id}" AS SELECT * FROM df_tmp')
                con.unregister("df_tmp")
        finally:
            con.close()

    # ------------------------------------------------------------ queries
    def query(self, sql: str, limit: int = 1000) -> dict:
        con = duckdb.connect(str(self.db_path), read_only=True)
        try:
            df = con.execute(sql).fetchdf().head(limit)
            return {"columns": list(df.columns), "rows": df.astype(object).where(df.notna(), None).values.tolist()}
        finally:
            con.close()

    def preview(self, dataset_id: str, limit: int = 50) -> dict:
        return self.query(f'SELECT * FROM "{dataset_id}" LIMIT {int(limit)}')

    def aggregate_by_dimension(self, profile: TableProfile, measure: str, dimension: str, top: int = 10) -> dict:
        sql = (
            f'SELECT "{dimension}" AS dim, SUM(TRY_CAST("{measure}" AS DOUBLE)) AS total '
            f'FROM "{profile.dataset_id}" WHERE "{dimension}" IS NOT NULL '
            f'GROUP BY 1 ORDER BY 2 DESC NULLS LAST LIMIT {int(top)}'
        )
        return self.query(sql)

    def time_rollup(self, profile: TableProfile, measure: str, grain: str = "month") -> dict:
        trunc = {"day": "day", "week": "week", "month": "month", "quarter": "quarter", "year": "year"}.get(grain, "month")
        sql = (
            f'SELECT date_trunc(\'{trunc}\', TRY_CAST("{profile.time_column}" AS TIMESTAMP)) AS period, '
            f'SUM(TRY_CAST("{measure}" AS DOUBLE)) AS total '
            f'FROM "{profile.dataset_id}" WHERE "{profile.time_column}" IS NOT NULL '
            f'GROUP BY 1 ORDER BY 1'
        )
        return self.query(sql)

    # ------------------------------------------- dashboard-ready breakdowns
    def dimension_breakdowns(self, profiles: list[TableProfile], max_charts: int = 8) -> list[dict]:
        charts: list[dict] = []
        for p in profiles:
            measures = [c for c in p.columns if c.role == ColumnRole.MEASURE]
            dims = [c for c in p.columns if c.role == ColumnRole.DIMENSION and 1 < c.distinct_count <= 50]
            for m in measures[:2]:
                for d in dims[:2]:
                    if len(charts) >= max_charts:
                        return charts
                    try:
                        data = self.aggregate_by_dimension(p, m.name, d.name)
                        if data["rows"]:
                            charts.append({
                                "dataset": p.name, "measure": m.name, "dimension": d.name,
                                "title": f"{m.name} by {d.name}", **data,
                            })
                    except Exception as exc:
                        logger.debug("breakdown failed: %s", exc)
        return charts

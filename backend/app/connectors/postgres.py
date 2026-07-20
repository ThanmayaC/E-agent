"""PostgreSQL Connector.

Everything a relational source needs is in ``DatabaseConnector``; PostgreSQL
adds only what is genuinely PostgreSQL: which URL schemes are valid, and a
row estimate read from ``pg_class.reltuples`` — the planner's own statistic,
which is free, rather than ``COUNT(*)``, which is not.

This is the shape every future database connector takes: a subclass with a
title, a URL check, and at most one engine-specific optimization. SQL Server
and Oracle land the same way, which is why V2.1 builds the base and one
implementation rather than four implementations.
"""
from __future__ import annotations

from app.connectors.database import DatabaseConnector
from app.core.logging import get_logger

logger = get_logger(__name__)


class PostgreSQLConnector(DatabaseConnector):
    """PostgreSQL: schema discovery, table metadata, incremental sync."""

    kind = "postgresql"
    title = "PostgreSQL"
    description = ("PostgreSQL: schema and table discovery, column types, "
                   "keys and indexes, watermark-based incremental sync.")
    url_prefixes = ("postgresql://", "postgresql+", "postgres://")

    def _row_estimate(self, schema: str | None, name: str) -> int:
        """The planner's estimate — accurate enough to notice a table growing,
        and cheap enough to read on every heartbeat.

        ``count_rows`` still forces an exact ``COUNT(*)`` for deployments that
        want it; the estimate is the default because a metadata sync should
        never table-scan.
        """
        if self.config.options.get("count_rows", False):
            return super()._row_estimate(schema, name)
        from sqlalchemy import text
        try:
            with self._engine.connect() as connection:
                estimate = connection.execute(text(
                    "SELECT c.reltuples::bigint FROM pg_class c "
                    "JOIN pg_namespace n ON n.oid = c.relnamespace "
                    "WHERE c.relname = :table AND n.nspname = :schema"
                ), {"table": name, "schema": schema or "public"}).scalar()
        except Exception:  # noqa: BLE001 — an estimate never fails a sync
            return -1
        # -1 from the planner means "never analyzed", which is the same
        # honest unknown the base class reports.
        return int(estimate) if estimate is not None and estimate >= 0 else -1

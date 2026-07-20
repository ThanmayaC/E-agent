"""Database Connector — the generic relational source.

One implementation covers every relational engine, because SQLAlchemy already
abstracts the differences and the platform already depends on it. PostgreSQL,
SQL Server, MySQL, and Oracle differ in their driver, which is part of the
connection URL the administrator supplies — so a new engine is a subclass
that changes a title and a URL prefix check, not a new connector.

What it extracts is the **schema**, not the data: schemas, tables, views,
columns, types, nullability, primary and foreign keys, indexes, and row
estimates. No profiling, no aggregation, no analytics — the intelligence
layers downstream already do that, on their own terms, from their own reads.

Incremental synchronization has two modes, chosen per table:

    watermark    a monotonic column (``updated_at``, ``id``) named in the
                 source's options. Only rows past the last high-water mark
                 are read. This is the mode that makes a large table
                 affordable on an hourly cadence.
    structural   no watermark: the table's *shape* is fingerprinted (columns,
                 types, keys, row estimate) and re-packaged only when it
                 moves. Metadata-only, which is exactly what V2.1 asks for.

Credentials are never stored: the connection URL is resolved from the
configured environment reference at connect time, held in memory, and never
logged, persisted, or returned by any API.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any

from app.connectors.base import (
    ConnectionFailed, ConnectorConfig, ConnectorHealth, ConnectorNotConfigured,
    ConnectorUnavailable, Discovery, DiscoveredItem, EnterpriseConnector,
    SyncCursor, SyncFailed, SyncOutcome, now_iso,
)
from app.connectors.package import KnowledgePackage
from app.core.logging import get_logger

logger = get_logger(__name__)

MAX_TABLES_PER_SYNC = 500
MAX_DISCOVERY_ITEMS = 500
# Rows read per table when a watermark is configured. Synchronization is a
# heartbeat job, not a bulk loader: a busy table catches up over several runs
# rather than blocking the scheduler for one.
MAX_ROWS_PER_TABLE = 5_000


class DatabaseConnector(EnterpriseConnector):
    """Any relational database reachable through SQLAlchemy."""

    kind = "database"
    title = "Database"
    description = ("A relational database: schema discovery, table and column "
                   "metadata, keys, and incremental synchronization.")
    capabilities = ("discover", "incremental", "deletions", "test_connection")
    produces = "tabular"
    # Subclasses restrict which URLs they accept; empty means "any".
    url_prefixes: tuple[str, ...] = ()

    def __init__(self, config: ConnectorConfig):
        super().__init__(config)
        self._engine = None
        self._inspector = None

    # ----------------------------------------------------------- lifecycle
    def initialize(self) -> None:
        super().initialize()
        if self.config.auth_kind != "env" or not self.config.auth_ref:
            raise ConnectorNotConfigured(
                f"{self.title} connector '{self.name}' needs its connection URL "
                f"by reference: auth {{'kind': 'env', 'ref': 'VAR_NAME'}} — the "
                f"platform never stores credentials")

    def connect(self) -> None:
        if self._engine is not None:
            self._connected = True
            return
        url = self.config.require_secret()
        if self.url_prefixes and not url.startswith(self.url_prefixes):
            raise ConnectorNotConfigured(
                f"'{self.config.auth_ref}' does not look like a {self.title} "
                f"URL (expected one of: {', '.join(self.url_prefixes)})")
        try:
            from sqlalchemy import create_engine, inspect
        except ImportError as exc:  # pragma: no cover — SQLAlchemy is a core dep
            raise ConnectorUnavailable(f"SQLAlchemy is not installed: {exc}")
        try:
            self._engine = create_engine(url, future=True, pool_pre_ping=True)
            with self._engine.connect():
                pass  # prove the credentials work now, not at first read
            self._inspector = inspect(self._engine)
        except Exception as exc:  # noqa: BLE001 — driver errors are readable text
            self._engine = None
            raise ConnectionFailed(_safe(exc, self.config.auth_ref))
        self._connected = True

    def disconnect(self) -> None:
        engine, self._engine, self._inspector = self._engine, None, None
        self._connected = False
        if engine is not None:
            try:
                engine.dispose()
            except Exception:  # noqa: BLE001 — teardown never raises
                logger.warning("Disposing the engine for %s failed", self.name)

    def _probe(self) -> str:
        tables = self._table_names()
        return (f"connected: {len(tables)} table(s) visible in "
                f"{', '.join(self._schemas()) or 'the default schema'}")

    def health(self) -> ConnectorHealth:
        if self.config.resolved_secret() is None:
            return ConnectorHealth(
                state="unconfigured",
                detail=f"auth reference '{self.config.auth_ref}' is not set here")
        import time
        started = time.monotonic()
        try:
            self.connect()
            from sqlalchemy import text
            with self._engine.connect() as connection:
                connection.execute(text("SELECT 1"))
        except Exception as exc:  # noqa: BLE001 — health reports, never raises
            return ConnectorHealth(state="unreachable",
                                   detail=_safe(exc, self.config.auth_ref))
        return ConnectorHealth(
            state="healthy", detail="connection verified",
            latency_ms=int((time.monotonic() - started) * 1000))

    # ----------------------------------------------------------- discovery
    def discover(self) -> Discovery:
        """Schemas, tables, and views — names and sizes only, no column
        reflection, so discovery stays fast on a wide database."""
        self.connect()
        items: list[DiscoveredItem] = []
        truncated = False
        for schema, name, item_type in self._table_names():
            if len(items) >= MAX_DISCOVERY_ITEMS:
                truncated = True
                break
            items.append(DiscoveredItem(
                item_id=f"{schema}.{name}", name=name, item_type=item_type,
                metadata={"schema": schema}))
        return Discovery(connector_id=self.connector_id, items=items,
                         truncated=truncated,
                         detail=f"{len(items)} table(s) and view(s)")

    def fetch_metadata(self, item_id: str) -> dict[str, Any]:
        """Full metadata for one table: columns, types, keys, indexes."""
        self.connect()
        schema, _, name = item_id.rpartition(".")
        return self._describe_table(schema or None, name)

    # ---------------------------------------------------------------- sync
    def sync(self, cursor: SyncCursor | None = None) -> SyncOutcome:
        return self._read(SyncCursor(), "full", cursor.version if cursor else 0)

    def incremental_sync(self, cursor: SyncCursor) -> SyncOutcome:
        return self._read(cursor, "incremental", cursor.version)

    def _read(self, cursor: SyncCursor, mode: str,
              previous_version: int) -> SyncOutcome:
        self.connect()
        previous = dict(cursor.fingerprints)
        watermarks = dict(cursor.extra.get("watermarks") or {})
        current: dict[str, str] = {}
        packages: list[KnowledgePackage] = []
        warnings: list[str] = []
        unchanged, truncated = 0, False

        for index, (schema, name, item_type) in enumerate(self._table_names()):
            if index >= MAX_TABLES_PER_SYNC:
                truncated = True
                warnings.append(
                    f"database holds more than {MAX_TABLES_PER_SYNC} tables — "
                    f"synchronized the first {MAX_TABLES_PER_SYNC}")
                break
            item_id = f"{schema}.{name}" if schema else name
            try:
                metadata = self._describe_table(schema, name)
            except Exception as exc:  # noqa: BLE001 — one table, not the database
                warnings.append(f"{item_id}: {type(exc).__name__}: {exc}"[:200])
                continue
            metadata["object_type"] = item_type

            # A configured watermark is used in both modes: a full sync
            # establishes the mark (reading from the beginning), and later
            # incremental syncs advance it. Skipping it on the full sync would
            # make the first incremental re-read the whole table.
            watermark_column = self._watermark_column(item_id, metadata)
            rows: list[dict] = []
            if watermark_column:
                since = watermarks.get(item_id, "") if mode == "incremental" else ""
                try:
                    rows, high = self._read_rows(schema, name,
                                                 watermark_column, since)
                except Exception as exc:  # noqa: BLE001
                    warnings.append(f"{item_id}: {exc}"[:200])
                else:
                    if high:
                        watermarks[item_id] = high
                    metadata["watermark_column"] = watermark_column
                    metadata["watermark"] = watermarks.get(item_id, "")

            fingerprint = _structure_hash(metadata, watermarks.get(item_id, ""))
            current[item_id] = fingerprint
            if previous.get(item_id) == fingerprint and not rows:
                unchanged += 1
                continue

            packages.append(KnowledgePackage(
                **self.package_defaults(), item_id=item_id,
                location=f"{self.config.location or self.title}/{item_id}",
                family="table", file_type="table", title=item_id,
                modified_date=watermarks.get(item_id, "") or now_iso(),
                checksum=fingerprint, version=previous_version + 1,
                structured_metadata=metadata, records=rows,
                permissions={"scope": self.config.options.get(
                    "scope", "organization")}))

        _, removed = self._diff_fingerprints(previous, current)
        if truncated:
            removed = []

        return SyncOutcome(
            connector_id=self.connector_id, mode=mode, packages=packages,
            removed=removed, unchanged=unchanged, truncated=truncated,
            warnings=warnings,
            cursor=SyncCursor(version=previous_version + 1,
                              fingerprints=current, last_synced_at=now_iso(),
                              extra={"watermarks": watermarks}))

    # ------------------------------------------------------------ internals
    def _schemas(self) -> list[str]:
        """Schemas to synchronize: the configured list, or everything the
        connection can see minus the engine's own system schemas."""
        configured = self.config.options.get("schemas")
        if configured:
            return [str(s) for s in configured]
        try:
            names = self._inspector.get_schema_names()
        except Exception:  # noqa: BLE001 — engines that have no schema concept
            return []
        return [n for n in names if not self._is_system_schema(n)]

    @staticmethod
    def _is_system_schema(name: str) -> bool:
        lowered = name.lower()
        return (lowered.startswith("pg_") or lowered.startswith("sys")
                or lowered in ("information_schema", "performance_schema"))

    def _table_names(self) -> list[tuple[str, str, str]]:
        """(schema, name, object_type) for every table and view in scope."""
        wanted = self.config.options.get("tables")
        wanted = {str(t) for t in wanted} if wanted else None
        out: list[tuple[str, str, str]] = []
        for schema in self._schemas() or [None]:
            try:
                tables = self._inspector.get_table_names(schema=schema)
                views = (self._inspector.get_view_names(schema=schema)
                         if self.config.options.get("include_views", True)
                         else [])
            except Exception as exc:  # noqa: BLE001 — one schema, not the sync
                logger.warning("Listing %s in %s failed: %s", schema,
                               self.name, exc)
                continue
            for name in sorted(tables):
                out.append((schema or "", name, "table"))
            for name in sorted(views):
                out.append((schema or "", name, "view"))
        if wanted is not None:
            out = [t for t in out
                   if t[1] in wanted or f"{t[0]}.{t[1]}" in wanted]
        return out

    def _describe_table(self, schema: str | None, name: str) -> dict[str, Any]:
        """Column schema, keys, and indexes for one table — metadata only."""
        schema = schema or None
        columns = [{
            "name": c["name"],
            "type": str(c.get("type", "")),
            "nullable": bool(c.get("nullable", True)),
            "default": None if c.get("default") is None else str(c["default"]),
            "autoincrement": bool(c.get("autoincrement", False)),
        } for c in self._inspector.get_columns(name, schema=schema)]

        try:
            primary_key = list(self._inspector.get_pk_constraint(
                name, schema=schema).get("constrained_columns") or [])
        except Exception:  # noqa: BLE001 — not every engine/view has one
            primary_key = []
        try:
            foreign_keys = [{
                "columns": list(fk.get("constrained_columns") or []),
                "references_table": fk.get("referred_table", ""),
                "references_schema": fk.get("referred_schema", "") or "",
                "references_columns": list(fk.get("referred_columns") or []),
            } for fk in self._inspector.get_foreign_keys(name, schema=schema)]
        except Exception:  # noqa: BLE001
            foreign_keys = []
        try:
            indexes = [{"name": i.get("name", ""),
                        "columns": list(i.get("column_names") or []),
                        "unique": bool(i.get("unique"))}
                       for i in self._inspector.get_indexes(name, schema=schema)]
        except Exception:  # noqa: BLE001
            indexes = []

        return {"schema": schema or "", "table": name,
                "columns": columns, "column_count": len(columns),
                "primary_key": primary_key, "foreign_keys": foreign_keys,
                "indexes": indexes,
                "row_estimate": self._row_estimate(schema, name)}

    def _row_estimate(self, schema: str | None, name: str) -> int:
        """Approximate size. ``-1`` when the engine will not say cheaply — an
        honest unknown beats a full table scan on every heartbeat."""
        if not self.config.options.get("count_rows", False):
            return -1
        from sqlalchemy import text
        qualified = f'"{schema}"."{name}"' if schema else f'"{name}"'
        try:
            with self._engine.connect() as connection:
                return int(connection.execute(
                    text(f"SELECT COUNT(*) FROM {qualified}")).scalar() or 0)
        except Exception:  # noqa: BLE001 — a count is never worth failing a sync
            return -1

    def _watermark_column(self, item_id: str, metadata: dict) -> str:
        """The configured incremental column for this table, if it exists.

        ``options.watermarks`` maps table → column; ``options.watermark_column``
        sets one default for every table. A column that is not actually in the
        table is ignored rather than raising — schemas drift.
        """
        options = self.config.options
        configured = (options.get("watermarks") or {}).get(item_id) \
            or (options.get("watermarks") or {}).get(metadata["table"]) \
            or options.get("watermark_column", "")
        if not configured:
            return ""
        names = {c["name"] for c in metadata["columns"]}
        if configured not in names:
            logger.debug("Watermark column %s is not in %s", configured, item_id)
            return ""
        return str(configured)

    def _read_rows(self, schema: str | None, name: str, column: str,
                   since: str) -> tuple[list[dict], str]:
        """Rows past the high-water mark, plus the new mark.

        Identifiers are quoted, not interpolated raw, and the bound is a
        parameter — a table name from configuration still never becomes a
        query fragment an operator did not intend.
        """
        from sqlalchemy import text
        qualified = f'"{schema}"."{name}"' if schema else f'"{name}"'
        quoted = f'"{column}"'
        sql = f"SELECT * FROM {qualified}"
        params: dict[str, Any] = {}
        if since:
            sql += f" WHERE {quoted} > :since"
            params["since"] = since
        sql += f" ORDER BY {quoted} ASC LIMIT :row_limit"
        params["row_limit"] = MAX_ROWS_PER_TABLE
        try:
            with self._engine.connect() as connection:
                result = connection.execute(text(sql), params)
                rows = [dict(row) for row in result.mappings()]
        except Exception as exc:  # noqa: BLE001
            raise SyncFailed(f"reading {name} failed: {exc}"[:250])
        high = str(rows[-1].get(column, "")) if rows else since
        return json.loads(json.dumps(rows, default=str)), high


def _structure_hash(metadata: dict, watermark: str) -> str:
    """Fingerprint of a table's shape and position — what "changed" means for
    a metadata-only sync.

    Deliberately excludes how many rows *this run* happened to read: that is a
    property of the run, not of the table, and including it would make a
    caught-up table look changed forever.
    """
    payload = json.dumps({"columns": metadata.get("columns"),
                          "primary_key": metadata.get("primary_key"),
                          "foreign_keys": metadata.get("foreign_keys"),
                          "row_estimate": metadata.get("row_estimate"),
                          "watermark": watermark},
                         sort_keys=True, default=str)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _safe(exc: Exception, auth_ref: str) -> str:
    """A driver error without the credential in it. SQLAlchemy puts the URL
    in some messages, and this text reaches the Admin console and the logs."""
    import os
    message = f"{type(exc).__name__}: {exc}"
    secret = os.environ.get(auth_ref) if auth_ref else None
    if secret:
        message = message.replace(secret, f"${auth_ref}")
    return message[:300]

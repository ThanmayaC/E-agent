"""Shared base for file-repository connectors (Excel, CSV).

An Excel repository and a CSV repository differ in exactly one thing: how a
single file is described. Everything else — walking the repository, hashing
for change detection, versioning, packaging, deletion detection — is
identical, so it lives here once.

These connectors extract **structure, not meaning**: sheet names, detected
tables, column names, inferred column types, row counts, last-modified. No
profiling, no KPIs, no analytics — those layers already exist downstream and
run on their own terms. A connector that started computing statistics would
be a second analytics engine, which is precisely what the framework exists to
avoid.
"""
from __future__ import annotations

import hashlib
from abc import abstractmethod
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from app.connectors.base import (
    ConnectionFailed, ConnectorConfig, ConnectorHealth, ConnectorNotConfigured,
    Discovery, DiscoveredItem, EnterpriseConnector, SyncCursor, SyncOutcome,
    now_iso,
)
from app.connectors.package import KnowledgePackage
from app.core.logging import get_logger

logger = get_logger(__name__)

MAX_FILES_PER_SYNC = 500
MAX_DISCOVERY_ITEMS = 200
HASH_CHUNK_BYTES = 1 << 20
# Rows read to infer a schema. Type inference does not get better with more
# rows; it gets slower.
SCHEMA_SAMPLE_ROWS = 200


def file_checksum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(HASH_CHUNK_BYTES):
            digest.update(chunk)
    return digest.hexdigest()


def column_type(series: pd.Series) -> str:
    """A column's type in business vocabulary, not dtype vocabulary."""
    if pd.api.types.is_bool_dtype(series):
        return "boolean"
    if pd.api.types.is_integer_dtype(series):
        return "integer"
    if pd.api.types.is_float_dtype(series):
        return "decimal"
    if pd.api.types.is_datetime64_any_dtype(series):
        return "datetime"
    non_null = series.dropna()
    if non_null.empty:
        return "unknown"
    if pd.api.types.is_object_dtype(series):
        parsed = pd.to_numeric(non_null, errors="coerce")
        if parsed.notna().all():
            return "integer" if (parsed % 1 == 0).all() else "decimal"
    return "text"


def schema_of(frame: pd.DataFrame) -> list[dict[str, Any]]:
    """Column schema: name, type, nullability, distinct count. Structure
    only — no distributions, no outliers, no correlations."""
    return [{
        "name": str(column),
        "type": column_type(frame[column]),
        "nullable": bool(frame[column].isna().any()),
        "non_null": int(frame[column].notna().sum()),
        "distinct": int(frame[column].nunique(dropna=True)),
    } for column in frame.columns]


class TabularRepositoryConnector(EnterpriseConnector):
    """A file or a directory of files of one tabular format."""

    kind = "tabular"
    produces = "tabular"
    capabilities = ("discover", "incremental", "content", "deletions",
                    "test_connection")
    # Extensions this connector owns. Subclasses must set this.
    extensions: tuple[str, ...] = ()

    def __init__(self, config: ConnectorConfig):
        super().__init__(config)
        self._root: Path | None = None

    # ----------------------------------------------------------- lifecycle
    def initialize(self) -> None:
        super().initialize()
        if not self.config.location:
            raise ConnectorNotConfigured(
                f"{self.title} connector '{self.name}' needs a location "
                f"(a file or a folder of files)")
        self._root = Path(self.config.location).expanduser()

    def connect(self) -> None:
        root = self._require_root()
        if not root.exists():
            raise ConnectionFailed(f"path does not exist: {root}")
        self._connected = True

    def _probe(self) -> str:
        files = list(self._files(limit=MAX_DISCOVERY_ITEMS))
        if not files:
            raise ConnectionFailed(
                f"no {self.title} files found at {self._root}")
        return f"{len(files)} {self.title} file(s) readable at {self._root}"

    def health(self) -> ConnectorHealth:
        try:
            root = self._require_root()
        except ConnectorNotConfigured as exc:
            return ConnectorHealth(state="unconfigured", detail=str(exc))
        if not root.exists():
            return ConnectorHealth(state="unreachable",
                                   detail=f"path does not exist: {root}")
        return ConnectorHealth(state="healthy", detail=f"reading {root}")

    # ----------------------------------------------------------- discovery
    def discover(self) -> Discovery:
        self.connect()
        items: list[DiscoveredItem] = []
        truncated = False
        for path in self._files(limit=MAX_DISCOVERY_ITEMS + 1):
            if len(items) >= MAX_DISCOVERY_ITEMS:
                truncated = True
                break
            try:
                stat = path.stat()
                summary = self.describe_file(path)
            except Exception as exc:  # noqa: BLE001 — one bad file, not the repo
                logger.warning("Discovery skipped %s: %s", path.name, exc)
                continue
            items.append(DiscoveredItem(
                item_id=self._item_id(path), name=path.name, item_type="file",
                size=stat.st_size, modified_at=_iso(stat.st_mtime),
                metadata=summary))
        return Discovery(connector_id=self.connector_id, items=items,
                         truncated=truncated,
                         detail=f"{len(items)} {self.title} file(s)")

    def fetch_metadata(self, item_id: str) -> dict[str, Any]:
        path = self._resolve(item_id)
        stat = path.stat()
        return {"item_id": item_id, "name": path.name, "path": str(path),
                "size": stat.st_size, "modified_at": _iso(stat.st_mtime),
                "checksum": file_checksum(path), **self.describe_file(path)}

    def fetch_content(self, item_id: str) -> bytes:
        return self._resolve(item_id).read_bytes()

    # ---------------------------------------------------------------- sync
    def sync(self, cursor: SyncCursor | None = None) -> SyncOutcome:
        return self._scan(SyncCursor(), "full",
                          cursor.version if cursor else 0)

    def incremental_sync(self, cursor: SyncCursor) -> SyncOutcome:
        return self._scan(cursor, "incremental", cursor.version)

    def _scan(self, cursor: SyncCursor, mode: str,
              previous_version: int) -> SyncOutcome:
        self.connect()
        previous = dict(cursor.fingerprints)
        current: dict[str, str] = {}
        packages: list[KnowledgePackage] = []
        warnings: list[str] = []
        unchanged, truncated = 0, False

        for index, path in enumerate(self._files(limit=MAX_FILES_PER_SYNC + 1)):
            if index >= MAX_FILES_PER_SYNC:
                truncated = True
                warnings.append(
                    f"repository holds more than {MAX_FILES_PER_SYNC} files — "
                    f"synchronized the first {MAX_FILES_PER_SYNC}")
                break
            item_id = self._item_id(path)
            try:
                stat = path.stat()
                checksum = file_checksum(path)
            except OSError as exc:
                warnings.append(f"{path.name}: {exc}")
                continue

            current[item_id] = checksum
            if previous.get(item_id) == checksum:
                unchanged += 1
                continue
            try:
                metadata = self.describe_file(path)
            except Exception as exc:  # noqa: BLE001 — degrade one file
                warnings.append(f"{path.name}: {type(exc).__name__}: {exc}")
                metadata = {"error": str(exc)[:200]}
            packages.append(KnowledgePackage(
                **self.package_defaults(), item_id=item_id, location=str(path),
                family="table", file_type=path.suffix.lower(), title=path.name,
                author=str(self.config.options.get("author", "")),
                tags=list(self.config.options.get("tags", [])),
                created_date=_iso(stat.st_ctime),
                modified_date=_iso(stat.st_mtime),
                checksum=checksum, size=stat.st_size,
                version=previous_version + 1,
                structured_metadata=metadata,
                permissions={"scope": self.config.options.get(
                    "scope", "organization")}))

        _, removed = self._diff_fingerprints(previous, current)
        if truncated:
            removed = []  # an unseen tail is not a deletion

        return SyncOutcome(
            connector_id=self.connector_id, mode=mode, packages=packages,
            removed=removed, unchanged=unchanged, truncated=truncated,
            warnings=warnings,
            cursor=SyncCursor(version=previous_version + 1,
                              fingerprints=current, last_synced_at=now_iso()))

    # ---------------------------------------------------- format specifics
    @abstractmethod
    def describe_file(self, path: Path) -> dict[str, Any]:
        """Structural metadata for one file: sheets/tables, schema, types."""

    # -------------------------------------------------------------- helpers
    def _require_root(self) -> Path:
        if self._root is None:
            self.initialize()
        assert self._root is not None
        return self._root

    def _files(self, limit: int):
        root = self._require_root()
        if root.is_file():
            if root.suffix.lower() in self.extensions:
                yield root
            return
        recursive = bool(self.config.options.get("recursive", True))
        yielded = 0
        for path in sorted(root.rglob("*") if recursive else root.glob("*")):
            if yielded >= limit:
                return
            if not path.is_file() or path.suffix.lower() not in self.extensions:
                continue
            if path.name.startswith("~$") or path.name.startswith("."):
                continue
            yielded += 1
            yield path

    def _item_id(self, path: Path) -> str:
        root = self._require_root()
        if root.is_file():
            return path.name
        return path.relative_to(root).as_posix()

    def _resolve(self, item_id: str) -> Path:
        root = self._require_root()
        path = root if root.is_file() else (root / item_id)
        if not path.is_file():
            raise ConnectionFailed(f"no such file in this source: {item_id}")
        return path


def _iso(timestamp: float) -> str:
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()

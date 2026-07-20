"""Folder Connector — monitored local and shared folders.

The first and most common enterprise source: a directory (local, mapped
drive, UNC share, or a OneDrive/SharePoint-synced folder, which is a local
directory as far as this connector is concerned) that people already put
documents in. Nobody uploads anything; the folder *is* the interface.

Change detection is by content hash, not modification time: a file that is
touched but unchanged must not re-enter the pipeline, and a file restored
from backup with an old timestamp must. Hashing every file on every sync is
affordable because the hash is streamed and the pipeline downstream of it
only runs on the delta.

    new file      → package, version 1
    updated file  → package, next version (same key)
    deleted file  → key in ``removed``, archived downstream

Supported: PDF, DOCX, PPTX, XLSX/XLSM, CSV/TSV, TXT, Markdown — the formats
Document Intelligence can already parse. Anything else in the folder is
ignored silently: enterprise folders contain noise, and a connector that
fails on an unknown file type is a connector that never finishes.
"""
from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from app.connectors.base import (
    ConnectionFailed, ConnectorConfig, ConnectorHealth, ConnectorNotConfigured,
    Discovery, DiscoveredItem, EnterpriseConnector, SyncCursor, SyncOutcome,
    now_iso,
)
from app.connectors.package import KnowledgePackage
from app.core.logging import get_logger

logger = get_logger(__name__)

# A folder sync is a heartbeat scan, not a crawl. A folder larger than this
# syncs its first slice and reports the truncation rather than pretending it
# saw everything.
MAX_FILES_PER_SYNC = 2_000
MAX_DISCOVERY_ITEMS = 500
HASH_CHUNK_BYTES = 1 << 20
# Content is loaded for text-ish formats only; binary formats are parsed from
# disk by Document Intelligence, which is better at it than a byte blob.
INLINE_CONTENT_EXTENSIONS = (".txt", ".md", ".markdown", ".csv", ".tsv")


def file_checksum(path: Path) -> str:
    """Streamed SHA-256 — a 2 GB spreadsheet must not become 2 GB of RAM."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(HASH_CHUNK_BYTES):
            digest.update(chunk)
    return digest.hexdigest()


class FolderConnector(EnterpriseConnector):
    """Monitors one configured folder tree."""

    kind = "folder"
    title = "Folder"
    description = ("A monitored local, shared, or synced folder. Detects new, "
                   "updated, and deleted documents by content hash.")
    capabilities = ("discover", "incremental", "content", "deletions",
                    "test_connection")
    produces = "documents"

    def __init__(self, config: ConnectorConfig):
        super().__init__(config)
        self._root: Path | None = None

    # ----------------------------------------------------------- lifecycle
    def initialize(self) -> None:
        super().initialize()
        if not self.config.location:
            raise ConnectorNotConfigured(
                f"Folder connector '{self.name}' needs a location (the folder path)")
        self._root = Path(self.config.location).expanduser()

    def connect(self) -> None:
        root = self._require_root()
        if not root.exists():
            raise ConnectionFailed(f"folder does not exist: {root}")
        if not root.is_dir():
            raise ConnectionFailed(f"location is not a folder: {root}")
        self._connected = True

    def _probe(self) -> str:
        root = self._require_root()
        count = sum(1 for _ in self._files(limit=MAX_DISCOVERY_ITEMS))
        return (f"folder reachable: {root} "
                f"({count}{'+' if count >= MAX_DISCOVERY_ITEMS else ''} "
                f"supported document{'s' if count != 1 else ''})")

    def health(self) -> ConnectorHealth:
        try:
            root = self._require_root()
        except ConnectorNotConfigured as exc:
            return ConnectorHealth(state="unconfigured", detail=str(exc))
        if not root.exists():
            return ConnectorHealth(state="unreachable",
                                   detail=f"folder does not exist: {root}")
        if not root.is_dir():
            return ConnectorHealth(state="degraded",
                                   detail=f"not a folder: {root}")
        return ConnectorHealth(state="healthy",
                               detail=f"monitoring {root}")

    # ----------------------------------------------------------- discovery
    def discover(self) -> Discovery:
        """What the folder holds right now — metadata only, no hashing, so
        an administrator gets an answer immediately while registering."""
        self.connect()
        items: list[DiscoveredItem] = []
        truncated = False
        for path in self._files(limit=MAX_DISCOVERY_ITEMS + 1):
            if len(items) >= MAX_DISCOVERY_ITEMS:
                truncated = True
                break
            try:
                stat = path.stat()
            except OSError:
                continue
            items.append(DiscoveredItem(
                item_id=self._item_id(path), name=path.name,
                item_type="file", size=stat.st_size,
                modified_at=_iso(stat.st_mtime),
                metadata={"extension": path.suffix.lower(),
                          "folder": str(path.parent)}))
        return Discovery(connector_id=self.connector_id, items=items,
                         truncated=truncated,
                         detail=f"{len(items)} document(s) under {self._root}")

    def fetch_metadata(self, item_id: str) -> dict[str, Any]:
        path = self._resolve(item_id)
        stat = path.stat()
        return {"item_id": item_id, "name": path.name,
                "extension": path.suffix.lower(), "path": str(path),
                "size": stat.st_size, "modified_at": _iso(stat.st_mtime),
                "created_at": _iso(stat.st_ctime),
                "checksum": file_checksum(path)}

    def fetch_content(self, item_id: str) -> bytes:
        return self._resolve(item_id).read_bytes()

    # ---------------------------------------------------------------- sync
    def sync(self, cursor: SyncCursor | None = None) -> SyncOutcome:
        """Full scan: every supported document becomes a package."""
        return self._scan(SyncCursor(), mode="full",
                          previous_version=(cursor.version if cursor else 0))

    def incremental_sync(self, cursor: SyncCursor) -> SyncOutcome:
        """Only what changed since the last scan, plus what disappeared."""
        return self._scan(cursor, mode="incremental",
                          previous_version=cursor.version)

    def _scan(self, cursor: SyncCursor, mode: str,
              previous_version: int) -> SyncOutcome:
        self.connect()
        previous = dict(cursor.fingerprints)
        current: dict[str, str] = {}
        packages: list[KnowledgePackage] = []
        warnings: list[str] = []
        unchanged = 0
        truncated = False

        for index, path in enumerate(self._files(limit=MAX_FILES_PER_SYNC + 1)):
            if index >= MAX_FILES_PER_SYNC:
                truncated = True
                warnings.append(
                    f"folder holds more than {MAX_FILES_PER_SYNC} documents — "
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
            packages.append(self._package(path, item_id, stat, checksum,
                                          previous_version))

        _, removed = self._diff_fingerprints(previous, current)
        if truncated:
            # A truncated scan has not seen the tail of the folder; treating
            # unseen files as deleted would archive real documents.
            removed = []

        return SyncOutcome(
            connector_id=self.connector_id, mode=mode, packages=packages,
            removed=removed, unchanged=unchanged, truncated=truncated,
            warnings=warnings,
            cursor=SyncCursor(version=previous_version + 1,
                              fingerprints=current, last_synced_at=now_iso()))

    def _package(self, path: Path, item_id: str, stat, checksum: str,
                 previous_version: int) -> KnowledgePackage:
        extension = path.suffix.lower()
        content: bytes | None = None
        if extension in INLINE_CONTENT_EXTENSIONS:
            try:
                content = path.read_bytes()
            except OSError as exc:  # metadata still ships; content is optional
                logger.warning("Could not read %s: %s", path.name, exc)
        return KnowledgePackage(
            **self.package_defaults(), item_id=item_id, location=str(path),
            family="document", file_type=extension, title=path.name,
            author=str(self.config.options.get("author", "")),
            tags=list(self.config.options.get("tags", [])),
            created_date=_iso(stat.st_ctime),
            modified_date=_iso(stat.st_mtime),
            raw_content=content, checksum=checksum, size=stat.st_size,
            version=previous_version + 1,
            structured_metadata={"folder": str(path.parent),
                                 "relative_path": item_id,
                                 "extension": extension},
            permissions={"scope": self.config.options.get("scope", "organization")})

    # -------------------------------------------------------------- helpers
    def _require_root(self) -> Path:
        if self._root is None:
            self.initialize()
        assert self._root is not None  # initialize() raises otherwise
        return self._root

    def _extensions(self) -> set[str]:
        """Supported formats — the parser's list, optionally narrowed by the
        source's own configuration."""
        from app.documents.parser import DocumentParser
        supported = set(DocumentParser.supported_extensions())
        configured = self.config.options.get("extensions")
        if configured:
            return {e.lower() if e.startswith(".") else f".{e.lower()}"
                    for e in configured} & supported
        return supported

    def _files(self, limit: int):
        """Supported documents under the root, deterministically ordered."""
        root = self._require_root()
        extensions = self._extensions()
        recursive = bool(self.config.options.get("recursive", True))
        paths = sorted(root.rglob("*") if recursive else root.glob("*"))
        yielded = 0
        for path in paths:
            if yielded >= limit:
                return
            if not path.is_file() or path.suffix.lower() not in extensions:
                continue
            if path.name.startswith("~$") or path.name.startswith("."):
                continue  # Office lock files and dotfiles are never documents
            yielded += 1
            yield path

    def _item_id(self, path: Path) -> str:
        """Path relative to the root: stable across syncs, and readable."""
        return path.relative_to(self._require_root()).as_posix()

    def _resolve(self, item_id: str) -> Path:
        root = self._require_root()
        path = (root / item_id).resolve()
        if not str(path).startswith(str(root.resolve())):
            raise ConnectionFailed(f"item is outside the monitored folder: {item_id}")
        if not path.is_file():
            raise ConnectionFailed(f"no such document in this source: {item_id}")
        return path


def _iso(timestamp: float) -> str:
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()

"""Unified Knowledge Package — the one shape every connector produces.

A folder full of PDFs, an Excel workbook's sheets, a PostgreSQL table, and
(later) an Outlook mailbox have nothing in common at the source. They have
everything in common by the time they reach the Enterprise Brain, because
every connector normalizes to this object before anything downstream sees it.

That is the whole point of the framework: Document Intelligence, the
embedding pipeline, the knowledge graph, and memory consume ``KnowledgePackage``
and never branch on where it came from. Adding a connector adds a producer,
never a consumer change.

    Connector → KnowledgePackage → Document Intelligence → Embeddings
        → Enterprise Brain → Knowledge Graph → Memory → AI Services

``raw_content`` is optional and kept out of persistence deliberately: a
package is a *record*, and the record must stay small enough to keep in sync
history. Content flows through the pipeline in memory; what persists is the
metadata, the checksum, and the version.
"""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

# What kind of thing the package holds. Decides which downstream pipeline
# consumes it — the same routing vocabulary the sync layer already uses.
PACKAGE_FAMILIES = ("document", "table", "record", "message")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def checksum_of(payload: Any) -> str:
    """Content checksum: bytes hash directly, anything else through a stable
    JSON encoding so two equal records always agree."""
    if isinstance(payload, (bytes, bytearray)):
        return hashlib.sha256(bytes(payload)).hexdigest()
    import json
    encoded = json.dumps(payload, sort_keys=True, default=str)
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


@dataclass
class KnowledgePackage:
    """One unit of organizational knowledge, normalized.

    Identity is ``(source_id, item_id)``: stable across syncs, which is what
    lets the platform version a document rather than duplicating it every
    time its folder is re-read.
    """

    # ---- provenance: where this came from
    source_id: str                          # the connector's id
    source_name: str = ""
    connector_type: str = ""                # folder | excel | csv | postgresql | ...
    item_id: str = ""                       # stable id within the source
    location: str = ""                      # path, URL, schema.table

    # ---- what it is
    family: str = "document"                # PACKAGE_FAMILIES
    file_type: str = ""                     # .pdf, .xlsx, table, ...
    title: str = ""
    author: str = ""
    tags: list[str] = field(default_factory=list)

    # ---- when
    created_date: str = ""
    modified_date: str = ""
    ingested_at: str = field(default_factory=now_iso)

    # ---- content and structure
    raw_content: bytes | str | None = None  # in memory only; never persisted
    structured_metadata: dict[str, Any] = field(default_factory=dict)
    records: list[dict[str, Any]] = field(default_factory=list)

    # ---- integrity, versioning, access
    checksum: str = ""
    version: int = 1
    permissions: dict[str, Any] = field(default_factory=dict)
    size: int = 0
    project_id: str = ""

    def __post_init__(self) -> None:
        if self.family not in PACKAGE_FAMILIES:
            raise ValueError(f"Unknown package family: {self.family}")
        if not self.checksum:
            self.checksum = checksum_of(
                self.raw_content if self.raw_content is not None
                else {"metadata": self.structured_metadata,
                      "records": self.records})
        if not self.title:
            self.title = self.item_id or self.source_name

    # ------------------------------------------------------------- identity
    @property
    def key(self) -> str:
        """The stable cross-sync identity used for fingerprints and versions."""
        return f"{self.source_id}:{self.item_id}"

    def content_text(self) -> str:
        """Best-effort text of the raw content, for parsers that want a
        string. Binary content that is not valid UTF-8 comes back empty
        rather than mangled — the document parser handles bytes properly."""
        if isinstance(self.raw_content, str):
            return self.raw_content
        if isinstance(self.raw_content, (bytes, bytearray)):
            try:
                return bytes(self.raw_content).decode("utf-8")
            except UnicodeDecodeError:
                return ""
        return ""

    # -------------------------------------------------------------- views
    def describe(self) -> dict:
        """The persistable record: everything except the content itself."""
        return {
            "source_id": self.source_id, "source_name": self.source_name,
            "connector_type": self.connector_type, "item_id": self.item_id,
            "key": self.key, "location": self.location,
            "family": self.family, "file_type": self.file_type,
            "title": self.title, "author": self.author, "tags": self.tags,
            "created_date": self.created_date,
            "modified_date": self.modified_date,
            "ingested_at": self.ingested_at,
            "structured_metadata": self.structured_metadata,
            "records": len(self.records),
            "checksum": self.checksum, "version": self.version,
            "permissions": self.permissions, "size": self.size,
            "project_id": self.project_id,
            "has_content": self.raw_content is not None,
        }

    def as_document_record(self) -> dict:
        """The shape ``DocumentIntelligence`` already consumes.

        The document pipeline was built against sync-delta records and is
        unchanged by this framework: packages adapt to it, not the reverse.
        """
        return {
            "id": self.item_id, "name": self.title,
            "extension": self.file_type,
            "path": self.location, "size": self.size,
            "modified_at": self.modified_date,
            "content_hash": self.checksum,
        }

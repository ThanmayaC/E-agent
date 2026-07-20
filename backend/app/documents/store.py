"""Document store — every ingested document and its version history.

A document's identity is (source, relative id); its versions accumulate: an
update appends a version, it never overwrites the last one — the same
history-preserving contract the Knowledge Store and the organizational model
already keep. Chunk vectors live in the vector store; this store holds the
facts about documents so "what changed, when, and what did we do about it?"
is always answerable.
"""
from __future__ import annotations

import threading
from pathlib import Path

from app.sync.store import SyncStore, new_id, now_iso

DOCUMENT_STATUSES = ("active", "archived")
MAX_VERSIONS_PER_DOCUMENT = 25
MAX_TEXT_PREVIEW = 800

# What a source kind's documents *are* to the organization. This is the
# bridge between "a folder synchronized" and "the Brain knows SOPs".
CATEGORY_BY_SOURCE_KIND = {
    "sop_repository": "sop",
    "rca_repository": "rca",
    "policy_repository": "policy",
    "meeting_notes": "meeting",
    "product_documents": "product_document",
    "document_folder": "document",
    "onedrive": "document",
    "sharepoint": "document",
}


class DocumentStore:
    def __init__(self, documents_dir: Path):
        self._store = SyncStore(documents_dir,
                                sections=("documents", "versions"))
        self._lock = threading.RLock()

    # --------------------------------------------------------------- write
    def upsert(self, source_name: str, source_kind: str, doc_id: str,
               name: str, extension: str, size: int, modified_at: str,
               content_hash: str, text: str, chunks: int, parser: str,
               ocr_used: bool, warnings: list[str], change: str,
               location: str = "") -> tuple[dict, bool]:
        """Record a document observation. Returns ``(document, new_version)``
        — ``new_version`` is False when the content hash is already the
        current version (nothing to learn)."""
        document_key = f"{source_name}:{doc_id}"
        category = CATEGORY_BY_SOURCE_KIND.get(source_kind, "document")
        with self._lock:
            existing = self._store.get("documents", "document_key",
                                       document_key)
            if existing and existing.get("content_hash") == content_hash \
                    and existing.get("status") == "active":
                return existing, False

            version_n = (existing.get("version", 0) + 1) if existing else 1
            fields = {
                "document_key": document_key, "source": source_name,
                "source_kind": source_kind, "category": category,
                "doc_id": doc_id, "name": name[:200],
                "extension": extension, "size": size,
                "modified_at": modified_at, "content_hash": content_hash,
                "location": location[:500], "version": version_n,
                "status": "active", "parsed": bool(text.strip()),
                "parser": parser, "ocr_used": ocr_used,
                "warnings": warnings[:5], "chars": len(text),
                "chunks": chunks,
                "text_preview": text[:MAX_TEXT_PREVIEW],
                "updated_at": now_iso(),
            }
            if existing:
                document = self._store.update("documents", "document_key",
                                              document_key, fields)
            else:
                fields["document_id"] = new_id("doc")
                fields["first_seen_at"] = now_iso()
                document = self._store.append("documents", fields)

            self._append_version(document["document_id"], {
                "version": version_n, "change": change,
                "content_hash": content_hash, "chars": len(text),
                "chunks": chunks, "parsed": bool(text.strip()),
                "at": now_iso()})
            return document, True

    def archive(self, source_name: str, doc_id: str) -> dict | None:
        """The source no longer has this document. History is kept."""
        document_key = f"{source_name}:{doc_id}"
        with self._lock:
            existing = self._store.get("documents", "document_key",
                                       document_key)
            if existing is None or existing.get("status") == "archived":
                return None
            document = self._store.update(
                "documents", "document_key", document_key,
                {"status": "archived", "updated_at": now_iso()})
            self._append_version(existing["document_id"], {
                "version": existing.get("version", 1), "change": "removed",
                "content_hash": existing.get("content_hash", ""),
                "at": now_iso()})
            return document

    def _append_version(self, document_id: str, version: dict) -> None:
        with self._store.mutate("versions") as versions:
            versions.append({"document_id": document_id, **version})
            mine = [v for v in versions if v["document_id"] == document_id]
            if len(mine) > MAX_VERSIONS_PER_DOCUMENT:
                drop = {id(v) for v in mine[:-MAX_VERSIONS_PER_DOCUMENT]}
                versions[:] = [v for v in versions if id(v) not in drop]

    def mark_processed(self, document_id: str, workflow: str,
                       version: int) -> None:
        """Record that a workflow consumed this document version, so
        summarization work is done once per version, not once per run."""
        document = self._store.get("documents", "document_id", document_id)
        if document is None:
            return
        processed = dict(document.get("processed") or {})
        processed[workflow] = version
        self._store.update("documents", "document_id", document_id,
                           {"processed": processed})

    # ---------------------------------------------------------------- read
    def documents(self, category: str = "", source: str = "",
                  status: str = "active", limit: int = 200) -> list[dict]:
        items = self._store.read("documents")
        if category:
            items = [d for d in items if d.get("category") == category]
        if source:
            items = [d for d in items if d.get("source") == source]
        if status:
            items = [d for d in items if d.get("status") == status]
        items.sort(key=lambda d: d.get("updated_at", ""), reverse=True)
        return items[:limit]

    def get(self, document_id: str) -> dict | None:
        return self._store.get("documents", "document_id", document_id)

    def versions(self, document_id: str) -> list[dict]:
        return [v for v in self._store.read("versions")
                if v["document_id"] == document_id]

    def unprocessed(self, workflow: str, category: str,
                    limit: int = 20) -> list[dict]:
        """Active documents whose current version this workflow has not
        consumed yet — the workfeed for summarization workflows."""
        out = []
        for document in self.documents(category=category, limit=500):
            if not document.get("parsed"):
                continue
            done = (document.get("processed") or {}).get(workflow, 0)
            if document.get("version", 1) > done:
                out.append(document)
            if len(out) >= limit:
                break
        return out

    def stats(self) -> dict:
        items = self._store.read("documents")
        by_category: dict[str, int] = {}
        by_source: dict[str, int] = {}
        for d in items:
            if d.get("status") != "active":
                continue
            by_category[d["category"]] = by_category.get(d["category"], 0) + 1
            by_source[d["source"]] = by_source.get(d["source"], 0) + 1
        return {
            "documents": sum(1 for d in items if d.get("status") == "active"),
            "archived": sum(1 for d in items if d.get("status") == "archived"),
            "parsed": sum(1 for d in items
                          if d.get("status") == "active" and d.get("parsed")),
            "versions": len(self._store.read("versions")),
            "chunks": sum(d.get("chunks", 0) for d in items
                          if d.get("status") == "active"),
            "by_category": by_category, "by_source": by_source,
        }

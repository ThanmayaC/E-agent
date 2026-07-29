"""Document Intelligence pipeline — sync deltas in, Brain updates out.

    detect (sync delta) → metadata → parse (+OCR) → chunk → embed
      → update Enterprise Brain → track versions

Change detection is NOT here: the Synchronization Engine already fingerprints
every record, and a document source's records carry the content hash, so
"new or updated document" is exactly the sync delta. This pipeline consumes
only added/changed/removed document records — an unchanged folder costs
nothing, which is what lets document sources run on the same hourly cadence
as everything else.

Per-document degradation: one unparseable file is recorded with its warnings
and skipped; it never stops the folder, the source, or the refresh.
"""
from __future__ import annotations

import hashlib
import tempfile
import time
from pathlib import Path
from typing import Any

from app.core.logging import get_logger
from app.documents.chunker import chunk_text
from app.documents.parser import DocumentParser
from app.documents.store import CATEGORY_BY_SOURCE_KIND, DocumentStore

logger = get_logger(__name__)

# Documents are searchable enterprise-wide, in one collection.
VECTOR_COLLECTION = "_documents"
MAX_DOCUMENTS_PER_DELTA = 200
MAX_CHUNKS_PER_DOCUMENT = 60

# Document category → organizational entity kind. Meetings map onto the
# entity kind the model already has; the V2 kinds were added alongside.
ENTITY_KIND_BY_CATEGORY = {
    "sop": "sop", "rca": "rca", "policy": "policy", "meeting": "meeting",
    "product_document": "document", "document": "document",
}


class DocumentIntelligence:
    """The unified document processing pipeline."""

    def __init__(self, store: DocumentStore, parser: DocumentParser,
                 chunk_chars: int = 1600, chunk_overlap: int = 200,
                 embedder=None, vector_store_for=None, knowledge=None,
                 organization=None, bus=None, graph_client_for=None,
                 latency=None, embedding_model: str = ""):
        self._store = store
        self._parser = parser
        self._chunk_chars = chunk_chars
        self._chunk_overlap = chunk_overlap
        self._embedder = embedder
        self._vector_store_for = vector_store_for
        self._knowledge = knowledge
        self._organization = organization
        self._bus = bus
        # source dict -> GraphClient, for remote documents (SharePoint)
        self._graph_client_for = graph_client_for
        # Optional — retrieval timing for the RAG diagnostics panel, and the
        # configured embedding model name so the UI can state honestly
        # whether embeddings are semantic or the built-in hash fallback.
        self._latency = latency
        self._embedding_model = embedding_model

    def attach_bus(self, bus) -> None:
        self._bus = bus

    # -------------------------------------------------------------- process
    def process_sync(self, source: dict, deltas: list) -> dict[str, int]:
        """Consume one source's sync deltas. Only document tables are
        processed; a source can also carry ordinary tabular data untouched."""
        counts = {"ingested": 0, "updated": 0, "archived": 0, "failed": 0,
                  "chunks": 0}
        categories: set[str] = set()
        for delta in deltas:
            if delta.table != "documents":
                continue
            changed = (list(delta.added) + list(delta.changed))
            for item in changed[:MAX_DOCUMENTS_PER_DELTA]:
                outcome = self._process_record(source, item["record"])
                if outcome is None:
                    counts["failed"] += 1
                    continue
                document, is_new_version = outcome
                if is_new_version:
                    key = "ingested" if document["version"] == 1 else "updated"
                    counts[key] += 1
                    counts["chunks"] += document.get("chunks", 0)
                    categories.add(document["category"])
            for key in delta.removed:
                doc_id = key.split(":", 1)[1] if ":" in key else key
                if self._store.archive(source["name"], doc_id) is not None:
                    counts["archived"] += 1

        if counts["ingested"] or counts["updated"] or counts["archived"]:
            self._record_learning(source, counts)
            self._announce(source, counts, sorted(categories))
        return counts

    def _process_record(self, source: dict,
                        record: dict) -> tuple[dict, bool] | None:
        """metadata → parse → chunk → embed → store, for one document."""
        try:
            doc_id = str(record.get("id") or record.get("name") or "")
            name = str(record.get("name") or doc_id)
            extension = str(record.get("extension")
                            or Path(name).suffix).lower()
            text, parsed_meta = self._extract_text(source, record, extension)
            chunks = chunk_text(text, self._chunk_chars, self._chunk_overlap)
            chunks = chunks[:MAX_CHUNKS_PER_DOCUMENT]

            document, is_new = self._store.upsert(
                source_name=source["name"], source_kind=source["kind"],
                doc_id=doc_id, name=name, extension=extension,
                size=int(record.get("size") or 0),
                modified_at=str(record.get("modified_at") or ""),
                content_hash=str(record.get("content_hash") or ""),
                text=text, chunks=len(chunks),
                parser=parsed_meta.get("parser", ""),
                ocr_used=bool(parsed_meta.get("ocr_used")),
                warnings=parsed_meta.get("warnings", []),
                change="added" if record.get("_change") != "changed" else "changed",
                location=str(record.get("path") or record.get("web_url") or ""))
            if is_new and chunks:
                self._embed(document, chunks)
            if is_new:
                self._observe_entity(document)
            return document, is_new
        except Exception:  # noqa: BLE001 — per-document degradation
            logger.exception("Document processing failed for record %s",
                             str(record.get("name", ""))[:80])
            return None

    # ------------------------------------------------------------- parsing
    def _extract_text(self, source: dict, record: dict,
                      extension: str) -> tuple[str, dict]:
        """Parse from the local path when the source is a folder; download to
        a temp file when the document lives behind Microsoft Graph."""
        path_text = str(record.get("path") or "")
        if path_text:
            path = Path(path_text)
            if path.exists() and self._parser.can_parse(path):
                parsed = self._parser.parse(path)
                return parsed.text, {"parser": parsed.parser,
                                     "ocr_used": parsed.ocr_used,
                                     "warnings": parsed.warnings}
            return "", {"warnings": [f"file not parseable here: {path.name}"]}

        download_url = str(record.get("download_url") or "")
        if download_url and self._graph_client_for is not None:
            try:
                client = self._graph_client_for(source)
                content = client.download(download_url)
                with tempfile.NamedTemporaryFile(suffix=extension,
                                                 delete=False) as handle:
                    handle.write(content)
                    temp_path = Path(handle.name)
                try:
                    parsed = self._parser.parse(temp_path)
                finally:
                    temp_path.unlink(missing_ok=True)
                return parsed.text, {"parser": parsed.parser,
                                     "ocr_used": parsed.ocr_used,
                                     "warnings": parsed.warnings}
            except Exception as exc:  # noqa: BLE001
                return "", {"warnings": [f"remote fetch failed: {exc}"[:200]]}
        return "", {"warnings": ["no readable content location"]}

    # ----------------------------------------------------------- embeddings
    def _embed(self, document: dict, chunks: list[str]) -> None:
        if self._embedder is None or self._vector_store_for is None:
            return
        try:
            vectors = self._embedder.embed(chunks)
            store = self._vector_store_for(VECTOR_COLLECTION)
            ids = [f"{document['document_id']}:v{document['version']}:{i}"
                   for i in range(len(chunks))]
            store.upsert(ids, vectors, [
                {"kind": "document_chunk",
                 "document_id": document["document_id"],
                 "document": document["name"],
                 "category": document["category"],
                 "source": document["source"],
                 "version": document["version"], "chunk": i, "text": chunk}
                for i, chunk in enumerate(chunks)])
            store.persist()
        except Exception:  # noqa: BLE001 — embeddings degrade, never fail
            logger.exception("Document embedding failed for %s",
                             document["name"])

    # ------------------------------------------------------ brain updates
    def _observe_entity(self, document: dict) -> None:
        """The organizational model learns the document exists."""
        if self._organization is None:
            return
        kind = ENTITY_KIND_BY_CATEGORY.get(document["category"], "document")
        try:
            self._organization.observe(
                kind=kind, name=Path(document["name"]).stem,
                source=f"document:{document['source']}",
                attributes={"category": document["category"],
                            "extension": document["extension"],
                            "version": document["version"]})
        except Exception:  # noqa: BLE001 — observation degrades
            logger.exception("Entity observation failed for document %s",
                             document["name"])

    def _record_learning(self, source: dict, counts: dict) -> None:
        if self._knowledge is None:
            return
        try:
            self._knowledge.record_learning_event(
                "document_intelligence", source="document_pipeline",
                details={"source": source["name"], **counts})
        except Exception:  # noqa: BLE001
            logger.exception("Learning event recording failed")

    def _announce(self, source: dict, counts: dict,
                  categories: list[str]) -> None:
        if self._bus is None:
            return
        try:
            self._bus.publish("DocumentsUpdated", {
                "source": source["name"], "source_kind": source["kind"],
                "categories": categories, **counts},
                source="document_pipeline")
        except Exception:  # noqa: BLE001 — announcing never fails ingestion
            logger.exception("Document event publication failed")

    # ------------------------------------------------------------ read side
    def documents(self, category: str = "", source: str = "",
                  status: str = "active", limit: int = 200) -> list[dict]:
        return self._store.documents(category, source, status, limit)

    def get(self, document_id: str) -> dict | None:
        return self._store.get(document_id)

    def versions(self, document_id: str) -> list[dict]:
        return self._store.versions(document_id)

    def unprocessed(self, workflow: str, category: str,
                    limit: int = 20) -> list[dict]:
        return self._store.unprocessed(workflow, category, limit)

    def mark_processed(self, document_id: str, workflow: str,
                       version: int) -> None:
        self._store.mark_processed(document_id, workflow, version)

    def search(self, query: str, limit: int = 8) -> list[dict]:
        """Semantic search over document chunks."""
        if self._embedder is None or self._vector_store_for is None:
            return []
        started = time.monotonic()
        try:
            vector = self._embedder.embed([query])[0]
            store = self._vector_store_for(VECTOR_COLLECTION)
            hits = store.search(vector, limit)
        except Exception:  # noqa: BLE001
            logger.exception("Document search failed")
            return []
        if self._latency is not None:
            self._latency.record("rag_retrieval",
                                 (time.monotonic() - started) * 1000)
        return hits

    def retrieval_stats(self) -> dict:
        """What the retrieval layer actually holds — the numbers the RAG
        diagnostics page reports, read from the live vector store rather
        than counted at ingestion time."""
        model = self._embedding_model or "unknown"
        stats: dict[str, Any] = {
            "embedding_model": model,
            # The built-in "hash" embedder is a deterministic feature-hash
            # vector, not a trained semantic model. Saying so is the
            # difference between an honest diagnostic and a badge.
            "semantic": model not in ("", "hash", "unknown"),
            "embedder_available": self._embedder is not None,
            "vector_store_available": self._vector_store_for is not None,
        }
        if self._vector_store_for is None:
            stats["vectors"] = 0
            stats["reason"] = "No vector store is configured in this deployment"
            return stats
        try:
            store = self._vector_store_for(VECTOR_COLLECTION)
            stats.update(store.stats())
        except Exception as exc:  # noqa: BLE001 — diagnostics never raise
            stats["vectors"] = 0
            stats["reason"] = f"{type(exc).__name__}: {exc}"[:200]
        return stats

    def status(self) -> dict:
        return {"enabled": True, "formats": DocumentParser.formats(),
                "retrieval": self.retrieval_stats(),
                **self._store.stats()}


def file_content_hash(path: Path) -> str:
    """Streaming SHA-256 of a file — the identity of a document version."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()

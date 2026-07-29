"""Document Intelligence API (Version 2).

Read-only observability over the unified document pipeline: what has been
ingested, parsed, chunked, and versioned, plus semantic search over chunks.
Ingestion itself is autonomous — documents arrive through the connector
layer's synchronization, never through this API.
"""
from __future__ import annotations

import time

from fastapi import APIRouter, Depends, HTTPException, Query

from app.api.deps import container
from app.core.container import Container

router = APIRouter(tags=["documents"])


def _documents(c: Container):
    documents = getattr(c.sync, "documents", None)
    if documents is None:
        raise HTTPException(status_code=503,
                            detail="Document Intelligence is disabled")
    return documents


@router.get("/documents")
def list_documents(category: str = "", source: str = "",
                   status: str = Query("active"),
                   limit: int = Query(100, ge=1, le=500),
                   c: Container = Depends(container)):
    return {"documents": _documents(c).documents(category, source, status,
                                                 limit)}


@router.get("/documents/status")
def documents_status(c: Container = Depends(container)):
    """Pipeline status: counts by category and source, parser availability."""
    return _documents(c).status()


@router.get("/documents/search")
def search_documents(q: str, limit: int = Query(8, ge=1, le=25),
                     c: Container = Depends(container)):
    """Retrieval over document chunks. Returns the elapsed time alongside the
    hits so the caller can see what retrieval actually cost, rather than
    trusting a dashboard average."""
    started = time.monotonic()
    results = _documents(c).search(q, limit)
    return {"results": results, "count": len(results),
            "took_ms": round((time.monotonic() - started) * 1000, 1)}


@router.get("/documents/rag")
def rag_diagnostics(c: Container = Depends(container)):
    """Enterprise RAG diagnostics: what is indexed, how many vectors exist,
    which embedding model produced them, and how long retrieval takes.

    Every number is read live — document counts from the document store,
    vector count from the vector store itself, retrieval timing from the
    platform's latency tracker. Nothing here is a static figure.
    """
    documents = _documents(c)
    store_stats = documents.status()
    retrieval = store_stats.get("retrieval", {})
    timings = c.latency.summary().get("rag_retrieval", {})
    return {
        "documents_indexed": store_stats.get("documents", 0),
        "chunks_embedded": store_stats.get("chunks", 0),
        "by_category": store_stats.get("by_category", {}),
        "retrieval": retrieval,
        "timing": timings or {
            "samples": 0,
            "note": "No retrieval has run yet since the backend started.",
        },
        "pipeline": {
            "parsed": store_stats.get("parsed", 0),
            "versions": store_stats.get("versions", 0),
        },
    }


@router.get("/documents/{document_id}")
def get_document(document_id: str, c: Container = Depends(container)):
    document = _documents(c).get(document_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document


@router.get("/documents/{document_id}/versions")
def document_versions(document_id: str, c: Container = Depends(container)):
    documents = _documents(c)
    if documents.get(document_id) is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"versions": documents.versions(document_id)}

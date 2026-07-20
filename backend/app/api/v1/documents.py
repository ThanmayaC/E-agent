"""Document Intelligence API (Version 2).

Read-only observability over the unified document pipeline: what has been
ingested, parsed, chunked, and versioned, plus semantic search over chunks.
Ingestion itself is autonomous — documents arrive through the connector
layer's synchronization, never through this API.
"""
from __future__ import annotations

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
    return {"results": _documents(c).search(q, limit)}


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

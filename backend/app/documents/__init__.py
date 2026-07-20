"""Document Intelligence (Version 2).

The unified document processing pipeline: detect new or updated documents
(via the Synchronization Engine's fingerprint delta — this package never
re-implements change detection), extract metadata, parse text, OCR where
applicable, chunk, embed, update the Enterprise Brain, and track versions.

Components:
- ``DocumentParser``               — text extraction per format (PDF, DOCX,
  PPTX, Excel, CSV, Markdown, plain text), with an optional OCR fallback.
- ``chunk_text``                   — paragraph-aware chunking with overlap.
- ``DocumentStore``                — documents, versions, and their history.
- ``DocumentIntelligence``         — the pipeline that consumes sync deltas.
"""
from app.documents.chunker import chunk_text
from app.documents.parser import DocumentParser, ParsedDocument
from app.documents.pipeline import DocumentIntelligence
from app.documents.store import DocumentStore

__all__ = ["DocumentIntelligence", "DocumentParser", "DocumentStore",
           "ParsedDocument", "chunk_text"]

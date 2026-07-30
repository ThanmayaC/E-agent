"""Knowledge Engine — retrieval over the enterprise's own documents.

This is RAG, and it is exactly one engine among several — the correction the
whole orchestrator exists to make. It answers what documents actually hold:
meetings, decisions, RCAs, policies, SOPs, reports, the email/Teams corpus. It
does not answer "what is the success rate over July" — that is the Analytics
engine's job — but it does answer "what happened after the July outage".

Reuses the existing document-intelligence search (the same chunk→embed→cosine
pipeline the copilot already uses). Each passage is citable by its document id
and is surfaced under the document's real title, never a raw id (Phase 10).
"""
from __future__ import annotations

import re

from app.orchestrator.base import Engine, EngineRequest, EngineResult

MAX_CHUNKS = 8

# A raw spreadsheet dump — a wide table of date columns ("01-Jul | 02-Jul | …")
# — is not narrative evidence. Retrieved and truncated, it tempts the model to
# quote a cell whose value sits past the truncation, which the validator then
# (correctly) rejects. When analytics is the primary lens, the KPI series is the
# authoritative source of those numbers, so these dumps are dropped from the
# answer's evidence rather than fed as noise.
_DATE_COL = re.compile(r"\d{1,2}-(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|"
                       r"Nov|Dec)", re.I)


def _is_data_dump(text: str) -> bool:
    return len(_DATE_COL.findall(text)) >= 6 or text.count("|") >= 12


class KnowledgeEngine(Engine):
    key = "knowledge"
    label = "Knowledge Engine (RAG)"
    categories = ("knowledge", "report")

    def __init__(self, sync=None):
        self._sync = sync

    def _documents(self):
        return getattr(self._sync, "documents", None)

    def available(self) -> bool:
        return self._documents() is not None

    def run(self, request: EngineRequest) -> EngineResult:
        res = self._result()
        documents = self._documents()
        if documents is None:
            res.status = "unavailable"
            res.ran = False
            res.note = "document intelligence is disabled"
            return res
        matches = documents.search(request.message, limit=MAX_CHUNKS + 6)
        titles: list[str] = []
        skipped = 0
        for match in matches:
            if len(res.evidence) >= MAX_CHUNKS:
                break
            payload = match.get("payload") or match
            text = str(payload.get("text") or "").strip()
            if not text:
                continue
            if _is_data_dump(text):
                skipped += 1
                continue  # a raw spreadsheet dump is not narrative evidence
            i = len(res.evidence)
            document = str(payload.get("document") or "document")
            category = str(payload.get("category") or "document")
            titles.append(f"{document} ({category})")
            res.add(
                "document_chunk",
                str(payload.get("document_id") or f"doc:{i}"),
                f"[{category}] {document}: {text[:220]}",
                {"document": document, "category": category,
                 "source": payload.get("source"), "text": text[:1200]})
        res.detail = {"retriever": "document_intelligence",
                      "query": request.message[:200],
                      "documents_retrieved": len(res.evidence),
                      "data_dumps_skipped": skipped,
                      "titles": titles[:MAX_CHUNKS]}
        return res

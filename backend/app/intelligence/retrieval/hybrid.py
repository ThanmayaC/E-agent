"""Hybrid retrieval — dense + BM25 fused with Reciprocal Rank Fusion, reranked.

Pipeline:  query → (dense semantic search ‖ BM25 lexical search) → RRF fusion
→ rerank → top-k chunks with per-signal scores and retrieval diagnostics.

RRF is used instead of raw-score blending because dense cosine scores and BM25
scores live on different scales; rank fusion needs no calibration and is the
standard production choice. The reranker is a dependency-free lexical
cross-scorer by default, with a hook (`cross_encoder`) to plug a real
cross-encoder model when one is available — the interface does not change.

Every result carries where it came from (dense rank, bm25 rank, fused score) so
answers can cite grounded evidence and the diagnostics page can show exactly
what was retrieved.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any, Callable

from app.intelligence.retrieval.bm25 import BM25Index, tokenize


@dataclass
class RetrievedChunk:
    id: str
    text: str
    payload: dict[str, Any]
    fused_score: float
    dense_rank: int | None = None
    bm25_rank: int | None = None
    rerank_score: float | None = None
    scores: dict[str, float] = field(default_factory=dict)

    def cite(self) -> dict[str, Any]:
        return {"id": self.id, "title": self.payload.get("title", ""),
                "kind": self.payload.get("kind", ""),
                "ref": self.payload.get("ref", ""),
                "fused_score": round(self.fused_score, 4),
                "dense_rank": self.dense_rank, "bm25_rank": self.bm25_rank,
                "rerank_score": (round(self.rerank_score, 4)
                                 if self.rerank_score is not None else None)}


# Dense search returns an ordered list of {"id":..., "score":..., ...payload}.
DenseSearchFn = Callable[[str, int], list[dict[str, Any]]]
CrossEncoderFn = Callable[[str, list[str]], list[float]]


class HybridRetriever:
    """Fuse dense + BM25 retrieval and rerank the result.

    ``dense_search`` is optional — with a weak (e.g. hash) embedder, BM25 alone
    still returns strong lexical matches, so the retriever degrades gracefully.
    """

    def __init__(self, bm25: BM25Index,
                 payloads_by_id: dict[str, dict[str, Any]],
                 dense_search: DenseSearchFn | None = None,
                 rrf_k: int = 60,
                 cross_encoder: CrossEncoderFn | None = None):
        self._bm25 = bm25
        self._payloads = payloads_by_id
        self._dense = dense_search
        self._rrf_k = rrf_k
        self._cross_encoder = cross_encoder

    # ------------------------------------------------------------- retrieve
    def retrieve(self, query: str, top_k: int = 8, *, dense_k: int = 30,
                 bm25_k: int = 30, rerank: bool = True
                 ) -> tuple[list[RetrievedChunk], dict[str, Any]]:
        t0 = time.monotonic()

        dense_hits: list[dict[str, Any]] = []
        dense_ms = 0.0
        if self._dense is not None:
            d0 = time.monotonic()
            try:
                dense_hits = self._dense(query, dense_k) or []
            except Exception:  # noqa: BLE001 — retrieval degrades to BM25
                dense_hits = []
            dense_ms = (time.monotonic() - d0) * 1000

        b0 = time.monotonic()
        bm25_hits = self._bm25.search(query, top_k=bm25_k)
        bm25_ms = (time.monotonic() - b0) * 1000

        dense_rank = {h["id"]: r for r, h in enumerate(dense_hits) if h.get("id")}
        bm25_rank = {doc_id: r for r, (doc_id, _s) in enumerate(bm25_hits)}

        # Reciprocal Rank Fusion across both result lists.
        fused: dict[str, float] = {}
        for doc_id, r in dense_rank.items():
            fused[doc_id] = fused.get(doc_id, 0.0) + 1.0 / (self._rrf_k + r + 1)
        for doc_id, r in bm25_rank.items():
            fused[doc_id] = fused.get(doc_id, 0.0) + 1.0 / (self._rrf_k + r + 1)

        candidates: list[RetrievedChunk] = []
        for doc_id, score in fused.items():
            payload = self._payloads.get(doc_id, {})
            candidates.append(RetrievedChunk(
                id=doc_id, text=str(payload.get("text", "")), payload=payload,
                fused_score=score, dense_rank=dense_rank.get(doc_id),
                bm25_rank=bm25_rank.get(doc_id),
                scores={"rrf": round(score, 5)}))
        candidates.sort(key=lambda c: c.fused_score, reverse=True)

        # Rerank a shortlist (fusion is recall-oriented; rerank is precision).
        pool = candidates[: max(top_k * 3, 12)]
        rerank_ms = 0.0
        if rerank and pool:
            r0 = time.monotonic()
            self._rerank(query, pool)
            pool.sort(key=lambda c: (c.rerank_score if c.rerank_score is not None
                                     else c.fused_score), reverse=True)
            rerank_ms = (time.monotonic() - r0) * 1000
            results = pool[:top_k]
        else:
            results = candidates[:top_k]

        diagnostics = {
            "query": query,
            "dense_candidates": len(dense_hits),
            "bm25_candidates": len(bm25_hits),
            "fused_candidates": len(candidates),
            "returned": len(results),
            "reranked": bool(rerank and pool),
            "dense_ms": round(dense_ms, 1),
            "bm25_ms": round(bm25_ms, 1),
            "rerank_ms": round(rerank_ms, 1),
            "total_ms": round((time.monotonic() - t0) * 1000, 1),
            "bm25_index": self._bm25.stats(),
        }
        return results, diagnostics

    # -------------------------------------------------------------- rerank
    def _rerank(self, query: str, chunks: list[RetrievedChunk]) -> None:
        """Assign each chunk a rerank score. Uses a real cross-encoder when
        supplied; otherwise a dependency-free lexical relevance score (query
        term coverage + title boost) that is a meaningful precision signal on
        top of RRF recall."""
        if self._cross_encoder is not None:
            scores = self._cross_encoder(query, [c.text for c in chunks])
            for c, s in zip(chunks, scores):
                c.rerank_score = float(s)
                c.scores["cross_encoder"] = round(float(s), 4)
            return
        q_terms = set(tokenize(query))
        if not q_terms:
            for c in chunks:
                c.rerank_score = c.fused_score
            return
        for c in chunks:
            body = set(tokenize(c.text))
            title = set(tokenize(str(c.payload.get("title", ""))))
            coverage = len(q_terms & body) / len(q_terms)
            title_boost = 0.25 * (len(q_terms & title) / len(q_terms))
            # blend lexical relevance with the fusion prior
            c.rerank_score = round(0.7 * (coverage + title_boost)
                                   + 0.3 * min(c.fused_score * 30, 1.0), 4)
            c.scores["lexical_coverage"] = round(coverage, 3)

    # ------------------------------------------------- retrieve → LLM prompt
    def retrieve_context(self, query: str, top_k: int = 8, *,
                         token_budget: int = 3000, header: str | None = None,
                         **retrieve_kwargs):
        """Full RAG path in one call: retrieve, then assemble a budgeted,
        cited context package ready to drop into a prompt. Returns a
        :class:`~app.intelligence.retrieval.context_package.ContextPackage`."""
        from app.intelligence.retrieval.context_package import (
            DEFAULT_HEADER, ContextAssembler)

        chunks, diagnostics = self.retrieve(query, top_k=top_k, **retrieve_kwargs)
        return ContextAssembler(token_budget=token_budget).assemble(
            chunks, query=query, retrieval_diagnostics=diagnostics,
            header=DEFAULT_HEADER if header is None else header)

    # --------------------------------------------------------------- build
    @classmethod
    def from_documents(cls, documents: list[dict[str, Any]],
                       dense_search: DenseSearchFn | None = None,
                       cross_encoder: CrossEncoderFn | None = None
                       ) -> "HybridRetriever":
        """Build a retriever from ``[{id, text, ...}]`` documents (the same
        shape `vector_store.build_documents` produces)."""
        bm25 = BM25Index()
        payloads: dict[str, dict[str, Any]] = {}
        for d in documents:
            doc_id = d.get("id")
            if not doc_id:
                continue
            bm25.add(doc_id, d.get("text", ""))
            payloads[doc_id] = d
        bm25.build()
        return cls(bm25, payloads, dense_search=dense_search,
                   cross_encoder=cross_encoder)

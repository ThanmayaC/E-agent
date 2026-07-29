"""Production retrieval: BM25 sparse + dense hybrid fusion + reranking, plus
the context-package assembler that turns retrieved chunks into a budgeted,
cited LLM prompt.

This package sits beside the existing embedding/vector store and upgrades
retrieval quality without replacing it: dense semantic search stays, a BM25
lexical index is added, and the two are fused with Reciprocal Rank Fusion, then
reranked. It is additive — callers opt in through :class:`HybridRetriever`,
and ``HybridRetriever.retrieve_context`` completes the path to the model.
"""
from app.intelligence.retrieval.bm25 import BM25Index
from app.intelligence.retrieval.context_package import (
    DEFAULT_HEADER, ContextAssembler, ContextPackage, ContextPassage,
    estimate_tokens,
)
from app.intelligence.retrieval.hybrid import HybridRetriever, RetrievedChunk

__all__ = [
    "BM25Index", "HybridRetriever", "RetrievedChunk",
    "ContextAssembler", "ContextPackage", "ContextPassage",
    "estimate_tokens", "DEFAULT_HEADER",
]

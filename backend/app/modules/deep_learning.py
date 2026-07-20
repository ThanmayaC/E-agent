"""Deep Learning Module (SDS §2.4) — status: partial.

Implemented: embeddings (hashing baseline + optional sentence-transformers)
and vector stores (in-memory persisted / pgvector) powering semantic
similarity and enterprise search.

SDS scope still open: sequence modelling, behaviour learning, deep anomaly
detection, long-horizon forecasting, GNN integration. The ML module's
eligibility gates already reserve their admission criteria (lstm/deepar,
tft gates in the selection trace).
"""
from app.intelligence.embeddings.embedder import Embedder, HashingEmbedder, SentenceTransformerEmbedder, create_embedder
from app.intelligence.embeddings.vector_store import (
                                                  MemoryVectorStore,
                                                  PgVectorStore,
                                                  VectorStore,
                                                  build_documents,
                                                  create_vector_store,
)

__all__ = ["Embedder", "HashingEmbedder", "SentenceTransformerEmbedder",
           "create_embedder", "MemoryVectorStore", "PgVectorStore",
           "VectorStore", "build_documents", "create_vector_store"]

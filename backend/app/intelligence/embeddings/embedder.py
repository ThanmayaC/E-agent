"""Embedding layer.

Uses Sentence Transformers when installed/configured; otherwise a
deterministic feature-hashing embedder so the platform runs anywhere with
zero model downloads. Both implement the same protocol (interchangeable).
"""
from __future__ import annotations

import hashlib
import math
import re
from typing import Protocol

from app.core.logging import get_logger

logger = get_logger(__name__)


class Embedder(Protocol):
    dim: int

    def embed(self, texts: list[str]) -> list[list[float]]: ...


class HashingEmbedder:
    """Deterministic char-trigram + word feature hashing with L2 norm.

    Not semantic like a transformer, but stable, dependency-free, and good
    enough for schema/KPI similarity where vocabulary overlap dominates.
    """

    def __init__(self, dim: int = 256):
        self.dim = dim

    def embed(self, texts: list[str]) -> list[list[float]]:
        return [self._one(t) for t in texts]

    def _one(self, text: str) -> list[float]:
        vec = [0.0] * self.dim
        tokens = re.findall(r"[a-z0-9]+", text.lower())
        features = list(tokens)
        joined = " ".join(tokens)
        features += [joined[i:i + 3] for i in range(len(joined) - 2)]
        for f in features:
            h = int(hashlib.md5(f.encode()).hexdigest(), 16)
            idx = h % self.dim
            sign = 1.0 if (h >> 16) % 2 == 0 else -1.0
            vec[idx] += sign
        norm = math.sqrt(sum(v * v for v in vec)) or 1.0
        return [v / norm for v in vec]


class SentenceTransformerEmbedder:
    def __init__(self, model_name: str):
        from sentence_transformers import SentenceTransformer  # optional dependency

        self._model = SentenceTransformer(model_name)
        self.dim = self._model.get_sentence_embedding_dimension()

    def embed(self, texts: list[str]) -> list[list[float]]:
        return self._model.encode(texts, normalize_embeddings=True).tolist()


def create_embedder(model: str, dim: int) -> Embedder:
    if model and model != "hash":
        try:
            return SentenceTransformerEmbedder(model)
        except Exception as exc:
            logger.warning("Falling back to hashing embedder (%s)", exc)
    return HashingEmbedder(dim=dim)

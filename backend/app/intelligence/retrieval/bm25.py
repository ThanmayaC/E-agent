"""BM25 Okapi lexical index — dependency-free.

Dense embeddings miss exact terms (bank names, incident ids like INC-2026-14,
KPI names, decline codes). BM25 scores documents by term frequency / inverse
document frequency and is the sparse half of the hybrid retriever. Pure Python,
no external dependency, deterministic — it rebuilds in milliseconds over the
corpus sizes this platform handles (thousands of chunks).
"""
from __future__ import annotations

import math
import re
from collections import Counter

_TOKEN_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def tokenize(text: str) -> list[str]:
    """Lowercase word/id tokens, keeping hyphenated ids (inc-2026-14, u30)."""
    return _TOKEN_RE.findall((text or "").lower())


class BM25Index:
    """Okapi BM25 over a fixed set of documents.

    ``k1`` controls term-frequency saturation, ``b`` the length normalization —
    the standard defaults (1.5 / 0.75) are used and exposed for tuning.
    """

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self._ids: list[str] = []
        self._docs_tokens: list[list[str]] = []
        self._doc_freqs: list[Counter] = []
        self._doc_len: list[int] = []
        self._df: Counter = Counter()          # term -> #docs containing it
        self._idf: dict[str, float] = {}
        self._avgdl: float = 0.0

    def add(self, doc_id: str, text: str) -> None:
        tokens = tokenize(text)
        self._ids.append(doc_id)
        self._docs_tokens.append(tokens)
        freqs = Counter(tokens)
        self._doc_freqs.append(freqs)
        self._doc_len.append(len(tokens))
        for term in freqs:
            self._df[term] += 1

    def build(self) -> "BM25Index":
        """Finalize IDF and average document length after all documents added."""
        n = len(self._ids)
        self._avgdl = (sum(self._doc_len) / n) if n else 0.0
        # BM25+ style idf with a floor so common terms never go negative.
        for term, df in self._df.items():
            self._idf[term] = math.log(1 + (n - df + 0.5) / (df + 0.5))
        return self

    def search(self, query: str, top_k: int = 20) -> list[tuple[str, float]]:
        """Return ``[(doc_id, score), ...]`` ranked by BM25, best first."""
        if not self._ids:
            return []
        q_terms = tokenize(query)
        scores: list[tuple[str, float]] = []
        for idx, doc_id in enumerate(self._ids):
            freqs = self._doc_freqs[idx]
            dl = self._doc_len[idx] or 1
            score = 0.0
            for term in q_terms:
                tf = freqs.get(term, 0)
                if not tf:
                    continue
                idf = self._idf.get(term, 0.0)
                denom = tf + self.k1 * (1 - self.b + self.b * dl / (self._avgdl or 1))
                score += idf * (tf * (self.k1 + 1)) / denom
            if score > 0:
                scores.append((doc_id, score))
        scores.sort(key=lambda t: t[1], reverse=True)
        return scores[:top_k]

    def stats(self) -> dict:
        return {"documents": len(self._ids), "vocabulary": len(self._df),
                "avg_doc_len": round(self._avgdl, 1)}

"""Vector store abstraction: in-memory (default, JSON-persisted) or pgvector."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Protocol

from app.core.logging import get_logger

logger = get_logger(__name__)


class VectorStore(Protocol):
    def upsert(self, ids: list[str], vectors: list[list[float]], payloads: list[dict]) -> None: ...
    def search(self, vector: list[float], top_k: int = 8, kind: str | None = None) -> list[dict]: ...
    def persist(self) -> None: ...


class MemoryVectorStore:
    """Cosine-similarity store persisted as JSON alongside project artifacts."""

    def __init__(self, path: Path):
        self.path = path
        self._ids: list[str] = []
        self._vectors: list[list[float]] = []
        self._payloads: list[dict] = []
        if path.exists():
            data = json.loads(path.read_text(encoding="utf-8"))
            self._ids, self._vectors, self._payloads = data["ids"], data["vectors"], data["payloads"]

    def upsert(self, ids: list[str], vectors: list[list[float]], payloads: list[dict]) -> None:
        existing = {i: n for n, i in enumerate(self._ids)}
        for i, v, p in zip(ids, vectors, payloads):
            if i in existing:
                n = existing[i]
                self._vectors[n], self._payloads[n] = v, p
            else:
                self._ids.append(i)
                self._vectors.append(v)
                self._payloads.append(p)

    def search(self, vector: list[float], top_k: int = 8, kind: str | None = None) -> list[dict]:
        scored: list[tuple[float, dict]] = []
        for i, v, p in zip(self._ids, self._vectors, self._payloads):
            if kind and p.get("kind") != kind:
                continue
            score = sum(a * b for a, b in zip(vector, v))
            scored.append((score, {"id": i, "score": round(score, 4), **p}))
        scored.sort(key=lambda t: t[0], reverse=True)
        return [p for _, p in scored[:top_k]]

    def persist(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(
            {"ids": self._ids, "vectors": self._vectors, "payloads": self._payloads}
        ), encoding="utf-8")


class PgVectorStore:
    """pgvector-backed store. Requires EDIP_PGVECTOR_URL and the pgvector extension."""

    def __init__(self, url: str, dim: int, collection: str):
        import sqlalchemy as sa

        self._sa = sa
        self._engine = sa.create_engine(url)
        self._table = f"embeddings_{collection}"
        with self._engine.begin() as conn:
            conn.execute(sa.text("CREATE EXTENSION IF NOT EXISTS vector"))
            conn.execute(sa.text(
                f"CREATE TABLE IF NOT EXISTS {self._table} "
                f"(id TEXT PRIMARY KEY, embedding vector({dim}), payload JSONB)"
            ))

    def upsert(self, ids: list[str], vectors: list[list[float]], payloads: list[dict]) -> None:
        sa = self._sa
        with self._engine.begin() as conn:
            for i, v, p in zip(ids, vectors, payloads):
                conn.execute(sa.text(
                    f"INSERT INTO {self._table} (id, embedding, payload) "
                    "VALUES (:id, :emb, CAST(:payload AS JSONB)) "
                    "ON CONFLICT (id) DO UPDATE SET embedding = :emb, payload = CAST(:payload AS JSONB)"
                ), {"id": i, "emb": str(v), "payload": json.dumps(p)})

    def search(self, vector: list[float], top_k: int = 8, kind: str | None = None) -> list[dict]:
        sa = self._sa
        where = "WHERE payload->>'kind' = :kind" if kind else ""
        with self._engine.begin() as conn:
            rows = conn.execute(sa.text(
                f"SELECT id, payload, 1 - (embedding <=> CAST(:v AS vector)) AS score "
                f"FROM {self._table} {where} ORDER BY embedding <=> CAST(:v AS vector) LIMIT :k"
            ), {"v": str(vector), "k": top_k, **({"kind": kind} if kind else {})}).fetchall()
        return [{"id": r[0], "score": round(float(r[2]), 4), **(r[1] or {})} for r in rows]

    def persist(self) -> None:  # pgvector persists transactionally
        pass


def create_vector_store(backend: str, *, path: Path, pg_url: str = "", dim: int = 256,
                        collection: str = "default") -> VectorStore:
    if backend == "pgvector" and pg_url:
        try:
            return PgVectorStore(pg_url, dim, collection)
        except Exception as exc:
            logger.warning("pgvector unavailable, using memory store (%s)", exc)
    return MemoryVectorStore(path)


def build_documents(profiles, mappings, kpis, signals, relationships) -> list[dict[str, Any]]:
    """Flatten every artifact into embeddable documents for semantic search."""
    docs: list[dict[str, Any]] = []
    for p in profiles:
        docs.append({"id": f"ds:{p.dataset_id}", "kind": "dataset",
                     "text": f"Dataset {p.name}. {p.description}. Columns: "
                             + ", ".join(c.name for c in p.columns),
                     "ref": p.dataset_id, "title": p.name})
        for c in p.columns:
            docs.append({"id": f"col:{p.dataset_id}.{c.name}", "kind": "column",
                         "text": f"Column {c.name} in {p.name}: {c.semantic_type.value}, "
                                 f"concept {c.concept.value}, role {c.role.value}",
                         "ref": p.dataset_id, "title": c.name})
    for k in kpis:
        docs.append({"id": f"kpi:{k.id}", "kind": "kpi",
                     "text": f"KPI {k.name}: {k.expression}, current {k.current_value}, "
                             f"growth {k.growth_pct}%, trend {k.trend}",
                     "ref": k.id, "title": k.name})
    for s in signals:
        stats = ", ".join(f"{k}={v}" for k, v in s.stats.items())
        docs.append({"id": f"signal:{s.id}", "kind": "signal",
                     "text": f"Signal {s.kind.value} on {s.kpi_name or s.dataset_id}: {stats}",
                     "ref": s.id, "title": f"{s.kind.value}: {s.kpi_name or ''}"})
    for r in relationships:
        docs.append({"id": f"rel:{r.id}", "kind": "relationship",
                     "text": f"{r.from_dataset}.{r.from_column} relates to "
                             f"{r.to_dataset}.{r.to_column} ({r.rel_type.value}). {r.evidence}",
                     "ref": r.id, "title": f"{r.from_dataset} → {r.to_dataset}"})
    return docs

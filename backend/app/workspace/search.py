"""Unified enterprise search (V9.0).

One query, every surface: banks, PSPs, merchants, products, features, KPIs,
reports, decisions, meetings, uploaded files and Knowledge-Graph nodes. It is a
thin federation over intelligence the platform already holds — the ecosystem /
evolution / executive layers, the Enterprise Knowledge Graph and the workspace
file store — ranked by match quality. Every result carries a type, a title, a
snippet and a link target the frontend can route to.
"""
from __future__ import annotations

from app.core.logging import get_logger
from app.intelligence.retrieval import HybridRetriever

logger = get_logger(__name__)


def _score(query: str, text: str) -> float:
    q, t = query.lower().strip(), (text or "").lower()
    if not q or not t:
        return 0.0
    if q == t:
        return 1.0
    if t.startswith(q):
        return 0.9
    if q in t:
        return 0.7
    # token overlap
    qt, tt = set(q.split()), set(t.split())
    if qt & tt:
        return 0.4 * len(qt & tt) / len(qt)
    return 0.0


class EnterpriseSearch:
    """Federated read-only search across every enterprise surface."""

    def __init__(self, container):
        self._c = container

    def search(self, query: str, limit: int = 40) -> dict:
        query = (query or "").strip()
        if not query:
            return {"query": query, "results": [], "groups": {}, "total": 0}
        candidates: list[dict] = []
        for collector in (self._entities, self._kpis, self._reports_decisions,
                          self._files, self._graph):
            try:
                candidates.extend(collector(query))
            except Exception:  # noqa: BLE001 — one bad source never fails search
                logger.exception("enterprise search collector failed")

        results, retrieval = self._hybrid_rank(query, candidates, limit)
        groups: dict[str, list] = {}
        for r in results:
            groups.setdefault(r["type"], []).append(r)
        return {"query": query, "results": results, "groups": groups,
                "total": len(results), "retrieval": retrieval,
                "counts": {k: len(v) for k, v in groups.items()}}

    def _hybrid_rank(self, query: str, candidates: list[dict],
                     limit: int) -> tuple[list[dict], dict]:
        """Rank federated candidates with BM25 lexical + the collectors' own
        semantic score, fused via Reciprocal Rank Fusion and reranked. Returns
        the ranked hits and retrieval diagnostics. Falls back to the plain score
        ordering if anything goes wrong — search must never fail."""
        if not candidates:
            return [], {"strategy": "none", "candidates": 0}
        try:
            docs = [{"id": f"h{i}",
                     "text": f"{c.get('title','')} {c.get('snippet','')}".strip(),
                     "title": c.get("title", ""), "_hit": c}
                    for i, c in enumerate(candidates)]
            # The collectors' own score is the "dense"/semantic signal.
            ordered = sorted(docs, key=lambda d: d["_hit"].get("score", 0.0),
                             reverse=True)

            def dense(_q: str, k: int) -> list[dict]:
                return [{"id": d["id"], "score": d["_hit"].get("score", 0.0)}
                        for d in ordered[:k]]

            retriever = HybridRetriever.from_documents(docs, dense_search=dense)
            ranked, diag = retriever.retrieve(query, top_k=limit,
                                              dense_k=len(docs), bm25_k=len(docs))
            hits = []
            for c in ranked:
                hit = dict(c.payload.get("_hit", {}))
                hit["retrieval_score"] = round(c.rerank_score
                                               if c.rerank_score is not None
                                               else c.fused_score, 4)
                hits.append(hit)
            diag["strategy"] = "hybrid_bm25_dense_rrf_rerank"
            return hits, diag
        except Exception:  # noqa: BLE001 — never fail search on ranking
            logger.exception("hybrid ranking failed; using score fallback")
            fallback = sorted(candidates, key=lambda r: r.get("score", 0),
                              reverse=True)[:limit]
            return fallback, {"strategy": "score_fallback",
                              "candidates": len(candidates)}

    # ------------------------------------------------------------ sources
    def _entities(self, q: str) -> list[dict]:
        out: list[dict] = []
        eco = getattr(self._c, "ecosystem", None)
        evo = getattr(self._c, "evolution", None)
        if eco and eco.available:
            for r in eco.compare_banks():
                out.append(self._hit(q, "bank", r["name"],
                                     f"Share {r.get('share_pct')}% · success "
                                     f"{r.get('avg_success_rate')}%", "/ecosystem"))
            for r in eco.compare_psps():
                out.append(self._hit(q, "psp", r["name"],
                                     f"Share {r.get('share_pct')}%", "/ecosystem"))
            for r in eco.compare_features():
                out.append(self._hit(q, "feature", r["name"],
                                     f"{r.get('txns')} txns · {r.get('growth_pct')}% m/m",
                                     "/products"))
        if evo and evo.available:
            m = evo.merchants()
            for r in m.get("merchants", []):
                out.append(self._hit(q, "merchant", r["merchant"],
                                     f"{r.get('category','')} · health "
                                     f"{r.get('health_score')} · {r.get('status')}",
                                     "/evolution"))
            for r in evo.products().get("products", []):
                out.append(self._hit(q, "product", r["product"],
                                     f"{r.get('lifecycle_stage')} · share "
                                     f"{r.get('market_share_pct')}%", "/evolution"))
        return [r for r in out if r["score"] > 0]

    def _kpis(self, q: str) -> list[dict]:
        eco = getattr(self._c, "ecosystem", None)
        if not (eco and eco.available):
            return []
        out = []
        for t in eco.ecosystem().trends:
            series = str(t.get("series", ""))
            if series.startswith("total::"):
                name = series.split("::", 1)[1]
                out.append(self._hit(q, "kpi", name,
                                     f"today {t.get('today')} · {t.get('growth_pct')}% growth",
                                     "/ecosystem"))
        return [r for r in out if r["score"] > 0]

    def _reports_decisions(self, q: str) -> list[dict]:
        out: list[dict] = []
        ex = getattr(self._c, "executive", None)
        if ex and getattr(ex, "available", False):
            try:
                for r in ex.reports():
                    out.append(self._hit(q, "report",
                                         r.get("title", r.get("report_id", "")),
                                         r.get("category", ""), "/reports"))
            except Exception:  # noqa: BLE001
                pass
        evo = getattr(self._c, "evolution", None)
        if evo and evo.available:
            for d in evo.decisions().get("decisions", []):
                out.append(self._hit(q, "decision",
                                     f"{d.get('decision_id')} — {d.get('title')}",
                                     f"₹{d.get('business_value_cr')}cr · {d.get('status')}",
                                     "/evolution"))
        return [r for r in out if r["score"] > 0]

    def _files(self, q: str) -> list[dict]:
        ws = getattr(self._c, "workspace", None)
        if not ws:
            return []
        out = []
        for f in ws.list_files():
            title = f.get("file", "")
            tags = " ".join(f.get("tags", []))
            score = max(_score(q, title), 0.6 * _score(q, tags),
                        0.5 * _score(q, f.get("summary", "")))
            if score > 0:
                out.append({"type": "file", "title": title,
                            "snippet": f.get("summary", "")[:140],
                            "score": score, "link": "/files",
                            "ref": f.get("id")})
        return out

    def _graph(self, q: str) -> list[dict]:
        graph = getattr(self._c, "enterprise_graph", None)
        if not graph:
            return []
        out = []
        try:
            nodes = graph.nodes() if hasattr(graph, "nodes") else []
            for n in list(nodes)[:5000]:
                label = n.get("label") if isinstance(n, dict) else str(n)
                kind = n.get("type", "node") if isinstance(n, dict) else "node"
                s = _score(q, label or "")
                if s > 0.5:
                    out.append({"type": f"graph:{kind}", "title": label,
                                "snippet": kind, "score": 0.6 * s,
                                "link": "/admin/graph"})
        except Exception:  # noqa: BLE001
            return []
        return out[:20]

    @staticmethod
    def _hit(q, typ, title, snippet, link) -> dict:
        return {"type": typ, "title": title, "snippet": snippet,
                "score": _score(q, title or ""), "link": link}

"""Enterprise Knowledge Graph — the organization-wide, persistent graph.

The per-project graph (``KnowledgeGraphBuilder``) is rebuilt from scratch on
every analysis; this graph is the opposite: it accumulates. Every successful
run merges its project graph into the enterprise graph, and every knowledge
event (terms, rules, decisions, reports, recommendations, clarifications)
becomes a node linked to the entities it concerns — so relationships between
entities, metrics, KPIs, products, merchants, customers, regions, documents,
reports, business rules, recommendations, decisions, and historical events
grow across projects and over time.

Persistence is node-link JSON under ``data/knowledge`` (same profile as the
KnowledgeStore). When ``EDIP_NEO4J_URI`` is configured and the ``neo4j``
driver is installed, every sync mirrors the graph into Neo4j so knowledge is
queryable through Cypher; without it the NetworkX graph remains the store and
the query API is served from it directly.
"""
from __future__ import annotations

import json
import threading
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

import networkx as nx

from app.core.logging import get_logger

logger = get_logger(__name__)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


class EnterpriseKnowledgeGraph:
    """Persistent, continuously growing organizational knowledge graph."""

    def __init__(self, knowledge_dir: Path, neo4j_uri: str = "",
                 neo4j_user: str = "", neo4j_password: str = ""):
        self._path = knowledge_dir / "enterprise_graph.json"
        self._lock = threading.RLock()
        self._suspend_save = False
        self._graph = self._load()
        self._neo4j = _Neo4jMirror(neo4j_uri, neo4j_user, neo4j_password) \
            if neo4j_uri else None

    # ------------------------------------------------------- persistence
    def _load(self) -> nx.MultiDiGraph:
        if not self._path.exists():
            return nx.MultiDiGraph()
        try:
            payload = json.loads(self._path.read_text(encoding="utf-8"))
            g = nx.MultiDiGraph()
            for n in payload.get("nodes", []):
                g.add_node(n.pop("id"), **n)
            for e in payload.get("edges", []):
                g.add_edge(e.pop("source"), e.pop("target"),
                           **{k: v for k, v in e.items() if k != "id"})
            return g
        except Exception:  # corrupt file must never take the platform down
            logger.exception("Enterprise graph unreadable — starting empty")
            return nx.MultiDiGraph()

    def _save(self) -> None:
        if self._suspend_save:
            return
        self._path.write_text(
            json.dumps(self.payload(limit=0), ensure_ascii=False, default=str),
            encoding="utf-8")
        if self._neo4j:
            self._neo4j.mirror(self._graph)

    @contextmanager
    def batch(self):
        """Group many mutations into one lock/save (one file write, one
        Neo4j mirror) — used by the continuous learning pipeline."""
        with self._lock:
            previous = self._suspend_save
            self._suspend_save = True
            try:
                yield self
            finally:
                self._suspend_save = previous
                self._save()

    # ------------------------------------------------------------ growth
    def upsert_node(self, node_id: str, kind: str, label: str = "",
                    project_id: str = "", **attrs) -> None:
        """Add or enrich a node. Existing knowledge is merged, never lost:
        first_seen is preserved, the project provenance list grows."""
        with self._lock:
            self._upsert_node(node_id, kind, label, project_id, **attrs)
            self._save()

    def _upsert_node(self, node_id: str, kind: str, label: str = "",
                     project_id: str = "", **attrs) -> None:
        existing = self._graph.nodes.get(node_id)
        if existing is None:
            self._graph.add_node(node_id, kind=kind, label=label or node_id,
                                 first_seen=_now(), last_seen=_now(),
                                 projects=[project_id] if project_id else [],
                                 **attrs)
            return
        existing["last_seen"] = _now()
        if project_id and project_id not in existing.get("projects", []):
            existing.setdefault("projects", []).append(project_id)
        for k, v in attrs.items():
            if v is not None:
                existing[k] = v
        if label:
            existing["label"] = label

    def relate(self, source: str, target: str, kind: str,
               project_id: str = "", **attrs) -> None:
        """Create a relationship if an equivalent one does not already exist."""
        with self._lock:
            self._relate(source, target, kind, project_id, **attrs)
            self._save()

    def _relate(self, source: str, target: str, kind: str,
                project_id: str = "", **attrs) -> None:
        for node in (source, target):
            if node not in self._graph:
                self._upsert_node(node, kind="concept", project_id=project_id)
        existing = self._graph.get_edge_data(source, target) or {}
        for data in existing.values():
            if data.get("kind") == kind:
                data["last_seen"] = _now()
                if project_id and project_id not in data.get("projects", []):
                    data.setdefault("projects", []).append(project_id)
                return
        self._graph.add_edge(source, target, kind=kind, first_seen=_now(),
                             last_seen=_now(),
                             projects=[project_id] if project_id else [],
                             **attrs)

    def merge_project_graph(self, project_id: str, payload: dict) -> dict:
        """Merge one project's analysis graph (KnowledgeGraphBuilder payload)
        into the enterprise graph. Project node ids are namespaced so datasets
        from different projects never collide; shared business concepts
        (``concept:*``) intentionally converge into single enterprise nodes —
        that convergence is what links projects together."""
        added_nodes = added_edges = 0
        with self._lock:
            def qualify(node_id: str) -> str:
                return node_id if node_id.startswith("concept:") \
                    else f"{project_id}:{node_id}"

            for n in payload.get("nodes", []):
                node = dict(n)
                node_id = qualify(node.pop("id"))
                if node_id not in self._graph:
                    added_nodes += 1
                self._upsert_node(node_id, kind=node.pop("kind", "unknown"),
                                  label=node.pop("label", ""),
                                  project_id=project_id, **node)
            for e in payload.get("edges", []):
                edge = dict(e)
                edge.pop("id", None)
                src, dst = qualify(edge.pop("source")), qualify(edge.pop("target"))
                before = self._graph.number_of_edges()
                self._relate(src, dst, edge.pop("kind", "related"),
                             project_id=project_id, **edge)
                added_edges += self._graph.number_of_edges() - before
            self._save()
        return {"nodes_added": added_nodes, "edges_added": added_edges}

    # ------------------------------------------------------------ queries
    def related_projects(self, project_id: str) -> list[str]:
        """Other projects that share at least one enterprise concept with
        this one — the cross-project links that make knowledge organizational
        rather than per-project."""
        related: set[str] = set()
        with self._lock:
            for node_id, data in self._graph.nodes(data=True):
                if not node_id.startswith("concept:"):
                    continue
                projects = data.get("projects", [])
                if project_id in projects:
                    related.update(p for p in projects
                                   if p and p != project_id)
        return sorted(related)

    def find(self, query: str, limit: int = 25) -> list[dict]:
        needle = query.strip().lower()
        hits = []
        for node_id, data in self._graph.nodes(data=True):
            text = f"{node_id} {data.get('label', '')}".lower()
            if needle in text:
                hits.append({"id": node_id, **data})
                if len(hits) >= limit:
                    break
        return hits

    def neighbors(self, node_id: str) -> dict:
        if node_id not in self._graph:
            return {"node": None, "relations": []}
        relations = []
        for _, dst, data in self._graph.out_edges(node_id, data=True):
            relations.append({"direction": "out", "kind": data.get("kind"),
                              "node": {"id": dst, **self._graph.nodes[dst]}})
        for src, _, data in self._graph.in_edges(node_id, data=True):
            relations.append({"direction": "in", "kind": data.get("kind"),
                              "node": {"id": src, **self._graph.nodes[src]}})
        return {"node": {"id": node_id, **self._graph.nodes[node_id]},
                "relations": relations}

    def relations(self, kind: str = "", limit: int = 200) -> list[dict]:
        out = []
        for src, dst, data in self._graph.edges(data=True):
            if kind and data.get("kind") != kind:
                continue
            out.append({"source": src, "target": dst, **data})
            if len(out) >= limit:
                break
        return out

    def payload(self, limit: int = 500) -> dict:
        """Node-link JSON (same shape as the project graph explorer)."""
        nodes = [{"id": n, **d} for n, d in self._graph.nodes(data=True)]
        edges = [{"id": f"e{i}", "source": u, "target": v, **d}
                 for i, (u, v, d) in enumerate(self._graph.edges(data=True))]
        if limit:
            nodes, edges = nodes[:limit], edges[: limit * 2]
        return {"nodes": nodes, "edges": edges, "stats": self.stats()}

    def stats(self) -> dict:
        kinds: dict[str, int] = {}
        for _, d in self._graph.nodes(data=True):
            kinds[d.get("kind", "unknown")] = kinds.get(d.get("kind", "unknown"), 0) + 1
        return {"node_count": self._graph.number_of_nodes(),
                "edge_count": self._graph.number_of_edges(),
                "node_kinds": kinds,
                "neo4j": self._neo4j.status if self._neo4j else "not_configured"}


class _Neo4jMirror:
    """Best-effort Neo4j mirror: MERGE every node and relationship so the
    enterprise graph is queryable through Cypher. Failures degrade to the
    local graph — they never break learning."""

    def __init__(self, uri: str, user: str, password: str):
        self.status = "configured"
        self._driver = None
        try:
            from neo4j import GraphDatabase  # optional dependency
            self._driver = GraphDatabase.driver(uri, auth=(user, password))
            self.status = "connected"
        except ImportError:
            self.status = "driver_missing"
            logger.warning("EDIP_NEO4J_URI set but the neo4j driver is not "
                           "installed (pip install neo4j) — local graph only")
        except Exception as exc:  # noqa: BLE001 — availability is optional
            self.status = f"unreachable: {str(exc)[:120]}"
            logger.warning("Neo4j unreachable (%s) — local graph only", exc)

    def mirror(self, graph: nx.MultiDiGraph) -> None:
        if self._driver is None:
            return
        try:
            with self._driver.session() as session:
                for node_id, data in graph.nodes(data=True):
                    session.run(
                        "MERGE (n:Knowledge {id: $id}) "
                        "SET n.kind = $kind, n.label = $label",
                        id=node_id, kind=data.get("kind", ""),
                        label=str(data.get("label", "")))
                for src, dst, data in graph.edges(data=True):
                    session.run(
                        "MATCH (a:Knowledge {id: $src}), (b:Knowledge {id: $dst}) "
                        "MERGE (a)-[r:RELATES {kind: $kind}]->(b)",
                        src=src, dst=dst, kind=data.get("kind", ""))
        except Exception as exc:  # noqa: BLE001
            self.status = f"sync_failed: {str(exc)[:120]}"
            logger.warning("Neo4j mirror failed (%s) — local graph remains "
                           "authoritative", exc)

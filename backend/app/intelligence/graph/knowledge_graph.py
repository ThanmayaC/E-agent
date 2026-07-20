"""AI knowledge graph built with NetworkX.

Nodes: datasets, columns, business concepts, KPIs, insights.
Edges: contains, maps_to, joins, measures, derived_from, about.
Exported as node-link JSON for the React Flow explorer.
"""
from __future__ import annotations

import networkx as nx

from app.domain.entities import KPI, AnalyticsSignal, Relationship, TableProfile
from app.domain.enums import BusinessConcept


class KnowledgeGraphBuilder:
    def build(
        self,
        profiles: list[TableProfile],
        relationships: list[Relationship],
        kpis: list[KPI],
        signals: list[AnalyticsSignal],
    ) -> nx.MultiDiGraph:
        g = nx.MultiDiGraph()

        for p in profiles:
            g.add_node(f"ds:{p.dataset_id}", kind="dataset", label=p.name,
                       rows=p.row_count, entity=p.entity.value,
                       is_fact=p.is_fact, description=p.description)
            if p.entity is not BusinessConcept.UNKNOWN:
                cid = f"concept:{p.entity.value}"
                g.add_node(cid, kind="concept", label=p.entity.value)
                g.add_edge(f"ds:{p.dataset_id}", cid, kind="about")
            for c in p.columns:
                col_id = f"col:{p.dataset_id}.{c.name}"
                g.add_node(col_id, kind="column", label=c.name,
                           semantic_type=c.semantic_type.value, role=c.role.value)
                g.add_edge(f"ds:{p.dataset_id}", col_id, kind="contains")
                if c.concept is not BusinessConcept.UNKNOWN:
                    cid = f"concept:{c.concept.value}"
                    g.add_node(cid, kind="concept", label=c.concept.value)
                    g.add_edge(col_id, cid, kind="maps_to", confidence=c.concept_confidence)

        for r in relationships:
            g.add_edge(
                f"ds:{r.from_dataset}", f"ds:{r.to_dataset}", kind="joins",
                label=f"{r.from_column} → {r.to_column}", rel_type=r.rel_type.value,
                cardinality=r.cardinality.value, confidence=r.confidence,
            )

        for k in kpis:
            kid = f"kpi:{k.id}"
            g.add_node(kid, kind="kpi", label=k.name, value=k.current_value,
                       growth=k.growth_pct, trend=k.trend)
            g.add_edge(kid, f"ds:{k.dataset_id}", kind="measured_from")
            if k.concept is not BusinessConcept.UNKNOWN:
                cid = f"concept:{k.concept.value}"
                g.add_node(cid, kind="concept", label=k.concept.value)
                g.add_edge(kid, cid, kind="measures")

        for sig in signals:
            sid = f"signal:{sig.id}"
            label = sig.kind.value + (f" · {sig.kpi_name}" if sig.kpi_name else "")
            g.add_node(sid, kind="signal", label=label,
                       signal_kind=sig.kind.value, strength=sig.strength,
                       stats=sig.stats)
            if sig.kpi_id:
                g.add_edge(sid, f"kpi:{sig.kpi_id}", kind="derived_from")
            elif sig.dataset_id:
                g.add_edge(sid, f"ds:{sig.dataset_id}", kind="derived_from")
        return g

    @staticmethod
    def to_payload(g: nx.MultiDiGraph) -> dict:
        nodes = [{"id": n, **data} for n, data in g.nodes(data=True)]
        edges = [
            {"id": f"e{i}", "source": u, "target": v, **data}
            for i, (u, v, data) in enumerate(g.edges(data=True))
        ]
        return {
            "nodes": nodes,
            "edges": edges,
            "stats": {
                "node_count": g.number_of_nodes(),
                "edge_count": g.number_of_edges(),
                "concepts": sum(1 for _, d in g.nodes(data=True) if d.get("kind") == "concept"),
                "datasets": sum(1 for _, d in g.nodes(data=True) if d.get("kind") == "dataset"),
            },
        }

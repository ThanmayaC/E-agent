"""Enterprise Knowledge Engine — continuous organizational learning.

The learning half of the Enterprise Brain. After every successful workflow it
ingests what the other SDS modules produced — Observation (datasets), Schema
Intelligence (profiles), Data Intelligence (semantics, relationships),
Analytics (KPIs, signals), Forecasting/ML/Deep Learning (predictions),
Document Intelligence (extracted tables), Report Generation (AI narrative),
plus user clarifications and business rules — and converts it into structured,
versioned enterprise knowledge:

- terminology and KPI definitions        → KnowledgeStore.terminology
- entity definitions                     → KnowledgeStore.entity_definitions
- schema aliases (column → concept)      → KnowledgeStore.schema_aliases
- insights / recommendations / decisions → structured sections
- entities, metrics, documents, reports  → EnterpriseKnowledgeGraph nodes
- every mutation                         → knowledge_versions journal

Learning is merge-based: existing knowledge is compared and enriched, never
overwritten blindly (the store journals every version with source, confidence,
timestamp, and project origin). Running the same extraction twice is a no-op —
knowledge converges instead of duplicating.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.knowledge.graph import EnterpriseKnowledgeGraph
from app.knowledge.store import KnowledgeStore

logger = get_logger(__name__)

SOURCE = "learning_pipeline"

# minimum inference confidence before an automatic mapping is memorized
MIN_LEARN_CONFIDENCE = 0.75


class KnowledgeEngine:
    """Turns module outputs into versioned enterprise knowledge + graph."""

    def __init__(self, store: KnowledgeStore, graph: EnterpriseKnowledgeGraph):
        self.store = store
        self.graph = graph

    # ------------------------------------------------------------ learning
    def learn_from_artifacts(self, project_id: str, project_name: str,
                             artifacts: dict[str, Any]) -> dict[str, int]:
        """Business Knowledge Extraction over one completed workflow.

        ``artifacts`` carries the project's persisted analysis outputs
        (profiles, semantic_layer, relationships, kpis, signals, forecasts,
        business_context, ai_report, understanding) as plain dicts/lists,
        exactly as the ArtifactStore returns them. Missing artifacts are
        skipped — learning degrades, it never fails."""
        counters = {"terms": 0, "entities": 0, "aliases": 0, "kpis": 0,
                    "insights": 0, "recommendations": 0, "rules": 0,
                    "graph_nodes": 0, "graph_edges": 0}
        with self.graph.batch():
            self._learn_project(project_id, project_name, counters)
            self._learn_profiles(project_id, artifacts.get("profiles") or [],
                                 counters)
            self._learn_semantics(project_id,
                                  artifacts.get("semantic_layer") or [],
                                  counters)
            self._learn_kpis(project_id, artifacts.get("kpis") or [], counters)
            self._learn_relationships(project_id,
                                      artifacts.get("relationships") or [],
                                      counters)
            self._learn_report(project_id, artifacts.get("ai_report") or {},
                               counters)
            self._learn_understanding(project_id,
                                      artifacts.get("understanding") or {},
                                      counters)
        return counters

    # --------------------------------------------------------- extractors
    def _learn_project(self, project_id: str, project_name: str,
                       counters: dict) -> None:
        self.graph.upsert_node(f"project:{project_id}", kind="project",
                               label=project_name, project_id=project_id)
        counters["graph_nodes"] += 1

    def _learn_profiles(self, project_id: str, profiles: list[dict],
                        counters: dict) -> None:
        """Datasets become entity definitions and graph nodes; their business
        entity (Customer, Merchant, Product, Region, ...) links them to the
        shared enterprise concept nodes."""
        for p in profiles:
            name, entity = p.get("name", ""), p.get("entity", "Unknown")
            if not name:
                continue
            description = p.get("description") or (
                f"Dataset with {p.get('row_count', 0)} rows and "
                f"{p.get('column_count', 0)} columns")
            self.store.define_entity(
                name, kind="dataset", definition=description, source=SOURCE,
                confidence=p.get("confidence"), project_id=project_id)
            counters["entities"] += 1
            ds_node = f"{project_id}:ds:{p.get('dataset_id', name)}"
            self.graph.upsert_node(ds_node, kind="dataset", label=name,
                                   project_id=project_id,
                                   rows=p.get("row_count"))
            self.graph.relate(f"project:{project_id}", ds_node, "contains",
                              project_id=project_id)
            counters["graph_nodes"] += 1
            counters["graph_edges"] += 1
            if entity and entity != "Unknown":
                concept = f"concept:{entity}"
                self.graph.upsert_node(concept, kind="concept", label=entity,
                                       project_id=project_id)
                self.graph.relate(ds_node, concept, "about",
                                  project_id=project_id)
                counters["graph_edges"] += 1

    def _learn_semantics(self, project_id: str, mappings: list[dict],
                         counters: dict) -> None:
        """High-confidence column→concept mappings become permanent schema
        aliases, so the next dataset with the same column names is understood
        immediately (confidence improves run over run)."""
        for m in mappings:
            column = m.get("column", "")
            canonical = m.get("canonical_name") or m.get("concept", "")
            confidence = float(m.get("confidence") or 0.0)
            if not column or not canonical or canonical == "Unknown":
                continue
            if confidence < MIN_LEARN_CONFIDENCE:
                continue
            if self.store.resolve_schema_alias(column):
                continue  # already known — user-taught aliases always win
            self.store.add_schema_alias(column, canonical, source=SOURCE,
                                        confidence=confidence,
                                        project_id=project_id)
            counters["aliases"] += 1

    def _learn_kpis(self, project_id: str, kpis: list[dict],
                    counters: dict) -> None:
        """Discovered KPIs become enterprise terminology and graph metrics."""
        for k in kpis:
            name, expression = k.get("name", ""), k.get("expression", "")
            if not name:
                continue
            self.store.add_term(
                name,
                definition=f"KPI defined as {expression or 'a measured value'}"
                           + (f" ({k['unit']})" if k.get("unit") else ""),
                added_by=SOURCE, confidence=k.get("confidence"),
                project_id=project_id)
            counters["terms"] += 1
            counters["kpis"] += 1
            kpi_node = f"kpi:{name.strip().lower()}"
            self.graph.upsert_node(kpi_node, kind="kpi", label=name,
                                   project_id=project_id,
                                   expression=expression)
            self.graph.relate(f"project:{project_id}", kpi_node, "measures",
                              project_id=project_id)
            counters["graph_nodes"] += 1
            counters["graph_edges"] += 1
            concept = k.get("concept", "Unknown")
            if concept and concept != "Unknown":
                self.graph.relate(kpi_node, f"concept:{concept}", "about",
                                  project_id=project_id)
                counters["graph_edges"] += 1

    def _learn_relationships(self, project_id: str, relationships: list[dict],
                             counters: dict) -> None:
        for r in relationships:
            src = f"{project_id}:ds:{r.get('from_dataset', '')}"
            dst = f"{project_id}:ds:{r.get('to_dataset', '')}"
            self.graph.relate(src, dst, kind="joins", project_id=project_id,
                              label=f"{r.get('from_column')} → {r.get('to_column')}",
                              confidence=r.get("confidence"))
            counters["graph_edges"] += 1

    def _learn_report(self, project_id: str, ai_report: dict,
                      counters: dict) -> None:
        """Verified insights, recommendations, and priority actions from the
        executive report become structured, queryable knowledge."""
        if ai_report.get("status") != "ok":
            return
        report_node = f"report:{project_id}"
        self.graph.upsert_node(report_node, kind="report",
                               label=f"Executive report — {project_id}",
                               project_id=project_id)
        self.graph.relate(f"project:{project_id}", report_node, "produced",
                          project_id=project_id)
        counters["graph_nodes"] += 1
        counters["graph_edges"] += 1
        for item in ai_report.get("key_insights") or []:
            if not isinstance(item, dict):
                continue
            text = str(item.get("title") or item.get("detail") or "").strip()
            if not text or item.get("verification") != "evidence_verified":
                continue  # only evidence-verified statements become knowledge
            self.store.record_insight(
                text, statement_type=str(item.get("statement_type", "")),
                project_id=project_id,
                confidence=_as_float(item.get("confidence")),
                evidence_ids=[str(e) for e in item.get("evidence_ids") or []])
            counters["insights"] += 1
            node = f"insight:{text[:60].strip().lower()}"
            self.graph.upsert_node(node, kind="insight", label=text[:120],
                                   project_id=project_id)
            self.graph.relate(report_node, node, "states",
                              project_id=project_id)
            counters["graph_nodes"] += 1
            counters["graph_edges"] += 1
        for item in ai_report.get("recommendations") or []:
            if not isinstance(item, dict):
                continue
            action = str(item.get("action", "")).strip()
            if not action:
                continue
            self.store.record_recommendation(
                action, priority=_as_int(item.get("priority")),
                project_id=project_id,
                evidence_ids=[str(e) for e in item.get("evidence_ids") or []])
            counters["recommendations"] += 1
            node = f"recommendation:{action[:60].strip().lower()}"
            self.graph.upsert_node(node, kind="recommendation",
                                   label=action[:120], project_id=project_id)
            self.graph.relate(report_node, node, "recommends",
                              project_id=project_id)
            counters["graph_nodes"] += 1
            counters["graph_edges"] += 1
        for action in (ai_report.get("priority_actions") or [])[:5]:
            text = str(action).strip()
            if text:
                self.store.record_decision(
                    f"Priority action: {text}", context="executive report",
                    project_id=project_id, source=SOURCE)

    def _learn_understanding(self, project_id: str, understanding: dict,
                             counters: dict) -> None:
        """Clarification learning: answered questions are already stored
        org-wide by the gate; here their aliases link into the graph so the
        learned mapping is visible as a relationship."""
        for q in understanding.get("questions") or []:
            if not isinstance(q, dict) or not q.get("answered"):
                continue
            answer = str(q.get("answer", "")).strip()
            if not answer:
                continue
            node = f"clarification:{(q.get('signature') or answer)[:60].lower()}"
            self.graph.upsert_node(node, kind="clarification",
                                   label=str(q.get("question", ""))[:120],
                                   project_id=project_id, answer=answer[:200])
            self.graph.relate(f"project:{project_id}", node, "clarified_by",
                              project_id=project_id)
            counters["graph_nodes"] += 1
            counters["graph_edges"] += 1

    # ------------------------------------------------------------- status
    def stats(self) -> dict[str, Any]:
        return {"knowledge": self.store.stats(), "graph": self.graph.stats()}


def _as_float(v: Any) -> float | None:
    try:
        return float(v) if v is not None else None
    except (TypeError, ValueError):
        return None


def _as_int(v: Any) -> int | None:
    try:
        return int(v) if v is not None else None
    except (TypeError, ValueError):
        return None

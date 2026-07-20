"""Knowledge Module (SDS §2.5).

Organization-wide learning that outlives any single project:
- ``KnowledgeStore``           — versioned terminology, schema aliases,
  entity definitions, business rules, clarifications, decisions, report
  history, insights, recommendations (every mutation journaled).
- ``KnowledgeEngine``          — the Enterprise Brain's learning engine:
  converts module outputs into merged, versioned knowledge after every
  successful analysis.
- ``EnterpriseKnowledgeGraph`` — the accumulating org-wide graph
  (optional Neo4j mirror for Cypher querying).
- ``KnowledgeGraphBuilder``    — the per-project analysis graph.

The business ontology used for semantic matching currently lives with the
Data Intelligence Module's ``MeaningDetector``.
"""
from app.intelligence.graph.knowledge_graph import KnowledgeGraphBuilder
from app.knowledge.engine import KnowledgeEngine
from app.knowledge.graph import EnterpriseKnowledgeGraph
from app.knowledge.store import KnowledgeStore

__all__ = ["KnowledgeGraphBuilder", "KnowledgeEngine",
           "EnterpriseKnowledgeGraph", "KnowledgeStore"]

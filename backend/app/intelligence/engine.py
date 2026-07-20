"""Enterprise Intelligence Engine.

The single facade over every deterministic capability of the platform:
connectors (Excel, CSV, PDF, Word, SQL, API, ...), schema discovery,
profiling, semantic understanding, entity/relationship discovery, KPI
discovery, analytics, forecasting, anomaly signals, data quality, knowledge
graph, embeddings, and business-context generation.

The engine produces FACTS ONLY. It never generates executive summaries,
recommendations, or narrative — that is the job of reasoning agents that
consume its output.
"""
from __future__ import annotations

import uuid
from typing import Any

import pandas as pd

from app.core.config import Settings
from app.core.logging import get_logger
from app.domain.entities import TableProfile, UnderstandingAssessment
from app.intelligence.analytics.engine import AnalyticsEngine
from app.intelligence.analytics.signals import SignalEngine
from app.intelligence.confidence.assessor import ConfidenceAssessor
from app.intelligence.connectors import ConnectorRegistry, ExtractedTable, SourceExtract
from app.intelligence.context.builder import BusinessContextBuilder
from app.intelligence.dedup.merger import DatasetMerger
from app.intelligence.embeddings.embedder import Embedder
from app.intelligence.embeddings.vector_store import build_documents, create_vector_store
from app.intelligence.forecasting.engine import ForecastEngine
from app.intelligence.graph.knowledge_graph import KnowledgeGraphBuilder
from app.intelligence.kpi.discovery import KPIDiscovery
from app.intelligence.profiling.profiler import ColumnProfiler
from app.intelligence.quality.engine import QualityEngine
from app.intelligence.relationships.detector import RelationshipDetector
from app.intelligence.semantics.meaning import MeaningDetector
from app.intelligence.timeseries.detector import TimeSeriesDetector
from app.repositories.artifact_store import ArtifactStore

logger = get_logger(__name__)


class IntelligenceEngine:
    """Facts-only analytical core. One instance serves every project."""

    def __init__(self, settings: Settings, store: ArtifactStore,
                 embedder: Embedder, connectors: ConnectorRegistry):
        self.s = settings
        self.store = store
        self.embedder = embedder
        self.connectors = connectors

    # ----------------------------------------------------------- ingestion
    def ingest(self, project_id: str) -> list[SourceExtract]:
        """Read every uploaded source through its connector."""
        extracts: list[SourceExtract] = []
        for f in sorted(self.store.uploads_dir(project_id).iterdir()):
            if not self.connectors.accepts(f.name):
                logger.warning("No available connector for %s — skipped", f.name)
                continue
            extracts.append(self.connectors.for_file(f).extract(f))
        return extracts

    def deduplicate(self, project_id: str,
                    tables: list[ExtractedTable]) -> tuple[list[ExtractedTable], dict]:
        merged, lineage = DatasetMerger(self.s.duplicate_schema_similarity).merge(tables)
        self.store.save(project_id, "lineage", lineage)
        return merged, lineage

    # ------------------------------------------------------------- schema
    def profile(self, merged: list[ExtractedTable],
                lineage: dict) -> tuple[list[TableProfile], dict[str, pd.DataFrame]]:
        profiler = ColumnProfiler(self.s.sample_rows_for_profiling,
                                  self.s.pk_uniqueness_threshold)
        profiles: list[TableProfile] = []
        frames: dict[str, pd.DataFrame] = {}
        for t in merged:
            dataset_id = f"{t.name}_{uuid.uuid4().hex[:6]}"
            profiles.append(profiler.profile_table(t, dataset_id))
            frames[dataset_id] = t.df
        for p in profiles:
            p.merged_from = lineage.get(p.name, [p.name])
        return profiles, frames

    def semantics(self, project_id: str, profiles: list[TableProfile]) -> list:
        detector = MeaningDetector(self.s.fuzzy_match_threshold,
                                   embedder=self.embedder,
                                   semantic_threshold=self.s.semantic_similarity_threshold)
        mappings = detector.annotate(profiles)
        self.store.save(project_id, "semantic_layer", mappings)
        return mappings

    def relationships(self, project_id: str, profiles: list[TableProfile],
                      frames: dict[str, pd.DataFrame]) -> list:
        rels = RelationshipDetector(self.s.fk_overlap_threshold).detect(profiles, frames)
        self.store.save(project_id, "relationships", rels)
        return rels

    def timeseries(self, profiles: list[TableProfile],
                   frames: dict[str, pd.DataFrame]) -> None:
        TimeSeriesDetector().annotate(profiles, frames)

    # ---------------------------------------------------------- analytics
    def kpis(self, profiles: list[TableProfile],
             frames: dict[str, pd.DataFrame]) -> list:
        return KPIDiscovery().discover(profiles, frames)

    def quality(self, project_id: str, profiles: list[TableProfile],
                frames: dict[str, pd.DataFrame]) -> Any:
        quality = QualityEngine(self.s.outlier_zscore).assess(profiles, frames)
        self.store.save(project_id, "quality", quality)
        return quality

    def warehouse(self, project_id: str, profiles: list[TableProfile],
                  frames: dict[str, pd.DataFrame]) -> list:
        analytics = AnalyticsEngine(self.store.duckdb_path(project_id))
        analytics.load(frames)
        breakdowns = analytics.dimension_breakdowns(profiles)
        self.store.save(project_id, "breakdowns", breakdowns)
        return breakdowns

    def signals(self, project_id: str, kpis: list, breakdowns: list) -> list:
        signals = SignalEngine(self.s.min_confidence_to_report).compute(kpis, breakdowns)
        self.store.save(project_id, "signals", signals)
        return signals

    def forecasts(self, project_id: str, kpis: list) -> list:
        forecasts = ForecastEngine().forecast_all(kpis)
        self.store.save(project_id, "forecasts", forecasts)
        self.store.save(project_id, "kpis", kpis)  # after forecast enrichment
        return forecasts

    # ---------------------------------------------------------- knowledge
    def knowledge_graph(self, project_id: str, profiles: list[TableProfile],
                        relationships: list, kpis: list, signals: list) -> None:
        builder = KnowledgeGraphBuilder()
        graph = builder.build(profiles, relationships, kpis, signals)
        self.store.save(project_id, "graph", builder.to_payload(graph))

    def embed(self, project_id: str, profiles: list[TableProfile], mappings: list,
              kpis: list, signals: list, relationships: list) -> None:
        """Rebuild the project vector store from scratch so no documents from
        previous analyses linger."""
        self.store.vectors_path(project_id).unlink(missing_ok=True)
        docs = build_documents(profiles, mappings, kpis, signals, relationships)
        vectors = self.embedder.embed([d["text"] for d in docs])
        vs = create_vector_store(
            self.s.vector_backend, path=self.store.vectors_path(project_id),
            pg_url=self.s.pgvector_url, dim=self.embedder.dim, collection=project_id)
        vs.upsert([d["id"] for d in docs], vectors, docs)
        vs.persist()

    def assess(self, profiles: list[TableProfile], kpis: list,
               relationships: list | None = None,
               quality: Any = None) -> UnderstandingAssessment:
        """Score how confidently the platform understands the data — per
        understanding category, aggregated by weighted scoring — and derive
        the clarification questions that are genuinely necessary. Deterministic
        facts about the platform's own inferences — the workflow decides
        whether to proceed or pause."""
        assessor = ConfidenceAssessor(self.s.clarification_confidence_threshold)
        return assessor.assess(profiles, kpis, relationships, quality)

    def business_context(self, project_id: str, name: str,
                         profiles: list[TableProfile], relationships: list,
                         kpis: list, signals: list, forecasts: list,
                         quality: Any, understanding: dict | None = None) -> dict:
        """Compact factual JSON — the only thing reasoning agents ever see."""
        context = BusinessContextBuilder().build(
            name, profiles, relationships, kpis, signals, forecasts, quality,
            understanding=understanding)
        self.store.save(project_id, "business_context", context)
        return context

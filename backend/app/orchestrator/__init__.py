"""Enterprise AI Orchestrator (V11).

The central intelligence layer: it classifies every question, routes it to the
engines that own the answer, runs them in parallel, and merges their evidence
into the copilot's existing reason-over-facts pipeline. It rewrites no module —
every engine wraps a capability the platform already has (Analytics, Knowledge/
RAG, Machine Learning, Forecast, Recommendation, Report).

Build one from the container with :func:`build_orchestrator`; it wires each
engine to the layer it federates and returns an :class:`EnterpriseOrchestrator`.
"""
from __future__ import annotations

from app.orchestrator.base import (Engine, EngineRequest, EngineResult,
                                    EvidenceItem)
from app.orchestrator.classifier import QueryClassifier
from app.orchestrator.engines import (AnalyticsEngine, ForecastEngine,
                                       KnowledgeEngine, MLEngine,
                                       RecommendationEngine, ReportEngine)
from app.orchestrator.orchestrator import (EnterpriseOrchestrator,
                                           OrchestrationResult)
from app.orchestrator.router import EngineRouter

__all__ = ["EnterpriseOrchestrator", "OrchestrationResult", "EngineRouter",
           "QueryClassifier", "Engine", "EngineRequest", "EngineResult",
           "EvidenceItem", "build_orchestrator", "build_entity_vocab"]


def build_entity_vocab(container) -> dict[str, list[str]]:
    """The banks/PSPs/merchants/products the classifier should recognise. Read
    straight from the raw-transaction warehouse when it holds data, so every
    name the classifier knows is one the analytics engines can actually filter
    on; otherwise fall back to the legacy ecosystem/evolution cubes. Never
    hardcoded — an entity the platform does not know is not an entity."""
    tx = getattr(container, "tx_analytics", None)
    if tx is not None and getattr(tx, "available", False):
        from app.orchestrator.engines._slice import warehouse_entity_vocab
        vocab = warehouse_entity_vocab(tx)
        if any(vocab.values()):
            return {k: [str(v) for v in vs if v] for k, vs in vocab.items()}

    vocab: dict[str, list[str]] = {"bank": [], "psp": [], "merchant": [],
                                   "product": []}
    eco = getattr(container, "ecosystem", None)
    if eco is not None:
        try:
            vocab["bank"] = [r.get("bank") for r in eco.compare_banks()
                             if r.get("bank")]
            vocab["psp"] = [r.get("psp") for r in eco.compare_psps()
                            if r.get("psp")]
        except Exception:  # noqa: BLE001
            pass
    evo = getattr(container, "evolution", None)
    if evo is not None:
        try:
            vocab["merchant"] = [r.get("merchant")
                                 for r in evo.merchants().get("merchants", [])
                                 if r.get("merchant")][:60]
            vocab["product"] = [r.get("product")
                                for r in evo.products().get("products", [])
                                if r.get("product")]
        except Exception:  # noqa: BLE001
            pass
    return {k: [str(v) for v in vs if v] for k, vs in vocab.items()}


def build_orchestrator(container) -> EnterpriseOrchestrator:
    """Assemble the orchestrator over the container's existing layers."""
    tx_analytics = getattr(container, "tx_analytics", None)
    ml_pipeline = getattr(container, "ml_pipeline", None)
    insight_engine = getattr(container, "insight_engine", None)
    executive = getattr(container, "executive", None)
    sync = getattr(container, "sync", None)
    knowledge = getattr(container, "knowledge", None)

    engines: list[Engine] = [
        # The data engines run on the raw-transaction warehouse.
        AnalyticsEngine(analytics=tx_analytics),
        MLEngine(ml_pipeline=ml_pipeline, analytics=tx_analytics),
        ForecastEngine(ml_pipeline=ml_pipeline, analytics=tx_analytics),
        # Knowledge / recommendation / report federate the existing layers.
        KnowledgeEngine(sync=sync),
        RecommendationEngine(insight_engine=insight_engine, executive=executive),
        ReportEngine(knowledge=knowledge, executive=executive),
    ]
    router = EngineRouter(engines, parallel=True)
    classifier = QueryClassifier(entity_vocab=build_entity_vocab(container))
    return EnterpriseOrchestrator(classifier=classifier, router=router)

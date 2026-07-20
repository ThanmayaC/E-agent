"""Enterprise Agent — canonical SDS module namespace.

The SDS defines twenty permanent modules. This package is their canonical
home: ``app.modules.<module>`` is the one import path other layers should
use when they need a module's public interface.

Phase 1 of the migration (strangler-fig): every facade re-exports the
existing, working implementation from its current location — nothing is
rewritten, moved, or duplicated. Later phases move implementations behind
these facades module by module; callers of ``app.modules.*`` never change.

``MODULES`` is the machine-readable registry: SDS module name → facade
import path, implementation status, and the existing packages that back it.
"""
from __future__ import annotations

from importlib import import_module
from types import ModuleType

# status: implemented — SDS responsibilities substantially covered
#         partial     — working core exists, SDS scope not yet complete
#         planned     — canonical home exists, implementation is roadmap
MODULES: dict[str, dict] = {
    "supervisor": {
        "title": "Supervisor Module", "status": "implemented",
        "backed_by": ["app.orchestration.agents"]},
    "planner": {
        "title": "Planner Module", "status": "implemented",
        "backed_by": ["app.orchestration.agents", "app.agents.specialists"]},
    "observation": {
        "title": "Observation Module", "status": "implemented",
        "backed_by": ["app.intelligence.connectors"]},
    "data_intelligence": {
        "title": "Data Intelligence Module", "status": "implemented",
        "backed_by": ["app.intelligence.semantics", "app.intelligence.dedup",
                       "app.intelligence.relationships", "app.intelligence.confidence",
                       "app.intelligence.context"]},
    "schema_intelligence": {
        "title": "Schema Intelligence Module", "status": "implemented",
        "backed_by": ["app.intelligence.profiling", "app.intelligence.timeseries"]},
    "analytics": {
        "title": "Analytics Module", "status": "implemented",
        "backed_by": ["app.intelligence.analytics", "app.intelligence.kpi",
                       "app.intelligence.quality"]},
    "machine_learning": {
        "title": "Machine Learning Module", "status": "implemented",
        "backed_by": ["app.ml.selection", "app.ml.tabular", "app.ml.features",
                       "app.ml.pipelines", "app.ml.registry",
                       "app.ml.monitoring", "app.ml.explain"]},
    "deep_learning": {
        "title": "Deep Learning Module", "status": "partial",
        "backed_by": ["app.intelligence.embeddings"]},
    "knowledge": {
        "title": "Knowledge Module", "status": "implemented",
        "backed_by": ["app.knowledge.store", "app.knowledge.engine",
                       "app.knowledge.graph", "app.intelligence.graph"]},
    "memory": {
        "title": "Memory Module", "status": "implemented",
        "backed_by": ["app.memory.manager", "app.memory.sync"]},
    "forecasting": {
        "title": "Forecasting Module", "status": "implemented",
        "backed_by": ["app.intelligence.forecasting"]},
    "evidence_verification": {
        "title": "Evidence Verification Module", "status": "implemented",
        "backed_by": ["app.evidence"]},
    "recommendation": {
        "title": "Recommendation Module", "status": "implemented",
        "backed_by": ["app.intelligence.recommendations"]},
    "report_generation": {
        "title": "Report Generation Module", "status": "implemented",
        "backed_by": ["app.reports", "app.agents.report_writer"]},
    "portfolio": {
        "title": "Portfolio Module", "status": "implemented",
        "backed_by": ["app.manager.portfolio", "app.product.portfolio",
                       "app.agents.specialists"]},
    "manager": {
        "title": "Manager Module", "status": "implemented",
        "backed_by": ["app.manager", "app.agents.specialists",
                       "app.agents.reasoning", "app.agents.prompt_generator",
                       "app.agents.copilot"]},
    "document_intelligence": {
        "title": "Document Intelligence Module", "status": "partial",
        "backed_by": ["app.intelligence.connectors.pdf",
                       "app.intelligence.connectors.word"]},
    "communication": {
        "title": "Communication Module", "status": "partial",
        "backed_by": ["app.communication", "app.tools.planned"]},
    "workflow": {
        "title": "Workflow Module", "status": "implemented",
        "backed_by": ["app.workflows", "app.workflows.autonomous"]},
    "automation": {
        "title": "Automation Module", "status": "implemented",
        "backed_by": ["app.runtime.scheduler", "app.runtime.triggers",
                       "app.runtime.queue", "app.runtime.background",
                       "app.runtime.runtime", "app.workflows.engine"]},
}


def resolve(name: str) -> ModuleType:
    """Import and return the facade for an SDS module name."""
    if name not in MODULES:
        raise KeyError(f"Unknown SDS module: {name!r}")
    return import_module(f"app.modules.{name}")


def catalog() -> list[dict]:
    """Registry as a serializable list (for the platform API / UI)."""
    return [{"name": name, **meta} for name, meta in MODULES.items()]

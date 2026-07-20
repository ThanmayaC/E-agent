"""Phase 1 migration guard: every SDS module has a canonical, importable
facade under app.modules, and every symbol a facade declares actually
resolves. Keeps the strangler-fig namespace honest as implementations move
behind it."""
from __future__ import annotations

import pytest

from app.modules import MODULES, catalog, resolve

SDS_MODULE_NAMES = {
    "supervisor", "planner", "observation", "data_intelligence",
    "schema_intelligence", "analytics", "machine_learning", "deep_learning",
    "knowledge", "memory", "forecasting", "evidence_verification",
    "recommendation", "report_generation", "portfolio", "manager",
    "document_intelligence", "communication", "workflow", "automation",
}


def test_registry_covers_all_twenty_sds_modules():
    assert set(MODULES) == SDS_MODULE_NAMES


@pytest.mark.parametrize("name", sorted(SDS_MODULE_NAMES))
def test_facade_imports_and_exports_resolve(name):
    module = resolve(name)
    exports = getattr(module, "__all__", [])
    assert exports, f"facade app.modules.{name} declares no exports"
    for symbol in exports:
        assert hasattr(module, symbol), (
            f"app.modules.{name} declares {symbol!r} but does not expose it")


def test_unknown_module_rejected():
    with pytest.raises(KeyError):
        resolve("dashboards")


def test_catalog_is_serializable_registry():
    entries = catalog()
    assert len(entries) == 20
    for entry in entries:
        assert entry["status"] in {"implemented", "partial", "planned"}
        assert entry["backed_by"]

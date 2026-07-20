"""Connector Registry — the catalogue, and the only place a connector class
is named.

Connectors are registered by *kind* and instantiated from a
``ConnectorConfig``. The registry can load a class from a dotted path
(``app.connectors.folder:FolderConnector``), which is what makes the
framework extensible without framework changes: a new connector is a module
plus one entry in ``CONNECTOR_PATHS`` — or a runtime ``load()`` call from a
deployment's own package, with nothing in this repository touched at all.

A kind that is declared but whose module will not import is not an error: it
is reported as unavailable with the reason, exactly as the format-connector
registry already does. A missing optional driver must degrade one connector,
never break the catalogue.
"""
from __future__ import annotations

import importlib
import threading

from app.connectors.base import ConnectorConfig, EnterpriseConnector
from app.core.logging import get_logger

logger = get_logger(__name__)

# The V2.1 catalogue. Only the first four are implemented; the rest are
# declared so they appear in the Admin catalogue as planned, and so adding
# them later is a module, not a design change.
CONNECTOR_PATHS: dict[str, str] = {
    "folder": "app.connectors.folder:FolderConnector",
    "excel": "app.connectors.excel:ExcelConnector",
    "csv": "app.connectors.csv:CSVConnector",
    "postgresql": "app.connectors.postgres:PostgreSQLConnector",
}

# Declared but not yet implemented — the framework's roadmap, visible in the
# API so administrators can see what is coming without reading the source.
PLANNED_CONNECTORS: dict[str, str] = {
    "shared_folder": "Shared/network folder — arrives with FolderConnector's UNC support",
    "sqlserver": "SQL Server — DatabaseConnector subclass, Version 2.2",
    "oracle": "Oracle — DatabaseConnector subclass, Version 2.2",
    "outlook": "Outlook — Microsoft Graph connector, Version 2.2",
    "teams": "Microsoft Teams — Microsoft Graph connector, Version 2.2",
    "sharepoint": "SharePoint — Microsoft Graph connector, Version 2.2",
    "onedrive": "OneDrive — Microsoft Graph connector, Version 2.2",
    "rest_api": "REST API — RestApiConnector, Version 2.2",
}


class ConnectorNotRegistered(KeyError):
    """No connector is registered for this kind."""


class ConnectorRegistry:
    """Every known connector kind, and the factory for instances of it."""

    def __init__(self) -> None:
        self._classes: dict[str, type[EnterpriseConnector]] = {}
        self._unavailable: dict[str, str] = {}
        self._lock = threading.RLock()

    # ------------------------------------------------------- registration
    def register(self, connector_class: type[EnterpriseConnector],
                 kind: str = "") -> None:
        """Register a connector class under its own ``kind`` (or an override)."""
        key = kind or connector_class.kind
        if not key or key == "connector":
            raise ValueError(
                f"{connector_class.__name__} must declare a 'kind' class attribute")
        with self._lock:
            self._classes[key] = connector_class
            self._unavailable.pop(key, None)

    def load(self, kind: str, dotted_path: str) -> bool:
        """Import ``module:ClassName`` and register it. Returns whether it
        loaded; a failure is recorded as an unavailable kind, never raised —
        one missing driver must not empty the catalogue."""
        try:
            module_name, _, class_name = dotted_path.partition(":")
            if not class_name:
                raise ValueError(
                    f"connector path must be 'module:ClassName', got {dotted_path!r}")
            module = importlib.import_module(module_name)
            connector_class = getattr(module, class_name)
            if not issubclass(connector_class, EnterpriseConnector):
                raise TypeError(
                    f"{dotted_path} is not an EnterpriseConnector subclass")
            self.register(connector_class, kind)
            return True
        except Exception as exc:  # noqa: BLE001 — a bad entry degrades one kind
            reason = f"{type(exc).__name__}: {exc}"[:200]
            logger.warning("Connector '%s' unavailable (%s): %s", kind,
                           dotted_path, reason)
            with self._lock:
                self._unavailable[kind] = reason
            return False

    # ------------------------------------------------------------ factory
    def create(self, config: ConnectorConfig) -> EnterpriseConnector:
        """Build and initialize a connector for one configured source."""
        connector_class = self.get(config.kind)
        connector = connector_class(config)
        connector.initialize()
        return connector

    def get(self, kind: str) -> type[EnterpriseConnector]:
        with self._lock:
            if kind in self._classes:
                return self._classes[kind]
            if kind in self._unavailable:
                raise ConnectorNotRegistered(
                    f"Connector '{kind}' is registered but unavailable in this "
                    f"deployment: {self._unavailable[kind]}")
        planned = PLANNED_CONNECTORS.get(kind)
        if planned:
            raise ConnectorNotRegistered(f"Connector '{kind}' is planned: {planned}")
        raise ConnectorNotRegistered(f"No connector registered for kind '{kind}'")

    def has(self, kind: str) -> bool:
        with self._lock:
            return kind in self._classes

    def kinds(self) -> list[str]:
        with self._lock:
            return sorted(self._classes)

    # --------------------------------------------------------- inspection
    def describe(self) -> list[dict]:
        """The catalogue for the Admin console: available, unavailable, and
        planned connectors in one list, each saying which it is and why."""
        with self._lock:
            entries = [{**cls.describe_kind(), "available": True,
                        "unavailable_reason": ""}
                       for cls in self._classes.values()]
            entries += [{"kind": kind, "title": kind, "description": "",
                         "capabilities": [], "produces": "",
                         "available": False, "unavailable_reason": reason}
                        for kind, reason in self._unavailable.items()]
        entries += [{"kind": kind, "title": kind, "description": detail,
                     "capabilities": [], "produces": "",
                     "available": False, "unavailable_reason": detail}
                    for kind, detail in PLANNED_CONNECTORS.items()
                    if not self.has(kind) and kind not in self._unavailable]
        return sorted(entries, key=lambda e: (not e["available"], e["kind"]))


def build_registry(paths: dict[str, str] | None = None) -> ConnectorRegistry:
    """The default registry: every connector this version ships."""
    registry = ConnectorRegistry()
    for kind, path in (paths or CONNECTOR_PATHS).items():
        registry.load(kind, path)
    return registry

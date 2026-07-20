"""Connector Framework persistence.

Registered connector configurations, their sync cursors, run history, and the
knowledge-package catalogue live under ``data/connectors`` — one JSON document
per section, the same inspectable profile as the RuntimeStore and SyncStore.

This is not a second SyncStore: it *is* SyncStore, pointed at its own
directory with its own sections, because a second implementation of
read-modify-write-under-a-lock is a second thing to keep correct. Cursors
reuse the fingerprint files, which are already per-source and already the
high-churn path.
"""
from __future__ import annotations

import json
from pathlib import Path

from app.sync.store import SyncStore, new_id, now_iso

SECTIONS = ("connectors", "runs", "packages", "failures")

__all__ = ["SECTIONS", "ConnectorStore", "new_id", "now_iso"]


class ConnectorStore(SyncStore):
    """Connector configurations, cursors, run history, package catalogue."""

    def __init__(self, connectors_dir: Path):
        super().__init__(connectors_dir, sections=SECTIONS)
        self._cursors_dir = connectors_dir / "cursors"
        self._cursors_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------ cursors
    def cursor(self, connector_id: str) -> dict:
        """The stored sync cursor for one connector ({} when never synced)."""
        path = self._cursors_dir / f"{connector_id}.json"
        if not path.exists():
            return {}
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:  # unreadable state degrades to a full re-sync
            return {}

    def save_cursor(self, connector_id: str, cursor: dict) -> None:
        with self._lock:
            (self._cursors_dir / f"{connector_id}.json").write_text(
                json.dumps(cursor, ensure_ascii=False, default=str),
                encoding="utf-8")

    def drop_cursor(self, connector_id: str) -> None:
        (self._cursors_dir / f"{connector_id}.json").unlink(missing_ok=True)

"""Synchronization Store — persistence for the knowledge synchronization layer.

Registered sources, their sync state, the organizational model's entities and
relationships, and the sync/refresh history are org-wide records (not analysis
artifacts, not organizational knowledge, not executive workspace state, not
autonomy runtime state), stored as one JSON document per section under
``data/sync`` — the same simple, inspectable profile as the KnowledgeStore and
RuntimeStore, swappable for a database later without touching callers.

``fingerprints`` is the only high-churn section: one record hash per synced
record, which is what makes delta synchronization possible. It is keyed by
source and kept in its own file per source so a large source never rewrites
another's state.
"""
from __future__ import annotations

import json
import threading
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

SECTIONS = ("sources", "entities", "relationships", "sync_runs",
            "refresh_events")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


class SyncStore:
    def __init__(self, sync_dir: Path, sections: tuple[str, ...] = SECTIONS):
        self._dir = sync_dir
        self._dir.mkdir(parents=True, exist_ok=True)
        self._fingerprints_dir = self._dir / "fingerprints"
        self._fingerprints_dir.mkdir(parents=True, exist_ok=True)
        self._sections = sections
        self._lock = threading.RLock()

    def _path(self, section: str) -> Path:
        if section not in self._sections:
            raise ValueError(f"Unknown sync section: {section}")
        return self._dir / f"{section}.json"

    def read(self, section: str) -> list[dict]:
        path = self._path(section)
        if not path.exists():
            return []
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:  # a corrupt file must never take synchronization down
            return []

    def write(self, section: str, items: list[dict]) -> None:
        with self._lock:
            self._write(section, items)

    def append(self, section: str, item: dict, cap: int = 0) -> dict:
        with self._lock:
            items = self.read(section)
            items.append(item)
            self._write(section, items[-cap:] if cap else items)
        return item

    def update(self, section: str, id_key: str, item_id: str,
               fields: dict[str, Any]) -> dict | None:
        with self._lock:
            items = self.read(section)
            for item in items:
                if item.get(id_key) == item_id:
                    item.update(fields)
                    item["updated_at"] = now_iso()
                    self._write(section, items)
                    return item
        return None

    def get(self, section: str, id_key: str, item_id: str) -> dict | None:
        for item in self.read(section):
            if item.get(id_key) == item_id:
                return item
        return None

    def delete(self, section: str, id_key: str, item_id: str) -> bool:
        with self._lock:
            items = self.read(section)
            remaining = [i for i in items if i.get(id_key) != item_id]
            if len(remaining) == len(items):
                return False
            self._write(section, remaining)
            return True

    @contextmanager
    def mutate(self, section: str) -> Iterator[list[dict]]:
        """Read-modify-write a whole section atomically.

        The scheduler's sync jobs and API requests touch these sections
        concurrently; a plain ``read`` then ``write`` pair loses whichever
        update wrote first.
        """
        with self._lock:
            items = self.read(section)
            yield items
            self._write(section, items)

    # ------------------------------------------------------- fingerprints
    def fingerprints(self, source_id: str) -> dict[str, str]:
        """Record key → content hash for one source, from its last sync."""
        path = self._fingerprints_dir / f"{source_id}.json"
        if not path.exists():
            return {}
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return {}  # unreadable state degrades to a full re-sync, not a crash

    def save_fingerprints(self, source_id: str,
                          fingerprints: dict[str, str]) -> None:
        with self._lock:
            (self._fingerprints_dir / f"{source_id}.json").write_text(
                json.dumps(fingerprints, ensure_ascii=False, default=str),
                encoding="utf-8")

    def drop_fingerprints(self, source_id: str) -> None:
        (self._fingerprints_dir / f"{source_id}.json").unlink(missing_ok=True)

    def _write(self, section: str, items: list[dict]) -> None:
        self._path(section).write_text(
            json.dumps(items, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8")

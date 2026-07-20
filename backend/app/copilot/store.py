"""Copilot Store — persistence for enterprise conversations.

Conversations, their messages, the executive's preferences, and pinned
threads. One JSON document per section under ``data/copilot`` — the same
simple, inspectable profile as the Knowledge, Runtime, Sync, and Product
stores, swappable for a database later without touching callers.

The per-*project* copilot already persists its own history through
``ConversationMemory`` (an artifact per project). This store is the
*enterprise* conversation: an executive talking to the platform as a whole,
not to one analysis. The two coexist; neither replaces the other.
"""
from __future__ import annotations

import json
import threading
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

SECTIONS = ("conversations", "messages", "preferences")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


class CopilotStore:
    def __init__(self, copilot_dir: Path):
        self._dir = copilot_dir
        self._dir.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()

    def _path(self, section: str) -> Path:
        if section not in SECTIONS:
            raise ValueError(f"Unknown copilot section: {section}")
        return self._dir / f"{section}.json"

    def read(self, section: str) -> list[dict]:
        path = self._path(section)
        if not path.exists():
            return []
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:  # a corrupt file must never take the copilot down
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
        """Read-modify-write a section atomically — the scheduler's copilot
        jobs and chat requests touch these sections concurrently."""
        with self._lock:
            items = self.read(section)
            yield items
            self._write(section, items)

    def _write(self, section: str, items: list[dict]) -> None:
        self._path(section).write_text(
            json.dumps(items, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8")

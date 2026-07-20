"""Manager Store — persistence for executive workspace state.

Tasks, decisions, report reviews, and daily briefs are org-wide operational
records (not analysis artifacts and not organizational knowledge), stored as
one JSON document per section under ``data/manager`` — the same simple,
inspectable profile as the KnowledgeStore, swappable for a database later
without touching callers.
"""
from __future__ import annotations

import json
import threading
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SECTIONS = ("tasks", "decisions", "report_reviews", "daily_briefs")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


class ManagerStore:
    def __init__(self, manager_dir: Path):
        self._dir = manager_dir
        self._dir.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()

    def _path(self, section: str) -> Path:
        if section not in SECTIONS:
            raise ValueError(f"Unknown manager section: {section}")
        return self._dir / f"{section}.json"

    def read(self, section: str) -> list[dict]:
        path = self._path(section)
        if not path.exists():
            return []
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:  # corrupt file must never take the workspace down
            return []

    def write(self, section: str, items: list[dict]) -> None:
        with self._lock:
            self._path(section).write_text(
                json.dumps(items, ensure_ascii=False, indent=2, default=str),
                encoding="utf-8")

    def append(self, section: str, item: dict) -> dict:
        with self._lock:
            items = self.read(section)
            items.append(item)
            self._path(section).write_text(
                json.dumps(items, ensure_ascii=False, indent=2, default=str),
                encoding="utf-8")
        return item

    def update(self, section: str, id_key: str, item_id: str,
               fields: dict[str, Any]) -> dict | None:
        """Merge fields into the item with the given id; None if missing."""
        with self._lock:
            items = self.read(section)
            for item in items:
                if item.get(id_key) == item_id:
                    item.update(fields)
                    item["updated_at"] = now_iso()
                    self._path(section).write_text(
                        json.dumps(items, ensure_ascii=False, indent=2,
                                   default=str), encoding="utf-8")
                    return item
        return None

"""Runtime Store — persistence for the autonomous execution layer.

Goals, queued actions, trigger rules, job state, plans, and execution
records are org-wide runtime state (not analysis artifacts, not
organizational knowledge, not executive workspace records), stored as one
JSON document per section under ``data/runtime`` — the same simple,
inspectable profile as the ManagerStore, swappable for a database later
without touching callers.
"""
from __future__ import annotations

import json
import threading
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

SECTIONS = ("goals", "actions", "triggers", "jobs", "plans", "decisions",
            "executions", "events")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


class RuntimeStore:
    def __init__(self, runtime_dir: Path):
        self._dir = runtime_dir
        self._dir.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()

    def _path(self, section: str) -> Path:
        if section not in SECTIONS:
            raise ValueError(f"Unknown runtime section: {section}")
        return self._dir / f"{section}.json"

    def read(self, section: str) -> list[dict]:
        path = self._path(section)
        if not path.exists():
            return []
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:  # corrupt file must never take the runtime down
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
        """Merge fields into the item with the given id; None if missing."""
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

    @contextmanager
    def mutate(self, section: str) -> Iterator[list[dict]]:
        """Read-modify-write a whole section atomically.

        ``read`` then ``write`` is NOT safe here: the scheduler thread and an
        API request mutate the same sections concurrently, and an interleaved
        pair loses whichever update wrote first. Callers that change an item
        in place (a plan's steps, a decision's outcome) must go through this
        instead, which holds the lock across the read and the write::

            with store.mutate("plans") as plans:
                plans[i]["status"] = "superseded"
        """
        with self._lock:
            items = self.read(section)
            yield items
            self._write(section, items)

    def _write(self, section: str, items: list[dict]) -> None:
        self._path(section).write_text(
            json.dumps(items, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8")

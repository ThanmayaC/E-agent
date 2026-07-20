"""Product Store — persistence for the Product Intelligence layer.

The product catalogue, computed health, generated reviews, strategic
recommendations, scenarios, KPI alerts, and executive briefs. One JSON
document per section under ``data/product`` — the same simple, inspectable
profile as the Knowledge, Runtime, and Sync stores, swappable for a database
later without touching callers.

This layer stores *judgements*, not facts. The facts stay where they already
live (analytics artifacts, the Knowledge Store, the Organizational Model);
what is kept here is what the Product Manager concluded from them, with a
citation back to the evidence — which is why a product's health can always be
explained rather than merely displayed.
"""
from __future__ import annotations

import json
import threading
import uuid
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

SECTIONS = ("products", "health", "reviews", "recommendations", "scenarios",
            "kpi_alerts", "kpi_thresholds", "briefs")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:10]}"


class ProductStore:
    def __init__(self, product_dir: Path):
        self._dir = product_dir
        self._dir.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()

    def _path(self, section: str) -> Path:
        if section not in SECTIONS:
            raise ValueError(f"Unknown product section: {section}")
        return self._dir / f"{section}.json"

    def read(self, section: str) -> list[dict]:
        path = self._path(section)
        if not path.exists():
            return []
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:  # a corrupt file must never take the layer down
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
        """Read-modify-write a section atomically — the scheduler's product
        jobs and API requests touch these sections concurrently."""
        with self._lock:
            items = self.read(section)
            yield items
            self._write(section, items)

    def _write(self, section: str, items: list[dict]) -> None:
        self._path(section).write_text(
            json.dumps(items, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8")

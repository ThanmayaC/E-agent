"""Retrieval / semantic cache (V10.0) — performance layer.

A small in-process TTL + LRU cache keyed on a normalised query string, so
repeated or near-identical requests (the common case in an interactive
workspace) are served without recomputation. It reports hit/miss stats for the
observability surface. Deliberately dependency-free and bounded.
"""
from __future__ import annotations

import re
import time
from collections import OrderedDict

_WS = re.compile(r"\s+")
_PUNCT = re.compile(r"[^\w\s]")


def normalize(text: str) -> str:
    t = (text or "").lower().strip()
    t = _PUNCT.sub(" ", t)
    return _WS.sub(" ", t).strip()


class SemanticCache:
    def __init__(self, ttl: float = 60.0, capacity: int = 256):
        self._ttl = ttl
        self._cap = capacity
        self._store: OrderedDict[str, tuple[float, object]] = OrderedDict()
        self._hits = 0
        self._misses = 0

    def get(self, key: str):
        k = normalize(key)
        item = self._store.get(k)
        if item and (time.monotonic() - item[0]) < self._ttl:
            self._store.move_to_end(k)
            self._hits += 1
            return item[1]
        if item:
            self._store.pop(k, None)  # expired
        self._misses += 1
        return None

    def set(self, key: str, value) -> None:
        k = normalize(key)
        self._store[k] = (time.monotonic(), value)
        self._store.move_to_end(k)
        while len(self._store) > self._cap:
            self._store.popitem(last=False)

    def clear(self) -> None:
        self._store.clear()

    def stats(self) -> dict:
        total = self._hits + self._misses
        return {"entries": len(self._store), "hits": self._hits,
                "misses": self._misses, "capacity": self._cap,
                "ttl_seconds": self._ttl,
                "hit_rate": round(self._hits / total, 3) if total else 0.0}

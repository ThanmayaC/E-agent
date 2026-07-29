"""Continuous learning (V10.0) — improve without retraining the LLM.

A lightweight, file-backed feedback + usage store. It records what the user
accepts and rejects, which questions recur, which files and dashboards are used
most, and which reports land — then exposes aggregates the rest of the platform
uses to re-rank suggestions and recommendations. No model is retrained; the
system simply learns the user's preferences and surfaces them.
"""
from __future__ import annotations

import json
import time
from collections import Counter
from pathlib import Path

from app.core.logging import get_logger

logger = get_logger(__name__)


class LearningStore:
    def __init__(self, base_dir: Path):
        self._dir = Path(base_dir)
        self._dir.mkdir(parents=True, exist_ok=True)
        self._path = self._dir / "learning.json"

    def _load(self) -> dict:
        if self._path.exists():
            try:
                return json.loads(self._path.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                pass
        return {"events": [], "questions": {}, "files": {}, "dashboards": {},
                "recommendations": {}}

    def _save(self, data: dict) -> None:
        # keep the event log bounded
        data["events"] = data.get("events", [])[-2000:]
        self._path.write_text(json.dumps(data, ensure_ascii=False),
                              encoding="utf-8")

    # ------------------------------------------------------------- record
    def record_feedback(self, kind: str, ref: str, action: str,
                        meta: dict | None = None) -> dict:
        """action ∈ accepted / rejected / dismissed / applied / helpful / not_helpful"""
        data = self._load()
        ev = {"ts": time.time(), "kind": kind, "ref": ref, "action": action,
              "meta": meta or {}}
        data["events"].append(ev)
        if kind == "recommendation":
            rec = data["recommendations"].setdefault(
                ref, {"accepted": 0, "rejected": 0})
            if action in ("accepted", "applied", "helpful"):
                rec["accepted"] += 1
            elif action in ("rejected", "dismissed", "not_helpful"):
                rec["rejected"] += 1
        self._save(data)
        return ev

    def record_question(self, q: str) -> None:
        q = (q or "").strip().lower()
        if not q:
            return
        data = self._load()
        data["questions"][q] = data["questions"].get(q, 0) + 1
        self._save(data)

    def record_access(self, kind: str, ref: str) -> None:
        if not ref:
            return
        bucket = "files" if kind == "file" else "dashboards"
        data = self._load()
        data[bucket][ref] = data[bucket].get(ref, 0) + 1
        self._save(data)

    # --------------------------------------------------------------- read
    def top_questions(self, n: int = 8) -> list[dict]:
        data = self._load()
        return [{"question": q, "count": c} for q, c in
                Counter(data["questions"]).most_common(n)]

    def frequent(self, bucket: str, n: int = 8) -> list[dict]:
        data = self._load()
        return [{"ref": r, "count": c} for r, c in
                Counter(data.get(bucket, {})).most_common(n)]

    def recommendation_score(self, ref: str) -> float:
        """Net preference in [-1, 1] used to re-rank recommendations."""
        data = self._load()
        rec = data["recommendations"].get(ref)
        if not rec:
            return 0.0
        a, r = rec["accepted"], rec["rejected"]
        return (a - r) / max(1, a + r)

    def rerank(self, items: list[dict], key: str = "id") -> list[dict]:
        """Stable re-rank of items by learned acceptance (accepted first)."""
        return sorted(items, key=lambda it: -self.recommendation_score(
            str(it.get(key, ""))))

    def stats(self) -> dict:
        data = self._load()
        recs = data.get("recommendations", {})
        accepted = sum(v["accepted"] for v in recs.values())
        rejected = sum(v["rejected"] for v in recs.values())
        return {"available": True, "events": len(data.get("events", [])),
                "accepted": accepted, "rejected": rejected,
                "acceptance_rate": round(accepted / max(1, accepted + rejected), 2),
                "top_questions": self.top_questions(),
                "frequent_files": self.frequent("files"),
                "preferred_dashboards": self.frequent("dashboards")}

"""Internal notification framework (Communication Module).

In-platform notifications only — no Outlook, Teams, or any external channel
(Version 2). Producers across the platform call ``notify``; the executive
workspace consumes ``recent``/``unread``. Deduplicated by reference so
re-analysis never spams the executive.
"""
from __future__ import annotations

import json
import threading
import uuid
from datetime import datetime, timezone
from pathlib import Path

NOTIFICATION_KINDS = ("new_report", "critical_risk", "task_deadline",
                      "portfolio_change", "workflow_failure",
                      "recommendation")

MAX_NOTIFICATIONS = 500


class NotificationCenter:
    def __init__(self, data_dir: Path):
        self._path = data_dir / "notifications.json"
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()

    # --------------------------------------------------------------- write
    def notify(self, kind: str, title: str, detail: str = "",
               project_id: str = "", ref: str = "") -> dict | None:
        """Create a notification. ``ref`` identifies the underlying event —
        a notification with the same (kind, project_id, ref) is created only
        once. Returns None when deduplicated."""
        if kind not in NOTIFICATION_KINDS:
            raise ValueError(f"Unknown notification kind: {kind}")
        with self._lock:
            items = self._read()
            if ref and any(n.get("kind") == kind and n.get("ref") == ref
                           and n.get("project_id") == project_id
                           for n in items):
                return None
            item = {"notification_id": f"ntf_{uuid.uuid4().hex[:10]}",
                    "kind": kind, "title": title[:200], "detail": detail[:500],
                    "project_id": project_id, "ref": ref, "read": False,
                    "created_at": datetime.now(timezone.utc).isoformat()}
            items.append(item)
            self._write(items[-MAX_NOTIFICATIONS:])
            return item

    def mark_read(self, notification_id: str) -> bool:
        with self._lock:
            items = self._read()
            for n in items:
                if n["notification_id"] == notification_id:
                    n["read"] = True
                    self._write(items)
                    return True
        return False

    def mark_all_read(self) -> int:
        with self._lock:
            items = self._read()
            changed = sum(1 for n in items if not n["read"])
            for n in items:
                n["read"] = True
            self._write(items)
            return changed

    # ---------------------------------------------------------------- read
    def recent(self, limit: int = 30, unread_only: bool = False,
               kind: str = "") -> list[dict]:
        items = self._read()
        if unread_only:
            items = [n for n in items if not n["read"]]
        if kind:
            items = [n for n in items if n["kind"] == kind]
        return list(reversed(items))[:limit]  # newest first

    def unread_count(self) -> int:
        return sum(1 for n in self._read() if not n["read"])

    def stats(self) -> dict:
        items = self._read()
        by_kind: dict[str, int] = {}
        for n in items:
            by_kind[n["kind"]] = by_kind.get(n["kind"], 0) + 1
        return {"total": len(items), "unread": self.unread_count(),
                "by_kind": by_kind}

    # ------------------------------------------------------------ internal
    def _read(self) -> list[dict]:
        if not self._path.exists():
            return []
        try:
            return json.loads(self._path.read_text(encoding="utf-8"))
        except Exception:
            return []

    def _write(self, items: list[dict]) -> None:
        self._path.write_text(
            json.dumps(items, ensure_ascii=False, indent=2, default=str),
            encoding="utf-8")

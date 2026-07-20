"""Executive Task Manager.

Tracks pending / completed / suggested / follow-up tasks and generates them
automatically from reports (priority actions), recommendations (AI +
rule-derived), and approvals (pending clarifications). Generation is
idempotent: a task is keyed by its source signature and never duplicated.
Future communication workflows push tasks through the same ``create`` seam.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from app.manager.store import ManagerStore, new_id, now_iso

STATUSES = ("pending", "completed", "suggested", "follow_up", "dismissed")
SOURCE_KINDS = ("report", "recommendation", "business_rule", "approval",
                "decision", "manual", "communication")


class ExecutiveTaskManager:
    def __init__(self, store: ManagerStore):
        self.store = store

    # ---------------------------------------------------------------- CRUD
    def create(self, title: str, detail: str = "", status: str = "pending",
               priority: int | None = None, source_kind: str = "manual",
               source_ref: str = "", project_id: str = "",
               due_date: str = "", owner: str = "") -> dict | None:
        """Create a task; None when an equivalent task already exists
        (matched by source kind + ref, or by title for manual tasks)."""
        if status not in STATUSES:
            raise ValueError(f"Unknown task status: {status}")
        if source_kind not in SOURCE_KINDS:
            raise ValueError(f"Unknown task source: {source_kind}")
        signature = f"{source_kind}:{source_ref or title.strip().lower()}"
        existing = self.store.read("tasks")
        if any(t.get("signature") == signature for t in existing):
            return None
        task = {"task_id": new_id("task"), "title": title[:300],
                "detail": detail[:800], "status": status,
                "priority": priority, "source_kind": source_kind,
                "source_ref": source_ref, "signature": signature,
                "project_id": project_id, "due_date": due_date,
                "owner": owner, "created_at": now_iso(), "completed_at": ""}
        return self.store.append("tasks", task)

    def update_status(self, task_id: str, status: str) -> dict | None:
        if status not in STATUSES:
            raise ValueError(f"Unknown task status: {status}")
        fields = {"status": status}
        if status == "completed":
            fields["completed_at"] = now_iso()
        return self.store.update("tasks", "task_id", task_id, fields)

    def tasks(self, status: str = "", limit: int = 100) -> list[dict]:
        items = self.store.read("tasks")
        if status:
            items = [t for t in items if t["status"] == status]
        ranked = sorted(items, key=lambda t: (t.get("priority") is None,
                                              t.get("priority") or 99))
        return ranked[:limit]

    def open_tasks(self, limit: int = 100) -> list[dict]:
        items = [t for t in self.store.read("tasks")
                 if t["status"] in ("pending", "follow_up")]
        return sorted(items, key=lambda t: (t.get("priority") is None,
                                            t.get("priority") or 99))[:limit]

    def due_soon(self, days: int = 3) -> list[dict]:
        horizon = (datetime.now(timezone.utc) + timedelta(days=days)).date()
        out = []
        for t in self.open_tasks(500):
            due = (t.get("due_date") or "")[:10]
            if due:
                try:
                    if datetime.fromisoformat(due).date() <= horizon:
                        out.append(t)
                except ValueError:
                    continue
        return out

    def stats(self) -> dict:
        counts: dict[str, int] = {s: 0 for s in STATUSES}
        for t in self.store.read("tasks"):
            counts[t["status"]] = counts.get(t["status"], 0) + 1
        return counts

    # ---------------------------------------------------------- generation
    def generate_from_report(self, project_id: str, report_version: int,
                             ai_report: dict,
                             deterministic_recs: list[dict]) -> int:
        """Priority actions become pending tasks; AI and rule-derived
        recommendations become suggested tasks."""
        created = 0
        if (ai_report or {}).get("status") == "ok":
            for i, action in enumerate(
                    (ai_report.get("priority_actions") or [])[:5], start=1):
                text = str(action).strip()
                if text and self.create(
                        text, status="pending", priority=i,
                        source_kind="report",
                        source_ref=f"{project_id}:priority:{text[:60].lower()}",
                        project_id=project_id,
                        detail=f"Priority action from report v{report_version}"):
                    created += 1
            for rec in (ai_report.get("recommendations") or [])[:5]:
                if not isinstance(rec, dict):
                    continue
                action = str(rec.get("action", "")).strip()
                if action and self.create(
                        action, status="suggested",
                        priority=rec.get("priority"),
                        source_kind="recommendation",
                        source_ref=f"{project_id}:ai:{action[:60].lower()}",
                        project_id=project_id,
                        detail=str(rec.get("expected_impact", ""))[:300]):
                    created += 1
        for rec in (deterministic_recs or [])[:5]:
            if not isinstance(rec, dict):
                continue
            action = str(rec.get("action") or rec.get("recommendation", "")).strip()
            if action and self.create(
                    action, status="suggested",
                    source_kind="business_rule",
                    source_ref=f"{project_id}:rule:{action[:60].lower()}",
                    project_id=project_id,
                    detail=str(rec.get("trigger", ""))[:300]):
                created += 1
        return created

    def generate_from_approvals(self, pending: list[dict]) -> int:
        """Every pending approval (clarification pause, report review)
        becomes a follow-up task for the executive."""
        created = 0
        for item in pending:
            ref = item.get("ref", "")
            title = item.get("title", "").strip()
            if title and self.create(title, status="follow_up",
                                     source_kind="approval", source_ref=ref,
                                     project_id=item.get("project_id", ""),
                                     detail=item.get("detail", "")):
                created += 1
        return created

"""Executive Decision Center.

The operational record of enterprise decisions: status, owner, impact,
follow-ups, and the evidence a decision rests on. Every decision is also
recorded into organizational decision memory (Knowledge Module) so the
Enterprise Brain learns from it — the Decision Center is the workspace
view, the knowledge store is the memory.
"""
from __future__ import annotations

from app.knowledge.store import KnowledgeStore
from app.manager.store import ManagerStore, new_id, now_iso

STATUSES = ("proposed", "approved", "rejected", "implemented", "superseded")


class DecisionCenter:
    def __init__(self, store: ManagerStore, knowledge: KnowledgeStore):
        self.store = store
        self.knowledge = knowledge

    def record(self, decision: str, owner: str = "", impact: str = "",
               status: str = "proposed", project_id: str = "",
               evidence_ids: list[str] | None = None,
               context: str = "") -> dict:
        if status not in STATUSES:
            raise ValueError(f"Unknown decision status: {status}")
        entry = {"decision_id": new_id("dec"), "decision": decision[:500],
                 "status": status, "owner": owner, "impact": impact[:500],
                 "project_id": project_id,
                 "evidence_ids": evidence_ids or [], "context": context[:500],
                 "follow_up_task_ids": [],
                 "history": [{"status": status, "at": now_iso(),
                              "by": owner}],
                 "created_at": now_iso()}
        self.store.append("decisions", entry)
        # organizational decision memory — the Brain learns every decision
        self.knowledge.record_decision(decision, context=context,
                                       project_id=project_id,
                                       source="decision_center")
        return entry

    def update(self, decision_id: str, status: str = "", owner: str = "",
               impact: str = "", by: str = "") -> dict | None:
        fields: dict = {}
        if status:
            if status not in STATUSES:
                raise ValueError(f"Unknown decision status: {status}")
            fields["status"] = status
        if owner:
            fields["owner"] = owner
        if impact:
            fields["impact"] = impact
        if not fields:
            return None
        current = next((d for d in self.store.read("decisions")
                        if d["decision_id"] == decision_id), None)
        if current is None:
            return None
        if status:
            fields["history"] = current.get("history", []) + [
                {"status": status, "at": now_iso(), "by": by or owner}]
        return self.store.update("decisions", "decision_id", decision_id,
                                 fields)

    def add_follow_up(self, decision_id: str, task_id: str) -> dict | None:
        current = next((d for d in self.store.read("decisions")
                        if d["decision_id"] == decision_id), None)
        if current is None:
            return None
        ids = current.get("follow_up_task_ids", [])
        if task_id not in ids:
            ids.append(task_id)
        return self.store.update("decisions", "decision_id", decision_id,
                                 {"follow_up_task_ids": ids})

    def decisions(self, status: str = "", limit: int = 50) -> list[dict]:
        items = self.store.read("decisions")
        if status:
            items = [d for d in items if d["status"] == status]
        return list(reversed(items))[:limit]

    def stats(self) -> dict:
        counts: dict[str, int] = {s: 0 for s in STATUSES}
        for d in self.store.read("decisions"):
            counts[d["status"]] = counts.get(d["status"], 0) + 1
        return counts

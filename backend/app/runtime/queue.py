"""Enterprise Action Queue — the execution centre of Enterprise Agent.

Nothing the platform does to the outside world happens inline. Every
communication, workflow run, approval, and automation is *queued* as an
action, and the queue decides what happens next:

    submit → pending_approval ──approve──> approved → executing → executed
                │                                          └─fail─> failed
                └──reject──> rejected
    submit → approved (auto)   when the action's kind needs no human

The approval policy is configuration, not code: ``requires_approval`` names
the action kinds a human must sign off. Sending email, creating meetings,
updating business rules, and executing automation require approval by
default; internal, reversible work (queueing a task, refreshing knowledge)
does not.

Executors are registered per action kind. An action whose kind has no
executor stays approved and waits — the queue is the seam where V2
communication providers plug in without touching any producer.
"""
from __future__ import annotations

import threading
from typing import Any, Callable

from app.core.logging import get_logger
from app.runtime.events import EventBus
from app.runtime.store import RuntimeStore, new_id, now_iso

logger = get_logger(__name__)

STATUSES = ("pending_approval", "approved", "rejected", "executing",
            "executed", "failed", "cancelled")
TERMINAL_STATUSES = ("rejected", "executed", "cancelled")

# Action kinds the platform can queue. External-effect kinds are listed in
# REQUIRES_APPROVAL_DEFAULT — an autonomous agent may decide anything, but
# it does not speak for the business without a human.
ACTION_KINDS = ("send_email", "create_meeting", "send_message",
                "update_business_rule", "execute_automation", "run_workflow",
                "create_task", "generate_report", "refresh_knowledge",
                "record_recommendation", "notify")

REQUIRES_APPROVAL_DEFAULT = ("send_email", "create_meeting", "send_message",
                             "update_business_rule", "execute_automation")

MAX_ACTIONS = 500


class ActionQueue:
    def __init__(self, store: RuntimeStore, bus: EventBus,
                 requires_approval: tuple[str, ...] | list[str] =
                 REQUIRES_APPROVAL_DEFAULT):
        self._store = store
        self._bus = bus
        self._requires_approval = set(requires_approval)
        self._executors: dict[str, Callable[[dict], Any]] = {}
        self._lock = threading.RLock()

    # -------------------------------------------------------------- policy
    def register_executor(self, kind: str,
                          executor: Callable[[dict], Any]) -> None:
        if kind not in ACTION_KINDS:
            raise ValueError(f"Unknown action kind: {kind}")
        self._executors[kind] = executor

    def requires_approval(self, kind: str) -> bool:
        return kind in self._requires_approval

    def policy(self) -> dict:
        return {"requires_approval": sorted(self._requires_approval),
                "auto_execute": sorted(set(ACTION_KINDS)
                                       - self._requires_approval),
                "executors": sorted(self._executors),
                "awaiting_executor": sorted(set(ACTION_KINDS)
                                            - set(self._executors))}

    # -------------------------------------------------------------- submit
    def submit(self, kind: str, title: str, payload: dict | None = None,
               detail: str = "", priority: int = 5, project_id: str = "",
               source: str = "runtime", source_ref: str = "",
               confidence: float | None = None,
               evidence_ids: list[str] | None = None) -> dict | None:
        """Queue an action. Returns None when an equivalent open action is
        already queued — an autonomous loop that observes the same condition
        twice must not queue the same action twice."""
        if kind not in ACTION_KINDS:
            raise ValueError(f"Unknown action kind: {kind}")
        signature = f"{kind}:{source_ref or title.strip().lower()}"
        with self._lock:
            if any(a["signature"] == signature
                   and a["status"] not in TERMINAL_STATUSES
                   for a in self._store.read("actions")):
                return None
            needs_approval = self.requires_approval(kind)
            action = {
                "action_id": new_id("act"), "kind": kind, "title": title[:300],
                "detail": detail[:800], "payload": payload or {},
                "status": "pending_approval" if needs_approval else "approved",
                "requires_approval": needs_approval, "priority": priority,
                "project_id": project_id, "source": source,
                "source_ref": source_ref, "signature": signature,
                "confidence": confidence, "evidence_ids": evidence_ids or [],
                "created_at": now_iso(), "updated_at": now_iso(),
                "approved_by": "", "approved_at": "", "rejected_reason": "",
                "executed_at": "", "result": None, "error": "", "attempts": 0,
            }
            self._store.append("actions", action, cap=MAX_ACTIONS)
        self._bus.publish("ActionQueued",
                          {"action_id": action["action_id"], "kind": kind,
                           "title": action["title"],
                           "requires_approval": needs_approval},
                          project_id=project_id, source=source)
        return action

    # ------------------------------------------------------------ approval
    def approve(self, action_id: str, by: str = "") -> dict:
        action = self._require(action_id)
        if action["status"] != "pending_approval":
            raise ValueError(
                f"Action is {action['status']}, not pending approval")
        updated = self._store.update("actions", "action_id", action_id,
                                     {"status": "approved", "approved_by": by,
                                      "approved_at": now_iso()})
        self._bus.publish("ActionApproved",
                          {"action_id": action_id, "kind": action["kind"],
                           "by": by}, project_id=action["project_id"],
                          source="approval")
        return updated

    def reject(self, action_id: str, by: str = "", reason: str = "") -> dict:
        action = self._require(action_id)
        if action["status"] != "pending_approval":
            raise ValueError(
                f"Action is {action['status']}, not pending approval")
        updated = self._store.update("actions", "action_id", action_id,
                                     {"status": "rejected", "approved_by": by,
                                      "rejected_reason": reason[:300]})
        self._bus.publish("ActionRejected",
                          {"action_id": action_id, "kind": action["kind"],
                           "by": by, "reason": reason[:200]},
                          project_id=action["project_id"], source="approval")
        return updated

    def edit(self, action_id: str, title: str = "", detail: str = "",
             payload: dict | None = None, by: str = "") -> dict:
        """Edit an action before it executes (V2 Approval Engine): the
        manager can rewrite the draft — subject, body, recipients — instead
        of only accepting or rejecting it. Allowed while the action is
        pending approval or approved-but-not-executed; the edit trail is
        kept on the action."""
        action = self._require(action_id)
        if action["status"] not in ("pending_approval", "approved"):
            raise ValueError(
                f"Action is {action['status']} — only queued actions can "
                f"be edited")
        fields: dict[str, Any] = {"updated_at": now_iso()}
        changed: list[str] = []
        if title.strip():
            fields["title"] = title.strip()[:300]
            changed.append("title")
        if detail.strip():
            fields["detail"] = detail.strip()[:800]
            changed.append("detail")
        if payload:
            fields["payload"] = {**(action.get("payload") or {}), **payload}
            changed.append("payload")
        if not changed:
            return action
        edits = list(action.get("edits") or [])
        edits.append({"by": by, "fields": changed, "at": now_iso()})
        fields["edits"] = edits[-10:]
        updated = self._store.update("actions", "action_id", action_id, fields)
        self._bus.publish("ActionEdited",
                          {"action_id": action_id, "kind": action["kind"],
                           "by": by, "fields": changed},
                          project_id=action["project_id"], source="approval")
        return updated

    def cancel(self, action_id: str, reason: str = "") -> dict:
        action = self._require(action_id)
        if action["status"] in TERMINAL_STATUSES:
            raise ValueError(f"Action is already {action['status']}")
        return self._store.update("actions", "action_id", action_id,
                                  {"status": "cancelled",
                                   "rejected_reason": reason[:300]})

    # ----------------------------------------------------------- execution
    def execute_ready(self, limit: int = 20) -> dict[str, int]:
        """Execute approved actions that have an executor, highest priority
        first. This is what the scheduler's ``action_queue`` job calls every
        tick — the queue drains itself, nobody pushes it."""
        ready = [a for a in self.actions(status="approved", limit=MAX_ACTIONS)
                 if a["kind"] in self._executors][:limit]
        executed, failed = 0, 0
        for action in ready:
            outcome = self.execute(action["action_id"])
            if outcome["status"] == "executed":
                executed += 1
            else:
                failed += 1
        return {"executed": executed, "failed": failed,
                "waiting_for_executor": sum(
                    1 for a in self.actions(status="approved", limit=MAX_ACTIONS)
                    if a["kind"] not in self._executors)}

    def execute(self, action_id: str) -> dict:
        """Execute one approved action. Never raises: a failed action is
        recorded and announced, so the queue keeps draining."""
        action = self._require(action_id)
        if action["status"] != "approved":
            raise ValueError(f"Action is {action['status']}, not approved")
        executor = self._executors.get(action["kind"])
        if executor is None:
            raise RuntimeError(
                f"No executor registered for action kind '{action['kind']}'")

        self._store.update("actions", "action_id", action_id,
                           {"status": "executing",
                            "attempts": action["attempts"] + 1})
        try:
            result = executor(action)
        except Exception as exc:  # noqa: BLE001 — one bad action never stops the queue
            logger.exception("Action %s (%s) failed", action_id,
                             action["kind"])
            updated = self._store.update(
                "actions", "action_id", action_id,
                {"status": "failed", "error": str(exc)[:300]})
            self._bus.publish("ActionFailed",
                              {"action_id": action_id, "kind": action["kind"],
                               "error": str(exc)[:200]},
                              project_id=action["project_id"], source="queue")
            return updated

        updated = self._store.update(
            "actions", "action_id", action_id,
            {"status": "executed", "executed_at": now_iso(),
             "result": _small(result), "error": ""})
        self._bus.publish("ActionExecuted",
                          {"action_id": action_id, "kind": action["kind"],
                           "title": action["title"]},
                          project_id=action["project_id"], source="queue")
        return updated

    def retry(self, action_id: str) -> dict:
        """Return a failed action to the approved state so the next drain
        picks it up — approval already given is not asked for twice."""
        action = self._require(action_id)
        if action["status"] != "failed":
            raise ValueError(f"Action is {action['status']}, not failed")
        return self._store.update("actions", "action_id", action_id,
                                  {"status": "approved", "error": ""})

    # ---------------------------------------------------------------- read
    def actions(self, status: str = "", kind: str = "", project_id: str = "",
                limit: int = 100) -> list[dict]:
        items = self._store.read("actions")
        if status:
            items = [a for a in items if a["status"] == status]
        if kind:
            items = [a for a in items if a["kind"] == kind]
        if project_id:
            items = [a for a in items if a["project_id"] == project_id]
        items.sort(key=lambda a: (a.get("priority", 5), a["created_at"]))
        return items[:limit]

    def pending_approvals(self, limit: int = 50) -> list[dict]:
        return self.actions(status="pending_approval", limit=limit)

    def recent(self, limit: int = 20) -> list[dict]:
        items = sorted(self._store.read("actions"),
                       key=lambda a: a.get("updated_at") or a["created_at"],
                       reverse=True)
        return items[:limit]

    def stats(self) -> dict:
        items = self._store.read("actions")
        by_status = {s: 0 for s in STATUSES}
        by_kind: dict[str, int] = {}
        for a in items:
            by_status[a["status"]] = by_status.get(a["status"], 0) + 1
            by_kind[a["kind"]] = by_kind.get(a["kind"], 0) + 1
        return {"total": len(items), "by_status": by_status,
                "by_kind": by_kind,
                "pending_approval": by_status["pending_approval"],
                "in_flight": by_status["approved"] + by_status["executing"]}

    def _require(self, action_id: str) -> dict:
        action = self._store.get("actions", "action_id", action_id)
        if action is None:
            raise KeyError(f"Unknown action: {action_id}")
        return action


def _small(result: Any) -> Any:
    """Executor results are persisted and served over the API — keep them
    bounded and JSON-safe."""
    if result is None or isinstance(result, (bool, int, float)):
        return result
    if isinstance(result, str):
        return result[:300]
    if isinstance(result, dict):
        return {k: _small(v) for k, v in list(result.items())[:20]}
    if isinstance(result, (list, tuple)):
        return [_small(v) for v in list(result)[:20]]
    return str(result)[:300]

"""Planning Engine — goals become executable work.

The Planner Module already plans *within* a run (the graph's ExecutionPlan)
and routes an interactive goal to an agent (``PlannerAgent``). This engine
is the third planning surface the SDS calls for and the one autonomy needs:
it turns a *business* objective into a durable plan of steps, each of which
is either a workflow to run or an action to queue, and it keeps that plan
honest as conditions change.

    goal → plan → steps → (workflow | action) → completion → replan

Replanning is what makes the plan autonomous rather than a to-do list
written once: when a goal stalls, its deadline closes in, or a step fails
repeatedly, the engine revises the remaining steps instead of waiting for
the manager to notice.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.runtime.events import Event, EventBus
from app.runtime.goals import GoalEngine
from app.runtime.queue import ActionQueue
from app.runtime.store import RuntimeStore, new_id, now_iso

logger = get_logger(__name__)

PLAN_STATUSES = ("draft", "active", "completed", "superseded", "failed")
STEP_STATUSES = ("pending", "running", "completed", "failed", "skipped")
STEP_KINDS = ("workflow", "action", "measure")

# A step that fails this many times stops being retried and triggers a replan.
MAX_STEP_ATTEMPTS = 3
# Below this progress with the deadline this close, the plan is revised.
REPLAN_PROGRESS = 0.5
REPLAN_DAYS = 21


class PlanningEngine:
    def __init__(self, store: RuntimeStore, bus: EventBus, goals: GoalEngine,
                 queue: ActionQueue, workflows=None):
        self._store = store
        self._bus = bus
        self._goals = goals
        self._queue = queue
        self._workflows = workflows
        bus.subscribe("GoalCreated", self._on_goal_created,
                      name="planning_engine.plan")
        bus.subscribe("GoalProgressed", self._on_goal_progressed,
                      name="planning_engine.replan")

    # ---------------------------------------------------------------- plan
    def plan_for_goal(self, goal_id: str) -> dict | None:
        """Break an objective into steps. Deterministic and idempotent: the
        same goal yields the same plan, and an existing active plan is
        returned rather than duplicated."""
        goal = self._goals.get(goal_id)
        if goal is None:
            return None
        existing = self.plan_for(goal_id)
        if existing and existing["status"] == "active":
            return existing

        steps = self._decompose(goal)
        plan = {"plan_id": new_id("plan"), "kind": "plan", "goal_id": goal_id,
                "objective": goal["objective"], "status": "active",
                "project_id": goal.get("project_id", ""), "steps": steps,
                "revision": 1, "replan_reason": "",
                "created_at": now_iso(), "updated_at": now_iso()}
        self._store.append("plans", plan)
        self._goals.attach_plan(goal_id, plan["plan_id"])
        logger.info("Planned goal %s into %d steps", goal_id, len(steps))
        return plan

    def _decompose(self, goal: dict) -> list[dict]:
        """Objective → steps. Every goal needs current data, a measurement of
        each KPI, and a review; KPIs that are behind get their own
        investigation step. This is the deterministic backbone — the
        Recommendation Module supplies the content, planning supplies the
        order."""
        steps: list[dict] = [
            self._step("Refresh the portfolio and knowledge behind this goal",
                       "workflow", {"workflow": "background_intelligence"}),
        ]
        for kpi in goal["kpis"]:
            steps.append(self._step(
                f"Measure {kpi['name']} against its target of "
                f"{kpi['target']}{kpi['unit']}", "measure",
                {"goal_id": goal["goal_id"], "kpi": kpi["name"],
                 "metric": kpi.get("metric", "")}))
            if kpi.get("current") is not None and kpi["attainment"] < 0.5:
                steps.append(self._step(
                    f"Investigate why {kpi['name']} is behind target",
                    "action", {"action_kind": "create_task",
                               "title": f"Investigate {kpi['name']} shortfall "
                                        f"against goal: {goal['objective'][:80]}",
                               "priority": 2}))
        steps.append(self._step(
            f"Report progress on: {goal['objective'][:120]}", "action",
            {"action_kind": "create_task",
             "title": f"Review goal progress: {goal['objective'][:100]}",
             "priority": 4}))
        return steps

    def _step(self, title: str, kind: str, params: dict) -> dict:
        if kind not in STEP_KINDS:
            raise ValueError(f"Unknown plan step kind: {kind}")
        return {"step_id": new_id("step"), "title": title[:250], "kind": kind,
                "params": params, "status": "pending", "attempts": 0,
                "result": None, "error": "", "started_at": "",
                "finished_at": ""}

    # ------------------------------------------------------------- execute
    def advance(self, plan_id: str, limit: int = 3) -> dict[str, Any]:
        """Run the next pending steps of a plan. Steps run in order — a plan
        is a sequence, not a bag — and a step that fails past its attempt
        budget triggers a replan instead of blocking the goal forever."""
        plan = self._plan(plan_id)
        if plan is None or plan["status"] != "active":
            return {"advanced": 0, "status": plan["status"] if plan else "unknown"}

        advanced, failed = 0, 0
        for step in plan["steps"]:
            if advanced >= limit:
                break
            if step["status"] in ("completed", "skipped"):
                continue
            if step["status"] == "failed" and step["attempts"] >= MAX_STEP_ATTEMPTS:
                continue  # exhausted — the replan sweep handles it
            outcome = self._run_step(plan, step)
            advanced += 1
            if outcome == "failed":
                failed += 1
                break  # a sequence stops at its first unresolved failure

        if all(s["status"] in ("completed", "skipped") for s in plan["steps"]):
            plan["status"] = "completed"
        plan["updated_at"] = now_iso()
        self._save(plan)
        return {"advanced": advanced, "failed": failed,
                "status": plan["status"],
                "remaining": sum(1 for s in plan["steps"]
                                 if s["status"] == "pending")}

    def _run_step(self, plan: dict, step: dict) -> str:
        step["attempts"] += 1
        step["status"] = "running"
        step["started_at"] = now_iso()
        try:
            step["result"] = self._dispatch(plan, step)
            step["status"] = "completed"
            step["error"] = ""
        except Exception as exc:  # noqa: BLE001 — a step fails, the plan survives
            logger.exception("Plan step failed: %s", step["title"])
            step["status"] = "failed"
            step["error"] = str(exc)[:300]
        step["finished_at"] = now_iso()
        return step["status"]

    def _dispatch(self, plan: dict, step: dict) -> Any:
        kind, params = step["kind"], step["params"]
        if kind == "workflow":
            if self._workflows is None:
                raise RuntimeError("No workflow engine wired into planning")
            return self._workflows.run(params["workflow"],
                                       plan.get("project_id", ""))
        if kind == "action":
            queued = self._queue.submit(
                params.get("action_kind", "create_task"),
                params.get("title", step["title"]),
                payload={"plan_id": plan["plan_id"], "step_id": step["step_id"],
                         "goal_id": plan["goal_id"]},
                detail=f"Planned step for goal: {plan['objective'][:150]}",
                priority=params.get("priority", 5),
                project_id=plan.get("project_id", ""), source="planning_engine",
                source_ref=f"{plan['plan_id']}:{step['step_id']}")
            return {"queued": queued is not None,
                    "action_id": queued["action_id"] if queued else ""}
        if kind == "measure":
            goal = self._goals.get(params["goal_id"])
            if goal is None:
                raise RuntimeError(f"Goal {params['goal_id']} no longer exists")
            kpi = next((k for k in goal["kpis"] if k["name"] == params["kpi"]),
                       None)
            return {"kpi": params["kpi"],
                    "current": kpi.get("current") if kpi else None,
                    "attainment": kpi.get("attainment") if kpi else None}
        raise RuntimeError(f"Unknown step kind: {kind}")

    def advance_all(self, limit_per_plan: int = 2) -> dict[str, int]:
        """The scheduler's planning job: move every active plan forward."""
        advanced, completed = 0, 0
        for plan in self.plans(status="active"):
            outcome = self.advance(plan["plan_id"], limit=limit_per_plan)
            advanced += outcome["advanced"]
            if outcome["status"] == "completed":
                completed += 1
        return {"steps_advanced": advanced, "plans_completed": completed}

    # -------------------------------------------------------------- replan
    def replan(self, plan_id: str, reason: str) -> dict | None:
        """Supersede a plan with a fresh decomposition of its goal, carrying
        completed steps forward — replanning revises the route, it does not
        discard the distance already travelled."""
        plan = self._plan(plan_id)
        if plan is None:
            return None
        goal = self._goals.get(plan["goal_id"])
        if goal is None:
            return None

        done = {s["title"] for s in plan["steps"]
                if s["status"] == "completed"}
        revised = [s for s in self._decompose(goal) if s["title"] not in done]
        plan["status"] = "superseded"
        plan["updated_at"] = now_iso()
        self._save(plan)

        successor = {"plan_id": new_id("plan"), "kind": "plan",
                     "goal_id": plan["goal_id"], "objective": goal["objective"],
                     "status": "active", "project_id": plan.get("project_id", ""),
                     "steps": [s for s in plan["steps"]
                               if s["status"] == "completed"] + revised,
                     "revision": plan["revision"] + 1, "replan_reason": reason[:200],
                     "supersedes": plan_id, "created_at": now_iso(),
                     "updated_at": now_iso()}
        self._store.append("plans", successor)
        self._goals.attach_plan(plan["goal_id"], successor["plan_id"])
        logger.info("Replanned goal %s (revision %d): %s", plan["goal_id"],
                    successor["revision"], reason)
        return successor

    def replan_sweep(self) -> dict[str, int]:
        """Conditions changed? Revise. Runs on the scheduler, so a stalled
        goal is re-planned without the manager asking."""
        replanned = 0
        for plan in self.plans(status="active"):
            reason = self._replan_reason(plan)
            if reason and self.replan(plan["plan_id"], reason):
                replanned += 1
        return {"replanned": replanned}

    def _replan_reason(self, plan: dict) -> str:
        exhausted = [s for s in plan["steps"]
                     if s["status"] == "failed"
                     and s["attempts"] >= MAX_STEP_ATTEMPTS]
        if exhausted:
            return f"{len(exhausted)} step(s) failed past their attempt budget"
        goal = self._goals.get(plan["goal_id"])
        if goal is None:
            return ""
        if goal["status"] == "achieved":
            return ""
        remaining = self._goals.days_remaining(goal)
        if remaining is not None and 0 <= remaining <= REPLAN_DAYS \
                and goal["progress"] < REPLAN_PROGRESS:
            return (f"deadline in {remaining}d with progress at "
                    f"{goal['progress']:.0%}")
        return ""

    # -------------------------------------------------------------- events
    def _on_goal_created(self, event: Event) -> None:
        self.plan_for_goal(event.payload["goal_id"])

    def _on_goal_progressed(self, event: Event) -> None:
        goal_id = event.payload.get("goal_id", "")
        plan = self.plan_for(goal_id)
        if plan is None or plan["status"] != "active":
            return
        if event.payload.get("status") == "at_risk":
            self.replan(plan["plan_id"], "the goal is at risk of missing its "
                                         "deadline")

    # ---------------------------------------------------------------- read
    def plans(self, status: str = "", goal_id: str = "",
              limit: int = 50) -> list[dict]:
        items = [p for p in self._store.read("plans") if p.get("kind") == "plan"]
        if status:
            items = [p for p in items if p["status"] == status]
        if goal_id:
            items = [p for p in items if p["goal_id"] == goal_id]
        return list(reversed(items))[:limit]  # newest first

    def plan_for(self, goal_id: str) -> dict | None:
        active = [p for p in self.plans(goal_id=goal_id)
                  if p["status"] == "active"]
        return active[0] if active else None

    def _plan(self, plan_id: str) -> dict | None:
        for plan in self._store.read("plans"):
            if plan.get("kind") == "plan" and plan["plan_id"] == plan_id:
                return plan
        return None

    def _save(self, plan: dict) -> None:
        """Persist a plan the caller has been holding.

        Advancing a plan takes as long as its steps do, and the scheduler
        thread and an API request can be inside ``advance`` and ``replan``
        for the same goal at once. Two rules keep that honest: the
        read-modify-write is atomic, and a plan another thread superseded
        while we were working never comes back.
        """
        with self._store.mutate("plans") as plans:
            for i, existing in enumerate(plans):
                if existing.get("plan_id") != plan["plan_id"]:
                    continue
                if existing.get("status") == "superseded" \
                        and plan["status"] != "superseded":
                    return
                plans[i] = plan
                return

    def stats(self) -> dict:
        plans = self.plans(limit=200)
        steps = [s for p in plans for s in p["steps"]]
        return {"total": len(plans),
                "active": sum(1 for p in plans if p["status"] == "active"),
                "completed": sum(1 for p in plans if p["status"] == "completed"),
                "superseded": sum(1 for p in plans if p["status"] == "superseded"),
                "steps_total": len(steps),
                "steps_completed": sum(1 for s in steps
                                       if s["status"] == "completed"),
                "steps_pending": sum(1 for s in steps
                                     if s["status"] == "pending")}

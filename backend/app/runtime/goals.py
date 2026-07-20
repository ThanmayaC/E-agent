"""Agent Goal Engine — what the manager wants, kept in front of the agent.

A goal is an objective with measurable KPIs, business targets, and a
deadline. The manager states it once; the platform then works toward it
continuously — the Planning Engine turns it into workflows, background jobs
measure it, and progress is reported back without anyone asking.

Progress is measured, never asserted: each KPI carries a target, a
direction, and a current value refreshed from the platform's own metrics.
Goal progress is the mean of its KPIs' individual attainment, so a goal
cannot look healthy because one metric ran ahead.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

from app.core.logging import get_logger
from app.runtime.events import EventBus
from app.runtime.store import RuntimeStore, new_id, now_iso

logger = get_logger(__name__)

STATUSES = ("active", "achieved", "at_risk", "missed", "paused", "cancelled")
DIRECTIONS = ("increase", "decrease", "maintain")
HORIZONS = ("quarter", "month", "week", "year", "open")

# A goal whose deadline is inside this window and below this attainment is
# flagged at_risk, so the manager hears about it while it can still move.
AT_RISK_DAYS = 14
AT_RISK_ATTAINMENT = 0.6


class GoalEngine:
    def __init__(self, store: RuntimeStore, bus: EventBus):
        self._store = store
        self._bus = bus

    # -------------------------------------------------------------- create
    def create(self, objective: str, kpis: list[dict] | None = None,
               deadline: str = "", owner: str = "", horizon: str = "quarter",
               project_id: str = "", detail: str = "") -> dict:
        """Define an objective.

        Each KPI: ``{"name", "target", "direction", "baseline", "unit",
        "metric"}`` — ``metric`` names the platform metric that measures it
        (e.g. ``portfolio.average_health_score``), which is what lets the
        background jobs refresh it without a human typing numbers in.
        """
        if horizon not in HORIZONS:
            raise ValueError(f"Unknown horizon: {horizon}")
        goal = {"goal_id": new_id("goal"), "objective": objective[:300],
                "detail": detail[:800], "kpis": [self._kpi(k)
                                                 for k in (kpis or [])],
                "deadline": deadline, "owner": owner, "horizon": horizon,
                "project_id": project_id, "status": "active", "progress": 0.0,
                "plan_id": "", "created_at": now_iso(),
                "updated_at": now_iso(), "achieved_at": ""}
        self._store.append("goals", goal)
        self._bus.publish("GoalCreated",
                          {"goal_id": goal["goal_id"],
                           "objective": goal["objective"],
                           "kpis": len(goal["kpis"]), "deadline": deadline},
                          project_id=project_id, source="goal_engine")
        return goal

    def _kpi(self, spec: dict) -> dict:
        direction = spec.get("direction", "increase")
        if direction not in DIRECTIONS:
            raise ValueError(f"Unknown KPI direction: {direction}")
        if spec.get("target") is None:
            raise ValueError(f"KPI {spec.get('name')!r} needs a target")
        return {"name": str(spec.get("name", ""))[:120],
                "metric": str(spec.get("metric", ""))[:120],
                "target": float(spec["target"]),
                "baseline": (float(spec["baseline"])
                             if spec.get("baseline") is not None else None),
                "current": (float(spec["current"])
                            if spec.get("current") is not None else None),
                "direction": direction, "unit": str(spec.get("unit", ""))[:20],
                "attainment": 0.0, "measured_at": ""}

    # ------------------------------------------------------------ progress
    def record_measurement(self, goal_id: str, kpi_name: str,
                           value: float) -> dict | None:
        """Set a KPI's current value and recompute the goal's progress."""
        goal = self._store.get("goals", "goal_id", goal_id)
        if goal is None:
            return None
        for kpi in goal["kpis"]:
            if kpi["name"] == kpi_name:
                kpi["current"] = float(value)
                kpi["measured_at"] = now_iso()
                kpi["attainment"] = self._attainment(kpi)
        return self._recompute(goal)

    def refresh(self, goal_id: str, metrics: dict[str, float]) -> dict | None:
        """Refresh every KPI whose ``metric`` appears in the supplied metric
        snapshot. This is the seam the background intelligence job uses —
        goals measure themselves from the platform's own numbers."""
        goal = self._store.get("goals", "goal_id", goal_id)
        if goal is None:
            return None
        for kpi in goal["kpis"]:
            metric = kpi.get("metric")
            if metric and metric in metrics and metrics[metric] is not None:
                kpi["current"] = float(metrics[metric])
                kpi["measured_at"] = now_iso()
            kpi["attainment"] = self._attainment(kpi)
        return self._recompute(goal)

    def refresh_all(self, metrics: dict[str, float]) -> dict[str, Any]:
        refreshed, achieved, at_risk = 0, 0, 0
        for goal in self.goals(status="active"):
            updated = self.refresh(goal["goal_id"], metrics)
            if updated is None:
                continue
            refreshed += 1
            if updated["status"] == "achieved":
                achieved += 1
            elif updated["status"] == "at_risk":
                at_risk += 1
        return {"refreshed": refreshed, "achieved": achieved,
                "at_risk": at_risk}

    def _attainment(self, kpi: dict) -> float:
        """How far this KPI has travelled from its baseline to its target,
        clamped to 0..1. Without a baseline, attainment is a plain ratio to
        target (direction-aware)."""
        current, target = kpi.get("current"), kpi["target"]
        if current is None:
            return 0.0
        baseline = kpi.get("baseline")
        direction = kpi["direction"]
        if direction == "maintain":
            if target == 0:
                return 1.0 if current == 0 else 0.0
            drift = abs(current - target) / abs(target)
            return round(max(0.0, 1.0 - drift), 3)
        if baseline is not None and baseline != target:
            progress = (current - baseline) / (target - baseline)
            return round(min(max(progress, 0.0), 1.0), 3)
        if target == 0:
            return 1.0 if current == 0 else 0.0
        ratio = current / target if direction == "increase" else target / current \
            if current else 0.0
        return round(min(max(ratio, 0.0), 1.0), 3)

    def _recompute(self, goal: dict) -> dict:
        kpis = goal["kpis"]
        previous_progress = goal["progress"]
        goal["progress"] = round(
            sum(k["attainment"] for k in kpis) / len(kpis), 3) if kpis else 0.0
        goal["updated_at"] = now_iso()

        if goal["status"] in ("active", "at_risk"):
            if kpis and all(k["attainment"] >= 1.0 for k in kpis):
                goal["status"] = "achieved"
                goal["achieved_at"] = now_iso()
            elif self._at_risk(goal):
                goal["status"] = "at_risk"
            else:
                goal["status"] = "active"

        self._save(goal)
        if goal["status"] == "achieved" and previous_progress < 1.0:
            self._bus.publish("GoalAchieved",
                              {"goal_id": goal["goal_id"],
                               "objective": goal["objective"]},
                              project_id=goal.get("project_id", ""),
                              source="goal_engine")
        elif goal["progress"] != previous_progress:
            self._bus.publish("GoalProgressed",
                              {"goal_id": goal["goal_id"],
                               "objective": goal["objective"],
                               "progress": goal["progress"],
                               "previous": previous_progress,
                               "status": goal["status"],
                               "days_remaining": self.days_remaining(goal)},
                              project_id=goal.get("project_id", ""),
                              source="goal_engine")
        return goal

    def _at_risk(self, goal: dict) -> bool:
        remaining = self.days_remaining(goal)
        if remaining is None:
            return False
        return remaining <= AT_RISK_DAYS and goal["progress"] < AT_RISK_ATTAINMENT

    def days_remaining(self, goal: dict) -> int | None:
        deadline = (goal.get("deadline") or "")[:10]
        if not deadline:
            return None
        try:
            due = datetime.fromisoformat(deadline).replace(tzinfo=timezone.utc)
        except ValueError:
            return None
        return (due - datetime.now(timezone.utc)).days

    # -------------------------------------------------------------- status
    def set_status(self, goal_id: str, status: str) -> dict | None:
        if status not in STATUSES:
            raise ValueError(f"Unknown goal status: {status}")
        return self._store.update("goals", "goal_id", goal_id,
                                  {"status": status})

    def attach_plan(self, goal_id: str, plan_id: str) -> dict | None:
        return self._store.update("goals", "goal_id", goal_id,
                                  {"plan_id": plan_id})

    def sweep_deadlines(self) -> dict[str, int]:
        """Goals past their deadline are missed, not eternally active."""
        missed, at_risk = 0, 0
        for goal in self.goals(status=""):
            if goal["status"] not in ("active", "at_risk"):
                continue
            remaining = self.days_remaining(goal)
            if remaining is not None and remaining < 0:
                self.set_status(goal["goal_id"], "missed")
                missed += 1
            elif self._at_risk(goal) and goal["status"] != "at_risk":
                self.set_status(goal["goal_id"], "at_risk")
                at_risk += 1
        return {"missed": missed, "at_risk": at_risk}

    # ---------------------------------------------------------------- read
    def goals(self, status: str = "", project_id: str = "",
              limit: int = 100) -> list[dict]:
        items = self._store.read("goals")
        if status:
            items = [g for g in items if g["status"] == status]
        if project_id:
            items = [g for g in items if g.get("project_id") == project_id]
        return items[:limit]

    def get(self, goal_id: str) -> dict | None:
        return self._store.get("goals", "goal_id", goal_id)

    def progress_report(self) -> dict:
        """The Goal Progress panel: where every objective stands."""
        goals = self.goals()
        active = [g for g in goals if g["status"] in ("active", "at_risk")]
        return {
            "total": len(goals),
            "active": len(active),
            "achieved": sum(1 for g in goals if g["status"] == "achieved"),
            "at_risk": sum(1 for g in goals if g["status"] == "at_risk"),
            "missed": sum(1 for g in goals if g["status"] == "missed"),
            "average_progress": round(
                sum(g["progress"] for g in active) / len(active), 3)
            if active else 0.0,
            "goals": [{"goal_id": g["goal_id"], "objective": g["objective"],
                       "status": g["status"], "progress": g["progress"],
                       "deadline": g["deadline"], "owner": g["owner"],
                       "days_remaining": self.days_remaining(g),
                       "kpis": [{"name": k["name"], "current": k["current"],
                                 "target": k["target"], "unit": k["unit"],
                                 "attainment": k["attainment"]}
                                for k in g["kpis"]]}
                      for g in sorted(goals,
                                      key=lambda g: (g["status"] != "at_risk",
                                                     g["progress"]))[:20]],
        }

    def _save(self, goal: dict) -> None:
        # Atomic: the scheduler's goal_refresh job and an API measurement can
        # recompute the same goal at once, and a plain read-then-write pair
        # would drop whichever landed first.
        with self._store.mutate("goals") as goals:
            for i, existing in enumerate(goals):
                if existing["goal_id"] == goal["goal_id"]:
                    goals[i] = goal
                    return

    @staticmethod
    def default_deadline(days: int = 90) -> str:
        return (datetime.now(timezone.utc) + timedelta(days=days)).date().isoformat()

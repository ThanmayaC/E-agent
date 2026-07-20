"""Enterprise Workflow Engine.

Workflows are named, registered units of autonomous work (full analysis,
report review, monitoring, follow-ups, recurring briefings, ...). The engine
runs them, persists every run for the Workflow Monitoring UI, and keeps a
schedule scaffold for recurring work.

Two shapes of workflow share one engine and one run history:

- a **single-runner** workflow wraps one callable (``full_analysis`` — the
  analysis graph);
- an **autonomous** workflow is an ordered chain of named steps that the
  engine executes without a user, recording each step on the run (see
  ``app.workflows.autonomous``).

Runs announce themselves on the event bus when one is wired in, which is
what lets triggers, plans, and the Action Queue react to work finishing
without the engine knowing any of them exist.
"""
from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable

from app.core.logging import get_logger
from app.repositories.artifact_store import ArtifactStore

logger = get_logger(__name__)

# A workflow with no project scope (portfolio-wide background work) runs
# under this pseudo-project so its run history has a durable home.
ENTERPRISE_SCOPE = "_enterprise"


@dataclass
class WorkflowStep:
    """One step of an autonomous workflow.

    ``run`` takes the project id and the results of the steps before it, so
    a chain can pass work forward (refresh → analyse → brief → queue).
    ``optional`` marks a step whose failure degrades the run instead of
    ending it.
    """
    name: str
    description: str
    run: Callable[[str, dict], Any]
    optional: bool = False

    def describe(self) -> dict:
        return {"name": self.name, "description": self.description,
                "optional": self.optional}


@dataclass
class WorkflowDefinition:
    name: str
    description: str
    runner: Callable[[str], Any] | None = None  # project_id -> result
    available: bool = True
    unavailable_reason: str = ""
    tags: list[str] = field(default_factory=list)
    steps: list[WorkflowStep] = field(default_factory=list)
    autonomous: bool = False   # runs without user interaction
    scope: str = "project"     # project | enterprise

    def __post_init__(self) -> None:
        if self.steps and self.runner is not None:
            raise ValueError(
                f"Workflow {self.name}: give it steps or a runner, not both")

    def describe(self) -> dict:
        return {"name": self.name, "description": self.description,
                "available": self.available,
                "unavailable_reason": self.unavailable_reason,
                "tags": self.tags, "autonomous": self.autonomous,
                "scope": self.scope,
                "steps": [s.describe() for s in self.steps]}


class WorkflowEngine:
    def __init__(self, store: ArtifactStore, on_failure=None, bus=None):
        self._store = store
        self._definitions: dict[str, WorkflowDefinition] = {}
        # optional callback(workflow_name, project_id, error) — the
        # Communication Module's notification framework hooks in here
        self._on_failure = on_failure
        # optional EventBus — set by the runtime so completed work is
        # announced; absent (lite profile, tests) the engine behaves exactly
        # as it did before autonomy existed.
        self._bus = bus

    # --------------------------------------------------------- definitions
    def register(self, definition: WorkflowDefinition) -> None:
        self._definitions[definition.name] = definition

    def describe(self) -> list[dict]:
        return [d.describe() for d in self._definitions.values()]

    def definition(self, name: str) -> WorkflowDefinition | None:
        return self._definitions.get(name)

    def attach_bus(self, bus) -> None:
        """Wire the event bus after construction — the container builds the
        engine before the runtime exists."""
        self._bus = bus

    # --------------------------------------------------------------- runs
    def run(self, workflow_name: str, project_id: str) -> dict:
        definition = self._definitions.get(workflow_name)
        if definition is None:
            raise KeyError(f"Unknown workflow: {workflow_name}")
        if not definition.available or (definition.runner is None
                                        and not definition.steps):
            raise RuntimeError(
                f"Workflow '{workflow_name}' is not executable yet: "
                f"{definition.unavailable_reason or 'planned'}")
        if definition.scope == "enterprise":
            project_id = project_id or ENTERPRISE_SCOPE

        run = {"run_id": uuid.uuid4().hex[:12], "workflow": workflow_name,
               "project_id": project_id, "status": "running",
               "started_at": datetime.now(timezone.utc).isoformat(),
               "finished_at": None, "error": "",
               "autonomous": definition.autonomous, "steps": []}
        self._append_run(project_id, run)
        try:
            if definition.steps:
                run["steps"] = self._run_steps(definition, project_id)
            else:
                definition.runner(project_id)
            run["status"] = "completed"
        except Exception as exc:  # noqa: BLE001 — run record must always close
            logger.exception("Workflow %s failed for %s", workflow_name, project_id)
            run["status"] = "failed"
            run["error"] = str(exc)[:300]
            if self._on_failure is not None:
                try:
                    self._on_failure(workflow_name, project_id, str(exc))
                except Exception:  # noqa: BLE001 — notification is best-effort
                    logger.exception("Workflow failure notification failed")
        run["finished_at"] = datetime.now(timezone.utc).isoformat()
        self._update_run(project_id, run)
        self._announce(run)
        return run

    def _run_steps(self, definition: WorkflowDefinition,
                   project_id: str) -> list[dict]:
        """Execute an autonomous chain. Each step sees the results of the
        steps before it; a required step's failure ends the run, an optional
        step's failure is recorded and the chain continues."""
        results: dict[str, Any] = {}
        records: list[dict] = []
        for step in definition.steps:
            record = {"name": step.name, "status": "running",
                      "started_at": datetime.now(timezone.utc).isoformat(),
                      "finished_at": "", "error": ""}
            try:
                results[step.name] = step.run(project_id, dict(results))
                record["status"] = "completed"
                record["result"] = _brief(results[step.name])
            except Exception as exc:  # noqa: BLE001 — see docstring
                logger.exception("Workflow %s step %s failed", definition.name,
                                 step.name)
                record["status"] = "failed"
                record["error"] = str(exc)[:300]
                record["finished_at"] = datetime.now(timezone.utc).isoformat()
                records.append(record)
                if not step.optional:
                    raise RuntimeError(
                        f"step '{step.name}' failed: {str(exc)[:200]}") from exc
                continue
            record["finished_at"] = datetime.now(timezone.utc).isoformat()
            records.append(record)
        return records

    def _announce(self, run: dict) -> None:
        if self._bus is None:
            return
        try:
            kind = ("WorkflowCompleted" if run["status"] == "completed"
                    else "WorkflowFailed")
            self._bus.publish(kind, {"workflow": run["workflow"],
                                     "run_id": run["run_id"],
                                     "status": run["status"],
                                     "error": run["error"],
                                     "steps": len(run.get("steps") or [])},
                              project_id=run["project_id"], source="workflow_engine")
        except Exception:  # noqa: BLE001 — announcing never fails a run
            logger.exception("Workflow event publication failed")

    def runs(self, project_id: str, limit: int = 50) -> list[dict]:
        return (self._store.load(project_id, "workflow_runs", []) or [])[-limit:]

    def running(self, limit: int = 20) -> list[dict]:
        """Every in-flight run across the portfolio — the Executive
        Workspace's Running Workflows panel."""
        return [r for r in self.recent_runs(200)
                if r["status"] == "running"][:limit]

    def recent_runs(self, limit: int = 20) -> list[dict]:
        """Run history across every project plus enterprise-scoped work,
        newest first."""
        scopes = dict.fromkeys(list(self._store.list_projects())
                               + [ENTERPRISE_SCOPE])
        out = [run for pid in scopes for run in self.runs(pid, 50)]
        return sorted(out, key=lambda r: r["started_at"], reverse=True)[:limit]

    # ----------------------------------------------------------- schedule
    def schedule(self, project_id: str, workflow_name: str, cadence: str) -> dict:
        """Register recurring work (cadence: daily | weekly | monthly).

        Scheduling is a declaration today — execution by a beat process
        (Celery beat / cron) hooks in here without touching callers.
        """
        schedules = self._store.load(project_id, "workflow_schedules", []) or []
        entry = {"schedule_id": uuid.uuid4().hex[:12], "workflow": workflow_name,
                 "cadence": cadence, "created_at": datetime.now(timezone.utc).isoformat(),
                 "active": True}
        schedules.append(entry)
        self._store.save(project_id, "workflow_schedules", schedules)
        return entry

    def schedules(self, project_id: str) -> list[dict]:
        return self._store.load(project_id, "workflow_schedules", []) or []

    # ------------------------------------------------------------ helpers
    def _append_run(self, project_id: str, run: dict) -> None:
        runs = self._store.load(project_id, "workflow_runs", []) or []
        runs.append(run)
        self._store.save(project_id, "workflow_runs", runs[-200:])

    def _update_run(self, project_id: str, run: dict) -> None:
        runs = self._store.load(project_id, "workflow_runs", []) or []
        for i, r in enumerate(runs):
            if r.get("run_id") == run["run_id"]:
                runs[i] = run
                break
        self._store.save(project_id, "workflow_runs", runs)


def _brief(value: Any) -> Any:
    """Step results are persisted on the run record and served to the UI —
    keep them small and JSON-safe."""
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, str):
        return value[:200]
    if isinstance(value, dict):
        return {k: _brief(v) for k, v in list(value.items())[:10]}
    if isinstance(value, (list, tuple)):
        return [_brief(v) for v in list(value)[:10]]
    return str(value)[:200]


PLANNED_WORKFLOWS = [
    WorkflowDefinition("report_review", "Review a new report against history and flag deviations",
                       available=False, unavailable_reason="requires report comparison agent",
                       tags=["review"]),
    WorkflowDefinition("follow_up", "Draft and track follow-ups with owning teams",
                       available=False, unavailable_reason="requires email/calendar tools",
                       tags=["communication"]),
    WorkflowDefinition("executive_briefing", "Prepare a recurring executive briefing deck",
                       available=False, unavailable_reason="requires PowerPoint tool",
                       tags=["reporting"]),
]

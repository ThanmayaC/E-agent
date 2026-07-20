"""Enterprise Scheduler — the heartbeat of Enterprise Agent.

Jobs are named units of autonomous work owned by the runtime. Four kinds:

    startup   run once when the runtime starts (ordered by dependencies)
    interval  run every N seconds
    cron      run on a 5-field cron schedule
    event     run whenever an event kind is published on the bus

Dependency ordering, retry policies with exponential backoff, and failure
recovery are the scheduler's job, not each job's. Every execution is
recorded (``/runtime/executions``) and announced on the bus, so a job that
degrades is visible instead of silent.

The tick loop runs on a single daemon thread: jobs are enterprise
coordination work (refresh, plan, queue), not CPU work, and a single thread
means a job never races itself. A job that overruns its interval simply
runs again on the next tick after it returns.
"""
from __future__ import annotations

import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable

from app.core.logging import get_logger
from app.runtime.cron import CronError, CronSchedule
from app.runtime.events import Event, EventBus
from app.runtime.store import RuntimeStore, new_id, now_iso

logger = get_logger(__name__)

JOB_KINDS = ("startup", "interval", "cron", "event")
MAX_EXECUTIONS = 300
DEFAULT_TICK_SECONDS = 30


@dataclass
class RetryPolicy:
    """How many times to retry a failing job, and how long to wait."""
    attempts: int = 1           # total attempts, including the first
    backoff_seconds: float = 2.0
    backoff_multiplier: float = 2.0

    def delay_for(self, attempt: int) -> float:
        return self.backoff_seconds * (self.backoff_multiplier ** (attempt - 1))


@dataclass
class JobDefinition:
    name: str
    description: str
    kind: str                                   # startup | interval | cron | event
    run: Callable[[], Any]
    interval_seconds: float | None = None       # kind=interval
    cron: str = ""                              # kind=cron
    event: str = ""                             # kind=event
    depends_on: list[str] = field(default_factory=list)
    retry: RetryPolicy = field(default_factory=RetryPolicy)
    enabled: bool = True
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.kind not in JOB_KINDS:
            raise ValueError(f"Unknown job kind: {self.kind}")
        if self.kind == "interval" and not self.interval_seconds:
            raise ValueError(f"Job {self.name}: interval_seconds is required")
        if self.kind == "cron":
            if not self.cron:
                raise ValueError(f"Job {self.name}: cron expression is required")
            CronSchedule(self.cron)  # fail at registration, not at 03:00
        if self.kind == "event" and not self.event:
            raise ValueError(f"Job {self.name}: event is required")


@dataclass
class JobState:
    """Mutable runtime state, kept separate from the definition."""
    status: str = "idle"        # idle | running | completed | failed | disabled
    last_run_at: str = ""
    last_finished_at: str = ""
    last_error: str = ""
    next_run_at: str = ""
    runs: int = 0
    failures: int = 0
    consecutive_failures: int = 0


class EnterpriseScheduler:
    def __init__(self, bus: EventBus, store: RuntimeStore | None = None,
                 tick_seconds: float = DEFAULT_TICK_SECONDS):
        self._bus = bus
        self._store = store
        self._tick_seconds = tick_seconds
        self._definitions: dict[str, JobDefinition] = {}
        self._state: dict[str, JobState] = {}
        self._due: dict[str, float] = {}          # interval jobs: monotonic deadline
        self._cron: dict[str, CronSchedule] = {}
        self._lock = threading.RLock()
        self._thread: threading.Thread | None = None
        self._stop = threading.Event()
        self._started_at: str = ""
        self._ticks = 0

    # --------------------------------------------------------- registration
    def register(self, definition: JobDefinition) -> JobDefinition:
        with self._lock:
            self._definitions[definition.name] = definition
            self._state.setdefault(definition.name, JobState(
                status="idle" if definition.enabled else "disabled"))
            if definition.kind == "interval":
                self._due[definition.name] = (time.monotonic()
                                              + definition.interval_seconds)
            elif definition.kind == "cron":
                schedule = CronSchedule(definition.cron)
                self._cron[definition.name] = schedule
                self._schedule_next_cron(definition.name, schedule)
            elif definition.kind == "event":
                self._bus.subscribe(
                    definition.event,
                    lambda event, name=definition.name: self._on_event(name,
                                                                       event),
                    name=f"job:{definition.name}")
        return definition

    def enable(self, name: str, enabled: bool = True) -> dict:
        with self._lock:
            if name not in self._definitions:
                raise KeyError(f"Unknown job: {name}")
            self._definitions[name].enabled = enabled
            state = self._state[name]
            state.status = "idle" if enabled else "disabled"
            if enabled and self._definitions[name].kind == "interval":
                self._due[name] = (time.monotonic()
                                   + self._definitions[name].interval_seconds)
        return self.describe_job(name)

    # ------------------------------------------------------------ lifecycle
    def start(self) -> dict:
        """Run startup jobs in dependency order, then begin ticking."""
        with self._lock:
            if self._thread is not None and self._thread.is_alive():
                return self.status()
            self._stop.clear()
            self._started_at = now_iso()

        for name in self._startup_order():
            self.run_job(name, reason="startup")

        self._thread = threading.Thread(target=self._loop, name="enterprise-scheduler",
                                        daemon=True)
        self._thread.start()
        self._bus.publish("RuntimeStarted", {"jobs": len(self._definitions)},
                          source="scheduler")
        logger.info("Enterprise Scheduler started (%d jobs, tick %ss)",
                    len(self._definitions), self._tick_seconds)
        return self.status()

    def stop(self, timeout: float = 5.0) -> None:
        self._stop.set()
        thread = self._thread
        if thread is not None and thread.is_alive():
            thread.join(timeout=timeout)
        self._thread = None
        logger.info("Enterprise Scheduler stopped")

    @property
    def running(self) -> bool:
        return self._thread is not None and self._thread.is_alive()

    # ---------------------------------------------------------------- ticks
    def _loop(self) -> None:
        while not self._stop.wait(self._tick_seconds):
            try:
                self.tick()
            except Exception:  # noqa: BLE001 — the heartbeat never dies of one bad beat
                logger.exception("Scheduler tick failed")

    def tick(self, moment: datetime | None = None) -> list[str]:
        """Run every job that is due. Returns the names that ran.

        Exposed directly so the scheduler is testable without a clock: a
        test ticks it by hand instead of sleeping.
        """
        moment = moment or datetime.now(timezone.utc)
        with self._lock:
            self._ticks += 1
            due = [name for name in self._definitions
                   if self._is_due(name, moment)]
        ran = []
        for name in self._resolve_order(due):
            self.run_job(name, reason="scheduled")
            ran.append(name)
        return ran

    def _is_due(self, name: str, moment: datetime) -> bool:
        definition = self._definitions[name]
        if not definition.enabled or self._state[name].status == "running":
            return False
        if definition.kind == "interval":
            return time.monotonic() >= self._due.get(name, 0)
        if definition.kind == "cron":
            next_run = self._state[name].next_run_at
            return bool(next_run) and moment >= datetime.fromisoformat(next_run)
        return False  # startup and event jobs are never tick-driven

    def _on_event(self, name: str, event: Event) -> None:
        definition = self._definitions.get(name)
        if definition is None or not definition.enabled:
            return
        self.run_job(name, reason=f"event:{event.kind}",
                     context={"event": event.describe()})

    # ------------------------------------------------------------ execution
    def run_job(self, name: str, reason: str = "manual",
                context: dict | None = None) -> dict:
        """Run one job now, honouring its retry policy. Never raises: a
        failed job is recorded, announced, and left for the next tick."""
        with self._lock:
            definition = self._definitions.get(name)
            if definition is None:
                raise KeyError(f"Unknown job: {name}")
            state = self._state[name]
            if state.status == "running":
                return {"job": name, "status": "already_running"}
            state.status = "running"
            state.last_run_at = now_iso()

        execution = {"execution_id": new_id("exec"), "job": name,
                     "reason": reason, "status": "running",
                     "started_at": state.last_run_at, "finished_at": "",
                     "attempts": 0, "error": "", "result": None,
                     "context": context or {}}
        self._bus.publish("JobStarted", {"job": name, "reason": reason},
                          source="scheduler")

        started = time.monotonic()
        result, error = None, ""
        for attempt in range(1, definition.retry.attempts + 1):
            execution["attempts"] = attempt
            try:
                result = definition.run()
                error = ""
                break
            except Exception as exc:  # noqa: BLE001 — retry, then degrade
                error = str(exc)[:300]
                logger.exception("Job %s failed (attempt %d/%d)", name, attempt,
                                 definition.retry.attempts)
                if attempt < definition.retry.attempts:
                    delay = definition.retry.delay_for(attempt)
                    if self._stop.wait(delay):  # shutdown beats a retry nap
                        break

        execution["finished_at"] = now_iso()
        execution["duration_ms"] = int((time.monotonic() - started) * 1000)
        execution["status"] = "failed" if error else "completed"
        execution["error"] = error
        execution["result"] = _summarize(result)

        with self._lock:
            state.status = execution["status"]
            state.last_finished_at = execution["finished_at"]
            state.last_error = error
            state.runs += 1
            if error:
                state.failures += 1
                state.consecutive_failures += 1
            else:
                state.consecutive_failures = 0
            self._reschedule(name, definition)
        self._record(execution)

        if error:
            self._bus.publish("JobFailed", {"job": name, "error": error,
                                            "attempts": execution["attempts"]},
                              source="scheduler")
        else:
            self._bus.publish("JobCompleted",
                              {"job": name, "result": execution["result"],
                               "duration_ms": execution["duration_ms"]},
                              source="scheduler")
        return execution

    def _reschedule(self, name: str, definition: JobDefinition) -> None:
        """Failure recovery: a failed job is retried on its normal cadence,
        backed off proportionally to how long it has been failing (capped),
        so a broken dependency never becomes a hot loop."""
        state = self._state[name]
        if definition.kind == "interval":
            interval = definition.interval_seconds or 0
            if state.consecutive_failures:
                interval *= min(2 ** state.consecutive_failures, 8)
            self._due[name] = time.monotonic() + interval
            state.next_run_at = ""
        elif definition.kind == "cron":
            self._schedule_next_cron(name, self._cron[name])

    def _schedule_next_cron(self, name: str, schedule: CronSchedule) -> None:
        next_run = schedule.next_after(datetime.now(timezone.utc))
        self._state[name].next_run_at = next_run.isoformat() if next_run else ""

    def _record(self, execution: dict) -> None:
        if self._store is None:
            return
        try:
            self._store.append("executions", execution, cap=MAX_EXECUTIONS)
        except Exception:  # noqa: BLE001 — history is observability, not truth
            logger.exception("Execution history persistence failed")

    # ----------------------------------------------------- dependency order
    def _startup_order(self) -> list[str]:
        with self._lock:
            names = [n for n, d in self._definitions.items()
                     if d.kind == "startup" and d.enabled]
        return self._resolve_order(names)

    def _resolve_order(self, names: list[str]) -> list[str]:
        """Topological order over ``depends_on``. Dependencies that are not
        in the batch are ignored (they run on their own cadence); a cycle
        degrades to registration order rather than deadlocking the runtime."""
        wanted = set(names)
        ordered: list[str] = []
        visiting: set[str] = set()
        placed: set[str] = set()

        def visit(name: str) -> None:
            if name in placed or name not in wanted:
                return
            if name in visiting:
                logger.error("Dependency cycle at job %s — running unordered",
                             name)
                return
            visiting.add(name)
            for dependency in self._definitions[name].depends_on:
                visit(dependency)
            visiting.discard(name)
            placed.add(name)
            ordered.append(name)

        for name in names:
            visit(name)
        return ordered

    # ----------------------------------------------------------- inspection
    def describe_job(self, name: str) -> dict:
        definition = self._definitions[name]
        state = self._state[name]
        return {"name": definition.name, "description": definition.description,
                "kind": definition.kind, "enabled": definition.enabled,
                "interval_seconds": definition.interval_seconds,
                "cron": definition.cron, "event": definition.event,
                "depends_on": definition.depends_on, "tags": definition.tags,
                "retry": {"attempts": definition.retry.attempts,
                          "backoff_seconds": definition.retry.backoff_seconds},
                "status": state.status, "runs": state.runs,
                "failures": state.failures,
                "consecutive_failures": state.consecutive_failures,
                "last_run_at": state.last_run_at,
                "last_finished_at": state.last_finished_at,
                "last_error": state.last_error,
                "next_run_at": state.next_run_at}

    def describe(self) -> list[dict]:
        with self._lock:
            return [self.describe_job(name) for name in self._definitions]

    def executions(self, limit: int = 50, job: str = "") -> list[dict]:
        items = self._store.read("executions") if self._store else []
        if job:
            items = [e for e in items if e["job"] == job]
        return list(reversed(items))[:limit]  # newest first

    def status(self) -> dict:
        with self._lock:
            jobs = list(self._state.values())
            return {
                "running": self.running,
                "started_at": self._started_at,
                "tick_seconds": self._tick_seconds,
                "ticks": self._ticks,
                "jobs_total": len(self._definitions),
                "jobs_enabled": sum(1 for d in self._definitions.values()
                                    if d.enabled),
                "jobs_by_kind": {kind: sum(1 for d in self._definitions.values()
                                           if d.kind == kind)
                                 for kind in JOB_KINDS},
                "runs": sum(j.runs for j in jobs),
                "failures": sum(j.failures for j in jobs),
                "degraded_jobs": [name for name, j in self._state.items()
                                  if j.consecutive_failures >= 3],
            }


def _summarize(result: Any) -> Any:
    """Job results land in the execution log and the API — keep them small
    and JSON-safe regardless of what a job returns."""
    if result is None or isinstance(result, (bool, int, float)):
        return result
    if isinstance(result, str):
        return result[:300]
    if isinstance(result, dict):
        return {k: _summarize(v) for k, v in list(result.items())[:20]}
    if isinstance(result, (list, tuple)):
        return [_summarize(v) for v in list(result)[:20]]
    return str(result)[:300]

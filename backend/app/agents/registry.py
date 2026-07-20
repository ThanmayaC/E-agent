"""Enterprise Agent Registry (Version 2.2).

Every autonomous capability the platform has registers here, with enough
metadata that the Runtime can discover and execute it **without importing
it** — which is the whole point: agent execution stops being hardcoded.

This registry is a **catalogue over implementations that already exist**, not
a new agent framework. The Executive Brief, RCA, SOP, Meeting, and Report
"agents" the SDS names are already implemented — as workflows in
``app/workflows/library.py``, as reasoning agents in ``app/agents``, as the
Product Intelligence layer's brief generators, and as Document Intelligence.
V2.2 gives them one uniform descriptor and one uniform way to be found and
run. Registering a capability twice would create a second implementation to
keep correct, which is exactly what this milestone forbids.

    BaseAgent            a reasoning agent (Observe → … → Learn)
    AgentDescriptor      what any capability IS: id, capabilities, I/O,
                         required tools, execution policy, approval policy
    AgentRegistry        register · discover by capability · execute · health

The Enterprise Brain remains the centre. An agent is an implementation
detail that either feeds the Brain, consumes it, validates it, or automates
work with it — the descriptor says which, in ``consumes`` and ``produces``.
"""
from __future__ import annotations

import threading
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Callable

from app.agents.base import AgentRequest, AgentResult, BaseAgent
from app.core.logging import get_logger

logger = get_logger(__name__)

# What an agent can do. Declared so the Runtime can ask "who can summarize a
# meeting?" instead of naming a class.
CAPABILITIES = (
    "summarize", "analyze", "generate_report", "generate_brief",
    "detect_risk", "recommend", "forecast", "extract_actions",
    "answer_question", "draft_communication", "process_document",
    "detect_change", "plan",
)

# How the Runtime is allowed to run it.
EXECUTION_POLICIES = (
    "automatic",        # the Runtime may run it unattended
    "scheduled_only",   # only from a scheduled job, never ad hoc
    "on_demand",        # only when a human or a workflow asks
    "disabled",         # registered, visible, not runnable
)

# What must happen before its output has an effect outside the platform.
APPROVAL_POLICIES = (
    "none",             # internal, reversible work
    "review",           # a human reviews the output before it is used
    "required",         # explicit approval before any external effect
)

# "catalogue" is distinct from "unavailable" on purpose: a capability that is
# declared but has no runner here is documentation, not a fault, and an
# observability dashboard that reports it as broken teaches operators to
# ignore the dashboard.
HEALTH_STATES = ("unknown", "healthy", "degraded", "unavailable", "disabled",
                 "catalogue")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class AgentDescriptor:
    """What one autonomous capability is, and how it may be run.

    ``runner`` is what makes the registry executable rather than decorative:
    a callable taking an ``AgentRequest`` and returning an ``AgentResult``.
    For a ``BaseAgent`` it is the agent's own ``run``; for a workflow-backed
    capability it is a thin adapter onto the Workflow Engine. Either way the
    Runtime calls one thing and does not know the difference.
    """
    agent_id: str
    name: str
    description: str = ""
    capabilities: tuple[str, ...] = ()
    inputs: tuple[str, ...] = ()          # what it accepts
    outputs: tuple[str, ...] = ()         # what it produces
    required_tools: tuple[str, ...] = ()
    execution_policy: str = "on_demand"
    approval_policy: str = "none"
    # Where this capability sits relative to the Brain — the architectural
    # question the SDS cares about.
    brain_role: str = "consumes"          # feeds | consumes | validates | automates
    implementation: str = ""              # module path, for the Admin console
    tags: tuple[str, ...] = ()
    runner: Callable[[AgentRequest], AgentResult] | None = None

    def __post_init__(self) -> None:
        if self.execution_policy not in EXECUTION_POLICIES:
            raise ValueError(
                f"Agent {self.agent_id}: unknown execution policy "
                f"{self.execution_policy!r}")
        if self.approval_policy not in APPROVAL_POLICIES:
            raise ValueError(
                f"Agent {self.agent_id}: unknown approval policy "
                f"{self.approval_policy!r}")
        unknown = set(self.capabilities) - set(CAPABILITIES)
        if unknown:
            raise ValueError(
                f"Agent {self.agent_id}: unknown capabilities "
                f"{', '.join(sorted(unknown))}")

    @property
    def executable(self) -> bool:
        return self.runner is not None and self.execution_policy != "disabled"

    def describe(self) -> dict:
        return {
            "id": self.agent_id, "name": self.name,
            "description": self.description,
            "capabilities": list(self.capabilities),
            "inputs": list(self.inputs), "outputs": list(self.outputs),
            "required_tools": list(self.required_tools),
            "execution_policy": self.execution_policy,
            "approval_policy": self.approval_policy,
            "brain_role": self.brain_role,
            "implementation": self.implementation,
            "tags": list(self.tags), "executable": self.executable,
        }


@dataclass
class AgentHealth:
    """Observed health — derived from real executions, not declared."""
    state: str = "unknown"
    detail: str = ""
    runs: int = 0
    failures: int = 0
    consecutive_failures: int = 0
    last_run_at: str = ""
    last_error: str = ""
    avg_duration_ms: int = 0

    def describe(self) -> dict:
        return {"state": self.state, "detail": self.detail, "runs": self.runs,
                "failures": self.failures,
                "consecutive_failures": self.consecutive_failures,
                "last_run_at": self.last_run_at, "last_error": self.last_error,
                "avg_duration_ms": self.avg_duration_ms,
                "success_rate": (round((self.runs - self.failures) / self.runs, 3)
                                 if self.runs else None)}


class AgentRegistry:
    """Every registered autonomous capability, discoverable by capability.

    Backward compatible with the V1 registry: ``register(agent)`` still takes
    a ``BaseAgent`` and ``get(name)`` still returns it, so every existing call
    site keeps working. What is new is that an agent can also carry a
    descriptor, and that the Runtime can find one by what it *does*.
    """

    def __init__(self, tools=None) -> None:
        self._agents: dict[str, BaseAgent] = {}
        self._descriptors: dict[str, AgentDescriptor] = {}
        self._health: dict[str, AgentHealth] = {}
        self._durations: dict[str, list[int]] = {}
        self._tools = tools          # optional ToolRegistry, for readiness
        self._lock = threading.RLock()

    # ------------------------------------------------------- registration
    def register(self, agent: BaseAgent,
                 descriptor: AgentDescriptor | None = None) -> AgentDescriptor:
        """Register a reasoning agent. Unchanged V1 signature.

        Without a descriptor one is derived from the agent itself, so V1 call
        sites gain a catalogue entry for free rather than losing one.
        """
        descriptor = descriptor or self._derive(agent)
        with self._lock:
            self._agents[agent.name] = agent
            self._descriptors[descriptor.agent_id] = descriptor
            self._health.setdefault(descriptor.agent_id, AgentHealth())
        return descriptor

    def register_capability(self, descriptor: AgentDescriptor) -> AgentDescriptor:
        """Register a capability that is not a ``BaseAgent`` — a workflow, a
        pipeline, a layer method. This is how the Executive Brief, RCA, SOP,
        Meeting, and Document agents enter the catalogue without any of them
        being reimplemented."""
        with self._lock:
            self._descriptors[descriptor.agent_id] = descriptor
            self._health.setdefault(descriptor.agent_id, AgentHealth())
        logger.debug("Registered capability %s", descriptor.agent_id)
        return descriptor

    @staticmethod
    def _derive(agent: BaseAgent) -> AgentDescriptor:
        return AgentDescriptor(
            agent_id=agent.name, name=agent.name.replace("_", " ").title(),
            description=getattr(agent, "role", ""),
            execution_policy="on_demand", approval_policy="none",
            implementation=f"{type(agent).__module__}.{type(agent).__name__}",
            runner=agent.run)

    # ----------------------------------------------------------- discovery
    def get(self, name: str) -> BaseAgent:
        """V1 contract: the agent instance, or KeyError."""
        with self._lock:
            if name not in self._agents:
                raise KeyError(f"Unknown agent: {name}")
            return self._agents[name]

    def descriptor(self, agent_id: str) -> AgentDescriptor:
        with self._lock:
            if agent_id not in self._descriptors:
                raise KeyError(f"Unknown agent: {agent_id}")
            return self._descriptors[agent_id]

    def has(self, agent_id: str) -> bool:
        with self._lock:
            return agent_id in self._descriptors

    def find(self, capability: str = "", brain_role: str = "",
             executable_only: bool = False) -> list[AgentDescriptor]:
        """Discover agents by what they do — the reason the Runtime does not
        need to import any of them."""
        with self._lock:
            found = list(self._descriptors.values())
        if capability:
            found = [d for d in found if capability in d.capabilities]
        if brain_role:
            found = [d for d in found if d.brain_role == brain_role]
        if executable_only:
            found = [d for d in found if d.executable]
        return found

    # ---------------------------------------------------------- execution
    def execute(self, agent_id: str, request: AgentRequest,
                reason: str = "manual") -> AgentResult:
        """Run one agent through the registry.

        Never raises for an agent-level failure: a failed agent is recorded,
        its health degrades, and the caller gets a failed ``AgentResult`` —
        the same contract ``BaseAgent.run`` already honours, extended to
        workflow-backed capabilities that never had it.
        """
        descriptor = self.descriptor(agent_id)
        if descriptor.runner is None:
            raise RuntimeError(
                f"Agent '{agent_id}' is a catalogue entry with no runner "
                f"({descriptor.implementation or 'not implemented'})")
        if descriptor.execution_policy == "disabled":
            return AgentResult(status="unavailable", agent=agent_id,
                               output="agent is disabled by policy")
        if reason == "automatic" and descriptor.execution_policy == "on_demand":
            return AgentResult(
                status="unavailable", agent=agent_id,
                output="execution policy 'on_demand' forbids automatic runs")

        missing = self._missing_tools(descriptor)
        if missing:
            self._record(agent_id, ok=False, duration_ms=0,
                         error=f"required tools unavailable: {', '.join(missing)}")
            return AgentResult(
                status="unavailable", agent=agent_id,
                output=f"required tools unavailable: {', '.join(missing)}")

        started = time.monotonic()
        try:
            result = descriptor.runner(request)
        except Exception as exc:  # noqa: BLE001 — a broken agent degrades itself
            logger.exception("Agent %s failed", agent_id)
            self._record(agent_id, ok=False,
                         duration_ms=int((time.monotonic() - started) * 1000),
                         error=f"{type(exc).__name__}: {exc}"[:300])
            return AgentResult(status="failed", agent=agent_id,
                               output=str(exc)[:500])

        duration = int((time.monotonic() - started) * 1000)
        ok = getattr(result, "status", "ok") not in ("failed", "unavailable")
        self._record(agent_id, ok=ok, duration_ms=duration,
                     error="" if ok else str(getattr(result, "output", ""))[:300])
        return result

    def _missing_tools(self, descriptor: AgentDescriptor) -> list[str]:
        """Required tools that are not registered or not available here."""
        if self._tools is None or not descriptor.required_tools:
            return []
        missing = []
        for name in descriptor.required_tools:
            try:
                self._tools.get(name)
            except Exception:  # noqa: BLE001 — unknown or unavailable, same outcome
                missing.append(name)
        return missing

    # -------------------------------------------------------------- health
    def _record(self, agent_id: str, ok: bool, duration_ms: int,
                error: str = "") -> None:
        with self._lock:
            health = self._health.setdefault(agent_id, AgentHealth())
            health.runs += 1
            health.last_run_at = now_iso()
            if ok:
                health.consecutive_failures = 0
                health.last_error = ""
            else:
                health.failures += 1
                health.consecutive_failures += 1
                health.last_error = error
            durations = self._durations.setdefault(agent_id, [])
            durations.append(duration_ms)
            del durations[:-50]                       # a rolling window
            health.avg_duration_ms = int(sum(durations) / len(durations))
            health.state, health.detail = self._assess(agent_id, health)

    def _assess(self, agent_id: str, health: AgentHealth) -> tuple[str, str]:
        descriptor = self._descriptors.get(agent_id)
        if descriptor is not None and descriptor.execution_policy == "disabled":
            return "disabled", "disabled by policy"
        if descriptor is not None and descriptor.runner is None:
            return ("catalogue",
                    "declared capability — invoked as part of a larger "
                    "pipeline rather than executed on its own here")
        if health.consecutive_failures >= 3:
            return "unavailable", f"{health.consecutive_failures} consecutive failures"
        if health.consecutive_failures:
            return "degraded", health.last_error[:160]
        if health.runs:
            return "healthy", ""
        return "unknown", "never executed"

    def health(self, agent_id: str) -> AgentHealth:
        with self._lock:
            health = self._health.setdefault(agent_id, AgentHealth())
            if health.state == "unknown":
                health.state, health.detail = self._assess(agent_id, health)
            return health

    # --------------------------------------------------------- inspection
    def describe(self) -> list[dict]:
        """V1 contract returned a list of dicts; it still does — with more in
        each dict, and health alongside."""
        with self._lock:
            ids = list(self._descriptors)
        return [{**self._descriptors[i].describe(),
                 "health": self.health(i).describe()} for i in ids]

    def status(self) -> dict:
        """Agent Health for the Observability dashboard."""
        descriptors = self.describe()
        by_state: dict[str, int] = {}
        for d in descriptors:
            state = d["health"]["state"]
            by_state[state] = by_state.get(state, 0) + 1
        runs = sum(d["health"]["runs"] for d in descriptors)
        failures = sum(d["health"]["failures"] for d in descriptors)
        return {
            "total": len(descriptors),
            "executable": sum(1 for d in descriptors if d["executable"]),
            "by_state": by_state,
            "by_capability": {c: len(self.find(capability=c))
                              for c in CAPABILITIES
                              if self.find(capability=c)},
            "by_brain_role": {role: len(self.find(brain_role=role))
                              for role in ("feeds", "consumes", "validates",
                                           "automates")},
            "runs": runs, "failures": failures,
            "success_rate": round((runs - failures) / runs, 3) if runs else None,
            # Only genuine faults. A "catalogue" agent is declared-but-not-
            # runnable here, which is a design fact, not an incident.
            "degraded": [d["id"] for d in descriptors
                         if d["health"]["state"] in ("degraded", "unavailable")],
            "catalogue_only": [d["id"] for d in descriptors
                               if d["health"]["state"] == "catalogue"],
        }

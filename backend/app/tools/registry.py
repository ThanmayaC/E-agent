"""Enterprise Tool Registry (Version 2.2).

Agents request capabilities; they do not import implementations. A tool is
declared once — with its capability, its permission, its input and output
schema, which agent types may use it, and its live execution status — and
every agent reaches it by name through this registry.

This extends the V1 ``ToolRegistry`` rather than replacing it: ``register``,
``get``, ``run``, and ``describe`` keep their signatures, so every existing
call site is untouched. What is new is the ``ToolSpec`` beside each tool, the
permission check before each run, and the recorded outcome after it.

Why schemas matter here and nowhere else: the moment a language model is
allowed to choose a tool, "what arguments does this take" stops being
documentation and becomes a contract. Declaring it in the registry means one
answer, checked before execution, instead of a stack trace inside a tool.
"""
from __future__ import annotations

import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from app.core.logging import get_logger
from app.tools.base import Tool, ToolNotAvailable

logger = get_logger(__name__)

# What kind of work a tool does. The Governance layer grants permissions per
# capability, not per tool, so a new tool inherits a policy instead of needing
# one written for it.
CAPABILITIES = (
    "search",           # knowledge/enterprise search
    "read",             # read a source (Excel, PDF, database)
    "generate",         # produce an artifact (report, deck, dashboard)
    "draft",            # produce a communication for approval
    "summarize",        # condense existing content
    "refresh",          # trigger a knowledge/sync refresh
    "query",            # structured query over analytics
)

# What a tool is allowed to touch. This is the vocabulary Governance checks.
PERMISSIONS = (
    "read_knowledge",       # read organizational knowledge
    "read_project",         # read one project's artifacts
    "read_source",          # read a connected enterprise source
    "write_artifact",       # produce a stored artifact
    "draft_external",       # draft something that could leave the platform
    "trigger_sync",         # cause synchronization work to run
)

STATUSES = ("ready", "unavailable", "degraded", "forbidden")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class ToolSpec:
    """What a tool is, who may use it, and what it takes and returns.

    Schemas are intentionally lightweight — a dict of ``field -> type name``
    plus a required list. A full JSON-Schema implementation would be a second
    validation framework; this is enough to reject a malformed call before it
    reaches an implementation, which is the actual goal.
    """
    tool_id: str
    capability: str
    description: str = ""
    permissions: tuple[str, ...] = ()
    supported_agents: tuple[str, ...] = ()      # empty = every agent
    inputs: dict[str, str] = field(default_factory=dict)
    required: tuple[str, ...] = ()
    outputs: dict[str, str] = field(default_factory=dict)
    tags: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.capability not in CAPABILITIES:
            raise ValueError(
                f"Tool {self.tool_id}: unknown capability {self.capability!r}")
        unknown = set(self.permissions) - set(PERMISSIONS)
        if unknown:
            raise ValueError(
                f"Tool {self.tool_id}: unknown permissions "
                f"{', '.join(sorted(unknown))}")
        missing = set(self.required) - set(self.inputs)
        if missing:
            raise ValueError(
                f"Tool {self.tool_id}: required inputs not declared in the "
                f"input schema: {', '.join(sorted(missing))}")

    def allows(self, agent_id: str) -> bool:
        return not self.supported_agents or agent_id in self.supported_agents

    def validate(self, kwargs: dict[str, Any]) -> list[str]:
        """Problems with a proposed call. Empty means it may run."""
        problems = [f"missing required input '{name}'"
                    for name in self.required if kwargs.get(name) is None]
        for name in kwargs:
            if self.inputs and name not in self.inputs:
                problems.append(f"unknown input '{name}'")
        return problems

    def describe(self) -> dict:
        return {"id": self.tool_id, "capability": self.capability,
                "description": self.description,
                "permissions": list(self.permissions),
                "supported_agents": list(self.supported_agents),
                "inputs": self.inputs, "required": list(self.required),
                "outputs": self.outputs, "tags": list(self.tags)}


@dataclass
class ToolStatus:
    """Live execution status, observed rather than declared."""
    status: str = "ready"
    detail: str = ""
    calls: int = 0
    failures: int = 0
    last_called_at: str = ""
    last_error: str = ""
    avg_duration_ms: int = 0

    def describe(self) -> dict:
        return {"status": self.status, "detail": self.detail,
                "calls": self.calls, "failures": self.failures,
                "last_called_at": self.last_called_at,
                "last_error": self.last_error,
                "avg_duration_ms": self.avg_duration_ms}


class ToolPermissionDenied(RuntimeError):
    """Governance refused this tool call."""


class ToolInputInvalid(ValueError):
    """The call does not satisfy the tool's declared input schema."""


class ToolRegistry:
    """Every tool the platform exposes, with its spec, policy, and status.

    Backward compatible with V1: ``register(tool)``, ``get(name)``,
    ``run(name, **kwargs)`` and ``describe()`` behave as before.
    """

    def __init__(self, governance=None) -> None:
        self._tools: dict[str, Tool] = {}
        self._specs: dict[str, ToolSpec] = {}
        self._status: dict[str, ToolStatus] = {}
        self._durations: dict[str, list[int]] = {}
        # Optional GovernanceLayer. Absent (lite profile, tests) every call is
        # permitted — governance is a gate the deployment installs, not a
        # dependency the tool layer requires to function.
        self._governance = governance
        self._lock = threading.RLock()

    def attach_governance(self, governance) -> None:
        """Wire the Governance layer after construction — the container
        builds tools before policies exist."""
        self._governance = governance

    # ------------------------------------------------------- registration
    def register(self, tool: Tool, spec: ToolSpec | None = None) -> ToolSpec:
        """Register a tool. V1 signature; the spec is derived when absent so
        existing registrations gain a catalogue entry rather than losing one."""
        spec = spec or self._derive(tool)
        with self._lock:
            self._tools[tool.name] = tool
            self._specs[spec.tool_id] = spec
            self._status.setdefault(spec.tool_id, ToolStatus(
                status="ready" if tool.available else "unavailable",
                detail=tool.unavailable_reason))
        return spec

    @staticmethod
    def _derive(tool: Tool) -> ToolSpec:
        """A conservative spec for a tool registered without one: read-only,
        no declared schema, available to every agent. Guessing a *narrower*
        permission would silently break a working V1 tool."""
        return ToolSpec(tool_id=tool.name, capability="read",
                        description=tool.description,
                        permissions=("read_project",))

    # ----------------------------------------------------------- discovery
    def get(self, name: str) -> Tool:
        """V1 contract: the tool, or KeyError / ToolNotAvailable."""
        with self._lock:
            if name not in self._tools:
                raise KeyError(f"Unknown tool: {name}")
            tool = self._tools[name]
        if not tool.available:
            raise ToolNotAvailable(
                f"Tool '{name}' unavailable: {tool.unavailable_reason}")
        return tool

    def spec(self, tool_id: str) -> ToolSpec:
        with self._lock:
            if tool_id not in self._specs:
                raise KeyError(f"Unknown tool: {tool_id}")
            return self._specs[tool_id]

    def has(self, tool_id: str) -> bool:
        with self._lock:
            return tool_id in self._specs

    def find(self, capability: str = "", agent_id: str = "",
             permission: str = "") -> list[ToolSpec]:
        """Which tools can do this — how an agent asks for a capability
        instead of importing an implementation."""
        with self._lock:
            found = list(self._specs.values())
        if capability:
            found = [s for s in found if s.capability == capability]
        if agent_id:
            found = [s for s in found if s.allows(agent_id)]
        if permission:
            found = [s for s in found if permission in s.permissions]
        return found

    # ----------------------------------------------------------- execution
    def run(self, name: str, **kwargs: Any) -> Any:
        """V1 contract, now with schema validation and status recording."""
        return self.run_as("", name, **kwargs)

    def run_as(self, agent_id: str, name: str, **kwargs: Any) -> Any:
        """Run a tool on behalf of an agent, through every gate:

            registered → available → agent permitted → governance permits
            → inputs valid → execute → record

        A refusal raises rather than returning a falsy value, because a tool
        call that silently did nothing is the hardest kind of bug to see in a
        generated report.
        """
        tool = self.get(name)               # KeyError / ToolNotAvailable
        spec = self.spec(name)

        if agent_id and not spec.allows(agent_id):
            raise ToolPermissionDenied(
                f"Agent '{agent_id}' may not use tool '{name}' "
                f"(permitted: {', '.join(spec.supported_agents)})")

        if self._governance is not None:
            verdict = self._governance.check_tool(agent_id or "system", spec)
            if not verdict.allowed:
                self._set_status(name, "forbidden", verdict.reason)
                raise ToolPermissionDenied(
                    f"Tool '{name}' denied by policy: {verdict.reason}")

        problems = spec.validate(kwargs)
        if problems:
            raise ToolInputInvalid(
                f"Tool '{name}' called incorrectly: {'; '.join(problems)}")

        started = time.monotonic()
        try:
            result = tool.run(**kwargs)
        except Exception as exc:  # noqa: BLE001 — record, then re-raise
            self._record(name, ok=False,
                         duration_ms=int((time.monotonic() - started) * 1000),
                         error=f"{type(exc).__name__}: {exc}"[:300])
            raise
        self._record(name, ok=True,
                     duration_ms=int((time.monotonic() - started) * 1000))
        return result

    # -------------------------------------------------------------- status
    def _record(self, tool_id: str, ok: bool, duration_ms: int,
                error: str = "") -> None:
        with self._lock:
            status = self._status.setdefault(tool_id, ToolStatus())
            status.calls += 1
            status.last_called_at = now_iso()
            if ok:
                status.last_error = ""
                if status.status == "degraded":
                    status.status, status.detail = "ready", ""
            else:
                status.failures += 1
                status.last_error = error
                status.status, status.detail = "degraded", error[:160]
            durations = self._durations.setdefault(tool_id, [])
            durations.append(duration_ms)
            del durations[:-50]
            status.avg_duration_ms = int(sum(durations) / len(durations))

    def _set_status(self, tool_id: str, status: str, detail: str = "") -> None:
        with self._lock:
            current = self._status.setdefault(tool_id, ToolStatus())
            current.status, current.detail = status, detail

    def status_of(self, tool_id: str) -> ToolStatus:
        with self._lock:
            status = self._status.setdefault(tool_id, ToolStatus())
            tool = self._tools.get(tool_id)
            if tool is not None and not tool.available and status.status == "ready":
                status.status, status.detail = ("unavailable",
                                                tool.unavailable_reason)
            return status

    # --------------------------------------------------------- inspection
    def describe(self) -> list[dict]:
        """V1 contract: a list of dicts — now carrying spec and status."""
        with self._lock:
            ids = list(self._specs)
        out = []
        for tool_id in ids:
            tool = self._tools.get(tool_id)
            out.append({
                **self._specs[tool_id].describe(),
                "name": tool_id,
                "available": bool(tool and tool.available),
                "unavailable_reason": (tool.unavailable_reason if tool else
                                       "not registered"),
                "execution_status": self.status_of(tool_id).describe(),
            })
        return out

    def status(self) -> dict:
        """Tool Health for the Observability dashboard."""
        tools = self.describe()
        by_status: dict[str, int] = {}
        for t in tools:
            state = t["execution_status"]["status"]
            by_status[state] = by_status.get(state, 0) + 1
        calls = sum(t["execution_status"]["calls"] for t in tools)
        failures = sum(t["execution_status"]["failures"] for t in tools)
        return {
            "total": len(tools),
            "available": sum(1 for t in tools if t["available"]),
            "by_status": by_status,
            "by_capability": {c: len(self.find(capability=c))
                              for c in CAPABILITIES if self.find(capability=c)},
            "calls": calls, "failures": failures,
            "success_rate": (round((calls - failures) / calls, 3)
                             if calls else None),
            "degraded": [t["id"] for t in tools
                         if t["execution_status"]["status"] in ("degraded",
                                                                "forbidden")],
        }

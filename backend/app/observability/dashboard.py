"""Enterprise Observability (Version 2.2) — one operational view of the platform.

Every layer already reports its own status: the scheduler knows its jobs, the
connector framework knows its sources, the agent registry knows its health,
the evaluation pipeline knows its verdicts. What nobody could do was see all
of it at once and answer "is the platform healthy right now?".

This module composes those existing status surfaces. It computes almost
nothing of its own — asking each owner is what keeps one number from having
two answers. What it adds is composition, an overall verdict, and latency
measurement, which genuinely had no owner before.

**Admin-only, and business-surface-neutral.** Nothing here touches the
Executive Workspace: an executive sees reports and approvals, never agent
health. Every section degrades independently — a layer that is disabled or
throwing reports itself as unavailable instead of failing the dashboard,
because an observability page that goes down with the thing it observes is
worse than useless.
"""
from __future__ import annotations

import threading
import time
from collections import deque
from datetime import datetime, timezone
from typing import Any, Callable

from app.core.logging import get_logger

logger = get_logger(__name__)

# Overall verdicts, ordered by severity.
VERDICTS = ("healthy", "degraded", "unhealthy", "unknown")
MAX_LATENCY_SAMPLES = 200


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


class LatencyTracker:
    """Processing latency by operation — the one metric with no other owner.

    Sampled rather than aggregated forever: a rolling window answers "is it
    slow now", which is the operational question. Long-term trends belong in
    whatever metrics system the enterprise already runs.
    """

    def __init__(self, window: int = MAX_LATENCY_SAMPLES):
        self._samples: dict[str, deque[float]] = {}
        self._window = window
        self._lock = threading.RLock()

    def record(self, operation: str, duration_ms: float) -> None:
        with self._lock:
            samples = self._samples.setdefault(operation,
                                               deque(maxlen=self._window))
            samples.append(float(duration_ms))

    def measure(self, operation: str):
        """Context manager: ``with latency.measure("analysis"): ...``"""
        tracker = self

        class _Measure:
            def __enter__(self):
                self.started = time.monotonic()
                return self

            def __exit__(self, *exc):
                tracker.record(operation,
                               (time.monotonic() - self.started) * 1000)
                return False

        return _Measure()

    def summary(self) -> dict[str, Any]:
        with self._lock:
            snapshot = {name: list(values)
                        for name, values in self._samples.items()}
        out: dict[str, Any] = {}
        for name, values in snapshot.items():
            if not values:
                continue
            ordered = sorted(values)
            out[name] = {
                "samples": len(ordered),
                "avg_ms": int(sum(ordered) / len(ordered)),
                "p50_ms": int(ordered[len(ordered) // 2]),
                "p95_ms": int(ordered[min(int(len(ordered) * 0.95),
                                          len(ordered) - 1)]),
                "max_ms": int(ordered[-1]),
            }
        return out


class ObservabilityDashboard:
    """Composes every layer's own status into one operational picture."""

    def __init__(self, *, agents=None, tools=None, prompts=None,
                 evaluation=None, governance=None, connectors=None,
                 runtime=None, lifecycle=None, workflows=None, brain=None,
                 latency: LatencyTracker | None = None):
        self._sources: dict[str, Any] = {
            "agents": agents, "tools": tools, "prompts": prompts,
            "evaluation": evaluation, "governance": governance,
            "connectors": connectors, "runtime": runtime,
            "knowledge": lifecycle, "workflows": workflows, "brain": brain,
        }
        self.latency = latency or LatencyTracker()

    # ---------------------------------------------------------- sections
    def _section(self, name: str, reader: Callable[[Any], dict]) -> dict:
        """One section, or an honest explanation of why it is missing."""
        component = self._sources.get(name)
        if component is None:
            return {"available": False,
                    "reason": f"{name} is not enabled in this deployment"}
        try:
            return {"available": True, **reader(component)}
        except Exception as exc:  # noqa: BLE001 — one section, not the page
            logger.exception("Observability section %s failed", name)
            return {"available": False,
                    "reason": f"{type(exc).__name__}: {exc}"[:200]}

    def agent_health(self) -> dict:
        return self._section("agents", lambda c: c.status())

    def tool_health(self) -> dict:
        return self._section("tools", lambda c: c.status())

    def connector_health(self) -> dict:
        return self._section("connectors", lambda c: c.status()["sources"])

    def knowledge_growth(self) -> dict:
        return self._section("knowledge", lambda c: c.status())

    def runtime_statistics(self) -> dict:
        return self._section("runtime", lambda c: {
            "running": c.running,
            "scheduler": c.scheduler.status(),
            "events": c.bus.stats(),
            "queue": c.queue.stats(),
        })

    def evaluation_metrics(self) -> dict:
        return self._section("evaluation", lambda c: c.status())

    def workflow_success(self) -> dict:
        return self._section("workflows", lambda c: c.status())

    def approval_queue(self) -> dict:
        return self._section("runtime", lambda c: c.queue.stats())

    def llm_usage(self) -> dict:
        return self._section("governance",
                             lambda c: c.model_usage_summary())

    def prompt_registry(self) -> dict:
        return self._section("prompts", lambda c: c.status())

    def governance_status(self) -> dict:
        return self._section("governance", lambda c: {
            "enabled": c.enabled, "roles": len(c.roles()),
            "principals": len(c.principals()),
            "audit_entries": c.status()["audit_entries"],
            "security_policy": c.security_policy().describe(),
        })

    def processing_latency(self) -> dict:
        return {"available": True, "operations": self.latency.summary()}

    # --------------------------------------------------------- composition
    def snapshot(self) -> dict[str, Any]:
        """The whole dashboard, in one call."""
        sections = {
            "agent_health": self.agent_health(),
            "tool_health": self.tool_health(),
            "connector_health": self.connector_health(),
            "knowledge_growth": self.knowledge_growth(),
            "runtime_statistics": self.runtime_statistics(),
            "evaluation_metrics": self.evaluation_metrics(),
            "workflow_success": self.workflow_success(),
            "approval_queue": self.approval_queue(),
            "llm_usage": self.llm_usage(),
            "prompt_registry": self.prompt_registry(),
            "governance": self.governance_status(),
            "processing_latency": self.processing_latency(),
        }
        return {"generated_at": now_iso(),
                "verdict": self._verdict(sections),
                "sections": sections}

    def _verdict(self, sections: dict[str, dict]) -> dict:
        """One overall answer, with the reasons that produced it.

        A verdict without reasons is a traffic light nobody trusts, so every
        concern that moved the needle is named.
        """
        concerns: list[str] = []
        unavailable: list[str] = []

        for name, section in sections.items():
            if not section.get("available"):
                unavailable.append(name)
                continue
            concerns.extend(self._concerns(name, section))

        if any(c.startswith("critical:") for c in concerns):
            verdict = "unhealthy"
        elif concerns:
            verdict = "degraded"
        elif len(unavailable) == len(sections):
            verdict = "unknown"
        else:
            verdict = "healthy"

        return {"state": verdict, "concerns": concerns,
                "unavailable_sections": unavailable}

    @staticmethod
    def _concerns(name: str, section: dict) -> list[str]:
        """What is wrong in one section, in operator language."""
        out: list[str] = []
        degraded = section.get("degraded") or []
        if degraded:
            out.append(f"{name}: {len(degraded)} degraded "
                       f"({', '.join(map(str, degraded[:3]))})")
        if name == "connector_health":
            needs = section.get("needs_attention") or 0
            if needs:
                out.append(f"connectors: {needs} source(s) need attention")
        if name == "knowledge_growth":
            stale = section.get("needs_refresh") or []
            if stale:
                out.append(f"knowledge: {', '.join(stale)} stale")
        if name == "runtime_statistics":
            scheduler = section.get("scheduler") or {}
            if scheduler.get("degraded_jobs"):
                out.append("critical: scheduler has degraded jobs "
                           f"({', '.join(scheduler['degraded_jobs'][:3])})")
            if section.get("running") is False:
                out.append("critical: the autonomy runtime is not running")
        if name == "evaluation_metrics":
            rate = section.get("acceptance_rate")
            if rate is not None and rate < 0.5 and section.get("evaluated", 0) >= 5:
                out.append(f"evaluation: only {int(rate * 100)}% of generated "
                           f"output is accepted")
        if name == "workflow_success":
            rate = section.get("success_rate")
            if rate is not None and rate < 0.8:
                out.append(f"workflows: {int(rate * 100)}% success rate")
        return out

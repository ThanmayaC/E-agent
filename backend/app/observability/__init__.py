"""Enterprise Observability (Version 2.2).

One Admin-only operational view composed from the status surfaces every layer
already exposes: agent health, tool health, connector health, knowledge
growth, runtime statistics, evaluation metrics, workflow success, approval
queue, LLM usage, and processing latency.

It composes rather than computes — asking each owner is what stops one number
from having two answers. Business dashboards are untouched.
"""
from app.observability.dashboard import (
    VERDICTS, LatencyTracker, ObservabilityDashboard,
)

__all__ = ["LatencyTracker", "ObservabilityDashboard", "VERDICTS"]

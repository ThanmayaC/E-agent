"""Automation Module (SDS §2.8) — status: implemented.

Triggering workflows, continuous monitoring, scheduled execution. The
Enterprise Scheduler is the beat process this module always needed: startup,
interval, cron, and event jobs with dependency ordering, retry policies, and
failure recovery. The Trigger Engine adds configurable rule-based automation
over the Event Bus, and the Action Queue is where every automated effect is
recorded and (when it reaches outside the platform) approved.

This module consumes the Workflow Module's engine — it never reimplements
it: ``WorkflowEngine.schedule()`` still declares recurring work, and the
scheduler is what now executes it.
"""
from app.runtime.background import BackgroundIntelligence
from app.runtime.queue import ActionQueue
from app.runtime.runtime import AutonomyRuntime
from app.runtime.scheduler import (
    EnterpriseScheduler, JobDefinition, RetryPolicy,
)
from app.runtime.triggers import TriggerEngine
from app.workflows.engine import PLANNED_WORKFLOWS, WorkflowEngine

__all__ = ["ActionQueue", "AutonomyRuntime", "BackgroundIntelligence",
           "EnterpriseScheduler", "JobDefinition", "PLANNED_WORKFLOWS",
           "RetryPolicy", "TriggerEngine", "WorkflowEngine"]

STATUS = "implemented"

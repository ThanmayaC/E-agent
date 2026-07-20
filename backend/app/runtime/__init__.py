"""Autonomous execution layer — the runtime that makes Enterprise Agent act.

The platform observes, learns, plans, executes, monitors, and improves on
its own heartbeat; the manager reviews, approves, communicates, and decides
strategy. This package is that heartbeat:

    events      Event Bus — modules announce, they never call each other
    scheduler   Enterprise Scheduler — startup/interval/cron/event jobs
    triggers    Trigger Engine — configurable rules over the bus
    goals       Agent Goal Engine — objectives, KPIs, targets, deadlines
    planning    Planning Engine — goals into executable plans, replanned
    decisions   Decision Engine — recommendation → … → execute → learn
    queue       Action Queue — the execution centre and approval layer
    background  Background Intelligence — continuous refresh jobs
    runtime     AutonomyRuntime — the composition root that wires it up
"""
from app.runtime.background import BackgroundIntelligence
from app.runtime.decisions import DecisionEngine
from app.runtime.events import EVENT_KINDS, Event, EventBus
from app.runtime.goals import GoalEngine
from app.runtime.planning import PlanningEngine
from app.runtime.queue import ACTION_KINDS, ActionQueue
from app.runtime.runtime import AutonomyRuntime
from app.runtime.scheduler import (
    EnterpriseScheduler, JobDefinition, RetryPolicy,
)
from app.runtime.store import RuntimeStore
from app.runtime.triggers import TriggerEngine

__all__ = [
    "ACTION_KINDS", "ActionQueue", "AutonomyRuntime",
    "BackgroundIntelligence", "DecisionEngine", "EVENT_KINDS",
    "EnterpriseScheduler", "Event", "EventBus", "GoalEngine",
    "JobDefinition", "PlanningEngine", "RetryPolicy", "RuntimeStore",
    "TriggerEngine",
]

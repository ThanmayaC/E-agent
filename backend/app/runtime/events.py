"""Enterprise Event Bus.

Modules announce what happened; they do not call each other to make things
happen. A producer publishes ``DatasetImported``; the Trigger Engine, the
scheduler's event jobs, and (in V2) the communication modules subscribe.
Adding a consumer never touches the producer.

Delivery is synchronous and best-effort: a failing subscriber is logged and
recorded on the event, never propagated to the publisher — an autonomous
platform must not let a notification bug fail an analysis. Publication is
re-entrant (a subscriber may publish), and every event is persisted to a
bounded history that powers ``/runtime/events``.
"""
from __future__ import annotations

import threading
from collections import deque
from dataclasses import dataclass, field
from typing import Any, Callable

from app.core.logging import get_logger
from app.runtime.store import RuntimeStore, new_id, now_iso

logger = get_logger(__name__)

# The SDS event vocabulary. Publishing an unknown name is rejected: the bus
# is a contract between modules, not a free-text channel.
EVENT_KINDS = (
    "DatasetImported",
    "KnowledgeUpdated",
    "ReportGenerated",
    "PortfolioChanged",
    "RecommendationCreated",
    "DecisionRecorded",
    "WorkflowCompleted",
    "WorkflowFailed",
    "TaskCompleted",
    "NotificationCreated",
    "GoalCreated",
    "GoalProgressed",
    "GoalAchieved",
    "ActionQueued",
    "ActionApproved",
    "ActionRejected",
    "ActionExecuted",
    "ActionFailed",
    "ActionEdited",       # V2: a queued draft was edited before approval
    "DocumentsUpdated",   # V2: Document Intelligence ingested changes
    "AnomalyDetected",
    "PredictionConfidenceDropped",
    "RiskIncreased",
    "ReportApproved",
    # Enterprise Knowledge Synchronization Layer
    "SourceRegistered",
    "SourceSynchronized",
    "SourceSyncFailed",
    "EntityDiscovered",
    "EntityUpdated",
    "RelationshipDiscovered",
    # V2.1: Enterprise Connector Framework
    "ConnectorRegistered",
    "ConnectorSyncStarted",
    "ConnectorSyncCompleted",
    "ConnectorSyncFailed",
    "ConnectorHealthChanged",
    "KnowledgePackagesProduced",
    # Product Intelligence & Strategic Decision Layer
    "ProductRegistered",
    "ProductUpdated",
    "ProductHealthEvaluated",
    "ProductReviewGenerated",
    "GrowthRiskDetected",
    "KPIThresholdCrossed",
    "ScenarioSimulated",
    # Enterprise Copilot Layer
    "CopilotAnswered",
    "JobStarted",
    "JobCompleted",
    "JobFailed",
    "RuntimeStarted",
)

WILDCARD = "*"
MAX_EVENT_HISTORY = 500


@dataclass
class Event:
    kind: str
    payload: dict[str, Any] = field(default_factory=dict)
    project_id: str = ""
    source: str = ""
    event_id: str = field(default_factory=lambda: new_id("evt"))
    created_at: str = field(default_factory=now_iso)

    def describe(self) -> dict:
        return {"event_id": self.event_id, "kind": self.kind,
                "project_id": self.project_id, "source": self.source,
                "payload": self.payload, "created_at": self.created_at}


class EventBus:
    def __init__(self, store: RuntimeStore | None = None):
        self._subscribers: dict[str, list[tuple[str, Callable[[Event], Any]]]] = {}
        self._history: deque[dict] = deque(maxlen=MAX_EVENT_HISTORY)
        self._store = store
        self._lock = threading.RLock()
        self._published = 0
        self._failures = 0
        if store is not None:
            for item in store.read("events")[-MAX_EVENT_HISTORY:]:
                self._history.append(item)

    # ---------------------------------------------------------- subscription
    def subscribe(self, kind: str, handler: Callable[[Event], Any],
                  name: str = "") -> None:
        """Register a handler for one event kind, or for ``*`` (every event).

        Handlers run in publication order, synchronously, on the publishing
        thread.
        """
        if kind != WILDCARD and kind not in EVENT_KINDS:
            raise ValueError(f"Unknown event kind: {kind}")
        with self._lock:
            self._subscribers.setdefault(kind, []).append(
                (name or getattr(handler, "__name__", "handler"), handler))

    def subscribers(self) -> list[dict]:
        with self._lock:
            return [{"event": kind, "handler": name}
                    for kind, handlers in sorted(self._subscribers.items())
                    for name, _ in handlers]

    # ----------------------------------------------------------- publication
    def publish(self, kind: str, payload: dict | None = None,
                project_id: str = "", source: str = "") -> Event:
        if kind not in EVENT_KINDS:
            raise ValueError(f"Unknown event kind: {kind}")
        event = Event(kind=kind, payload=payload or {}, project_id=project_id,
                      source=source)
        return self.publish_event(event)

    def publish_event(self, event: Event) -> Event:
        with self._lock:
            handlers = list(self._subscribers.get(event.kind, [])) + \
                list(self._subscribers.get(WILDCARD, []))
            self._published += 1

        delivered, errors = 0, []
        for name, handler in handlers:
            try:
                handler(event)
                delivered += 1
            except Exception as exc:  # noqa: BLE001 — a subscriber never breaks a publisher
                logger.exception("Event subscriber %s failed on %s", name,
                                 event.kind)
                errors.append(f"{name}: {str(exc)[:120]}")
                with self._lock:
                    self._failures += 1

        record = {**event.describe(), "delivered": delivered,
                  "subscribers": len(handlers), "errors": errors}
        with self._lock:
            self._history.append(record)
            if self._store is not None:
                try:
                    self._store.append("events", record, cap=MAX_EVENT_HISTORY)
                except Exception:  # noqa: BLE001 — history is observability, not truth
                    logger.exception("Event history persistence failed")
        return event

    # ------------------------------------------------------------ inspection
    def history(self, limit: int = 50, kind: str = "",
                project_id: str = "") -> list[dict]:
        items = list(self._history)
        if kind:
            items = [e for e in items if e["kind"] == kind]
        if project_id:
            items = [e for e in items if e.get("project_id") == project_id]
        return list(reversed(items))[:limit]  # newest first

    def stats(self) -> dict:
        with self._lock:
            by_kind: dict[str, int] = {}
            for e in self._history:
                by_kind[e["kind"]] = by_kind.get(e["kind"], 0) + 1
            return {"published": self._published,
                    "subscriber_failures": self._failures,
                    "subscriptions": sum(len(h) for h in
                                         self._subscribers.values()),
                    "history": len(self._history), "by_kind": by_kind}

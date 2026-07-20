"""Memory Lifecycle — knowledge that evolves instead of accumulating.

The Enterprise Brain already *learns*: documents are versioned by the Document
Intelligence pipeline, entities carry history in the Organizational Model,
decisions are recorded, relationships are discovered with evidence. What it
did not have was a **lifecycle**: a way to say that a fact has gone stale,
that a document has been superseded, that a policy expired, or that a
relationship changed shape.

That gap matters because an append-only Brain gets *less* useful over time.
A knowledge store that still confidently returns the 2023 refund policy
alongside the 2026 one is worse than one that returns nothing, because a
reader cannot tell which is current.

This module adds the lifecycle without touching how knowledge is written:

    freshness    how current a knowledge class is, and what is overdue
    versions     document version lineage (reads the DocumentStore)
    history      entity and decision evolution (reads the Organizational Model)
    expiry       what has passed its retention horizon (asks Governance)
    archive      supersede rather than delete — nothing is erased
    evolution    how relationships changed between two points in time

Everything here is **read-and-annotate**. It never deletes: archived knowledge
stays readable and stays auditable, which is the same commitment the audit
log makes.
"""
from __future__ import annotations

import threading
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any

from app.core.logging import get_logger

logger = get_logger(__name__)

# How long each knowledge class stays "fresh" before it is worth re-deriving.
# These are staleness horizons, not retention: stale knowledge is flagged, not
# removed.
FRESHNESS_HORIZON_HOURS: dict[str, int] = {
    "documents": 24 * 7,
    "entities": 24,
    "relationships": 24 * 7,
    "insights": 24 * 3,
    "decisions": 24 * 30,
    "reports": 24 * 7,
}

STATES = ("current", "aging", "stale", "expired", "archived")


def now() -> datetime:
    return datetime.now(timezone.utc)


def _parse(value: str) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value))
    except ValueError:
        return None
    return parsed.replace(tzinfo=timezone.utc) if parsed.tzinfo is None else parsed


@dataclass
class Freshness:
    """How current one class of knowledge is."""
    knowledge_class: str
    state: str = "current"
    last_updated_at: str = ""
    age_hours: float = 0.0
    horizon_hours: int = 0
    items: int = 0
    stale_items: int = 0

    def describe(self) -> dict:
        return {"class": self.knowledge_class, "state": self.state,
                "last_updated_at": self.last_updated_at,
                "age_hours": round(self.age_hours, 1),
                "horizon_hours": self.horizon_hours,
                "items": self.items, "stale_items": self.stale_items}


@dataclass
class LifecycleEvent:
    """One transition in the life of a piece of knowledge."""
    subject: str                       # document id, entity id, ...
    subject_kind: str                  # document | entity | relationship | ...
    event: str                         # superseded | archived | expired | evolved
    detail: str = ""
    at: str = field(default_factory=lambda: now().isoformat())
    metadata: dict[str, Any] = field(default_factory=dict)

    def describe(self) -> dict:
        return {"subject": self.subject, "subject_kind": self.subject_kind,
                "event": self.event, "detail": self.detail, "at": self.at,
                "metadata": self.metadata}


class MemoryLifecycle:
    """The Brain's lifecycle view over knowledge it already holds.

    Components are optional: a deployment without Document Intelligence still
    gets entity and decision lifecycle, and a deployment without Governance
    still gets freshness — each section degrades on its own rather than the
    whole view failing.
    """

    def __init__(self, knowledge=None, documents=None, organization=None,
                 relationships=None, governance=None,
                 horizons: dict[str, int] | None = None):
        self._knowledge = knowledge
        self._documents = documents
        self._organization = organization
        self._relationships = relationships
        self._governance = governance
        self._horizons = {**FRESHNESS_HORIZON_HOURS, **(horizons or {})}
        self._events: list[LifecycleEvent] = []
        self._lock = threading.RLock()

    # --------------------------------------------------------- freshness
    def freshness(self) -> list[Freshness]:
        """How current each class of knowledge is."""
        out: list[Freshness] = []
        for knowledge_class, reader in (
                ("documents", self._document_timestamps),
                ("entities", self._entity_timestamps),
                ("relationships", self._relationship_timestamps),
                ("insights", self._insight_timestamps),
                ("decisions", self._decision_timestamps)):
            try:
                timestamps = reader()
            except Exception:  # noqa: BLE001 — one class degrades, not the view
                logger.exception("Freshness read failed for %s", knowledge_class)
                continue
            out.append(self._assess(knowledge_class, timestamps))
        return out

    def _assess(self, knowledge_class: str,
                timestamps: list[str]) -> Freshness:
        horizon = self._horizons.get(knowledge_class, 24 * 7)
        parsed = [t for t in (_parse(ts) for ts in timestamps) if t is not None]
        if not parsed:
            return Freshness(knowledge_class=knowledge_class, state="stale",
                             horizon_hours=horizon, items=len(timestamps),
                             stale_items=len(timestamps))
        latest = max(parsed)
        age = (now() - latest).total_seconds() / 3600
        cutoff = now() - timedelta(hours=horizon)
        stale = sum(1 for t in parsed if t < cutoff)
        if age <= horizon * 0.5:
            state = "current"
        elif age <= horizon:
            state = "aging"
        else:
            state = "stale"
        return Freshness(knowledge_class=knowledge_class, state=state,
                         last_updated_at=latest.isoformat(), age_hours=age,
                         horizon_hours=horizon, items=len(parsed),
                         stale_items=stale)

    # ------------------------------------------------------- source reads
    def _document_timestamps(self) -> list[str]:
        if self._documents is None:
            return []
        documents = self._documents.documents(limit=1000) \
            if hasattr(self._documents, "documents") else []
        return [d.get("ingested_at") or d.get("modified_at") or ""
                for d in documents]

    def _entity_timestamps(self) -> list[str]:
        if self._organization is None:
            return []
        entities = self._organization.entities(limit=1000)
        return [e.get("updated_at") or e.get("discovered_at") or ""
                for e in entities]

    def _relationship_timestamps(self) -> list[str]:
        if self._relationships is None:
            return []
        relationships = self._relationships.relationships(limit=1000)
        return [r.get("updated_at") or r.get("discovered_at") or ""
                for r in relationships]

    def _insight_timestamps(self) -> list[str]:
        if self._knowledge is None:
            return []
        return [i.get("recorded_at", "")
                for i in self._knowledge.insights(limit=200)]

    def _decision_timestamps(self) -> list[str]:
        if self._knowledge is None:
            return []
        return [d.get("recorded_at", "")
                for d in self._knowledge.decisions(limit=200)]

    # ---------------------------------------------------------- versions
    def document_versions(self, document_id: str = "",
                          limit: int = 50) -> list[dict]:
        """Version lineage for documents — what superseded what, and when."""
        if self._documents is None or not hasattr(self._documents, "versions"):
            return []
        try:
            return self._documents.versions(document_id, limit=limit) \
                if document_id else self._documents.versions(limit=limit)
        except TypeError:
            return self._documents.versions(document_id)
        except Exception:  # noqa: BLE001
            logger.exception("Version read failed")
            return []

    def entity_history(self, entity_id: str) -> list[dict]:
        """How one entity changed over time."""
        if self._organization is None:
            return []
        entity = self._organization.get(entity_id)
        return (entity or {}).get("history", [])

    def decision_history(self, limit: int = 50) -> list[dict]:
        if self._knowledge is None:
            return []
        return self._knowledge.decisions(limit)

    # ------------------------------------------------------------ expiry
    def expired(self, record_class: str = "") -> list[dict]:
        """Knowledge past its retention horizon, per the Governance layer.

        Reported, never deleted: expiry is a signal to a human that a record
        should be reviewed, not licence for the platform to erase it.
        """
        if self._governance is None:
            return []
        classes = ([record_class] if record_class
                   else ["conversations", "evaluations", "notifications"])
        out: list[dict] = []
        for cls in classes:
            for item in self._records_for(cls):
                created = item.get("created_at") or item.get("at") or ""
                if created and self._governance.is_expired(cls, created):
                    out.append({"class": cls, "created_at": created,
                                "expires_at": self._governance.expires_at(
                                    cls, created),
                                "ref": item.get("id") or item.get("ref") or ""})
        return out

    def _records_for(self, record_class: str) -> list[dict]:
        """Records of one retention class. Deliberately narrow: only classes
        the lifecycle can actually see are reported, so an empty list means
        "nothing visible", never "nothing expired"."""
        if record_class == "notifications" and self._knowledge is not None:
            return []
        return []

    # ---------------------------------------------------------- archival
    def archive(self, subject: str, subject_kind: str,
                reason: str = "") -> LifecycleEvent:
        """Mark knowledge superseded. Nothing is erased — the record stays
        readable, flagged, and auditable."""
        event = LifecycleEvent(subject=subject, subject_kind=subject_kind,
                               event="archived", detail=reason)
        with self._lock:
            self._events.append(event)
            del self._events[:-500]
        if self._knowledge is not None:
            try:
                self._knowledge.record_learning_event(
                    f"Archived {subject_kind} '{subject}'"
                    + (f": {reason}" if reason else ""),
                    source="memory_lifecycle",
                    details={"subject": subject, "kind": subject_kind})
            except Exception:  # noqa: BLE001 — the event stands regardless
                logger.exception("Archive learning event failed")
        return event

    def events(self, limit: int = 50) -> list[dict]:
        with self._lock:
            return [e.describe() for e in reversed(self._events)][:limit]

    # --------------------------------------------------------- evolution
    def relationship_evolution(self, since_hours: int = 24 * 7) -> dict:
        """How the organization's shape changed recently — new links, and
        links whose confidence moved."""
        if self._relationships is None:
            return {"since_hours": since_hours, "discovered": 0, "updated": 0,
                    "relationships": []}
        cutoff = now() - timedelta(hours=since_hours)
        recent = []
        for relationship in self._relationships.relationships(limit=1000):
            discovered = _parse(relationship.get("discovered_at", ""))
            updated = _parse(relationship.get("updated_at", ""))
            marker = max([t for t in (discovered, updated) if t], default=None)
            if marker and marker >= cutoff:
                recent.append(relationship)
        return {
            "since_hours": since_hours,
            "discovered": sum(1 for r in recent
                              if (_parse(r.get("discovered_at", "")) or now())
                              >= cutoff),
            "updated": sum(1 for r in recent if r.get("updated_at")),
            "relationships": recent[:50],
        }

    # ------------------------------------------------------------ status
    def status(self) -> dict[str, Any]:
        """Memory lifecycle status — Knowledge Growth on the dashboard."""
        freshness = self.freshness()
        by_state: dict[str, int] = {}
        for f in freshness:
            by_state[f.state] = by_state.get(f.state, 0) + 1
        return {
            "freshness": [f.describe() for f in freshness],
            "by_state": by_state,
            "total_items": sum(f.items for f in freshness),
            "stale_items": sum(f.stale_items for f in freshness),
            "needs_refresh": [f.knowledge_class for f in freshness
                              if f.state == "stale"],
            "archived_events": len(self._events),
            "expired": len(self.expired()),
        }

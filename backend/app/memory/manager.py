"""Memory layers for agents.

- WorkingMemory        — scratch state for one agent task (in-process).
- ConversationMemory   — persisted per-project chat history (copilot recall).
- BusinessMemory       — read access to a project's analytical artifacts.
- OrganizationalMemory — the enterprise KnowledgeStore (long-term, org-wide).

MemoryManager hands agents the right layer; agents never touch persistence
directly.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from app.knowledge.store import KnowledgeStore
from app.repositories.artifact_store import ArtifactStore


class WorkingMemory:
    """Ephemeral scratchpad for a single agent run."""

    def __init__(self) -> None:
        self._data: dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        self._data[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def snapshot(self) -> dict[str, Any]:
        return dict(self._data)


class ConversationMemory:
    """Persisted per-project conversation history."""

    def __init__(self, store: ArtifactStore, project_id: str, max_turns: int = 200):
        self._store = store
        self._project_id = project_id
        self._max_turns = max_turns

    def append(self, role: str, content: str, meta: dict | None = None) -> None:
        history = self._store.load(self._project_id, "conversation", []) or []
        history.append({"role": role, "content": content, "meta": meta or {},
                        "at": datetime.now(timezone.utc).isoformat()})
        self._store.save(self._project_id, "conversation", history[-self._max_turns:])

    def recent(self, n: int = 10) -> list[dict]:
        history = self._store.load(self._project_id, "conversation", []) or []
        return history[-n:]


class BusinessMemory:
    """What the platform currently knows about one project's business."""

    def __init__(self, store: ArtifactStore, project_id: str):
        self._store = store
        self._project_id = project_id

    def artifact(self, name: str, default: Any = None) -> Any:
        return self._store.load(self._project_id, name, default)

    def context(self) -> dict:
        return self.artifact("business_context", {}) or {}


class MemoryManager:
    """Single entry point agents use to reach every memory layer."""

    def __init__(self, store: ArtifactStore, knowledge: KnowledgeStore):
        self._store = store
        self.organizational: KnowledgeStore = knowledge  # long-term, org-wide

    def working(self) -> WorkingMemory:
        return WorkingMemory()

    def conversation(self, project_id: str) -> ConversationMemory:
        return ConversationMemory(self._store, project_id)

    def business(self, project_id: str) -> BusinessMemory:
        return BusinessMemory(self._store, project_id)

    def project(self, project_id: str) -> BusinessMemory:
        """Project memory: everything persisted for one project (artifacts,
        analysis outputs, plan, business context) — same surface as business
        memory, named per the SDS memory layers."""
        return BusinessMemory(self._store, project_id)

    # SDS memory layers persisted in organizational knowledge -------------
    def decision_memory(self, limit: int = 20) -> list[dict]:
        return self.organizational.decisions(limit)

    def report_memory(self, limit: int = 20) -> list[dict]:
        return self.organizational.report_history(limit)

    def learning_memory(self, limit: int = 50) -> list[dict]:
        return self.organizational.learning_history(limit)

    def strategic_memory(self, limit: int = 20) -> list[dict]:
        return self.organizational.strategic_insights(limit)

    # Convenience passthroughs for the most common learning events -------
    def remember_clarification(self, question: str, answer: str,
                               signature: str = "", project_id: str = "") -> None:
        self.organizational.remember_clarification(question, answer, signature, project_id)

    def recall_clarification(self, question: str, signature: str = "") -> dict | None:
        return self.organizational.find_clarification(question, signature)

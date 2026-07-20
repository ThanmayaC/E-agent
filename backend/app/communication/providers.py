"""Provider interfaces for future enterprise integrations (Version 2).

Automation Preparation: clean, abstract contracts for email, calendar,
meetings, messaging, documents, and external task systems. NO external
provider is implemented here — Outlook, Teams, SharePoint, Slack, Jira etc.
arrive in Version 2 by implementing one of these interfaces and registering
it; no other layer changes.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

PROVIDER_KINDS = ("email", "calendar", "meeting", "messaging", "document",
                  "task",
                  # V2.2: generic outbound channels. "rest" calls a configured
                  # enterprise API; "webhook" posts an event to a subscriber.
                  # Both exist so an integration that is not email/chat/docs
                  # still arrives as an adapter rather than as bespoke code.
                  "rest", "webhook")


class ProviderNotConfigured(RuntimeError):
    pass


class BaseProvider(ABC):
    """Common contract every integration provider fulfils."""

    kind: str = ""          # one of PROVIDER_KINDS
    name: str = ""          # e.g. "outlook", "google-calendar" (V2)

    @property
    def available(self) -> bool:
        return False

    @property
    def unavailable_reason(self) -> str:
        return "no external provider configured (Version 2)"

    def describe(self) -> dict:
        return {"kind": self.kind, "name": self.name,
                "available": self.available,
                "unavailable_reason": self.unavailable_reason}


class EmailProvider(BaseProvider):
    kind = "email"

    @abstractmethod
    def draft(self, to: list[str], subject: str, body: str) -> dict: ...

    @abstractmethod
    def send(self, draft_id: str) -> dict: ...


class CalendarProvider(BaseProvider):
    kind = "calendar"

    @abstractmethod
    def schedule_event(self, title: str, start: str, end: str,
                       attendees: list[str]) -> dict: ...

    @abstractmethod
    def upcoming_events(self, days: int = 7) -> list[dict]: ...


class MeetingProvider(BaseProvider):
    kind = "meeting"

    @abstractmethod
    def schedule_meeting(self, title: str, start: str,
                         attendees: list[str]) -> dict: ...

    @abstractmethod
    def meeting_summary(self, meeting_id: str) -> dict: ...


class MessagingProvider(BaseProvider):
    kind = "messaging"

    @abstractmethod
    def post_message(self, channel: str, text: str) -> dict: ...


class DocumentProvider(BaseProvider):
    kind = "document"

    @abstractmethod
    def fetch_document(self, uri: str) -> bytes: ...

    @abstractmethod
    def store_document(self, name: str, content: bytes) -> str: ...


class TaskProvider(BaseProvider):
    kind = "task"

    @abstractmethod
    def push_task(self, task: dict) -> str: ...

    @abstractmethod
    def pull_tasks(self) -> list[dict]: ...


class RestProvider(BaseProvider):
    """A configured enterprise REST endpoint the platform may call.

    Deliberately narrow: ``call`` takes a path relative to a configured base
    URL, never an arbitrary URL. An adapter that accepts any URL is a
    server-side request forgery waiting to be triggered by generated content.
    """
    kind = "rest"

    @abstractmethod
    def call(self, method: str, path: str, payload: dict | None = None,
             params: dict | None = None) -> dict: ...


class WebhookProvider(BaseProvider):
    """Outbound event delivery to a configured subscriber."""
    kind = "webhook"

    @abstractmethod
    def emit(self, event: str, payload: dict) -> dict: ...


class ProviderRegistry:
    """Registered integrations by kind. Empty in Version 1 — the describe()
    surface still exposes every slot so the UI and the Automation Module can
    show what will become available."""

    def __init__(self) -> None:
        self._providers: dict[str, BaseProvider] = {}

    def register(self, provider: BaseProvider) -> None:
        if provider.kind not in PROVIDER_KINDS:
            raise ValueError(f"Unknown provider kind: {provider.kind}")
        self._providers[provider.kind] = provider

    def get(self, kind: str) -> BaseProvider:
        provider = self._providers.get(kind)
        if provider is None or not provider.available:
            raise ProviderNotConfigured(
                f"No {kind} provider configured (Version 2)")
        return provider

    def describe(self) -> list[dict[str, Any]]:
        out = []
        for kind in PROVIDER_KINDS:
            provider = self._providers.get(kind)
            out.append(provider.describe() if provider else {
                "kind": kind, "name": "", "available": False,
                "unavailable_reason": "no external provider configured "
                                      "(Version 2)"})
        return out

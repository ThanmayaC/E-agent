"""Communication Module (SDS §2.8) — status: partial.

Implemented: the internal notification framework (new reports, critical
risks, task deadlines, portfolio changes, workflow failures,
recommendations) consumed by the Executive Workspace.

Prepared (interfaces only — Version 2): Email, Calendar, Meeting,
Messaging, Document, and Task provider contracts plus the registry that
future external integrations (Outlook, Teams, Slack, ...) plug into. The
legacy planned tools remain registered in the tool layer.
"""
from app.communication import (
    NOTIFICATION_KINDS, BaseProvider, CalendarProvider, DocumentProvider,
    EmailProvider, MeetingProvider, MessagingProvider, NotificationCenter,
    ProviderRegistry, TaskProvider,
)
from app.tools.planned import CalendarTool, EmailTool

__all__ = ["NOTIFICATION_KINDS", "NotificationCenter", "BaseProvider",
           "CalendarProvider", "DocumentProvider", "EmailProvider",
           "MeetingProvider", "MessagingProvider", "ProviderRegistry",
           "TaskProvider", "CalendarTool", "EmailTool"]

STATUS = "partial"

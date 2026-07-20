"""Communication Module.

Internal notification framework, the provider contracts, and — since
Version 2 — the external adapters that fulfil them: Outlook (email via
Microsoft Graph), Teams (messaging via incoming webhook), and SharePoint
(documents via Graph). Adapters are configured by environment reference and
report their own availability; the Action Queue's approval layer remains
the only path to an external send.
"""
from app.communication.adapters import (
    OutlookEmailAdapter, SharePointDocumentAdapter, TeamsMessagingAdapter,
    build_default_adapters,
)
from app.communication.notifications import NOTIFICATION_KINDS, NotificationCenter
from app.communication.providers import (
    BaseProvider, CalendarProvider, DocumentProvider, EmailProvider,
    MeetingProvider, MessagingProvider, ProviderRegistry, TaskProvider,
)

__all__ = ["NOTIFICATION_KINDS", "NotificationCenter", "BaseProvider",
           "CalendarProvider", "DocumentProvider", "EmailProvider",
           "MeetingProvider", "MessagingProvider", "OutlookEmailAdapter",
           "ProviderRegistry", "SharePointDocumentAdapter", "TaskProvider",
           "TeamsMessagingAdapter", "build_default_adapters"]

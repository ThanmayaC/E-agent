"""Communication adapters (Version 2) — Outlook, Teams, SharePoint.

Each adapter implements one of the V1 provider contracts and registers in
the existing ProviderRegistry; no producer changed to gain them. They are
configured by environment reference, never by stored credential:

    EDIP_MS_GRAPH_AUTH      bearer token, or "tenant:client_id:client_secret"
    EDIP_MAIL_SENDER        mailbox to send as (client-credentials flow);
                            empty = /me (delegated token)
    EDIP_TEAMS_WEBHOOK_URL  a Teams incoming-webhook URL
    EDIP_SP_DRIVE_ID        SharePoint drive id for stored documents

An adapter whose configuration is absent reports ``available = False`` and
the platform behaves exactly as V1: approved communications stay queued,
visibly waiting, until an administrator configures the channel. Nothing is
sent anywhere without going through the Action Queue's approval layer first.
"""
from __future__ import annotations

import os
import uuid
from datetime import datetime, timezone
from typing import Any

import httpx

from app.communication.providers import (
    DocumentProvider, EmailProvider, MessagingProvider, ProviderNotConfigured,
    RestProvider, WebhookProvider,
)
from app.core.logging import get_logger

logger = get_logger(__name__)

GRAPH_AUTH_ENV = "EDIP_MS_GRAPH_AUTH"
MAIL_SENDER_ENV = "EDIP_MAIL_SENDER"
TEAMS_WEBHOOK_ENV = "EDIP_TEAMS_WEBHOOK_URL"
SP_DRIVE_ENV = "EDIP_SP_DRIVE_ID"
# V2.2 generic outbound channels
REST_BASE_ENV = "EDIP_REST_BASE_URL"
REST_AUTH_ENV = "EDIP_REST_AUTH_TOKEN"
WEBHOOK_URL_ENV = "EDIP_WEBHOOK_URL"


def _graph_client():
    from app.communication.graph import GraphClient
    return GraphClient(os.environ[GRAPH_AUTH_ENV])


class OutlookEmailAdapter(EmailProvider):
    """Sends approved email through Microsoft Graph (Outlook)."""

    name = "outlook"

    def __init__(self, auth_env: str = GRAPH_AUTH_ENV,
                 sender_env: str = MAIL_SENDER_ENV):
        self._auth_env = auth_env
        self._sender_env = sender_env
        self._drafts: dict[str, dict] = {}

    @property
    def available(self) -> bool:
        return bool(os.environ.get(self._auth_env))

    @property
    def unavailable_reason(self) -> str:
        if self.available:
            return ""
        return (f"set {self._auth_env} (bearer token or "
                f"'tenant:client_id:client_secret') to enable Outlook")

    def draft(self, to: list[str], subject: str, body: str) -> dict:
        draft = {"draft_id": f"draft_{uuid.uuid4().hex[:10]}", "to": to,
                 "subject": subject, "body": body}
        self._drafts[draft["draft_id"]] = draft
        return draft

    def send(self, draft_id: str) -> dict:
        draft = self._drafts.get(draft_id)
        if draft is None:
            raise KeyError(f"Unknown draft: {draft_id}")
        result = self.send_direct(draft["to"], draft["subject"],
                                  draft["body"])
        self._drafts.pop(draft_id, None)
        return result

    def send_direct(self, to: list[str], subject: str, body: str) -> dict:
        """One approved send. The Action Queue is the only caller."""
        if not to:
            raise ValueError("email needs at least one recipient")
        client = _graph_client()
        sender = os.environ.get(self._sender_env, "")
        base = f"/users/{sender}" if sender else "/me"
        client.post(f"{base}/sendMail", {
            "message": {
                "subject": subject[:250],
                "body": {"contentType": "Text", "content": body},
                "toRecipients": [{"emailAddress": {"address": addr}}
                                 for addr in to],
            },
            "saveToSentItems": True,
        })
        logger.info("Sent email '%s' to %d recipient(s) via Outlook",
                    subject[:60], len(to))
        return {"sent": True, "to": to, "subject": subject[:120],
                "channel": "outlook"}


class TeamsMessagingAdapter(MessagingProvider):
    """Posts approved messages to a Teams channel via an incoming webhook."""

    name = "teams"

    def __init__(self, webhook_env: str = TEAMS_WEBHOOK_ENV,
                 timeout: float = 20.0):
        self._webhook_env = webhook_env
        self._timeout = timeout

    @property
    def available(self) -> bool:
        return bool(os.environ.get(self._webhook_env))

    @property
    def unavailable_reason(self) -> str:
        if self.available:
            return ""
        return (f"set {self._webhook_env} to a Teams incoming-webhook URL "
                f"to enable Teams announcements")

    def post_message(self, channel: str, text: str) -> dict:
        """``channel`` may carry a webhook URL to target a different channel;
        empty means the default configured webhook."""
        url = channel if channel.startswith("https://") \
            else os.environ.get(self._webhook_env, "")
        if not url:
            raise RuntimeError(self.unavailable_reason)
        response = httpx.post(url, json={"text": text[:4000]},
                              timeout=self._timeout)
        if response.status_code >= 400:
            raise RuntimeError(
                f"Teams webhook rejected the message "
                f"({response.status_code}): {response.text[:150]}")
        logger.info("Posted a Teams message (%d chars)", len(text))
        return {"posted": True, "channel": "teams", "chars": len(text)}


class SharePointDocumentAdapter(DocumentProvider):
    """Fetches and stores documents on a SharePoint drive via Graph."""

    name = "sharepoint"

    def __init__(self, auth_env: str = GRAPH_AUTH_ENV,
                 drive_env: str = SP_DRIVE_ENV):
        self._auth_env = auth_env
        self._drive_env = drive_env

    @property
    def available(self) -> bool:
        return bool(os.environ.get(self._auth_env)) \
            and bool(os.environ.get(self._drive_env))

    @property
    def unavailable_reason(self) -> str:
        if self.available:
            return ""
        return (f"set {self._auth_env} and {self._drive_env} to enable "
                f"SharePoint document storage")

    def fetch_document(self, uri: str) -> bytes:
        client = _graph_client()
        if uri.startswith("http"):
            return client.download(uri)
        drive = os.environ[self._drive_env]
        item = client.get(f"/drives/{drive}/root:/{uri.strip('/')}")
        download_url = item.get("@microsoft.graph.downloadUrl", "")
        if not download_url:
            raise RuntimeError(f"no downloadable content at {uri}")
        return client.download(download_url)

    def store_document(self, name: str, content: bytes) -> str:
        client = _graph_client()
        drive = os.environ[self._drive_env]
        item = client.put_content(
            f"/drives/{drive}/root:/{name.strip('/')}:/content", content)
        return item.get("webUrl", "") or item.get("id", "")


class RestApiAdapter(RestProvider):
    """Calls a configured enterprise REST API.

    The base URL comes from configuration, never from a caller: ``call``
    takes a *path*, which is joined onto that base. Generated content can
    therefore influence which endpoint of a trusted API is called, but never
    which host is contacted.
    """

    name = "rest"

    def __init__(self, base_env: str = REST_BASE_ENV,
                 auth_env: str = REST_AUTH_ENV, timeout: float = 20.0):
        self._base_env = base_env
        self._auth_env = auth_env
        self._timeout = timeout

    @property
    def available(self) -> bool:
        return bool(os.environ.get(self._base_env))

    @property
    def unavailable_reason(self) -> str:
        if self.available:
            return ""
        return (f"set {self._base_env} to the API base URL (and "
                f"{self._auth_env} for a bearer token) to enable REST calls")

    def call(self, method: str, path: str, payload: dict | None = None,
             params: dict | None = None) -> dict:
        base = os.environ.get(self._base_env, "")
        if not base:
            raise ProviderNotConfigured(self.unavailable_reason)
        if method.upper() not in ("GET", "POST", "PUT", "PATCH", "DELETE"):
            raise ValueError(f"Unsupported HTTP method: {method}")
        url = f"{base.rstrip('/')}/{str(path).lstrip('/')}"
        headers = {"Accept": "application/json"}
        token = os.environ.get(self._auth_env, "")
        if token:
            headers["Authorization"] = f"Bearer {token}"
        response = httpx.request(method.upper(), url, json=payload,
                                 params=params, headers=headers,
                                 timeout=self._timeout)
        response.raise_for_status()
        logger.info("REST %s %s -> %s", method.upper(), path,
                    response.status_code)
        try:
            body = response.json()
        except ValueError:
            body = {"text": response.text[:2000]}
        return {"status_code": response.status_code, "body": body}


class WebhookAdapter(WebhookProvider):
    """Posts platform events to a configured subscriber endpoint."""

    name = "webhook"

    def __init__(self, url_env: str = WEBHOOK_URL_ENV, timeout: float = 20.0):
        self._url_env = url_env
        self._timeout = timeout

    @property
    def available(self) -> bool:
        return bool(os.environ.get(self._url_env))

    @property
    def unavailable_reason(self) -> str:
        if self.available:
            return ""
        return f"set {self._url_env} to a subscriber URL to enable webhooks"

    def emit(self, event: str, payload: dict) -> dict:
        url = os.environ.get(self._url_env, "")
        if not url:
            raise ProviderNotConfigured(self.unavailable_reason)
        body = {"event": event, "payload": payload,
                "emitted_at": datetime.now(timezone.utc).isoformat()}
        response = httpx.post(url, json=body, timeout=self._timeout)
        response.raise_for_status()
        logger.info("Webhook '%s' delivered (%s)", event, response.status_code)
        return {"delivered": True, "event": event,
                "status_code": response.status_code}


def build_default_adapters() -> list[Any]:
    """The V2/V2.2 communication adapters, ready to register. Availability is
    each adapter's own report — registration is unconditional so the
    Settings surface can show what is configured and what is missing."""
    return [OutlookEmailAdapter(), TeamsMessagingAdapter(),
            SharePointDocumentAdapter(), RestApiAdapter(), WebhookAdapter()]

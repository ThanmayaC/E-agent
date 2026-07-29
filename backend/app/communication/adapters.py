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

    def describe(self) -> dict:
        return {**super().describe(),
                "capabilities": ["read", "search", "draft", "send"]}

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

    def _mailbox_base(self) -> str:
        """The mailbox to act on: a configured sender (app/client-credentials
        flow) or ``/me`` (a delegated token)."""
        sender = os.environ.get(self._sender_env, "")
        return f"/users/{sender}" if sender else "/me"

    def read_messages(self, folder: str = "inbox", top: int = 25) -> list[dict]:
        """Read recent messages from a mail folder. A read-only view the
        Enterprise Brain can treat as another knowledge source; it never
        sends. Returns [] with a clear reason when Outlook is not configured."""
        if not self.available:
            raise ProviderNotConfigured(self.unavailable_reason)
        client = _graph_client()
        path = f"{self._mailbox_base()}/mailFolders/{folder}/messages"
        messages = client.get_all(path, params={
            "$top": min(int(top), 100),
            "$select": "id,subject,from,receivedDateTime,bodyPreview,isRead",
            "$orderby": "receivedDateTime desc"}, limit=int(top))
        return [_email_summary(m) for m in messages]

    def search_messages(self, query: str, top: int = 25) -> list[dict]:
        """Search historical email by free text (Graph ``$search``)."""
        if not self.available:
            raise ProviderNotConfigured(self.unavailable_reason)
        if not str(query).strip():
            raise ValueError("a search needs a query")
        client = _graph_client()
        path = f"{self._mailbox_base()}/messages"
        # $search must be quoted; Graph requires no $orderby alongside it.
        messages = client.get_all(path, params={
            "$search": f'"{query}"', "$top": min(int(top), 100),
            "$select": "id,subject,from,receivedDateTime,bodyPreview"},
            limit=int(top))
        return [_email_summary(m) for m in messages]

    def get_message(self, message_id: str) -> dict:
        """One message with its body — for drafting a grounded reply."""
        if not self.available:
            raise ProviderNotConfigured(self.unavailable_reason)
        client = _graph_client()
        message = client.get(
            f"{self._mailbox_base()}/messages/{message_id}",
            params={"$select": "id,subject,from,toRecipients,"
                               "receivedDateTime,body,bodyPreview"})
        summary = _email_summary(message)
        body = message.get("body") or {}
        summary["body"] = str(body.get("content", ""))[:8000]
        return summary

    def send_direct(self, to: list[str], subject: str, body: str) -> dict:
        """One approved send. The Action Queue is the only caller."""
        if not to:
            raise ValueError("email needs at least one recipient")
        client = _graph_client()
        base = self._mailbox_base()
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


GMAIL_AUTH_ENV = "EDIP_GMAIL_AUTH"          # OAuth2 access token (Bearer)
GMAIL_SENDER_ENV = "EDIP_GMAIL_SENDER"      # "From" address; empty = the token's own address
GMAIL_API = "https://gmail.googleapis.com/gmail/v1/users/me"


class GmailEmailAdapter(EmailProvider):
    """Reads, searches, drafts and sends approved email through the Gmail REST
    API. Same contract and summary shape as :class:`OutlookEmailAdapter`, so the
    Enterprise Brain and the workspace treat Gmail as just another email source
    and the Action Queue is still the only path to an actual send.

    Configured purely by environment reference — never a stored credential:

        EDIP_GMAIL_AUTH    an OAuth2 access token (Bearer) for the mailbox
        EDIP_GMAIL_SENDER  optional display "From" address

    Absent configuration ⇒ ``available = False`` and nothing is contacted."""

    name = "gmail"

    def __init__(self, auth_env: str = GMAIL_AUTH_ENV,
                 sender_env: str = GMAIL_SENDER_ENV, timeout: float = 20.0):
        self._auth_env = auth_env
        self._sender_env = sender_env
        self._timeout = timeout
        self._drafts: dict[str, dict] = {}

    @property
    def available(self) -> bool:
        return bool(os.environ.get(self._auth_env))

    @property
    def unavailable_reason(self) -> str:
        if self.available:
            return ""
        return (f"set {self._auth_env} to a Gmail OAuth2 access token "
                f"to enable Gmail")

    def describe(self) -> dict:
        return {**super().describe(),
                "capabilities": ["read", "search", "draft", "send"]}

    # -- HTTP helpers ----------------------------------------------------
    def _headers(self) -> dict:
        token = os.environ.get(self._auth_env, "")
        if not token:
            raise ProviderNotConfigured(self.unavailable_reason)
        return {"Authorization": f"Bearer {token}",
                "Accept": "application/json"}

    def _get(self, path: str, params: dict | None = None) -> dict:
        r = httpx.get(f"{GMAIL_API}{path}", headers=self._headers(),
                      params=params, timeout=self._timeout)
        r.raise_for_status()
        return r.json()

    def _post(self, path: str, payload: dict) -> dict:
        r = httpx.post(f"{GMAIL_API}{path}", headers=self._headers(),
                       json=payload, timeout=self._timeout)
        r.raise_for_status()
        return r.json()

    # -- read-only knowledge source -------------------------------------
    def read_messages(self, folder: str = "inbox", top: int = 25) -> list[dict]:
        """Recent messages from a Gmail label (``inbox`` by default). Read-only
        — another knowledge source for the Brain; it never sends."""
        return self._list_and_hydrate(f"in:{folder or 'inbox'}", top)

    def search_messages(self, query: str, top: int = 25) -> list[dict]:
        """Search historical mail with Gmail's native query syntax."""
        if not str(query).strip():
            raise ValueError("a search needs a query")
        return self._list_and_hydrate(query, top)

    def _list_and_hydrate(self, q: str, top: int) -> list[dict]:
        listing = self._get("/messages",
                            {"q": q, "maxResults": min(int(top), 100)})
        out: list[dict] = []
        for stub in (listing.get("messages") or [])[:int(top)]:
            msg = self._get(f"/messages/{stub['id']}",
                            {"format": "metadata",
                             "metadataHeaders": ["Subject", "From", "Date"]})
            out.append(_gmail_summary(msg))
        return out

    def get_message(self, message_id: str) -> dict:
        """One message with its plain-text body — for a grounded reply."""
        msg = self._get(f"/messages/{message_id}", {"format": "full"})
        summary = _gmail_summary(msg)
        summary["body"] = _gmail_extract_body(msg.get("payload") or {})[:8000]
        return summary

    # -- draft / approved send ------------------------------------------
    def draft(self, to: list[str], subject: str, body: str) -> dict:
        draft = {"draft_id": f"draft_{uuid.uuid4().hex[:10]}", "to": to,
                 "subject": subject, "body": body}
        self._drafts[draft["draft_id"]] = draft
        return draft

    def send(self, draft_id: str) -> dict:
        draft = self._drafts.get(draft_id)
        if draft is None:
            raise KeyError(f"Unknown draft: {draft_id}")
        result = self.send_direct(draft["to"], draft["subject"], draft["body"])
        self._drafts.pop(draft_id, None)
        return result

    def send_direct(self, to: list[str], subject: str, body: str) -> dict:
        """One approved send. The Action Queue is the only caller."""
        if not to:
            raise ValueError("email needs at least one recipient")
        self._post("/messages/send", {"raw": _gmail_raw(
            to, subject, body, os.environ.get(self._sender_env, ""))})
        logger.info("Sent email '%s' to %d recipient(s) via Gmail",
                    subject[:60], len(to))
        return {"sent": True, "to": to, "subject": subject[:120],
                "channel": "gmail"}


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

    def describe(self) -> dict:
        return {**super().describe(),
                "read_available": self.read_available,
                "read_unavailable_reason": self.read_unavailable_reason,
                "capabilities": (["read"] if self.read_available else [])
                + (["post"] if self.available else [])}

    @property
    def read_available(self) -> bool:
        """Reading channels and messages needs a Graph credential, which is a
        different capability from the outgoing webhook used to post."""
        return bool(os.environ.get(GRAPH_AUTH_ENV))

    @property
    def read_unavailable_reason(self) -> str:
        if self.read_available:
            return ""
        return (f"set {GRAPH_AUTH_ENV} to read Teams channels and messages "
                f"(a bearer token or 'tenant:client_id:client_secret')")

    def read_channels(self, team_id: str) -> list[dict]:
        """List a team's channels — read-only, another Brain knowledge source."""
        if not self.read_available:
            raise ProviderNotConfigured(self.read_unavailable_reason)
        client = _graph_client()
        channels = client.get_all(f"/teams/{team_id}/channels",
                                  params={"$select": "id,displayName,"
                                                     "description"}, limit=100)
        return [{"id": c.get("id", ""),
                 "name": c.get("displayName", ""),
                 "description": c.get("description", "")} for c in channels]

    def read_messages(self, team_id: str, channel_id: str,
                      top: int = 25) -> list[dict]:
        """Read recent messages in a channel. Never posts."""
        if not self.read_available:
            raise ProviderNotConfigured(self.read_unavailable_reason)
        client = _graph_client()
        messages = client.get_all(
            f"/teams/{team_id}/channels/{channel_id}/messages",
            params={"$top": min(int(top), 50)}, limit=int(top))
        return [_teams_message_summary(m) for m in messages]

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


def _email_summary(message: dict) -> dict:
    """Normalize a Graph message into a compact, body-preview-only summary —
    the shape the Brain and the workspace consume."""
    sender = ((message.get("from") or {}).get("emailAddress") or {})
    return {
        "id": message.get("id", ""),
        "subject": message.get("subject", ""),
        "from": sender.get("address", "") or sender.get("name", ""),
        "received": message.get("receivedDateTime", ""),
        "preview": str(message.get("bodyPreview", ""))[:500],
        "is_read": message.get("isRead"),
        "channel": "outlook",
    }


def _gmail_header(headers: list[dict], name: str) -> str:
    for h in headers or []:
        if str(h.get("name", "")).lower() == name.lower():
            return str(h.get("value", ""))
    return ""


def _gmail_summary(message: dict) -> dict:
    """Normalize a Gmail message into the same compact shape as Outlook's, so
    downstream code is provider-agnostic."""
    payload = message.get("payload") or {}
    headers = payload.get("headers") or []
    label_ids = message.get("labelIds") or []
    return {
        "id": message.get("id", ""),
        "subject": _gmail_header(headers, "Subject"),
        "from": _gmail_header(headers, "From"),
        "received": _gmail_header(headers, "Date"),
        "preview": str(message.get("snippet", ""))[:500],
        "is_read": "UNREAD" not in label_ids,
        "channel": "gmail",
    }


def _gmail_extract_body(payload: dict) -> str:
    """Depth-first walk of a Gmail MIME tree for the first text/plain part."""
    import base64

    def _decode(data: str) -> str:
        try:
            return base64.urlsafe_b64decode(data.encode()).decode(
                "utf-8", "replace")
        except Exception:  # noqa: BLE001 — malformed part, skip it
            return ""

    if payload.get("mimeType") == "text/plain":
        return _decode((payload.get("body") or {}).get("data", ""))
    for part in payload.get("parts") or []:
        text = _gmail_extract_body(part)
        if text:
            return text
    # fall back to any body data present on the root
    return _decode((payload.get("body") or {}).get("data", ""))


def _gmail_raw(to: list[str], subject: str, body: str, sender: str) -> str:
    """Build an RFC-2822 message and base64url-encode it for Gmail's API."""
    import base64
    from email.message import EmailMessage

    msg = EmailMessage()
    msg["To"] = ", ".join(to)
    msg["Subject"] = subject[:250]
    if sender:
        msg["From"] = sender
    msg.set_content(body)
    return base64.urlsafe_b64encode(msg.as_bytes()).decode()


def _teams_message_summary(message: dict) -> dict:
    from_user = (((message.get("from") or {}).get("user")) or {})
    body = (message.get("body") or {})
    return {
        "id": message.get("id", ""),
        "from": from_user.get("displayName", ""),
        "created": message.get("createdDateTime", ""),
        "text": str(body.get("content", ""))[:2000],
        "channel": "teams",
    }


def build_default_adapters() -> list[Any]:
    """The V2/V2.2 communication adapters, ready to register. Availability is
    each adapter's own report — registration is unconditional so the
    Settings surface can show what is configured and what is missing."""
    return [OutlookEmailAdapter(), GmailEmailAdapter(), TeamsMessagingAdapter(),
            SharePointDocumentAdapter(), RestApiAdapter(), WebhookAdapter()]

"""Microsoft Graph client (Version 2).

One small HTTP client shared by everything that talks to Microsoft 365: the
Outlook/Teams/SharePoint synchronization readers and the communication
adapters. Nothing here knows what a mailbox or a drive *means* — it resolves
credentials, paginates, and moves bytes.

Credentials follow the platform's reference-only rule: the credential value
lives in an environment variable and is resolved in memory at call time.
Two credential shapes are accepted:

    "<bearer token>"                         — a ready access token
    "<tenant_id>:<client_id>:<client_secret>" — client-credentials flow;
                                                tokens are fetched and cached
                                                until shortly before expiry
"""
from __future__ import annotations

import threading
import time
from typing import Any

import httpx

from app.core.logging import get_logger

logger = get_logger(__name__)

GRAPH_BASE = "https://graph.microsoft.com/v1.0"
LOGIN_BASE = "https://login.microsoftonline.com"
TOKEN_EARLY_REFRESH_S = 120
MAX_PAGES = 20


class GraphAuthError(RuntimeError):
    """The credential cannot be turned into a Graph access token."""


class GraphError(RuntimeError):
    """A Graph call failed."""


class GraphClient:
    """Minimal Microsoft Graph client: auth, GET with pagination, POST,
    content download/upload. Synchronous — every caller runs on the
    scheduler thread or a request thread, never in an event loop."""

    def __init__(self, credential: str, base_url: str = GRAPH_BASE,
                 timeout: float = 30.0):
        if not credential or not credential.strip():
            raise GraphAuthError("empty Microsoft Graph credential")
        self._credential = credential.strip()
        self._base = base_url.rstrip("/")
        self._timeout = timeout
        self._token: str = ""
        self._token_expires: float = 0.0
        self._lock = threading.Lock()

    # ------------------------------------------------------------------ auth
    def token(self) -> str:
        parts = self._credential.split(":")
        if len(parts) != 3:
            return self._credential  # a ready bearer token
        with self._lock:
            if self._token and time.time() < self._token_expires:
                return self._token
            tenant, client_id, secret = parts
            response = httpx.post(
                f"{LOGIN_BASE}/{tenant}/oauth2/v2.0/token",
                data={"grant_type": "client_credentials",
                      "client_id": client_id, "client_secret": secret,
                      "scope": "https://graph.microsoft.com/.default"},
                timeout=self._timeout)
            if response.status_code != 200:
                raise GraphAuthError(
                    f"token request failed ({response.status_code}): "
                    f"{response.text[:200]}")
            payload = response.json()
            self._token = payload["access_token"]
            self._token_expires = (time.time()
                                   + int(payload.get("expires_in", 3600))
                                   - TOKEN_EARLY_REFRESH_S)
            return self._token

    def _headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.token()}"}

    # ----------------------------------------------------------------- calls
    def get(self, path: str, params: dict | None = None) -> dict:
        url = path if path.startswith("http") else f"{self._base}{path}"
        response = httpx.get(url, params=params, headers=self._headers(),
                             timeout=self._timeout)
        if response.status_code >= 400:
            raise GraphError(f"GET {path} → {response.status_code}: "
                             f"{response.text[:200]}")
        return response.json()

    def get_all(self, path: str, params: dict | None = None,
                limit: int = 500) -> list[dict[str, Any]]:
        """Follow @odata.nextLink pagination up to ``limit`` records."""
        records: list[dict] = []
        payload = self.get(path, params)
        for _ in range(MAX_PAGES):
            records.extend(payload.get("value", []))
            next_link = payload.get("@odata.nextLink", "")
            if not next_link or len(records) >= limit:
                break
            payload = self.get(next_link)
        return records[:limit]

    def post(self, path: str, json: dict) -> dict:
        response = httpx.post(f"{self._base}{path}", json=json,
                              headers=self._headers(), timeout=self._timeout)
        if response.status_code >= 400:
            raise GraphError(f"POST {path} → {response.status_code}: "
                             f"{response.text[:200]}")
        return response.json() if response.content else {}

    def download(self, url: str) -> bytes:
        """Fetch file content. Pre-authenticated download URLs (the
        ``@microsoft.graph.downloadUrl`` shape) need no auth header."""
        headers = {} if "sharepoint.com" in url or "1drv" in url else self._headers()
        response = httpx.get(url, headers=headers, timeout=self._timeout,
                             follow_redirects=True)
        if response.status_code >= 400:
            raise GraphError(f"download → {response.status_code}")
        return response.content

    def put_content(self, path: str, content: bytes,
                    content_type: str = "application/octet-stream") -> dict:
        response = httpx.put(
            f"{self._base}{path}", content=content,
            headers={**self._headers(), "Content-Type": content_type},
            timeout=max(self._timeout, 120.0))
        if response.status_code >= 400:
            raise GraphError(f"PUT {path} → {response.status_code}: "
                             f"{response.text[:200]}")
        return response.json() if response.content else {}

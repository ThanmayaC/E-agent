"""Enterprise Data Source Registry.

Every enterprise system the platform synchronizes with is registered here
once: what it is, how to reach it, how to authenticate, how often to refresh,
whether it is healthy, and where its synchronization got to.

**Credentials are never stored.** A source carries an auth *reference* — the
name of an environment variable (or, in V2, a secret-manager key) — which is
resolved to a value only in memory, at sync time, and never written to disk,
returned by an API, or logged. A registry that holds connection strings is a
credential store, and this one refuses to be one: ``describe()`` is the only
public view and it cannot leak a secret because the secret was never there.

Source kinds are declared for the whole SDS catalogue. What a kind can
actually *do* today is decided by its capability, not by its presence:

    native    — reads through an existing connector today (csv, excel,
                rest_api, and the SQL family via SQLAlchemy)
    interface — the contract exists, the provider arrives in V2
                (sharepoint, outlook, teams)

Registering an interface-only source is allowed and useful: it appears in
Connected Systems as "awaiting integration", and the day its provider lands
nothing else changes.
"""
from __future__ import annotations

import os
import threading
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from app.core.logging import get_logger
from app.sync.store import SyncStore, new_id, now_iso

logger = get_logger(__name__)

CADENCES = {"startup": 0, "15m": 900, "hourly": 3600, "daily": 86400,
            "weekly": 604800, "manual": -1}

HEALTH_STATES = ("unknown", "healthy", "degraded", "unreachable",
                 "unconfigured", "awaiting_integration")

SYNC_STATES = ("never_synced", "syncing", "synced", "failed", "retrying")


@dataclass(frozen=True)
class SourceKind:
    """What a kind of enterprise system is and what it can do here."""
    name: str
    title: str
    capability: str            # native | interface
    connector: str = ""        # existing connector that reads it (native only)
    descriptor: str = ""       # descriptor extension for connector-based reads
    unavailable_reason: str = ""
    # What the source's records ARE: tabular data, documents to parse, or
    # communications. Decides which downstream pipeline consumes the delta.
    family: str = "tabular"    # tabular | documents | communications

    def describe(self) -> dict:
        return {"kind": self.name, "title": self.title,
                "capability": self.capability, "connector": self.connector,
                "family": self.family,
                "available": self.capability == "native",
                "unavailable_reason": self.unavailable_reason}


# The SDS source catalogue. The SQL family shares one connector (SQLAlchemy)
# and differs only in driver — which is part of the URL the operator supplies,
# so there is no provider-specific code here and none is needed.
#
# V2 additions:
#   documents family — folders of enterprise documents (SOPs, RCAs, policies,
#     meeting notes, product docs, OneDrive-synced folders). Read locally,
#     versioned by content hash, parsed by Document Intelligence.
#   graph connector — Microsoft 365 through Microsoft Graph (Outlook mail,
#     Teams channel messages, SharePoint drives). Native the moment an
#     administrator sets the credential env reference; unconfigured until.
SOURCE_KINDS: dict[str, SourceKind] = {
    k.name: k for k in (
        SourceKind("postgresql", "PostgreSQL", "native", "sql",
                   ".sqlsource.json"),
        SourceKind("sqlserver", "SQL Server", "native", "sql",
                   ".sqlsource.json"),
        SourceKind("mysql", "MySQL", "native", "sql", ".sqlsource.json"),
        SourceKind("oracle", "Oracle", "native", "sql", ".sqlsource.json"),
        SourceKind("csv", "CSV files", "native", "csv"),
        SourceKind("excel", "Excel workbooks", "native", "excel"),
        SourceKind("rest_api", "REST APIs", "native", "api",
                   ".apisource.json"),
        # ------------------------------------------------- V2: documents
        SourceKind("document_folder", "Document folder", "native",
                   "documents", family="documents"),
        SourceKind("sop_repository", "SOP repository", "native",
                   "documents", family="documents"),
        SourceKind("rca_repository", "RCA repository", "native",
                   "documents", family="documents"),
        SourceKind("policy_repository", "Policy repository", "native",
                   "documents", family="documents"),
        SourceKind("meeting_notes", "Meeting notes", "native",
                   "documents", family="documents"),
        SourceKind("product_documents", "Product documents", "native",
                   "documents", family="documents"),
        SourceKind("onedrive", "OneDrive (synced folder)", "native",
                   "documents", family="documents"),
        # -------------------------------------------- V2: Microsoft 365
        SourceKind("sharepoint", "SharePoint", "native", "graph",
                   family="documents"),
        SourceKind("outlook", "Outlook", "native", "graph",
                   family="communications"),
        SourceKind("teams", "Microsoft Teams", "native", "graph",
                   family="communications"),
    )
}

SQL_KINDS = tuple(k.name for k in SOURCE_KINDS.values()
                  if k.connector == "sql")


class SecretNotConfigured(RuntimeError):
    """The source's auth reference does not resolve to a value here."""


@dataclass
class AuthConfig:
    """How to authenticate — by reference, never by value.

    ``kind``:
        none  — no authentication (a local file, a public endpoint)
        env   — ``ref`` names an environment variable holding the secret
                (a connection URL, a token). Resolved at sync time only.
    """
    kind: str = "none"
    ref: str = ""

    def describe(self) -> dict:
        """Safe by construction: reports whether the secret resolves, never
        what it is."""
        return {"kind": self.kind, "ref": self.ref,
                "configured": self.resolved() is not None}

    def resolved(self) -> str | None:
        if self.kind == "none":
            return ""
        if self.kind == "env":
            return os.environ.get(self.ref) or None
        return None

    def require(self, source_name: str) -> str:
        value = self.resolved()
        if value is None:
            raise SecretNotConfigured(
                f"Source '{source_name}' needs {self.kind} reference "
                f"'{self.ref}', which is not set in this environment")
        return value


class DataSourceRegistry:
    """Every configured enterprise data source, with its sync state."""

    def __init__(self, store: SyncStore, bus=None):
        self._store = store
        self._bus = bus  # optional EventBus — attached by the runtime
        self._lock = threading.RLock()

    def attach_bus(self, bus) -> None:
        """Announce registrations on the enterprise event bus. The bus is
        owned by the autonomy runtime, which is built after this registry."""
        self._bus = bus

    # ------------------------------------------------------------ catalogue
    @staticmethod
    def kinds() -> list[dict]:
        """The source catalogue: what can be connected, and what is V2."""
        return [k.describe() for k in SOURCE_KINDS.values()]

    # ---------------------------------------------------------- registration
    def register(self, name: str, kind: str, location: str = "",
                 auth: dict | None = None, cadence: str = "hourly",
                 description: str = "", options: dict | None = None,
                 project_id: str = "") -> dict:
        """Register an enterprise system.

        ``location`` is the non-secret half of reaching the source: a file
        path, a base URL, a table list — never a credential. Credentials go in
        ``auth`` as a reference (``{"kind": "env", "ref": "EDIP_PG_URL"}``).
        """
        if kind not in SOURCE_KINDS:
            raise ValueError(f"Unknown source kind: {kind}")
        if cadence not in CADENCES:
            raise ValueError(f"Unknown refresh cadence: {cadence}")
        auth_config = self._auth(auth)
        if _looks_like_a_secret(location):
            raise ValueError(
                "location looks like it contains credentials — put the "
                "connection secret in an environment variable and reference "
                "it via auth {'kind': 'env', 'ref': 'VAR_NAME'}")

        spec = SOURCE_KINDS[kind]
        if spec.connector == "graph" and auth_config.kind == "none":
            raise ValueError(
                f"{spec.title} connects through Microsoft Graph and needs a "
                f"credential reference: auth {{'kind': 'env', 'ref': "
                f"'EDIP_MS_GRAPH_AUTH'}} where the variable holds either a "
                f"bearer token or 'tenant_id:client_id:client_secret'")
        with self._lock:
            if any(s["name"] == name for s in self._store.read("sources")):
                raise ValueError(f"A source named '{name}' is already registered")
            source = {
                "source_id": new_id("src"), "name": name[:120], "kind": kind,
                "title": spec.title, "capability": spec.capability,
                "description": description[:300], "location": location[:500],
                "auth": auth_config.describe(), "cadence": cadence,
                "options": options or {}, "project_id": project_id,
                "enabled": spec.capability == "native",
                "health": self._initial_health(spec, auth_config),
                "health_detail": spec.unavailable_reason,
                "health_checked_at": "",
                "sync_state": "never_synced", "sync_version": 0,
                "first_synced_at": "", "last_synced_at": "",
                "last_sync_status": "", "last_error": "",
                "consecutive_failures": 0, "records_total": 0,
                "next_sync_at": "", "created_at": now_iso(),
                "updated_at": now_iso(),
            }
            self._store.append("sources", source)
        logger.info("Registered data source '%s' (%s, %s)", name, kind,
                    spec.capability)
        self._announce("SourceRegistered", source)
        return source

    def _auth(self, auth: dict | None) -> AuthConfig:
        auth = auth or {}
        kind = auth.get("kind", "none")
        if kind not in ("none", "env"):
            raise ValueError(
                f"Unsupported auth kind: {kind!r}. Use 'none', or 'env' with "
                f"a 'ref' naming the environment variable that holds the "
                f"secret — credentials are never stored by the platform.")
        if kind == "env" and not auth.get("ref"):
            raise ValueError("auth kind 'env' needs a 'ref' (variable name)")
        if any(k in auth for k in ("value", "secret", "password", "token",
                                   "url", "connection_string")):
            raise ValueError(
                "auth must not carry a secret value — pass a reference "
                "({'kind': 'env', 'ref': 'VAR_NAME'}) instead")
        return AuthConfig(kind=kind, ref=auth.get("ref", ""))

    @staticmethod
    def _initial_health(spec: SourceKind, auth: AuthConfig) -> str:
        if spec.capability == "interface":
            return "awaiting_integration"
        if auth.resolved() is None:
            return "unconfigured"
        return "unknown"

    def auth_for(self, source: dict) -> AuthConfig:
        """Rehydrate the auth config for a stored source (reference only)."""
        stored = source.get("auth") or {}
        return AuthConfig(kind=stored.get("kind", "none"),
                          ref=stored.get("ref", ""))

    def remove(self, source_id: str) -> bool:
        with self._lock:
            if not self._store.delete("sources", "source_id", source_id):
                return False
            self._store.drop_fingerprints(source_id)
            return True

    def set_enabled(self, source_id: str, enabled: bool) -> dict | None:
        source = self._require(source_id)
        if enabled and source["capability"] != "native":
            raise ValueError(
                f"'{source['name']}' is {source['title']} — "
                f"{SOURCE_KINDS[source['kind']].unavailable_reason}")
        return self._store.update("sources", "source_id", source_id,
                                  {"enabled": enabled})

    def set_cadence(self, source_id: str, cadence: str) -> dict | None:
        if cadence not in CADENCES:
            raise ValueError(f"Unknown refresh cadence: {cadence}")
        return self._store.update("sources", "source_id", source_id,
                                  {"cadence": cadence})

    # --------------------------------------------------------------- health
    def check_health(self, source_id: str) -> dict:
        """Assess a source without reading it: is it integrable here, are its
        credentials present, is its location reachable-looking, and is its
        sync failing? A real connection attempt is the sync's job — health
        must stay cheap enough to run on every tick."""
        source = self._require(source_id)
        spec = SOURCE_KINDS[source["kind"]]
        auth = self.auth_for(source)

        if spec.capability == "interface":
            health, detail = "awaiting_integration", spec.unavailable_reason
        elif auth.resolved() is None:
            health, detail = ("unconfigured",
                              f"auth reference '{auth.ref}' is not set here")
        elif source["consecutive_failures"] >= 3:
            health, detail = ("unreachable",
                              f"{source['consecutive_failures']} consecutive "
                              f"failed syncs: {source['last_error'][:120]}")
        elif source["consecutive_failures"] > 0:
            health, detail = ("degraded",
                              f"last sync failed: {source['last_error'][:120]}")
        elif source["sync_state"] == "synced":
            health, detail = "healthy", ""
        else:
            health, detail = "unknown", "never synchronized"

        updated = self._store.update(
            "sources", "source_id", source_id,
            {"health": health, "health_detail": detail,
             "health_checked_at": now_iso()})
        return updated

    def check_all(self) -> dict[str, int]:
        counts: dict[str, int] = {}
        for source in self.sources():
            checked = self.check_health(source["source_id"])
            counts[checked["health"]] = counts.get(checked["health"], 0) + 1
        return counts

    # ----------------------------------------------------------- sync state
    def mark_syncing(self, source_id: str) -> dict:
        return self._store.update("sources", "source_id", source_id,
                                  {"sync_state": "syncing"})

    def mark_synced(self, source_id: str, records: int, version: int,
                    mode: str) -> dict:
        source = self._require(source_id)
        fields = {
            "sync_state": "synced", "sync_version": version,
            "last_synced_at": now_iso(), "last_sync_status": mode,
            "last_error": "", "consecutive_failures": 0,
            "records_total": records, "health": "healthy", "health_detail": "",
            "next_sync_at": self.next_sync_at(source),
        }
        if not source["first_synced_at"]:
            fields["first_synced_at"] = now_iso()
        return self._store.update("sources", "source_id", source_id, fields)

    def mark_failed(self, source_id: str, error: str,
                    retrying: bool = False) -> dict:
        source = self._require(source_id)
        failures = source["consecutive_failures"] + 1
        return self._store.update("sources", "source_id", source_id, {
            "sync_state": "retrying" if retrying else "failed",
            "last_sync_status": "failed", "last_error": error[:300],
            "consecutive_failures": failures,
            "health": "unreachable" if failures >= 3 else "degraded",
            "health_detail": error[:200],
            "next_sync_at": self.next_sync_at(source),
        })

    def next_sync_at(self, source: dict) -> str:
        """When this source is next due. Manual sources are never due; a
        failing source backs off so a broken system is not hammered."""
        seconds = CADENCES[source["cadence"]]
        if seconds < 0:
            return ""
        failures = source.get("consecutive_failures", 0)
        if failures:
            seconds = max(seconds, 60) * min(2 ** failures, 8)
        return (datetime.now(timezone.utc)
                + timedelta(seconds=seconds)).isoformat()

    def due(self) -> list[dict]:
        """Every enabled, native source whose cadence says it is time."""
        now = datetime.now(timezone.utc)
        out = []
        for source in self.sources(enabled_only=True):
            if source["capability"] != "native":
                continue
            if CADENCES[source["cadence"]] < 0:
                continue
            if source["sync_state"] == "syncing":
                continue
            due_at = source.get("next_sync_at")
            if not due_at or datetime.fromisoformat(due_at) <= now:
                out.append(source)
        return out

    # ----------------------------------------------------------------- read
    def sources(self, kind: str = "", enabled_only: bool = False,
                health: str = "") -> list[dict]:
        items = self._store.read("sources")
        if kind:
            items = [s for s in items if s["kind"] == kind]
        if enabled_only:
            items = [s for s in items if s["enabled"]]
        if health:
            items = [s for s in items if s["health"] == health]
        return items

    def get(self, source_id: str) -> dict | None:
        return self._store.get("sources", "source_id", source_id)

    def by_name(self, name: str) -> dict | None:
        return next((s for s in self.sources() if s["name"] == name), None)

    def status(self) -> dict:
        """Connected Systems: what is attached, healthy, and how fresh."""
        sources = self.sources()
        by_health: dict[str, int] = {}
        by_kind: dict[str, int] = {}
        for s in sources:
            by_health[s["health"]] = by_health.get(s["health"], 0) + 1
            by_kind[s["kind"]] = by_kind.get(s["kind"], 0) + 1
        synced = [s["last_synced_at"] for s in sources if s["last_synced_at"]]
        return {
            "total": len(sources),
            "connected": sum(1 for s in sources if s["health"] == "healthy"),
            "needs_attention": sum(1 for s in sources
                                   if s["health"] in ("degraded", "unreachable",
                                                      "unconfigured")),
            "awaiting_integration": sum(1 for s in sources
                                        if s["capability"] == "interface"),
            "by_health": by_health, "by_kind": by_kind,
            "last_sync_at": max(synced) if synced else "",
            "records_total": sum(s["records_total"] for s in sources),
            "catalogue": self.kinds(),
        }

    def _require(self, source_id: str) -> dict:
        source = self.get(source_id)
        if source is None:
            raise KeyError(f"Unknown source: {source_id}")
        return source

    def _announce(self, kind: str, source: dict) -> None:
        if self._bus is None:
            return
        try:
            self._bus.publish(kind, {"source_id": source["source_id"],
                                     "name": source["name"],
                                     "source_kind": source["kind"]},
                              project_id=source.get("project_id", ""),
                              source="source_registry")
        except Exception:  # noqa: BLE001 — announcing never fails registration
            logger.exception("Source event publication failed")


def _looks_like_a_secret(location: str) -> bool:
    """Catch the obvious mistake of pasting a credentialed connection string
    into ``location``, where it would be persisted and served over the API."""
    text = (location or "").lower()
    return "://" in text and "@" in text.split("://", 1)[1].split("/", 1)[0]

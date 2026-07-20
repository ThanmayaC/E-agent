"""Enterprise Connector interface — the contract every data source implements.

A *source connector* owns one configured enterprise system for its whole
life: it initializes, connects, proves it can connect, discovers what the
system holds, synchronizes fully and then incrementally, reports its own
health, and disconnects. It is the only place that knows anything
provider-specific.

This is deliberately a different layer from ``app/intelligence/connectors``,
which holds *format* connectors — one file in, tabular extracts out, no
lifecycle, no state. Source connectors reuse those format connectors for
content extraction rather than re-implementing parsing:

    EnterpriseConnector (this layer)   a configured system, over time
      └── uses ──▶ DataConnector       one file/descriptor, right now

Every connector produces the same thing regardless of origin: a stream of
``KnowledgePackage`` objects (``app.connectors.package``). Downstream —
Document Intelligence, the embedding pipeline, the Enterprise Brain — never
learns which connector produced a package, which is what makes adding the
tenth connector cost nothing anywhere else.

Failure is a first-class outcome, not an exception that escapes: a connector
raises the typed errors below, and the Enterprise Sync Service records,
retries, and degrades the source. A broken system must never stop the others.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable, Iterator

from app.connectors.package import KnowledgePackage

# What a connector reports it can actually do. Declared per connector class so
# the API, the scheduler, and the admin UI can reason about a connector
# without instantiating or connecting to anything.
CAPABILITIES = (
    "discover",           # can enumerate what the source holds
    "incremental",        # can sync only what changed since a cursor
    "content",            # can fetch raw content, not just metadata
    "deletions",          # can detect records/files that disappeared
    "test_connection",    # can prove connectivity without a full sync
)

HEALTH_STATES = ("unknown", "healthy", "degraded", "unreachable",
                 "unconfigured", "disconnected")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# --------------------------------------------------------------- exceptions
class ConnectorError(RuntimeError):
    """Base for every connector failure. Carries whether a retry is worth it.

    Transience is the connector's judgement, not the service's: only the
    connector knows that a dropped socket is worth another attempt while a
    missing credential is not.
    """

    transient: bool = False

    def __init__(self, message: str, *, transient: bool | None = None):
        super().__init__(message)
        if transient is not None:
            self.transient = transient


class ConnectorNotConfigured(ConnectorError):
    """Configuration or credentials are missing — retrying cannot help."""
    transient = False


class ConnectorUnavailable(ConnectorError):
    """The connector cannot run in this deployment (missing dependency)."""
    transient = False


class ConnectionFailed(ConnectorError):
    """The source could not be reached. Worth another attempt."""
    transient = True


class SyncFailed(ConnectorError):
    """The source was reached but the read failed."""
    transient = True


# ------------------------------------------------------------------ config
@dataclass
class ConnectorConfig:
    """Everything needed to run one connector — and nothing secret.

    ``auth_ref`` names an environment variable holding the credential; the
    value is resolved in memory at connect time and never stored, logged, or
    returned by an API. This mirrors the Data Source Registry's contract
    (``app/sync/registry.py``) rather than inventing a second one.
    """
    connector_id: str
    name: str
    kind: str                                  # registry key: folder, excel, ...
    location: str = ""                         # path, DSN host, base URL — never a secret
    auth_kind: str = "none"                    # none | env
    auth_ref: str = ""
    cadence: str = "hourly"                    # matches app.sync.registry.CADENCES
    enabled: bool = True
    options: dict[str, Any] = field(default_factory=dict)
    description: str = ""
    project_id: str = ""

    def resolved_secret(self) -> str | None:
        """The credential, in memory only. ``None`` when not configured."""
        import os
        if self.auth_kind == "none":
            return ""
        if self.auth_kind == "env":
            return os.environ.get(self.auth_ref) or None
        return None

    def require_secret(self) -> str:
        value = self.resolved_secret()
        if value is None:
            raise ConnectorNotConfigured(
                f"Connector '{self.name}' needs {self.auth_kind} reference "
                f"'{self.auth_ref}', which is not set in this environment")
        return value

    def describe(self) -> dict:
        """Safe by construction: says whether the secret resolves, never what
        it is."""
        return {"connector_id": self.connector_id, "name": self.name,
                "kind": self.kind, "location": self.location,
                "auth": {"kind": self.auth_kind, "ref": self.auth_ref,
                         "configured": self.resolved_secret() is not None},
                "cadence": self.cadence, "enabled": self.enabled,
                "options": self.options, "description": self.description,
                "project_id": self.project_id}

    @classmethod
    def from_dict(cls, data: dict) -> ConnectorConfig:
        auth = data.get("auth") or {}
        return cls(
            connector_id=data["connector_id"], name=data["name"],
            kind=data["kind"], location=data.get("location", ""),
            auth_kind=auth.get("kind", data.get("auth_kind", "none")),
            auth_ref=auth.get("ref", data.get("auth_ref", "")),
            cadence=data.get("cadence", "hourly"),
            enabled=bool(data.get("enabled", True)),
            options=data.get("options") or {},
            description=data.get("description", ""),
            project_id=data.get("project_id", ""))


# ------------------------------------------------------------- result types
@dataclass
class ConnectorHealth:
    """A connector's own assessment of itself."""
    state: str = "unknown"          # HEALTH_STATES
    detail: str = ""
    checked_at: str = field(default_factory=now_iso)
    latency_ms: int = 0

    def describe(self) -> dict:
        return {"state": self.state, "detail": self.detail,
                "checked_at": self.checked_at, "latency_ms": self.latency_ms}


@dataclass
class ConnectionTest:
    """The outcome of ``test_connection()`` — never raises, always answers."""
    ok: bool
    detail: str = ""
    latency_ms: int = 0
    tested_at: str = field(default_factory=now_iso)

    def describe(self) -> dict:
        return {"ok": self.ok, "detail": self.detail,
                "latency_ms": self.latency_ms, "tested_at": self.tested_at}


@dataclass
class DiscoveredItem:
    """One thing the source holds: a file, a sheet, a table, an endpoint."""
    item_id: str
    name: str
    item_type: str                  # file | sheet | table | endpoint | folder
    size: int = 0
    modified_at: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    def describe(self) -> dict:
        return {"item_id": self.item_id, "name": self.name,
                "item_type": self.item_type, "size": self.size,
                "modified_at": self.modified_at, "metadata": self.metadata}


@dataclass
class Discovery:
    """What one ``discover()`` found. Cheap by contract: metadata only, no
    content — an administrator runs this interactively while registering a
    source and must not wait for a full read."""
    connector_id: str
    items: list[DiscoveredItem] = field(default_factory=list)
    truncated: bool = False
    detail: str = ""

    def describe(self) -> dict:
        return {"connector_id": self.connector_id,
                "items": [i.describe() for i in self.items],
                "count": len(self.items), "truncated": self.truncated,
                "detail": self.detail}


@dataclass
class SyncCursor:
    """Where incremental synchronization got to.

    Two mechanisms, because enterprise sources split cleanly in two:

        ``fingerprints``  content hash per item key — folders, workbooks, CSV
                          repositories. Detects updates AND deletions, needs
                          no cooperation from the source.
        ``watermark``     a monotonic column value (updated_at, id) — large
                          databases, where re-reading everything to hash it
                          would defeat the point.

    A connector uses whichever its source supports; both are persisted by the
    service, so a connector is stateless between runs and a crashed sync
    resumes rather than restarts.
    """
    version: int = 0
    watermark: str = ""
    fingerprints: dict[str, str] = field(default_factory=dict)
    last_synced_at: str = ""
    extra: dict[str, Any] = field(default_factory=dict)

    def describe(self) -> dict:
        return {"version": self.version, "watermark": self.watermark,
                "tracked_items": len(self.fingerprints),
                "last_synced_at": self.last_synced_at, "extra": self.extra}

    @classmethod
    def from_dict(cls, data: dict | None) -> SyncCursor:
        data = data or {}
        return cls(version=int(data.get("version", 0)),
                   watermark=str(data.get("watermark", "")),
                   fingerprints=dict(data.get("fingerprints") or {}),
                   last_synced_at=str(data.get("last_synced_at", "")),
                   extra=dict(data.get("extra") or {}))

    def to_dict(self) -> dict:
        return {"version": self.version, "watermark": self.watermark,
                "fingerprints": self.fingerprints,
                "last_synced_at": self.last_synced_at, "extra": self.extra}


@dataclass
class SyncOutcome:
    """What one connector run produced.

    ``packages`` are the normalized knowledge the run yielded; ``removed`` are
    the keys that vanished from the source, so downstream can archive them.
    The cursor is returned rather than written by the connector — persistence
    belongs to the service, so a connector stays a pure reader.
    """
    connector_id: str
    mode: str = "full"                  # full | incremental
    packages: list[KnowledgePackage] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)
    unchanged: int = 0
    cursor: SyncCursor = field(default_factory=SyncCursor)
    truncated: bool = False
    warnings: list[str] = field(default_factory=list)

    @property
    def changed(self) -> int:
        return len(self.packages) + len(self.removed)

    def describe(self) -> dict:
        return {"connector_id": self.connector_id, "mode": self.mode,
                "packages": len(self.packages), "removed": len(self.removed),
                "unchanged": self.unchanged, "changed": self.changed,
                "truncated": self.truncated, "warnings": self.warnings,
                "cursor": self.cursor.describe()}


# --------------------------------------------------------------- interface
class EnterpriseConnector(ABC):
    """Base class for every enterprise data source connector.

    Lifecycle, in the order the Enterprise Sync Service calls it::

        initialize()        validate configuration — no I/O, never fails on
                            an unreachable system, only on a nonsensical one
        connect()           establish/prepare the connection
        test_connection()   prove it works (also called on its own from Admin)
        discover()          enumerate what is there (metadata only)
        sync()              full read           ─┐ both yield SyncOutcome
        incremental_sync()  delta since cursor  ─┘
        fetch_metadata()    metadata for one item
        fetch_content()     raw content for one item
        health()            self-assessment, cheap enough to run every tick
        disconnect()        release resources

    Subclasses must implement the abstract members; everything else has a
    working default so a new connector is small. ``incremental_sync`` defaults
    to a full ``sync``, which is always *correct* — a connector that cannot do
    better is slower, not wrong.
    """

    kind: str = "connector"
    title: str = "Connector"
    description: str = ""
    capabilities: tuple[str, ...] = ("discover", "test_connection")
    # Extensions/record families this connector produces, for the API catalogue.
    produces: str = "documents"     # documents | tabular | communications

    def __init__(self, config: ConnectorConfig):
        self.config = config
        self._connected = False
        self._health = ConnectorHealth()

    # ------------------------------------------------------------ identity
    @property
    def connector_id(self) -> str:
        return self.config.connector_id

    @property
    def name(self) -> str:
        return self.config.name

    @property
    def connected(self) -> bool:
        return self._connected

    def supports(self, capability: str) -> bool:
        return capability in self.capabilities

    @classmethod
    def describe_kind(cls) -> dict:
        """Catalogue entry — what this connector is, before one exists."""
        return {"kind": cls.kind, "title": cls.title,
                "description": cls.description,
                "capabilities": list(cls.capabilities),
                "produces": cls.produces}

    # ----------------------------------------------------------- lifecycle
    def initialize(self) -> None:
        """Validate configuration. No I/O — a source that is merely
        unreachable must still initialize, so it can be registered, shown in
        Admin, and retried later."""
        if not self.config.name:
            raise ConnectorNotConfigured("a connector needs a name")

    def connect(self) -> None:
        """Prepare the connection. Idempotent: calling it twice is a no-op."""
        self._connected = True

    def disconnect(self) -> None:
        """Release whatever ``connect`` acquired. Never raises."""
        self._connected = False

    def test_connection(self) -> ConnectionTest:
        """Prove connectivity without a full sync. Never raises — Admin's
        "Test connection" button always gets an answer, not a 500."""
        import time
        started = time.monotonic()
        try:
            self.initialize()
            self.connect()
            detail = self._probe()
            return ConnectionTest(
                ok=True, detail=detail,
                latency_ms=int((time.monotonic() - started) * 1000))
        except ConnectorError as exc:
            return ConnectionTest(
                ok=False, detail=str(exc),
                latency_ms=int((time.monotonic() - started) * 1000))
        except Exception as exc:  # noqa: BLE001 — a probe never escapes as a crash
            return ConnectionTest(
                ok=False, detail=f"{type(exc).__name__}: {exc}"[:300],
                latency_ms=int((time.monotonic() - started) * 1000))

    def _probe(self) -> str:
        """Connector-specific reachability check behind ``test_connection``.
        Returns a human-readable confirmation; raises ``ConnectorError``."""
        return "connector initialized"

    def health(self) -> ConnectorHealth:
        """Self-assessment. The default derives health from configuration and
        connection state; connectors with a cheap liveness signal override."""
        if self.config.resolved_secret() is None:
            self._health = ConnectorHealth(
                state="unconfigured",
                detail=f"auth reference '{self.config.auth_ref}' is not set here")
        elif self._connected:
            self._health = ConnectorHealth(state="healthy")
        else:
            self._health = ConnectorHealth(state="disconnected",
                                           detail="not connected")
        return self._health

    # ----------------------------------------------------------- discovery
    @abstractmethod
    def discover(self) -> Discovery:
        """Enumerate what the source holds. Metadata only, bounded, cheap."""

    @abstractmethod
    def fetch_metadata(self, item_id: str) -> dict[str, Any]:
        """Structured metadata for one discovered item."""

    def fetch_content(self, item_id: str) -> bytes:
        """Raw bytes for one item. Connectors whose records are rows rather
        than files do not implement this and say so."""
        raise ConnectorUnavailable(
            f"{self.title} does not expose raw content per item")

    # --------------------------------------------------------------- sync
    @abstractmethod
    def sync(self, cursor: SyncCursor | None = None) -> SyncOutcome:
        """Full read: every item becomes a KnowledgePackage."""

    def incremental_sync(self, cursor: SyncCursor) -> SyncOutcome:
        """Delta since ``cursor``. The default is a full sync, which is
        correct for every source and optimal for none — connectors that can
        do better override this and declare the ``incremental`` capability."""
        outcome = self.sync(cursor)
        outcome.mode = "full"
        return outcome

    # ------------------------------------------------------------ helpers
    def package_defaults(self) -> dict[str, Any]:
        """Fields every package from this connector carries."""
        return {"source_id": self.connector_id,
                "source_name": self.config.name,
                "connector_type": self.kind,
                "project_id": self.config.project_id}

    @staticmethod
    def _diff_fingerprints(previous: dict[str, str], current: dict[str, str]
                           ) -> tuple[list[str], list[str]]:
        """(changed_or_new_keys, removed_keys) between two fingerprint maps."""
        changed = [k for k, digest in current.items()
                   if previous.get(k) != digest]
        removed = [k for k in previous if k not in current]
        return changed, removed

    def __repr__(self) -> str:  # pragma: no cover — debugging aid
        return (f"<{type(self).__name__} {self.config.name!r} "
                f"kind={self.kind} connected={self._connected}>")


def iter_packages(outcomes: Iterable[SyncOutcome]) -> Iterator[KnowledgePackage]:
    """Flatten several runs' packages — the ingestion queue's input."""
    for outcome in outcomes:
        yield from outcome.packages

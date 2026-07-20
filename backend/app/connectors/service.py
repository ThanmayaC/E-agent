"""Enterprise Sync Service — one engine that drives every connector.

Responsibilities, all of them centralized here so no connector implements any
of them:

    configuration   register, edit, enable/disable, delete data sources
    scheduling      decide which connectors are *due* — the Enterprise
                    Scheduler runs this service; this service does not run a
                    clock. There is exactly one heartbeat in the platform.
    change detection ask each connector for its delta (full or incremental)
    ingestion       queue every KnowledgePackage into the pipeline
    retries         attempt again on transient failure, back off on repeat
    history         every run, its outcome, and every failure, kept readable
    events          announce on the enterprise bus; nobody is called directly

A connector is a reader. This service is everything around the reader, which
is why a new connector costs one file.

Failure containment is the design rule: ``sync_one`` never raises. An
unreachable database degrades itself, records why, and the other twelve
sources synchronize normally on the same tick.
"""
from __future__ import annotations

import threading
import time
from typing import Any, Callable

from app.connectors.base import (
    ConnectorConfig, ConnectorError, EnterpriseConnector, SyncCursor,
    SyncOutcome,
)
from app.connectors.package import KnowledgePackage
from app.connectors.registry import ConnectorRegistry
from app.connectors.store import ConnectorStore, new_id, now_iso
from app.core.logging import get_logger
from app.sync.registry import CADENCES

logger = get_logger(__name__)

MAX_RUNS = 300
MAX_FAILURES = 200
MAX_PACKAGE_RECORDS = 2_000
DEFAULT_ATTEMPTS = 2
BACKOFF_SECONDS = 3.0

# An ingestion handler consumes one connector's packages and reports what it
# did. The service does not know or care what happens inside — that is the
# Document Intelligence pipeline's business.
IngestionHandler = Callable[[dict, list[KnowledgePackage], list[str]],
                            dict[str, Any]]


class EnterpriseSyncService:
    """The centralized synchronization engine for the connector framework."""

    def __init__(self, store: ConnectorStore, registry: ConnectorRegistry,
                 ingest: IngestionHandler | None = None, bus=None,
                 max_attempts: int = DEFAULT_ATTEMPTS):
        self._store = store
        self._registry = registry
        self._ingest = ingest
        self._bus = bus
        self._max_attempts = max_attempts
        self._lock = threading.RLock()
        # Live connector instances, one per configured source. Cached because
        # connect() may be expensive (a database pool); rebuilt when the
        # configuration changes.
        self._instances: dict[str, EnterpriseConnector] = {}

    def attach_bus(self, bus) -> None:
        """Announce on the enterprise event bus, which the runtime owns."""
        self._bus = bus

    def set_ingestion_handler(self, handler: IngestionHandler) -> None:
        self._ingest = handler

    # ------------------------------------------------------- configuration
    def register(self, name: str, kind: str, location: str = "",
                 auth: dict | None = None, cadence: str = "hourly",
                 description: str = "", options: dict | None = None,
                 project_id: str = "", enabled: bool = True) -> dict:
        """Configure one enterprise data source. Validated by instantiating
        the connector — a misconfiguration is refused at registration, not
        discovered at 03:00."""
        if not self._registry.has(kind):
            self._registry.get(kind)  # raises with the reason (planned/unavailable)
        if cadence not in CADENCES:
            raise ValueError(f"Unknown refresh cadence: {cadence}")
        auth = auth or {}
        if any(k in auth for k in ("value", "secret", "password", "token",
                                   "url", "connection_string")):
            raise ValueError(
                "auth must not carry a secret value — pass a reference "
                "({'kind': 'env', 'ref': 'VAR_NAME'}) instead")
        if _looks_like_a_secret(location):
            raise ValueError(
                "location looks like it contains credentials — put the secret "
                "in an environment variable and reference it via auth")

        with self._lock:
            if any(c["name"] == name for c in self._store.read("connectors")):
                raise ValueError(f"A data source named '{name}' already exists")
            config = ConnectorConfig(
                connector_id=new_id("conn"), name=name[:120], kind=kind,
                location=location[:500], auth_kind=auth.get("kind", "none"),
                auth_ref=auth.get("ref", ""), cadence=cadence,
                enabled=enabled, options=options or {},
                description=description[:300], project_id=project_id)
            connector = self._registry.create(config)  # validates; may raise
            record = {**config.describe(), **_initial_state(),
                      "title": connector.title,
                      "capabilities": list(connector.capabilities),
                      "produces": connector.produces,
                      "created_at": now_iso(), "updated_at": now_iso()}
            self._store.append("connectors", record)
            self._instances[config.connector_id] = connector

        logger.info("Registered data source '%s' (%s)", name, kind)
        self._announce("ConnectorRegistered", record)
        return record

    def update(self, connector_id: str, **fields) -> dict:
        """Edit a source. Changing anything the connector reads rebuilds the
        instance, so a corrected path takes effect on the next tick."""
        record = self._require(connector_id)
        allowed = {"name", "location", "cadence", "enabled", "options",
                   "description", "auth", "project_id"}
        unknown = set(fields) - allowed
        if unknown:
            raise ValueError(f"Cannot update: {', '.join(sorted(unknown))}")
        if "cadence" in fields and fields["cadence"] not in CADENCES:
            raise ValueError(f"Unknown refresh cadence: {fields['cadence']}")
        if "location" in fields and _looks_like_a_secret(fields["location"]):
            raise ValueError("location looks like it contains credentials")

        updated = self._store.update("connectors", "connector_id",
                                     connector_id, fields)
        self._drop_instance(connector_id)
        return updated or record

    def set_enabled(self, connector_id: str, enabled: bool) -> dict:
        return self.update(connector_id, enabled=enabled)

    def remove(self, connector_id: str) -> bool:
        """Delete a source and everything the platform kept about its sync
        state. Ingested knowledge is not deleted — that is a separate,
        audited decision, not a side effect of unplugging a source."""
        with self._lock:
            if not self._store.delete("connectors", "connector_id", connector_id):
                return False
            self._store.drop_cursor(connector_id)
            self._drop_instance(connector_id)
        return True

    # ------------------------------------------------------------ instances
    def connector(self, connector_id: str) -> EnterpriseConnector:
        """The live connector for a source, built on first use."""
        with self._lock:
            existing = self._instances.get(connector_id)
            if existing is not None:
                return existing
            record = self._require(connector_id)
            connector = self._registry.create(ConnectorConfig.from_dict(record))
            self._instances[connector_id] = connector
            return connector

    def _drop_instance(self, connector_id: str) -> None:
        connector = self._instances.pop(connector_id, None)
        if connector is not None:
            try:
                connector.disconnect()
            except Exception:  # noqa: BLE001 — teardown never raises
                logger.warning("Disconnecting %s failed", connector_id)

    # --------------------------------------------------------- admin actions
    def test_connection(self, connector_id: str) -> dict:
        """Admin's "Test connection". Always answers, never 500s."""
        record = self._require(connector_id)
        try:
            result = self.connector(connector_id).test_connection()
        except Exception as exc:  # noqa: BLE001 — even construction can fail
            result_dict = {"ok": False, "detail": f"{type(exc).__name__}: {exc}"[:300],
                           "latency_ms": 0, "tested_at": now_iso()}
        else:
            result_dict = result.describe()
        self._store.update("connectors", "connector_id", connector_id, {
            "last_test": result_dict,
            "health": "healthy" if result_dict["ok"] else "unreachable",
            "health_detail": "" if result_dict["ok"] else result_dict["detail"],
            "health_checked_at": now_iso()})
        return {"connector_id": connector_id, "name": record["name"],
                **result_dict}

    def discover(self, connector_id: str) -> dict:
        """What is in there — run from Admin while configuring a source."""
        self._require(connector_id)
        try:
            return self.connector(connector_id).discover().describe()
        except ConnectorError as exc:
            return {"connector_id": connector_id, "items": [], "count": 0,
                    "truncated": False, "detail": str(exc), "error": str(exc)}

    def check_health(self, connector_id: str) -> dict:
        record = self._require(connector_id)
        try:
            health = self.connector(connector_id).health().describe()
        except Exception as exc:  # noqa: BLE001 — health always answers
            health = {"state": "unreachable",
                      "detail": f"{type(exc).__name__}: {exc}"[:300],
                      "checked_at": now_iso(), "latency_ms": 0}
        previous = record.get("health", "unknown")
        self._store.update("connectors", "connector_id", connector_id, {
            "health": health["state"], "health_detail": health["detail"],
            "health_checked_at": health["checked_at"]})
        if health["state"] != previous:
            self._announce("ConnectorHealthChanged",
                           {**record, "health": health["state"]},
                           extra={"previous": previous,
                                  "detail": health["detail"]})
        return health

    def check_all(self) -> dict[str, int]:
        """The scheduler's health job: every source, every tick."""
        counts: dict[str, int] = {}
        for record in self.sources():
            state = self.check_health(record["connector_id"])["state"]
            counts[state] = counts.get(state, 0) + 1
        return counts

    # ------------------------------------------------------------ scheduling
    def due(self) -> list[dict]:
        """Enabled sources whose cadence says it is time. Manual sources are
        never due; a failing source is backed off so a broken system is not
        hammered every tick."""
        from datetime import datetime, timezone
        now = datetime.now(timezone.utc)
        out = []
        for record in self.sources(enabled_only=True):
            if CADENCES[record["cadence"]] < 0:
                continue
            if record["sync_state"] == "syncing":
                continue
            next_at = record.get("next_sync_at")
            if not next_at or datetime.fromisoformat(next_at) <= now:
                out.append(record)
        return out

    def sync_due(self) -> dict[str, Any]:
        """The scheduler's synchronization job."""
        return self._summarize([self.sync_one(r["connector_id"])
                                for r in self.due()], trigger="scheduled")

    def sync_all(self, full: bool = False) -> dict[str, Any]:
        return self._summarize(
            [self.sync_one(r["connector_id"], full=full)
             for r in self.sources(enabled_only=True)], trigger="manual")

    # ------------------------------------------------------------------ sync
    def sync_one(self, connector_id: str, full: bool = False,
                 trigger: str = "scheduled") -> dict:
        """Synchronize one source end to end. Never raises.

        full read or delta → packages → ingestion → cursor → history → events
        """
        record = self._require(connector_id)
        run = {"run_id": new_id("crun"), "connector_id": connector_id,
               "connector": record["name"], "kind": record["kind"],
               "trigger": trigger, "mode": "full", "status": "failed",
               "attempts": 0, "packages": 0, "removed": 0, "unchanged": 0,
               "ingested": {}, "warnings": [], "error": "",
               "started_at": now_iso(), "finished_at": "", "duration_ms": 0}

        if not record["enabled"]:
            return self._finish_skipped(run, connector_id, "source is disabled")

        started = time.monotonic()
        self._store.update("connectors", "connector_id", connector_id,
                           {"sync_state": "syncing"})
        self._announce("ConnectorSyncStarted", record, extra={"trigger": trigger})

        cursor = SyncCursor.from_dict(self._store.cursor(connector_id))
        outcome, error = None, ""
        for attempt in range(1, self._max_attempts + 1):
            run["attempts"] = attempt
            try:
                outcome = self._run_connector(connector_id, cursor, full)
                error = ""
                break
            except ConnectorError as exc:
                error = str(exc)[:300]
                if not exc.transient or attempt >= self._max_attempts:
                    break
                logger.warning("Sync of %s failed (attempt %d/%d): %s",
                               record["name"], attempt, self._max_attempts, error)
                time.sleep(BACKOFF_SECONDS * attempt)
            except Exception as exc:  # noqa: BLE001 — unknown failures are transient
                error = f"{type(exc).__name__}: {exc}"[:300]
                logger.exception("Sync of %s failed (attempt %d/%d)",
                                 record["name"], attempt, self._max_attempts)
                if attempt >= self._max_attempts:
                    break
                time.sleep(BACKOFF_SECONDS * attempt)

        run["duration_ms"] = int((time.monotonic() - started) * 1000)
        run["finished_at"] = now_iso()

        if outcome is None:
            return self._finish_failed(run, record, error)
        return self._finish_completed(run, record, outcome)

    def _run_connector(self, connector_id: str, cursor: SyncCursor,
                       full: bool) -> SyncOutcome:
        connector = self.connector(connector_id)
        connector.connect()
        use_incremental = (not full and cursor.version > 0
                           and connector.supports("incremental"))
        return (connector.incremental_sync(cursor) if use_incremental
                else connector.sync(cursor))

    # ------------------------------------------------------------ finishing
    def _finish_completed(self, run: dict, record: dict,
                          outcome: SyncOutcome) -> dict:
        connector_id = record["connector_id"]
        run.update({"status": "completed", "mode": outcome.mode,
                    "packages": len(outcome.packages),
                    "removed": len(outcome.removed),
                    "unchanged": outcome.unchanged,
                    "warnings": outcome.warnings[:20],
                    "version": outcome.cursor.version})

        # Ingestion is downstream of the read and must not lose the sync: a
        # pipeline failure is recorded on the run, and the cursor still
        # advances only if ingestion succeeded, so nothing is silently skipped.
        ingested, ingest_error = self._queue_ingestion(record, outcome)
        run["ingested"] = ingested
        if ingest_error:
            run["status"] = "degraded"
            run["error"] = ingest_error

        if not ingest_error:
            self._store.save_cursor(connector_id, outcome.cursor.to_dict())
        self._record_packages(record, outcome)

        self._store.update("connectors", "connector_id", connector_id, {
            "sync_state": "synced", "sync_version": outcome.cursor.version,
            "last_synced_at": run["finished_at"], "last_sync_status": run["status"],
            "last_error": run.get("error", ""), "consecutive_failures": 0,
            "items_total": len(outcome.cursor.fingerprints),
            "health": "healthy" if not ingest_error else "degraded",
            "health_detail": run.get("error", ""),
            "first_synced_at": record.get("first_synced_at") or run["finished_at"],
            "next_sync_at": self._next_sync_at(record["cadence"], 0)})

        self._append("runs", run, MAX_RUNS)
        self._announce("ConnectorSyncCompleted", record, extra={
            "mode": outcome.mode, "packages": len(outcome.packages),
            "removed": len(outcome.removed), "version": outcome.cursor.version})
        if outcome.packages or outcome.removed:
            self._announce("KnowledgePackagesProduced", record, extra={
                "packages": len(outcome.packages),
                "removed": len(outcome.removed), "ingested": ingested})
        return run

    def _finish_failed(self, run: dict, record: dict, error: str) -> dict:
        connector_id = record["connector_id"]
        failures = int(record.get("consecutive_failures", 0)) + 1
        run.update({"status": "failed", "error": error})
        self._store.update("connectors", "connector_id", connector_id, {
            "sync_state": "failed", "last_sync_status": "failed",
            "last_error": error, "consecutive_failures": failures,
            "health": "unreachable" if failures >= 3 else "degraded",
            "health_detail": error[:200],
            "next_sync_at": self._next_sync_at(record["cadence"], failures)})
        self._append("runs", run, MAX_RUNS)
        self._append("failures", {
            "failure_id": new_id("fail"), "connector_id": connector_id,
            "connector": record["name"], "error": error,
            "attempts": run["attempts"], "consecutive_failures": failures,
            "at": run["finished_at"]}, MAX_FAILURES)
        self._announce("ConnectorSyncFailed", record,
                       extra={"error": error, "attempts": run["attempts"],
                              "consecutive_failures": failures})
        return run

    def _finish_skipped(self, run: dict, connector_id: str,
                        reason: str) -> dict:
        run.update({"status": "skipped", "error": reason,
                    "finished_at": now_iso()})
        self._store.update("connectors", "connector_id", connector_id,
                           {"sync_state": "skipped"})
        self._append("runs", run, MAX_RUNS)
        return run

    # ------------------------------------------------------------ ingestion
    def _queue_ingestion(self, record: dict,
                         outcome: SyncOutcome) -> tuple[dict, str]:
        """Hand the packages to the ingestion pipeline.

        Returns (counts, error). A pipeline that is not wired is not an
        error — the connector framework is useful on its own, and a
        deployment with Document Intelligence disabled still gets sync,
        health, and the package catalogue.
        """
        if self._ingest is None:
            return {"queued": len(outcome.packages),
                    "note": "no ingestion pipeline configured"}, ""
        if not outcome.packages and not outcome.removed:
            return {}, ""
        try:
            return self._ingest(record, outcome.packages, outcome.removed), ""
        except Exception as exc:  # noqa: BLE001 — ingestion never kills the sync
            logger.exception("Ingestion failed for source %s", record["name"])
            return {}, f"ingestion failed: {type(exc).__name__}: {exc}"[:300]

    def _record_packages(self, record: dict, outcome: SyncOutcome) -> None:
        """The package catalogue: what this source has produced, without the
        content. Bounded — it is a window into the pipeline, not an archive."""
        if not outcome.packages:
            return
        try:
            with self._store.mutate("packages") as packages:
                packages.extend(p.describe() for p in outcome.packages)
                del packages[:-MAX_PACKAGE_RECORDS]
        except Exception:  # noqa: BLE001 — the catalogue is observability
            logger.exception("Package catalogue persistence failed")

    # --------------------------------------------------------------- reads
    def sources(self, kind: str = "", enabled_only: bool = False,
                health: str = "") -> list[dict]:
        items = self._store.read("connectors")
        if kind:
            items = [c for c in items if c["kind"] == kind]
        if enabled_only:
            items = [c for c in items if c["enabled"]]
        if health:
            items = [c for c in items if c.get("health") == health]
        return items

    def get(self, connector_id: str) -> dict | None:
        return self._store.get("connectors", "connector_id", connector_id)

    def runs(self, connector_id: str = "", limit: int = 50) -> list[dict]:
        items = self._store.read("runs")
        if connector_id:
            items = [r for r in items if r["connector_id"] == connector_id]
        return list(reversed(items))[:limit]  # newest first

    def failures(self, connector_id: str = "", limit: int = 50) -> list[dict]:
        items = self._store.read("failures")
        if connector_id:
            items = [f for f in items if f["connector_id"] == connector_id]
        return list(reversed(items))[:limit]

    def packages(self, connector_id: str = "", limit: int = 100) -> list[dict]:
        items = self._store.read("packages")
        if connector_id:
            items = [p for p in items if p["source_id"] == connector_id]
        return list(reversed(items))[:limit]

    def status(self) -> dict:
        """Enterprise Data Sources: what is connected, healthy, and fresh."""
        sources = self.sources()
        runs = self._store.read("runs")
        by_health: dict[str, int] = {}
        by_kind: dict[str, int] = {}
        for s in sources:
            by_health[s.get("health", "unknown")] = \
                by_health.get(s.get("health", "unknown"), 0) + 1
            by_kind[s["kind"]] = by_kind.get(s["kind"], 0) + 1
        synced = [s["last_synced_at"] for s in sources if s["last_synced_at"]]
        return {
            "total": len(sources),
            "enabled": sum(1 for s in sources if s["enabled"]),
            "healthy": sum(1 for s in sources if s.get("health") == "healthy"),
            "needs_attention": sum(
                1 for s in sources
                if s.get("health") in ("degraded", "unreachable", "unconfigured")),
            "by_health": by_health, "by_kind": by_kind,
            "items_total": sum(int(s.get("items_total", 0)) for s in sources),
            "last_sync_at": max(synced) if synced else "",
            "runs": len(runs),
            "completed": sum(1 for r in runs if r["status"] == "completed"),
            "failed": sum(1 for r in runs if r["status"] == "failed"),
            "packages_produced": sum(int(r.get("packages", 0)) for r in runs),
            "catalogue": self._registry.describe(),
        }

    # -------------------------------------------------------------- helpers
    def _require(self, connector_id: str) -> dict:
        record = self.get(connector_id)
        if record is None:
            raise KeyError(f"Unknown data source: {connector_id}")
        return record

    @staticmethod
    def _next_sync_at(cadence: str, failures: int) -> str:
        from datetime import datetime, timedelta, timezone
        seconds = CADENCES[cadence]
        if seconds < 0:
            return ""
        if failures:
            seconds = max(seconds, 60) * min(2 ** failures, 8)
        return (datetime.now(timezone.utc)
                + timedelta(seconds=seconds)).isoformat()

    def _append(self, section: str, item: dict, cap: int) -> None:
        try:
            self._store.append(section, item, cap=cap)
        except Exception:  # noqa: BLE001 — history is observability, not truth
            logger.exception("Persisting %s failed", section)

    @staticmethod
    def _summarize(runs: list[dict], trigger: str) -> dict[str, Any]:
        return {"trigger": trigger, "sources": len(runs),
                "completed": sum(1 for r in runs if r["status"] == "completed"),
                "degraded": sum(1 for r in runs if r["status"] == "degraded"),
                "failed": sum(1 for r in runs if r["status"] == "failed"),
                "skipped": sum(1 for r in runs if r["status"] == "skipped"),
                "packages": sum(int(r.get("packages", 0)) for r in runs),
                "with_changes": [r["connector"] for r in runs
                                 if r.get("packages") or r.get("removed")]}

    def _announce(self, kind: str, record: dict,
                  extra: dict | None = None) -> None:
        if self._bus is None:
            return
        try:
            self._bus.publish(kind, {
                "connector_id": record.get("connector_id", ""),
                "name": record.get("name", ""),
                "connector_kind": record.get("kind", ""), **(extra or {})},
                project_id=record.get("project_id", ""),
                source="connector_framework")
        except Exception:  # noqa: BLE001 — announcing never fails the work
            logger.exception("Connector event publication failed")


def _initial_state() -> dict:
    return {"health": "unknown", "health_detail": "", "health_checked_at": "",
            "sync_state": "never_synced", "sync_version": 0,
            "first_synced_at": "", "last_synced_at": "",
            "last_sync_status": "", "last_error": "",
            "consecutive_failures": 0, "items_total": 0, "next_sync_at": "",
            "last_test": {}}


def _looks_like_a_secret(location: str) -> bool:
    """Catch the obvious mistake of pasting a credentialed connection string
    where it would be persisted and served over the API."""
    text = (location or "").lower()
    return "://" in text and "@" in text.split("://", 1)[1].split("/", 1)[0]

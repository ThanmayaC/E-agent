"""Synchronization Engine — incremental, versioned, resumable.

A sync is a comparison, not a reload. Every record gets a stable **key** and a
content **fingerprint**; the next sync reads the source, fingerprints it
again, and emits only the difference:

    added     a key that was not there before
    changed   a key whose fingerprint moved
    removed   a key that is gone from the source
    unchanged everything else — the overwhelming majority, and the reason
              this layer can run every hour without melting anything

    first sync  → every record is "added"     (mode: first)
    later syncs → only the delta is reported  (mode: delta)
    failure     → recorded, retried with backoff, state preserved
                  (mode: retry) — a failed sync never destroys the last
                  good fingerprints, so the next attempt resumes rather
                  than restarts

Each successful sync increments the source's version. Downstream (the
Knowledge Refresh Pipeline) consumes the *delta*, which is what makes
incremental learning possible: nothing rebuilds knowledge that did not change.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Any

import pandas as pd

from app.core.logging import get_logger
from app.sync.reader import SourceReader, SourceUnreadable
from app.sync.registry import DataSourceRegistry, SecretNotConfigured
from app.sync.store import SyncStore, new_id, now_iso

logger = get_logger(__name__)

MAX_SYNC_RUNS = 300
# Columns whose name suggests a stable business identifier, in preference
# order. A source without one falls back to a hash of the whole record, which
# still detects change correctly — it just cannot tell "changed" from
# "removed + added".
KEY_HINTS = ("id", "_id", "key", "code", "number", "no", "uuid", "guid")
# Per-sync record ceiling: synchronization is a background heartbeat job, not
# a bulk loader. A source bigger than this syncs its first slice and reports
# the truncation rather than pretending it saw everything.
MAX_RECORDS_PER_TABLE = 50_000


@dataclass
class SyncDelta:
    """What changed in one table since the last sync."""
    table: str
    added: list[dict] = field(default_factory=list)
    changed: list[dict] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)
    unchanged: int = 0
    columns: list[str] = field(default_factory=list)
    truncated: bool = False

    @property
    def changed_count(self) -> int:
        return len(self.added) + len(self.changed) + len(self.removed)

    def describe(self) -> dict:
        return {"table": self.table, "added": len(self.added),
                "changed": len(self.changed), "removed": len(self.removed),
                "unchanged": self.unchanged, "columns": self.columns,
                "truncated": self.truncated}


@dataclass
class SyncResult:
    """The outcome of synchronizing one source."""
    source_id: str
    source_name: str
    mode: str                       # first | delta | retry | failed | skipped
    status: str                     # completed | failed | skipped
    version: int = 0
    deltas: list[SyncDelta] = field(default_factory=list)
    records_total: int = 0
    error: str = ""
    started_at: str = ""
    finished_at: str = ""
    run_id: str = ""

    @property
    def changed_records(self) -> int:
        return sum(d.changed_count for d in self.deltas)

    @property
    def has_changes(self) -> bool:
        return self.changed_records > 0

    def describe(self) -> dict:
        return {"run_id": self.run_id, "source_id": self.source_id,
                "source": self.source_name, "mode": self.mode,
                "status": self.status, "version": self.version,
                "records_total": self.records_total,
                "changed_records": self.changed_records,
                "tables": [d.describe() for d in self.deltas],
                "error": self.error, "started_at": self.started_at,
                "finished_at": self.finished_at}


class SynchronizationEngine:
    def __init__(self, store: SyncStore, registry: DataSourceRegistry,
                 reader: SourceReader, bus=None, max_attempts: int = 2):
        self._store = store
        self._registry = registry
        self._reader = reader
        self._bus = bus
        self._max_attempts = max_attempts

    def attach_bus(self, bus) -> None:
        """Announce sync outcomes on the enterprise event bus."""
        self._bus = bus

    # ---------------------------------------------------------------- sync
    def sync(self, source_id: str, force_full: bool = False) -> SyncResult:
        """Synchronize one source. Never raises: a failure is recorded on the
        source, announced, and retried on the next cadence — one unreachable
        system must not stop the others."""
        source = self._registry.get(source_id)
        if source is None:
            raise KeyError(f"Unknown source: {source_id}")

        result = SyncResult(source_id=source_id, source_name=source["name"],
                            mode="first", status="failed",
                            started_at=now_iso(), run_id=new_id("sync"))
        if source["capability"] != "native":
            return self._skip(result, source,
                              f"{source['title']} awaits its Version 2 provider")
        if not source["enabled"]:
            return self._skip(result, source, "source is disabled")

        previous = {} if force_full else self._store.fingerprints(source_id)
        result.mode = "first" if not previous else "delta"
        self._registry.mark_syncing(source_id)

        error = ""
        for attempt in range(1, self._max_attempts + 1):
            try:
                tables = self._reader.read(source,
                                           self._registry.auth_for(source))
                result.deltas, fingerprints, total = self._diff(tables, previous)
                result.records_total = total
                result.version = source["sync_version"] + 1
                result.status = "completed"
                error = ""
                self._store.save_fingerprints(source_id, fingerprints)
                break
            except (SourceUnreadable, SecretNotConfigured) as exc:
                error = str(exc)[:300]  # configuration, not transience
                break
            except Exception as exc:  # noqa: BLE001 — transient: worth a retry
                error = str(exc)[:300]
                logger.exception("Sync of source %s failed (attempt %d/%d)",
                                 source["name"], attempt, self._max_attempts)
                if attempt < self._max_attempts:
                    result.mode = "retry"

        result.finished_at = now_iso()
        if error:
            result.status = "failed"
            result.error = error
            self._registry.mark_failed(source_id, error)
        else:
            self._registry.mark_synced(source_id, result.records_total,
                                       result.version, result.mode)
        self._record(result)
        self._announce(result)
        return result

    def sync_due(self) -> dict[str, Any]:
        """The scheduler's job: synchronize every source whose cadence is up."""
        results = [self.sync(s["source_id"]) for s in self._registry.due()]
        return self._summarize(results)

    def sync_all(self, force_full: bool = False) -> dict[str, Any]:
        results = [self.sync(s["source_id"], force_full=force_full)
                   for s in self._registry.sources(enabled_only=True)
                   if s["capability"] == "native"]
        return self._summarize(results)

    @staticmethod
    def _summarize(results: list[SyncResult]) -> dict[str, Any]:
        return {"sources": len(results),
                "synced": sum(1 for r in results if r.status == "completed"),
                "failed": sum(1 for r in results if r.status == "failed"),
                "skipped": sum(1 for r in results if r.status == "skipped"),
                "changed_records": sum(r.changed_records for r in results),
                "with_changes": [r.source_name for r in results
                                 if r.has_changes]}

    # ---------------------------------------------------------------- diff
    def _diff(self, tables, previous: dict[str, str]
              ) -> tuple[list[SyncDelta], dict[str, str], int]:
        """Fingerprint every record and compare against the last sync."""
        deltas: list[SyncDelta] = []
        fingerprints: dict[str, str] = {}
        total = 0

        for table in tables:
            frame = table.df
            truncated = len(frame) > MAX_RECORDS_PER_TABLE
            if truncated:
                frame = frame.head(MAX_RECORDS_PER_TABLE)
            delta = SyncDelta(table=table.name,
                              columns=[str(c) for c in frame.columns],
                              truncated=truncated)
            key_column = _key_column(frame)
            total += len(frame)

            for record in _records(frame):
                key = _record_key(table.name, record, key_column)
                digest = _fingerprint(record)
                fingerprints[key] = digest
                before = previous.get(key)
                if before is None:
                    delta.added.append({"key": key, "table": table.name,
                                        "record": record})
                elif before != digest:
                    delta.changed.append({"key": key, "table": table.name,
                                          "record": record})
                else:
                    delta.unchanged += 1

            deltas.append(delta)

        # Keys that were present last time and are gone now, attributed to the
        # table they came from.
        live = set(fingerprints)
        by_table = {d.table: d for d in deltas}
        for key in previous:
            if key in live:
                continue
            table_name = key.split(":", 1)[0]
            target = by_table.get(table_name)
            if target is not None:
                target.removed.append(key)
        return deltas, fingerprints, total

    # -------------------------------------------------------------- record
    def _skip(self, result: SyncResult, source: dict,
              reason: str) -> SyncResult:
        result.mode, result.status = "skipped", "skipped"
        result.error = reason
        result.finished_at = now_iso()
        self._record(result)
        return result

    def _record(self, result: SyncResult) -> None:
        try:
            self._store.append("sync_runs", result.describe(),
                               cap=MAX_SYNC_RUNS)
        except Exception:  # noqa: BLE001 — history is observability, not truth
            logger.exception("Sync history persistence failed")

    def _announce(self, result: SyncResult) -> None:
        if self._bus is None:
            return
        try:
            kind = ("SourceSynchronized" if result.status == "completed"
                    else "SourceSyncFailed" if result.status == "failed"
                    else "")
            if not kind:
                return
            self._bus.publish(kind, {
                "source_id": result.source_id, "source": result.source_name,
                "mode": result.mode, "version": result.version,
                "changed_records": result.changed_records,
                "records_total": result.records_total,
                "error": result.error}, source="sync_engine")
        except Exception:  # noqa: BLE001 — announcing never fails a sync
            logger.exception("Sync event publication failed")

    # ---------------------------------------------------------------- read
    def runs(self, source_id: str = "", limit: int = 50) -> list[dict]:
        items = self._store.read("sync_runs")
        if source_id:
            items = [r for r in items if r["source_id"] == source_id]
        return list(reversed(items))[:limit]  # newest first

    def stats(self) -> dict:
        runs = self._store.read("sync_runs")
        return {"runs": len(runs),
                "completed": sum(1 for r in runs if r["status"] == "completed"),
                "failed": sum(1 for r in runs if r["status"] == "failed"),
                "records_synchronized": sum(r.get("changed_records", 0)
                                            for r in runs),
                "last_run_at": runs[-1]["finished_at"] if runs else ""}


# --------------------------------------------------------------- utilities
def _records(frame: pd.DataFrame) -> list[dict]:
    """Rows as JSON-safe dicts (NaN → None, timestamps → ISO strings)."""
    return json.loads(frame.to_json(orient="records", date_format="iso"))


def _key_column(frame: pd.DataFrame) -> str | None:
    """The column that best identifies a record: a unique, non-null,
    identifier-looking column. Without one, records are keyed positionally."""
    for hint in KEY_HINTS:
        for column in frame.columns:
            name = str(column).strip().lower()
            if (name == hint or name.endswith(f"_{hint}")
                    or name.startswith(f"{hint}_")):
                series = frame[column]
                if series.notna().all() and series.is_unique:
                    return str(column)
    return None


def _record_key(table: str, record: dict, key_column: str | None) -> str:
    if key_column is not None:
        return f"{table}:{record.get(key_column)}"
    # No business key: identity is the record's content, so an edit reads as
    # a removal plus an addition. Correct, just less precise — and honest.
    return f"{table}:#{_fingerprint(record)[:16]}"


def _fingerprint(record: dict) -> str:
    payload = json.dumps(record, sort_keys=True, default=str)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()

"""The transaction warehouse — DuckDB over the raw parquet corpus.

Every analytical answer in the platform is a SQL query against this layer. That
is a deliberate constraint: there is no aggregate table, no nightly rollup and
no stored dashboard anywhere in the system, so a number on a screen can always
be traced to the transactions that produced it.

Repeated queries are memoised against the corpus signature (newest parquet
mtime), which makes dashboards fast without ever persisting a derived table —
invalidate by touching the corpus and the cache is gone.
"""
from __future__ import annotations

import hashlib
import json
import threading
import time
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.core.logging import get_logger

logger = get_logger(__name__)

try:
    import duckdb
    _DUCKDB = True
except ImportError:  # pragma: no cover
    _DUCKDB = False

# Transaction rows that represent a payment *attempt* on the rail.
ATTEMPT_TYPES = ("PAYMENT", "MANDATE_EXECUTION", "RETRY", "MANDATE_RETRY")
# Rows that move money back rather than forward.
ADJUSTMENT_TYPES = ("REFUND", "REVERSAL", "CHARGEBACK")

_REFERENCE = ("products", "mcc", "banks", "psps", "cities", "segments",
              "customers", "merchants", "mandates", "mandate_events",
              "incidents", "calendar", "failure_codes")


@dataclass
class QueryStat:
    sql_hash: str
    label: str
    rows: int
    ms: float
    cached: bool
    at: float


class Warehouse:
    """Read-only SQL surface over the raw transaction corpus."""

    def __init__(self, root: Path, cache_size: int = 512):
        self.root = Path(root)
        self.txn_dir = self.root / "transactions"
        self.ref_dir = self.root / "reference"
        self._lock = threading.Lock()
        self._con = None
        self._sig: tuple[float, float] | None = None
        self._cache: dict[str, tuple[float, Any]] = {}
        self._cache_size = cache_size
        self._stats: list[QueryStat] = []
        self._hits = 0
        self._misses = 0

    # ------------------------------------------------------------ lifecycle
    @property
    def available(self) -> bool:
        return (_DUCKDB and self.txn_dir.exists()
                and any(self.txn_dir.glob("txns_*.parquet")))

    def signature(self) -> float:
        """Newest mtime across the corpus — the cache key. Memoised briefly so
        a burst of dashboard queries does not re-stat hundreds of files."""
        now = time.monotonic()
        if self._sig and now - self._sig[0] < 5.0:
            return self._sig[1]
        latest = 0.0
        for d in (self.txn_dir, self.ref_dir):
            if not d.exists():
                continue
            for p in d.glob("*.parquet"):
                try:
                    latest = max(latest, p.stat().st_mtime)
                except OSError:
                    pass
        self._sig = (now, latest)
        return latest

    def _connection(self):
        with self._lock:
            if self._con is None:
                self._con = duckdb.connect(":memory:")
                self._con.execute("SET enable_progress_bar=false")
                self._con.execute("PRAGMA threads=4")
                self._define_views(self._con)
                self._view_sig = self.signature()
            elif getattr(self, "_view_sig", None) != self.signature():
                # A rebuild landed: rebind the views and drop the memo.
                self._define_views(self._con)
                self._view_sig = self.signature()
                self._cache.clear()
            return self._con

    def _define_views(self, con) -> None:
        glob = (self.txn_dir / "txns_*.parquet").as_posix()
        con.execute(f"""
            CREATE OR REPLACE VIEW txn AS
            SELECT * FROM read_parquet('{glob}', union_by_name=true)""")
        attempts = ", ".join(f"'{t}'" for t in ATTEMPT_TYPES)
        adjust = ", ".join(f"'{t}'" for t in ADJUSTMENT_TYPES)
        con.execute(f"""
            CREATE OR REPLACE VIEW attempts AS
            SELECT * FROM txn WHERE txn_type IN ({attempts})""")
        con.execute("""
            CREATE OR REPLACE VIEW settled AS
            SELECT * FROM attempts WHERE status = 'SUCCESS'""")
        con.execute(f"""
            CREATE OR REPLACE VIEW adjustments AS
            SELECT * FROM txn WHERE txn_type IN ({adjust})""")
        for name in _REFERENCE:
            path = self.ref_dir / f"{name}.parquet"
            if path.exists():
                con.execute(
                    f"CREATE OR REPLACE VIEW dim_{name} AS "
                    f"SELECT * FROM read_parquet('{path.as_posix()}')")

    # --------------------------------------------------------------- query
    def query(self, sql: str, params: tuple | list | None = None, *,
              label: str = "", cache: bool = True) -> list[dict]:
        """Run SQL and return rows as dicts. Results are memoised per corpus
        signature; pass cache=False for genuinely one-shot queries."""
        if not self.available:
            return []
        key = self._key(sql, params)
        if cache:
            hit = self._cache.get(key)
            if hit and hit[0] == self.signature():
                self._hits += 1
                return hit[1]
        t0 = time.perf_counter()
        con = self._connection().cursor()
        try:
            cur = con.execute(sql, params) if params else con.execute(sql)
            cols = [d[0] for d in cur.description]
            rows = [dict(zip(cols, r)) for r in cur.fetchall()]
        except Exception as exc:  # noqa: BLE001 — a bad query must not 500 the app
            logger.exception("warehouse query failed: %s", label or sql[:120])
            raise WarehouseQueryError(str(exc)) from exc
        finally:
            con.close()
        ms = (time.perf_counter() - t0) * 1000
        self._misses += 1
        self._record(key, label or sql.strip().split("\n")[0][:80], len(rows),
                     ms, False)
        if cache:
            if len(self._cache) >= self._cache_size:
                self._cache.pop(next(iter(self._cache)))
            self._cache[key] = (self.signature(), rows)
        return rows

    def one(self, sql: str, params=None, *, label: str = "") -> dict:
        rows = self.query(sql, params, label=label)
        return rows[0] if rows else {}

    def scalar(self, sql: str, params=None, default=None):
        row = self.one(sql, params)
        return next(iter(row.values()), default) if row else default

    def df(self, sql: str, params=None):
        """Pandas frame — used by the ML layer, never cached (it is large)."""
        if not self.available:
            import pandas as pd
            return pd.DataFrame()
        con = self._connection().cursor()
        try:
            cur = con.execute(sql, params) if params else con.execute(sql)
            return cur.df()
        finally:
            con.close()

    @staticmethod
    def _key(sql: str, params) -> str:
        blob = sql + "||" + json.dumps(params, default=str, sort_keys=True)
        return hashlib.sha1(blob.encode("utf-8")).hexdigest()

    def _record(self, key: str, label: str, rows: int, ms: float,
                cached: bool) -> None:
        self._stats.append(QueryStat(key[:10], label, rows, round(ms, 2),
                                     cached, time.time()))
        if len(self._stats) > 300:
            del self._stats[:100]

    # -------------------------------------------------------------- status
    def manifest(self) -> dict:
        mf = self.root / "MANIFEST.json"
        if mf.exists():
            try:
                return json.loads(mf.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                return {}
        return {}

    def status(self) -> dict:
        """Real runtime state of the warehouse — for the Admin console."""
        files = sorted(self.txn_dir.glob("txns_*.parquet")) \
            if self.txn_dir.exists() else []
        bytes_on_disk = sum(p.stat().st_size for p in files)
        ref_files = sorted(self.ref_dir.glob("*.parquet")) \
            if self.ref_dir.exists() else []
        bytes_on_disk += sum(p.stat().st_size for p in ref_files)
        out = {
            "available": self.available,
            "engine": "duckdb" if _DUCKDB else "unavailable",
            "root": str(self.root),
            "partitions": len(files),
            "reference_tables": [p.stem for p in ref_files],
            "bytes_on_disk": bytes_on_disk,
            "mb_on_disk": round(bytes_on_disk / 1_048_576, 1),
            "cache": {"entries": len(self._cache), "hits": self._hits,
                      "misses": self._misses,
                      "hit_rate_pct": round(
                          100 * self._hits / max(1, self._hits + self._misses),
                          1)},
            "manifest": {k: v for k, v in self.manifest().items()
                         if k != "per_day"},
        }
        if self.available:
            try:
                row = self.one(
                    "SELECT count(*) AS transactions, "
                    "min(txn_date) AS first_date, max(txn_date) AS last_date, "
                    "count(DISTINCT txn_date) AS days, "
                    "count(DISTINCT product_code) AS products "
                    "FROM txn", label="warehouse.status")
                out.update(row)
            except WarehouseQueryError:
                out["available"] = False
        return out

    def recent_queries(self, limit: int = 40) -> list[dict]:
        return [{"hash": s.sql_hash, "label": s.label, "rows": s.rows,
                 "ms": s.ms, "cached": s.cached, "at": s.at}
                for s in reversed(self._stats[-limit:])]

    def table_profile(self) -> list[dict]:
        """Row counts per logical table — genuinely queried, not asserted."""
        if not self.available:
            return []
        out = []
        for view in ("txn", "attempts", "settled", "adjustments"):
            try:
                n = self.scalar(f"SELECT count(*) FROM {view}", default=0)
                out.append({"table": view, "rows": int(n or 0),
                            "kind": "derived view"})
            except WarehouseQueryError:
                pass
        for name in _REFERENCE:
            if (self.ref_dir / f"{name}.parquet").exists():
                try:
                    n = self.scalar(f"SELECT count(*) FROM dim_{name}",
                                    default=0)
                    out.append({"table": f"dim_{name}", "rows": int(n or 0),
                                "kind": "reference"})
                except WarehouseQueryError:
                    pass
        return out

    def schema(self, view: str = "txn") -> list[dict]:
        if not self.available:
            return []
        return self.query(f"DESCRIBE {view}", label=f"schema.{view}")


class WarehouseQueryError(RuntimeError):
    """Raised when a warehouse query cannot be executed."""


@lru_cache(maxsize=4)
def get_warehouse(root: str) -> Warehouse:
    return Warehouse(Path(root))

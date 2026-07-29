"""EnterpriseReader — structured facts from the ingested NPCI UPI corpus.

The Enterprise Brain holds the organization as documents and vector chunks;
this reader recovers the *structured* facts an executive layer needs to reason
without hallucinating — the KPI series (from the workbook, the numeric source
of truth), the master data (products, banks, PSPs, merchants, employees), and
the narrative artifacts (decisions, incidents, RCAs, SOPs, reports, meetings,
tasks) parsed from their front-matter.

It reads the generated ``enterprise_data`` tree directly, so every number it
returns equals the workbook cell and every name equals the roster — the same
guarantee the generator enforces. If the corpus has not been generated the
reader degrades to empty results and the platform behaves exactly as before.
"""
from __future__ import annotations

import csv
import os
import re
import time
from dataclasses import dataclass, field
from datetime import datetime
from functools import lru_cache
from pathlib import Path

from app.core.logging import get_logger

try:
    import openpyxl
    _XLSX = True
except ImportError:  # pragma: no cover
    _XLSX = False

logger = get_logger(__name__)

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday", "Sunday"]

_FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_TITLE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
_REFS = re.compile(r"^Refs:\s*(.+)$", re.MULTILINE)


@dataclass
class Artifact:
    art_id: str
    kind: str
    title: str
    timestamp: str
    text: str
    refs: list[str]
    day: int
    path: str

    @property
    def when(self) -> datetime | None:
        try:
            return datetime.fromisoformat(self.timestamp)
        except (ValueError, TypeError):
            return None


@dataclass
class Enterprise:
    """Everything the executive layer reasons over, loaded once."""
    organization: str = ""
    department: str = ""
    week_start: str = ""
    kpis: dict[str, list[float]] = field(default_factory=dict)
    kpi_units: dict[str, str] = field(default_factory=dict)
    banks_perf: list[dict] = field(default_factory=list)
    psps_perf: list[dict] = field(default_factory=list)
    merchants_perf: list[dict] = field(default_factory=list)
    products: list[dict] = field(default_factory=list)
    banks: list[dict] = field(default_factory=list)
    psps: list[dict] = field(default_factory=list)
    merchants: list[dict] = field(default_factory=list)
    employees: list[dict] = field(default_factory=list)
    artifacts: list[Artifact] = field(default_factory=list)

    def by_kind(self, kind: str) -> list[Artifact]:
        return [a for a in self.artifacts if a.kind == kind]

    def get(self, art_id: str) -> Artifact | None:
        return next((a for a in self.artifacts if a.art_id == art_id), None)

    @property
    def available(self) -> bool:
        return bool(self.kpis or self.artifacts)


# Day sub-folder -> the artifact kind we treat it as for the executive layer.
_SUB_KIND = {
    "outlook": "email", "teams": "teams", "meetings": "meeting",
    "decisions": "decision", "incidents": "incident", "docs": "product_document",
    "reports": "report", "tasks": "task",
}


class EnterpriseReader:
    def __init__(self, enterprise_dir: Path):
        self._dir = Path(enterprise_dir)
        self._sig_cache: tuple[float, float] | None = None

    # ------------------------------------------------------------- loading
    def load(self) -> Enterprise:
        if not self._dir.exists():
            logger.info("Executive layer: %s does not exist — running with no "
                        "enterprise facts", self._dir)
            return Enterprise()
        try:
            return self._load(self._mtime_signature())
        except Exception:  # noqa: BLE001 — the executive layer never breaks the app
            logger.exception("Executive layer: reading the enterprise failed")
            return Enterprise()

    def _mtime_signature(self) -> float:
        """Newest mtime under the tree — the cache key, so a re-ingested or
        regenerated corpus is picked up automatically (dashboard refresh).

        On the 180-day corpus this used to walk + stat every file (thousands,
        including the per-day raw ledger CSVs) on *every* call, and the
        executive layer calls ``load()`` many times per request — so it was the
        dominant cost behind the slow ``/executive/reports``. It is now (a)
        pruned of the ``ledger/`` dirs the executive facts never read, and (b)
        memoised for a short window so a burst of calls collapses to one walk.
        Any regeneration/re-ingest still rewrites non-ledger files, so the
        signature still changes and the cache still refreshes."""
        now = time.monotonic()
        if self._sig_cache and now - self._sig_cache[0] < 3.0:
            return self._sig_cache[1]
        latest = 0.0
        for root, dirs, files in os.walk(self._dir):
            if "ledger" in dirs:
                dirs.remove("ledger")  # raw ledger is never read here
            for fn in files:
                try:
                    m = os.stat(os.path.join(root, fn)).st_mtime
                    if m > latest:
                        latest = m
                except OSError:  # a file vanished mid-walk — ignore
                    pass
        self._sig_cache = (now, latest)
        return latest

    @lru_cache(maxsize=4)
    def _load(self, _signature: float) -> Enterprise:
        ent = Enterprise()
        self._read_manifest(ent)
        self._read_kpis(ent)
        self._read_master(ent)
        self._read_artifacts(ent)
        return ent

    # ------------------------------------------------------------- manifest
    def _read_manifest(self, ent: Enterprise) -> None:
        import json
        mf = self._dir / "INGEST_MANIFEST.json"
        if mf.exists():
            data = json.loads(mf.read_text(encoding="utf-8"))
            ent.organization = data.get("organization", "")
            ent.department = data.get("department", "")
            ent.week_start = data.get("week_start", "")

    # ------------------------------------------------------------- KPIs
    def _read_kpis(self, ent: Enterprise) -> None:
        """Reads either the current month-wide workbook (``upi_kpis_month.
        xlsx``, "Monthly KPIs" sheet, one column per day across up to 5
        weeks) or the older single-week workbook (``upi_kpis_week.xlsx``,
        "Weekly KPIs" sheet, 7 columns) so a not-yet-regenerated corpus keeps
        working."""
        wb_path = self._dir / "master" / "upi_kpis_month.xlsx"
        sheet_name = "Monthly KPIs"
        if not (_XLSX and wb_path.exists()):
            wb_path = self._dir / "master" / "upi_kpis_week.xlsx"
            sheet_name = "Weekly KPIs"
        if not (_XLSX and wb_path.exists()):
            return
        wb = openpyxl.load_workbook(wb_path, data_only=True)
        if sheet_name in wb.sheetnames:
            for row in wb[sheet_name].iter_rows(min_row=2, values_only=True):
                if not row or row[0] is None:
                    continue
                kpi = str(row[0])
                ent.kpi_units[kpi] = str(row[1] or "")
                ent.kpis[kpi] = [self._num(v) for v in row[2:] if v is not None]
        ent.banks_perf = self._sheet_rows(wb, "Bank Performance")
        ent.psps_perf = self._sheet_rows(wb, "PSP Performance")
        ent.merchants_perf = self._sheet_rows(wb, "Merchant KPIs")

    def week_of(self, day_index: int) -> int:
        """0-based week number for a 0-based day index."""
        return day_index // 7

    def kpi_trend(self, kpi: str) -> dict:
        """{today, yesterday, last_week, last_month, trend} for one KPI,
        reading straight from the loaded month-wide series."""
        ent = self.load()
        series = ent.kpis.get(kpi) or []
        if not series:
            return {}
        last = len(series) - 1
        def at(i: int):
            return series[i] if 0 <= i < len(series) else None
        today = at(last)
        yesterday = at(last - 1)
        last_week = at(last - 7)
        last_month = at(0)
        trend = None
        if today is not None and last_month is not None:
            trend = round(today - last_month, 4)
        return {"kpi": kpi, "today": today, "yesterday": yesterday,
                "last_week": last_week, "last_month": last_month,
                "trend": trend}

    @staticmethod
    def _sheet_rows(wb, name: str) -> list[dict]:
        if name not in wb.sheetnames:
            return []
        rows = list(wb[name].iter_rows(values_only=True))
        if not rows:
            return []
        header = [str(h) for h in rows[0]]
        return [dict(zip(header, r)) for r in rows[1:] if any(v is not None
                                                              for v in r)]

    @staticmethod
    def _num(v):
        try:
            f = float(v)
            return int(f) if f.is_integer() else round(f, 4)
        except (TypeError, ValueError):
            return v

    # ------------------------------------------------------------- master
    def _read_master(self, ent: Enterprise) -> None:
        m = self._dir / "master"
        ent.products = self._csv(m / "products.csv")
        ent.banks = self._csv(m / "banks.csv")
        ent.psps = self._csv(m / "psps.csv")
        ent.merchants = self._csv(m / "merchants.csv")
        ent.employees = self._csv(m / "employees.csv")

    @staticmethod
    def _csv(path: Path) -> list[dict]:
        if not path.exists():
            return []
        with path.open(encoding="utf-8") as f:
            return list(csv.DictReader(f))

    # ------------------------------------------------------------- artifacts
    def _read_artifacts(self, ent: Enterprise) -> None:
        for day_dir in sorted(self._dir.glob("day_*")):
            try:
                day = int(day_dir.name.split("_")[1])
            except (IndexError, ValueError):
                continue
            for sub, kind in _SUB_KIND.items():
                folder = day_dir / sub
                if not folder.exists():
                    continue
                for path in sorted(folder.glob("*.md")):
                    art = self._parse(path, kind, day)
                    if art:
                        ent.artifacts.append(art)

    def _parse(self, path: Path, kind: str, day: int) -> Artifact | None:
        try:
            raw = path.read_text(encoding="utf-8")
        except OSError:
            return None
        meta: dict[str, str] = {}
        m = _FRONTMATTER.match(raw)
        body = raw
        if m:
            for line in m.group(1).splitlines():
                if ":" in line:
                    key, _, val = line.partition(":")
                    meta[key.strip()] = val.strip()
            body = raw[m.end():]
        title_m = _TITLE.search(body)
        refs_m = _REFS.search(body)
        # A doc's real kind can be more specific than its folder (SOP vs BRD).
        declared = meta.get("type", kind)
        if declared in ("sop",) or path.name.upper().startswith("SOP"):
            kind = "sop"
        elif declared in ("rca",) or "RCA" in path.name.upper():
            kind = "rca"
        return Artifact(
            art_id=meta.get("id", path.stem),
            kind=kind,
            title=title_m.group(1).strip() if title_m else path.stem,
            timestamp=meta.get("timestamp", ""),
            text=body.strip(),
            refs=[r.strip() for r in refs_m.group(1).split(",")] if refs_m
            else [],
            day=day, path=str(path))

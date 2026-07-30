"""Engine contract — the interface every reasoning engine implements.

The Enterprise AI Orchestrator's whole design rests on one idea: the chat is a
*router over independent engines*, not a single RAG pipeline. Each engine wraps
a capability the platform already owns (analytics, knowledge/RAG, machine
learning, forecasting, recommendation, reporting) behind a uniform interface,
so the orchestrator can decide which run — one, several, or all in parallel —
without knowing how any of them work.

An engine does three things and nothing more:

    can_handle(request)  -> is this engine relevant to this request?
    run(request)         -> EngineResult: evidence + an observability record
    describe()           -> static metadata for the /copilot/orchestration UI

Two invariants keep the layer honest:

- **Engines produce evidence, never prose.** Every fact an engine returns is an
  ``EvidenceItem`` with an id and its numbers inside a ``text`` field, so the
  copilot's existing validator grounds anything the LLM later quotes. The
  engine layer adds no new answering path — it feeds the one that exists.
- **An engine reuses an existing module; it never computes new truth.** Reading
  a KPI series and averaging it is aggregation of facts the platform already
  holds. Inventing a KPI is not an engine's job and not allowed.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any


@dataclass
class EvidenceItem:
    """One citable fact an engine contributes. Mirrors ``Evidence.add`` so the
    orchestrator can merge it straight into the copilot's evidence set — the id
    is the validator's contract, and numbers live in ``payload['text']``."""
    kind: str
    id: str
    summary: str
    payload: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict:
        return {"kind": self.kind, "id": self.id,
                "summary": self.summary[:300], **self.payload}


@dataclass
class EngineResult:
    """What one engine produced for one request — facts plus the trace the
    observability layer shows the operator (Phase 14)."""
    engine: str
    label: str
    ran: bool = True
    evidence: list[EvidenceItem] = field(default_factory=list)
    # A human-readable account of *how* the answer was fetched: the pseudo-SQL
    # an analytics query ran, the ML model used, the documents retrieved. This
    # is the observability payload, not something the LLM sees.
    detail: dict[str, Any] = field(default_factory=dict)
    latency_ms: float = 0.0
    status: str = "ok"          # ok | empty | unavailable | error
    note: str = ""

    def add(self, kind: str, item_id: str, summary: str,
            payload: dict | None = None) -> None:
        if not item_id:
            return
        self.evidence.append(EvidenceItem(kind, item_id, summary,
                                          payload or {}))

    def describe(self) -> dict:
        return {"engine": self.engine, "label": self.label, "ran": self.ran,
                "status": self.status, "latency_ms": round(self.latency_ms, 1),
                "evidence_count": len(self.evidence), "detail": self.detail,
                "note": self.note}


@dataclass
class EngineRequest:
    """Everything an engine needs to decide relevance and gather evidence.

    The orchestrator builds this once from the classified query and hands the
    same object to every engine, so relevance and execution see identical
    inputs.
    """
    message: str
    intent: str
    subject: str = ""
    categories: tuple[str, ...] = ()
    time_range: dict[str, Any] | None = None   # {start, end, label, days}
    kpi_hints: tuple[str, ...] = ()
    entities: dict[str, list[str]] = field(default_factory=dict)


class Engine:
    """Base class: an independent reasoning engine over an existing module."""

    key: str = "engine"
    label: str = "Engine"
    #: Query categories this engine serves. The router matches these against
    #: the classifier's categories to decide whether the engine runs.
    categories: tuple[str, ...] = ()

    def available(self) -> bool:
        """Is the underlying module wired and holding data? An unavailable
        engine is reported as such, never silently skipped."""
        return True

    def can_handle(self, request: EngineRequest) -> bool:
        """Default relevance: the request's categories intersect this engine's.
        Engines override to add shape-based signals (a date range, a KPI name).
        """
        return bool(set(request.categories) & set(self.categories))

    def run(self, request: EngineRequest) -> EngineResult:  # pragma: no cover
        raise NotImplementedError

    # -- helpers ---------------------------------------------------------
    def _result(self) -> EngineResult:
        return EngineResult(engine=self.key, label=self.label)

    def timed(self, request: EngineRequest) -> EngineResult:
        """Run the engine, timing it and turning any failure into an honest
        ``error`` status rather than breaking the whole answer."""
        start = time.perf_counter()
        try:
            if not self.available():
                res = self._result()
                res.ran = False
                res.status = "unavailable"
                res.note = f"{self.label} is not wired or holds no data"
            else:
                res = self.run(request)
        except Exception as exc:  # noqa: BLE001 — one engine never fails the answer
            res = self._result()
            res.status = "error"
            res.note = str(exc)[:200]
        res.latency_ms = (time.perf_counter() - start) * 1000
        if res.status == "ok" and not res.evidence:
            res.status = "empty"
        return res

    def describe(self) -> dict:
        return {"engine": self.key, "label": self.label,
                "categories": list(self.categories),
                "available": self._safe_available()}

    def _safe_available(self) -> bool:
        try:
            return self.available()
        except Exception:  # noqa: BLE001
            return False

"""Evidence Ledger — the control-plane system of record (v3 Phase A/B).

Append-only recorder and query surface for: analysis runs and their node
events, evidence records extracted from the business context, every AI
statement with its citations and verification verdict, report versions, and
the audit log.

During the strangler migration this is a DUAL-WRITE target: the JSON artifact
store remains the v1 API's read path and behaviour is unchanged; the ledger
adds the relational audit fabric that v2 (LangGraph runs, governance
consoles, RBAC) builds on. Audit rows are never purged — deleting a project
removes its data and leaves the record that it was deleted.
"""
from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Any

from sqlalchemy import delete, func, select

from app.core.logging import get_logger
from app.db.control import (
    AuditRow, CitationRow, EvidenceRow, ModelRow, ReportRow, RunEventRow,
    RunRow, StatementRow, create_session_factory,
)

logger = get_logger(__name__)

# AIReport sections that become statements: (section, primary text field)
STATEMENT_SECTIONS: list[tuple[str, str]] = [
    ("key_insights", "title"),
    ("root_causes", "problem"),
    ("risks", "risk"),
    ("opportunities", "opportunity"),
    ("recommendations", "action"),
]


def _now() -> datetime:
    return datetime.now(timezone.utc)


class EvidenceLedger:
    def __init__(self, db_url: str):
        self._session = create_session_factory(db_url)

    # ---------------------------------------------------------------- runs
    def open_run(self, project_id: str, graph: str = "full_analysis") -> str:
        run_id = uuid.uuid4().hex[:16]
        with self._session() as s, s.begin():
            s.add(RunRow(run_id=run_id, project_id=project_id, graph=graph,
                         status="running", started_at=_now()))
        return run_id

    def close_run(self, run_id: str, status: str, error: str = "") -> None:
        with self._session() as s, s.begin():
            run = s.get(RunRow, run_id)
            if run is not None:
                run.status = status
                run.error = error[:2000]
                run.finished_at = _now()

    def record_event(self, run_id: str, node: str, event: str,
                     payload: dict | None = None) -> None:
        with self._session() as s, s.begin():
            seq = s.scalar(select(func.count()).select_from(RunEventRow)
                           .where(RunEventRow.run_id == run_id)) or 0
            s.add(RunEventRow(run_id=run_id, seq=seq + 1, node=node,
                              event=event, payload=payload, at=_now()))

    # ------------------------------------------------------------ evidence
    def record_evidence(self, project_id: str, run_id: str,
                        records: list[dict[str, Any]]) -> int:
        """Append evidence records; (run_id, evidence_id) is unique so
        re-recording within a run is a no-op, not a duplicate."""
        written = 0
        with self._session() as s, s.begin():
            existing = set(s.scalars(
                select(EvidenceRow.evidence_id)
                .where(EvidenceRow.run_id == run_id)))
            for r in records:
                if r["evidence_id"] in existing:
                    continue
                s.add(EvidenceRow(project_id=project_id, run_id=run_id,
                                  evidence_id=r["evidence_id"], kind=r["kind"],
                                  producer=r.get("producer", ""),
                                  payload=r["payload"],
                                  content_hash=r["content_hash"],
                                  created_at=_now()))
                written += 1
        return written

    # ---------------------------------------------------------- statements
    def record_statements(self, project_id: str, run_id: str,
                          ai_report: dict[str, Any]) -> int:
        """Persist every AI statement with its citations and verification
        verdict, exactly as the deterministic verifier left them."""
        written = 0
        with self._session() as s, s.begin():
            for section, text_field in STATEMENT_SECTIONS:
                for item in ai_report.get(section) or []:
                    if not isinstance(item, dict):
                        continue
                    written += 1
                    self._add_statement(s, project_id, run_id, section,
                                        text=str(item.get(text_field, "")),
                                        statement_type=item.get("statement_type"),
                                        verification=str(item.get("verification",
                                                                  "unverified")),
                                        confidence=self._as_float(item.get("confidence")),
                                        payload=item,
                                        evidence_ids=item.get("evidence_ids") or [])
            for text in ai_report.get("data_limitations") or []:
                written += 1
                self._add_statement(s, project_id, run_id, "data_limitations",
                                    text=str(text), statement_type="unknown",
                                    verification="deterministic_source",
                                    confidence=None, payload={"text": str(text)},
                                    evidence_ids=["limitations:dataset"])
        return written

    def record_deterministic_recommendations(self, project_id: str, run_id: str,
                                             recs: list[Any]) -> int:
        """Rule-derived recommendations are statements too — verified by
        construction, since each cites the finding that triggered it."""
        written = 0
        with self._session() as s, s.begin():
            for r in recs:
                item = r.model_dump() if hasattr(r, "model_dump") else dict(r)
                written += 1
                self._add_statement(s, project_id, run_id,
                                    "deterministic_recommendations",
                                    text=str(item.get("action", "")),
                                    statement_type="recommendation",
                                    verification="evidence_verified"
                                    if item.get("evidence_ids") else "rule_derived",
                                    confidence=None, payload=item,
                                    evidence_ids=item.get("evidence_ids") or [])
        return written

    @staticmethod
    def _add_statement(s, project_id: str, run_id: str, section: str, *,
                       text: str, statement_type: Any, verification: str,
                       confidence: float | None, payload: dict,
                       evidence_ids: list) -> None:
        row = StatementRow(project_id=project_id, run_id=run_id, section=section,
                           statement_type=str(statement_type) if statement_type else None,
                           verification=verification, text=text,
                           confidence=confidence, payload=payload, created_at=_now())
        s.add(row)
        s.flush()  # assign row.id for citations
        for eid in evidence_ids:
            s.add(CitationRow(statement_id=row.id, evidence_id=str(eid)))

    @staticmethod
    def _as_float(v: Any) -> float | None:
        try:
            return float(v)
        except (TypeError, ValueError):
            return None  # root-cause confidence may be "low|medium|high"

    # --------------------------------------------------------------- models
    def register_model(self, project_id: str, run_id: str, *, name: str,
                       family: str, task: str, metrics: dict,
                       selection_trace: dict) -> int:
        """Register an admitted model and return its version (per
        project+name). A prediction without a registered model version does
        not enter the ledger — the ML analogue of the anti-hallucination rule."""
        with self._session() as s, s.begin():
            prior = s.scalar(select(func.max(ModelRow.version))
                             .where(ModelRow.project_id == project_id,
                                    ModelRow.name == name)) or 0
            version = prior + 1
            s.add(ModelRow(project_id=project_id, run_id=run_id, name=name,
                           family=family, task=task, version=version,
                           metrics=metrics, selection_trace=selection_trace,
                           created_at=_now()))
        return version

    def models(self, project_id: str) -> list[dict]:
        with self._session() as s:
            rows = s.scalars(select(ModelRow)
                             .where(ModelRow.project_id == project_id)
                             .order_by(ModelRow.id.desc())).all()
        return [{"name": r.name, "family": r.family, "task": r.task,
                 "version": r.version, "stage": r.stage, "run_id": r.run_id,
                 "metrics": r.metrics, "selection_trace": r.selection_trace,
                 "created_at": r.created_at} for r in rows]

    # -------------------------------------------------------------- reports
    def record_report(self, project_id: str, run_id: str, version: int,
                      confidence: float | None, meta: dict) -> None:
        with self._session() as s, s.begin():
            s.add(ReportRow(project_id=project_id, run_id=run_id, version=version,
                            confidence=confidence, meta=meta, generated_at=_now()))

    # ---------------------------------------------------------------- audit
    def audit(self, action: str, resource: str, detail: dict | None = None,
              actor: str = "api") -> None:
        with self._session() as s, s.begin():
            s.add(AuditRow(actor=actor, action=action, resource=resource,
                           detail=detail, at=_now()))

    # -------------------------------------------------------------- queries
    def runs(self, project_id: str) -> list[dict]:
        with self._session() as s:
            rows = s.scalars(select(RunRow).where(RunRow.project_id == project_id)
                             .order_by(RunRow.started_at.desc())).all()
            counts = dict(s.execute(
                select(RunEventRow.run_id, func.count())
                .where(RunEventRow.run_id.in_([r.run_id for r in rows]))
                .group_by(RunEventRow.run_id)).all()) if rows else {}
        return [{"run_id": r.run_id, "graph": r.graph, "status": r.status,
                 "error": r.error, "started_at": r.started_at,
                 "finished_at": r.finished_at,
                 "events": counts.get(r.run_id, 0)} for r in rows]

    def run_events(self, run_id: str) -> list[dict]:
        with self._session() as s:
            rows = s.scalars(select(RunEventRow).where(RunEventRow.run_id == run_id)
                             .order_by(RunEventRow.seq)).all()
        return [{"seq": e.seq, "node": e.node, "event": e.event,
                 "payload": e.payload, "at": e.at} for e in rows]

    def statements(self, project_id: str, run_id: str | None = None) -> list[dict]:
        with self._session() as s:
            q = select(StatementRow).where(StatementRow.project_id == project_id)
            if run_id:
                q = q.where(StatementRow.run_id == run_id)
            rows = s.scalars(q.order_by(StatementRow.id)).all()
            cites: dict[int, list[str]] = {}
            if rows:
                for sid, eid in s.execute(
                        select(CitationRow.statement_id, CitationRow.evidence_id)
                        .where(CitationRow.statement_id.in_([r.id for r in rows]))):
                    cites.setdefault(sid, []).append(eid)
        return [{"id": r.id, "run_id": r.run_id, "section": r.section,
                 "statement_type": r.statement_type, "verification": r.verification,
                 "text": r.text, "confidence": r.confidence,
                 "evidence_ids": cites.get(r.id, []), "detail": r.payload}
                for r in rows]

    def evidence(self, project_id: str, run_id: str | None = None,
                 kind: str | None = None) -> list[dict]:
        with self._session() as s:
            q = select(EvidenceRow).where(EvidenceRow.project_id == project_id)
            if run_id:
                q = q.where(EvidenceRow.run_id == run_id)
            if kind:
                q = q.where(EvidenceRow.kind == kind)
            rows = s.scalars(q.order_by(EvidenceRow.id)).all()
        return [{"evidence_id": r.evidence_id, "run_id": r.run_id, "kind": r.kind,
                 "producer": r.producer, "payload": r.payload,
                 "content_hash": r.content_hash} for r in rows]

    def evidence_ids(self, project_id: str, run_id: str) -> set[str]:
        with self._session() as s:
            return set(s.scalars(select(EvidenceRow.evidence_id)
                                 .where(EvidenceRow.project_id == project_id,
                                        EvidenceRow.run_id == run_id)))

    # ---------------------------------------------------------------- purge
    def purge_project(self, project_id: str) -> None:
        """Remove every ledger row a project owns. audit_log survives —
        deletions are audited, never erased."""
        with self._session() as s, s.begin():
            run_ids = list(s.scalars(select(RunRow.run_id)
                                     .where(RunRow.project_id == project_id)))
            stmt_ids = list(s.scalars(select(StatementRow.id)
                                      .where(StatementRow.project_id == project_id)))
            if stmt_ids:
                s.execute(delete(CitationRow)
                          .where(CitationRow.statement_id.in_(stmt_ids)))
            s.execute(delete(StatementRow)
                      .where(StatementRow.project_id == project_id))
            s.execute(delete(EvidenceRow)
                      .where(EvidenceRow.project_id == project_id))
            s.execute(delete(ReportRow)
                      .where(ReportRow.project_id == project_id))
            s.execute(delete(ModelRow)
                      .where(ModelRow.project_id == project_id))
            if run_ids:
                s.execute(delete(RunEventRow)
                          .where(RunEventRow.run_id.in_(run_ids)))
            s.execute(delete(RunRow).where(RunRow.project_id == project_id))

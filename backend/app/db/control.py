"""Control-plane schema (v3 Phase A).

Relational system of record for runs, evidence, AI statements and their
citations, report versions, and the audit log. SQLite by default (lite
profile — zero extra infrastructure), PostgreSQL via EDIP_DATABASE_URL (full
profile). JSON artifacts remain the read path for the v1 API during the
strangler migration; this schema is the dual-write target that v2 APIs and
governance consoles build on.

statements × citations × evidence is the platform's constitutional core:
every AI sentence, its type, its verification verdict, and exactly which
deterministic facts it rests on — one join away.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, Optional

from sqlalchemy import (
    JSON, DateTime, Float, ForeignKey, Integer, String, Text, UniqueConstraint,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker


class Base(DeclarativeBase):
    pass


class RunRow(Base):
    __tablename__ = "runs"
    run_id: Mapped[str] = mapped_column(String(32), primary_key=True)
    project_id: Mapped[str] = mapped_column(String(80), index=True)
    graph: Mapped[str] = mapped_column(String(40), default="full_analysis")
    status: Mapped[str] = mapped_column(String(24), default="running")
    # running | ready | awaiting_clarification | failed
    error: Mapped[str] = mapped_column(Text, default="")
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    finished_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True),
                                                            nullable=True)


class RunEventRow(Base):
    __tablename__ = "run_events"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    run_id: Mapped[str] = mapped_column(String(32), index=True)
    seq: Mapped[int] = mapped_column(Integer)
    node: Mapped[str] = mapped_column(String(60))
    event: Mapped[str] = mapped_column(String(24))  # started | completed | failed
    payload: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class EvidenceRow(Base):
    __tablename__ = "evidence"
    __table_args__ = (UniqueConstraint("run_id", "evidence_id",
                                       name="uq_evidence_run_eid"),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    project_id: Mapped[str] = mapped_column(String(80), index=True)
    run_id: Mapped[str] = mapped_column(String(32), index=True)
    evidence_id: Mapped[str] = mapped_column(String(120), index=True)
    kind: Mapped[str] = mapped_column(String(30))
    # kpi | signal | forecast | quality | limitation | fact
    producer: Mapped[str] = mapped_column(String(60), default="")
    payload: Mapped[dict] = mapped_column(JSON)
    content_hash: Mapped[str] = mapped_column(String(40), index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class StatementRow(Base):
    __tablename__ = "statements"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    project_id: Mapped[str] = mapped_column(String(80), index=True)
    run_id: Mapped[str] = mapped_column(String(32), index=True)
    section: Mapped[str] = mapped_column(String(50))
    # key_insights | root_causes | risks | opportunities | recommendations |
    # deterministic_recommendations | data_limitations
    statement_type: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    verification: Mapped[str] = mapped_column(String(30), default="unverified")
    text: Mapped[str] = mapped_column(Text)
    confidence: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    payload: Mapped[dict] = mapped_column(JSON)  # the full statement object
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class CitationRow(Base):
    __tablename__ = "citations"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    statement_id: Mapped[int] = mapped_column(ForeignKey("statements.id"), index=True)
    evidence_id: Mapped[str] = mapped_column(String(120), index=True)


class ReportRow(Base):
    __tablename__ = "reports"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    project_id: Mapped[str] = mapped_column(String(80), index=True)
    run_id: Mapped[str] = mapped_column(String(32), index=True)
    version: Mapped[int] = mapped_column(Integer)
    confidence: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    meta: Mapped[dict] = mapped_column(JSON)
    generated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class ModelRow(Base):
    """Model registry (v3 Phase F seed): every admitted model, its selection
    trace, and its evaluation metrics — the audit trail behind each
    ml_prediction evidence record. Versions are per (project, name)."""
    __tablename__ = "models"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    project_id: Mapped[str] = mapped_column(String(80), index=True)
    run_id: Mapped[str] = mapped_column(String(32), index=True)
    name: Mapped[str] = mapped_column(String(80), index=True)
    family: Mapped[str] = mapped_column(String(40))   # linear | ets | gbm | ...
    task: Mapped[str] = mapped_column(String(40))     # kpi_forecast | churn | ...
    version: Mapped[int] = mapped_column(Integer)
    stage: Mapped[str] = mapped_column(String(24), default="run_scoped")
    # run_scoped | staging | production — promotion beyond run_scoped
    # requires human approval (03-ml-platform §6)
    metrics: Mapped[dict] = mapped_column(JSON)
    selection_trace: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


class AuditRow(Base):
    """Append-only. Never purged — deletions are audited, not erased."""
    __tablename__ = "audit_log"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    actor: Mapped[str] = mapped_column(String(80), default="api")
    action: Mapped[str] = mapped_column(String(60), index=True)
    resource: Mapped[str] = mapped_column(String(160), index=True)
    detail: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    at: Mapped[datetime] = mapped_column(DateTime(timezone=True))


def create_session_factory(db_url: str) -> sessionmaker:
    """Engine + schema bootstrap. SQLite needs cross-thread access because
    analysis runs on background threads/workers while the API reads."""
    connect_args: dict[str, Any] = {}
    if db_url.startswith("sqlite"):
        connect_args["check_same_thread"] = False
    engine = create_engine(db_url, future=True, connect_args=connect_args)
    Base.metadata.create_all(engine)
    return sessionmaker(engine, expire_on_commit=False, future=True)

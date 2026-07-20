"""Clarification answer intake shared by the gate node and the resume API.

Mirrors the v1 endpoint's contract: an answer that picks a candidate column
becomes a permanent schema alias, and every answer is remembered org-wide by
schema signature so an equivalent dataset is never asked twice.
"""
from __future__ import annotations

from typing import Any

from app.domain.entities import UnderstandingAssessment
from app.knowledge.store import KnowledgeStore

CANONICAL_BY_KIND = {"revenue_ambiguity": "Revenue",
                     "identifier_ambiguity": "Primary Identifier",
                     "time_ambiguity": "Reporting Period"}


def record_answers(knowledge: KnowledgeStore, project_id: str,
                   understanding: UnderstandingAssessment,
                   answers: dict[str, Any]) -> int:
    """Persist {question_id: answer} into enterprise knowledge and mark the
    matching questions answered on the assessment. Returns answers recorded."""
    recorded = 0
    by_id = {q.id: q for q in understanding.questions}
    for question_id, raw in (answers or {}).items():
        q = by_id.get(str(question_id))
        answer = str(raw or "").strip()
        if q is None or not answer:
            continue
        aliases = [answer] if answer in (q.candidates or []) else []
        canonical = CANONICAL_BY_KIND.get(q.kind or "")
        if aliases and canonical:
            knowledge.add_schema_alias(answer, canonical)
        knowledge.remember_clarification(
            question=q.question, answer=answer, signature=q.signature or "",
            project_id=project_id, kind=q.kind or "", dataset=q.dataset or "",
            confidence_before=understanding.confidence, aliases=aliases)
        q.answer = answer
        q.answered = True
        recorded += 1
    return recorded

"""Enterprise knowledge APIs — the platform's persistent, org-wide learning.

Terminology, business rules, and clarifications entered here are injected
into every future reasoning prompt, so the system gets smarter over time.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel

from app.api.deps import container
from app.core.container import Container

router = APIRouter(tags=["knowledge"])


@router.get("/knowledge")
def knowledge_snapshot(c: Container = Depends(container)):
    """Full knowledge dump for the Knowledge Explorer."""
    return c.knowledge.snapshot()


@router.get("/knowledge/search")
def knowledge_search(q: str = Query(..., min_length=2), c: Container = Depends(container)):
    return c.knowledge.search(q)


@router.get("/knowledge/history")
def knowledge_history(limit: int = Query(50, ge=1, le=500), section: str = "",
                      c: Container = Depends(container)):
    """Most recent knowledge mutations (the version journal), newest last."""
    return c.knowledge.history(limit=limit, section=section)


@router.get("/knowledge/versions")
def knowledge_versions(key: str = Query(..., min_length=3),
                       c: Container = Depends(container)):
    """Full version history of one knowledge key (e.g. ``term:revenue``,
    ``alias:cust_id``), oldest first — every version records timestamp,
    source, confidence, and project origin."""
    return c.knowledge.versions(key)


@router.get("/knowledge/graph")
def enterprise_graph(limit: int = Query(500, ge=1, le=5000),
                     c: Container = Depends(container)):
    """The organization-wide knowledge graph (node-link JSON + stats)."""
    return c.enterprise_graph.payload(limit=limit)


@router.get("/knowledge/graph/search")
def enterprise_graph_search(q: str = Query(..., min_length=2),
                            c: Container = Depends(container)):
    return c.enterprise_graph.find(q)


@router.get("/knowledge/graph/node")
def enterprise_graph_node(id: str = Query(..., min_length=1),
                          c: Container = Depends(container)):
    """One node with all its in/out relationships."""
    return c.enterprise_graph.neighbors(id)


@router.get("/knowledge/relationships")
def enterprise_relationships(kind: str = "",
                             limit: int = Query(200, ge=1, le=2000),
                             c: Container = Depends(container)):
    """Enterprise graph relationships, optionally filtered by kind."""
    return c.enterprise_graph.relations(kind=kind, limit=limit)


@router.get("/knowledge/terminology")
def terminology(c: Container = Depends(container)):
    return c.knowledge.snapshot().get("terminology", {})


@router.get("/knowledge/rules")
def business_rules(c: Container = Depends(container)):
    return c.knowledge.snapshot().get("business_rules", [])


@router.get("/knowledge/clarifications")
def clarifications(c: Container = Depends(container)):
    return c.knowledge.snapshot().get("clarifications", [])


class Term(BaseModel):
    term: str
    definition: str
    aliases: list[str] = []


@router.post("/knowledge/terms", status_code=201)
def add_term(body: Term, c: Container = Depends(container)):
    c.knowledge.add_term(body.term, body.definition, body.aliases)
    return {"status": "learned", "term": body.term}


class Rule(BaseModel):
    rule: str
    scope: str = "global"


@router.post("/knowledge/rules", status_code=201)
def add_rule(body: Rule, c: Container = Depends(container)):
    c.knowledge.add_rule(body.rule, body.scope)
    return {"status": "learned"}


class Clarification(BaseModel):
    question: str
    answer: str
    project_id: str = ""
    signature: str = ""


@router.post("/knowledge/clarifications", status_code=201)
def add_clarification(body: Clarification, c: Container = Depends(container)):
    """Store a user clarification — it will never be asked again for a
    similar dataset."""
    c.knowledge.remember_clarification(body.question, body.answer,
                                       body.signature, body.project_id)
    return {"status": "remembered"}

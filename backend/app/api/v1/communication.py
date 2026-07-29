"""Communications APIs (Phase 2 #12/#13) — email as enterprise knowledge.

Read-only inbox/search endpoints that return each message *already analysed*
(category, entities, action items, decisions, deadlines, risks), the provider
status surface (Outlook, Gmail, Teams …), an analyzer for an arbitrary message,
and a context-grounded draft endpoint. Nothing is ever sent from here — drafting
returns a draft; an actual send still goes through the approval/Action Queue.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.api.deps import container
from app.communication.providers import ProviderNotConfigured
from app.core.container import Container

router = APIRouter(tags=["communication"])


@router.get("/communication/providers")
def communication_providers(c: Container = Depends(container)):
    """Every registered channel and whether it is configured — the
    Communications surface uses this to show what is live vs. what needs setup."""
    return {"providers": c.providers.describe_all()}


def _read(c: Container, provider: str, reader, *args) -> dict:
    """Shared inbox/search handler: pick the email provider, read, analyse, and
    degrade gracefully with a clear reason when it is not configured."""
    try:
        prov = (c.providers.get_by_name("email", provider) if provider
                else c.providers.get("email"))
    except ProviderNotConfigured as exc:
        return {"available": False, "reason": str(exc), "messages": []}
    if not prov.available:
        return {"available": False, "reason": prov.unavailable_reason,
                "messages": []}
    try:
        raw = getattr(prov, reader)(*args)
    except ProviderNotConfigured as exc:
        return {"available": False, "reason": str(exc), "messages": []}
    messages = c.email_intelligence.analyze_many(raw)
    return {"available": True, "provider": prov.name, "count": len(messages),
            "messages": messages}


@router.get("/communication/inbox")
def communication_inbox(provider: str = "", folder: str = "inbox",
                        top: int = 25, c: Container = Depends(container)):
    """Recent mail, each message enriched with extracted business signal."""
    return _read(c, provider, "read_messages", folder, top)


@router.get("/communication/search")
def communication_search(q: str, provider: str = "", top: int = 25,
                         c: Container = Depends(container)):
    """Search mail (provider-native query) with the same enrichment."""
    return _read(c, provider, "search_messages", q, top)


class AnalyzeRequest(BaseModel):
    subject: str = ""
    body: str = ""
    sender: str = ""
    id: str = ""


@router.post("/communication/analyze")
def communication_analyze(req: AnalyzeRequest,
                          c: Container = Depends(container)):
    """Analyse an arbitrary email (e.g. pasted or uploaded) without a provider —
    the same deterministic extraction used for inbox messages."""
    return c.email_intelligence.analyze(
        {"id": req.id, "subject": req.subject, "body": req.body,
         "from": req.sender})


class DraftRequest(BaseModel):
    kind: str = "management_update"
    context: dict = {}


@router.post("/communication/draft")
def communication_draft(req: DraftRequest, c: Container = Depends(container)):
    """Draft an email grounded in supplied business context (real figures,
    entities, next steps). Returns a draft only — never sends."""
    return c.email_intelligence.draft(req.kind, req.context or {})

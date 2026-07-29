"""Enterprise Copilot APIs.

The executive's conversational surface over the whole platform. APIs only —
no business logic in this module.

Distinct from ``/projects/{id}/copilot/chat``, which answers questions about
one project's analytics and is unchanged. This surface answers questions about
the *enterprise*: products, portfolio, risks, approvals, strategy.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

from app.api.deps import container
from app.core.container import Container

router = APIRouter(tags=["copilot"])


def _layer(c: Container):
    if c.copilot_layer is None:
        raise HTTPException(status_code=503,
                            detail="The Enterprise Copilot is disabled")
    return c.copilot_layer


# ------------------------------------------------------------------ chat
class Chat(BaseModel):
    message: str = Field(..., min_length=1)
    conversation_id: str = ""
    owner: str = ""


@router.post("/copilot/chat")
def chat(body: Chat, c: Container = Depends(container)):
    """Ask the platform anything. Returns the answer plus everything behind
    it: the detected intent, the execution plan, the evidence gathered, the
    validation verdict, and the suggested actions."""
    try:
        res = _layer(c).copilot.chat(body.message,
                                     conversation_id=body.conversation_id,
                                     owner=body.owner)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))
    # V10.0: never expose the internal day/week/phase clock to end users —
    # rewrite it into business language; and remember the question (learning).
    try:
        from app.analyst.timeline import BusinessTimeline
        tl = BusinessTimeline.from_container(c)
        if isinstance(res, dict) and res.get("answer"):
            res["answer"] = tl.humanize(res["answer"])
        ls = getattr(c, "learning_store", None)
        if ls:
            ls.record_question(body.message)
    except Exception:  # noqa: BLE001 — polish/learning never breaks the answer
        pass
    return res


@router.get("/copilot")
def workspace(c: Container = Depends(container)):
    """The Copilot Workspace: conversations, pinned threads, suggested
    questions, recent reports, and the configured provider."""
    return _layer(c).workspace()


# --------------------------------------------------------------- context
@router.get("/copilot/context")
def context(q: str = "", c: Container = Depends(container)):
    """What the copilot would bring to a request: the intent it detects, the
    plan it would run, the context it would assemble, and the evidence it
    would gather. The honest answer to "what do you actually know?"."""
    return _layer(c).copilot.context_for(q)


@router.get("/copilot/intents")
def intents(c: Container = Depends(container)):
    """The intents the copilot understands and the routes behind them."""
    layer = _layer(c)
    return {"intents": layer.intent.vocabulary(),
            "routes": layer.planner.routes()}


@router.get("/copilot/suggestions")
def suggestions(limit: int = Query(6, ge=1, le=20),
                c: Container = Depends(container)):
    """What is worth asking right now, from the platform's actual state."""
    return {"suggestions": _layer(c).copilot.suggested_questions(limit)}


# --------------------------------------------------------- conversations
@router.get("/copilot/conversations")
def conversations(pinned: bool = False, owner: str = "",
                  limit: int = Query(50, ge=1, le=200),
                  c: Container = Depends(container)):
    layer = _layer(c)
    return {"conversations": layer.conversations.conversations(
                pinned_only=pinned, owner=owner, limit=limit),
            "stats": layer.conversations.stats()}


@router.post("/copilot/conversations", status_code=201)
def start_conversation(title: str = "", owner: str = "",
                       c: Container = Depends(container)):
    return _layer(c).conversations.start(title=title, owner=owner)


@router.get("/copilot/conversations/{conversation_id}")
def conversation(conversation_id: str, c: Container = Depends(container)):
    layer = _layer(c)
    found = layer.conversations.get(conversation_id)
    if found is None:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return {"conversation": found,
            "messages": layer.conversations.messages(conversation_id)}


class ConversationUpdate(BaseModel):
    pinned: bool | None = None
    title: str | None = None


@router.patch("/copilot/conversations/{conversation_id}")
def update_conversation(conversation_id: str, body: ConversationUpdate,
                        c: Container = Depends(container)):
    layer = _layer(c)
    if layer.conversations.get(conversation_id) is None:
        raise HTTPException(status_code=404, detail="Conversation not found")
    updated = None
    if body.title is not None:
        updated = layer.conversations.rename(conversation_id, body.title)
    if body.pinned is not None:
        updated = layer.conversations.pin(conversation_id, body.pinned)
    return updated or layer.conversations.get(conversation_id)


@router.delete("/copilot/conversations/{conversation_id}", status_code=204)
def delete_conversation(conversation_id: str,
                        c: Container = Depends(container)):
    if not _layer(c).conversations.delete(conversation_id):
        raise HTTPException(status_code=404, detail="Conversation not found")


# --------------------------------------------------------------- history
@router.get("/copilot/history")
def history(conversation_id: str = "", limit: int = Query(50, ge=1, le=200),
            c: Container = Depends(container)):
    """One conversation's messages, or every conversation's summary."""
    layer = _layer(c)
    if conversation_id:
        if layer.conversations.get(conversation_id) is None:
            raise HTTPException(status_code=404,
                                detail="Conversation not found")
        return {"conversation_id": conversation_id,
                "messages": layer.conversations.messages(conversation_id,
                                                         limit=limit)}
    return {"conversations": layer.conversations.conversations(limit=limit)}


# ---------------------------------------------------------------- search
@router.get("/copilot/search")
def search(q: str = Query(..., min_length=1),
           limit: int = Query(20, ge=1, le=100),
           c: Container = Depends(container)):
    """Search past conversations by what was said in them."""
    return {"query": q,
            "results": _layer(c).conversations.search(q, limit=limit)}


# ----------------------------------------------------------- preferences
@router.get("/copilot/preferences")
def preferences(owner: str = "", c: Container = Depends(container)):
    """What this executive keeps asking about — counted, never inferred."""
    return _layer(c).conversations.preferences(owner=owner)


class Preference(BaseModel):
    key: str
    value: object
    owner: str = ""


@router.post("/copilot/preferences", status_code=201)
def set_preference(body: Preference, c: Container = Depends(container)):
    return _layer(c).conversations.set_preference(body.key, body.value,
                                                  owner=body.owner)


class Clarification(BaseModel):
    question: str
    answer: str
    conversation_id: str = ""


@router.post("/copilot/clarifications", status_code=201)
def record_clarification(body: Clarification,
                         c: Container = Depends(container)):
    """An answer the executive gives the platform. It goes to the Knowledge
    Store, which guarantees it is never asked again."""
    recorded = _layer(c).conversations.record_clarification(
        body.question, body.answer, conversation_id=body.conversation_id)
    if not recorded:
        raise HTTPException(status_code=422,
                            detail="The clarification could not be recorded")
    return {"recorded": True, "question": body.question}

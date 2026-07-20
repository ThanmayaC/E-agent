"""Conversation Memory — the executive's thread with the platform.

    conversation history · clarifications · follow-up questions
    previous recommendations · pending decisions · executive preferences

Two things make this more than a chat log:

- **Follow-ups resolve.** "Why did it fall?" only means something after "how
  is Payments doing?". Recent turns travel into the next prompt for reference
  resolution only — never as a source of facts, because a model's own earlier
  sentence is not evidence.
- **Preferences persist.** What an executive keeps asking about is what they
  care about; the copilot learns that deterministically (by counting subjects
  and intents), not by asking a model to summarise a personality.

Clarifications the executive answers are pushed into the *Knowledge Store*,
not kept here — an answer the business gives once belongs to the organization,
and the platform already has a home for that which never asks twice.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.copilot.store import CopilotStore, new_id, now_iso

logger = get_logger(__name__)

ROLES = ("user", "assistant")
MAX_MESSAGES = 500
MAX_TITLE = 80
# How many turns travel into the next prompt for reference resolution.
CONTEXT_TURNS = 6


class ConversationMemory:
    """Enterprise conversations, their history, and what they taught us."""

    def __init__(self, store: CopilotStore, knowledge=None):
        self._store = store
        self._knowledge = knowledge

    # ------------------------------------------------------ conversations
    def start(self, title: str = "", owner: str = "") -> dict:
        conversation = {
            "conversation_id": new_id("cnv"),
            "title": (title or "New conversation")[:MAX_TITLE],
            "owner": owner[:120], "pinned": False, "message_count": 0,
            "intents": {}, "subjects": {}, "last_message": "",
            "created_at": now_iso(), "updated_at": now_iso(),
        }
        return self._store.append("conversations", conversation)

    def get(self, conversation_id: str) -> dict | None:
        return self._store.get("conversations", "conversation_id",
                               conversation_id)

    def ensure(self, conversation_id: str = "", title: str = "",
               owner: str = "") -> dict:
        """The conversation to append to: the one named, or a new one. A
        conversation id that no longer exists starts a fresh thread rather
        than failing — an executive mid-question should never see a 404."""
        if conversation_id:
            existing = self.get(conversation_id)
            if existing is not None:
                return existing
        return self.start(title=title, owner=owner)

    def conversations(self, pinned_only: bool = False, owner: str = "",
                      limit: int = 50) -> list[dict]:
        items = self._store.read("conversations")
        if pinned_only:
            items = [c for c in items if c["pinned"]]
        if owner:
            items = [c for c in items if c["owner"] == owner]
        return sorted(items, key=lambda c: c["updated_at"],
                      reverse=True)[:limit]

    def pin(self, conversation_id: str, pinned: bool = True) -> dict | None:
        return self._store.update("conversations", "conversation_id",
                                  conversation_id, {"pinned": pinned})

    def rename(self, conversation_id: str, title: str) -> dict | None:
        return self._store.update("conversations", "conversation_id",
                                  conversation_id, {"title": title[:MAX_TITLE]})

    def delete(self, conversation_id: str) -> bool:
        with self._store.mutate("messages") as messages:
            messages[:] = [m for m in messages
                           if m["conversation_id"] != conversation_id]
        return self._store.delete("conversations", "conversation_id",
                                  conversation_id)

    # ----------------------------------------------------------- messages
    def append(self, conversation_id: str, role: str, content: str,
               meta: dict | None = None) -> dict:
        if role not in ROLES:
            raise ValueError(f"Unknown message role: {role}")
        message = {"message_id": new_id("msg"),
                   "conversation_id": conversation_id, "role": role,
                   "content": str(content)[:8000], "meta": meta or {},
                   "at": now_iso()}
        self._store.append("messages", message, cap=MAX_MESSAGES)
        self._touch(conversation_id, role, content, meta or {})
        return message

    def messages(self, conversation_id: str, limit: int = 50) -> list[dict]:
        items = [m for m in self._store.read("messages")
                 if m["conversation_id"] == conversation_id]
        return items[-limit:]

    def recent_turns(self, conversation_id: str) -> list[dict]:
        """The turns that travel into the next prompt — for resolving "it"
        and "that product", never as evidence."""
        return [{"role": m["role"], "content": m["content"][:300]}
                for m in self.messages(conversation_id, limit=CONTEXT_TURNS)]

    def _touch(self, conversation_id: str, role: str, content: str,
               meta: dict) -> None:
        """Keep the conversation's summary current, and learn from it: what
        the executive asks about repeatedly is what they care about."""
        with self._store.mutate("conversations") as conversations:
            for conversation in conversations:
                if conversation["conversation_id"] != conversation_id:
                    continue
                conversation["message_count"] += 1
                conversation["updated_at"] = now_iso()
                if role == "user":
                    conversation["last_message"] = str(content)[:200]
                    if conversation["title"] == "New conversation":
                        conversation["title"] = str(content)[:MAX_TITLE]
                    intent = meta.get("intent")
                    if intent:
                        conversation["intents"][intent] = \
                            conversation["intents"].get(intent, 0) + 1
                    subject = meta.get("subject")
                    if subject:
                        conversation["subjects"][subject] = \
                            conversation["subjects"].get(subject, 0) + 1
                return

    # ------------------------------------------------- clarifications etc.
    def record_clarification(self, question: str, answer: str,
                             conversation_id: str = "") -> bool:
        """An answer the executive gives belongs to the organization, not to
        this thread — it goes to the Knowledge Store, which already guarantees
        it is never asked again."""
        if self._knowledge is None or not question.strip():
            return False
        try:
            self._knowledge.remember_clarification(
                question.strip(), answer.strip(), kind="copilot",
                signature=f"copilot:{question.strip().lower()[:80]}")
            return True
        except Exception:  # noqa: BLE001 — learning degrades, never fails a chat
            logger.exception("Recording a copilot clarification failed")
            return False

    def preferences(self, owner: str = "") -> dict[str, Any]:
        """What this executive keeps asking about — counted, never inferred by
        a model."""
        conversations = self.conversations(owner=owner, limit=200)
        intents: dict[str, int] = {}
        subjects: dict[str, int] = {}
        for conversation in conversations:
            for intent, count in (conversation.get("intents") or {}).items():
                intents[intent] = intents.get(intent, 0) + count
            for subject, count in (conversation.get("subjects") or {}).items():
                subjects[subject] = subjects.get(subject, 0) + count
        stored = self._store.get("preferences", "owner", owner or "_default")
        return {
            "owner": owner or "_default",
            "frequent_intents": sorted(intents.items(), key=lambda kv: -kv[1])[:5],
            "frequent_subjects": sorted(subjects.items(),
                                        key=lambda kv: -kv[1])[:5],
            "conversations": len(conversations),
            "explicit": (stored or {}).get("preferences", {}),
        }

    def set_preference(self, key: str, value: Any,
                       owner: str = "") -> dict:
        """An explicitly stated preference ("always show me revenue first")."""
        owner = owner or "_default"
        with self._store.mutate("preferences") as items:
            for item in items:
                if item["owner"] == owner:
                    item["preferences"][key] = value
                    item["updated_at"] = now_iso()
                    return item
            record = {"owner": owner, "preferences": {key: value},
                      "created_at": now_iso(), "updated_at": now_iso()}
            items.append(record)
            return record

    # ------------------------------------------------------------- search
    def search(self, query: str, limit: int = 20) -> list[dict]:
        """Find a past conversation by what was said in it."""
        needle = str(query).strip().lower()
        if not needle:
            return []
        titles = {c["conversation_id"]: c for c in
                  self._store.read("conversations")}
        hits: dict[str, dict] = {}
        for message in self._store.read("messages"):
            if needle not in message["content"].lower():
                continue
            conversation = titles.get(message["conversation_id"])
            if conversation is None:
                continue
            hit = hits.setdefault(message["conversation_id"], {
                "conversation_id": message["conversation_id"],
                "title": conversation["title"],
                "pinned": conversation["pinned"],
                "updated_at": conversation["updated_at"],
                "matches": []})
            if len(hit["matches"]) < 3:
                hit["matches"].append({"role": message["role"],
                                       "excerpt": _excerpt(message["content"],
                                                           needle),
                                       "at": message["at"]})
        return sorted(hits.values(), key=lambda h: h["updated_at"],
                      reverse=True)[:limit]

    def stats(self) -> dict:
        conversations = self._store.read("conversations")
        return {"conversations": len(conversations),
                "pinned": sum(1 for c in conversations if c["pinned"]),
                "messages": len(self._store.read("messages"))}

    def prune(self, keep: int = 200) -> dict[str, int]:
        """Keep the store bounded: unpinned, oldest conversations age out.
        A pinned conversation is never pruned — pinning is the executive
        saying "this one matters"."""
        conversations = self._store.read("conversations")
        if len(conversations) <= keep:
            return {"pruned": 0}
        ordered = sorted(conversations, key=lambda c: c["updated_at"],
                         reverse=True)
        keeping = {c["conversation_id"] for c in ordered[:keep]}
        keeping |= {c["conversation_id"] for c in conversations if c["pinned"]}
        dropped = [c["conversation_id"] for c in conversations
                   if c["conversation_id"] not in keeping]
        if not dropped:
            return {"pruned": 0}
        with self._store.mutate("conversations") as items:
            items[:] = [c for c in items
                        if c["conversation_id"] in keeping]
        with self._store.mutate("messages") as items:
            items[:] = [m for m in items
                        if m["conversation_id"] in keeping]
        return {"pruned": len(dropped)}


def _excerpt(content: str, needle: str, width: int = 80) -> str:
    index = content.lower().find(needle)
    start = max(0, index - width // 2)
    return ("…" if start else "") + content[start:start + width].strip() + "…"

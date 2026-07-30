"""Enterprise Copilot — the executive's way into the platform.

    intent → plan → context → evidence → prompt → LLM → validate
           → suggested actions → remember

Its job is **orchestration, not calculation**. Every fact in an answer was
produced by a module that already existed; the copilot decides which of them to
ask, gathers what they say, and has the reasoning model narrate it. It computes
no analytics, runs no second workflow engine, and holds no truth of its own.

Two properties are load-bearing:

- **Evidence precedes the model.** Facts are gathered deterministically before
  a prompt is built, so the model narrates a closed set rather than deciding
  what is true.
- **The pipeline degrades, it does not fail.** No LLM configured, a module
  absent, a source erroring — each removes something from the answer and says
  so. An executive gets the evidence and an honest account of what is missing,
  which beats an error page and beats a fabrication.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.copilot.actions import SuggestedActionsBuilder
from app.copilot.context import ContextBuilder
from app.copilot.conversations import ConversationMemory
from app.copilot.evidence import EvidenceCollector
from app.copilot.intent import IntentClassifier
from app.copilot.planner import RequestPlanner
from app.copilot.router import LLMRouter
from app.copilot.store import now_iso
from app.copilot.validator import ResponseValidator, Validation

logger = get_logger(__name__)

# Deterministic intents answer from the platform's own state; the model is not
# asked to narrate what a module already stated precisely.
DETERMINISTIC_OUTPUTS = ("approval_summary", "task_confirmation",
                         "workflow_status", "search_results",
                         "decision_record")


class EnterpriseCopilot:
    """Understands an executive request and orchestrates the platform."""

    def __init__(self, intent: IntentClassifier, planner: RequestPlanner,
                 context: ContextBuilder, evidence: EvidenceCollector,
                 router: LLMRouter, validator: ResponseValidator,
                 conversations: ConversationMemory,
                 actions: SuggestedActionsBuilder, prompt_agent,
                 product=None, search=None, bus=None, orchestrator=None):
        self._intent = intent
        self._planner = planner
        self._context = context
        self._evidence = evidence
        self._router = router
        self._validator = validator
        self._conversations = conversations
        self._actions = actions
        self._prompts = prompt_agent
        self._product = product
        self._search = search
        self._bus = bus
        # The Enterprise AI Orchestrator (V11). When wired, it classifies the
        # question and routes it to the analytics/ML/forecast/recommendation
        # engines, merging their evidence into the set the model reasons over.
        # None = the copilot behaves exactly as before (per-intent evidence).
        self._orchestrator = orchestrator

    def attach_orchestrator(self, orchestrator) -> None:
        self._orchestrator = orchestrator

    def attach_bus(self, bus) -> None:
        self._bus = bus

    # ---------------------------------------------------------------- chat
    def chat(self, message: str, conversation_id: str = "",
             owner: str = "") -> dict[str, Any]:
        """Answer one executive request end to end."""
        if not str(message).strip():
            raise ValueError("A copilot request needs a message")

        conversation = self._conversations.ensure(conversation_id,
                                                  title=message, owner=owner)
        conversation_id = conversation["conversation_id"]

        # 1. Intent ------------------------------------------------------
        intent = self._intent.classify(message)
        # 2. Plan --------------------------------------------------------
        plan = self._planner.plan(intent, message)
        # 3. Context -----------------------------------------------------
        context = self._context.build(plan, conversation_id=conversation_id)
        # 4. Evidence (always before the model) --------------------------
        evidence = self._evidence.collect(plan, message)

        # 4b. Orchestrate — classify the question and route it to the engines
        #     that actually own the answer (analytics/ML/forecast/…), merging
        #     their evidence into the set the model reasons over. This is what
        #     lets "UPI trends July 1-20" answer from the KPI series instead of
        #     returning "no evidence found". Only for LLM-narrated answers;
        #     deterministic outputs (approvals, tasks) do not need engines.
        orchestration = None
        if (self._orchestrator is not None and plan.needs_llm
                and plan.expected_output not in DETERMINISTIC_OUTPUTS):
            orchestration = self._orchestrate(evidence, message, intent)

        # 5-7. Prompt → LLM → validate -----------------------------------
        if plan.needs_llm and plan.expected_output not in DETERMINISTIC_OUTPUTS:
            response, validation = self._reason(message, plan, context,
                                                evidence, conversation_id)
        else:
            response, validation = self._deterministic(plan, evidence)

        # 8. Suggested actions -------------------------------------------
        suggestions = self._actions.build(plan, evidence, response)

        answer = {
            "conversation_id": conversation_id,
            "message": message,
            "answer": response["answer"],
            "status": response["status"],
            "confidence": response["confidence"],
            "intent": intent.describe(),
            "plan": plan.describe(),
            "evidence": {
                **evidence.describe(),
                "items": [{"id": i["id"], "kind": i["kind"],
                           "summary": i["summary"]}
                          for i in evidence.items[:12]],
                "cited": response.get("evidence_ids", []),
            },
            "cited_facts": response.get("cited_facts", []),
            "limitations": response.get("limitations", []),
            "validation": validation.describe(),
            "context_gaps": context.get("unavailable", []),
            "provider": {"provider": response.get("provider", ""),
                         "model": response.get("model", "")},
            "orchestration": orchestration,
            **suggestions,
            "answered_at": now_iso(),
        }

        # 9. Remember ----------------------------------------------------
        self._remember(conversation_id, message, answer, intent)
        self._announce(answer)
        return answer

    # ------------------------------------------------------- orchestrate
    def _orchestrate(self, evidence, message: str, intent) -> dict | None:
        """Run the Enterprise AI Orchestrator and merge its engine evidence
        into ``evidence`` (deduped by id, so a document the plan already pulled
        is not added twice). Returns the observability record for the answer;
        never fails the chat — a broken engine degrades to no extra evidence."""
        try:
            result = self._orchestrator.run(message, intent)
        except Exception:  # noqa: BLE001 — orchestration never fails an answer
            logger.exception("Orchestrator run failed")
            return None
        existing = evidence.ids
        added_ids: list[str] = []
        for item in result.evidence:
            item_id = item.get("id")
            if not item_id or item_id in existing:
                continue
            payload = {k: v for k, v in item.items()
                       if k not in ("id", "kind", "summary")}
            evidence.add(item["kind"], item_id, item.get("summary", ""),
                         payload)
            existing.add(item_id)
            added_ids.append(item_id)

        # The routed engines produced the evidence most directly relevant to the
        # question — the analytics KPI series, the forecast, the ML result. The
        # prompt is budgeted front-first, so this evidence must LEAD, or it is
        # dropped behind ~90 background facts and the model answers "no data"
        # despite holding the series. Move the merged engine items to the front,
        # preserving the router's engine order (analytics first).
        if added_ids:
            order = {eid: i for i, eid in enumerate(added_ids)}
            lead = sorted((it for it in evidence.items
                           if it["id"] in order), key=lambda it: order[it["id"]])
            rest = [it for it in evidence.items if it["id"] not in order]
            evidence.items = lead + rest

        record = result.describe()
        record["evidence_merged"] = len(added_ids)
        return record

    # ------------------------------------------------------------ reason
    def _reason(self, message: str, plan, context: dict, evidence,
                conversation_id: str) -> tuple[dict, Any]:
        """Build the prompt, route it, and validate what comes back."""
        prompt = self._prompts.enterprise_copilot_prompt(
            question=message, intent=plan.intent,
            business_context=_narrow(context), evidence=evidence.items,
            output_format=plan.expected_output,
            conversation=self._conversations.recent_turns(conversation_id)
            or None,
            business_rules=context.get("business_rules") or [],
            weak_evidence=evidence.is_weak)
        response = self._router.route(prompt)
        return self._validator.validate(response, evidence,
                                        context.get("business_rules") or [])

    def _deterministic(self, plan, evidence) -> tuple[dict, Any]:
        """Answer from the platform's own state, with no model involved.

        Approvals, tasks, workflows, search, and decisions are things the
        platform *knows*, stated precisely by the module that owns them.
        Asking a language model to rephrase them adds latency and a chance of
        error, and buys nothing.
        """
        lines = [item["summary"] for item in evidence.items[:8]]
        if lines:
            answer = (f"{len(evidence.items)} item(s) found:\n"
                      + "\n".join(f"- {line}" for line in lines))
            confidence = 1.0  # the platform's own state, not an inference
        else:
            answer = ("Nothing matches that in the platform's current state."
                      + (f" ({'; '.join(evidence.missing[:2])})"
                         if evidence.missing else ""))
            confidence = 1.0
        response = {"status": "ok", "answer": answer,
                    "cited_facts": lines[:5],
                    "evidence_ids": [i["id"] for i in evidence.items[:8]],
                    "confidence": confidence, "limitations": evidence.missing,
                    "suggested_actions": [], "provider": "deterministic",
                    "model": ""}
        validation = Validation(verdict="verified", confidence=confidence,
                                original_confidence=confidence,
                                verified_ids=response["evidence_ids"])
        return response, validation

    # ---------------------------------------------------------- remember
    def _remember(self, conversation_id: str, message: str, answer: dict,
                  intent) -> None:
        try:
            self._conversations.append(
                conversation_id, "user", message,
                meta={"intent": intent.intent, "subject": intent.subject})
            self._conversations.append(
                conversation_id, "assistant", answer["answer"],
                meta={"confidence": answer["confidence"],
                      "verdict": answer["validation"]["verdict"],
                      "evidence": answer["evidence"]["total"],
                      "provider": answer["provider"]["provider"]})
        except Exception:  # noqa: BLE001 — memory degrades, never fails a chat
            logger.exception("Copilot conversation persistence failed")

    def _announce(self, answer: dict) -> None:
        if self._bus is None:
            return
        try:
            self._bus.publish("CopilotAnswered", {
                "conversation_id": answer["conversation_id"],
                "intent": answer["intent"]["intent"],
                "confidence": answer["confidence"],
                "verdict": answer["validation"]["verdict"],
                "evidence": answer["evidence"]["total"]},
                source="enterprise_copilot")
        except Exception:  # noqa: BLE001 — announcing never fails an answer
            logger.exception("Copilot event publication failed")

    # ------------------------------------------------------------ surface
    def refresh_subjects(self) -> dict[str, int]:
        """Teach the classifier the products the platform actually knows, so
        "how is Payments doing?" resolves to a real subject. Runs on the
        scheduler; never hardcoded."""
        if self._product is None:
            return {"subjects": 0}
        names = [p["name"] for p in self._product.catalog.products(limit=500)]
        self._intent.set_subjects(names)
        return {"subjects": len(names)}

    def context_for(self, message: str = "") -> dict[str, Any]:
        """What the copilot would bring to this request — the /copilot/context
        surface. Useful on its own, and the honest answer to "what do you
        actually know?"."""
        intent = self._intent.classify(message or "what is our position?")
        plan = self._planner.plan(intent, message)
        context = self._context.build(plan)
        evidence = self._evidence.collect(plan, message)
        return {"intent": intent.describe(), "plan": plan.describe(),
                "context": context, "evidence": evidence.describe(),
                "evidence_items": [{"id": i["id"], "kind": i["kind"],
                                    "summary": i["summary"]}
                                   for i in evidence.items[:20]],
                "provider": self._router.describe()}

    def suggested_questions(self, limit: int = 6) -> list[dict]:
        """What is worth asking right now, from the platform's actual state —
        not a static list. A suggestion points at something real: a product
        that needs attention, an approval that is waiting, a risk that is
        open."""
        suggestions: list[dict] = []
        if self._product is not None:
            try:
                overview = self._product.overview()
                for entry in overview.get("attention", [])[:2]:
                    suggestions.append({
                        "question": f"Why does {entry['product']} need "
                                    f"attention?",
                        "intent": "explanation", "reason": entry.get(
                            "priority_reason", "")})
                for risk in overview.get("top_risks", [])[:2]:
                    suggestions.append({
                        "question": f"What should we do about "
                                    f"{risk['product']}?",
                        "intent": "recommendation",
                        "reason": risk["finding"][:120]})
                if overview.get("products", {}).get("total"):
                    suggestions.append({
                        "question": "How is the product portfolio performing?",
                        "intent": "question", "reason": "portfolio overview"})
            except Exception:  # noqa: BLE001 — suggestions are a nicety
                logger.exception("Building suggested questions failed")
        suggestions.append({"question": "What needs my approval?",
                            "intent": "approval",
                            "reason": "pending decisions"})
        suggestions.append({"question": "Give me the board brief",
                            "intent": "executive_brief",
                            "reason": "executive summary"})
        return suggestions[:limit]

    def orchestration_for(self, message: str) -> dict[str, Any]:
        """What the orchestrator would do with this question — the classified
        query, the engines it would run, each with its SQL/model/documents and
        timing. The /copilot/orchestration surface (Phase 14)."""
        if self._orchestrator is None:
            return {"enabled": False,
                    "note": "the Enterprise AI Orchestrator is disabled"}
        intent = self._intent.classify(message or "what is our position?")
        record = self._orchestrator.context_for(message, intent)
        return {"enabled": True, "intent": intent.describe(), **record}

    def orchestrator_overview(self) -> dict[str, Any]:
        """The registered engines and query categories, for the UI."""
        if self._orchestrator is None:
            return {"enabled": False}
        return {"enabled": True, **self._orchestrator.describe()}

    def stats(self) -> dict[str, Any]:
        return {"conversations": self._conversations.stats(),
                "provider": self._router.describe(),
                "intents": len(self._intent.vocabulary()),
                "orchestrator": self._orchestrator is not None}


def _narrow(context: dict) -> dict:
    """The business context, minus the copilot's own bookkeeping.

    ``unavailable`` and the conversation are operational detail; sending them
    to the model wastes tokens and invites it to narrate its own plumbing.
    """
    return {k: v for k, v in context.items()
            if k not in ("unavailable", "recent_conversation")}

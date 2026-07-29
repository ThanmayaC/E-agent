"""Prompt Generation Agent.

Prompts are never hardcoded per call site. This agent observes the schema,
the analytics, the business context, and the enterprise knowledge store, then
generates the best prompt for the reasoning model. When its confidence in the
available context is low it emits clarification questions instead of letting
the model guess — and questions the organization already answered are never
asked again (they are recalled from the knowledge store and injected as
facts).
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any

from app.agents.base import AgentPlan, AgentRequest, AgentResult, BaseAgent
from app.core.logging import get_logger
from app.knowledge.store import KnowledgeStore
from app.memory.manager import MemoryManager, WorkingMemory
from app.tools.registry import ToolRegistry

logger = get_logger(__name__)

# Context budget (Enterprise RAG / Prompt Builder, production hardening).
# The copilot prompt must never carry the *entire* evidence set or business
# context to the model — an oversized prompt is the single biggest cause of
# local-model timeouts. These caps bound the serialized evidence and business
# context (characters ≈ tokens×4). Overridable per call and, at the call site,
# from settings (llm_max_prompt_chars). Rough guide: 12000 chars ≈ 3000 tokens.
DEFAULT_EVIDENCE_BUDGET_CHARS = 12000
DEFAULT_CONTEXT_BUDGET_CHARS = 6000


def _budget_evidence(evidence: list[dict], max_chars: int) -> tuple[list[dict], int]:
    """Keep evidence items in their given (relevance) order until the character
    budget is spent. Returns the kept items and how many were dropped — so only
    the minimum required evidence reaches the LLM, and the drop is observable."""
    kept: list[dict] = []
    used = 0
    for item in evidence:
        size = len(json.dumps(item, default=str))
        if kept and used + size > max_chars:
            break
        kept.append(item)
        used += size
    return kept, len(evidence) - len(kept)


def _cap_json(obj: Any, max_chars: int) -> str:
    """Serialize, and if it exceeds the budget drop the largest top-level keys
    (dicts) until it fits, marking what was omitted rather than sending it all."""
    text = json.dumps(obj, default=str)
    if len(text) <= max_chars or not isinstance(obj, dict):
        return text
    trimmed = dict(obj)
    omitted: list[str] = []
    # drop biggest keys first until within budget
    for key in sorted(trimmed, key=lambda k: len(json.dumps(trimmed[k], default=str)),
                      reverse=True):
        if len(json.dumps(trimmed, default=str)) <= max_chars:
            break
        omitted.append(key)
        trimmed.pop(key, None)
    if omitted:
        trimmed["_omitted_for_budget"] = omitted
    return json.dumps(trimmed, default=str)

# Prompts live in the Prompt Registry (V2.2), not in this module: an
# enterprise must be able to read every instruction the platform gives a model
# without reading Python, and must be able to version and own that wording.
# These names are re-exported so existing importers keep working.
from app.prompts.domains.copilot import (  # noqa: E402
    CONFIDENCE_STRONG, CONFIDENCE_WEAK,
)
from app.prompts.domains.reports import (  # noqa: E402
    ENTERPRISE_NOTE, INSUFFICIENT_DATA_STATEMENT, REPORT_SCHEMA,
)

__all__ = ["GeneratedPrompt", "INSUFFICIENT_DATA_STATEMENT",
           "PromptGenerationAgent", "REPORT_SCHEMA"]


@dataclass
class GeneratedPrompt:
    system: str
    user: str
    confidence: float = 1.0
    clarification_questions: list[str] = field(default_factory=list)


class PromptGenerationAgent(BaseAgent):
    name = "prompt_generator"
    role = ("Observes schema, analytics, and enterprise knowledge to generate "
            "the best prompt for the reasoning model, asking clarification "
            "questions when confidence is low")

    def __init__(self, tools: ToolRegistry | None = None,
                 memory: MemoryManager | None = None,
                 knowledge: KnowledgeStore | None = None,
                 min_confidence: float = 0.5, prompts=None):
        # Usable standalone (tests, degraded mode) or fully wired via DI.
        self.tools = tools
        self.memory = memory
        self.knowledge = knowledge
        self.min_confidence = min_confidence
        # V2.2: prompts come from the Prompt Registry, not from this module.
        # A registry is built by default so standalone use keeps working.
        if prompts is None:
            from app.prompts.registry import PromptRegistry
            prompts = PromptRegistry()
        self.prompts = prompts

    # -------------------------------------------------------- agent hooks
    def plan(self, request: AgentRequest, understanding: dict[str, Any],
             working: WorkingMemory) -> AgentPlan:
        return AgentPlan(steps=[f"generate {request.payload.get('kind', 'report')} prompt"])

    def execute(self, request: AgentRequest, plan: AgentPlan,
                working: WorkingMemory) -> AgentResult:
        kind = request.payload.get("kind", "report")
        context = request.payload.get("context", {})
        if kind == "copilot":
            prompt = self.copilot_prompt(request.payload.get("question", request.goal),
                                         context,
                                         request.payload.get("conversation", []))
        else:
            prompt = self.report_prompt(context)
        return AgentResult(status="ok", output=prompt, confidence=prompt.confidence)

    # ---------------------------------------------------- prompt building
    def report_prompt(self, context: dict[str, Any]) -> GeneratedPrompt:
        confidence, questions = self._assess(context)
        user = self.prompts.render(
            "reports.executive_analysis",
            enterprise_note=(ENTERPRISE_NOTE if "enterprise" in context else ""),
            context_json=json.dumps(context, default=str),
            knowledge_block=self._knowledge_block(context),
            schema=REPORT_SCHEMA)
        return GeneratedPrompt(system=self._system(), user=user,
                               confidence=confidence,
                               clarification_questions=questions)

    def copilot_prompt(self, question: str, context: dict[str, Any],
                       conversation: list[dict] | None = None) -> GeneratedPrompt:
        confidence, questions = self._assess(context)
        history = ""
        if conversation:
            turns = [f"{t.get('role')}: {str(t.get('content'))[:300]}" for t in conversation[-6:]]
            history = "Recent conversation (for reference resolution only):\n" + "\n".join(turns) + "\n\n"
        user = self.prompts.render(
            "copilot.project_answer", question=repr(question), history=history,
            context_json=json.dumps(context, default=str),
            knowledge_block=self._knowledge_block(context))
        return GeneratedPrompt(system=self._system(), user=user,
                               confidence=confidence,
                               clarification_questions=questions)

    def _system(self) -> str:
        """The evidence contract, from the Prompt Registry."""
        return self.prompts.render("reports.evidence_narrator")

    def enterprise_copilot_prompt(
            self, question: str, intent: str, business_context: dict[str, Any],
            evidence: list[dict], output_format: str,
            conversation: list[dict] | None = None,
            business_rules: list[str] | None = None,
            weak_evidence: bool = False,
            max_evidence_chars: int = DEFAULT_EVIDENCE_BUDGET_CHARS,
            max_context_chars: int = DEFAULT_CONTEXT_BUDGET_CHARS) -> GeneratedPrompt:
        """The Enterprise Copilot's prompt: an executive request answered from
        a closed set of evidence.

        Structured exactly as the SDS requires — system context, business
        context, evidence, the request, the expected output format, confidence
        requirements, and hallucination prevention — and built here rather than
        at the call site, because this module owns prompts.

        The distinction that matters: ``business_context`` tells the model what
        the organization *is* (its terminology, portfolio, memory); ``evidence``
        is the only thing it may make claims *from*. Both are supplied, and the
        prompt says which is which.
        """
        history = ""
        if conversation:
            turns = "\n".join(f"{t.get('role')}: {str(t.get('content'))[:300]}"
                              for t in conversation[-6:])
            history = self.prompts.render("copilot.history_block", turns=turns)
        rules_block = ""
        if business_rules:
            rules_block = self.prompts.render(
                "copilot.rules_block",
                rules="\n".join(f"- {r}" for r in business_rules))

        confidence_requirement = (CONFIDENCE_WEAK if weak_evidence
                                  else CONFIDENCE_STRONG)

        # Budget the two large payloads BEFORE serialization so the prompt
        # carries only the minimum required evidence + a bounded business
        # context — never the whole set. This is what keeps the local model
        # from being handed a 10k-token prompt it cannot finish in time.
        budgeted_evidence, dropped = _budget_evidence(evidence or [],
                                                      max_evidence_chars)
        evidence_json = json.dumps(budgeted_evidence, default=str)
        business_context_json = _cap_json(business_context, max_context_chars)

        user = self.prompts.render(
            "copilot.enterprise_answer", question=repr(question), intent=intent,
            history=history,
            business_context_json=business_context_json,
            rules_block=rules_block,
            evidence_json=evidence_json,
            output_format=output_format,
            confidence_requirement=confidence_requirement)
        confidence = 0.3 if weak_evidence else 0.8
        prompt = GeneratedPrompt(system=self._system(), user=user,
                                 confidence=confidence)
        logger.info("copilot prompt built: %d evidence kept (%d dropped), "
                    "context=%d chars, prompt=%d chars (~%d tokens)",
                    len(budgeted_evidence), dropped, len(business_context_json),
                    len(prompt.system) + len(prompt.user),
                    (len(prompt.system) + len(prompt.user)) // 4)
        return prompt

    # ----------------------------------------------------------- internals
    def _knowledge_block(self, context: dict[str, Any] | None = None) -> str:
        """Inject organization terminology, rules, and answered clarifications
        so the model reasons in the enterprise's own language. Skipped when
        the context is already a unified Enterprise Context — it carries the
        knowledge under its ``enterprise`` key and must stay the single
        source the Prompt Engine consumes."""
        if context is not None and "enterprise" in context:
            return ""
        if self.knowledge is None:
            return ""
        slice_ = self.knowledge.context_for_reasoning()
        if not any(slice_.values()):
            return ""
        return ("\n=== ENTERPRISE KNOWLEDGE (organization terminology and rules) ===\n"
                f"{json.dumps(slice_, default=str)}\n")

    def _assess(self, context: dict[str, Any]) -> tuple[float, list[str]]:
        """Score how well the context supports high-quality reasoning, and
        draft clarification questions for the gaps — skipping any question the
        organization has already answered."""
        kpis = context.get("kpis", []) or []
        signals = context.get("signals", []) or []
        schema = context.get("schema", []) or []
        score = 0.25
        score += min(len(kpis), 5) * 0.09
        score += min(len(signals), 5) * 0.04
        score += min(len(schema), 4) * 0.025
        confidence = round(min(score, 1.0), 2)

        questions: list[str] = []
        if confidence < self.min_confidence:
            if not kpis:
                questions.append(
                    "No KPIs were discovered automatically. Which columns represent the "
                    "measures that matter to your business (e.g. revenue, volume, users)?")
            if not schema:
                questions.append(
                    "No schema could be derived from the uploaded data. What does each "
                    "dataset represent?")
            if not signals and kpis:
                questions.append(
                    "No time-based trends were detected. Is there a date column or period "
                    "field we should use to track these KPIs over time?")
        # Never re-ask what the enterprise already answered.
        if self.knowledge is not None:
            unanswered = []
            for q in questions:
                known = self.knowledge.find_clarification(q)
                if known is None:
                    unanswered.append(q)
            questions = unanswered
        return confidence, questions

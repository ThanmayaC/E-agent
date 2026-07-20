"""Copilot prompts — the executive's conversational surface.

Two shapes: the project copilot (analytics context, one project) and the
Enterprise Copilot (business context + a closed evidence set, organization
wide). Both are governed: they are the surface where an executive is most
likely to act on a sentence immediately.

Moved verbatim out of ``app/agents/prompt_generator.py`` in V2.2.
"""
from __future__ import annotations

from app.prompts.registry import PromptTemplate

PROJECT_COPILOT = """A business user asks: {question}

{history}Answer using ONLY this analytics context:
{context_json}
{knowledge_block}
Respond as a JSON object with EXACTLY this shape:
{{"answer": "direct, quantified answer for the user",
 "cited_facts": ["specific figures/facts from the context you relied on"],
 "confidence": 0.0}}
If the context cannot answer the question, set answer to an explanation of \
what data would be required. JSON only."""

ENTERPRISE_COPILOT = """An executive asks: {question}
Detected intent: {intent}. Answer in that shape.

{history}=== BUSINESS CONTEXT (what this organization is — reason WITHIN it, but do not quote it as evidence) ===
{business_context_json}

{rules_block}=== EVIDENCE (the ONLY facts you may assert; each has an `id` you must cite) ===
{evidence_json}

=== TASK ===
Produce a {output_format} for the executive as a JSON object with EXACTLY this shape:
{{"answer": "a direct, quantified answer in business language — lead with the conclusion, then the numbers that support it",
 "cited_facts": ["the exact figures/facts you used"],
 "evidence_ids": ["the `id` of every evidence item your answer rests on — an answer citing none will be rejected"],
 "confidence": 0.0,
 "limitations": ["what this evidence cannot tell the executive"],
 "suggested_actions": ["concrete next steps that follow from the cited evidence — omit rather than invent"]}}

{confidence_requirement}
Every number in your answer must appear in the evidence. Every KPI you name \
must exist in the evidence. If the evidence cannot answer the question, say so \
plainly and list what data would be required — that is a complete and correct \
answer, not a failure. JSON only."""

CONFIDENCE_STRONG = (
    "CONFIDENCE: report a confidence between 0 and 1 that reflects the "
    "evidence, not your fluency. Lower it when the evidence is indirect, "
    "dated, or contradictory. A confident sentence built on nothing is the "
    "worst possible answer for an executive.")

CONFIDENCE_WEAK = (
    "CONFIDENCE: report a confidence between 0 and 1 that reflects the "
    "evidence, not your fluency. The evidence supplied is thin, so your "
    "confidence must not exceed 0.4 and you must say what additional data "
    "would raise it. A confident sentence built on nothing is the worst "
    "possible answer for an executive.")

RULES_BLOCK = ("=== BUSINESS RULES (the organization's own rules — an answer "
               "that contradicts one of these is wrong however well it reads) "
               "===\n{rules}\n\n")

HISTORY_BLOCK = ("=== RECENT CONVERSATION (for reference resolution only — "
                 "never a source of facts) ===\n{turns}\n\n")


TEMPLATES = [
    PromptTemplate(
        prompt_id="copilot.project_answer", domain="copilot",
        template=PROJECT_COPILOT, version=1, owner="platform-architecture",
        description="Project copilot: answer a question from one project's "
                    "analytics context.",
        tags=("task", "conversation"), governed=True),
    PromptTemplate(
        prompt_id="copilot.enterprise_answer", domain="copilot",
        template=ENTERPRISE_COPILOT, version=1, owner="platform-architecture",
        description="Enterprise Copilot: answer an executive request from a "
                    "closed evidence set, with citations and limitations.",
        tags=("task", "conversation"), governed=True),
    PromptTemplate(
        prompt_id="copilot.rules_block", domain="copilot",
        template=RULES_BLOCK, version=1, owner="platform-architecture",
        description="Business-rules preamble injected when the organization "
                    "has explicit rules.",
        tags=("fragment",)),
    PromptTemplate(
        prompt_id="copilot.history_block", domain="copilot",
        template=HISTORY_BLOCK, version=1, owner="platform-architecture",
        description="Conversation-history preamble, explicitly marked as "
                    "non-evidence.",
        tags=("fragment",)),
]

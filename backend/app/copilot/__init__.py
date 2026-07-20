"""Enterprise Copilot Layer — the executive's primary way into the platform.

Its responsibility is **not** to calculate. It understands what an executive
is asking for, orchestrates the modules that already know the answer, and has
the reasoning model narrate the evidence they returned.

    intent          what is being asked — deterministic, so routing cannot
                    hallucinate and understanding survives with no LLM
    planner         intent → execution plan: modules, order, evidence,
                    reports, approvals, expected output
    context         what the organization IS — brain, knowledge, memory,
                    organization, portfolio, product, tasks, rules, decisions
    evidence        what is TRUE right now — gathered before the model is
                    asked, every item carrying a citable id
    router          reuses the platform's provider abstraction (Ollama /
                    OpenAI / Azure / Anthropic / Gemini) — no provider code
    validator       rejects invented numbers, invented KPIs, and answers that
                    contradict evidence or business rules; caps confidence
    conversations   history, clarifications, preferences, pinned threads
    actions         recommended actions, next steps, risks, approvals,
                    related reports and products
    copilot         the orchestrator that runs the pipeline
    copilot_runtime composition root, wired into the existing scheduler
"""
from app.copilot.actions import SuggestedActionsBuilder
from app.copilot.context import ContextBuilder
from app.copilot.conversations import ConversationMemory
from app.copilot.copilot import EnterpriseCopilot
from app.copilot.copilot_runtime import CopilotLayer
from app.copilot.evidence import Evidence, EvidenceCollector
from app.copilot.intent import INTENTS, Intent, IntentClassifier
from app.copilot.planner import MODULES, ExecutionPlan, RequestPlanner
from app.copilot.router import LLMRouter
from app.copilot.store import CopilotStore
from app.copilot.validator import ResponseValidator, Validation

__all__ = [
    "INTENTS", "MODULES", "ContextBuilder", "ConversationMemory",
    "CopilotLayer", "CopilotStore", "EnterpriseCopilot", "Evidence",
    "EvidenceCollector", "ExecutionPlan", "Intent", "IntentClassifier",
    "LLMRouter", "RequestPlanner", "ResponseValidator",
    "SuggestedActionsBuilder", "Validation",
]

"""Intent Understanding — what is the executive actually asking for?

Fifteen intents, from the SDS vocabulary. Classification is **deterministic**:
scored keyword and shape evidence, not an LLM call. Three reasons, and they
are the design:

1. Routing decides which modules run and what evidence is gathered. An LLM
   that hallucinates the *route* produces a confidently wrong answer before
   the answering model ever sees a fact.
2. It must work with no provider configured. `EDIP_LLM_PROVIDER=none` degrades
   the *answer*, not the platform's ability to understand and orchestrate.
3. It is instant and free. Intent runs on every message; a network round-trip
   per keystroke-length question is a cost with no benefit.

Ambiguity is reported, never hidden: the classifier returns its confidence and
the runner-up, so the copilot can ask rather than guess when the two are close.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

# The SDS intent vocabulary. Closed by design — an intent the planner has no
# route for is not an intent, it is a guess.
INTENTS = (
    "question",           # "what is our merchant retention?"
    "analysis",           # "analyse the payments decline"
    "recommendation",     # "what should we do about churn?"
    "report",             # "generate the Q3 report"
    "comparison",         # "compare Payments and Checkout"
    "forecast",           # "what will revenue be next quarter?"
    "explanation",        # "why did revenue fall?"
    "scenario",           # "what if customer growth rises 15%?"
    "approval",           # "approve the board email"
    "task",               # "create a task to review pricing"
    "workflow",           # "run the daily cycle"
    "search",             # "find everything about merchant fees"
    "decision",           # "record that we chose vendor A"
    "meeting_prep",       # "prepare me for the board meeting"
    "executive_brief",    # "give me the board brief"
)

DEFAULT_INTENT = "question"
# Below this the copilot should confirm rather than assume; above it, route.
CONFIDENT = 0.5
# When the top two intents are this close, the request is genuinely ambiguous.
AMBIGUOUS_MARGIN = 0.15

# Signals per intent. Phrases score higher than single words: "what if" is a
# much stronger scenario signal than "if".
PHRASES: dict[str, tuple[str, ...]] = {
    "scenario": ("what if", "what happens if", "simulate", "scenario",
                 "if we increase", "if we decrease", "suppose", "model the "
                 "impact"),
    "explanation": ("why did", "why is", "why has", "why are", "explain why",
                    "what caused", "root cause", "reason for", "driver of"),
    "comparison": ("compare", "versus", " vs ", "difference between",
                   "better than", "against last", "relative to"),
    "forecast": ("forecast", "predict", "projection", "next quarter",
                 "next month", "will we", "expected to", "outlook"),
    "recommendation": ("what should", "recommend", "advise", "suggestion",
                       "how do we improve", "how can we", "best course",
                       "what would you do"),
    "report": ("generate a report", "produce a report", "write a report",
               "full report", "the report for"),
    "executive_brief": ("board brief", "executive brief", "decision pack",
                        "board pack", "monthly review", "quarterly strategy",
                        "risk summary", "growth summary", "brief me"),
    "meeting_prep": ("prepare me", "prep me", "for the meeting", "before the "
                     "meeting", "talking points", "board meeting", "agenda for",
                     "walk into"),
    "approval": ("approve", "reject", "sign off", "authorise", "authorize",
                 "waiting on me", "needs my approval", "pending approval"),
    "task": ("create a task", "add a task", "remind me to", "assign",
             "action item", "follow up on", "put on my list"),
    "workflow": ("run the", "trigger the", "kick off", "execute the workflow",
                 "start the workflow", "refresh the"),
    "decision": ("we decided", "record the decision", "log the decision",
                 "we have chosen", "decision was", "note that we"),
    "search": ("find", "search for", "look up", "where is", "show me "
               "everything", "anything about"),
    "analysis": ("analyse", "analyze", "deep dive", "break down", "assess the",
                 "look into", "investigate"),
    "question": ("what is", "what are", "how many", "how much", "who owns",
                 "when did", "which product", "status of"),
}

WORDS: dict[str, tuple[str, ...]] = {
    "scenario": ("simulation", "hypothetical", "elasticity"),
    "explanation": ("because", "cause", "caused", "driver", "attribution"),
    "comparison": ("compared", "comparison", "benchmark", "against"),
    "forecast": ("forecasted", "projected", "trajectory", "trend"),
    "recommendation": ("recommendation", "recommendations", "should",
                       "improve", "optimise", "optimize", "strategy"),
    "report": ("report",),
    "executive_brief": ("brief", "briefing"),
    "meeting_prep": ("meeting", "presentation", "prep"),
    "approval": ("approval", "approvals", "approved", "pending"),
    "task": ("task", "tasks", "todo"),
    "workflow": ("workflow", "pipeline", "job", "sync"),
    "decision": ("decision", "decisions", "decided"),
    "search": ("search", "find"),
    "analysis": ("analysis", "analytics", "breakdown"),
    "question": ("what", "which", "who", "when", "where", "how"),
}

PHRASE_WEIGHT = 3.0
WORD_WEIGHT = 1.0
# A question mark is weak evidence of a question, and only that.
QUESTION_MARK_WEIGHT = 0.5


@dataclass
class Intent:
    """What the executive wants, and how sure we are."""
    intent: str
    confidence: float
    matched: list[str] = field(default_factory=list)
    alternatives: list[dict] = field(default_factory=list)
    subject: str = ""            # the product/entity the request is about
    ambiguous: bool = False

    def describe(self) -> dict:
        return {"intent": self.intent, "confidence": self.confidence,
                "matched": self.matched, "alternatives": self.alternatives,
                "subject": self.subject, "ambiguous": self.ambiguous}


class IntentClassifier:
    """Deterministic intent detection over the SDS vocabulary."""

    def __init__(self, subjects: list[str] | None = None):
        # Known subjects (product names) sharpen classification and give the
        # planner something to scope evidence to. Refreshed by the copilot
        # from the product catalogue — never hardcoded.
        self._subjects = [s.lower() for s in (subjects or [])]

    def set_subjects(self, subjects: list[str]) -> None:
        self._subjects = [s.lower() for s in subjects if s]

    def classify(self, message: str) -> Intent:
        text = f" {str(message).strip().lower()} "
        if not text.strip():
            return Intent(intent=DEFAULT_INTENT, confidence=0.0,
                          ambiguous=True)

        scores: dict[str, float] = {}
        matched: dict[str, list[str]] = {}

        for intent, phrases in PHRASES.items():
            for phrase in phrases:
                if phrase in text:
                    scores[intent] = scores.get(intent, 0.0) + PHRASE_WEIGHT
                    matched.setdefault(intent, []).append(phrase)
        for intent, words in WORDS.items():
            for word in words:
                if re.search(rf"\b{re.escape(word)}\b", text):
                    scores[intent] = scores.get(intent, 0.0) + WORD_WEIGHT
                    matched.setdefault(intent, []).append(word)
        if "?" in message:
            scores["question"] = scores.get("question", 0.0) + QUESTION_MARK_WEIGHT

        if not scores:
            return Intent(intent=DEFAULT_INTENT, confidence=0.3,
                          subject=self._subject(text),
                          matched=[], ambiguous=True)

        ranked = sorted(scores.items(), key=lambda kv: -kv[1])
        top_intent, top_score = ranked[0]
        total = sum(scores.values())
        confidence = round(top_score / total, 3) if total else 0.0

        alternatives = [{"intent": i, "confidence": round(s / total, 3)}
                        for i, s in ranked[1:4]]
        ambiguous = bool(
            alternatives
            and (confidence - alternatives[0]["confidence"]) < AMBIGUOUS_MARGIN)

        return Intent(intent=top_intent, confidence=confidence,
                      matched=matched.get(top_intent, [])[:5],
                      alternatives=alternatives, subject=self._subject(text),
                      ambiguous=ambiguous)

    def _subject(self, text: str) -> str:
        """The product or entity the request is about, when it names one the
        platform actually knows. Never guessed: an unknown noun is not a
        subject, it is just a word."""
        for subject in sorted(self._subjects, key=len, reverse=True):
            if subject and re.search(rf"\b{re.escape(subject)}\b", text):
                return subject
        return ""

    @staticmethod
    def vocabulary() -> list[dict]:
        """The intents the copilot understands, for the UI and the API."""
        return [{"intent": i,
                 "examples": list(PHRASES.get(i, ()))[:3]} for i in INTENTS]

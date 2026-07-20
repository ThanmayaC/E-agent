"""Enterprise Copilot Layer — composition root and runtime integration.

Assembles intent understanding, the planner, the context builder, the evidence
collector, the LLM router, the validator, conversation memory, and suggested
actions, then registers its jobs on the **existing** Enterprise Scheduler.

No new scheduler, no new provider abstraction, no new analytics: the copilot
reaches every module through the interface that module already publishes.

Jobs:

    copilot_subjects       teach the classifier the products that exist
                           (startup, and again when the catalogue changes)
    copilot_maintenance    prune old conversations, keep the store bounded
                           (cron, nightly)
"""
from __future__ import annotations

from typing import Any

from app.copilot.actions import SuggestedActionsBuilder
from app.copilot.context import ContextBuilder
from app.copilot.conversations import ConversationMemory
from app.copilot.copilot import EnterpriseCopilot
from app.copilot.evidence import EvidenceCollector
from app.copilot.intent import IntentClassifier
from app.copilot.planner import RequestPlanner
from app.copilot.router import LLMRouter
from app.copilot.store import CopilotStore
from app.copilot.validator import ResponseValidator
from app.core.logging import get_logger

logger = get_logger(__name__)


class CopilotLayer:
    """The Enterprise Copilot, assembled over the existing platform."""

    def __init__(self, settings, store, knowledge, prompt_agent, provider=None,
                 fallback=None, manager=None, portfolio=None, brain=None,
                 sync=None, product=None):
        self.settings = settings
        self.store = CopilotStore(settings.copilot_dir)
        self.conversations = ConversationMemory(self.store,
                                                knowledge=knowledge)
        self.intent = IntentClassifier()
        self.planner = RequestPlanner()
        self.context = ContextBuilder(
            knowledge=knowledge, artifacts=store, manager=manager,
            portfolio=portfolio, brain=brain, sync=sync, product=product,
            conversations=self.conversations)
        self.evidence = EvidenceCollector(
            knowledge=knowledge, artifacts=store, product=product, sync=sync,
            portfolio=portfolio, manager=manager,
            search=getattr(sync, "search", None))
        # The LLM Router reuses the platform's provider abstraction — the
        # concrete providers are built once, in the container, from config.
        self.router = LLMRouter(provider, fallback)
        self.validator = ResponseValidator()
        self.actions = SuggestedActionsBuilder(product=product,
                                               manager=manager,
                                               knowledge=knowledge)
        self.copilot = EnterpriseCopilot(
            intent=self.intent, planner=self.planner, context=self.context,
            evidence=self.evidence, router=self.router,
            validator=self.validator, conversations=self.conversations,
            actions=self.actions, prompt_agent=prompt_agent, product=product,
            search=getattr(sync, "search", None))
        self._knowledge = knowledge
        self._product = product
        self._bus = None

    # ------------------------------------------------------------- wiring
    def attach_bus(self, bus) -> None:
        """Announce on the enterprise event bus, owned by the autonomy
        runtime — which is built after this layer."""
        self._bus = bus
        self.copilot.attach_bus(bus)

    def register_jobs(self, scheduler, JobDefinition, RetryPolicy) -> None:
        """Register copilot work on the existing Enterprise Scheduler. The
        classes are passed in so this layer never imports the runtime."""
        retry = RetryPolicy(attempts=2, backoff_seconds=5.0)

        scheduler.register(JobDefinition(
            "copilot_subjects",
            "Teach the copilot the products the platform knows about",
            "startup", self.copilot.refresh_subjects, retry=retry,
            tags=["startup", "copilot"]))
        # The catalogue changes when products are registered or discovered;
        # the classifier must learn the new names without a restart.
        scheduler.register(JobDefinition(
            "copilot_subjects_refresh",
            "Refresh the copilot's known subjects when products change",
            "event", self.copilot.refresh_subjects, event="ProductRegistered",
            retry=retry, tags=["copilot", "event"]))
        scheduler.register(JobDefinition(
            "copilot_maintenance",
            "Prune old conversations and keep the copilot store bounded",
            "cron", self.maintain, cron=self.settings.copilot_prune_cron,
            retry=retry, tags=["copilot", "nightly"]))

    # --------------------------------------------------------------- jobs
    def maintain(self) -> dict[str, Any]:
        """Conversation persistence upkeep: bounded history, pinned threads
        kept forever."""
        pruned = self.conversations.prune(
            keep=self.settings.copilot_keep_conversations)
        subjects = self.copilot.refresh_subjects()
        return {**pruned, **subjects,
                "conversations": self.conversations.stats()}

    # ------------------------------------------------------------- status
    def status(self) -> dict[str, Any]:
        return self.copilot.stats()

    def workspace(self) -> dict[str, Any]:
        """The Copilot Workspace: chat surface, history, suggestions, recent
        reports, pinned conversations."""
        conversations = self.conversations.conversations(limit=20)
        return {
            "conversations": conversations,
            "pinned": [c for c in conversations if c["pinned"]],
            "suggested_questions": self.copilot.suggested_questions(),
            "recent_reports": self._recent_reports(),
            "intents": self.intent.vocabulary(),
            "provider": self.router.describe(),
            "stats": self.conversations.stats(),
        }

    def _recent_reports(self, limit: int = 5) -> list[dict]:
        """Reports an executive might want to talk about — read from the
        Knowledge Store's report history, and from the product layer's briefs
        when it is wired."""
        reports: list[dict] = []
        try:
            for report in self._knowledge.report_history(limit):
                reports.append({"title": report.get("title"),
                                "project_id": report.get("project_id"),
                                "health_score": report.get("health_score"),
                                "kind": "analysis",
                                "generated_at": report.get("generated_at")})
        except Exception:  # noqa: BLE001 — the workspace degrades, never fails
            logger.exception("Reading report history for the copilot "
                             "workspace failed")
        if self._product is not None:
            try:
                for brief in self._product.briefs.briefs(limit=limit):
                    reports.append({"title": brief["title"],
                                    "project_id": "", "health_score": None,
                                    "kind": brief["kind"],
                                    "generated_at": brief["generated_at"]})
            except Exception:  # noqa: BLE001
                logger.exception("Reading briefs for the copilot workspace "
                                 "failed")
        return sorted(reports, key=lambda r: str(r.get("generated_at") or ""),
                      reverse=True)[:limit]

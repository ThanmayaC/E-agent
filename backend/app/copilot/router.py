"""LLM Router — reuses the platform's provider abstraction.

This module deliberately contains **no provider code**. `app/llm/` already
decides which of Ollama / OpenAI / Azure OpenAI / Anthropic / Gemini /
enterprise runs, from configuration alone (`EDIP_LLM_PROVIDER`), with an
optional fallback tried when the primary fails after its retries. A second
place that knows providers exist is a second place to keep correct.

What the router adds is the copilot's two needs on top of that:

- **routing a prompt to the configured provider, then the fallback** — the
  existing ``AIReasoningEngine.answer`` uses the primary only, so the copilot
  routes explicitly to get the fallback behaviour the report path already has;
- **saying which provider answered**, so an executive can see whether they are
  reading a local model or a production gateway.

With no provider configured, the router returns ``unavailable`` and the copilot
answers from evidence alone. That is the platform's standing contract: AI
degrades, the platform does not substitute template narrative.
"""
from __future__ import annotations

import time
from typing import Any

from app.core.logging import get_logger
from app.llm.base_provider import BaseLLMProvider, ChatMessage, LLMError

logger = get_logger(__name__)

AI_UNAVAILABLE = (
    "No LLM provider is configured, so the copilot cannot narrate this answer. "
    "The evidence below is complete and was gathered deterministically. "
    "Configure EDIP_LLM_PROVIDER (ollama / openai / azure-openai / anthropic / "
    "gemini / enterprise) to enable narration.")


class LLMRouter:
    """Routes a generated prompt to the configured provider."""

    def __init__(self, provider: BaseLLMProvider | None,
                 fallback: BaseLLMProvider | None = None,
                 governance=None, latency=None):
        self._provider = provider
        self._fallback = fallback
        # Optional — when wired, every call is recorded for the Admin
        # console's LLM usage metrics (governance) and processing-latency
        # dashboard (latency).
        self._governance = governance
        self._latency = latency

    def _record_usage(self, provider: BaseLLMProvider, duration_ms: float,
                      status: str) -> None:
        if self._latency is not None:
            self._latency.record("llm_chat", duration_ms)
        if self._governance is None:
            return
        usage = getattr(provider, "last_usage", None) or {}
        try:
            self._governance.record_model_usage(
                provider=provider.name,
                model=getattr(provider, "model", provider.config.model),
                tokens_in=usage.get("tokens_in", 0),
                tokens_out=usage.get("tokens_out", 0),
                duration_ms=int(duration_ms), status=status)
        except Exception:  # noqa: BLE001 — usage tracking must never break the copilot
            logger.exception("Recording model usage failed")

    @property
    def available(self) -> bool:
        return self._provider is not None

    def describe(self) -> dict[str, Any]:
        """Which provider is configured — the same information the platform
        already reports for reports, surfaced for the copilot."""
        def name(provider) -> dict | None:
            if provider is None:
                return None
            return {"provider": provider.name,
                    "model": getattr(provider, "model",
                                     provider.config.model)}
        return {"available": self.available, "primary": name(self._provider),
                "fallback": name(self._fallback)}

    # -------------------------------------------------------------- route
    def route(self, prompt) -> dict[str, Any]:
        """Send a ``GeneratedPrompt`` to the primary, then the fallback.

        Never raises: an unreachable model is a degraded answer, not a failed
        request — the executive still gets the evidence.
        """
        if self._provider is None:
            return {"status": "unavailable", "answer": AI_UNAVAILABLE,
                    "cited_facts": [], "evidence_ids": [], "confidence": 0.0,
                    "limitations": ["AI narration is not configured."],
                    "suggested_actions": [], "provider": "", "model": ""}

        messages = [ChatMessage("system", prompt.system),
                    ChatMessage("user", prompt.user)]
        last_error = ""
        for provider in [p for p in (self._provider, self._fallback) if p]:
            started = time.monotonic()
            try:
                raw = provider.chat_json(messages)
                self._record_usage(provider, (time.monotonic() - started) * 1000, "ok")
                return self._normalize(raw, provider)
            except (LLMError, Exception) as exc:  # noqa: BLE001 — must degrade
                self._record_usage(provider, (time.monotonic() - started) * 1000, "failed")
                logger.exception("Copilot reasoning failed on provider %s",
                                 provider.name)
                last_error = f"{provider.name}: {str(exc)[:300]}"
        return {"status": "failed",
                "answer": f"AI reasoning failed: {last_error}",
                "cited_facts": [], "evidence_ids": [], "confidence": 0.0,
                "limitations": ["The reasoning model could not be reached."],
                "suggested_actions": [], "provider": self._provider.name,
                "model": ""}

    @staticmethod
    def _normalize(raw: dict, provider) -> dict[str, Any]:
        """Whatever shape the model emitted, the copilot's contract is fixed."""
        def strings(value: Any, limit: int) -> list[str]:
            if not isinstance(value, list):
                value = [value] if value else []
            return [str(v).strip() for v in value if v][:limit]

        try:
            confidence = float(raw.get("confidence") or 0.0)
        except (TypeError, ValueError):
            confidence = 0.0
        return {
            "status": "ok",
            "answer": str(raw.get("answer", "")).strip() or "(empty answer)",
            "cited_facts": strings(raw.get("cited_facts"), 10),
            "evidence_ids": strings(raw.get("evidence_ids"), 12),
            "confidence": max(0.0, min(confidence, 1.0)),
            "limitations": strings(raw.get("limitations"), 5),
            "suggested_actions": strings(raw.get("suggested_actions"), 5),
            "provider": provider.name,
            "model": getattr(provider, "model", provider.config.model),
        }

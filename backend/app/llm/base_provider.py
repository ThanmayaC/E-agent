"""LLM provider abstraction.

The rest of the application never knows which provider is in use: it calls
`chat()` / `chat_json()` on the interface. Concrete providers (Ollama, OpenAI,
Azure OpenAI, Anthropic, Gemini, enterprise gateway) are selected purely by
configuration in the factory.
"""
from __future__ import annotations

import json
import re
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Iterator

from app.core.logging import get_logger

logger = get_logger(__name__)


@dataclass
class LLMConfig:
    provider: str
    model: str = ""
    api_key: str = ""
    base_url: str = ""
    temperature: float = 0.2
    max_tokens: int = 4096
    timeout_s: float = 120.0
    retries: int = 2
    retry_backoff_s: float = 1.5
    extra: dict[str, Any] = field(default_factory=dict)  # e.g. azure api_version


@dataclass
class ChatMessage:
    role: str  # system | user | assistant
    content: str


class LLMError(RuntimeError):
    """Provider call failed after retries."""


class BaseLLMProvider(ABC):
    name: str = "base"

    def __init__(self, config: LLMConfig):
        self.config = config
        # Token usage from the most recent _chat_once call, when the provider's
        # API reports it. Read by the caller right after chat()/chat_json()
        # returns — there is one call in flight per provider instance per
        # request, so this needs no locking.
        self.last_usage: dict[str, int] = {"tokens_in": 0, "tokens_out": 0}
        # Richer diagnostics from the most recent call (prompt size, latency),
        # surfaced on the runtime diagnostics page. Providers that measure it
        # populate this; the default is empty.
        self.last_call: dict[str, Any] = {}

    # ------------------------------------------------------------ interface
    @abstractmethod
    def _chat_once(self, messages: list[ChatMessage], json_mode: bool) -> str:
        """Single non-streaming completion. Raise on transport/HTTP errors."""

    def stream(self, messages: list[ChatMessage]) -> Iterator[str]:
        """Token stream. Default: yield the full completion once."""
        yield self.chat(messages)

    # ------------------------------------------------------------- retries
    def chat(self, messages: list[ChatMessage], json_mode: bool = False) -> str:
        last_exc: Exception | None = None
        prompt_chars = sum(len(m.content) for m in messages)
        for attempt in range(self.config.retries + 1):
            started = time.monotonic()
            try:
                return self._chat_once(messages, json_mode)
            except Exception as exc:  # transport, HTTP, timeout
                last_exc = exc
                took = int((time.monotonic() - started) * 1000)
                # Log why and how long — a timeout on a large prompt is a very
                # different failure from a connection refused, and both were
                # previously invisible behind "failed after N attempts".
                logger.warning("%s chat attempt %d/%d failed after %d ms "
                               "(prompt=%d chars): %s", self.name, attempt + 1,
                               self.config.retries + 1, took, prompt_chars, exc)
                if attempt < self.config.retries:
                    time.sleep(self.config.retry_backoff_s * (attempt + 1))
        raise LLMError(f"{self.name} failed after {self.config.retries + 1} "
                       f"attempts (prompt={prompt_chars} chars): {last_exc}")

    def chat_json(self, messages: list[ChatMessage]) -> dict[str, Any]:
        """Completion that must yield a JSON object; re-asks once on bad JSON."""
        text = self.chat(messages, json_mode=True)
        parsed = extract_json(text)
        if parsed is not None:
            return parsed
        retry_messages = messages + [
            ChatMessage("assistant", text[:4000]),
            ChatMessage("user", "That was not valid JSON. Respond again with ONLY the JSON object, no prose, no markdown fences."),
        ]
        text = self.chat(retry_messages, json_mode=True)
        parsed = extract_json(text)
        if parsed is None:
            raise LLMError(f"{self.name} did not return valid JSON")
        return parsed


def extract_json(text: str) -> dict[str, Any] | None:
    """Pull the first JSON object out of a completion (tolerates fences/prose)."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.MULTILINE).strip()
    # models with visible reasoning may prefix <think>...</think>
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    try:
        obj = json.loads(text)
        return obj if isinstance(obj, dict) else None
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    if start == -1:
        return None
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                try:
                    obj = json.loads(text[start:i + 1])
                    return obj if isinstance(obj, dict) else None
                except json.JSONDecodeError:
                    return None
    return None

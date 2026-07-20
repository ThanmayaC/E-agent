"""Anthropic provider (Messages API)."""
from __future__ import annotations

import httpx

from app.llm.base_provider import BaseLLMProvider, ChatMessage, LLMConfig

DEFAULT_BASE_URL = "https://api.anthropic.com"


class AnthropicProvider(BaseLLMProvider):
    name = "anthropic"

    def _chat_once(self, messages: list[ChatMessage], json_mode: bool) -> str:
        system = "\n".join(m.content for m in messages if m.role == "system")
        convo = [{"role": m.role, "content": m.content} for m in messages if m.role != "system"]
        if json_mode:
            system += "\nRespond with ONLY a valid JSON object. No prose, no markdown."
        resp = httpx.post(
            f"{(self.config.base_url or DEFAULT_BASE_URL).rstrip('/')}/v1/messages",
            headers={"x-api-key": self.config.api_key,
                     "anthropic-version": "2023-06-01"},
            json={"model": self.config.model,
                  "max_tokens": self.config.max_tokens,
                  "temperature": self.config.temperature,
                  "system": system,
                  "messages": convo},
            timeout=self.config.timeout_s,
        )
        resp.raise_for_status()
        return "".join(b.get("text", "") for b in resp.json().get("content", []))

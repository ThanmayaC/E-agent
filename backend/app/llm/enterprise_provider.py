"""Enterprise provider — any company LLM behind an OpenAI-compatible gateway
(vLLM, TGI, LiteLLM, internal fine-tuned models). Point base_url at the
gateway; auth header name is configurable for non-Bearer schemes."""
from __future__ import annotations

import httpx

from app.llm.base_provider import BaseLLMProvider, ChatMessage, LLMConfig


class EnterpriseProvider(BaseLLMProvider):
    """Config extra: {"auth_header": "X-Api-Key"} (default: Authorization Bearer)."""

    name = "enterprise"

    def _headers(self) -> dict:
        header = self.config.extra.get("auth_header")
        if header:
            return {header: self.config.api_key}
        return {"Authorization": f"Bearer {self.config.api_key or 'none'}"}

    def _chat_once(self, messages: list[ChatMessage], json_mode: bool) -> str:
        payload = {
            "model": self.config.model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
        }
        if json_mode:
            payload["response_format"] = {"type": "json_object"}
        resp = httpx.post(f"{self.config.base_url.rstrip('/')}/chat/completions",
                          headers=self._headers(), json=payload,
                          timeout=self.config.timeout_s)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]

"""OpenAI provider (chat completions API)."""
from __future__ import annotations

from typing import Iterator

import httpx

from app.llm.base_provider import BaseLLMProvider, ChatMessage, LLMConfig

DEFAULT_BASE_URL = "https://api.openai.com/v1"


class OpenAIProvider(BaseLLMProvider):
    name = "openai"

    def __init__(self, config: LLMConfig):
        super().__init__(config)
        self.base_url = (config.base_url or DEFAULT_BASE_URL).rstrip("/")

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.config.api_key}"}

    def _payload(self, messages: list[ChatMessage], json_mode: bool, stream: bool = False) -> dict:
        payload = {
            "model": self.config.model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
            "stream": stream,
        }
        if json_mode:
            payload["response_format"] = {"type": "json_object"}
        return payload

    def _chat_once(self, messages: list[ChatMessage], json_mode: bool) -> str:
        resp = httpx.post(f"{self.base_url}/chat/completions",
                          headers=self._headers(),
                          json=self._payload(messages, json_mode),
                          timeout=self.config.timeout_s)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]

    def stream(self, messages: list[ChatMessage]) -> Iterator[str]:
        import json as _json
        with httpx.stream("POST", f"{self.base_url}/chat/completions",
                          headers=self._headers(),
                          json=self._payload(messages, False, stream=True),
                          timeout=self.config.timeout_s) as resp:
            resp.raise_for_status()
            for line in resp.iter_lines():
                if not line.startswith("data: ") or line.endswith("[DONE]"):
                    continue
                delta = _json.loads(line[6:])["choices"][0].get("delta", {})
                if delta.get("content"):
                    yield delta["content"]

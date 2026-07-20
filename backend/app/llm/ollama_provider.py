"""Ollama provider — real REST client (`/api/chat`).

Supports: chat, JSON mode (`format: json`), streaming, retry/timeout (base),
temperature, max tokens. Any installed model (qwen3, llama3, gemma3, mistral,
deepseek, ...) is selectable via configuration; if no model is configured the
first installed model is used.
"""
from __future__ import annotations

import json
from typing import Iterator

import httpx

from app.core.logging import get_logger
from app.llm.base_provider import BaseLLMProvider, ChatMessage, LLMConfig

logger = get_logger(__name__)

DEFAULT_BASE_URL = "http://localhost:11434"


class OllamaProvider(BaseLLMProvider):
    name = "ollama"

    def __init__(self, config: LLMConfig):
        super().__init__(config)
        self.base_url = (config.base_url or DEFAULT_BASE_URL).rstrip("/")
        self._model: str | None = config.model or None

    @property
    def model(self) -> str:
        if not self._model:
            self._model = self._first_installed_model()
        return self._model

    def _first_installed_model(self) -> str:
        resp = httpx.get(f"{self.base_url}/api/tags", timeout=10)
        resp.raise_for_status()
        models = resp.json().get("models", [])
        if not models:
            raise RuntimeError("No models installed in Ollama — run `ollama pull <model>`")
        name = models[0]["name"]
        logger.info("Ollama model auto-selected: %s", name)
        return name

    # -------------------------------------------------------------- chat
    def _chat_once(self, messages: list[ChatMessage], json_mode: bool) -> str:
        payload = {
            "model": self.model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "stream": False,
            # thinking models (qwen3, deepseek-r1, ...) burn the token budget on
            # reasoning and leave content empty; disable unless configured on
            "think": bool(self.config.extra.get("think", False)),
            "options": {
                "temperature": self.config.temperature,
                "num_predict": self.config.max_tokens,
            },
        }
        if json_mode:
            payload["format"] = "json"
        resp = httpx.post(f"{self.base_url}/api/chat", json=payload, timeout=self.config.timeout_s)
        resp.raise_for_status()
        message = resp.json()["message"]
        content = message.get("content", "")
        if not content and message.get("thinking"):
            return message["thinking"]  # fallback: some models ignore think=false
        return content

    def stream(self, messages: list[ChatMessage]) -> Iterator[str]:
        payload = {
            "model": self.model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "stream": True,
            "think": bool(self.config.extra.get("think", False)),
            "options": {
                "temperature": self.config.temperature,
                "num_predict": self.config.max_tokens,
            },
        }
        with httpx.stream("POST", f"{self.base_url}/api/chat", json=payload,
                          timeout=self.config.timeout_s) as resp:
            resp.raise_for_status()
            for line in resp.iter_lines():
                if not line:
                    continue
                chunk = json.loads(line)
                token = chunk.get("message", {}).get("content", "")
                if token:
                    yield token
                if chunk.get("done"):
                    break

"""Google Gemini provider (generateContent API)."""
from __future__ import annotations

import httpx

from app.llm.base_provider import BaseLLMProvider, ChatMessage, LLMConfig

DEFAULT_BASE_URL = "https://generativelanguage.googleapis.com/v1beta"


class GeminiProvider(BaseLLMProvider):
    name = "gemini"

    def _chat_once(self, messages: list[ChatMessage], json_mode: bool) -> str:
        system = "\n".join(m.content for m in messages if m.role == "system")
        contents = [
            {"role": "user" if m.role == "user" else "model",
             "parts": [{"text": m.content}]}
            for m in messages if m.role != "system"
        ]
        generation_config = {
            "temperature": self.config.temperature,
            "maxOutputTokens": self.config.max_tokens,
        }
        if json_mode:
            generation_config["responseMimeType"] = "application/json"
        payload = {"contents": contents, "generationConfig": generation_config}
        if system:
            payload["systemInstruction"] = {"parts": [{"text": system}]}
        url = (f"{(self.config.base_url or DEFAULT_BASE_URL).rstrip('/')}/models/"
               f"{self.config.model}:generateContent?key={self.config.api_key}")
        resp = httpx.post(url, json=payload, timeout=self.config.timeout_s)
        resp.raise_for_status()
        data = resp.json()
        usage = data.get("usageMetadata") or {}
        self.last_usage = {"tokens_in": int(usage.get("promptTokenCount", 0)),
                           "tokens_out": int(usage.get("candidatesTokenCount", 0))}
        candidates = data.get("candidates", [])
        if not candidates:
            raise RuntimeError("Gemini returned no candidates")
        return "".join(p.get("text", "") for p in candidates[0]["content"]["parts"])

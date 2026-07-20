"""Azure OpenAI provider (deployment-based endpoints, api-key auth)."""
from __future__ import annotations

import httpx

from app.llm.base_provider import BaseLLMProvider, ChatMessage, LLMConfig


class AzureOpenAIProvider(BaseLLMProvider):
    """Config:
    base_url  = https://<resource>.openai.azure.com
    model     = deployment name
    extra     = {"api_version": "2024-06-01"} (optional)
    """

    name = "azure-openai"

    def __init__(self, config: LLMConfig):
        super().__init__(config)
        self.api_version = config.extra.get("api_version", "2024-06-01")

    def _chat_once(self, messages: list[ChatMessage], json_mode: bool) -> str:
        url = (f"{self.config.base_url.rstrip('/')}/openai/deployments/"
               f"{self.config.model}/chat/completions?api-version={self.api_version}")
        payload = {
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
        }
        if json_mode:
            payload["response_format"] = {"type": "json_object"}
        resp = httpx.post(url, headers={"api-key": self.config.api_key},
                          json=payload, timeout=self.config.timeout_s)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]

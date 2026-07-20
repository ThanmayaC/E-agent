"""Provider factory — the ONLY place that knows which providers exist.

Selection is configuration-driven (EDIP_LLM_PROVIDER). The application depends
solely on BaseLLMProvider.
"""
from __future__ import annotations

from app.core.config import Settings
from app.llm.anthropic_provider import AnthropicProvider
from app.llm.azure_openai_provider import AzureOpenAIProvider
from app.llm.base_provider import BaseLLMProvider, LLMConfig
from app.llm.enterprise_provider import EnterpriseProvider
from app.llm.gemini_provider import GeminiProvider
from app.llm.mock_provider import MockProvider
from app.llm.ollama_provider import OllamaProvider
from app.llm.openai_provider import OpenAIProvider

_PROVIDERS: dict[str, type[BaseLLMProvider]] = {
    "ollama": OllamaProvider,
    "openai": OpenAIProvider,
    "azure-openai": AzureOpenAIProvider,
    "anthropic": AnthropicProvider,
    "gemini": GeminiProvider,
    "enterprise": EnterpriseProvider,
    "mock": MockProvider,
}


def _build(settings: Settings, name: str, model: str, api_key: str,
           base_url: str) -> BaseLLMProvider | None:
    name = name.lower().strip()
    if name in ("", "none"):
        return None
    cls = _PROVIDERS.get(name)
    if cls is None:
        raise ValueError(f"Unknown LLM provider '{name}'. Available: {sorted(_PROVIDERS)}")
    config = LLMConfig(
        provider=name,
        model=model,
        api_key=api_key,
        base_url=base_url,
        temperature=settings.llm_temperature,
        max_tokens=settings.llm_max_tokens,
        timeout_s=settings.llm_timeout_s,
        retries=settings.llm_retries,
        extra=settings.llm_extra,
    )
    return cls(config)


def create_provider(settings: Settings) -> BaseLLMProvider | None:
    """Return the configured provider, or None when AI reasoning is disabled
    (EDIP_LLM_PROVIDER=none). Callers must treat None as 'AI unavailable' —
    they must not substitute template narrative."""
    return _build(settings, settings.llm_provider, settings.llm_model,
                  settings.llm_api_key, settings.llm_base_url)


def create_fallback_provider(settings: Settings) -> BaseLLMProvider | None:
    """Optional secondary provider (EDIP_LLM_FALLBACK_PROVIDER) tried when the
    primary fails after its retries. None when not configured."""
    return _build(settings, settings.llm_fallback_provider,
                  settings.llm_fallback_model, settings.llm_fallback_api_key,
                  settings.llm_fallback_base_url)

"""Prompt Registry (Version 2.2).

Every LLM prompt the platform uses, declared once, versioned, owned, and
readable without reading Python. Business logic renders from the registry; no
prompt is embedded in the code that needs it.

    registry   PromptTemplate + PromptRegistry — versions, owners, variables,
               change history
    domains    one module per domain: executive, reports, meetings,
               communications, analytics, rca, sop, forecast, copilot
"""
from app.prompts.registry import (
    DOMAINS, PromptNotFound, PromptRegistry, PromptTemplate,
    PromptVariablesMissing,
)

__all__ = ["DOMAINS", "PromptNotFound", "PromptRegistry", "PromptTemplate",
           "PromptVariablesMissing"]

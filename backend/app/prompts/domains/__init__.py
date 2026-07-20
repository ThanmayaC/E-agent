"""Prompt domains — every prompt the platform sends to a language model.

One module per domain, as the SDS organizes them. A domain module declares
``TEMPLATES``; the registry loads them all at construction. Adding a prompt is
adding it to its domain module — never to the business logic that uses it.
"""
from __future__ import annotations

from app.prompts.domains import (
    analytics, communications, copilot, executive, forecast, meetings, rca,
    reports, sop,
)
from app.prompts.registry import PromptTemplate

MODULES = (executive, reports, meetings, communications, analytics, rca, sop,
           forecast, copilot)

__all__ = ["MODULES", "all_templates"]


def all_templates() -> list[PromptTemplate]:
    """Every declared template, across every domain."""
    return [template for module in MODULES for template in module.TEMPLATES]

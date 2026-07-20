"""Executive prompts — briefs and narrative for the Executive Workspace."""
from __future__ import annotations

from app.prompts.registry import PromptTemplate

BRIEF_NARRATIVE = ("Write a 3-4 sentence executive narrative for this daily "
                   "brief. State what changed, what needs attention, and what "
                   "is on track. Use only the figures supplied.")

TEMPLATES = [
    PromptTemplate(
        prompt_id="executive.brief_narrative", domain="executive",
        template=BRIEF_NARRATIVE, version=1, owner="executive-office",
        description="Narrative paragraph for the daily executive brief.",
        tags=("brief", "narrative"), governed=True),
]

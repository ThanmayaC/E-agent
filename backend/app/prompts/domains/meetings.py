"""Meeting prompts — meeting-note summarization and action extraction.

Moved out of ``app/workflows/library.py`` in V2.2.
"""
from __future__ import annotations

from app.prompts.registry import PromptTemplate

MEETING_SUMMARY = ("Summarize this meeting: decisions made, topics discussed, "
                   "and open questions.")

TEMPLATES = [
    PromptTemplate(
        prompt_id="meetings.summarize", domain="meetings",
        template=MEETING_SUMMARY, version=1, owner="operations",
        description="Instruction for summarizing meeting notes into "
                    "decisions, topics, and open questions.",
        tags=("summarization", "documents")),
]

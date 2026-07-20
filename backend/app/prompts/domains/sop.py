"""SOP prompts — standard-operating-procedure change handling.

Moved out of ``app/workflows/library.py`` in V2.2.
"""
from __future__ import annotations

from app.prompts.registry import PromptTemplate

SOP_SUMMARY = ("Summarize this standard operating procedure: its purpose, the "
               "steps it defines, and who owns it.")

SOP_CHANGE = ("Describe what changed in this revised standard operating "
              "procedure and who is affected by the change.")

TEMPLATES = [
    PromptTemplate(
        prompt_id="sop.summarize", domain="sop", template=SOP_SUMMARY,
        version=1, owner="operations",
        description="Instruction for summarizing an SOP document.",
        tags=("summarization", "documents")),
    PromptTemplate(
        prompt_id="sop.describe_change", domain="sop", template=SOP_CHANGE,
        version=1, owner="operations",
        description="Instruction for describing an SOP revision when a new "
                    "version is detected.",
        tags=("change-detection", "documents")),
]

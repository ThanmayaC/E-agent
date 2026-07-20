"""RCA prompts — root-cause analysis document summarization.

Moved out of ``app/workflows/library.py``, where the instruction was an
argument to a helper. A summarization instruction is a prompt: it decides
what the platform records as organizational knowledge about an incident.
"""
from __future__ import annotations

from app.prompts.registry import PromptTemplate

RCA_SUMMARY = ("Summarize this root-cause analysis: what failed, the root "
               "cause, and the corrective actions.")

TEMPLATES = [
    PromptTemplate(
        prompt_id="rca.summarize", domain="rca", template=RCA_SUMMARY,
        version=1, owner="operations",
        description="Instruction for summarizing an RCA document into "
                    "organizational knowledge.",
        tags=("summarization", "documents")),
]

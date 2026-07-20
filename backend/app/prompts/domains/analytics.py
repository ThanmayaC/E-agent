"""Analytics prompts — narration of deterministic analytical findings.

Analytics itself is deterministic and model-free. These prompts narrate
results that were already computed; they never produce a number.
"""
from __future__ import annotations

from app.prompts.registry import PromptTemplate

KPI_NARRATIVE = ("Describe what this KPI movement shows, in one or two "
                 "sentences. Quote only the figures supplied. Do not suggest "
                 "a cause unless a cause is present in the evidence.")

TEMPLATES = [
    PromptTemplate(
        prompt_id="analytics.kpi_narrative", domain="analytics",
        template=KPI_NARRATIVE, version=1, owner="analytics",
        description="Narration of a computed KPI movement.",
        tags=("narration",), governed=True),
]

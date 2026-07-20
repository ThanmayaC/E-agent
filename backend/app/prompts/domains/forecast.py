"""Forecast prompts — narration of validated forecasts.

A forecast the Forecasting Module refused to validate is never narrated: the
prompt exists to explain a result, never to produce one.
"""
from __future__ import annotations

from app.prompts.registry import PromptTemplate

FORECAST_NARRATIVE = ("Explain this validated forecast in two sentences: the "
                      "direction, the horizon, and the stated confidence. "
                      "Name the limitations supplied with it.")

TEMPLATES = [
    PromptTemplate(
        prompt_id="forecast.narrative", domain="forecast",
        template=FORECAST_NARRATIVE, version=1, owner="analytics",
        description="Narration of a validated KPI forecast.",
        tags=("narration",), governed=True),
]

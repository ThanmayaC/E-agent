"""Planned tools — registered so agents and the UI can see the roadmap, but
not yet executable. Each explains what integration it needs.

These become available by implementing ``run`` and flipping ``available``;
no other layer changes.
"""
from __future__ import annotations

from typing import Any

from app.tools.base import Tool, ToolNotAvailable


class _PlannedTool(Tool):
    reason = "planned capability — integration not configured yet"

    @property
    def available(self) -> bool:
        return False

    @property
    def unavailable_reason(self) -> str:
        return self.reason

    def run(self, **kwargs: Any) -> Any:
        raise ToolNotAvailable(f"Tool '{self.name}' is not available: {self.reason}")


class PowerPointTool(_PlannedTool):
    name = "powerpoint_generator"
    description = "Generate an executive PowerPoint deck from a structured report"
    reason = "requires python-pptx integration"


class PDFExportTool(_PlannedTool):
    name = "pdf_generator"
    description = "Export the executive report as a PDF document"
    reason = "requires a PDF rendering backend (weasyprint/reportlab)"


class EmailTool(_PlannedTool):
    name = "email"
    description = "Draft and send follow-up emails to teams"
    reason = "requires SMTP / Graph API credentials"


class CalendarTool(_PlannedTool):
    name = "calendar"
    description = "Schedule recurring reviews and meeting preparation"
    reason = "requires calendar integration (Google/Outlook)"

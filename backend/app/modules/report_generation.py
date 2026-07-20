"""Report Generation Module (SDS §2.8).

Fixed-structure enterprise reports: deterministic fact sections assembled by
``ReportAssembler``, AI narrative sections written by ``ReportWriterAgent``
over verified evidence only, rendered to JSON and Markdown.
"""
from app.agents.report_writer import ReportWriterAgent
from app.reports.generator import ReportAssembler
from app.reports.markdown import render_markdown

__all__ = ["ReportWriterAgent", "ReportAssembler", "render_markdown"]

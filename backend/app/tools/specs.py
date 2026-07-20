"""Tool specifications — the declared contract for every shipped tool.

Kept beside the tools rather than inside them so a spec can be read (by the
Admin console, by Governance, by an LLM choosing a tool) without importing
an implementation or constructing its dependencies.

Schemas mirror each tool's actual ``run`` signature. When the two disagree the
registry rejects the call before the implementation sees it, which turns a
stack trace inside a tool into a clear error at the boundary —
``test_specs_match_tool_signatures`` keeps them honest.
"""
from __future__ import annotations

from app.tools.registry import ToolSpec

# The enterprise tool catalogue. Capability and permissions are what
# Governance reasons about; inputs/outputs are what an agent (or a model
# choosing a tool) reasons about.
SPECS: dict[str, ToolSpec] = {
    "vector_search": ToolSpec(
        tool_id="vector_search", capability="search",
        description="Semantic search over a project's schema, KPIs, signals, "
                    "and relationships.",
        permissions=("read_project",),
        inputs={"project_id": "string", "query": "string", "top_k": "integer"},
        required=("project_id", "query"),
        outputs={"matches": "array<object>"}, tags=("core", "retrieval")),

    "knowledge_search": ToolSpec(
        tool_id="knowledge_search", capability="search",
        description="Search enterprise terminology, rules, clarifications, "
                    "and decision history.",
        permissions=("read_knowledge",),
        inputs={"query": "string", "limit": "integer"}, required=("query",),
        outputs={"results": "array<object>"}, tags=("core", "knowledge")),

    "artifact_lookup": ToolSpec(
        tool_id="artifact_lookup", capability="read",
        description="Load a project's analytical facts: KPIs, signals, "
                    "forecasts, quality, business context, relationships.",
        permissions=("read_project",),
        inputs={"project_id": "string", "artifact": "string",
                "default": "any"},
        required=("project_id", "artifact"),
        outputs={"artifact": "object"}, tags=("core", "evidence")),

    "analytics_sql": ToolSpec(
        tool_id="analytics_sql", capability="query",
        description="Run a read-only SELECT against the project analytics "
                    "warehouse.",
        permissions=("read_project",),
        inputs={"project_id": "string", "sql": "string"},
        required=("project_id", "sql"),
        outputs={"rows": "array<object>"}, tags=("core", "analytics")),

    "report_markdown": ToolSpec(
        tool_id="report_markdown", capability="generate",
        description="Render a project's assembled executive report as "
                    "markdown.",
        permissions=("read_project", "write_artifact"),
        inputs={"project_id": "string"}, required=("project_id",),
        outputs={"markdown": "string"}, tags=("core", "reporting")),

    # ---------------------------------------------------------- planned
    # Registered so the catalogue is complete and Governance can grant
    # permissions before the implementation lands. Each reports itself
    # unavailable until then — exactly as it did in V1.
    "powerpoint_generator": ToolSpec(
        tool_id="powerpoint_generator", capability="generate",
        description="Generate an executive PowerPoint deck from a structured "
                    "report.",
        permissions=("read_project", "write_artifact"),
        inputs={"project_id": "string", "report": "object"},
        required=("project_id",),
        outputs={"path": "string"}, tags=("planned", "reporting")),

    "pdf_generator": ToolSpec(
        tool_id="pdf_generator", capability="generate",
        description="Export the executive report as a PDF document.",
        permissions=("read_project", "write_artifact"),
        inputs={"project_id": "string"}, required=("project_id",),
        outputs={"path": "string"}, tags=("planned", "reporting")),

    "email": ToolSpec(
        tool_id="email", capability="draft",
        description="Draft follow-up email to teams. Drafting only — sending "
                    "goes through the Action Queue.",
        permissions=("draft_external",),
        inputs={"to": "array<string>", "subject": "string", "body": "string"},
        required=("to", "subject"),
        outputs={"draft_id": "string"}, tags=("planned", "communication")),

    "calendar": ToolSpec(
        tool_id="calendar", capability="draft",
        description="Schedule recurring reviews and meeting preparation.",
        permissions=("draft_external",),
        inputs={"title": "string", "start": "string", "attendees":
                "array<string>"},
        required=("title", "start"),
        outputs={"event_id": "string"}, tags=("planned", "communication")),
}


def spec_for(tool_name: str) -> ToolSpec | None:
    """The declared spec for a tool, or None to let the registry derive a
    conservative one."""
    return SPECS.get(tool_name)

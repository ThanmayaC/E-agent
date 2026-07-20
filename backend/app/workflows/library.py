"""Autonomous Workflow Library (Version 2).

The recurring managerial work the platform performs by itself, built on the
V1 machinery: each workflow is an ordinary ``WorkflowDefinition`` run by the
existing Workflow Engine on the existing Scheduler, and anything with an
external effect goes through the Action Queue — a workflow can *draft* an
email or a Teams announcement, but only an approved action sends one.

Document workflows consume the Document Intelligence workfeed
(``unprocessed(workflow, category)``), so each document version is
summarized exactly once no matter how many times the workflow runs.

The LLM is optional throughout: with a provider configured, summaries and
drafts are model-written from document text; without one, deterministic
extractive fallbacks keep every workflow producing useful output. A drafting
workflow never fails the day because the model is down.

V1 already covers the rest of the library's catalogue — daily executive
brief (``daily_cycle``), KPI analysis and dashboard refresh (product/
background jobs), report generation (``full_analysis``), insight generation
and risk detection (``monitoring`` + background sweeps), recommendation
generation (decision engine). Those are reused, not duplicated.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from app.core.logging import get_logger
from app.workflows.engine import WorkflowDefinition

logger = get_logger(__name__)

MAX_DOCS_PER_RUN = 10
MAX_ACTION_ITEMS_PER_MEETING = 8
SUMMARY_SENTENCES = 3
ACTION_LINE = re.compile(
    r"^\s*(?:[-*•]\s*(?:\[ \]\s*)?)?(?:action(?: item)?|todo|follow[- ]?up|ai)"
    r"\s*[:\-]\s*(.+)$", re.IGNORECASE)


@dataclass
class V2Context:
    """Everything the V2 workflows need, injected by the runtime — the same
    pattern AutonomousContext set, so the library stays testable with fakes."""
    documents: Any             # DocumentIntelligence
    knowledge: Any             # KnowledgeStore
    tasks: Any                 # ExecutiveTaskManager
    notifications: Any         # NotificationCenter
    queue: Any                 # ActionQueue
    brief: Any = None          # DailyBriefGenerator
    portfolio: Any = None      # PortfolioWorkspace
    reasoning: Any = None      # AIReasoningEngine (optional LLM)
    store: Any = None          # ArtifactStore
    default_recipients: list[str] | None = None


# ------------------------------------------------------------ summarization
def _extractive_summary(text: str, sentences: int = SUMMARY_SENTENCES) -> str:
    """Deterministic fallback: the opening sentences, which is where SOPs,
    RCAs, and minutes state what they are about."""
    text = re.sub(r"\s+", " ", text or "").strip()
    parts = re.split(r"(?<=[.!?])\s+", text)
    return " ".join(parts[:sentences])[:600]


def _summarize(context: V2Context, kind: str, document: dict,
               instruction: str) -> str:
    """LLM summary when a provider is configured, extractive otherwise."""
    text = document.get("text_preview", "")
    if context.reasoning is not None:
        try:
            answer = context.reasoning.answer(
                f"{instruction} Answer in 3-4 plain business sentences.",
                {"document_name": document["name"], "document_kind": kind,
                 "document_text": text})
            if answer.get("status") == "ok" and answer.get("answer"):
                return str(answer["answer"])[:800]
        except Exception:  # noqa: BLE001 — the fallback is the contract
            logger.exception("LLM summarization failed for %s",
                             document["name"])
    return _extractive_summary(text)


def _summarize_documents(context: V2Context, workflow: str, category: str,
                         instruction: str, notify_prefix: str) -> dict:
    """The shared engine of every document-summarization workflow."""
    documents = context.documents.unprocessed(workflow, category,
                                              limit=MAX_DOCS_PER_RUN)
    summarized = 0
    for document in documents:
        summary = _summarize(context, category, document, instruction)
        if summary:
            context.knowledge.record_insight(
                f"[{notify_prefix}] {document['name']}: {summary}",
                statement_type="fact", source=f"workflow:{workflow}")
            context.notifications.notify(
                "recommendation", f"{notify_prefix}: {document['name']}",
                detail=summary[:480],
                ref=f"{workflow}:{document['document_id']}"
                    f":v{document['version']}")
        context.documents.mark_processed(document["document_id"], workflow,
                                         document["version"])
        summarized += 1
    return {"documents": summarized}


# -------------------------------------------------------- document workflows
def _run_rca_summarization(context: V2Context):
    def run(project_id: str) -> dict:
        return _summarize_documents(
            context, "rca_summarization", "rca",
            "Summarize this root-cause analysis: what failed, the root "
            "cause, and the corrective actions.", "RCA summary")
    return run


def _run_meeting_summarization(context: V2Context):
    def run(project_id: str) -> dict:
        return _summarize_documents(
            context, "meeting_summarization", "meeting",
            "Summarize this meeting: decisions made, topics discussed, and "
            "open questions.", "Meeting summary")
    return run


def _run_sop_change_detection(context: V2Context):
    def run(project_id: str) -> dict:
        """A changed SOP is an operational event: the manager is notified and
        a review task is created. Version 1 of a document is its arrival, not
        a change."""
        documents = context.documents.unprocessed(
            "sop_change_detection", "sop", limit=MAX_DOCS_PER_RUN)
        changes = 0
        for document in documents:
            if document.get("version", 1) > 1:
                context.notifications.notify(
                    "recommendation",
                    f"SOP changed: {document['name']}",
                    detail=f"Now at version {document['version']}. "
                           f"{document.get('text_preview', '')[:200]}",
                    ref=f"sop_change:{document['document_id']}"
                        f":v{document['version']}")
                context.tasks.create(
                    f"Review the change to SOP '{document['name']}'",
                    detail="The document was updated at its source; confirm "
                           "the process change is intended and communicated.",
                    status="pending", priority=2, source_kind="communication",
                    source_ref=f"sop_change:{document['document_id']}"
                               f":v{document['version']}")
                changes += 1
            context.documents.mark_processed(
                document["document_id"], "sop_change_detection",
                document["version"])
        return {"documents": len(documents), "changes": changes}
    return run


def _run_action_item_extraction(context: V2Context):
    def run(project_id: str) -> dict:
        """Action items hide in meeting notes as 'Action:', 'TODO:', and
        checkbox lines; each becomes an executive task, deduplicated by the
        queue-style signature the task manager already keeps."""
        documents = context.documents.unprocessed(
            "action_item_extraction", "meeting", limit=MAX_DOCS_PER_RUN)
        extracted = 0
        for document in documents:
            items = _action_items(document.get("text_preview", ""))
            for i, item in enumerate(items[:MAX_ACTION_ITEMS_PER_MEETING]):
                task = context.tasks.create(
                    item[:200],
                    detail=f"Action item from '{document['name']}'",
                    status="pending", priority=3,
                    source_kind="communication",
                    source_ref=f"action_item:{document['document_id']}"
                               f":v{document['version']}:{i}")
                if task is not None:
                    extracted += 1
            context.documents.mark_processed(
                document["document_id"], "action_item_extraction",
                document["version"])
        return {"documents": len(documents), "action_items": extracted}
    return run


def _action_items(text: str) -> list[str]:
    items = []
    for line in (text or "").splitlines():
        match = ACTION_LINE.match(line)
        if match and len(match.group(1).strip()) > 5:
            items.append(match.group(1).strip())
    return items


# -------------------------------------------------------- drafting workflows
def _run_email_drafting(context: V2Context):
    def run(project_id: str) -> dict:
        """Draft the daily executive status email and queue it for approval.
        Nothing sends without a human: the queued ``send_email`` action is
        the Approval Engine's to approve, edit, or reject."""
        brief = context.brief.today() if context.brief is not None else {}
        subject, body = _status_email(context, brief)
        action = context.queue.submit(
            "send_email", f"Daily status email: {subject}",
            payload={"to": list(context.default_recipients or []),
                     "subject": subject, "body": body},
            detail="Drafted automatically from today's executive brief. "
                   "Edit recipients and content before approving.",
            priority=3, source="workflow:email_drafting",
            source_ref=f"daily_status_email:{brief.get('date', '')}")
        return {"drafted": action is not None,
                "action_id": action["action_id"] if action else ""}
    return run


def _status_email(context: V2Context, brief: dict) -> tuple[str, str]:
    date = brief.get("date", "today")
    issues = brief.get("high_priority_issues", [])
    changes = brief.get("portfolio_changes", [])
    recommendations = brief.get("recommendations", [])
    if context.reasoning is not None:
        try:
            answer = context.reasoning.answer(
                "Write a short executive status email body (plain text, no "
                "salutation placeholders) from this daily brief.",
                {"brief": {"issues": issues[:5], "changes": changes[:5],
                           "recommendations": recommendations[:5]}})
            if answer.get("status") == "ok" and answer.get("answer"):
                return (f"Executive status — {date}",
                        str(answer["answer"])[:4000])
        except Exception:  # noqa: BLE001
            logger.exception("LLM email drafting failed")
    lines = [f"Executive status for {date}.", ""]
    if issues:
        lines.append("High-priority issues:")
        lines += [f"  - {i.get('title', '')}" for i in issues[:5]]
    if changes:
        lines.append("Portfolio changes:")
        lines += [f"  - {c.get('project_id', '')}: {c.get('previous')} → "
                  f"{c.get('latest')}" for c in changes[:5]]
    if recommendations:
        lines.append("Recommended actions:")
        lines += [f"  - {r.get('action', '')}" for r in recommendations[:5]]
    if len(lines) == 2:
        lines.append("No open issues — portfolio is stable.")
    return f"Executive status — {date}", "\n".join(lines)


def _run_teams_drafting(context: V2Context):
    def run(project_id: str) -> dict:
        """Draft the morning Teams announcement and queue it for approval."""
        brief = context.brief.today() if context.brief is not None else {}
        issues = brief.get("high_priority_issues", [])
        headline = (f"{len(issues)} high-priority issue(s) need attention"
                    if issues else "portfolio is stable")
        text = f"**Daily update ({brief.get('date', 'today')})** — {headline}."
        for issue in issues[:3]:
            text += f"\n- {issue.get('title', '')}"
        action = context.queue.submit(
            "send_message", "Daily Teams update",
            payload={"channel": "", "text": text},
            detail="Drafted automatically from today's executive brief.",
            priority=3, source="workflow:teams_drafting",
            source_ref=f"daily_teams_update:{brief.get('date', '')}")
        return {"drafted": action is not None,
                "action_id": action["action_id"] if action else ""}
    return run


def _run_presentation_drafting(context: V2Context):
    def run(project_id: str) -> dict:
        """Draft the weekly portfolio review deck as a markdown outline the
        manager exports; a task points them at it."""
        overview = (context.portfolio.overview()
                    if context.portfolio is not None else {})
        health = overview.get("portfolio_health", {})
        slides = [
            "# Weekly Portfolio Review",
            "## Portfolio health\n"
            f"- Average health score: {health.get('average_health_score', 'n/a')}\n"
            f"- Businesses tracked: {health.get('projects_total', 0)}",
        ]
        reports = (overview.get("business_performance", {})
                   or {}).get("recent_reports", [])
        if reports:
            slides.append("## Recent reports\n" + "\n".join(
                f"- {r.get('title', '')} (health "
                f"{r.get('health_score', 'n/a')})" for r in reports[:6]))
        recommendations = context.knowledge.recommendations(6)
        if recommendations:
            slides.append("## Recommended actions\n" + "\n".join(
                f"- {r.get('action', '')}" for r in recommendations))
        outline = "\n\n".join(slides)
        if context.store is not None:
            context.store.save("_enterprise", "presentation_draft", {
                "title": "Weekly Portfolio Review", "format": "markdown",
                "outline": outline})
        context.tasks.create(
            "Review the drafted weekly portfolio presentation",
            detail="An outline was drafted from portfolio intelligence — "
                   "open Reports to review and export it.",
            status="pending", priority=3, source_kind="communication",
            source_ref=f"presentation_draft:{overview.get('generated_at', '')[:10]}")
        return {"drafted": True, "slides": len(slides)}
    return run


# ---------------------------------------------------------------- registry
def build_v2_workflows(context: V2Context) -> list[WorkflowDefinition]:
    """Every V2 workflow, as engine-registrable definitions."""
    document_workflows = [
        ("rca_summarization",
         "Summarize new and updated RCA documents into organizational "
         "knowledge", _run_rca_summarization),
        ("sop_change_detection",
         "Detect SOP changes and open review tasks",
         _run_sop_change_detection),
        ("meeting_summarization",
         "Summarize new meeting notes: decisions, topics, open questions",
         _run_meeting_summarization),
        ("action_item_extraction",
         "Extract action items from meeting notes into executive tasks",
         _run_action_item_extraction),
    ]
    drafting_workflows = [
        ("email_drafting",
         "Draft the daily executive status email for approval",
         _run_email_drafting),
        ("teams_message_drafting",
         "Draft the daily Teams announcement for approval",
         _run_teams_drafting),
        ("presentation_drafting",
         "Draft the weekly portfolio review presentation outline",
         _run_presentation_drafting),
    ]
    definitions = []
    for group, tag in ((document_workflows, "documents"),
                       (drafting_workflows, "drafting")):
        for name, description, factory in group:
            definitions.append(WorkflowDefinition(
                name, description, runner=factory(context), autonomous=True,
                scope="enterprise", tags=["v2", tag]))
    return definitions

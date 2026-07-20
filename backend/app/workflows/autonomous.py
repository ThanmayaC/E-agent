"""Autonomous workflows — chains that execute without a user.

The SDS daily cycle, as an ordered chain the Workflow Engine executes on the
scheduler's cadence:

    Refresh portfolio → Analyse new data → Update Enterprise Brain
      → Generate Daily Brief → Create Tasks → Generate Recommendations
      → Queue Communications

Each step is a small function over the services the platform already owns —
nothing here reimplements analysis, learning, or briefing; it *orders* them
and lets the results flow forward. Steps that depend on optional surfaces
(the Brain, LLM-derived recommendations) are marked optional: an autonomous
cycle degrades to what is available rather than failing the day.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from app.core.logging import get_logger
from app.workflows.engine import WorkflowDefinition, WorkflowStep

logger = get_logger(__name__)

# A project whose latest report is older than this is a candidate for an
# autonomous re-analysis when new data has landed.
STALE_REPORT_HOURS = 24


@dataclass
class AutonomousContext:
    """Everything the autonomous chains need, injected by the runtime.

    Holding the collaborators here (rather than importing them) keeps the
    chains testable with fakes and keeps the workflow layer free of any
    dependency on the container.
    """
    store: Any                 # ArtifactStore
    knowledge: Any             # KnowledgeStore
    manager: Any               # ManagerWorkspace
    portfolio: Any             # PortfolioWorkspace
    brief: Any                 # DailyBriefGenerator
    tasks: Any                 # ExecutiveTaskManager
    notifications: Any         # NotificationCenter
    queue: Any                 # ActionQueue
    bus: Any                   # EventBus
    decisions: Any = None      # DecisionEngine
    brain: Any = None          # EnterpriseBrain
    orchestrator: Any = None   # analysis graph / legacy workflow


# --------------------------------------------------------------- the steps
def _refresh_portfolio(context: AutonomousContext):
    def step(project_id: str, prior: dict) -> dict:
        overview = context.portfolio.overview()
        health = overview["portfolio_health"]
        previous = context.store.load("_enterprise", "portfolio_snapshot",
                                      {}) or {}
        current = health.get("average_health_score")
        before = previous.get("average_health_score")
        context.store.save("_enterprise", "portfolio_snapshot", health)

        if current is not None and before is not None:
            change = round(current - before, 2)
            if abs(change) >= 1.0:
                context.bus.publish(
                    "PortfolioChanged",
                    {"average_health_score": current, "previous": before,
                     "health_change": change,
                     "projects_attention": health.get("projects_attention", 0)},
                    source="autonomous.refresh_portfolio")
        return {"projects": health.get("projects_total", 0),
                "average_health_score": current}
    return step


def _analyse_new_data(context: AutonomousContext):
    """Re-analyse projects whose uploads changed since their last report.

    The agent does not re-run analysis for its own sake: a project is
    analysed when it has data the current report has never seen.
    """
    def step(project_id: str, prior: dict) -> dict:
        analysed, skipped = [], 0
        for pid in context.store.list_projects():
            state = context.store.load(pid, "state") or {}
            if not state or state.get("status") in ("analyzing",
                                                    "awaiting_clarification"):
                skipped += 1
                continue
            if not _has_new_data(context, pid, state):
                skipped += 1
                continue
            if context.orchestrator is None:
                skipped += 1
                continue
            try:
                context.orchestrator.run(pid)
                analysed.append(pid)
                context.bus.publish("DatasetImported",
                                    {"project_id": pid,
                                     "reason": "new data since last report"},
                                    project_id=pid,
                                    source="autonomous.analyse_new_data")
            except Exception:  # noqa: BLE001 — one project never stops the cycle
                logger.exception("Autonomous analysis failed for %s", pid)
        return {"analysed": analysed, "skipped": skipped}
    return step


def _has_new_data(context: AutonomousContext, project_id: str,
                  state: dict) -> bool:
    uploads_dir = context.store.uploads_dir(project_id)
    if not uploads_dir.exists():
        return False
    reported_at = state.get("report_generated_at") or ""
    if not reported_at:
        return any(uploads_dir.iterdir())
    try:
        reported = datetime.fromisoformat(reported_at)
    except ValueError:
        return False
    if reported.tzinfo is None:
        reported = reported.replace(tzinfo=timezone.utc)
    return any(
        datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc) > reported
        for f in uploads_dir.iterdir() if f.is_file())


def _update_brain(context: AutonomousContext):
    def step(project_id: str, prior: dict) -> dict:
        if context.brain is None:
            return {"skipped": "brain disabled"}
        learned = []
        for pid in (prior.get("analyse_new_data", {}) or {}).get("analysed", []):
            try:
                context.brain.learn_after_analysis(pid)
                learned.append(pid)
                context.bus.publish("KnowledgeUpdated",
                                    {"project_id": pid,
                                     "source": "continuous_learning_pipeline"},
                                    project_id=pid,
                                    source="autonomous.update_brain")
            except Exception:  # noqa: BLE001 — learning degrades, never fails
                logger.exception("Autonomous brain update failed for %s", pid)
        return {"learned": learned, "brain_state": context.brain.state}
    return step


def _generate_daily_brief(context: AutonomousContext):
    def step(project_id: str, prior: dict) -> dict:
        brief = context.brief.generate()
        context.bus.publish("ReportGenerated",
                            {"kind": "daily_brief", "date": brief["date"],
                             "portfolio_health": brief.get("portfolio_health"),
                             "high_priority_issues":
                                 brief.get("high_priority_issues")},
                            source="autonomous.daily_brief")
        return {"date": brief["date"],
                "high_priority_issues": brief.get("high_priority_issues")}
    return step


def _create_tasks(context: AutonomousContext):
    def step(project_id: str, prior: dict) -> dict:
        created = 0
        for pid in (prior.get("analyse_new_data", {}) or {}).get("analysed", []):
            try:
                outcome = context.manager.refresh_after_analysis(pid)
                created += outcome.get("tasks_created", 0)
            except Exception:  # noqa: BLE001 — the workspace refresh degrades
                logger.exception("Autonomous workspace refresh failed for %s",
                                 pid)
        created += context.tasks.generate_from_approvals(
            context.manager.pending_approvals())
        return {"tasks_created": created}
    return step


def _generate_recommendations(context: AutonomousContext):
    """Route every fresh recommendation through the Decision Engine, which
    decides what needs a human and what the agent may act on itself."""
    def step(project_id: str, prior: dict) -> dict:
        if context.decisions is None:
            return {"skipped": "decision engine unavailable"}
        decided = {"decided": 0, "skipped": 0}
        for pid in context.store.list_projects():
            report = context.store.load(pid, "report", {}) or {}
            ai = context.store.load(pid, "ai_report", {}) or {}
            recommendations = list(report.get("deterministic_recommendations")
                                   or [])
            if ai.get("status") == "ok":
                recommendations += [r for r in (ai.get("recommendations") or [])
                                    if isinstance(r, dict)]
            if not recommendations:
                continue
            outcome = context.decisions.decide_many(
                recommendations[:10], project_id=pid,
                source="autonomous.recommendations")
            decided["decided"] += outcome["decided"]
            decided["skipped"] += outcome["skipped"]
        return decided
    return step


def _queue_communications(context: AutonomousContext):
    """Queue the day's outbound communication for approval.

    Nothing is sent: the Communication Module's providers arrive in V2. The
    queue is where they will plug in, so the approval trail exists before
    the first email ever does.
    """
    def step(project_id: str, prior: dict) -> dict:
        brief = prior.get("generate_daily_brief") or {}
        issues = brief.get("high_priority_issues") or 0
        queued = 0
        if issues:
            action = context.queue.submit(
                "send_email",
                f"Email the executive brief for {brief.get('date', 'today')}",
                payload={"kind": "daily_brief", "date": brief.get("date"),
                         "high_priority_issues": issues},
                detail=f"{issues} high-priority issue(s) need the executive's "
                       f"attention today.",
                priority=2, source="autonomous.queue_communications",
                source_ref=f"daily_brief:{brief.get('date', '')}")
            queued += 1 if action else 0
        return {"queued": queued, "pending_approval":
                len(context.queue.pending_approvals())}
    return step


# -------------------------------------------------------------- the chains
def build_autonomous_workflows(context: AutonomousContext
                               ) -> list[WorkflowDefinition]:
    """The autonomous chains, registered on the standard Workflow Engine so
    they share its run history, failure notifications, and monitoring UI."""
    daily_cycle = WorkflowDefinition(
        "daily_cycle",
        "The autonomous enterprise cycle: refresh the portfolio, analyse new "
        "data, update the Enterprise Brain, brief the executive, create "
        "tasks, decide on recommendations, and queue communications",
        autonomous=True, scope="enterprise",
        tags=["autonomous", "daily", "core"],
        steps=[
            WorkflowStep("refresh_portfolio",
                         "Recompute portfolio health and announce material "
                         "changes", _refresh_portfolio(context)),
            WorkflowStep("analyse_new_data",
                         "Re-analyse every project whose data changed since "
                         "its last report", _analyse_new_data(context),
                         optional=True),
            WorkflowStep("update_brain",
                         "Feed new analysis into the Enterprise Brain's "
                         "continuous learning pipeline", _update_brain(context),
                         optional=True),
            WorkflowStep("generate_daily_brief",
                         "Generate today's executive brief",
                         _generate_daily_brief(context)),
            WorkflowStep("create_tasks",
                         "Turn new findings and approvals into executive tasks",
                         _create_tasks(context), optional=True),
            WorkflowStep("generate_recommendations",
                         "Run recommendations through the Decision Engine",
                         _generate_recommendations(context), optional=True),
            WorkflowStep("queue_communications",
                         "Queue outbound communication for approval",
                         _queue_communications(context), optional=True),
        ])

    background_intelligence = WorkflowDefinition(
        "background_intelligence",
        "Continuous background refresh: portfolio, brain, brief, and "
        "recommendations — no user interaction",
        autonomous=True, scope="enterprise",
        tags=["autonomous", "background"],
        steps=[
            WorkflowStep("refresh_portfolio", "Recompute portfolio health",
                         _refresh_portfolio(context)),
            WorkflowStep("generate_daily_brief", "Refresh today's brief",
                         _generate_daily_brief(context), optional=True),
            WorkflowStep("generate_recommendations",
                         "Decide on any new recommendations",
                         _generate_recommendations(context), optional=True),
        ])

    monitoring = WorkflowDefinition(
        "monitoring",
        "Continuously monitor portfolio health, risks, and deadlines, and "
        "raise alerts on anomalies",
        autonomous=True, scope="enterprise",
        tags=["autonomous", "monitoring", "alerts"],
        steps=[
            WorkflowStep("refresh_portfolio", "Recompute portfolio health",
                         _refresh_portfolio(context)),
            WorkflowStep("check_deadlines", "Notify on tasks due soon",
                         _check_deadlines(context)),
        ])

    return [daily_cycle, background_intelligence, monitoring]


def _check_deadlines(context: AutonomousContext):
    def step(project_id: str, prior: dict) -> dict:
        notified = 0
        for task in context.tasks.due_soon(3):
            if context.notifications.notify(
                    "task_deadline", f"Task due soon: {task['title']}",
                    project_id=task.get("project_id", ""),
                    ref=f"deadline:{task['task_id']}"):
                notified += 1
                context.bus.publish("NotificationCreated",
                                    {"kind": "task_deadline",
                                     "task_id": task["task_id"]},
                                    project_id=task.get("project_id", ""),
                                    source="autonomous.monitoring")
        return {"deadline_notifications": notified}
    return step

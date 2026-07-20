"""Executive Workspace (Manager Module) — tasks, decisions, reviews,
notifications, daily brief, workspace refresh, and the /manager APIs."""
from __future__ import annotations

import pytest

from app.communication.notifications import NotificationCenter
from app.communication.providers import ProviderNotConfigured, ProviderRegistry
from app.knowledge.store import KnowledgeStore
from app.manager import (
    DailyBriefGenerator, DecisionCenter, ExecutiveTaskManager, ManagerStore,
    ManagerWorkspace, PortfolioWorkspace, ReportReviewCenter,
)
from app.repositories.artifact_store import ArtifactStore

PID = "proj_exec01"

AI_REPORT = {
    "status": "ok",
    "priority_actions": ["Investigate failed transactions",
                         "Expand North region coverage"],
    "recommendations": [{"action": "Collect merchant category data",
                         "priority": 2, "expected_impact": "medium"}],
    "risks": [{"risk": "Failure rate is rising", "severity": "critical"},
              {"risk": "Cosmetic gap", "severity": "low"}],
    "opportunities": [{"opportunity": "North region growth",
                       "impact": "high"}],
}


@pytest.fixture()
def ws(tmp_path):
    store = ArtifactStore(tmp_path / "projects")
    knowledge = KnowledgeStore(tmp_path / "knowledge")
    mstore = ManagerStore(tmp_path / "manager")
    notifications = NotificationCenter(tmp_path / "manager")
    tasks = ExecutiveTaskManager(mstore)
    decisions = DecisionCenter(mstore, knowledge)
    reviews = ReportReviewCenter(mstore, notifications)
    portfolio = PortfolioWorkspace(store, knowledge)
    brief = DailyBriefGenerator(mstore, knowledge, notifications, tasks,
                                portfolio)
    workspace = ManagerWorkspace(store, knowledge, tasks, decisions, reviews,
                                 notifications, portfolio, brief)
    store.save(PID, "state", {"project_id": PID, "name": "Fintech P1",
                              "status": "ready", "report_version": 1})
    store.save(PID, "business_context",
               {"executive_metrics": {"health_score": 64.0}})
    store.save(PID, "ai_report", AI_REPORT)
    store.save(PID, "report", {"deterministic_recommendations": [
        {"action": "Improve data quality of transactions",
         "trigger": "critical data-quality issue"}]})
    return workspace


# ------------------------------------------------------------------- tasks
def test_tasks_generated_and_deduplicated(ws):
    created = ws.tasks.generate_from_report(PID, 1, AI_REPORT, [])
    assert created == 3  # 2 priority actions + 1 recommendation
    assert ws.tasks.generate_from_report(PID, 1, AI_REPORT, []) == 0
    pending = ws.tasks.tasks(status="pending")
    assert pending[0]["priority"] == 1
    suggested = ws.tasks.tasks(status="suggested")
    assert suggested and suggested[0]["source_kind"] == "recommendation"


def test_task_lifecycle(ws):
    task = ws.tasks.create("Prepare board summary", due_date="2026-07-17")
    updated = ws.tasks.update_status(task["task_id"], "completed")
    assert updated["status"] == "completed" and updated["completed_at"]
    with pytest.raises(ValueError):
        ws.tasks.update_status(task["task_id"], "nonsense")
    assert ws.tasks.due_soon(3) == []  # completed tasks have no deadline


# --------------------------------------------------------------- decisions
def test_decision_center_records_and_tracks(ws):
    d = ws.decisions.record("Focus Q3 on merchant retention",
                            owner="COO", impact="high",
                            project_id=PID, evidence_ids=["kpi:churn"])
    assert d["status"] == "proposed"
    updated = ws.decisions.update(d["decision_id"], status="approved",
                                  by="CEO")
    assert updated["status"] == "approved"
    assert [h["status"] for h in updated["history"]] == ["proposed",
                                                         "approved"]
    # decision memory learned it too (Brain input)
    assert any("merchant retention" in x["decision"]
               for x in ws.knowledge.decisions(10))


# ----------------------------------------------------------------- reviews
def test_report_review_workflow(ws):
    review = ws.reviews.register(PID, 1, "Fintech P1 — report v1", 64.0)
    assert review["status"] == "review"
    assert ws.reviews.register(PID, 1, "dup", 64.0) is None  # idempotent
    # new-report notification raised once
    kinds = [n["kind"] for n in ws.notifications.recent(10)]
    assert kinds.count("new_report") == 1
    approved = ws.reviews.set_status(review["review_id"], "approved",
                                     by="CFO", note="looks right")
    assert approved["status"] == "approved"
    with pytest.raises(ValueError):  # approved → review is not a transition
        ws.reviews.set_status(review["review_id"], "review")
    archived = ws.reviews.set_status(review["review_id"], "archived")
    assert [h["status"] for h in archived["history"]] == \
        ["review", "approved", "archived"]


# ------------------------------------------------------------ notifications
def test_notifications_dedupe_and_read(ws):
    n1 = ws.notifications.notify("critical_risk", "Risk A", ref="r1",
                                 project_id=PID)
    assert n1 is not None
    assert ws.notifications.notify("critical_risk", "Risk A", ref="r1",
                                   project_id=PID) is None
    assert ws.notifications.unread_count() == 1
    assert ws.notifications.mark_read(n1["notification_id"])
    assert ws.notifications.unread_count() == 0
    with pytest.raises(ValueError):
        ws.notifications.notify("teams_message", "not internal")


# ------------------------------------------------------- workspace runtime
def test_refresh_after_analysis_populates_workspace(ws):
    result = ws.refresh_after_analysis(PID)
    assert result["tasks_created"] >= 4  # 2 priority + 1 AI rec + 1 rule rec
    # critical risk notified, low severity not
    risks = ws.notifications.recent(20, kind="critical_risk")
    assert len(risks) == 1 and "Failure rate" in risks[0]["detail"]
    # re-running is idempotent
    again = ws.refresh_after_analysis(PID)
    assert again["tasks_created"] == 0 and again["notifications"] == 0

    payload = ws.workspace()
    assert payload["todays_summary"]["portfolio_health"]["projects_total"] == 1
    assert payload["pending_reviews"]
    assert payload["pending_tasks"]
    assert payload["recent_notifications"]
    assert payload["upcoming_meetings"] == []  # V2

    dash = ws.dashboard()
    assert dash["business_health"]["projects_total"] == 1
    assert dash["operational_status"]["analyses_ready"] == 1
    assert "knowledge_graph" not in dash  # no technical internals
    assert dash["recommended_actions"]


def test_daily_brief_generated_once_per_day(ws):
    ws.refresh_after_analysis(PID)
    brief = ws.brief.today()
    assert brief["open_action_items"]
    assert any("Failure rate" in i["detail"]
               for i in brief["high_priority_issues"])
    assert ws.brief.today()["generated_at"] == brief["generated_at"]  # cached
    assert ws.brief.generate()["generated_at"] != brief["generated_at"]


def test_workflow_failure_notification(ws):
    ws.notify_workflow_failure("full_analysis", PID, "boom")
    failures = ws.notifications.recent(10, kind="workflow_failure")
    assert failures and "full_analysis" in failures[0]["title"]


# ----------------------------------------------------- provider interfaces
def test_provider_registry_prepared_but_empty():
    registry = ProviderRegistry()
    slots = registry.describe()
    # V2.2 added the generic outbound channels (rest, webhook) alongside the
    # V1 vocabulary; every slot is still empty until an adapter is configured.
    assert {s["kind"] for s in slots} == {"email", "calendar", "meeting",
                                          "messaging", "document", "task",
                                          "rest", "webhook"}
    assert all(not s["available"] for s in slots)
    with pytest.raises(ProviderNotConfigured):
        registry.get("email")

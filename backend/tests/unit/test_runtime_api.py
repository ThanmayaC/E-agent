"""The /runtime surface and the autonomous workflow chain, driven through
the real container: the app boots, the heartbeat starts, and the agent is
working before anyone calls it.
"""
from __future__ import annotations

import os

import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def client(tmp_path_factory):
    os.environ["EDIP_DATA_DIR"] = str(tmp_path_factory.mktemp("runtime_data"))
    os.environ["EDIP_LLM_PROVIDER"] = "mock"
    from app.core import config, container
    config.get_settings.cache_clear()
    container.get_container.cache_clear()
    from app.main import create_app
    with TestClient(create_app()) as c:  # lifespan → brain, workspace, runtime
        yield c
    config.get_settings.cache_clear()
    container.get_container.cache_clear()


@pytest.fixture(scope="module")
def runtime():
    from app.core.container import get_container
    return get_container().runtime


# ---------------------------------------------------------------- startup
def test_the_agent_is_autonomous_the_moment_the_app_boots(client):
    body = client.get("/api/v1/runtime").json()

    assert body["running"] is True, "the heartbeat did not start with the app"
    assert body["autonomy"] == "active"
    assert body["scheduler"]["jobs_total"] > 0


def test_startup_jobs_ran_before_traffic_arrived(client):
    jobs = {j["name"]: j for j in client.get("/api/v1/runtime/jobs").json()}

    assert jobs["startup_portfolio"]["runs"] >= 1
    assert jobs["startup_knowledge"]["runs"] >= 1


def test_default_trigger_rules_are_installed(client):
    rules = {r["name"] for r in
             client.get("/api/v1/runtime/triggers").json()["rules"]}

    assert {"risk_increase_creates_task", "report_approved_generates_summary",
            "new_dataset_refreshes_brain", "anomaly_creates_recommendation",
            "low_confidence_creates_investigation"} <= rules


def test_every_runtime_dashboard_endpoint_answers(client):
    for path in ("/api/v1/runtime/jobs", "/api/v1/runtime/events",
                 "/api/v1/runtime/actions", "/api/v1/runtime/goals",
                 "/api/v1/runtime/queue", "/api/v1/runtime/executions",
                 "/api/v1/runtime/scheduler", "/api/v1/runtime/plans",
                 "/api/v1/runtime/decisions", "/api/v1/runtime/triggers",
                 "/api/v1/runtime/metrics", "/api/v1/runtime/activity"):
        assert client.get(path).status_code == 200, path


# ------------------------------------------------------ goals and planning
def test_a_new_goal_is_planned_without_anyone_asking(client):
    goal = client.post("/api/v1/runtime/goals", json={
        "objective": "Raise portfolio health to 90",
        "deadline": "2027-01-01", "owner": "cfo",
        "kpis": [{"name": "health", "target": 90.0,
                  "metric": "portfolio.average_health_score"}],
    }).json()

    plan = client.get(f"/api/v1/runtime/goals/{goal['goal_id']}").json()["plan"]
    assert plan is not None, "the goal was accepted but never planned"
    assert plan["status"] == "active"
    assert plan["steps"], "the plan has no steps"


def test_metrics_expose_the_names_a_kpi_can_point_at(client):
    metrics = client.get("/api/v1/runtime/metrics").json()

    assert "portfolio.projects_total" in metrics
    assert "tasks.open" in metrics


def test_a_kpi_without_a_target_is_rejected(client):
    response = client.post("/api/v1/runtime/goals", json={
        "objective": "Vague ambition",
        "kpis": [{"name": "something", "target": None}]})

    assert response.status_code == 422


# --------------------------------------------------- queue and approvals
def test_an_email_action_waits_for_a_human_then_executes(client):
    action = client.post("/api/v1/runtime/actions", json={
        "kind": "send_email", "title": "Email the quarterly brief",
        "detail": "Goes to the board"}).json()
    assert action["status"] == "pending_approval"

    approved = client.post(
        f"/api/v1/runtime/actions/{action['action_id']}/approve",
        json={"by": "cfo"}).json()
    assert approved["status"] == "approved"
    assert approved["approved_by"] == "cfo"

    # No executor is registered for send_email (V2 providers) — the action
    # holds its approval instead of vanishing.
    executed = client.post(
        f"/api/v1/runtime/actions/{action['action_id']}/execute")
    assert executed.status_code == 422
    assert "No executor" in executed.json()["detail"]


def test_a_rejected_action_cannot_be_executed(client):
    action = client.post("/api/v1/runtime/actions", json={
        "kind": "send_email", "title": "Email something unwise"}).json()
    client.post(f"/api/v1/runtime/actions/{action['action_id']}/reject",
                json={"by": "cfo", "reason": "not appropriate"})

    response = client.post(
        f"/api/v1/runtime/actions/{action['action_id']}/execute")
    assert response.status_code == 422


def test_an_internal_action_executes_autonomously(client):
    action = client.post("/api/v1/runtime/actions", json={
        "kind": "create_task", "title": "Review the North region pipeline",
        "priority": 3}).json()
    assert action["status"] == "approved", "an internal task needed approval"

    executed = client.post(
        f"/api/v1/runtime/actions/{action['action_id']}/execute").json()
    assert executed["status"] == "executed"

    titles = [t["title"] for t in
              client.get("/api/v1/manager/tasks").json()["tasks"]]
    assert "Review the North region pipeline" in titles


def test_pending_approvals_reach_the_executive_workspace(client):
    client.post("/api/v1/runtime/actions", json={
        "kind": "send_email", "title": "Email the weekly summary"})
    approvals = client.get("/api/v1/manager/workspace").json()["pending_approvals"]

    assert any(a["kind"] == "action_approval"
               and "Email the weekly summary" in a["title"] for a in approvals)


# --------------------------------------------------------------- triggers
def test_an_approved_report_triggers_an_executive_summary(client, runtime):
    from app.core.container import get_container
    c = get_container()
    c.store.save("proj_trig", "state", {"project_id": "proj_trig",
                                        "name": "Trigger Co",
                                        "status": "ready", "report_version": 1})
    review = c.reviews.register("proj_trig", 1, "Trigger Co — report v1", 70.0)

    client.post(f"/api/v1/manager/reports/{review['review_id']}/status",
                json={"status": "approved", "by": "cfo"})

    queued = [a["title"] for a in
              client.get("/api/v1/runtime/actions").json()["actions"]]
    assert any("Report approved" in t for t in queued), \
        "approving a report did not trigger an executive summary"


def test_a_custom_trigger_rule_fires_on_its_event(client, runtime):
    rule = client.post("/api/v1/runtime/triggers", json={
        "name": "test_health_watch", "event": "PortfolioChanged",
        "action": "create_task",
        "conditions": [{"field": "health_change", "op": "lte", "value": -20}],
        "params": {"title": "Emergency: health collapsed", "priority": 1},
    }).json()

    runtime.bus.publish("PortfolioChanged", {"health_change": -30.0})

    titles = [a["title"] for a in
              client.get("/api/v1/runtime/actions").json()["actions"]]
    assert "Emergency: health collapsed" in titles

    fired = next(r for r in client.get("/api/v1/runtime/triggers").json()["rules"]
                 if r["rule_id"] == rule["rule_id"])
    assert fired["fires"] == 1


def test_an_invalid_trigger_rule_is_rejected(client):
    response = client.post("/api/v1/runtime/triggers", json={
        "name": "bad", "event": "NotARealEvent", "action": "create_task"})

    assert response.status_code == 422


# ------------------------------------------------- the autonomous cycle
def test_the_daily_cycle_runs_end_to_end_without_a_user(client):
    run = client.post("/api/v1/runtime/jobs/daily_cycle/run").json()

    assert run["status"] == "completed", run.get("error")
    steps = client.get("/api/v1/runtime/activity").json()["recent_runs"]
    cycle = next(r for r in steps if r["workflow"] == "daily_cycle")
    completed = [s["name"] for s in cycle["steps"]
                 if s["status"] == "completed"]
    assert {"refresh_portfolio", "generate_daily_brief"} <= set(completed)


def test_the_autonomous_cycle_produced_a_brief_and_events(client):
    client.post("/api/v1/runtime/jobs/daily_cycle/run")
    brief = client.get("/api/v1/manager/daily-brief").json()
    kinds = {e["kind"] for e in
             client.get("/api/v1/runtime/events").json()["events"]}

    assert brief["date"], "the cycle did not generate a brief"
    assert {"WorkflowCompleted", "ReportGenerated"} <= kinds


def test_the_workspace_reports_what_the_agent_is_doing(client):
    autonomy = client.get("/api/v1/manager/workspace").json()["autonomy"]

    assert autonomy["status"] == "active"
    assert autonomy["scheduled_jobs"], "no scheduled jobs surfaced"
    assert "goal_progress" in autonomy
    assert autonomy["summary"]["jobs_running"] > 0


def test_the_dashboard_shows_the_autonomy_strip(client):
    status = client.get("/api/v1/manager/dashboard").json()["automation_status"]

    assert status["autonomy"] == "active"
    assert status["jobs_scheduled"] > 0


# -------------------------------------------------------------- lifecycle
def test_the_heartbeat_can_be_stopped_and_restarted(client):
    assert client.post("/api/v1/runtime/scheduler/stop").json()["running"] is False
    assert client.post("/api/v1/runtime/scheduler/start").json()["running"] is True


def test_running_an_unknown_job_is_a_404(client):
    assert client.post("/api/v1/runtime/jobs/not_a_job/run").status_code == 404

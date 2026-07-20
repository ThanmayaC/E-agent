"""Targeted API smoke test for the /manager surface (no analysis run)."""
from __future__ import annotations

import os

import pytest
from fastapi.testclient import TestClient

from app.communication.providers import PROVIDER_KINDS


@pytest.fixture(scope="module")
def client(tmp_path_factory):
    os.environ["EDIP_DATA_DIR"] = str(tmp_path_factory.mktemp("exec_data"))
    os.environ["EDIP_LLM_PROVIDER"] = "mock"
    from app.core import config, container
    config.get_settings.cache_clear()
    container.get_container.cache_clear()
    from app.main import create_app
    with TestClient(create_app()) as c:  # lifespan → brain + workspace boot
        yield c
    config.get_settings.cache_clear()
    container.get_container.cache_clear()


def test_manager_surface(client):
    dash = client.get("/api/v1/manager/dashboard")
    assert dash.status_code == 200
    body = dash.json()
    assert {"business_health", "operational_status", "portfolio_summary",
            "recommended_actions", "automation_status"} <= set(body)
    assert body["operational_status"]["continuous_learning"] == "active"

    ws = client.get("/api/v1/manager/workspace").json()
    for section in ("todays_summary", "pending_reviews", "critical_risks",
                    "growth_opportunities", "portfolio_health",
                    "pending_tasks", "pending_approvals", "recent_reports",
                    "recent_decisions", "upcoming_meetings",
                    "suggested_actions", "recent_notifications"):
        assert section in ws, section

    brief = client.get("/api/v1/manager/daily-brief").json()
    assert brief["date"] and "recommendations" in brief

    task = client.post("/api/v1/manager/tasks",
                       json={"title": "Prepare QBR deck"}).json()
    done = client.patch(f"/api/v1/manager/tasks/{task['task_id']}",
                        json={"status": "completed"})
    assert done.json()["status"] == "completed"

    dec = client.post("/api/v1/manager/decisions",
                      json={"decision": "Adopt weekly portfolio review",
                            "owner": "CEO"}).json()
    upd = client.patch(f"/api/v1/manager/decisions/{dec['decision_id']}",
                       json={"status": "approved"})
    assert upd.json()["status"] == "approved"

    assert client.get("/api/v1/manager/notifications").status_code == 200
    assert client.get("/api/v1/manager/reports").status_code == 200
    assert client.get("/api/v1/manager/portfolio").status_code == 200
    slots = client.get("/api/v1/manager/integrations").json()
    # One slot per provider kind (V2.2 added rest + webhook); all unconfigured
    # in a test deployment, so nothing can leave the platform.
    assert len(slots) == len(PROVIDER_KINDS)
    assert all(not s["available"] for s in slots)

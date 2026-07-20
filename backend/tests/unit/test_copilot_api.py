"""The /copilot surface through the real app: an executive asks a
natural-language business question and the copilot orchestrates the Brain,
Product Intelligence, Knowledge, Reports, Portfolio and Recommendations to
answer it from evidence.

Also asserts the layer changed nothing: the per-project copilot still answers,
and the copilot registers on the existing scheduler and event bus rather than
building its own.
"""
from __future__ import annotations

import os

import pytest
from fastapi.testclient import TestClient

PID = "proj_pay"


def _kpi(name, value, growth, unit=""):
    return {"id": f"kpi_{name.lower().replace(' ', '_')}", "name": name,
            "current_value": value, "growth_pct": growth,
            "trend": "up" if growth > 0 else "down", "unit": unit}


@pytest.fixture(scope="module")
def client(tmp_path_factory):
    os.environ["EDIP_DATA_DIR"] = str(tmp_path_factory.mktemp("copilot_data"))
    os.environ["EDIP_LLM_PROVIDER"] = "mock"
    from app.core import config, container
    config.get_settings.cache_clear()
    container.get_container.cache_clear()
    from app.core.container import get_container

    c = get_container()
    c.store.save(PID, "state", {"project_id": PID, "name": "Payments",
                                "status": "ready", "report_version": 1})
    c.store.save(PID, "kpis", [
        _kpi("Transaction Revenue", 120000.0, 12.0, "$"),
        _kpi("Active Customers", 5200.0, 15.0),
        _kpi("Failed Transactions", 800.0, 22.0),
    ])
    c.store.save(PID, "signals", [
        {"id": "sig_1", "kind": "trend", "kpi_name": "Transaction Revenue",
         "strength": 0.8, "stats": {"slope": 1.2}}])
    c.store.save(PID, "forecasts", [
        {"kpi_id": "kpi_transaction_revenue",
         "kpi_name": "Transaction Revenue", "values": [125000.0, 131000.0],
         "method": "holt_linear", "confidence": 0.82, "status": "ok",
         "validation": [], "horizon": "next_quarter"}])
    c.store.save(PID, "quality", {"overall_score": 88.0})
    c.knowledge.record_report(PID, "Payments — report v1", 74.0)
    c.knowledge.add_rule("Never offer discounts above 20%", scope="global")
    c.product.catalog.upsert("Payments", owner="Dana K", project_id=PID)
    c.product.build_catalog()
    c.product.health.evaluate_all()

    from app.main import create_app
    with TestClient(create_app()) as test_client:
        yield test_client
    config.get_settings.cache_clear()
    container.get_container.cache_clear()


# ------------------------------------------------------------------ chat
def test_an_executive_can_ask_a_business_question(client):
    answer = client.post("/api/v1/copilot/chat", json={
        "message": "How is the product portfolio performing?"}).json()

    assert answer["status"] in ("ok", "unavailable", "failed")
    assert answer["conversation_id"]
    assert answer["intent"]["intent"]
    assert answer["plan"]["modules"], "no modules were orchestrated"


def test_the_copilot_orchestrates_the_existing_modules(client):
    answer = client.post("/api/v1/copilot/chat", json={
        "message": "Analyse the Payments product"}).json()

    assert answer["intent"]["intent"] == "analysis"
    # The plan reaches the Brain, analytics, and product intelligence — the
    # modules that already hold the answer.
    assert {"brain", "analytics", "product"} <= set(answer["plan"]["modules"])
    assert answer["evidence"]["total"] > 0, "the copilot asked without facts"


def test_evidence_is_gathered_and_exposed(client):
    answer = client.post("/api/v1/copilot/chat", json={
        "message": "How is Transaction Revenue doing?"}).json()

    assert answer["evidence"]["items"], "no evidence surfaced"
    assert all(i["id"] for i in answer["evidence"]["items"])
    kinds = {i["kind"] for i in answer["evidence"]["items"]}
    assert "kpi" in kinds


def test_every_answer_carries_its_validation_verdict(client):
    answer = client.post("/api/v1/copilot/chat", json={
        "message": "What should we do about Payments?"}).json()

    assert answer["validation"]["verdict"] in ("verified", "downgraded",
                                               "rejected")
    assert "confidence" in answer["validation"]


def test_a_scenario_question_is_answered_deterministically(client):
    answer = client.post("/api/v1/copilot/chat", json={
        "message": "What if customer growth increases 15%?"}).json()

    assert answer["intent"]["intent"] == "scenario"
    assert answer["plan"]["needs_llm"] is False
    assert any("deterministic" in n.lower() for n in answer["plan"]["notes"])


def test_an_approval_question_never_approves_anything(client):
    answer = client.post("/api/v1/copilot/chat", json={
        "message": "What needs my approval?"}).json()

    assert answer["intent"]["intent"] == "approval"
    assert answer["provider"]["provider"] == "deterministic"
    assert any("never approves" in n for n in answer["plan"]["notes"])


def test_an_empty_message_is_rejected(client):
    assert client.post("/api/v1/copilot/chat",
                       json={"message": ""}).status_code == 422


def test_suggested_actions_accompany_the_answer(client):
    answer = client.post("/api/v1/copilot/chat", json={
        "message": "What should we do about Payments?"}).json()

    for section in ("recommended_actions", "next_steps", "risks",
                    "approvals_required", "related_reports",
                    "related_products"):
        assert section in answer, section


def test_context_gaps_are_reported(client):
    answer = client.post("/api/v1/copilot/chat", json={
        "message": "How is the portfolio?"}).json()

    assert "context_gaps" in answer


# --------------------------------------------------------------- context
def test_the_context_surface_shows_what_the_copilot_knows(client):
    context = client.get(
        "/api/v1/copilot/context?q=how+is+revenue").json()

    assert context["intent"]["intent"]
    assert context["plan"]["modules"]
    assert context["evidence"]["total"] >= 0
    assert "provider" in context


def test_the_intents_and_routes_are_discoverable(client):
    body = client.get("/api/v1/copilot/intents").json()
    intents = {i["intent"] for i in body["intents"]}

    assert {"question", "analysis", "recommendation", "report", "comparison",
            "forecast", "explanation", "scenario", "approval", "task",
            "workflow", "search", "decision", "meeting_prep",
            "executive_brief"} == intents
    assert body["routes"]


def test_suggested_questions_come_from_real_state(client):
    suggestions = client.get("/api/v1/copilot/suggestions").json()["suggestions"]

    assert suggestions
    assert all(s["question"] and s["intent"] for s in suggestions)


# --------------------------------------------------------- conversations
def test_a_conversation_persists_across_turns(client):
    first = client.post("/api/v1/copilot/chat", json={
        "message": "How is Payments?"}).json()
    client.post("/api/v1/copilot/chat", json={
        "message": "And what about the risks?",
        "conversation_id": first["conversation_id"]})

    history = client.get(
        f"/api/v1/copilot/history?conversation_id={first['conversation_id']}"
    ).json()
    assert len(history["messages"]) >= 4


def test_conversations_can_be_listed_pinned_and_renamed(client):
    conversation = client.post("/api/v1/copilot/conversations").json()
    cid = conversation["conversation_id"]

    pinned = client.patch(f"/api/v1/copilot/conversations/{cid}",
                          json={"pinned": True, "title": "Board prep"}).json()
    assert pinned["pinned"] is True
    assert pinned["title"] == "Board prep"

    listed = client.get("/api/v1/copilot/conversations?pinned=true").json()
    assert any(c["conversation_id"] == cid for c in listed["conversations"])


def test_a_conversation_can_be_deleted(client):
    conversation = client.post("/api/v1/copilot/conversations").json()
    cid = conversation["conversation_id"]

    assert client.delete(f"/api/v1/copilot/conversations/{cid}").status_code == 204
    assert client.get(f"/api/v1/copilot/conversations/{cid}").status_code == 404


def test_an_unknown_conversation_is_a_404(client):
    assert client.get(
        "/api/v1/copilot/conversations/cnv_nope").status_code == 404


# ---------------------------------------------------------------- search
def test_conversations_are_searchable(client):
    client.post("/api/v1/copilot/chat", json={
        "message": "Tell me about merchant onboarding costs"})
    results = client.get("/api/v1/copilot/search?q=merchant+onboarding"
                         ).json()["results"]

    assert results
    assert results[0]["matches"]


def test_an_empty_search_is_rejected(client):
    assert client.get("/api/v1/copilot/search?q=").status_code == 422


# ----------------------------------------------------------- preferences
def test_preferences_are_counted_from_real_usage(client):
    for _ in range(2):
        client.post("/api/v1/copilot/chat",
                    json={"message": "How is Payments doing?"})
    preferences = client.get("/api/v1/copilot/preferences").json()

    assert preferences["conversations"] > 0
    assert preferences["frequent_intents"]


def test_a_clarification_reaches_the_knowledge_store(client):
    client.post("/api/v1/copilot/clarifications", json={
        "question": "What counts as an active customer?",
        "answer": "One transaction in the last 30 days"})
    knowledge = client.get("/api/v1/knowledge").json()

    assert any("active customer" in c["question"].lower()
               for c in knowledge["clarifications"])


# ------------------------------------------------------------- workspace
def test_the_workspace_composes_the_conversational_surface(client):
    workspace = client.get("/api/v1/copilot").json()

    for section in ("conversations", "pinned", "suggested_questions",
                    "recent_reports", "intents", "provider", "stats"):
        assert section in workspace, section


# --------------------------------------------------- nothing else changed
def test_the_per_project_copilot_still_answers(client):
    """The existing project-scoped copilot is untouched."""
    response = client.post(f"/api/v1/projects/{PID}/copilot/chat",
                           json={"question": "How is revenue?"})

    assert response.status_code == 200
    assert "answer" in response.json()


def test_the_copilot_runs_on_the_existing_heartbeat(client):
    jobs = {j["name"]: j for j in client.get("/api/v1/runtime/jobs").json()}

    assert jobs["copilot_subjects"]["runs"] >= 1, \
        "the copilot did not learn its subjects at startup"
    assert jobs["copilot_subjects_refresh"]["event"] == "ProductRegistered"
    assert jobs["copilot_maintenance"]["kind"] == "cron"


def test_the_runtime_reports_copilot_status(client):
    status = client.get("/api/v1/runtime").json()["copilot"]

    assert "conversations" in status
    assert "provider" in status


def test_the_copilot_announces_on_the_existing_bus(client):
    client.post("/api/v1/copilot/chat", json={"message": "How is revenue?"})
    kinds = {e["kind"] for e in
             client.get("/api/v1/runtime/events?limit=200").json()["events"]}

    assert "CopilotAnswered" in kinds


def test_the_copilot_learned_the_real_product_names(client):
    """Subjects are learned from the catalogue, never hardcoded."""
    answer = client.post("/api/v1/copilot/chat", json={
        "message": "How is Payments performing?"}).json()

    assert answer["intent"]["subject"] == "payments"

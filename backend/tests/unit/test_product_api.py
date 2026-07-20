"""The /product surface through the real app: the Enterprise Product Manager
boots with the platform, discovers its products, scores them, and proposes
strategy — without anyone asking.

Also asserts the layer sits *above* the Brain: it registers on the existing
scheduler, announces on the existing bus, and routes strategy through the
existing Decision Engine rather than creating parallel machinery.
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
    os.environ["EDIP_DATA_DIR"] = str(tmp_path_factory.mktemp("product_data"))
    os.environ["EDIP_LLM_PROVIDER"] = "mock"
    from app.core import config, container
    config.get_settings.cache_clear()
    container.get_container.cache_clear()
    from app.core.container import get_container

    # Seed a project the way the intelligence modules actually leave one.
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
    c.store.save(PID, "quality", {"overall_score": 88.0, "issues": [],
                                  "per_dataset": {}})
    c.knowledge.record_report(PID, "Payments — report v1", 74.0)

    from app.main import create_app
    with TestClient(create_app()) as test_client:
        yield test_client
    config.get_settings.cache_clear()
    container.get_container.cache_clear()


@pytest.fixture(scope="module")
def payments(client):
    return client.post("/api/v1/product/catalog", json={
        "name": "Payments", "owner": "Dana K", "business_unit": "Fintech",
        "project_id": PID}).json()


# --------------------------------------------------------------- catalog
def test_the_catalog_answers_and_carries_stats(client):
    body = client.get("/api/v1/product/catalog").json()

    assert "products" in body and "stats" in body


def test_a_product_can_be_registered(client, payments):
    assert payments["product_id"] == "product:payments"
    assert payments["owner"] == "Dana K"
    assert payments["business_unit"] == "Fintech"


def test_the_catalog_sync_attaches_kpis_and_reports(client, payments):
    client.post("/api/v1/product/catalog/sync")
    product = client.get(
        "/api/v1/product/catalog/product:payments").json()["product"]

    assert product["kpis"], "no KPIs attached from the platform"
    assert product["reports"], "no reports attached"


def test_an_invalid_lifecycle_is_rejected(client, payments):
    response = client.patch("/api/v1/product/catalog/product:payments",
                            json={"lifecycle": "vibes"})
    assert response.status_code == 422


def test_an_unknown_product_is_a_404(client):
    assert client.get(
        "/api/v1/product/catalog/product:nope").status_code == 404


# ---------------------------------------------------------------- health
def test_health_scores_the_product_with_evidence(client, payments):
    client.post("/api/v1/product/catalog/sync")
    record = client.post(
        "/api/v1/product/health/evaluate?product_id=product:payments").json()

    assert record["health_score"] is not None
    assert record["band"] in ("healthy", "watch", "at_risk")
    assert record["evidence_ids"], "a score with no evidence"
    assert record["reasons"]["growth"]


def test_the_health_endpoint_separates_scored_from_unscored(client, payments):
    body = client.get("/api/v1/product/health").json()

    assert body["scored"] >= 1
    assert isinstance(body["unscored"], list)


# ---------------------------------------------------------------- growth
def test_growth_findings_cite_their_evidence(client, payments):
    body = client.get("/api/v1/product/growth").json()

    assert body["findings"], "no growth findings from growing KPIs"
    assert all(f["evidence_ids"] for f in body["findings"] if f["product_id"])


# -------------------------------------------------------- recommendations
def test_recommendations_carry_the_full_business_case(client, payments):
    body = client.post(
        "/api/v1/product/recommendations?route=false").json()

    assert body["generated"] > 0
    for recommendation in body["recommendations"]:
        assert recommendation["business_impact"]
        assert recommendation["evidence_ids"]
        assert recommendation["estimated_effort"] in ("small", "medium",
                                                      "large")
        assert 1 <= recommendation["priority"] <= 5


def test_recommendations_route_through_the_existing_decision_engine(client,
                                                                    payments):
    """Strategy proposes; the runtime's Decision Engine decides. The proof is
    that routed recommendations appear as decisions on /runtime."""
    client.post("/api/v1/product/recommendations?route=true")
    decisions = client.get("/api/v1/runtime/decisions").json()["decisions"]

    assert any(d["source"] == "product_strategy" for d in decisions), \
        "product strategy did not reach the existing decision pipeline"
    routed = next(d for d in decisions if d["source"] == "product_strategy")
    assert routed["evidence_ids"] or routed["confidence"]
    assert [s["stage"] for s in routed["trace"]][:4] == [
        "recommendation", "evidence", "confidence", "priority"]


# --------------------------------------------------------------- reviews
def test_a_review_generates_with_every_section(client, payments):
    review = client.post(
        "/api/v1/product/reviews?product_id=product:payments").json()

    for section in ("executive_summary", "strengths", "weaknesses", "risks",
                    "recent_changes", "recommendations", "evidence",
                    "confidence", "action_items"):
        assert section in review, section


def test_a_review_can_register_with_the_existing_review_center(client,
                                                               payments):
    client.post("/api/v1/product/reviews?product_id=product:payments"
                "&register=true")
    reviews = client.get("/api/v1/manager/reports").json()["reviews"]

    assert any("product review" in r["title"] for r in reviews), \
        "the product review did not reach the executive's review center"


# ------------------------------------------------------------------ KPIs
def test_kpis_are_categorized_and_alerting(client, payments):
    client.post("/api/v1/product/kpis/monitor")
    body = client.get("/api/v1/product/kpis").json()

    assert body["counts"]["business"] >= 1
    assert body["counts"]["operational"] >= 1
    assert body["thresholds"]["defaults"]


def test_a_rising_failure_kpi_raises_an_alert(client, payments):
    alerts = client.get("/api/v1/product/kpis/alerts").json()["alerts"]

    assert any(a["kpi"] == "Failed Transactions" for a in alerts), \
        "a 22% rise in failures raised no alert"


def test_a_threshold_can_be_set_over_the_api(client):
    rule = client.post("/api/v1/product/kpis/thresholds", json={
        "kpi": "Transaction Revenue", "warning": -1.0,
        "critical": -2.0}).json()

    assert rule["warning"] == -1.0


def test_an_invalid_threshold_direction_is_rejected(client):
    response = client.post("/api/v1/product/kpis/thresholds", json={
        "kpi": "X", "warning": 1, "critical": 2, "direction": "sideways"})
    assert response.status_code == 422


# ------------------------------------------------------------- scenarios
def test_a_scenario_projects_from_real_forecasts(client, payments):
    scenario = client.post("/api/v1/product/scenarios", json={
        "lever": "customer_growth", "change_pct": 15.0}).json()

    assert scenario["projections"], "nothing projected"
    assert scenario["assumptions"], "a projection with no stated assumptions"
    revenue = next(p for p in scenario["projections"]
                   if p["kpi"] == "Transaction Revenue")
    assert revenue["change_pct"] == pytest.approx(12.0)
    assert revenue["confidence"] == pytest.approx(0.82), \
        "confidence was not inherited from the underlying forecast"


def test_an_unknown_lever_is_rejected(client):
    response = client.post("/api/v1/product/scenarios",
                           json={"lever": "vibes", "change_pct": 10})
    assert response.status_code == 422


def test_the_levers_are_discoverable(client):
    levers = {l["lever"] for l in
              client.get("/api/v1/product/scenarios").json()["levers"]}
    assert "customer_growth" in levers


# ------------------------------------------------------------- portfolio
def test_the_portfolio_ranks_products_and_states_why(client, payments):
    portfolio = client.get("/api/v1/product/portfolio").json()

    assert portfolio["product_ranking"]
    top = portfolio["product_ranking"][0]
    assert top["rank"] == 1
    assert top["investment_priority"] in ("invest", "fix", "maintain",
                                          "watch", "question")
    assert top["priority_reason"], "an investment call with no reason"
    assert portfolio["coverage"]["products"] >= 1


# ---------------------------------------------------------------- briefs
@pytest.mark.parametrize("kind", ["board_brief", "monthly_review",
                                  "quarterly_strategy", "risk_summary",
                                  "growth_summary", "decision_pack"])
def test_every_brief_generates(client, payments, kind):
    brief = client.post(f"/api/v1/product/briefs/{kind}").json()

    assert brief["headline"]
    assert brief["markdown"].startswith("#")


def test_an_unknown_brief_is_rejected(client):
    assert client.post(
        "/api/v1/product/briefs/vibes_report").status_code == 422


# -------------------------------------------------------------- strategy
def test_the_strategy_endpoint_composes_the_picture(client, payments):
    strategy = client.get("/api/v1/product/strategy").json()

    assert "portfolio" in strategy
    assert "recommendations" in strategy
    assert strategy["brief_kinds"]


def test_the_product_overview_is_business_framed(client, payments):
    overview = client.get("/api/v1/product").json()

    assert overview["products"]["total"] >= 1
    assert "portfolio_health" in overview
    assert "top_opportunities" in overview


# ------------------------------------------------------ executive surface
def test_the_workspace_shows_products_without_technical_detail(client,
                                                               payments):
    products = client.get("/api/v1/manager/workspace").json()["products"]

    assert products["status"] == "active"
    assert products["products"]["total"] >= 1
    # Business framing only: no evidence ids, no internals.
    assert "evidence_ids" not in str(products.get("portfolio_health", {}))


def test_the_dashboard_shows_the_product_strip(client, payments):
    summary = client.get("/api/v1/manager/dashboard").json()["product_summary"]

    assert summary["status"] == "active"
    assert summary["products"] >= 1
    assert summary["portfolio_band"] in ("healthy", "watch", "at_risk",
                                         "unknown")


def test_executive_reviews_reach_the_workspace(client, payments):
    client.post("/api/v1/product/reviews?product_id=product:payments")
    reviews = client.get("/api/v1/manager/product-reviews").json()["reviews"]

    assert reviews
    assert reviews[0]["summary"]


# -------------------------------------------------------- runtime wiring
def test_product_jobs_run_on_the_existing_heartbeat(client):
    jobs = {j["name"]: j for j in client.get("/api/v1/runtime/jobs").json()}

    assert jobs["startup_products"]["runs"] >= 1, \
        "the catalogue was not built at startup"
    assert jobs["product_health"]["kind"] == "interval"
    assert jobs["kpi_monitor"]["kind"] == "interval"
    assert jobs["board_brief"]["kind"] == "cron"


def test_recalculation_is_triggered_by_the_sds_events(client):
    jobs = {j["name"]: j for j in client.get("/api/v1/runtime/jobs").json()}

    assert jobs["refresh_on_knowledge"]["event"] == "KnowledgeUpdated"
    assert jobs["refresh_on_report"]["event"] == "ReportGenerated"
    assert jobs["refresh_on_portfolio"]["event"] == "PortfolioChanged"


def test_the_runtime_reports_product_intelligence_status(client, payments):
    status = client.get("/api/v1/runtime").json()["product_intelligence"]

    assert status["catalog"]["total"] >= 1
    assert "recommendations" in status


def test_the_product_layer_announces_on_the_existing_bus(client, payments):
    client.post("/api/v1/product/health/evaluate?product_id=product:payments")
    kinds = {e["kind"] for e in
             client.get("/api/v1/runtime/events?limit=200").json()["events"]}

    assert "ProductHealthEvaluated" in kinds

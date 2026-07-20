"""Product Intelligence & Strategic Decision Layer — catalogue, health,
growth, strategy, reviews, KPI intelligence, scenarios, portfolio, briefs.

Every engine is driven against real artifacts written to a real ArtifactStore
in the shapes the intelligence modules actually emit. "Evidence-based" is the
central claim of this layer, and a mocked evidence source cannot falsify it:
these tests assert that a judgement with no evidence is *not made*, and that
one that is made cites what it stands on.
"""
from __future__ import annotations

import pytest

from app.knowledge.store import KnowledgeStore
from app.product.briefs import ExecutiveBriefGenerator
from app.product.catalog import ProductCatalog
from app.product.evidence import EvidenceGatherer
from app.product.growth import GrowthIntelligenceEngine
from app.product.health import ProductHealthEngine
from app.product.kpis import KPIIntelligence, classify
from app.product.portfolio import PortfolioIntelligence
from app.product.reviews import ProductReviewEngine
from app.product.scenarios import ScenarioSimulation
from app.product.store import ProductStore
from app.product.strategy import StrategicRecommendationEngine
from app.repositories.artifact_store import ArtifactStore

PID = "proj_pay"


def _kpi(name, value, growth, kpi_id=None, trend=None, unit=""):
    return {"id": kpi_id or f"kpi_{name.lower().replace(' ', '_')}",
            "name": name, "current_value": value, "growth_pct": growth,
            "trend": trend or ("up" if (growth or 0) > 0 else "down"),
            "unit": unit}


@pytest.fixture()
def artifacts(tmp_path):
    store = ArtifactStore(tmp_path / "projects")
    store.save(PID, "state", {"project_id": PID, "name": "Payments",
                              "status": "ready", "report_version": 1})
    store.save(PID, "kpis", [
        _kpi("Transaction Revenue", 120000.0, 12.0, unit="$"),
        _kpi("Transaction Volume", 40000.0, 8.0),
        _kpi("Active Customers", 5200.0, 15.0),
        _kpi("Failed Transactions", 800.0, 22.0),
        _kpi("Merchant Retention", 91.0, 2.0, unit="%"),
    ])
    store.save(PID, "signals", [
        {"id": "sig_1", "kind": "trend", "kpi_name": "Transaction Revenue",
         "strength": 0.8, "stats": {"slope": 1.2}},
        {"id": "sig_2", "kind": "anomaly", "kpi_name": "Failed Transactions",
         "strength": 0.75, "stats": {"z": 3.4}},
    ])
    store.save(PID, "forecasts", [
        {"kpi_id": "kpi_transaction_revenue", "kpi_name": "Transaction Revenue",
         "horizon": "next_quarter", "periods": ["Q1", "Q2"],
         "values": [125000.0, 131000.0], "lower": [120000.0, 124000.0],
         "upper": [130000.0, 138000.0], "method": "holt_linear",
         "confidence": 0.82, "status": "ok", "validation": []},
    ])
    store.save(PID, "quality", {"overall_score": 88.0, "issues": [],
                                "per_dataset": {}})
    return store


@pytest.fixture()
def knowledge(tmp_path):
    store = KnowledgeStore(tmp_path / "knowledge")
    store.record_report(PID, "Payments — report v1", 74.0)
    return store


@pytest.fixture()
def product_store(tmp_path):
    return ProductStore(tmp_path / "product")


@pytest.fixture()
def gatherer(artifacts, knowledge):
    return EvidenceGatherer(artifacts, knowledge)


@pytest.fixture()
def catalog(product_store, knowledge, artifacts):
    return ProductCatalog(product_store, knowledge=knowledge,
                          artifacts=artifacts)


@pytest.fixture()
def payments(catalog):
    product, _ = catalog.upsert("Payments", owner="Dana K",
                                business_unit="Fintech", project_id=PID)
    return product


@pytest.fixture()
def health(product_store, catalog, gatherer):
    return ProductHealthEngine(product_store, catalog, gatherer)


@pytest.fixture()
def growth(catalog, health, gatherer):
    return GrowthIntelligenceEngine(catalog, health, gatherer)


@pytest.fixture()
def strategy(product_store, catalog, health, growth, gatherer):
    return StrategicRecommendationEngine(product_store, catalog, health,
                                         growth, gatherer)


# ---------------------------------------------------------------- catalog
def test_a_product_carries_its_identity_and_history(catalog):
    product, created = catalog.upsert("Payments", owner="Dana K",
                                      business_unit="Fintech")

    assert created is True
    assert product["product_id"] == "product:payments"
    assert product["owner"] == "Dana K"
    assert product["lifecycle"] == "growth"  # sensible default
    assert product["history"][0]["change"] == "registered"


def test_registering_a_known_product_enriches_it(catalog):
    catalog.upsert("Payments")
    product, changed = catalog.upsert("Payments", owner="Dana K")

    assert changed is True
    assert len(catalog.products()) == 1, "the product was duplicated"
    assert product["owner"] == "Dana K"
    assert any(h["change"] == "owner_changed" for h in product["history"])


def test_an_empty_field_never_overwrites_a_known_one(catalog):
    catalog.upsert("Payments", owner="Dana K")
    product, changed = catalog.upsert("Payments", owner="")

    assert product["owner"] == "Dana K", "an empty owner erased a known one"
    assert changed is False


def test_lifecycle_and_status_are_validated(catalog):
    with pytest.raises(ValueError, match="Unknown lifecycle"):
        catalog.upsert("X", lifecycle="vibes")
    with pytest.raises(ValueError, match="Unknown product status"):
        catalog.upsert("X", status="maybe")


def test_kpis_and_reports_attach_from_the_platform(catalog, payments):
    catalog.sync_kpis_and_reports()
    product = catalog.get(payments["product_id"])

    names = {k["name"] for k in product["kpis"]}
    assert "Transaction Revenue" in names
    assert product["reports"], "no report attached"
    assert product["reports"][0]["health_score"] == 74.0


def test_products_are_discovered_from_the_organizational_model(product_store,
                                                               knowledge,
                                                               artifacts):
    class _Org:
        def entities(self, kind="", limit=0):
            return [{"name": "Checkout", "entity_id": "product:checkout",
                     "owner": "Ravi P", "sources": ["crm"], "projects": [],
                     "attributes": {}}]

    class _Rel:
        def neighbourhood(self, entity_id):
            return {"related": [
                {"name": "North Coffee", "kind": "merchant",
                 "relationship": "association", "direction": "outgoing"},
                {"name": "Acme Ltd", "kind": "customer",
                 "relationship": "association", "direction": "outgoing"}]}

    catalog = ProductCatalog(product_store, organization=_Org(),
                             relationships=_Rel(), knowledge=knowledge,
                             artifacts=artifacts)
    outcome = catalog.sync_from_organization()
    product = catalog.resolve("Checkout")

    assert outcome["discovered"] == 1
    assert outcome["linked"] == 1
    assert product["owner"] == "Ravi P"
    assert product["merchants"] == ["North Coffee"], \
        "relationships were not resolved from the organizational model"
    assert product["customers"] == ["Acme Ltd"]


# ----------------------------------------------------------------- health
def test_health_scores_every_dimension_it_has_evidence_for(health, payments):
    record = health.evaluate(payments["product_id"])

    assert record["health_score"] is not None
    assert record["scores"]["growth"] > 50, "growing KPIs did not raise growth"
    assert record["scores"]["revenue"] is not None
    assert record["evidence_ids"], "a score with no evidence"
    assert record["confidence"] > 0


def test_an_unmeasurable_dimension_is_unknown_not_zero(health, catalog):
    """A product with no evidence must not score 0 — "unknown" and "bad" are
    different answers, and conflating them defunds products that were merely
    uninstrumented."""
    product, _ = catalog.upsert("Ghost Product")
    record = health.evaluate(product["product_id"])

    assert record["health_score"] is None
    assert record["band"] == "unknown"
    assert all(v is None for v in record["scores"].values())
    assert "no" in record["reasons"]["growth"].lower()


def test_every_score_carries_a_reason(health, payments):
    record = health.evaluate(payments["product_id"])

    for dimension, score in record["scores"].items():
        assert record["reasons"][dimension], f"{dimension} scored with no reason"


def test_anomalies_and_rising_failures_lower_the_risk_score(health, payments):
    record = health.evaluate(payments["product_id"])

    assert record["scores"]["risk"] < 100
    assert "anomaly" in record["reasons"]["risk"] \
        or "failure" in record["reasons"]["risk"]


def test_confidence_reflects_how_much_was_measurable(health, catalog,
                                                     payments):
    measured = health.evaluate(payments["product_id"])
    product, _ = catalog.upsert("Sparse Product")
    sparse = health.evaluate(product["product_id"])

    assert measured["confidence"] > sparse["confidence"]


def test_health_records_its_change_between_evaluations(health, payments,
                                                       artifacts):
    health.evaluate(payments["product_id"])
    artifacts.save(PID, "kpis", [_kpi("Transaction Revenue", 90000.0, -25.0)])
    record = health.evaluate(payments["product_id"])

    assert record["previous_health_score"] is not None
    assert record["change"] is not None
    assert record["change"] < 0, "a collapse in revenue did not lower health"


# ----------------------------------------------------------------- growth
def test_strong_kpi_growth_becomes_an_opportunity(growth, payments, health):
    health.evaluate(payments["product_id"])
    findings = growth.analyse()["findings"]
    opportunities = [f for f in findings if f["kind"] == "growth_opportunity"]

    assert opportunities
    assert all(f["evidence_ids"] for f in opportunities), \
        "an opportunity with no evidence"


def test_declining_kpis_become_a_decline_finding(growth, health, payments,
                                                 artifacts):
    artifacts.save(PID, "kpis", [_kpi("Transaction Revenue", 80000.0, -18.0)])
    health.evaluate(payments["product_id"])
    findings = growth.findings(kind="declining_product")

    assert findings
    assert "declining" in findings[0]["finding"].lower()


def test_cannibalization_reads_the_inverse_correlation_signal(growth, health,
                                                              payments,
                                                              artifacts):
    """The Analytics module already labels inverse correlation the
    cannibalization candidate — this layer must read that, not re-derive it."""
    artifacts.save(PID, "signals", [
        {"id": "sig_inv", "kind": "inverse_correlation",
         "kpi_name": "Transaction Revenue", "strength": 0.82,
         "stats": {"r": -0.78, "kpi_b_name": "Checkout Revenue"}}])
    health.evaluate(payments["product_id"])
    findings = growth.findings(kind="cannibalization")

    assert findings, "the inverse-correlation signal was ignored"
    assert "Checkout Revenue" in findings[0]["finding"]
    assert findings[0]["evidence_ids"] == ["signal:sig_inv"]


def test_a_strong_trend_becomes_an_emerging_trend(growth, health, payments):
    health.evaluate(payments["product_id"])
    findings = growth.findings(kind="emerging_trend")

    assert findings
    assert findings[0]["evidence_ids"] == ["signal:sig_1"]


def test_concentration_becomes_a_portfolio_gap(growth, health, payments,
                                               artifacts):
    artifacts.save(PID, "signals", [
        {"id": "sig_con", "kind": "concentration",
         "kpi_name": "Transaction Revenue", "strength": 0.9,
         "stats": {"dimension": "merchants", "top_share": 0.82}}])
    health.evaluate(payments["product_id"])
    findings = growth.findings(kind="portfolio_gap")

    assert any(f["evidence_ids"] == ["signal:sig_con"] for f in findings)


def test_a_rising_failure_rate_is_never_a_growth_opportunity(growth, health,
                                                             payments):
    """Failed Transactions rises 22% in the fixture. Telling a manager to
    "scale what is working" about failures is worse than saying nothing."""
    health.evaluate(payments["product_id"])
    opportunities = growth.findings(kind="growth_opportunity")

    assert not any("Failed" in f["finding"] for f in opportunities), \
        "a rising failure KPI was reported as a growth opportunity"


def test_a_falling_failure_rate_is_never_a_decline(growth, health, payments,
                                                   artifacts):
    """Failures falling is good news — direction belongs to what the KPI
    measures, not to the arithmetic."""
    artifacts.save(PID, "kpis", [_kpi("Failed Transactions", 200.0, -40.0)])
    health.evaluate(payments["product_id"])
    declines = growth.findings(kind="declining_product")

    assert not any("Failed" in f["finding"] for f in declines), \
        "a falling failure KPI was reported as a decline"


def test_a_product_with_no_evidence_produces_no_findings(growth, catalog):
    catalog.upsert("Ghost Product")
    findings = growth.findings(product_id="product:ghost_product")

    assert findings == [], "the growth engine invented a finding"


def test_weak_signals_are_ignored(growth, health, payments, artifacts):
    artifacts.save(PID, "signals", [
        {"id": "sig_weak", "kind": "inverse_correlation",
         "kpi_name": "X", "strength": 0.2, "stats": {"r": -0.2}}])
    health.evaluate(payments["product_id"])

    assert growth.findings(kind="cannibalization") == []


# --------------------------------------------------------------- strategy
def test_recommendations_carry_everything_a_manager_needs(strategy, health,
                                                          payments):
    health.evaluate(payments["product_id"])
    outcome = strategy.generate(route=False)

    assert outcome["generated"] > 0
    for recommendation in outcome["recommendations"]:
        assert recommendation["business_impact"]
        assert recommendation["evidence_ids"], "a recommendation with no evidence"
        assert 1 <= recommendation["priority"] <= 5
        assert recommendation["estimated_effort"] in ("small", "medium",
                                                      "large")
        assert 0 <= recommendation["confidence"] <= 1
        assert isinstance(recommendation["dependencies"], list)


def test_a_recommendation_cannot_be_made_without_evidence():
    from app.product.strategy import _recommendation
    with pytest.raises(ValueError, match="cites no evidence"):
        _recommendation("improve_onboarding", "X", "Do a thing",
                        business_impact="impact", confidence=0.9,
                        evidence_ids=[], priority=1, effort="small",
                        dependencies=[])


def test_a_declining_product_is_recommended_for_investigation(strategy, health,
                                                              payments,
                                                              artifacts):
    artifacts.save(PID, "kpis", [_kpi("Transaction Revenue", 80000.0, -20.0)])
    health.evaluate(payments["product_id"])
    strategy.generate(route=False)
    plays = {r["play"] for r in strategy.recommendations()}

    assert "investigate_decline" in plays


def test_regenerating_refreshes_rather_than_duplicating(strategy, health,
                                                        payments):
    health.evaluate(payments["product_id"])
    strategy.generate(route=False)
    first = len(strategy.recommendations())
    strategy.generate(route=False)

    assert len(strategy.recommendations()) == first, \
        "regenerating duplicated recommendations"
    assert any(r["observations"] > 1 for r in strategy.recommendations())


def test_recommendations_route_through_the_existing_decision_engine(
        strategy, health, payments):
    """The strategy engine proposes; the runtime's Decision Engine decides.
    No second approval path may exist."""
    decided = []

    class _Decisions:
        def decide(self, recommendation, source=""):
            decided.append(recommendation)
            return {"decision_id": "dec_1", "status": "queued"}

    strategy.attach_decisions(_Decisions())
    health.evaluate(payments["product_id"])
    outcome = strategy.generate(route=True)

    assert outcome["routed_to_decisions"] > 0
    assert decided[0]["evidence_ids"], "routed without evidence"
    assert decided[0]["expected_impact"]
    assert all(r["decision_id"] for r in strategy.recommendations())


# ---------------------------------------------------------------- reviews
@pytest.fixture()
def reviews(product_store, catalog, health, growth, strategy):
    return ProductReviewEngine(product_store, catalog, health, growth,
                               strategy)


def test_a_review_has_every_required_section(reviews, health, payments,
                                             strategy):
    health.evaluate(payments["product_id"])
    strategy.generate(route=False)
    review = reviews.review(payments["product_id"])

    for section in ("executive_summary", "strengths", "weaknesses", "risks",
                    "recent_changes", "recommendations", "evidence",
                    "confidence", "action_items"):
        assert section in review, section
    assert review["executive_summary"]
    assert review["evidence"], "a review with no evidence"


def test_a_review_of_an_unmeasurable_product_says_so(reviews, catalog):
    product, _ = catalog.upsert("Ghost Product")
    review = reviews.review(product["product_id"])

    assert "cannot be scored" in review["executive_summary"]
    assert any("Connect" in a["action"] for a in review["action_items"])


def test_empty_sections_state_the_absence_rather_than_pretending(reviews,
                                                                 health,
                                                                 payments):
    health.evaluate(payments["product_id"])
    review = reviews.review(payments["product_id"])

    assert review["risks"], "risks must never be a silently empty list"
    assert review["strengths"]
    assert review["weaknesses"]


def test_a_review_registers_with_the_existing_review_center(reviews, health,
                                                            payments):
    registered = []

    class _Center:
        def register(self, project_id, version, title, health_score):
            registered.append(title)

    reviews._reviews = _Center()
    health.evaluate(payments["product_id"])
    reviews.review(payments["product_id"], register=True)

    assert registered and "product review" in registered[0]


# ------------------------------------------------------------------- KPIs
@pytest.mark.parametrize("name,expected", [
    ("Transaction Revenue", "business"),
    ("Failed Transactions", "operational"),
    ("Active Customers", "growth"),
    ("Merchant Retention", "growth"),
    ("Transaction Volume", "operational"),
    ("Some Random Metric", None),
])
def test_kpis_are_classified_by_what_they_measure(name, expected):
    assert classify(name) == expected


def test_a_failure_kpi_is_operational_not_revenue():
    """"Failed payment value" measures a failure, not revenue — order of
    classification matters."""
    assert classify("Failed Payment Value") == "operational"


@pytest.fixture()
def kpi_intelligence(product_store, catalog, health, gatherer):
    return KPIIntelligence(product_store, catalog, health, gatherer)


def test_a_rising_failure_kpi_breaches_its_threshold(kpi_intelligence,
                                                     payments):
    outcome = kpi_intelligence.monitor()
    breaches = {b["kpi"]: b for b in outcome["breaches"]}

    assert "Failed Transactions" in breaches, \
        "a 22% rise in failures did not breach the operational threshold"
    assert breaches["Failed Transactions"]["category"] == "operational"
    assert breaches["Failed Transactions"]["severity"] == "warning"


def test_a_healthy_kpi_does_not_breach(kpi_intelligence, payments):
    outcome = kpi_intelligence.monitor()
    breached = {b["kpi"] for b in outcome["breaches"]}

    assert "Transaction Revenue" not in breached, \
        "a growing revenue KPI raised an alert"


def test_a_breach_creates_work_through_the_existing_task_manager(
        product_store, catalog, health, gatherer, payments, artifacts):
    created = []

    class _Tasks:
        def create(self, title, **kwargs):
            created.append(title)
            return {"task_id": "t1"}

    class _Notifications:
        def notify(self, kind, title, **kwargs):
            return {"kind": kind, "notification_id": "n1"}

    artifacts.save(PID, "kpis", [_kpi("Failed Transactions", 2000.0, 40.0)])
    engine = KPIIntelligence(product_store, catalog, health, gatherer,
                             tasks=_Tasks(), notifications=_Notifications())
    outcome = engine.monitor()

    assert outcome["generated"]["tasks"] == 1, "a critical breach made no task"
    assert created and "Investigate" in created[0]


def test_the_same_breach_does_not_nag_twice(kpi_intelligence, payments):
    """A breach that is still breaching is still true — it just must not
    raise the same task and alert on every heartbeat."""
    first = kpi_intelligence.monitor()
    second = kpi_intelligence.monitor()

    assert first["kpis_breached"] > 0
    assert second["kpis_breached"] == 0, "the same breach alerted twice"
    assert second["kpis_breaching"] == first["kpis_breaching"], \
        "a still-breaching KPI stopped being reported as breaching"


def test_a_threshold_can_be_configured_without_a_deploy(kpi_intelligence):
    rule = kpi_intelligence.set_threshold("Transaction Revenue", warning=-1.0,
                                          critical=-2.0)

    assert rule["warning"] == -1.0
    assert kpi_intelligence.threshold_for("transaction revenue",
                                          "business")["critical"] == -2.0


def test_an_unknown_threshold_direction_is_rejected(kpi_intelligence):
    with pytest.raises(ValueError, match="Unknown direction"):
        kpi_intelligence.set_threshold("X", 1, 2, direction="sideways")


# -------------------------------------------------------------- scenarios
@pytest.fixture()
def scenarios(product_store, catalog, gatherer):
    return ScenarioSimulation(product_store, catalog, gatherer)


def test_a_scenario_projects_from_real_kpis(scenarios, payments):
    scenario = scenarios.simulate("customer_growth", 15.0)

    assert scenario["projections"], "nothing was projected"
    revenue = next(p for p in scenario["projections"]
                   if p["kpi"] == "Transaction Revenue")
    # customer_growth propagates to revenue at 0.8 → 15% × 0.8 = 12%
    assert revenue["change_pct"] == pytest.approx(12.0)
    assert revenue["projected_value"] == pytest.approx(120000 * 1.12)


def test_a_scenario_inherits_the_forecast_confidence(scenarios, payments):
    scenario = scenarios.simulate("revenue", 10.0)
    revenue = next(p for p in scenario["projections"]
                   if p["kpi"] == "Transaction Revenue")

    assert revenue["confidence"] == pytest.approx(0.82), \
        "confidence was asserted rather than inherited from the forecast"
    assert "validated" in revenue["confidence_basis"]


def test_a_low_confidence_forecast_lowers_the_projection_confidence(
        scenarios, payments, artifacts):
    artifacts.save(PID, "forecasts", [
        {"kpi_id": "kpi_transaction_revenue", "kpi_name": "Transaction Revenue",
         "values": [1.0, 2.0], "method": "naive", "confidence": 0.9,
         "status": "low_confidence", "validation": ["only 4 observations"]}])
    scenario = scenarios.simulate("revenue", 10.0)
    revenue = next(p for p in scenario["projections"]
                   if p["kpi"] == "Transaction Revenue")

    assert revenue["confidence"] <= 0.4, \
        "a low-confidence forecast was trusted at face value"
    assert "only 4 observations" in revenue["confidence_basis"]


def test_a_scenario_states_its_assumptions(scenarios, payments):
    scenario = scenarios.simulate("customer_growth", 15.0)

    assert scenario["assumptions"]
    assert any("linear" in a for a in scenario["assumptions"])
    assert any("Nothing else moves" in a for a in scenario["assumptions"])


def test_an_unsupported_scenario_refuses_to_estimate(scenarios, catalog):
    """The platform must not invent a baseline it never measured."""
    catalog.upsert("Ghost Product")
    scenario = scenarios.simulate("customer_growth", 15.0,
                                  product_id="product:ghost_product")

    assert scenario["projections"] == []
    assert scenario["confidence"] == 0.0
    assert "cannot be simulated" in scenario["summary"]
    assert scenario["unsimulatable"]


def test_an_unknown_lever_is_rejected(scenarios):
    with pytest.raises(ValueError, match="Unknown scenario lever"):
        scenarios.simulate("vibes", 10.0)


def test_the_levers_are_discoverable(scenarios):
    levers = {l["lever"] for l in scenarios.levers()}

    assert {"customer_growth", "merchant_failures", "transaction_volume",
            "revenue", "feature_launch"} <= levers


# -------------------------------------------------------------- portfolio
@pytest.fixture()
def portfolio(catalog, health, growth, strategy):
    return PortfolioIntelligence(catalog, health, growth, strategy)


def test_the_portfolio_ranks_and_prioritizes(portfolio, health, payments):
    health.evaluate(payments["product_id"])
    evaluation = portfolio.evaluate()

    assert evaluation["portfolio_health"]["score"] is not None
    assert evaluation["product_ranking"][0]["rank"] == 1
    assert evaluation["product_ranking"][0]["investment_priority"] in (
        "invest", "fix", "maintain", "watch", "question")
    assert evaluation["product_ranking"][0]["priority_reason"]


def test_an_unmeasured_product_is_watch_not_defunded(portfolio, catalog,
                                                     health):
    product, _ = catalog.upsert("Ghost Product")
    health.evaluate(product["product_id"])
    ranking = {r["product"]: r for r in portfolio.evaluate()["product_ranking"]}

    entry = ranking["Ghost Product"]
    assert entry["investment_priority"] == "watch"
    assert "not measurable" in entry["priority_reason"]


def test_unmeasured_products_rank_last(portfolio, catalog, health, payments):
    catalog.upsert("Ghost Product")
    health.evaluate(payments["product_id"])
    health.evaluate("product:ghost_product")
    ranking = portfolio.evaluate()["product_ranking"]

    assert ranking[-1]["product"] == "Ghost Product", \
        "an unscored product outranked a measured one"


def test_a_healthy_growing_product_is_an_invest_call(portfolio, health,
                                                     payments):
    health.evaluate(payments["product_id"])
    ranking = {r["product"]: r for r in portfolio.evaluate()["product_ranking"]}

    assert ranking["Payments"]["investment_priority"] in ("invest", "maintain")


def test_the_portfolio_reports_coverage_honestly(portfolio, catalog, health,
                                                 payments):
    catalog.upsert("Ghost Product")
    health.evaluate(payments["product_id"])
    health.evaluate("product:ghost_product")
    coverage = portfolio.evaluate()["coverage"]

    assert coverage["products"] == 2
    assert coverage["measured"] == 1
    assert coverage["unmeasured"] == 1


# ----------------------------------------------------------------- briefs
@pytest.fixture()
def briefs(product_store, portfolio, catalog, health, growth, strategy,
           reviews):
    return ExecutiveBriefGenerator(product_store, portfolio, catalog, health,
                                   growth, strategy, reviews)


@pytest.mark.parametrize("kind", ["board_brief", "monthly_review",
                                  "quarterly_strategy", "risk_summary",
                                  "growth_summary", "decision_pack"])
def test_every_brief_generates_with_markdown(briefs, health, payments, kind):
    health.evaluate(payments["product_id"])
    brief = briefs.generate(kind)

    assert brief["headline"]
    assert brief["sections"]
    assert brief["markdown"].startswith("#")
    assert brief["coverage"]["products"] >= 1


def test_a_brief_over_an_unmeasured_portfolio_says_so(briefs, catalog, health):
    catalog.upsert("Ghost Product")
    health.evaluate("product:ghost_product")
    brief = briefs.generate("board_brief")

    assert "none measurable yet" in brief["headline"]


def test_an_unknown_brief_is_rejected(briefs):
    with pytest.raises(ValueError, match="Unknown brief"):
        briefs.generate("vibes_report")


def test_the_decision_pack_reads_the_existing_action_queue(briefs, health,
                                                           payments):
    class _Queue:
        def pending_approvals(self, limit=20):
            return [{"title": "Email the board", "kind": "send_email",
                     "priority": 2}]

    briefs.attach_queue(_Queue())
    health.evaluate(payments["product_id"])
    brief = briefs.generate("decision_pack")

    assert "1 decision(s) await approval" in brief["headline"]
    assert any("Email the board" in f
               for s in brief["sections"] for f in s["facts"])

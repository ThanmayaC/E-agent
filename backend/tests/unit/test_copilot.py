"""Enterprise Copilot Layer — intent, planning, context, evidence, routing,
validation, conversations, suggested actions, and the orchestrator.

The validator gets adversarial tests: it is the gate between a language model
and an executive who will act on what it says, so the tests feed it answers
that invent numbers, invent KPIs, cite nothing, and contradict the business's
own rules, and assert that none of them reach the executive.
"""
from __future__ import annotations

import pytest

from app.agents.prompt_generator import PromptGenerationAgent
from app.copilot.actions import SuggestedActionsBuilder
from app.copilot.context import ContextBuilder
from app.copilot.conversations import ConversationMemory
from app.copilot.copilot import EnterpriseCopilot
from app.copilot.evidence import Evidence, EvidenceCollector
from app.copilot.intent import IntentClassifier
from app.copilot.planner import ROUTES, RequestPlanner
from app.copilot.router import LLMRouter
from app.copilot.store import CopilotStore
from app.copilot.validator import ResponseValidator
from app.knowledge.store import KnowledgeStore
from app.repositories.artifact_store import ArtifactStore

PID = "proj_pay"


def _kpi(name, value, growth, kpi_id=None, unit=""):
    return {"id": kpi_id or f"kpi_{name.lower().replace(' ', '_')}",
            "name": name, "current_value": value, "growth_pct": growth,
            "trend": "up" if growth > 0 else "down", "unit": unit}


@pytest.fixture()
def artifacts(tmp_path):
    store = ArtifactStore(tmp_path / "projects")
    store.save(PID, "state", {"project_id": PID, "name": "Payments",
                              "status": "ready"})
    store.save(PID, "kpis", [
        _kpi("Transaction Revenue", 120000.0, 12.0, unit="$"),
        _kpi("Active Customers", 5200.0, 15.0),
    ])
    store.save(PID, "signals", [
        {"id": "sig_1", "kind": "trend", "kpi_name": "Transaction Revenue",
         "strength": 0.8, "stats": {"slope": 1.2}}])
    store.save(PID, "forecasts", [
        {"kpi_id": "kpi_transaction_revenue",
         "kpi_name": "Transaction Revenue", "horizon": "next_quarter",
         "values": [125000.0, 131000.0], "method": "holt_linear",
         "confidence": 0.82, "status": "ok", "validation": []}])
    store.save(PID, "quality", {"overall_score": 88.0})
    return store


@pytest.fixture()
def knowledge(tmp_path):
    store = KnowledgeStore(tmp_path / "knowledge")
    store.record_report(PID, "Payments — report v1", 74.0)
    store.add_rule("Never offer discounts above 20%", scope="global")
    store.add_term("Merchant", "A business that accepts payments")
    return store


@pytest.fixture()
def copilot_store(tmp_path):
    return CopilotStore(tmp_path / "copilot")


@pytest.fixture()
def conversations(copilot_store, knowledge):
    return ConversationMemory(copilot_store, knowledge=knowledge)


@pytest.fixture()
def collector(knowledge, artifacts):
    return EvidenceCollector(knowledge, artifacts)


@pytest.fixture()
def planner():
    return RequestPlanner()


@pytest.fixture()
def classifier():
    return IntentClassifier(subjects=["payments", "checkout"])


# --------------------------------------------------------------- intent
@pytest.mark.parametrize("message,expected", [
    ("What if customer growth increases 15%?", "scenario"),
    ("Why did revenue fall last month?", "explanation"),
    ("Compare Payments and Checkout", "comparison"),
    ("What will revenue be next quarter?", "forecast"),
    ("What should we do about churn?", "recommendation"),
    ("What needs my approval?", "approval"),
    ("Create a task to review pricing", "task"),
    ("Find everything about merchant fees", "search"),
    ("Give me the board brief", "executive_brief"),
    ("Prepare me for the board meeting", "meeting_prep"),
    ("Run the daily cycle workflow", "workflow"),
    ("We decided to go with vendor A", "decision"),
    ("Analyse the payments decline", "analysis"),
])
def test_intent_is_detected_from_the_request(classifier, message, expected):
    assert classifier.classify(message).intent == expected


def test_intent_detection_needs_no_llm(classifier):
    """Routing must not depend on a model: an LLM that hallucinates the route
    produces a wrong answer before the answering model sees a fact."""
    intent = classifier.classify("What if merchant failures increase 20%?")

    assert intent.intent == "scenario"
    assert intent.confidence > 0
    assert intent.matched, "the classifier gave no reason for its decision"


def test_a_known_subject_is_resolved(classifier):
    assert classifier.classify("How is Payments doing?").subject == "payments"


def test_an_unknown_noun_is_never_a_subject(classifier):
    """A word the platform does not know is not a subject; it is just a word."""
    assert classifier.classify("How is Fictional Product doing?").subject == ""


def test_subjects_are_learned_not_hardcoded():
    classifier = IntentClassifier()
    assert classifier.classify("How is Payments doing?").subject == ""

    classifier.set_subjects(["Payments"])
    assert classifier.classify("How is Payments doing?").subject == "payments"


def test_an_ambiguous_request_is_flagged_not_guessed(classifier):
    intent = classifier.classify("compare the forecast")

    assert intent.alternatives, "no runner-up was reported"
    if intent.ambiguous:
        assert intent.alternatives[0]["intent"] != intent.intent


def test_an_empty_message_is_ambiguous_not_a_crash(classifier):
    intent = classifier.classify("   ")

    assert intent.ambiguous is True
    assert intent.confidence == 0.0


# --------------------------------------------------------------- planner
def test_every_intent_has_a_route(classifier, planner):
    from app.copilot.intent import INTENTS
    for intent_name in INTENTS:
        assert intent_name in ROUTES, f"{intent_name} has no route"


def test_a_plan_names_only_real_modules(classifier, planner):
    from app.copilot.planner import MODULES
    for intent_name in ROUTES:
        plan = planner.plan(_intent(intent_name))
        assert set(plan.modules) <= set(MODULES)


def test_a_plan_orders_context_before_judgement(classifier, planner):
    plan = planner.plan(_intent("analysis"))

    assert plan.order[0] == "brain", "analytics were read before context"
    assert plan.order.index("analytics") < plan.order.index("product")


def test_a_scenario_plan_needs_no_llm_to_compute(planner):
    """Projections are computed deterministically by the Scenario module; the
    model only narrates them."""
    plan = planner.plan(_intent("scenario"))

    assert plan.expected_output == "scenario_projection"
    assert plan.needs_llm is False


def test_an_approval_plan_never_lets_the_copilot_approve(planner):
    plan = planner.plan(_intent("approval"))

    assert plan.approvals_required == ["executive"]
    assert any("never approves" in n for n in plan.notes)


def test_a_bad_route_fails_loudly(planner, monkeypatch):
    monkeypatch.setitem(ROUTES, "question",
                        {"modules": ["not_a_module"], "output": "answer"})
    with pytest.raises(ValueError, match="unknown modules"):
        planner.plan(_intent("question"))


# -------------------------------------------------------------- evidence
def test_evidence_is_collected_with_citable_ids(collector, planner):
    plan = planner.plan(_intent("analysis"))
    evidence = collector.collect(plan)

    assert evidence.items
    assert all(i["id"] for i in evidence.items), "evidence without an id"
    assert "kpi" in evidence.by_kind
    assert "signal" in evidence.by_kind


def test_evidence_without_an_id_is_not_evidence():
    """The ids are the contract the validator enforces — an item the validator
    cannot check is not evidence."""
    evidence = Evidence()
    evidence.add("kpi", "", "a fact with no id")

    assert evidence.items == []


def test_a_forecasts_validation_gate_travels_with_the_fact(collector, planner):
    plan = planner.plan(_intent("forecast"))
    evidence = collector.collect(plan)
    forecast = evidence.by_kind["forecast"][0]

    assert forecast["status"] == "ok"
    assert "confidence" in forecast


def test_a_missing_source_is_recorded_not_raised(knowledge, artifacts,
                                                 planner):
    """No product layer wired: evidence that needs it is reported missing."""
    collector = EvidenceCollector(knowledge, artifacts, product=None)
    evidence = collector.collect(planner.plan(_intent("recommendation")))

    assert evidence.missing, "an absent module produced no explanation"
    assert any("product" in m for m in evidence.missing)


def test_thin_evidence_is_flagged_as_weak(knowledge, tmp_path, planner):
    collector = EvidenceCollector(knowledge,
                                  ArtifactStore(tmp_path / "empty"))
    evidence = collector.collect(planner.plan(_intent("question")))

    assert evidence.is_weak is True


def test_evidence_exposes_its_numbers_and_kpi_names(collector, planner):
    evidence = collector.collect(planner.plan(_intent("analysis")))

    assert 120000.0 in evidence.numbers()
    assert "transaction revenue" in evidence.kpi_names()


# ------------------------------------------------------------- validator
@pytest.fixture()
def validator():
    return ResponseValidator()


@pytest.fixture()
def evidence(collector, planner):
    return collector.collect(planner.plan(_intent("analysis")))


def _response(answer: str, confidence: float = 0.9,
              evidence_ids: list[str] | None = None) -> dict:
    # `is None` rather than `or`: an explicit empty list is the uncited case
    # under test, and must not be silently replaced by the default.
    if evidence_ids is None:
        evidence_ids = ["kpi_transaction_revenue"]
    return {"status": "ok", "answer": answer, "cited_facts": [],
            "evidence_ids": evidence_ids, "confidence": confidence,
            "limitations": [], "suggested_actions": []}


def test_an_invented_number_is_rejected(validator, evidence):
    """The single most dangerous thing this layer could emit: a figure an
    executive acts on that the platform cannot source."""
    checked, validation = validator.validate(
        _response("Revenue reached 987654 this quarter."), evidence)

    assert validation.verdict == "rejected"
    assert checked["confidence"] == 0.0
    assert "not in the evidence" in validation.rejections[0]
    assert "987654" in validation.rejections[0]


def test_a_real_number_from_the_evidence_passes(validator, evidence):
    checked, validation = validator.validate(
        _response("Transaction Revenue is 120000, up 12%."), evidence)

    assert validation.verdict != "rejected", validation.rejections
    assert checked["confidence"] > 0


def test_a_rounded_number_is_accepted(validator, evidence):
    """Models legitimately round 120000.0 to 120,000 — rejecting that would
    make the gate useless."""
    _, validation = validator.validate(
        _response("Transaction Revenue is about 120,000."), evidence)

    assert validation.verdict != "rejected", validation.rejections


def test_small_numbers_in_prose_are_not_treated_as_claims(validator,
                                                          evidence):
    _, validation = validator.validate(
        _response("There are 3 things to note about revenue."), evidence)

    assert validation.verdict != "rejected", validation.rejections


def test_an_invented_kpi_is_rejected(validator, evidence):
    checked, validation = validator.validate(
        _response("Customer Churn Rate is 12%, which is concerning."),
        evidence)

    assert validation.verdict == "rejected"
    assert "KPI" in validation.rejections[0]


def test_an_answer_contradicting_a_business_rule_is_rejected(validator,
                                                             evidence):
    checked, validation = validator.validate(
        _response("We should offer discounts above 20% to win the segment."),
        evidence, business_rules=["Never offer discounts above 20%"])

    assert validation.verdict == "rejected"
    assert "business rule" in validation.rejections[0]


def test_a_number_quoted_from_a_business_rule_is_not_an_invention(validator,
                                                                  evidence):
    """The rules are given to the model as context, so a figure quoted from
    one is sourced. Flagging it would reject a correct answer — and a gate
    that cries wolf gets switched off."""
    _, validation = validator.validate(
        _response("Our policy caps discounts at 20%, so that offer is not "
                  "possible."),
        evidence, business_rules=["Never offer discounts above 20%"])

    assert validation.verdict != "rejected", validation.rejections


def test_a_rule_contradiction_outranks_an_unsourced_figure(validator,
                                                           evidence):
    """When an answer both breaks a rule and quotes a stray number, the
    executive should be told the important one first."""
    _, validation = validator.validate(
        _response("We should offer discounts above 20% and target 987654 in "
                  "new revenue."),
        evidence, business_rules=["Never offer discounts above 20%"])

    assert validation.verdict == "rejected"
    assert "business rule" in validation.rejections[0]


def test_an_invented_citation_is_stripped(validator, evidence):
    checked, validation = validator.validate(
        _response("Transaction Revenue is 120000.",
                  evidence_ids=["kpi_transaction_revenue", "kpi_fabricated"]),
        evidence)

    assert "kpi_fabricated" in validation.rejected_ids
    assert checked["evidence_ids"] == ["kpi_transaction_revenue"]
    assert validation.verdict == "downgraded"


def test_an_uncited_answer_cannot_claim_confidence(validator, evidence):
    checked, validation = validator.validate(
        _response("Things look broadly positive.", confidence=0.95,
                  evidence_ids=[]), evidence)

    assert checked["confidence"] <= 0.3
    assert validation.verdict == "downgraded"


def test_weak_evidence_caps_confidence(validator, knowledge, tmp_path,
                                       planner):
    collector = EvidenceCollector(knowledge, ArtifactStore(tmp_path / "empty"))
    thin = collector.collect(planner.plan(_intent("question")))
    checked, validation = validator.validate(
        _response("Everything is fine.", confidence=0.99, evidence_ids=[]),
        thin)

    assert checked["confidence"] <= 0.4
    assert any("capped" in w for w in validation.warnings)


def test_a_refusal_may_cite_nothing(validator, evidence):
    """Declining to answer asserts nothing, so it needs no citation and must
    not be punished for having none."""
    checked, validation = validator.validate(
        _response("The available evidence cannot answer that; revenue by "
                  "region would be required.", confidence=0.8,
                  evidence_ids=[]), evidence)

    assert validation.verdict != "rejected"
    assert checked["confidence"] == 0.8, "an honest refusal was downgraded"


def test_a_rejected_answer_is_replaced_with_an_honest_one(validator,
                                                          evidence):
    checked, _ = validator.validate(
        _response("Revenue reached 987654 this quarter."), evidence)

    assert "can't give you that answer" in checked["answer"]
    assert "What the evidence does support" in checked["answer"]
    assert checked["cited_facts"] == []


def test_an_unavailable_response_is_not_judged(validator, evidence):
    _, validation = validator.validate(
        {"status": "unavailable", "answer": "No provider configured",
         "confidence": 0.0}, evidence)

    assert validation.verdict == "verified"  # nothing was claimed


# ---------------------------------------------------------------- router
def test_the_router_reuses_the_provider_abstraction():
    class _Provider:
        name = "mock"
        model = "mock-1"
        config = type("C", (), {"model": "mock-1"})()

        def chat_json(self, messages):
            return {"answer": "Revenue is 120000.", "confidence": 0.8,
                    "evidence_ids": ["kpi_1"], "cited_facts": ["120000"]}

    router = LLMRouter(_Provider())
    outcome = router.route(type("P", (), {"system": "s", "user": "u"})())

    assert outcome["status"] == "ok"
    assert outcome["provider"] == "mock"
    assert router.describe()["primary"]["provider"] == "mock"


def test_the_router_falls_back_when_the_primary_fails():
    class _Broken:
        name = "broken"
        model = "x"
        config = type("C", (), {"model": "x"})()

        def chat_json(self, messages):
            raise RuntimeError("provider is down")

    class _Working(_Broken):
        name = "backup"

        def chat_json(self, messages):
            return {"answer": "ok", "confidence": 0.5}

    router = LLMRouter(_Broken(), _Working())
    outcome = router.route(type("P", (), {"system": "s", "user": "u"})())

    assert outcome["status"] == "ok"
    assert outcome["provider"] == "backup"


def test_no_provider_degrades_rather_than_failing():
    router = LLMRouter(None)
    outcome = router.route(type("P", (), {"system": "s", "user": "u"})())

    assert outcome["status"] == "unavailable"
    assert router.available is False
    assert "EDIP_LLM_PROVIDER" in outcome["answer"]


def test_a_failing_provider_never_raises():
    class _Broken:
        name = "broken"
        model = "x"
        config = type("C", (), {"model": "x"})()

        def chat_json(self, messages):
            raise RuntimeError("down")

    outcome = LLMRouter(_Broken()).route(
        type("P", (), {"system": "s", "user": "u"})())

    assert outcome["status"] == "failed"
    assert outcome["confidence"] == 0.0


# --------------------------------------------------------- conversations
def test_a_conversation_records_history(conversations):
    conversation = conversations.start(title="Portfolio review")
    conversations.append(conversation["conversation_id"], "user", "How are we?")
    conversations.append(conversation["conversation_id"], "assistant", "Fine.")

    messages = conversations.messages(conversation["conversation_id"])
    assert [m["role"] for m in messages] == ["user", "assistant"]


def test_an_unknown_role_is_rejected(conversations):
    conversation = conversations.start()
    with pytest.raises(ValueError, match="Unknown message role"):
        conversations.append(conversation["conversation_id"], "system", "x")


def test_a_stale_conversation_id_starts_a_fresh_thread(conversations):
    """An executive mid-question must never see a 404."""
    conversation = conversations.ensure("cnv_does_not_exist")

    assert conversation["conversation_id"] != "cnv_does_not_exist"


def test_preferences_are_counted_not_inferred(conversations):
    conversation = conversations.start()
    for _ in range(3):
        conversations.append(conversation["conversation_id"], "user",
                             "How is Payments?",
                             meta={"intent": "question", "subject": "payments"})
    preferences = conversations.preferences()

    assert preferences["frequent_intents"][0] == ("question", 3)
    assert preferences["frequent_subjects"][0] == ("payments", 3)


def test_conversations_are_searchable(conversations):
    conversation = conversations.start(title="Merchant fees")
    conversations.append(conversation["conversation_id"], "user",
                         "What are our merchant fees?")
    hits = conversations.search("merchant fees")

    assert hits and hits[0]["conversation_id"] == conversation["conversation_id"]
    assert hits[0]["matches"]


def test_a_clarification_goes_to_the_knowledge_store(conversations,
                                                     knowledge):
    """An answer the business gives once belongs to the organization."""
    assert conversations.record_clarification("What is a merchant?",
                                              "A business accepting payments")
    stored = knowledge.snapshot()["clarifications"]

    assert any("merchant" in c["question"].lower() for c in stored)


def test_pinned_conversations_are_never_pruned(conversations):
    pinned = conversations.start(title="Important")
    conversations.pin(pinned["conversation_id"])
    for i in range(5):
        conversations.start(title=f"Chat {i}")

    conversations.prune(keep=2)
    remaining = {c["conversation_id"] for c in conversations.conversations()}
    assert pinned["conversation_id"] in remaining


def test_deleting_a_conversation_removes_its_messages(conversations):
    conversation = conversations.start()
    conversations.append(conversation["conversation_id"], "user", "hello")
    conversations.delete(conversation["conversation_id"])

    assert conversations.messages(conversation["conversation_id"]) == []


# ------------------------------------------------------------ orchestrator
@pytest.fixture()
def copilot(knowledge, artifacts, conversations, classifier, planner,
            collector):
    context = ContextBuilder(knowledge=knowledge, artifacts=artifacts,
                             conversations=conversations)

    class _Provider:
        name = "mock"
        model = "mock-1"
        config = type("C", (), {"model": "mock-1"})()

        def chat_json(self, messages):
            return {"answer": "Transaction Revenue is 120000, up 12%.",
                    "confidence": 0.8,
                    "evidence_ids": ["kpi_transaction_revenue"],
                    "cited_facts": ["120000"],
                    "suggested_actions": ["Review the revenue trend"]}

    return EnterpriseCopilot(
        intent=classifier, planner=planner, context=context,
        evidence=collector, router=LLMRouter(_Provider()),
        validator=ResponseValidator(), conversations=conversations,
        actions=SuggestedActionsBuilder(), prompt_agent=PromptGenerationAgent())


def test_the_pipeline_runs_end_to_end(copilot):
    answer = copilot.chat("How is Transaction Revenue doing?")

    assert answer["status"] == "ok"
    assert answer["intent"]["intent"]
    assert answer["plan"]["modules"]
    assert answer["evidence"]["total"] > 0
    assert answer["validation"]["verdict"] in ("verified", "downgraded")
    assert answer["conversation_id"]


def test_evidence_is_gathered_before_the_model_is_asked(copilot):
    """The model narrates a closed set; it never decides what is true."""
    seen = {}

    class _Recording:
        name = "mock"
        model = "m"
        config = type("C", (), {"model": "m"})()

        def chat_json(self, messages):
            seen["prompt"] = messages[1].content
            return {"answer": "Revenue is 120000.", "confidence": 0.7,
                    "evidence_ids": ["kpi_transaction_revenue"]}

    copilot._router = LLMRouter(_Recording())
    copilot.chat("How is revenue?")

    assert "EVIDENCE" in seen["prompt"]
    assert "kpi_transaction_revenue" in seen["prompt"], \
        "the model was asked without being given the evidence"


def test_a_hallucinated_answer_never_reaches_the_executive(copilot):
    class _Hallucinating:
        name = "mock"
        model = "m"
        config = type("C", (), {"model": "m"})()

        def chat_json(self, messages):
            return {"answer": "Revenue hit 999999 after our campaign.",
                    "confidence": 0.95, "evidence_ids": []}

    copilot._router = LLMRouter(_Hallucinating())
    answer = copilot.chat("How is revenue?")

    assert answer["validation"]["verdict"] == "rejected"
    assert answer["confidence"] == 0.0
    # The fabricated claim never passes through. The rejection does quote the
    # offending figure back — deliberately: it is labelled as not being in the
    # evidence, which tells the executive exactly what was wrong.
    assert "Revenue hit 999999 after our campaign" not in answer["answer"]
    assert "can't give you that answer" in answer["answer"]
    assert "not in the evidence: 999999" in answer["answer"]


def test_a_deterministic_intent_never_calls_the_model(copilot):
    class _Exploding:
        name = "mock"
        model = "m"
        config = type("C", (), {"model": "m"})()

        def chat_json(self, messages):
            raise AssertionError("the model was called for a known fact")

    copilot._router = LLMRouter(_Exploding())
    answer = copilot.chat("What needs my approval?")

    assert answer["status"] == "ok"
    assert answer["provider"]["provider"] == "deterministic"


def test_the_copilot_answers_without_any_llm(knowledge, artifacts,
                                             conversations, classifier,
                                             planner, collector):
    """No provider configured: the executive still gets the evidence."""
    context = ContextBuilder(knowledge=knowledge, artifacts=artifacts)
    copilot = EnterpriseCopilot(
        intent=classifier, planner=planner, context=context,
        evidence=collector, router=LLMRouter(None),
        validator=ResponseValidator(), conversations=conversations,
        actions=SuggestedActionsBuilder(), prompt_agent=PromptGenerationAgent())
    answer = copilot.chat("How is revenue?")

    assert answer["status"] == "unavailable"
    assert answer["evidence"]["total"] > 0, "evidence was withheld with no LLM"
    assert "EDIP_LLM_PROVIDER" in answer["answer"]


def test_the_conversation_is_remembered(copilot):
    first = copilot.chat("How is revenue?")
    copilot.chat("And what about customers?",
                 conversation_id=first["conversation_id"])
    messages = copilot._conversations.messages(first["conversation_id"])

    assert len(messages) == 4  # two exchanges
    assert messages[0]["meta"]["intent"]


def test_an_empty_message_is_rejected(copilot):
    with pytest.raises(ValueError, match="needs a message"):
        copilot.chat("   ")


def test_context_gaps_are_reported_not_hidden(copilot):
    answer = copilot.chat("How is the product portfolio?")

    assert "context_gaps" in answer
    assert any(g["source"] == "product" for g in answer["context_gaps"]), \
        "an absent module was silently ignored"


def test_the_context_surface_explains_what_the_copilot_knows(copilot):
    context = copilot.context_for("how is revenue?")

    assert context["intent"]["intent"]
    assert context["plan"]["modules"]
    assert context["evidence_items"]
    assert context["provider"]["available"] is True


def _intent(name: str):
    """A classified intent, without going through the classifier."""
    from app.copilot.intent import Intent
    return Intent(intent=name, confidence=1.0)

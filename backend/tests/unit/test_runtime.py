"""Autonomous execution layer — event bus, scheduler, cron, action queue,
approval layer, trigger engine, goals, planning, and the decision pipeline.

Every test drives the runtime by hand (``tick``, ``run_job``, ``publish``)
rather than sleeping: the heartbeat is a thread in production and a function
call in tests, which is the whole reason ``tick`` is public.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from app.knowledge.store import KnowledgeStore
from app.runtime.cron import CronError, CronSchedule
from app.runtime.decisions import DecisionEngine
from app.runtime.events import EventBus
from app.runtime.goals import GoalEngine
from app.runtime.planning import PlanningEngine
from app.runtime.queue import ActionQueue
from app.runtime.scheduler import EnterpriseScheduler, JobDefinition, RetryPolicy
from app.runtime.store import RuntimeStore
from app.runtime.triggers import TriggerEngine


@pytest.fixture()
def store(tmp_path):
    return RuntimeStore(tmp_path / "runtime")


@pytest.fixture()
def bus(store):
    return EventBus(store)


@pytest.fixture()
def queue(store, bus):
    return ActionQueue(store, bus)


# ------------------------------------------------------------- event bus
def test_subscribers_receive_published_events(bus):
    seen = []
    bus.subscribe("DatasetImported", lambda e: seen.append(e))
    bus.publish("DatasetImported", {"rows": 10}, project_id="p1")

    assert len(seen) == 1
    assert seen[0].payload["rows"] == 10
    assert seen[0].project_id == "p1"


def test_wildcard_subscriber_sees_every_kind(bus):
    seen = []
    bus.subscribe("*", lambda e: seen.append(e.kind))
    bus.publish("DatasetImported")
    bus.publish("ReportGenerated")

    assert seen == ["DatasetImported", "ReportGenerated"]


def test_failing_subscriber_never_breaks_the_publisher(bus):
    delivered = []

    def explode(event):
        raise RuntimeError("subscriber is broken")

    bus.subscribe("DatasetImported", explode, name="broken")
    bus.subscribe("DatasetImported", lambda e: delivered.append(e),
                  name="healthy")
    bus.publish("DatasetImported")  # must not raise

    assert len(delivered) == 1, "a broken subscriber blocked a healthy one"
    assert bus.stats()["subscriber_failures"] == 1
    assert bus.history(1)[0]["errors"], "the failure was not recorded"


def test_unknown_event_kind_is_rejected(bus):
    with pytest.raises(ValueError, match="Unknown event kind"):
        bus.publish("SomethingInvented")


def test_event_history_survives_a_new_bus(store):
    EventBus(store).publish("ReportGenerated", {"v": 1})
    assert EventBus(store).history(10)[0]["kind"] == "ReportGenerated"


# ------------------------------------------------------------------ cron
@pytest.mark.parametrize("expression,moment,expected", [
    ("0 6 * * *", datetime(2026, 7, 16, 6, 0, tzinfo=timezone.utc), True),
    ("0 6 * * *", datetime(2026, 7, 16, 6, 1, tzinfo=timezone.utc), False),
    ("*/15 * * * *", datetime(2026, 7, 16, 9, 30, tzinfo=timezone.utc), True),
    ("*/15 * * * *", datetime(2026, 7, 16, 9, 31, tzinfo=timezone.utc), False),
    ("0 9 * * 1-5", datetime(2026, 7, 16, 9, 0, tzinfo=timezone.utc), True),
    ("0 9 * * 1-5", datetime(2026, 7, 18, 9, 0, tzinfo=timezone.utc), False),
])
def test_cron_matches(expression, moment, expected):
    assert CronSchedule(expression).matches(moment) is expected


def test_cron_next_after_is_the_next_matching_minute():
    schedule = CronSchedule("0 6 * * *")
    next_run = schedule.next_after(datetime(2026, 7, 16, 7, 0,
                                            tzinfo=timezone.utc))
    assert next_run == datetime(2026, 7, 17, 6, 0, tzinfo=timezone.utc)


@pytest.mark.parametrize("expression", ["0 6 * *", "99 * * * *", "0 6 * * x"])
def test_bad_cron_is_rejected_at_parse_time(expression):
    with pytest.raises(CronError):
        CronSchedule(expression)


# ------------------------------------------------------------- scheduler
def test_startup_jobs_run_in_dependency_order(bus, store):
    order = []
    scheduler = EnterpriseScheduler(bus, store)
    scheduler.register(JobDefinition("second", "runs second", "startup",
                                     lambda: order.append("second"),
                                     depends_on=["first"]))
    scheduler.register(JobDefinition("first", "runs first", "startup",
                                     lambda: order.append("first")))
    scheduler.start()
    scheduler.stop()

    assert order == ["first", "second"]


def test_job_retries_then_records_the_failure(bus, store):
    attempts = []

    def flaky():
        attempts.append(1)
        raise RuntimeError("still broken")

    scheduler = EnterpriseScheduler(bus, store)
    scheduler.register(JobDefinition(
        "flaky", "fails every time", "startup", flaky,
        retry=RetryPolicy(attempts=3, backoff_seconds=0.0)))
    execution = scheduler.run_job("flaky")

    assert len(attempts) == 3, "the retry policy was not honoured"
    assert execution["status"] == "failed"
    assert "still broken" in execution["error"]
    assert scheduler.describe_job("flaky")["consecutive_failures"] == 1


def test_a_failing_job_never_raises_to_the_caller(bus, store):
    scheduler = EnterpriseScheduler(bus, store)
    scheduler.register(JobDefinition(
        "boom", "explodes", "interval", lambda: 1 / 0,
        interval_seconds=1, retry=RetryPolicy(attempts=1)))
    scheduler.run_job("boom")  # the heartbeat must survive a bad beat

    assert scheduler.describe_job("boom")["status"] == "failed"


def test_interval_jobs_wait_one_interval_before_their_first_run(bus, store):
    scheduler = EnterpriseScheduler(bus, store)
    scheduler.register(JobDefinition("later", "not yet", "interval",
                                     lambda: "ran", interval_seconds=3600))

    assert scheduler.tick() == [], "an interval job ran before its interval"


def test_a_disabled_job_never_runs_on_a_tick(bus, store):
    scheduler = EnterpriseScheduler(bus, store)
    scheduler.register(JobDefinition("daily", "at 06:00", "cron",
                                     lambda: "ran", cron="0 6 * * *"))
    scheduler.enable("daily", False)
    next_run = datetime.fromisoformat(
        scheduler.describe_job("daily")["next_run_at"])

    assert scheduler.tick(next_run) == []


def test_event_jobs_run_when_their_event_is_published(bus, store):
    runs = []
    scheduler = EnterpriseScheduler(bus, store)
    scheduler.register(JobDefinition("on_import", "reacts", "event",
                                     lambda: runs.append(1),
                                     event="DatasetImported"))
    bus.publish("DatasetImported")

    assert len(runs) == 1


def test_cron_jobs_are_due_only_at_their_next_run(bus, store):
    scheduler = EnterpriseScheduler(bus, store)
    scheduler.register(JobDefinition("daily", "at 06:00", "cron",
                                     lambda: "ran", cron="0 6 * * *"))
    next_run = datetime.fromisoformat(
        scheduler.describe_job("daily")["next_run_at"])

    assert scheduler.tick(next_run - timedelta(minutes=1)) == []
    assert scheduler.tick(next_run) == ["daily"]


def test_executions_are_recorded_and_announced(bus, store):
    announced = []
    bus.subscribe("JobCompleted", lambda e: announced.append(e.payload["job"]))
    scheduler = EnterpriseScheduler(bus, store)
    scheduler.register(JobDefinition("work", "does work", "startup",
                                     lambda: {"did": "work"}))
    scheduler.run_job("work")

    assert announced == ["work"]
    assert scheduler.executions(1)[0]["result"] == {"did": "work"}


# ----------------------------------------------------------- action queue
def test_external_actions_wait_for_approval(queue):
    action = queue.submit("send_email", "Email the brief")

    assert action["status"] == "pending_approval"
    assert action["requires_approval"] is True


def test_internal_actions_are_auto_approved(queue):
    assert queue.submit("create_task", "Investigate X")["status"] == "approved"


def test_equivalent_open_actions_are_not_queued_twice(queue):
    assert queue.submit("create_task", "Investigate X", source_ref="x")
    assert queue.submit("create_task", "Investigate X", source_ref="x") is None


def test_approve_then_execute_runs_the_executor(queue):
    executed = []
    queue.register_executor("send_email", lambda a: executed.append(a["title"]))
    action = queue.submit("send_email", "Email the brief")
    queue.approve(action["action_id"], by="cfo")
    outcome = queue.execute(action["action_id"])

    assert executed == ["Email the brief"]
    assert outcome["status"] == "executed"
    assert outcome["approved_by"] == "cfo"


def test_rejected_actions_never_execute(queue):
    queue.register_executor("send_email", lambda a: pytest.fail("it was sent"))
    action = queue.submit("send_email", "Email the brief")
    queue.reject(action["action_id"], by="cfo", reason="not now")

    with pytest.raises(ValueError, match="not approved"):
        queue.execute(action["action_id"])


def test_an_unapproved_action_cannot_be_executed(queue):
    queue.register_executor("send_email", lambda a: pytest.fail("it was sent"))
    action = queue.submit("send_email", "Email the brief")

    with pytest.raises(ValueError, match="not approved"):
        queue.execute(action["action_id"])


def test_a_failing_executor_leaves_the_queue_draining(queue):
    def explode(action):
        raise RuntimeError("smtp is down")

    queue.register_executor("create_task", explode)
    queue.submit("create_task", "First")
    queue.submit("create_task", "Second")
    outcome = queue.execute_ready()

    assert outcome == {"executed": 0, "failed": 2, "waiting_for_executor": 0}
    assert all(a["error"] for a in queue.actions(status="failed"))


def test_execute_ready_only_drains_approved_actions_with_executors(queue):
    queue.register_executor("create_task", lambda a: "done")
    queue.submit("create_task", "Runs")
    queue.submit("send_email", "Waits for a human")

    assert queue.execute_ready()["executed"] == 1
    assert len(queue.pending_approvals()) == 1


def test_retry_returns_a_failed_action_without_reasking_approval(queue):
    calls = []

    def flaky(action):
        calls.append(1)
        if len(calls) == 1:
            raise RuntimeError("transient")
        return "sent"

    queue.register_executor("send_email", flaky)
    action = queue.submit("send_email", "Email the brief")
    queue.approve(action["action_id"], by="cfo")
    queue.execute(action["action_id"])
    queue.retry(action["action_id"])

    assert queue.execute(action["action_id"])["status"] == "executed"


# --------------------------------------------------------- trigger engine
def test_a_rule_fires_when_its_conditions_hold(store, bus, queue):
    triggers = TriggerEngine(store, bus, queue)
    fired = []
    triggers.register_handler("create_task",
                              lambda rule, event: fired.append(rule["name"]))
    triggers.add_rule("risk_up", "RiskIncreased", "create_task",
                      conditions=[{"field": "increase", "op": "gte",
                                   "value": 3}])
    bus.publish("RiskIncreased", {"increase": 5})

    assert fired == ["risk_up"]
    assert triggers.rules()[0]["fires"] == 1


def test_a_rule_stays_silent_when_its_conditions_fail(store, bus, queue):
    triggers = TriggerEngine(store, bus, queue)
    triggers.register_handler("create_task", lambda rule, event:
                              pytest.fail("the rule should not have fired"))
    triggers.add_rule("risk_up", "RiskIncreased", "create_task",
                      conditions=[{"field": "increase", "op": "gte",
                                   "value": 3}])
    bus.publish("RiskIncreased", {"increase": 1})


def test_conditions_read_dotted_paths(store, bus, queue):
    triggers = TriggerEngine(store, bus, queue)
    fired = []
    triggers.register_handler("notify", lambda rule, event: fired.append(1))
    triggers.add_rule("critical", "AnomalyDetected", "notify",
                      conditions=[{"field": "risk.severity", "op": "eq",
                                   "value": "critical"}])
    bus.publish("AnomalyDetected", {"risk": {"severity": "critical"}})

    assert fired == [1]


def test_a_missing_field_never_fires_a_threshold_rule(store, bus, queue):
    triggers = TriggerEngine(store, bus, queue)
    triggers.register_handler("create_task", lambda rule, event:
                              pytest.fail("fired on a missing field"))
    triggers.add_rule("drop", "PortfolioChanged", "create_task",
                      conditions=[{"field": "health_change", "op": "lte",
                                   "value": -5}])
    bus.publish("PortfolioChanged", {"average_health_score": 70})


def test_a_broken_rule_is_recorded_not_raised(store, bus, queue):
    triggers = TriggerEngine(store, bus, queue)

    def explode(rule, event):
        raise RuntimeError("handler is broken")

    triggers.register_handler("create_task", explode)
    triggers.add_rule("boom", "RiskIncreased", "create_task")
    bus.publish("RiskIncreased", {"increase": 9})  # must not raise

    assert "handler is broken" in triggers.rules()[0]["last_error"]


def test_unknown_events_and_operators_are_rejected(store, bus, queue):
    triggers = TriggerEngine(store, bus, queue)
    with pytest.raises(ValueError, match="Unknown event kind"):
        triggers.add_rule("x", "NotAnEvent", "create_task")
    with pytest.raises(ValueError, match="Unknown operator"):
        triggers.add_rule("x", "RiskIncreased", "create_task",
                          conditions=[{"field": "a", "op": "sql_injection"}])


def test_defaults_seed_once_and_respect_deletion(store, bus, queue):
    triggers = TriggerEngine(store, bus, queue)
    spec = [{"name": "only_once", "event": "RiskIncreased",
             "action": "create_task"}]

    assert triggers.ensure_defaults(spec) == 1
    assert triggers.ensure_defaults(spec) == 0, "a default was reinstalled"


# ------------------------------------------------------------ goal engine
def test_goal_progress_is_the_mean_of_kpi_attainment(store, bus):
    goals = GoalEngine(store, bus)
    goal = goals.create("Grow the North region", kpis=[
        {"name": "revenue", "target": 100.0, "baseline": 0.0,
         "metric": "portfolio.revenue"},
        {"name": "accounts", "target": 10.0, "baseline": 0.0,
         "metric": "portfolio.accounts"}])
    updated = goals.refresh(goal["goal_id"], {"portfolio.revenue": 50.0,
                                              "portfolio.accounts": 10.0})

    assert updated["kpis"][0]["attainment"] == 0.5
    assert updated["kpis"][1]["attainment"] == 1.0
    assert updated["progress"] == 0.75, "one KPI running ahead hid the other"


def test_a_goal_is_achieved_only_when_every_kpi_lands(store, bus):
    achieved = []
    bus.subscribe("GoalAchieved", lambda e: achieved.append(e.payload))
    goals = GoalEngine(store, bus)
    goal = goals.create("Ship it", kpis=[
        {"name": "a", "target": 10.0, "baseline": 0.0, "metric": "m.a"},
        {"name": "b", "target": 10.0, "baseline": 0.0, "metric": "m.b"}])

    goals.refresh(goal["goal_id"], {"m.a": 10.0, "m.b": 5.0})
    assert goals.get(goal["goal_id"])["status"] == "active"

    goals.refresh(goal["goal_id"], {"m.a": 10.0, "m.b": 10.0})
    assert goals.get(goal["goal_id"])["status"] == "achieved"
    assert len(achieved) == 1


def test_a_goal_near_its_deadline_and_behind_is_at_risk(store, bus):
    goals = GoalEngine(store, bus)
    goal = goals.create("Close the quarter", deadline=GoalEngine.default_deadline(3),
                        kpis=[{"name": "a", "target": 100.0, "baseline": 0.0,
                               "metric": "m.a"}])
    updated = goals.refresh(goal["goal_id"], {"m.a": 10.0})

    assert updated["status"] == "at_risk"


def test_a_goal_past_its_deadline_is_missed(store, bus):
    goals = GoalEngine(store, bus)
    goal = goals.create("Too late", deadline=GoalEngine.default_deadline(-1),
                        kpis=[{"name": "a", "target": 10.0, "metric": "m.a"}])
    goals.sweep_deadlines()

    assert goals.get(goal["goal_id"])["status"] == "missed"


def test_a_kpi_without_a_target_is_rejected(store, bus):
    with pytest.raises(ValueError, match="needs a target"):
        GoalEngine(store, bus).create("Vague", kpis=[{"name": "a"}])


# -------------------------------------------------------- planning engine
def test_creating_a_goal_plans_it_automatically(store, bus, queue):
    goals = GoalEngine(store, bus)
    planning = PlanningEngine(store, bus, goals, queue)
    goal = goals.create("Improve health", kpis=[
        {"name": "health", "target": 90.0,
         "metric": "portfolio.average_health_score"}])
    plan = planning.plan_for(goal["goal_id"])

    assert plan is not None, "GoalCreated did not produce a plan"
    assert plan["status"] == "active"
    assert any(s["kind"] == "measure" for s in plan["steps"])


def test_planning_is_idempotent(store, bus, queue):
    goals = GoalEngine(store, bus)
    planning = PlanningEngine(store, bus, goals, queue)
    goal = goals.create("Improve health",
                        kpis=[{"name": "h", "target": 90.0, "metric": "m.h"}])
    first = planning.plan_for_goal(goal["goal_id"])
    second = planning.plan_for_goal(goal["goal_id"])

    assert first["plan_id"] == second["plan_id"]


def test_advancing_a_plan_queues_its_action_steps(store, bus, queue):
    goals = GoalEngine(store, bus)
    planning = PlanningEngine(store, bus, goals, queue, workflows=_FakeWorkflows())
    goal = goals.create("Improve health",
                        kpis=[{"name": "h", "target": 90.0, "metric": "m.h"}])
    plan = planning.plan_for(goal["goal_id"])
    planning.advance(plan["plan_id"], limit=10)

    assert queue.actions(kind="create_task"), "no work reached the queue"


def test_replanning_keeps_completed_steps_and_supersedes_the_old_plan(
        store, bus, queue):
    goals = GoalEngine(store, bus)
    planning = PlanningEngine(store, bus, goals, queue, workflows=_FakeWorkflows())
    goal = goals.create("Improve health",
                        kpis=[{"name": "h", "target": 90.0, "metric": "m.h"}])
    plan = planning.plan_for(goal["goal_id"])
    planning.advance(plan["plan_id"], limit=1)
    successor = planning.replan(plan["plan_id"], "conditions changed")

    assert successor["revision"] == 2
    assert successor["supersedes"] == plan["plan_id"]
    assert any(s["status"] == "completed" for s in successor["steps"]), \
        "replanning discarded work already done"
    assert planning.plan_for(goal["goal_id"])["plan_id"] == successor["plan_id"]


def test_a_superseded_plan_is_never_resurrected_by_a_slow_advance(
        store, bus, queue):
    """The scheduler advances a plan while an API request replans the same
    goal: the replan wins. Without this, the advancing thread writes its
    stale copy back and the superseded plan returns from the dead."""
    goals = GoalEngine(store, bus)
    planning = PlanningEngine(store, bus, goals, queue, workflows=_FakeWorkflows())
    goal = goals.create("Improve health",
                        kpis=[{"name": "h", "target": 90.0, "metric": "m.h"}])
    plan = planning.plan_for(goal["goal_id"])
    stale = planning._plan(plan["plan_id"])  # what an in-flight advance holds

    planning.replan(plan["plan_id"], "conditions changed")
    stale["status"] = "completed"
    planning._save(stale)  # the slow advance finally writes back

    superseded = next(p for p in planning.plans(goal_id=goal["goal_id"])
                      if p["plan_id"] == plan["plan_id"])
    assert superseded["status"] == "superseded"
    assert len(planning.plans(status="active", goal_id=goal["goal_id"])) == 1


# -------------------------------------------------------- decision engine
@pytest.fixture()
def decisions(store, bus, queue, tmp_path):
    return DecisionEngine(store, bus, queue,
                          KnowledgeStore(tmp_path / "knowledge"))


def test_a_confident_routine_recommendation_is_autonomous(decisions):
    outcome = decisions.decide({"action": "Refresh the North dataset",
                                "confidence": 0.9, "priority": 5,
                                "evidence_ids": ["ev1", "ev2"]})

    assert outcome["requires_approval"] is False
    assert "autonomous" in outcome["approval_reason"]


def test_a_low_confidence_recommendation_escalates_to_a_human(decisions):
    outcome = decisions.decide({"action": "Rewrite the pricing model",
                                "confidence": 0.2, "priority": 5})

    assert outcome["requires_approval"] is True
    assert "below the autonomy threshold" in outcome["approval_reason"]


def test_an_external_action_always_escalates_however_confident(decisions):
    outcome = decisions.decide({"action": "Email the board", "confidence": 1.0,
                                "priority": 9}, action_kind="send_email")

    assert outcome["requires_approval"] is True
    assert "always requires approval" in outcome["approval_reason"]


def test_uncited_recommendations_are_trusted_less_than_cited_ones(decisions):
    uncited = decisions.decide({"action": "Do the uncited thing"})
    cited = decisions.decide({"action": "Do the cited thing",
                              "evidence_ids": ["e1", "e2", "e3", "e4", "e5"]})

    assert uncited["confidence"] < cited["confidence"]


def test_the_pipeline_records_every_stage(decisions):
    outcome = decisions.decide({"action": "Do the thing", "confidence": 0.9})
    stages = [s["stage"] for s in outcome["trace"]]

    assert stages == ["recommendation", "evidence", "confidence", "priority",
                      "approval", "execute"]


def test_executing_a_decisions_action_closes_and_learns(store, bus, queue,
                                                        tmp_path):
    knowledge = KnowledgeStore(tmp_path / "knowledge")
    engine = DecisionEngine(store, bus, queue, knowledge)
    queue.register_executor("create_task", lambda a: {"task_id": "t1"})
    outcome = engine.decide({"action": "Do the thing", "confidence": 0.9})
    queue.execute(outcome["queued_action_id"])

    closed = engine.decisions()[0]
    assert closed["status"] == "executed"
    assert [s["stage"] for s in closed["trace"]][-2:] == ["monitor", "learn"]
    assert knowledge.learning_history(10), "the outcome was never learned from"


def test_a_recommendation_without_an_action_is_rejected(decisions):
    with pytest.raises(ValueError, match="no action text"):
        decisions.decide({"expected_impact": "high"})


class _FakeWorkflows:
    """Stands in for the WorkflowEngine: planning must be testable without
    the analysis stack behind it."""

    def __init__(self):
        self.runs = []

    def run(self, name, project_id):
        self.runs.append((name, project_id))
        return {"run_id": "r1", "workflow": name, "status": "completed"}

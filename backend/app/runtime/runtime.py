"""Autonomy Runtime — the composition root of the autonomous execution layer.

This is where the heartbeat is assembled: the event bus, the scheduler and
its jobs, the trigger rules, the goal and planning engines, the decision
pipeline, and the action queue. Every piece is independently testable and
knows nothing about the others; the runtime is the only place that knows
they exist together.

Layering (top depends on bottom, never the reverse):

    Scheduler (jobs)  →  Workflows / Planning / Background Intelligence
    Trigger Engine    →  Action Queue  →  Executors
    Decision Engine   →  Action Queue
    Goal Engine       →  Planning Engine
    Event Bus (everything announces, nothing calls)

The runtime is built at container time but only *starts* when asked
(``start()``), so importing the app, running tests, or building the
container never spawns a thread or executes autonomous work.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.runtime.background import BackgroundIntelligence
from app.runtime.decisions import DecisionEngine
from app.runtime.events import Event, EventBus
from app.runtime.goals import GoalEngine
from app.runtime.planning import PlanningEngine
from app.runtime.queue import ActionQueue
from app.runtime.scheduler import EnterpriseScheduler, JobDefinition, RetryPolicy
from app.runtime.store import RuntimeStore
from app.runtime.triggers import TriggerEngine
from app.workflows.autonomous import (
    AutonomousContext, build_autonomous_workflows,
)

logger = get_logger(__name__)

# The SDS trigger rules, installed once on first start. They are ordinary
# rules after that: the operator may disable, delete, or add to them.
DEFAULT_TRIGGER_RULES = [
    {"name": "risk_increase_creates_task",
     "description": "If portfolio risk increases, generate a task",
     "event": "RiskIncreased", "action": "create_task",
     "conditions": [{"field": "increase", "op": "gte", "value": 1}],
     "params": {"title": "Investigate the increase in portfolio risk",
                "priority": 2}},
    {"name": "report_approved_generates_summary",
     "description": "If a report is approved, generate an executive summary",
     "event": "ReportApproved", "action": "generate_report",
     "conditions": [], "params": {"kind": "executive_summary"}},
    {"name": "new_dataset_refreshes_brain",
     "description": "If a new dataset arrives, refresh the Enterprise Brain",
     "event": "DatasetImported", "action": "refresh_knowledge",
     "conditions": [], "params": {}},
    {"name": "anomaly_creates_recommendation",
     "description": "If an anomaly is detected, generate a recommendation",
     "event": "AnomalyDetected", "action": "record_recommendation",
     "conditions": [], "params": {"priority": 2}},
    {"name": "low_confidence_creates_investigation",
     "description": "If prediction confidence drops, create an investigation "
                    "task",
     "event": "PredictionConfidenceDropped", "action": "create_task",
     "conditions": [{"field": "confidence", "op": "lt", "value": 0.5}],
     "params": {"title": "Investigate a drop in prediction confidence",
                "priority": 3}},
    {"name": "health_drop_creates_task",
     "description": "If portfolio health falls materially, generate a task",
     "event": "PortfolioChanged", "action": "create_task",
     "conditions": [{"field": "health_change", "op": "lte", "value": -5}],
     "params": {"title": "Review the decline in portfolio health",
                "priority": 1}},
    {"name": "goal_at_risk_notifies",
     "description": "If a goal falls at risk, notify the executive",
     "event": "GoalProgressed", "action": "notify",
     "conditions": [{"field": "status", "op": "eq", "value": "at_risk"}],
     "params": {"kind": "portfolio_change"}},
]


class AutonomyRuntime:
    """Observe → learn → plan → execute → monitor → improve, continuously."""

    def __init__(self, settings, store, knowledge, memory, manager, portfolio,
                 tasks, notifications, brief, workflows, orchestrator,
                 brain=None, sync=None, product=None, copilot=None,
                 providers=None, reasoning=None, connectors=None):
        self.settings = settings
        self.store = RuntimeStore(settings.data_dir / "runtime")
        self.bus = EventBus(self.store)
        self.workflows = workflows
        self.workflows.attach_bus(self.bus)
        # The Enterprise Knowledge Synchronization Layer announces on this bus
        # and schedules its refresh work on this scheduler. It is optional:
        # without it the platform still learns from analyses, it just does not
        # learn from connected systems.
        self.sync = sync
        # The Product Intelligence layer sits above the Brain and schedules
        # its recalculation here. Optional: without it the platform still
        # runs the enterprise, it just does not manage products.
        self.product = product
        # The Enterprise Copilot persists conversations and refreshes what it
        # knows about on this scheduler. Optional: without it the platform
        # runs exactly as before, it just has no conversational surface.
        self.copilot = copilot
        # The Enterprise Connector Framework (V2.1) synchronizes configured
        # enterprise data sources on this same scheduler and announces on this
        # same bus — it does not own a heartbeat. Optional: without it the
        # platform behaves exactly as V2 did.
        self.connectors = connectors

        self.queue = ActionQueue(
            self.store, self.bus,
            requires_approval=settings.autonomy_requires_approval)
        self.goals = GoalEngine(self.store, self.bus)
        self.planning = PlanningEngine(self.store, self.bus, self.goals,
                                       self.queue, workflows=self.workflows)
        self.decisions = DecisionEngine(
            self.store, self.bus, self.queue, knowledge,
            autonomy_threshold=settings.autonomy_confidence_threshold)
        self.triggers = TriggerEngine(self.store, self.bus, self.queue,
                                      workflows=self.workflows)
        self.background = BackgroundIntelligence(
            store=store, knowledge=knowledge, memory=memory,
            portfolio=portfolio, tasks=tasks, bus=self.bus, goals=self.goals,
            brain=brain)
        self.scheduler = EnterpriseScheduler(
            self.bus, self.store,
            tick_seconds=settings.autonomy_tick_seconds)

        self._manager = manager
        self._tasks = tasks
        self._notifications = notifications
        self._knowledge = knowledge
        # V2: external communication providers (Outlook, Teams, SharePoint)
        # and the reasoning engine the drafting workflows may use.
        self._providers = providers
        self._reasoning = reasoning
        self._started = False
        # An approved report is an enterprise event, not a workspace detail:
        # the Trigger Engine turns it into an executive summary.
        manager.reviews.bus = self.bus

        self._register_workflows(AutonomousContext(
            store=store, knowledge=knowledge, manager=manager,
            portfolio=portfolio, brief=brief, tasks=tasks,
            notifications=notifications, queue=self.queue, bus=self.bus,
            decisions=self.decisions, brain=brain, orchestrator=orchestrator))
        self._register_v2_workflows(store, knowledge, portfolio, tasks,
                                    notifications, brief)
        self._register_executors()
        self._register_trigger_handlers()
        self._register_jobs()
        if self.sync is not None:
            self.sync.attach_bus(self.bus)
            self.sync.register_jobs(self.scheduler, JobDefinition, RetryPolicy)
        if self.product is not None:
            self.product.attach_runtime(self.bus, decisions=self.decisions,
                                        queue=self.queue)
            self.product.register_jobs(self.scheduler, JobDefinition,
                                       RetryPolicy)
        if self.copilot is not None:
            self.copilot.attach_bus(self.bus)
            self.copilot.register_jobs(self.scheduler, JobDefinition,
                                       RetryPolicy)
        if self.connectors is not None:
            self.connectors.attach_bus(self.bus)
            self.connectors.register_jobs(self.scheduler, JobDefinition,
                                          RetryPolicy)

    # ------------------------------------------------------------ lifecycle
    def start(self) -> dict:
        """Install default rules and start the heartbeat. Idempotent."""
        if self._started:
            return self.status()
        installed = self.triggers.ensure_defaults(DEFAULT_TRIGGER_RULES)
        if installed:
            logger.info("Installed %d default trigger rules", installed)
        self.scheduler.start()
        self._started = True
        return self.status()

    def stop(self) -> None:
        self.scheduler.stop()
        self._started = False

    @property
    def running(self) -> bool:
        return self.scheduler.running

    # ------------------------------------------------------------ workflows
    def _register_workflows(self, context: AutonomousContext) -> None:
        for definition in build_autonomous_workflows(context):
            self.workflows.register(definition)

    def _register_v2_workflows(self, store, knowledge, portfolio, tasks,
                               notifications, brief) -> None:
        """The V2 Autonomous Workflow Library: document summarization and
        change detection, action-item extraction, and the drafting workflows.
        Registered only when Document Intelligence is available — they feed
        on its workfeed."""
        documents = getattr(self.sync, "documents", None) if self.sync else None
        if documents is None:
            return
        from app.workflows.library import V2Context, build_v2_workflows
        recipients = [r.strip() for r in
                      self.settings.v2_email_recipients.split(",")
                      if r.strip()]
        context = V2Context(
            documents=documents, knowledge=knowledge, tasks=tasks,
            notifications=notifications, queue=self.queue, brief=brief,
            portfolio=portfolio, reasoning=self._reasoning, store=store,
            default_recipients=recipients)
        for definition in build_v2_workflows(context):
            self.workflows.register(definition)

    # ------------------------------------------------------------ executors
    def _register_executors(self) -> None:
        """What the queue is allowed to actually do. Kinds with no executor
        (send_email, create_meeting, send_message) queue and wait — that is
        the V2 Communication Module's seam, and the approval trail for them
        already works today."""
        self.queue.register_executor("create_task", self._execute_create_task)
        self.queue.register_executor("run_workflow", self._execute_run_workflow)
        self.queue.register_executor("refresh_knowledge",
                                     self._execute_refresh_knowledge)
        self.queue.register_executor("record_recommendation",
                                     self._execute_record_recommendation)
        self.queue.register_executor("notify", self._execute_notify)
        self.queue.register_executor("generate_report",
                                     self._execute_generate_report)
        self.queue.register_executor("update_business_rule",
                                     self._execute_update_business_rule)
        self.queue.register_executor("execute_automation",
                                     self._execute_automation)
        self._register_communication_executors()

    def _register_communication_executors(self) -> None:
        """V2 Communication Layer: the queue learns to send through the
        configured adapters. An unconfigured channel registers nothing, so
        approved communications keep waiting visibly — exactly the V1
        contract — until an administrator sets the credential."""
        if self._providers is None:
            return
        try:
            email = self._providers.get("email")
            self.queue.register_executor(
                "send_email",
                lambda action: email.send_direct(
                    to=list((action.get("payload") or {}).get("to") or []),
                    subject=(action.get("payload") or {}).get("subject")
                    or action["title"],
                    body=(action.get("payload") or {}).get("body")
                    or action["detail"]))
            logger.info("Email executor registered (%s)", email.name)
        except Exception:  # noqa: BLE001 — unconfigured is normal, not an error
            logger.info("No email provider configured — approved emails "
                        "will wait in the queue")
        try:
            messaging = self._providers.get("messaging")
            self.queue.register_executor(
                "send_message",
                lambda action: messaging.post_message(
                    channel=(action.get("payload") or {}).get("channel", ""),
                    text=(action.get("payload") or {}).get("text")
                    or action["title"]))
            logger.info("Messaging executor registered (%s)", messaging.name)
        except Exception:  # noqa: BLE001
            logger.info("No messaging provider configured — approved "
                        "messages will wait in the queue")

    def _execute_create_task(self, action: dict) -> dict:
        task = self._tasks.create(
            action["title"], detail=action["detail"], status="pending",
            priority=action.get("priority"), source_kind="recommendation",
            source_ref=action["signature"],
            project_id=action.get("project_id", ""))
        return {"task_id": task["task_id"] if task else "",
                "created": task is not None}

    def _execute_run_workflow(self, action: dict) -> dict:
        payload = action.get("payload") or {}
        run = self.workflows.run(payload["workflow"],
                                 action.get("project_id", ""))
        return {"run_id": run["run_id"], "status": run["status"]}

    def _execute_refresh_knowledge(self, action: dict) -> dict:
        return self.background.refresh_knowledge()

    def _execute_record_recommendation(self, action: dict) -> dict:
        self._knowledge.record_recommendation(
            action["title"], priority=action.get("priority"),
            project_id=action.get("project_id", ""), source="enterprise_agent",
            evidence_ids=action.get("evidence_ids") or [])
        return {"recorded": True}

    def _execute_notify(self, action: dict) -> dict:
        payload = action.get("payload") or {}
        created = self._notifications.notify(
            payload.get("kind", "recommendation"), action["title"],
            detail=action["detail"], project_id=action.get("project_id", ""),
            ref=action["signature"])
        if created is not None:
            self.bus.publish("NotificationCreated",
                             {"kind": created["kind"],
                              "notification_id": created["notification_id"]},
                             project_id=action.get("project_id", ""),
                             source="queue.notify")
        return {"notified": created is not None}

    def _execute_generate_report(self, action: dict) -> dict:
        """Executive summaries are the Report Generation Module's work; the
        queue records the request as a task for now so the trail is intact
        when the summary generator lands."""
        task = self._tasks.create(
            action["title"], detail=action["detail"], status="pending",
            priority=action.get("priority", 3), source_kind="report",
            source_ref=action["signature"],
            project_id=action.get("project_id", ""))
        return {"task_id": task["task_id"] if task else "",
                "created": task is not None}

    def _execute_update_business_rule(self, action: dict) -> dict:
        payload = action.get("payload") or {}
        rule = payload.get("rule") or action["title"]
        self._knowledge.add_rule(rule, scope=payload.get("scope", "global"),
                                 source="enterprise_agent")
        return {"rule": rule[:120]}

    def _execute_automation(self, action: dict) -> dict:
        payload = action.get("payload") or {}
        workflow = payload.get("workflow")
        if not workflow:
            raise RuntimeError("execute_automation needs a workflow in payload")
        run = self.workflows.run(workflow, action.get("project_id", ""))
        return {"run_id": run["run_id"], "status": run["status"]}

    # ----------------------------------------------------- trigger handlers
    def _register_trigger_handlers(self) -> None:
        """Trigger actions are names, resolved here to platform work. Every
        one queues an action — a rule can never bypass the approval layer."""
        for kind in ("create_task", "refresh_knowledge",
                     "record_recommendation", "notify", "generate_report",
                     "run_workflow", "execute_automation"):
            self.triggers.register_handler(kind, self._handler_for(kind))

    def _handler_for(self, kind: str):
        def handler(rule: dict, event: Event) -> Any:
            params = rule.get("params") or {}
            title = params.get("title") or self._title_for(kind, rule, event)
            return self.queue.submit(
                kind, title,
                payload={**params, "event": event.describe(),
                         "rule": rule["name"]},
                detail=f"Triggered by rule '{rule['name']}' on {event.kind}",
                priority=params.get("priority", 4),
                project_id=event.project_id, source=f"trigger:{rule['name']}",
                source_ref=f"{rule['rule_id']}:{event.kind}:"
                           f"{event.project_id}:{_signature(event)}")
        return handler

    def _title_for(self, kind: str, rule: dict, event: Event) -> str:
        detail = (event.payload.get("detail")
                  or event.payload.get("insight")
                  or event.payload.get("objective") or event.kind)
        return f"{rule['name'].replace('_', ' ').capitalize()}: {detail}"[:200]

    # ----------------------------------------------------------------- jobs
    def _register_jobs(self) -> None:
        """The heartbeat. Startup jobs run once in dependency order; interval
        and cron jobs carry the day; event jobs react."""
        settings = self.settings
        retry = RetryPolicy(attempts=2, backoff_seconds=2.0)

        self.scheduler.register(JobDefinition(
            "startup_portfolio", "Snapshot portfolio health at startup",
            "startup", self.background.refresh_portfolio, retry=retry,
            tags=["startup", "portfolio"]))
        self.scheduler.register(JobDefinition(
            "startup_knowledge", "Verify Brain knowledge surfaces at startup",
            "startup", self.background.refresh_knowledge,
            depends_on=["startup_portfolio"], retry=retry,
            tags=["startup", "knowledge"]))
        self.scheduler.register(JobDefinition(
            "startup_goals", "Measure every active goal at startup",
            "startup", self.background.refresh_goals,
            depends_on=["startup_portfolio"], retry=retry,
            tags=["startup", "goals"]))

        self.scheduler.register(JobDefinition(
            "action_queue", "Drain the enterprise action queue",
            "interval", self.queue.execute_ready,
            interval_seconds=settings.autonomy_queue_interval_seconds,
            retry=RetryPolicy(attempts=1), tags=["queue", "core"]))
        self.scheduler.register(JobDefinition(
            "background_portfolio", "Refresh portfolio health",
            "interval", self.background.refresh_portfolio,
            interval_seconds=settings.autonomy_refresh_interval_seconds,
            retry=retry, tags=["background", "portfolio"]))
        self.scheduler.register(JobDefinition(
            "background_risks", "Refresh portfolio risks",
            "interval", self.background.refresh_risks,
            interval_seconds=settings.autonomy_refresh_interval_seconds,
            depends_on=["background_portfolio"], retry=retry,
            tags=["background", "risks"]))
        self.scheduler.register(JobDefinition(
            "background_opportunities", "Refresh growth opportunities",
            "interval", self.background.refresh_opportunities,
            interval_seconds=settings.autonomy_refresh_interval_seconds,
            depends_on=["background_portfolio"], retry=retry,
            tags=["background", "opportunities"]))
        self.scheduler.register(JobDefinition(
            "background_predictions", "Check forecast confidence",
            "interval", self.background.refresh_predictions,
            interval_seconds=settings.autonomy_refresh_interval_seconds,
            retry=retry, tags=["background", "predictions"]))
        self.scheduler.register(JobDefinition(
            "background_recommendations", "Surface unactioned recommendations",
            "interval", self.background.refresh_recommendations,
            interval_seconds=settings.autonomy_refresh_interval_seconds,
            retry=retry, tags=["background", "recommendations"]))
        self.scheduler.register(JobDefinition(
            "background_memory", "Keep memory and knowledge aligned",
            "interval", self.background.refresh_memory,
            interval_seconds=settings.autonomy_refresh_interval_seconds * 2,
            retry=retry, tags=["background", "memory"]))
        self.scheduler.register(JobDefinition(
            "anomaly_sweep", "Detect portfolio anomalies",
            "interval", self.background.detect_anomalies,
            interval_seconds=settings.autonomy_refresh_interval_seconds,
            depends_on=["background_portfolio"], retry=retry,
            tags=["background", "anomalies"]))
        self.scheduler.register(JobDefinition(
            "goal_refresh", "Measure goals and sweep deadlines",
            "interval", self.background.refresh_goals,
            interval_seconds=settings.autonomy_refresh_interval_seconds,
            depends_on=["background_portfolio"], retry=retry,
            tags=["goals"]))
        self.scheduler.register(JobDefinition(
            "plan_advance", "Advance every active plan",
            "interval", self.planning.advance_all,
            interval_seconds=settings.autonomy_planning_interval_seconds,
            depends_on=["goal_refresh"], retry=RetryPolicy(attempts=1),
            tags=["planning"]))
        self.scheduler.register(JobDefinition(
            "plan_replan", "Revise plans whose conditions changed",
            "interval", self.planning.replan_sweep,
            interval_seconds=settings.autonomy_planning_interval_seconds * 4,
            depends_on=["goal_refresh"], retry=RetryPolicy(attempts=1),
            tags=["planning"]))

        self.scheduler.register(JobDefinition(
            "daily_cycle", "The autonomous enterprise cycle",
            "cron", lambda: self.workflows.run("daily_cycle", ""),
            cron=settings.autonomy_daily_cycle_cron,
            retry=RetryPolicy(attempts=2, backoff_seconds=60.0),
            tags=["autonomous", "daily"]))
        self.scheduler.register(JobDefinition(
            "monitoring", "Continuous monitoring and alerting",
            "cron", lambda: self.workflows.run("monitoring", ""),
            cron=settings.autonomy_monitoring_cron, retry=retry,
            tags=["autonomous", "monitoring"]))

        # ------------------------------------------- V2 workflow library
        # Document workflows react to document change events; drafting
        # workflows run on their crons. Registered only when the workflows
        # themselves were (Document Intelligence available).
        if self.workflows.definition("rca_summarization") is not None:
            self.scheduler.register(JobDefinition(
                "document_workflows",
                "Summarize and act on new or changed documents",
                "event", self._run_document_workflows,
                event="DocumentsUpdated", retry=RetryPolicy(attempts=1),
                tags=["v2", "documents", "event"]))
            self.scheduler.register(JobDefinition(
                "document_workflows_sweep",
                "Catch up on unprocessed documents",
                "interval", self._run_document_workflows,
                interval_seconds=settings.autonomy_refresh_interval_seconds * 4,
                retry=RetryPolicy(attempts=1), tags=["v2", "documents"]))
            self.scheduler.register(JobDefinition(
                "email_drafting", "Draft the daily status email for approval",
                "cron", lambda: self.workflows.run("email_drafting", ""),
                cron=settings.v2_email_draft_cron, retry=retry,
                tags=["v2", "drafting", "daily"]))
            self.scheduler.register(JobDefinition(
                "teams_drafting", "Draft the daily Teams update for approval",
                "cron", lambda: self.workflows.run("teams_message_drafting", ""),
                cron=settings.v2_teams_update_cron, retry=retry,
                tags=["v2", "drafting", "daily"]))
            self.scheduler.register(JobDefinition(
                "presentation_drafting",
                "Draft the weekly portfolio presentation outline",
                "cron", lambda: self.workflows.run("presentation_drafting", ""),
                cron=settings.v2_presentation_cron, retry=retry,
                tags=["v2", "drafting", "weekly"]))

        self.scheduler.register(JobDefinition(
            "learn_on_import", "Refresh the Enterprise Brain when data lands",
            "event", self.background.refresh_knowledge,
            event="DatasetImported", retry=retry,
            tags=["event", "knowledge"]))
        self.scheduler.register(JobDefinition(
            "measure_on_report", "Re-measure goals when a report is generated",
            "event", self.background.refresh_goals, event="ReportGenerated",
            retry=retry, tags=["event", "goals"]))

    def _run_document_workflows(self) -> dict:
        """Run every document workflow once; each consumes only its own
        unprocessed workfeed, so a run with nothing new costs nothing."""
        outcomes = {}
        for name in ("rca_summarization", "sop_change_detection",
                     "meeting_summarization", "action_item_extraction"):
            run = self.workflows.run(name, "")
            outcomes[name] = run.get("status", "")
        return outcomes

    # --------------------------------------------------------------- status
    def status(self) -> dict:
        return {
            "running": self.running,
            "autonomy": "active" if self.running else "stopped",
            "scheduler": self.scheduler.status(),
            "events": self.bus.stats(),
            "queue": self.queue.stats(),
            "triggers": self.triggers.stats(),
            "goals": self.goals.progress_report(),
            "plans": self.planning.stats(),
            "decisions": self.decisions.stats(),
            "approval_policy": self.queue.policy(),
            "synchronization": (self.sync.status() if self.sync is not None
                                else {"enabled": False}),
            "product_intelligence": (self.product.status()
                                     if self.product is not None
                                     else {"enabled": False}),
            "copilot": (self.copilot.status() if self.copilot is not None
                        else {"enabled": False}),
            "connectors": (self.connectors.status()
                           if self.connectors is not None
                           else {"enabled": False}),
        }

    def activity(self, limit: int = 20) -> dict:
        """Autonomous Activities: what the agent did while nobody watched."""
        return {
            "running_workflows": self.workflows.running(limit),
            "recent_runs": self.workflows.recent_runs(limit),
            "recent_actions": self.queue.recent(limit),
            "recent_events": self.bus.history(limit),
            "recent_executions": self.scheduler.executions(limit),
            "pending_approvals": self.queue.pending_approvals(limit),
        }


def _signature(event: Event) -> str:
    """A stable dedupe key for a triggered action: the same condition on the
    same day must not queue the same action twice."""
    payload = event.payload
    for key in ("project_id", "goal_id", "metric", "kind", "workflow"):
        if payload.get(key):
            return str(payload[key])[:40].lower()
    return event.created_at[:10]  # fall back to the day

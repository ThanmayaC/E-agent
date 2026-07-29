"""Manager Workspace — the executive's single surface over the platform.

Composes every executive service (tasks, decisions, reviews, portfolio,
brief, notifications) plus the Enterprise Brain's business-level outputs
into the workspace and dashboard payloads. Strictly presentational
composition: no analytics, no LLM calls, no technical internals exposed —
executives see business health, never knowledge graphs or prompt engines.

``refresh_after_analysis`` is the runtime hook: after every successful
analysis (and the Brain's learning pass) it registers the report for
review, generates tasks and notifications, and refreshes the daily brief.
"""
from __future__ import annotations

from typing import Any

from app.communication.notifications import NotificationCenter
from app.core.logging import get_logger
from app.knowledge.store import KnowledgeStore
from app.manager.briefing import DailyBriefGenerator
from app.manager.decisions import DecisionCenter
from app.manager.portfolio import PortfolioWorkspace
from app.manager.reviews import ReportReviewCenter
from app.manager.tasks import ExecutiveTaskManager
from app.repositories.artifact_store import ArtifactStore

logger = get_logger(__name__)

PORTFOLIO_CHANGE_THRESHOLD = 5.0  # health-score points that count as a change


class ManagerWorkspace:
    def __init__(self, store: ArtifactStore, knowledge: KnowledgeStore,
                 tasks: ExecutiveTaskManager, decisions: DecisionCenter,
                 reviews: ReportReviewCenter,
                 notifications: NotificationCenter,
                 portfolio: PortfolioWorkspace, brief: DailyBriefGenerator,
                 brain=None):
        self.store = store
        self.knowledge = knowledge
        self.tasks = tasks
        self.decisions = decisions
        self.reviews = reviews
        self.notifications = notifications
        self.portfolio = portfolio
        self.brief = brief
        self.brain = brain
        self.workflow_engine = None  # assigned by the container after build
        self.runtime = None          # AutonomyRuntime, assigned by container
        self.sync = None             # SynchronizationLayer, ditto
        self.product = None          # ProductIntelligenceLayer, ditto
        self.executive = None        # ExecutiveIntelligence (V3.1), ditto

    # ------------------------------------------------------------ approvals
    def pending_approvals(self) -> list[dict]:
        """Everything waiting on an executive: clarification pauses and
        reports in review."""
        out = []
        for pid in self.store.list_projects():
            state = self.store.load(pid, "state") or {}
            if state.get("status") == "awaiting_clarification":
                understanding = self.store.load(pid, "understanding", {}) or {}
                open_qs = [q for q in understanding.get("questions", [])
                           if not q.get("answered")]
                out.append({
                    "kind": "clarification", "project_id": pid,
                    "ref": f"clarify:{pid}",
                    "title": f"Answer {len(open_qs) or 'the'} clarification "
                             f"question(s) for {state.get('name', pid)}",
                    "detail": (open_qs[0].get("question", "")[:200]
                               if open_qs else "")})
        for review in self.reviews.pending():
            out.append({"kind": "report_review",
                        "project_id": review["project_id"],
                        "ref": f"review:{review['review_id']}",
                        "title": f"Review report: {review['title']}",
                        "detail": f"status {review['status']}"})
        # Autonomous actions the agent decided on but may not take alone.
        if self.runtime is not None:
            for action in self.runtime.queue.pending_approvals():
                out.append({"kind": "action_approval",
                            "project_id": action["project_id"],
                            "ref": f"action:{action['action_id']}",
                            "title": f"Approve: {action['title']}",
                            "detail": action["detail"][:200]})
        return out

    # ------------------------------------------------------------ workspace
    def workspace(self) -> dict[str, Any]:
        """The Manager Workspace payload — every executive panel at once."""
        brief = self.brief.today()
        overview = self.portfolio.overview()
        approvals = self.pending_approvals()
        payload = {
            "todays_summary": {
                "date": brief["date"],
                "portfolio_health": brief["portfolio_health"],
                "high_priority_issues": brief["high_priority_issues"],
                "open_action_items": len(self.tasks.open_tasks(500)),
                "unread_notifications": self.notifications.unread_count(),
            },
            "pending_reviews": self.reviews.pending(),
            "critical_risks": brief["business_risks"],
            "growth_opportunities": brief["growth_opportunities"],
            "portfolio_health": overview["portfolio_health"],
            "pending_tasks": self.tasks.open_tasks(10),
            "pending_approvals": approvals,
            "recent_reports":
                overview["business_performance"]["recent_reports"],
            "recent_decisions": self.decisions.decisions(limit=5),
            "upcoming_meetings": [],  # calendar/meeting providers arrive in V2
            "suggested_actions": self.tasks.tasks(status="suggested",
                                                  limit=8),
            "recent_notifications": self.notifications.recent(10),
            "autonomy": self.autonomy(),
            "organization": self.organization(),
            "products": self.products(),
        }
        self._overlay_executive(payload)
        return payload

    def _overlay_executive(self, payload: dict[str, Any]) -> None:
        """V3.1: when the platform runs the ingested synthetic enterprise (no
        analysis projects), fill the executive panels from the Executive
        Intelligence layer so the dashboard shows real enterprise
        intelligence instead of empty placeholders. Only empty panels are
        filled — real project data always wins."""
        ei = self.executive
        if ei is None or not getattr(ei, "available", False):
            return
        try:
            brief = ei.executive_brief()
        except Exception:  # noqa: BLE001 — the workspace never breaks on overlay
            return
        health = brief.get("health", {})
        if payload["portfolio_health"].get("average_health_score") is None:
            payload["portfolio_health"]["average_health_score"] = \
                health.get("portfolio")
            payload["todays_summary"]["portfolio_health"] = health.get(
                "portfolio")
        if not payload["critical_risks"]:
            payload["critical_risks"] = [
                {"insight": f"{r['risk']} — {r['detail']}",
                 "severity": r.get("severity", "high"), "project_id": ""}
                for r in brief.get("risk_assessment", {}).get("top_risks", [])]
        if not payload["recent_reports"]:
            payload["recent_reports"] = [
                {"title": e["title"], "project_id": e.get("decision_id", ""),
                 "health_score": None}
                for e in brief.get("major_decisions", [])]
        if not payload["recent_decisions"]:
            payload["recent_decisions"] = [
                {"decision": d["title"], "context": d["business_value"],
                 "status": d["status"]}
                for d in ei.decisions()[:5]]
        if not payload["suggested_actions"]:
            payload["suggested_actions"] = [
                {"task_id": f"rec-{i}", "title": r["title"],
                 "detail": r["reason"], "status": "suggested",
                 "priority": 1 if r["priority"] == "high" else 3}
                for i, r in enumerate(brief.get("recommended_actions", []))]
        if not payload["growth_opportunities"]:
            payload["growth_opportunities"] = [
                {"insight": r["expected_benefit"], "project_id": ""}
                for r in brief.get("recommended_actions", [])[:3]]
        # Products at risk (the Executive Dashboard also reads /manager/products).
        payload["products"] = payload.get("products") or {}
        if isinstance(payload["products"], dict):
            payload["products"].setdefault("products", [])
            if not payload["products"]["products"]:
                payload["products"]["products"] = [
                    {"name": p["product"], "health_score": p["health"],
                     "status": p["status"], "owner": p.get("owner", ""),
                     "recommendation": p.get("note", "")}
                    for p in health.get("products", [])]
        # Carry the full executive brief for premium consumers.
        payload["executive"] = brief

    # ---------------------------------------------------- overnight (V2)
    def overnight_summary(self, hours: int = 16) -> dict[str, Any]:
        """What the platform did while nobody watched — the V2 landing
        panel. Pure composition over surfaces that already exist: workflow
        runs, executed and queued actions, notifications, and reports since
        the cutoff."""
        from datetime import datetime, timedelta, timezone
        cutoff = (datetime.now(timezone.utc)
                  - timedelta(hours=hours)).isoformat()

        def since(items: list[dict], key: str) -> list[dict]:
            return [i for i in items if str(i.get(key, "")) >= cutoff]

        runs = (self.workflow_engine.recent_runs(50)
                if self.workflow_engine is not None else [])
        runs = since(runs, "finished_at")
        actions_executed: list[dict] = []
        drafts_awaiting: list[dict] = []
        if self.runtime is not None:
            actions_executed = since(
                self.runtime.queue.actions(status="executed", limit=100),
                "executed_at")
            drafts_awaiting = self.runtime.queue.pending_approvals(20)
        notifications = since(self.notifications.recent(50), "created_at")
        reports = since(self.knowledge.report_history(30), "generated_at")

        return {
            "since": cutoff, "hours": hours,
            "workflows_completed": [
                {"workflow": r.get("workflow", ""),
                 "status": r.get("status", ""),
                 "finished_at": r.get("finished_at", "")}
                for r in runs if r.get("status") != "running"][:10],
            "actions_executed": [
                {"title": a["title"], "kind": a["kind"],
                 "executed_at": a.get("executed_at", "")}
                for a in actions_executed][:10],
            "awaiting_approval": [
                {"action_id": a["action_id"], "title": a["title"],
                 "kind": a["kind"], "detail": a.get("detail", ""),
                 "payload": a.get("payload") or {},
                 "created_at": a.get("created_at", "")}
                for a in drafts_awaiting][:10],
            "new_reports": [
                {"project_id": r.get("project_id", ""),
                 "title": r.get("title", ""),
                 "health_score": r.get("health_score")}
                for r in reports][:8],
            "new_notifications": [
                {"kind": n["kind"], "title": n["title"],
                 "created_at": n["created_at"]}
                for n in notifications][:10],
            "totals": {
                "workflows": len(runs),
                "actions_executed": len(actions_executed),
                "awaiting_approval": len(drafts_awaiting),
                "notifications": len(notifications),
                "reports": len(reports),
            },
        }

    # ------------------------------------------------------------- products
    def products(self, limit: int = 5) -> dict[str, Any]:
        """The Enterprise Product Manager's view, in business terms: how the
        portfolio stands, which products need attention, what growth is open,
        and what strategy is recommended.

        Empty and inactive without the product layer — the executive panels
        never depend on it being wired.
        """
        if self.product is None:
            return {"status": "inactive", "products": {"total": 0},
                    "portfolio_health": {"score": None, "band": "unknown"},
                    "attention": [], "top_opportunities": [], "top_risks": [],
                    "open_recommendations": [], "kpi_alerts": []}
        overview = self.product.overview()
        return {"status": "active", **overview,
                "top_products": overview["top_products"][:limit],
                "attention": overview["attention"][:limit]}

    def product_reviews(self, limit: int = 5) -> list[dict]:
        """Executive Reviews: the latest product review per product."""
        if self.product is None:
            return []
        return [{"product": r["product"], "product_id": r["product_id"],
                 "health_score": r.get("health_score"),
                 "summary": r["executive_summary"],
                 "risks": len([x for x in r["risks"]
                               if x["severity"] != "none"]),
                 "actions": len(r["action_items"]),
                 "generated_at": r["generated_at"]}
                for r in self.product.reviews.reviews(limit=limit)]

    # --------------------------------------------------------- organization
    def organization(self, limit: int = 8) -> dict[str, Any]:
        """What the platform knows about the organization, in business terms:
        how big it is, what is connected, how current it is, and what changed.

        Empty and inactive when the synchronization layer is absent — the
        executive panels never depend on it being wired.
        """
        if self.sync is None:
            return {"status": "inactive", "entities_total": 0, "by_kind": {},
                    "connected_systems": {"total": 0, "connected": 0,
                                          "systems": []},
                    "knowledge_freshness": {"status": "unknown",
                                            "last_updated_at": ""},
                    "recent_synchronizations": [], "recently_discovered": []}
        overview = self.sync.overview()
        return {"status": "active", **overview,
                "recent_synchronizations":
                    overview["recent_synchronizations"][:limit],
                "recently_discovered": overview["recently_discovered"][:limit]}

    def search(self, query: str, limit: int = 20) -> dict[str, Any]:
        """Executive search — one question across everything the organization
        knows. The Enterprise Search owns the searching; the workspace only
        asks."""
        if self.sync is None:
            return {"query": query, "results": [], "total": 0,
                    "note": "enterprise search is unavailable"}
        return self.sync.search.search(query, limit=limit)

    # ------------------------------------------------------------- autonomy
    def autonomy(self, limit: int = 8) -> dict[str, Any]:
        """What Enterprise Agent is doing by itself, in business terms.

        Empty and inactive when the runtime is absent (autonomy disabled, or
        a workspace built without it) — the executive panels never depend on
        the heartbeat being up.
        """
        if self.runtime is None:
            return {"status": "inactive", "running_workflows": [],
                    "scheduled_jobs": [], "pending_approvals": [],
                    "recent_actions": [], "activities": [],
                    "goal_progress": {"total": 0, "active": 0, "goals": []}}
        status = self.runtime.status()
        return {
            "status": status["autonomy"],
            "running_workflows": [
                {"workflow": r["workflow"], "project_id": r["project_id"],
                 "started_at": r["started_at"],
                 "steps": len(r.get("steps") or [])}
                for r in self.runtime.workflows.running(limit)],
            "scheduled_jobs": [
                {"name": j["name"], "description": j["description"],
                 "kind": j["kind"], "next_run_at": j["next_run_at"],
                 "last_run_at": j["last_run_at"], "status": j["status"],
                 "enabled": j["enabled"]}
                for j in self.runtime.scheduler.describe()
                if j["enabled"]][:limit * 2],
            "pending_approvals": [
                {"action_id": a["action_id"], "title": a["title"],
                 "kind": a["kind"], "detail": a["detail"],
                 "priority": a["priority"], "confidence": a["confidence"],
                 "created_at": a["created_at"]}
                for a in self.runtime.queue.pending_approvals(limit)],
            "recent_actions": [
                {"action_id": a["action_id"], "title": a["title"],
                 "kind": a["kind"], "status": a["status"],
                 "updated_at": a["updated_at"]}
                for a in self.runtime.queue.recent(limit)],
            "activities": self._activities(limit),
            "goal_progress": status["goals"],
            "summary": {
                "jobs_running": status["scheduler"]["jobs_enabled"],
                "actions_pending_approval": status["queue"]["pending_approval"],
                "actions_in_flight": status["queue"]["in_flight"],
                "decisions_autonomous": status["decisions"]["autonomous"],
                "goals_at_risk": status["goals"]["at_risk"],
                "plans_active": status["plans"]["active"],
            },
        }

    def _activities(self, limit: int) -> list[dict]:
        """Autonomous Activities: the agent's recent work as a plain
        business-readable feed — no jobs, events, or queue mechanics."""
        feed = []
        for run in self.runtime.workflows.recent_runs(limit):
            feed.append({"at": run["started_at"], "kind": "workflow",
                         "title": f"Ran the {run['workflow'].replace('_', ' ')} "
                                  f"workflow", "status": run["status"]})
        for action in self.runtime.queue.recent(limit):
            if action["status"] in ("executed", "failed"):
                feed.append({"at": action["updated_at"], "kind": "action",
                             "title": action["title"],
                             "status": action["status"]})
        return sorted(feed, key=lambda a: a["at"], reverse=True)[:limit]

    # ------------------------------------------------------------ dashboard
    def dashboard(self) -> dict[str, Any]:
        """Business views only — no technical implementation exposed."""
        overview = self.portfolio.overview()
        projects = overview["projects"]
        automations = []
        if self.workflow_engine is not None:
            automations = [{"name": w["name"],
                            "description": w["description"],
                            "active": w["available"]}
                           for w in self.workflow_engine.describe()]
        learning = self.knowledge.learning_history(1)
        return {
            "business_health": {
                **overview["portfolio_health"],
                "top_changes": overview["historical_comparison"][:5],
            },
            "operational_status": {
                "analyses_ready": sum(1 for p in projects
                                      if p["status"] == "ready"),
                "analyses_running": sum(1 for p in projects
                                        if p["status"] == "analyzing"),
                "awaiting_input": sum(
                    1 for p in projects
                    if p["status"] == "awaiting_clarification"),
                "failed": sum(1 for p in projects
                              if p["status"] == "failed"),
                "continuous_learning": ("active" if self.brain is not None
                                        and getattr(self.brain, "state", "")
                                        == "ready" else "inactive"),
                "last_learned_at": (learning[-1]["recorded_at"]
                                    if learning else None),
            },
            "portfolio_summary": {
                "projects": projects[:10],
                "risks": overview["risks"][:5],
                "opportunities": overview["opportunities"][:5],
            },
            "organization_summary": self._organization_summary(),
            "product_summary": self._product_summary(),
            "recommended_actions": self.tasks.open_tasks(8),
            "automation_status": {
                "automations": automations,
                "notifications": self.notifications.stats(),
                **self._autonomy_status(),
            },
        }

    def _organization_summary(self) -> dict[str, Any]:
        """The dashboard's organization strip: how much of the enterprise the
        platform models, and whether that model is current."""
        if self.sync is None:
            return {"status": "inactive"}
        overview = self.sync.overview()
        systems = overview["connected_systems"]
        return {
            "status": "active",
            "business_entities": overview["entities_total"],
            "by_kind": overview["by_kind"],
            "connected_systems": systems["connected"],
            "systems_needing_attention": systems["needs_attention"],
            "knowledge_freshness": overview["knowledge_freshness"]["status"],
            "last_updated_at": overview["knowledge_freshness"][
                "last_updated_at"],
        }

    def _product_summary(self) -> dict[str, Any]:
        """The dashboard's product strip: the portfolio position and what the
        product manager would raise first."""
        if self.product is None:
            return {"status": "inactive"}
        overview = self.product.overview()
        return {
            "status": "active",
            "products": overview["products"]["total"],
            "measured": overview["products"]["measured"],
            "portfolio_health": overview["portfolio_health"]["score"],
            "portfolio_band": overview["portfolio_health"]["band"],
            "growth_band": overview["portfolio_growth"]["band"],
            "risk_band": overview["portfolio_risk"]["band"],
            "needs_attention": len(overview["attention"]),
            "open_recommendations": len(overview["open_recommendations"]),
        }

    def _autonomy_status(self) -> dict[str, Any]:
        """The dashboard's autonomy strip: is the agent working by itself,
        and what is waiting on the executive."""
        if self.runtime is None:
            return {"autonomy": "inactive"}
        status = self.runtime.status()
        return {
            "autonomy": status["autonomy"],
            "jobs_scheduled": status["scheduler"]["jobs_enabled"],
            "jobs_degraded": len(status["scheduler"]["degraded_jobs"]),
            "workflows_running": len(self.runtime.workflows.running(20)),
            "actions_pending_approval": status["queue"]["pending_approval"],
            "goals_active": status["goals"]["active"],
            "goals_at_risk": status["goals"]["at_risk"],
            "goal_progress_average": status["goals"]["average_progress"],
        }

    # -------------------------------------------------------------- runtime
    def refresh_after_analysis(self, project_id: str) -> dict[str, int]:
        """Runtime hook: keep the executive workspace current after every
        successful analysis. Idempotent — re-running adds nothing."""
        state = self.store.load(project_id, "state") or {}
        name = state.get("name", project_id)
        version = int(state.get("report_version") or 0)
        context = self.store.load(project_id, "business_context", {}) or {}
        health = (context.get("executive_metrics") or {}).get("health_score")
        ai = self.store.load(project_id, "ai_report", {}) or {}
        report = self.store.load(project_id, "report", {}) or {}

        # report review + new-report notification
        self.reviews.register(project_id, version,
                              f"{name} — report v{version}", health)
        # tasks from priority actions + recommendations
        created_tasks = self.tasks.generate_from_report(
            project_id, version, ai,
            report.get("deterministic_recommendations") or [])
        created_tasks += self.tasks.generate_from_approvals(
            [a for a in self.pending_approvals()
             if a["kind"] == "clarification"])

        notified = 0
        if ai.get("status") == "ok":
            for r in (ai.get("risks") or [])[:5]:
                if isinstance(r, dict) and \
                        r.get("severity") in ("high", "critical"):
                    if self.notifications.notify(
                            "critical_risk",
                            f"{r['severity'].title()} risk — {name}",
                            detail=str(r.get("risk", ""))[:300],
                            project_id=project_id,
                            ref=f"{project_id}:v{version}:"
                                f"{str(r.get('risk',''))[:50].lower()}"):
                        notified += 1
            top_rec = next((x for x in ai.get("recommendations") or []
                            if isinstance(x, dict) and x.get("action")), None)
            if top_rec and self.notifications.notify(
                    "recommendation", f"New recommendation — {name}",
                    detail=str(top_rec["action"])[:300],
                    project_id=project_id,
                    ref=f"{project_id}:v{version}:top_rec"):
                notified += 1

        # portfolio change: health moved materially vs the previous report
        history = [h for h in self.knowledge.report_history(100)
                   if h["project_id"] == project_id
                   and h.get("health_score") is not None]
        if len(history) >= 2 and health is not None:
            change = round(health - history[-2]["health_score"], 1)
            if abs(change) >= PORTFOLIO_CHANGE_THRESHOLD:
                direction = "improved" if change > 0 else "declined"
                if self.notifications.notify(
                        "portfolio_change",
                        f"{name} health {direction} by {abs(change):.0f} pts",
                        project_id=project_id,
                        ref=f"{project_id}:v{version}:health_change"):
                    notified += 1

        # deadline notifications + brief refresh
        for t in self.tasks.due_soon(3):
            if self.notifications.notify(
                    "task_deadline", f"Task due soon: {t['title']}",
                    project_id=t.get("project_id", ""),
                    ref=f"deadline:{t['task_id']}"):
                notified += 1
        self.brief.generate()
        return {"tasks_created": created_tasks, "notifications": notified}

    def notify_workflow_failure(self, workflow: str, project_id: str,
                                error: str) -> None:
        state = self.store.load(project_id, "state") or {}
        self.notifications.notify(
            "workflow_failure",
            f"Workflow '{workflow}' failed — {state.get('name', project_id)}",
            detail=error[:300], project_id=project_id,
            ref=f"{project_id}:{workflow}:{error[:40].lower()}")

    def startup_refresh(self) -> None:
        """Runtime startup: today's brief exists, deadlines are notified."""
        try:
            self.brief.today()
            for t in self.tasks.due_soon(3):
                self.notifications.notify(
                    "task_deadline", f"Task due soon: {t['title']}",
                    project_id=t.get("project_id", ""),
                    ref=f"deadline:{t['task_id']}")
        except Exception:  # noqa: BLE001 — workspace refresh must never block boot
            logger.exception("Executive workspace startup refresh failed")

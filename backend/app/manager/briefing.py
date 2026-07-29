"""Executive Daily Brief.

Generated automatically from the Enterprise Brain — deterministic
composition of what the platform already verified: high-priority issues,
portfolio changes, important reports, open action items, deadlines, risks,
opportunities, and recommendations. One brief per calendar day, regenerated
when the underlying state changes (new analysis, startup refresh).
"""
from __future__ import annotations

from datetime import datetime, timezone

from app.communication.notifications import NotificationCenter
from app.knowledge.store import KnowledgeStore
from app.manager.portfolio import PortfolioWorkspace
from app.manager.store import ManagerStore, now_iso
from app.manager.tasks import ExecutiveTaskManager

MAX_BRIEFS = 60  # two months of history


class DailyBriefGenerator:
    def __init__(self, store: ManagerStore, knowledge: KnowledgeStore,
                 notifications: NotificationCenter,
                 tasks: ExecutiveTaskManager,
                 portfolio: PortfolioWorkspace):
        self.store = store
        self.knowledge = knowledge
        self.notifications = notifications
        self.tasks = tasks
        self.portfolio = portfolio
        self.executive = None  # ExecutiveIntelligence (V3.1), set by container

    def today(self) -> dict:
        """Today's brief — generated on first access, cached per day."""
        date = datetime.now(timezone.utc).date().isoformat()
        existing = next((b for b in self.store.read("daily_briefs")
                         if b.get("date") == date), None)
        brief = existing or self.generate()
        return self._overlay_executive(dict(brief))

    def _overlay_executive(self, brief: dict) -> dict:
        """V3.1: fill any empty brief panel from the Executive Intelligence
        layer, so the dashboard's AI Executive Brief reflects the ingested
        enterprise. Never overrides real project data (fills only blanks)."""
        ei = self.executive
        if ei is None or not getattr(ei, "available", False):
            return brief
        try:
            ex = ei.executive_brief()
        except Exception:  # noqa: BLE001 — brief never breaks on overlay
            return brief
        health = ex.get("health", {})
        if not brief.get("high_priority_issues"):
            brief["high_priority_issues"] = [
                {"title": e["event"], "detail": e["detail"],
                 "kind": "critical_risk", "project_id": "", "at": ""}
                for e in ex.get("critical_events", [])]
        if not brief.get("business_risks"):
            brief["business_risks"] = [
                {"insight": f"{r['risk']} — {r['detail']}", "project_id": ""}
                for r in ex.get("risk_assessment", {}).get("top_risks", [])]
        if not brief.get("recommendations"):
            brief["recommendations"] = [
                {"action": r["title"], "priority":
                 1 if r["priority"] == "high" else 3, "project_id": ""}
                for r in ex.get("recommended_actions", [])]
        if not brief.get("important_reports"):
            brief["important_reports"] = [
                {"title": d["title"], "project_id": d["decision_id"],
                 "health_score": None}
                for d in ex.get("major_decisions", [])]
        if not brief.get("upcoming_deadlines"):
            brief["upcoming_deadlines"] = [
                {"task_id": d.get("task_id", ""), "title": d["task"],
                 "due_date": d.get("due", "")}
                for d in ex.get("upcoming_deadlines", [])]
        if brief.get("portfolio_health", {}).get("average_health_score") is None:
            brief.setdefault("portfolio_health", {})["average_health_score"] = \
                health.get("portfolio")
        brief["executive"] = ex   # the full brief for premium consumers
        return brief

    def generate(self) -> dict:
        """(Re)generate today's brief from current Brain state."""
        date = datetime.now(timezone.utc).date().isoformat()
        overview = self.portfolio.overview()
        strategic = self.knowledge.strategic_insights(50)

        brief = {
            "date": date, "generated_at": now_iso(),
            "high_priority_issues": [
                {"title": n["title"], "detail": n.get("detail", ""),
                 "kind": n["kind"], "project_id": n["project_id"],
                 "at": n["created_at"]}
                for n in self.notifications.recent(50, unread_only=True)
                if n["kind"] in ("critical_risk", "workflow_failure")][:8],
            "portfolio_changes": overview["historical_comparison"][:5],
            "important_reports":
                overview["business_performance"]["recent_reports"],
            "open_action_items": [
                {"task_id": t["task_id"], "title": t["title"],
                 "priority": t.get("priority"), "status": t["status"],
                 "project_id": t.get("project_id", "")}
                for t in self.tasks.open_tasks(10)],
            "upcoming_deadlines": [
                {"task_id": t["task_id"], "title": t["title"],
                 "due_date": t["due_date"]}
                for t in self.tasks.due_soon(7)],
            "business_risks": [
                {"insight": s["insight"], "project_id": s.get("project_id")}
                for s in reversed(strategic) if s.get("horizon") == "risk"][:6],
            "growth_opportunities": [
                {"insight": s["insight"], "project_id": s.get("project_id")}
                for s in reversed(strategic)
                if s.get("horizon") == "opportunity"][:6],
            "recommendations": [
                {"action": r["action"], "priority": r.get("priority"),
                 "project_id": r.get("project_id")}
                for r in reversed(self.knowledge.recommendations(20))][:6],
            "portfolio_health": overview["portfolio_health"],
        }
        briefs = [b for b in self.store.read("daily_briefs")
                  if b.get("date") != date]
        briefs.append(brief)
        self.store.write("daily_briefs", briefs[-MAX_BRIEFS:])
        return brief

    def history(self, limit: int = 14) -> list[dict]:
        return list(reversed(self.store.read("daily_briefs")))[:limit]

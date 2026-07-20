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

    def today(self) -> dict:
        """Today's brief — generated on first access, cached per day."""
        date = datetime.now(timezone.utc).date().isoformat()
        existing = next((b for b in self.store.read("daily_briefs")
                         if b.get("date") == date), None)
        return existing or self.generate()

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

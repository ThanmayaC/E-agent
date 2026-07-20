"""Portfolio Workspace (Portfolio Module, executive view).

Business-level portfolio intelligence composed from what the platform
already knows: per-project health from business contexts, health trends and
historical comparison from organizational report memory, risks and
opportunities from strategic memory. No analytics are computed here — the
workspace reads, ranks, and presents.
"""
from __future__ import annotations

from app.knowledge.store import KnowledgeStore
from app.repositories.artifact_store import ArtifactStore


class PortfolioWorkspace:
    def __init__(self, store: ArtifactStore, knowledge: KnowledgeStore):
        self.store = store
        self.knowledge = knowledge

    # ------------------------------------------------------------ projects
    def projects(self) -> list[dict]:
        out = []
        for pid in self.store.list_projects():
            state = self.store.load(pid, "state") or {}
            if not state:
                continue
            context = self.store.load(pid, "business_context", {}) or {}
            metrics = context.get("executive_metrics") or {}
            out.append({
                "project_id": pid, "name": state.get("name", pid),
                "status": state.get("status", "unknown"),
                "health_score": metrics.get("health_score"),
                "report_version": state.get("report_version"),
                "report_generated_at": state.get("report_generated_at"),
            })
        out.sort(key=lambda p: str(p.get("report_generated_at") or ""),
                 reverse=True)
        return out

    # ------------------------------------------------------------ overview
    def overview(self) -> dict:
        projects = self.projects()
        scored = [p for p in projects if p.get("health_score") is not None]
        history = self.knowledge.report_history(100)

        # health trend per project + comparison latest vs previous
        trends: dict[str, list[dict]] = {}
        for entry in history:
            trends.setdefault(entry["project_id"], []).append(
                {"health_score": entry.get("health_score"),
                 "at": entry.get("generated_at")})
        comparison = []
        for pid, series in trends.items():
            if len(series) >= 2:
                latest, previous = series[-1], series[-2]
                if latest["health_score"] is not None \
                        and previous["health_score"] is not None:
                    comparison.append({
                        "project_id": pid,
                        "latest": latest["health_score"],
                        "previous": previous["health_score"],
                        "change": round(latest["health_score"]
                                        - previous["health_score"], 2)})
        comparison.sort(key=lambda c: abs(c["change"]), reverse=True)

        strategic = self.knowledge.strategic_insights(50)
        risks = [s for s in strategic if s.get("horizon") == "risk"]
        opportunities = [s for s in strategic
                         if s.get("horizon") == "opportunity"]

        return {
            "portfolio_health": {
                "average_health_score": round(
                    sum(p["health_score"] for p in scored) / len(scored), 1)
                    if scored else None,
                "projects_total": len(projects),
                "projects_ready": sum(1 for p in projects
                                      if p["status"] == "ready"),
                "projects_attention": sum(
                    1 for p in projects
                    if p["status"] in ("failed", "awaiting_clarification")),
            },
            "projects": projects,
            "trends": trends,
            "historical_comparison": comparison[:10],
            "risks": list(reversed(risks))[:10],
            "opportunities": list(reversed(opportunities))[:10],
            "business_performance": {
                "reports_generated": len(history),
                "recent_reports": list(reversed(history))[:5],
            },
            "recommended_priorities": [
                r for r in reversed(self.knowledge.recommendations(20))][:8],
        }

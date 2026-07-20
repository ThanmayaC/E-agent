"""Background Intelligence — the platform thinking while nobody is asking.

These are the job bodies the Enterprise Scheduler runs on a cadence:
knowledge, memory, portfolio, predictions, risks, opportunities, and
recommendations stay current without a manager pressing anything. Each is a
thin coordinator over services that already exist, written to be safe to run
repeatedly: every one is idempotent, bounded, and degrades to a recorded
skip rather than an exception when a surface is unavailable.

``metrics_snapshot`` is the other half of autonomy: it renders the
platform's own numbers under stable metric names, which is what lets goals
measure themselves (``portfolio.average_health_score`` and friends).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from app.core.logging import get_logger

logger = get_logger(__name__)

# A prediction whose confidence sits below this is worth investigating.
LOW_CONFIDENCE = 0.5
# A risk count jump of this size across the portfolio is an anomaly.
RISK_SPIKE = 3


@dataclass
class BackgroundIntelligence:
    """Continuous refresh jobs. Collaborators are injected by the runtime."""
    store: Any            # ArtifactStore
    knowledge: Any        # KnowledgeStore
    memory: Any           # MemoryManager
    portfolio: Any        # PortfolioWorkspace
    tasks: Any            # ExecutiveTaskManager
    bus: Any              # EventBus
    goals: Any            # GoalEngine
    brain: Any = None     # EnterpriseBrain

    # ------------------------------------------------------------ knowledge
    def refresh_knowledge(self) -> dict:
        """Verify the Brain's knowledge surfaces and rebuild enterprise
        context. Announces KnowledgeUpdated so triggers can react."""
        if self.brain is None:
            return {"skipped": "brain disabled"}
        stats = self.knowledge.stats()
        self.bus.publish("KnowledgeUpdated",
                         {"source": "background_refresh", **stats},
                         source="background.knowledge")
        return {"knowledge": stats, "brain_state": self.brain.state}

    def refresh_memory(self) -> dict:
        """Keep the memory layers and organizational knowledge aligned."""
        if self.brain is None:
            return {"skipped": "brain disabled"}
        return {"memory": self.brain.synchronizer.stats()}

    # ------------------------------------------------------------ portfolio
    def refresh_portfolio(self) -> dict:
        overview = self.portfolio.overview()
        health = overview["portfolio_health"]
        previous = self.store.load("_enterprise", "portfolio_snapshot",
                                   {}) or {}
        self.store.save("_enterprise", "portfolio_snapshot", health)
        current, before = (health.get("average_health_score"),
                           previous.get("average_health_score"))
        if current is not None and before is not None and \
                abs(current - before) >= 1.0:
            self.bus.publish("PortfolioChanged",
                             {"average_health_score": current,
                              "previous": before,
                              "health_change": round(current - before, 2),
                              "projects_attention":
                                  health.get("projects_attention", 0)},
                             source="background.portfolio")
        return {"projects": health.get("projects_total", 0),
                "average_health_score": current}

    # ---------------------------------------------------------- predictions
    def refresh_predictions(self) -> dict:
        """Watch forecast confidence across the portfolio. A model whose
        confidence has dropped is announced, not silently trusted."""
        low, checked = [], 0
        for pid in self.store.list_projects():
            forecasts = self.store.load(pid, "forecasts", {}) or {}
            series = forecasts.get("series") or forecasts.get("forecasts") or []
            if not isinstance(series, list):
                continue
            for forecast in series:
                if not isinstance(forecast, dict):
                    continue
                checked += 1
                confidence = forecast.get("confidence")
                if isinstance(confidence, (int, float)) and \
                        confidence < LOW_CONFIDENCE:
                    low.append({"project_id": pid,
                                "metric": forecast.get("metric",
                                                       forecast.get("name", "")),
                                "confidence": round(float(confidence), 3)})
        for item in low[:5]:
            self.bus.publish("PredictionConfidenceDropped", item,
                             project_id=item["project_id"],
                             source="background.predictions")
        return {"checked": checked, "low_confidence": len(low)}

    # ---------------------------------------------------------------- risks
    def refresh_risks(self) -> dict:
        overview = self.portfolio.overview()
        risks = overview["risks"]
        previous = self.store.load("_enterprise", "risk_snapshot", {}) or {}
        count_before = previous.get("count")
        self.store.save("_enterprise", "risk_snapshot", {"count": len(risks)})
        if count_before is not None and len(risks) - count_before >= RISK_SPIKE:
            self.bus.publish("RiskIncreased",
                             {"count": len(risks), "previous": count_before,
                              "increase": len(risks) - count_before,
                              "top_risk": str(risks[0].get("insight", ""))[:200]
                              if risks else ""},
                             source="background.risks")
        return {"risks": len(risks), "previous": count_before}

    def refresh_opportunities(self) -> dict:
        overview = self.portfolio.overview()
        return {"opportunities": len(overview["opportunities"])}

    # ------------------------------------------------------ recommendations
    def refresh_recommendations(self) -> dict:
        """Surface recommendations the platform holds but has never acted on
        — a recommendation nobody turned into a task is a recommendation the
        business never received."""
        recommendations = self.knowledge.recommendations(20)
        open_titles = {t["title"].strip().lower()
                       for t in self.tasks.tasks(limit=500)}
        unactioned = [r for r in recommendations
                      if str(r.get("action", "")).strip().lower()
                      not in open_titles]
        return {"total": len(recommendations),
                "without_a_task": len(unactioned)}

    # -------------------------------------------------------------- anomaly
    def detect_anomalies(self) -> dict:
        """Portfolio-level anomaly sweep: projects that failed, stalled at a
        clarification, or fell off a health cliff."""
        overview = self.portfolio.overview()
        anomalies = []
        for project in overview["projects"]:
            if project["status"] == "failed":
                anomalies.append({"project_id": project["project_id"],
                                  "kind": "analysis_failed",
                                  "detail": f"{project['name']} last analysis "
                                            f"failed"})
        for change in overview["historical_comparison"]:
            if change["change"] <= -10:
                anomalies.append({"project_id": change["project_id"],
                                  "kind": "health_drop",
                                  "detail": f"health fell {abs(change['change'])} "
                                            f"points to {change['latest']}",
                                  "health_change": change["change"]})
        for anomaly in anomalies[:5]:
            self.bus.publish("AnomalyDetected", anomaly,
                             project_id=anomaly["project_id"],
                             source="background.anomalies")
        return {"anomalies": len(anomalies)}

    # ---------------------------------------------------------------- goals
    def refresh_goals(self) -> dict:
        """Goals measure themselves from the platform's own metrics."""
        outcome = self.goals.refresh_all(self.metrics_snapshot())
        outcome.update(self.goals.sweep_deadlines())
        return outcome

    def metrics_snapshot(self) -> dict[str, float]:
        """The platform's numbers under stable names a KPI can point at."""
        overview = self.portfolio.overview()
        health = overview["portfolio_health"]
        task_stats = self.tasks.stats()
        knowledge_stats = self.knowledge.stats()
        metrics: dict[str, float] = {
            "portfolio.projects_total": float(health.get("projects_total") or 0),
            "portfolio.projects_ready": float(health.get("projects_ready") or 0),
            "portfolio.projects_attention":
                float(health.get("projects_attention") or 0),
            "portfolio.risks": float(len(overview["risks"])),
            "portfolio.opportunities": float(len(overview["opportunities"])),
            "portfolio.reports_generated":
                float(overview["business_performance"]["reports_generated"]),
            "tasks.open": float(task_stats.get("pending", 0)
                                + task_stats.get("follow_up", 0)),
            "tasks.completed": float(task_stats.get("completed", 0)),
            "knowledge.learning_events":
                float(knowledge_stats.get("learning_events", 0)),
        }
        if health.get("average_health_score") is not None:
            metrics["portfolio.average_health_score"] = \
                float(health["average_health_score"])
        for project in overview["projects"]:
            if project.get("health_score") is not None:
                metrics[f"project.{project['project_id']}.health_score"] = \
                    float(project["health_score"])
        return metrics

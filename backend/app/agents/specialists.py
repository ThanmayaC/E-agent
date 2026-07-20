"""Specialized analyst agents.

Each agent has a single responsibility and works exclusively from the
project's analytical artifacts (facts) through the tool layer. They give the
platform role-shaped entry points — Portfolio Managers, Product Managers, and
Executives each talk to the agent that matches their altitude — and are the
seams where deeper autonomous behavior lands over time.
"""
from __future__ import annotations

from typing import Any

from app.agents.base import AgentRequest, AgentResult, BaseAgent, WorkingMemory


class SchemaAnalystAgent(BaseAgent):
    name = "schema_analyst"
    role = "Explains datasets, columns, semantics, and relationships of a project"

    def execute(self, request: AgentRequest, plan, working: WorkingMemory) -> AgentResult:
        pid = request.project_id
        lookup = self.tools.get("artifact_lookup")
        output = {
            "datasets": lookup.run(project_id=pid, artifact="profiles", default=[]),
            "semantics": lookup.run(project_id=pid, artifact="semantic_layer", default=[]),
            "relationships": lookup.run(project_id=pid, artifact="relationships", default=[]),
        }
        return AgentResult(status="ok", output=output, confidence=1.0)


class BusinessAnalystAgent(BaseAgent):
    name = "business_analyst"
    role = "Surfaces KPIs, statistical signals, anomalies, and forecasts of a project"

    def execute(self, request: AgentRequest, plan, working: WorkingMemory) -> AgentResult:
        pid = request.project_id
        lookup = self.tools.get("artifact_lookup")
        output = {
            "kpis": lookup.run(project_id=pid, artifact="kpis", default=[]),
            "signals": lookup.run(project_id=pid, artifact="signals", default=[]),
            "forecasts": lookup.run(project_id=pid, artifact="forecasts", default=[]),
            "quality": lookup.run(project_id=pid, artifact="quality", default={}),
        }
        return AgentResult(status="ok", output=output, confidence=1.0)


class PortfolioAgent(BaseAgent):
    name = "portfolio"
    role = "Tracks portfolio health across analyses using enterprise report history"

    def execute(self, request: AgentRequest, plan, working: WorkingMemory) -> AgentResult:
        history = self.memory.organizational.report_history(limit=30)
        current = {}
        if request.project_id:
            context = self.memory.business(request.project_id).context()
            current = {
                "portfolio_summary": context.get("portfolio_summary", {}),
                "executive_metrics": context.get("executive_metrics", {}),
            }
        return AgentResult(status="ok",
                           output={"current": current, "report_history": history},
                           confidence=1.0)


class ManagerAgent(BaseAgent):
    name = "manager"
    role = "Turns AI recommendations into trackable priority actions and follow-ups"

    def execute(self, request: AgentRequest, plan, working: WorkingMemory) -> AgentResult:
        pid = request.project_id
        ai = self.tools.get("artifact_lookup").run(project_id=pid, artifact="ai_report",
                                                   default={}) or {}
        actions = [{"action": a, "status": "open"} for a in ai.get("priority_actions", [])]
        return AgentResult(status="ok", output={
            "priority_actions": actions,
            "recommendations": ai.get("recommendations", []),
            "follow_up_capabilities": ["email", "calendar"],  # planned tools
        }, confidence=float(ai.get("confidence") or 0.0))


class PlannerAgent(BaseAgent):
    name = "planner"
    role = "Routes a goal to the right specialized agent and tools"

    ROUTES = {
        "schema_analyst": ("schema", "column", "table", "dataset", "relationship"),
        "business_analyst": ("kpi", "trend", "anomaly", "forecast", "signal", "quality"),
        "portfolio": ("portfolio", "health", "history", "across"),
        "manager": ("action", "follow", "recommendation", "priority", "track"),
    }

    def execute(self, request: AgentRequest, plan, working: WorkingMemory) -> AgentResult:
        goal = request.goal.lower()
        scores = {name: sum(kw in goal for kw in kws) for name, kws in self.ROUTES.items()}
        best = max(scores, key=scores.get)
        chosen = best if scores[best] > 0 else "copilot"
        return AgentResult(status="ok", output={"agent": chosen,
                                                "reason": f"goal matched {scores[best]} keyword(s)"},
                           confidence=min(0.5 + scores[best] * 0.2, 1.0))

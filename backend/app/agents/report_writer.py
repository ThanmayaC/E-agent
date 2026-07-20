"""Report Writer Agent — produces the executive narrative.

The Intelligence Engine produces facts; this agent turns them into the
executive summary, recommendations, management commentary, risk and
opportunity analysis, and priority actions — through the reasoning model,
never through Python templates. Each generated report is recorded in the
enterprise knowledge store so the platform builds report history over time.
"""
from __future__ import annotations

from typing import Any

from app.agents.base import AgentPlan, AgentRequest, AgentResult, BaseAgent
from app.agents.reasoning import AIReasoningEngine
from app.domain.entities import AIReport
from app.memory.manager import MemoryManager, WorkingMemory
from app.tools.registry import ToolRegistry


class ReportWriterAgent(BaseAgent):
    name = "report_writer"
    role = "Writes executive reports (summary, risks, opportunities, recommendations) from facts"

    def __init__(self, tools: ToolRegistry, memory: MemoryManager,
                 reasoning: AIReasoningEngine):
        super().__init__(tools, memory)
        self._reasoning = reasoning

    # ------------------------------------------------------------ public
    def write(self, project_id: str, business_context: dict[str, Any]) -> AIReport:
        result = self.run(AgentRequest(goal="write executive report",
                                       project_id=project_id,
                                       payload={"context": business_context}))
        if isinstance(result.output, AIReport):
            return result.output
        return AIReport(status="failed", error=str(result.output or "report writer failed"))

    # ------------------------------------------------------- agent hooks
    def observe(self, request: AgentRequest, working: WorkingMemory) -> dict[str, Any]:
        context = request.payload.get("context") or \
            self.memory.business(request.project_id).context()
        return {"context": context}

    def plan(self, request: AgentRequest, understanding: dict[str, Any],
             working: WorkingMemory) -> AgentPlan:
        working.set("context", understanding["context"])
        return AgentPlan(steps=["generate prompt", "reason", "validate", "record history"])

    def execute(self, request: AgentRequest, plan: AgentPlan,
                working: WorkingMemory) -> AgentResult:
        report = self._reasoning.generate_report(working.get("context", {}))
        return AgentResult(status=report.status, output=report,
                           confidence=report.confidence)

    def learn(self, request: AgentRequest, result: AgentResult,
              working: WorkingMemory) -> None:
        if result.status != "ok" or not request.project_id:
            return
        context = working.get("context", {})
        health = ((context.get("executive_metrics") or {}).get("health_score")
                  if isinstance(context, dict) else None)
        self.memory.organizational.record_report(
            request.project_id,
            title=(context.get("portfolio_summary") or {}).get("name", request.project_id)
            if isinstance(context, dict) else request.project_id,
            health_score=float(health or 0.0))

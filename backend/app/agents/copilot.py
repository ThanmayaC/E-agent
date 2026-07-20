"""Copilot Agent — answers business questions over a project's analytics.

Observe:  semantic retrieval (vector search) + structured facts + memory.
Understand/Plan: focus the context on the question; decide the tools.
Execute:  generated prompt → reasoning model → grounded answer.
Learn:    the exchange is stored in conversation memory so follow-up
          questions can resolve references.

The copilot never answers from raw Excel and never uses template narrative;
all reasoning goes through the provider-agnostic LLM layer.
"""
from __future__ import annotations

from typing import Any

from app.agents.base import AgentPlan, AgentRequest, AgentResult, BaseAgent
from app.agents.reasoning import AIReasoningEngine
from app.memory.manager import MemoryManager, WorkingMemory
from app.tools.registry import ToolRegistry


class CopilotAgent(BaseAgent):
    name = "copilot"
    role = "Answers business questions with answers grounded in the project's analytics"

    def __init__(self, tools: ToolRegistry, memory: MemoryManager,
                 reasoning: AIReasoningEngine):
        super().__init__(tools, memory)
        self._reasoning = reasoning

    # ------------------------------------------------------------ public
    def ask(self, project_id: str, question: str) -> dict[str, Any]:
        result = self.run(AgentRequest(goal=question, project_id=project_id))
        if result.status == "failed":
            return {"status": "failed", "answer": f"Copilot failed: {result.output}",
                    "cited_facts": [], "confidence": 0.0}
        return result.output

    # ------------------------------------------------------- agent hooks
    def observe(self, request: AgentRequest, working: WorkingMemory) -> dict[str, Any]:
        """Assemble a compact, question-focused analytics context. Only
        aggregated facts — no raw rows, no DataFrames."""
        pid = request.project_id
        retrieved = self.tools.run("vector_search", project_id=pid,
                                   query=request.goal, top_k=8)
        business = self.memory.business(pid)
        working.set("conversation", self.memory.conversation(pid).recent(6))
        return {
            "retrieved": retrieved,
            "context": business.context(),
            "kpis": business.artifact("kpis", []) or [],
            "signals": business.artifact("signals", []) or [],
            "forecasts": business.artifact("forecasts", []) or [],
        }

    def understand(self, request: AgentRequest, observation: dict[str, Any],
                   working: WorkingMemory) -> dict[str, Any]:
        words = [w for w in request.goal.lower().split() if len(w) > 3]

        def focus(items: list[dict], keys: list[str], limit: int) -> list[dict]:
            hits = [i for i in items
                    if any(w in " ".join(str(i.get(k, "")) for k in keys).lower() for w in words)]
            return (hits or items)[:limit]

        full = observation["context"]
        return {
            "retrieved": [
                {"kind": r.get("kind"), "title": r.get("title"), "text": r.get("text", "")[:200]}
                for r in observation["retrieved"]
            ],
            "portfolio_summary": full.get("portfolio_summary", {}),
            "schema": full.get("schema", [])[:8],
            "relationships": full.get("relationships", [])[:8],
            "quality": full.get("quality", {}),
            "kpis": focus(observation["kpis"], ["name"], 8),
            "signals": focus(observation["signals"], ["kpi_name", "kind"], 8),
            "forecasts": focus(observation["forecasts"], ["kpi_name"], 5),
            "growth": full.get("growth", {}),
        }

    def plan(self, request: AgentRequest, understanding: dict[str, Any],
             working: WorkingMemory) -> AgentPlan:
        working.set("focused_context", understanding)
        return AgentPlan(steps=["retrieve", "reason", "remember"],
                         tools=["vector_search"])

    def execute(self, request: AgentRequest, plan: AgentPlan,
                working: WorkingMemory) -> AgentResult:
        context = working.get("focused_context", {})
        answer = self._reasoning.answer(request.goal, context,
                                        conversation=working.get("conversation"))
        answer["sources"] = context.get("retrieved", [])
        return AgentResult(status=answer.get("status", "ok"), output=answer,
                           confidence=float(answer.get("confidence") or 0.0))

    def learn(self, request: AgentRequest, result: AgentResult,
              working: WorkingMemory) -> None:
        if result.status != "ok" or not request.project_id:
            return
        conversation = self.memory.conversation(request.project_id)
        conversation.append("user", request.goal)
        conversation.append("assistant", str(result.output.get("answer", ""))[:2000],
                            meta={"confidence": result.confidence})

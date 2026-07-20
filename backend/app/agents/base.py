"""Agent framework.

Every agent follows the same reasoning loop instead of calling the LLM
directly for every request:

    Observe → Understand → Plan → Choose Tools → Execute → Verify → Learn

An agent has ONE clear responsibility, may invoke tools from the ToolRegistry,
and reads/writes memory through the MemoryManager. When a plan's confidence
is too low the agent returns clarification questions instead of guessing.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

from app.core.logging import get_logger
from app.memory.manager import MemoryManager, WorkingMemory
from app.tools.registry import ToolRegistry

logger = get_logger(__name__)


@dataclass
class AgentRequest:
    """What the agent is asked to do."""
    goal: str
    project_id: str = ""
    payload: dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentPlan:
    """Output of the planning phase."""
    steps: list[str] = field(default_factory=list)
    tools: list[str] = field(default_factory=list)
    confidence: float = 1.0
    clarification_questions: list[str] = field(default_factory=list)

    @property
    def needs_clarification(self) -> bool:
        return bool(self.clarification_questions)


@dataclass
class AgentResult:
    status: str  # ok | needs_clarification | failed | unavailable
    output: Any = None
    clarification_questions: list[str] = field(default_factory=list)
    confidence: float = 0.0
    agent: str = ""


class BaseAgent(ABC):
    """Base class for every specialized agent."""

    name: str = "agent"
    role: str = ""  # single-sentence responsibility statement

    def __init__(self, tools: ToolRegistry, memory: MemoryManager):
        self.tools = tools
        self.memory = memory

    # ------------------------------------------------------ reasoning loop
    def run(self, request: AgentRequest) -> AgentResult:
        working = self.memory.working()
        try:
            observation = self.observe(request, working)
            understanding = self.understand(request, observation, working)
            plan = self.plan(request, understanding, working)
            if plan.needs_clarification:
                return AgentResult(status="needs_clarification",
                                   clarification_questions=plan.clarification_questions,
                                   confidence=plan.confidence, agent=self.name)
            result = self.execute(request, plan, working)
            result = self.verify(request, result, working)
            self.learn(request, result, working)
            result.agent = self.name
            return result
        except Exception as exc:  # noqa: BLE001 — agents must degrade gracefully
            logger.exception("Agent %s failed", self.name)
            return AgentResult(status="failed", output=str(exc)[:500], agent=self.name)

    # --------------------------------------------------------------- hooks
    def observe(self, request: AgentRequest, working: WorkingMemory) -> dict[str, Any]:
        """Gather the facts relevant to the request (artifacts, memory, tools)."""
        return {}

    def understand(self, request: AgentRequest, observation: dict[str, Any],
                   working: WorkingMemory) -> dict[str, Any]:
        """Interpret the observation in business terms."""
        return observation

    def plan(self, request: AgentRequest, understanding: dict[str, Any],
             working: WorkingMemory) -> AgentPlan:
        """Decide steps and tools; emit clarification questions if unsure."""
        return AgentPlan(steps=["execute"])

    @abstractmethod
    def execute(self, request: AgentRequest, plan: AgentPlan,
                working: WorkingMemory) -> AgentResult:
        """Carry out the plan."""

    def verify(self, request: AgentRequest, result: AgentResult,
               working: WorkingMemory) -> AgentResult:
        """Check the result before returning it."""
        return result

    def learn(self, request: AgentRequest, result: AgentResult,
              working: WorkingMemory) -> None:
        """Persist anything worth remembering (memory / knowledge store)."""

    def describe(self) -> dict:
        return {"name": self.name, "role": self.role}


# The registry lives in ``app.agents.registry`` (V2.2): it grew descriptors,
# capability discovery, policies, and health, and importing it here would be
# circular. ``from app.agents.registry import AgentRegistry``.

"""Manager Module (SDS §2.7) — status: implemented.

The executive intelligence layer and the primary interface between the
Enterprise Brain and enterprise users. ``ManagerWorkspace`` composes the
Executive Workspace (dashboard, daily brief, tasks, decisions, report
reviews, portfolio, notifications) from other modules' outputs — it never
performs deterministic analytics directly. The reasoning stack it
coordinates: ``AIReasoningEngine`` (Enterprise Context → generated prompt →
LLM → validated structure), ``PromptGenerationAgent``, ``CopilotAgent``,
and ``ManagerAgent``.
"""
from app.agents.copilot import CopilotAgent
from app.agents.prompt_generator import PromptGenerationAgent
from app.agents.reasoning import AIReasoningEngine
from app.agents.specialists import ManagerAgent
from app.manager import (
    DailyBriefGenerator, DecisionCenter, ExecutiveTaskManager, ManagerStore,
    ManagerWorkspace, ReportReviewCenter,
)

__all__ = ["CopilotAgent", "PromptGenerationAgent", "AIReasoningEngine",
           "ManagerAgent", "DailyBriefGenerator", "DecisionCenter",
           "ExecutiveTaskManager", "ManagerStore", "ManagerWorkspace",
           "ReportReviewCenter"]

"""Manager Module — the Executive Workspace.

The primary interface between the Enterprise Brain and enterprise users.
Executives never touch the knowledge graph, memory layers, embeddings, the
prompt engine, or LangGraph — the Manager Module consumes what the other
modules produce and presents business views: today's summary, portfolio
health, risks, opportunities, tasks, decisions, report reviews, and the
daily brief. It performs NO deterministic analytics of its own (SDS).
"""
from app.manager.briefing import DailyBriefGenerator
from app.manager.decisions import DecisionCenter
from app.manager.portfolio import PortfolioWorkspace
from app.manager.reviews import ReportReviewCenter
from app.manager.store import ManagerStore
from app.manager.tasks import ExecutiveTaskManager
from app.manager.workspace import ManagerWorkspace

__all__ = ["DailyBriefGenerator", "DecisionCenter", "PortfolioWorkspace",
           "ReportReviewCenter", "ManagerStore", "ExecutiveTaskManager",
           "ManagerWorkspace"]

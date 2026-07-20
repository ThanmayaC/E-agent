"""Supervisor Module (SDS §2.6).

Rules-first run owner: entry validation, pass control, run close. The
supervisor agent nodes are built by ``build_agents`` and wired into the
analysis graph by the LangGraph orchestration layer; ``route_after_verifier``
is the supervisor's bounded repair-loop routing decision.
"""
from app.orchestration.agents import build_agents, route_after_verifier

__all__ = ["build_agents", "route_after_verifier"]

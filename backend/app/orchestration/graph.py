"""Analysis graph assembly and the LangGraph orchestrator.

Topology (02-orchestration-langgraph.md §3):

    supervisor_entry → planner → ingest → understanding
        → [quality ∥ quant]                    (parallel fan-out)
        → [graph_build ∥ index]                (parallel fan-out)
        → confidence_gate                      (interrupt() on ambiguity)
        → ml → context → report → verifier
        → (repair loop, bounded) → assembler → learning → supervisor_exit

Checkpointed in SQLite (lite profile) so an interrupted run resumes at the
exact node — days later, in a different process — via Command(resume=…).
"""
from __future__ import annotations

import sqlite3
import threading
from typing import Any

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command

from app.core.logging import get_logger
from app.orchestration.agents import build_agents, route_after_verifier
from app.orchestration.nodes import NodeContext, build_nodes
from app.orchestration.state import FRAMES, AnalysisState

logger = get_logger(__name__)


def build_analysis_graph(ctx: NodeContext, checkpointer) -> Any:
    nodes = build_nodes(ctx)
    agents = build_agents(ctx)

    g = StateGraph(AnalysisState)
    g.add_node("supervisor_entry", agents["supervisor_entry"])
    g.add_node("planner", agents["planner"])
    g.add_node("ingest", nodes["ingest"])
    g.add_node("understanding", nodes["understanding"])
    g.add_node("quality", nodes["quality"])
    g.add_node("quant", nodes["quant"])
    g.add_node("graph_build", nodes["graph_build"])
    g.add_node("index", nodes["index"])
    g.add_node("confidence_gate", nodes["confidence_gate"])
    g.add_node("ml", agents["ml"])
    g.add_node("context", nodes["context"])
    g.add_node("report", agents["report"])
    g.add_node("verifier", agents["verifier"])
    g.add_node("repair", _repair)
    g.add_node("assembler", nodes["assembler"])
    g.add_node("learning", nodes["learning"])
    g.add_node("supervisor_exit", agents["supervisor_exit"])

    g.add_edge(START, "supervisor_entry")
    g.add_edge("supervisor_entry", "planner")
    g.add_edge("planner", "ingest")
    g.add_edge("ingest", "understanding")
    g.add_edge("understanding", "quality")            # ── parallel branch A
    g.add_edge("understanding", "quant")              # ── parallel branch B
    g.add_edge(["quality", "quant"], "graph_build")   # barrier join, fan out
    g.add_edge(["quality", "quant"], "index")
    g.add_edge(["graph_build", "index"], "confidence_gate")
    g.add_edge("confidence_gate", "ml")
    g.add_edge("ml", "context")
    g.add_edge("context", "report")
    g.add_edge("report", "verifier")
    g.add_conditional_edges("verifier", route_after_verifier(ctx.settings),
                            {"repair": "repair", "assemble": "assembler"})
    g.add_edge("repair", "report")
    g.add_edge("assembler", "learning")
    g.add_edge("learning", "supervisor_exit")
    g.add_edge("supervisor_exit", END)
    return g.compile(checkpointer=checkpointer)


def _repair(state: AnalysisState) -> dict:
    return {"repair_attempts": state.get("repair_attempts", 0) + 1}


class LangGraphOrchestrator:
    """Runs and resumes analysis graphs. `run(project_id)` keeps the exact
    runner signature the WorkflowEngine and v1 API already use."""

    def __init__(self, ctx: NodeContext):
        self.ctx = ctx
        path = ctx.settings.data_dir / "checkpoints.db"
        conn = sqlite3.connect(str(path), check_same_thread=False)
        self.checkpointer = SqliteSaver(conn)
        self.graph = build_analysis_graph(ctx, self.checkpointer)
        self._lock = threading.Lock()

    # ---------------------------------------------------------------- runs
    def run(self, project_id: str) -> str:
        """Start a fresh analysis run. Returns run_id. Pauses (instead of
        failing) when the confidence gate raises clarification questions."""
        run_id = self.ctx.ledger.open_run(project_id, graph="analysis")
        self._invoke(project_id, run_id,
                     {"project_id": project_id, "run_id": run_id, "passes": 0})
        return run_id

    def resume(self, project_id: str, run_id: str,
               answers: dict[str, Any]) -> str:
        """Resume an interrupted run at the confidence gate with the human's
        answers ({question_id: answer})."""
        self._invoke(project_id, run_id, Command(resume=answers))
        return run_id

    # ------------------------------------------------------------ internal
    def _invoke(self, project_id: str, run_id: str, payload: Any) -> None:
        config = {"configurable": {"thread_id": run_id},
                  "recursion_limit": 50}
        try:
            result = self.graph.invoke(payload, config)
        except Exception as exc:
            logger.exception("Analysis run %s failed for %s", run_id, project_id)
            self.ctx.ledger.close_run(run_id, "failed", str(exc))
            self.ctx.set_project_status(project_id, "failed")
            FRAMES.drop(run_id)
            return
        if result.get("__interrupt__"):
            # paused at the gate — checkpoint holds the state; frames stay
            # cached so a same-process resume keeps its data plane
            self.ctx.ledger.close_run(run_id, "awaiting_clarification")
            self.ctx.set_project_status(project_id, "awaiting_clarification")
            return
        self.ctx.ledger.close_run(run_id, "ready")
        FRAMES.drop(run_id)

    # -------------------------------------------------------------- queries
    def pending_interrupt(self, run_id: str) -> dict | None:
        """The gate's question payload for an awaiting run (from the ledger's
        event stream — the durable record of the interrupt)."""
        events = self.ctx.ledger.run_events(run_id)
        for e in reversed(events):
            if e["event"] == "interrupt":
                return e["payload"]
        return None

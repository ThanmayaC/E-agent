"""Typed graph state and the run-scoped frame cache.

State carries facts, references, and compact artifacts only. Raw DataFrames
never enter checkpointed state — they live in an in-process cache keyed by
run_id, populated by the ingest node and consumed only by pre-gate nodes
(which always execute in the same process as ingest). Post-gate nodes — the
ones that may execute after a days-later interrupt resume — need nothing from
the cache.
"""
from __future__ import annotations

import threading
from typing import Annotated, Any, TypedDict

import pandas as pd


def _keep_last(a: Any, b: Any) -> Any:
    """Reducer for keys that parallel branches may both carry unchanged."""
    return b if b is not None else a


class AnalysisState(TypedDict, total=False):
    project_id: str
    run_id: str
    project_name: str
    passes: int                    # supervisor-ordered analysis passes
    repair_attempts: int           # verifier → report agent repair loops
    plan: dict                     # Planner output — stored, auditable
    profiles: list                 # TableProfile models (compact)
    mappings: list                 # SemanticMapping models
    relationships: list
    kpis: list
    breakdowns: list
    signals: list
    forecasts: list
    feasibility: dict              # which analyses the data actually supports
    quality: Any                   # QualityReport
    understanding: Any             # UnderstandingAssessment
    ml_results: list               # ml_prediction payload dicts (citable ids)
    ml_selection: list             # per-KPI selection traces (audit)
    business_context: dict
    enterprise_context: dict       # unified Brain context (Prompt Engine input)
    ai_report: dict                # AIReport.model_dump()
    learning: dict                 # continuous-learning summary (Brain)
    verification: dict             # verifier node verdict + statistics
    report_version: int
    errors: Annotated[list, lambda a, b: (a or []) + (b or [])]


class FrameCache:
    """Run-scoped DataFrame store — the data plane's in-process edge."""

    def __init__(self) -> None:
        self._frames: dict[str, dict[str, pd.DataFrame]] = {}
        self._lock = threading.Lock()

    def put(self, run_id: str, frames: dict[str, pd.DataFrame]) -> None:
        with self._lock:
            self._frames[run_id] = frames

    def get(self, run_id: str) -> dict[str, pd.DataFrame]:
        with self._lock:
            frames = self._frames.get(run_id)
        if frames is None:
            raise RuntimeError(
                f"No frames cached for run {run_id}: a pre-gate node executed "
                "outside the ingesting process. Re-run the analysis.")
        return frames

    def drop(self, run_id: str) -> None:
        with self._lock:
            self._frames.pop(run_id, None)


FRAMES = FrameCache()

"""Memory Synchronization (Enterprise Brain).

After every successful analysis the synchronizer pushes what the per-project
memory layers learned into organizational knowledge, so memory continuously
feeds the Knowledge Engine:

- report memory      — already recorded by the Report Writer (report_history)
- decision memory    — priority actions recorded by the Knowledge Engine
- strategic memory   — high-severity risks and high-impact opportunities
                       from the evidence-verified report become strategic
                       insights (deterministic extraction, deduplicated)
- learning memory    — the Brain records one learning event per pipeline run

Synchronization is idempotent: re-syncing the same analysis adds nothing.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.memory.manager import MemoryManager

logger = get_logger(__name__)

SOURCE = "memory_sync"


class MemorySynchronizer:
    """Feeds memory layers into the organizational knowledge store."""

    def __init__(self, memory: MemoryManager):
        self.memory = memory

    def sync_after_analysis(self, project_id: str,
                            artifacts: dict[str, Any]) -> dict[str, int]:
        org = self.memory.organizational
        before = len(org.strategic_insights(1000))
        ai = artifacts.get("ai_report") or {}
        if ai.get("status") == "ok":
            for r in ai.get("risks") or []:
                if isinstance(r, dict) and \
                        r.get("severity") in ("high", "critical"):
                    text = str(r.get("risk", "")).strip()
                    if text:
                        org.add_strategic_insight(
                            f"Risk ({r['severity']}): {text}",
                            horizon="risk", project_id=project_id,
                            source=SOURCE)
            for o in ai.get("opportunities") or []:
                if isinstance(o, dict) and o.get("impact") == "high":
                    text = str(o.get("opportunity", "")).strip()
                    if text:
                        org.add_strategic_insight(
                            f"Opportunity (high impact): {text}",
                            horizon="opportunity", project_id=project_id,
                            source=SOURCE)
        added = len(org.strategic_insights(1000)) - before
        return {"strategic_insights_added": added}

    def stats(self) -> dict[str, int]:
        """Per-memory-layer entry counts (Enterprise Brain statistics)."""
        s = self.memory.organizational.stats()
        return {
            "decision_memory": s.get("decisions", 0),
            "report_memory": s.get("report_history", 0),
            "strategic_memory": s.get("strategic_insights", 0),
            "learning_memory": s.get("learning_events", 0),
            "business_memory_insights": s.get("insights", 0),
            "clarification_memory": s.get("clarifications", 0),
        }

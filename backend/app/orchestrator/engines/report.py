"""Report Engine — the reports that already exist, surfaced by title.

A report request ("give me the weekly review", "board brief") is served by
pointing at the reports the platform has generated and the executive summary
that frames them — under real titles, never raw ids (Phase 10). The engine does
not render a new document here; it supplies the report evidence the copilot
narrates and links, and the existing Report/Workspace generators remain the
place a fresh artifact is produced.
"""
from __future__ import annotations

from app.orchestrator.base import Engine, EngineRequest, EngineResult

MAX = 6


class ReportEngine(Engine):
    key = "report"
    label = "Report Engine"
    categories = ("report",)

    def __init__(self, knowledge=None, executive=None):
        self._knowledge = knowledge
        self._executive = executive

    def available(self) -> bool:
        return self._knowledge is not None or self._executive is not None

    def run(self, request: EngineRequest) -> EngineResult:
        res = self._result()
        titles: list[str] = []
        if self._knowledge is not None:
            try:
                for rep in self._knowledge.report_history(MAX):
                    title = rep.get("title") or "Report"
                    titles.append(title)
                    res.add(
                        "report",
                        f"report:{rep.get('project_id')}:{title[:30]}",
                        f"{title} — health {rep.get('health_score')}",
                        {"title": title,
                         "health_score": rep.get("health_score"),
                         "text": (f"Report '{title}' "
                                  f"(health {rep.get('health_score')}, "
                                  f"generated {rep.get('generated_at', '')}).")})
            except Exception as exc:  # noqa: BLE001
                res.note = f"report history: {str(exc)[:120]}"
        if self._executive is not None and getattr(self._executive,
                                                    "available", False):
            try:
                brief = self._executive.executive_brief()
                summary = brief.get("business_summary", "")
                if summary:
                    res.add("report", "report:executive-brief",
                            "Executive Brief — current week",
                            {"title": "Executive Brief",
                             "text": f"Executive Brief: {summary}"})
            except Exception:  # noqa: BLE001
                pass
        res.detail = {"reports_found": len(res.evidence), "titles": titles}
        return res

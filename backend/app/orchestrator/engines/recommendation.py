"""Recommendation Engine — what to do about it, with the why and the evidence.

"What should we do about the ICICI declines?", "how do we improve retention?" —
these want a course of action grounded in the numbers, not a definition from a
document. The engine draws on the multi-layer Insight Engine (deterministic +
ML + graph, each insight carrying its why, confidence, and recommended actions)
and the Executive Intelligence layer's ranked recommendations.

Every recommendation keeps its confidence and its supporting evidence, and the
Insight Engine's hallucination gate travels with it — a low-evidence insight is
flagged, not asserted.
"""
from __future__ import annotations

from app.orchestrator.base import Engine, EngineRequest, EngineResult

MAX = 6


class RecommendationEngine(Engine):
    key = "recommendation"
    label = "Recommendation Engine"
    categories = ("recommendation",)

    def __init__(self, insight_engine=None, executive=None):
        self._insights = insight_engine
        self._executive = executive

    def available(self) -> bool:
        return self._insights is not None or self._executive is not None

    def run(self, request: EngineRequest) -> EngineResult:
        res = self._result()
        counts = {"insights": 0, "executive": 0}
        if self._insights is not None:
            try:
                for ins in self._insights.insights(limit=MAX).get("insights", []):
                    actions = "; ".join(
                        a if isinstance(a, str) else a.get("action", "")
                        for a in ins.get("recommended_actions", [])[:3])
                    res.add(
                        "recommendation", f"insight:{ins.get('id') or ins.get('iid')}",
                        ins.get("what") or ins.get("title", "insight"),
                        {"confidence": ins.get("confidence"),
                         "priority": ins.get("priority"),
                         "text": (f"{ins.get('what', '')} Why: "
                                  f"{ins.get('why', '')} Impact: "
                                  f"{ins.get('impact', '')} Recommended: "
                                  f"{actions} (confidence "
                                  f"{ins.get('confidence')}, "
                                  f"{ins.get('confidence_label', '')}).")})
                    counts["insights"] += 1
            except Exception as exc:  # noqa: BLE001
                res.note = f"insights: {str(exc)[:120]}"
        if self._executive is not None and getattr(self._executive,
                                                    "available", False):
            try:
                brief = self._executive.executive_brief()
                for i, r in enumerate(brief.get("recommended_actions", [])[:MAX]):
                    res.add(
                        "recommendation", f"exec-rec:{i}", r.get("title", ""),
                        {"confidence": r.get("confidence"),
                         "priority": r.get("priority"),
                         "text": (f"{r.get('title', '')}. {r.get('reason', '')} "
                                  f"Owner {r.get('owner', '')}, priority "
                                  f"{r.get('priority', '')}, confidence "
                                  f"{r.get('confidence', '')}.")})
                    counts["executive"] += 1
            except Exception as exc:  # noqa: BLE001
                res.note = f"executive: {str(exc)[:120]}"
        res.detail = {"sources": counts}
        return res

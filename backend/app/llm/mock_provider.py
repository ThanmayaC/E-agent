"""Deterministic mock provider for tests and CI.

Returns schema-valid JSON so pipelines can be exercised without a live model.
This is a test double — it never ships narrative to real users (the factory
only selects it when explicitly configured)."""
from __future__ import annotations

import json

from app.llm.base_provider import BaseLLMProvider, ChatMessage


class MockProvider(BaseLLMProvider):
    name = "mock"

    def _chat_once(self, messages: list[ChatMessage], json_mode: bool) -> str:
        user = next((m.content for m in reversed(messages) if m.role == "user"), "")
        if '"answer"' in user or "copilot" in user.lower():
            return json.dumps({
                "answer": "[mock] Grounded answer derived from the supplied analytics context.",
                "cited_facts": ["mock:context"],
                "confidence": 0.9,
            })
        # cite a real evidence id from the supplied context when one exists,
        # so the deterministic verification path is exercised end to end
        evidence_ids = []
        try:
            marker = "(sole source of truth) ===\n"
            start = user.index(marker) + len(marker)
            payload = user[start:user.index("=== TASK ===")]
            # a knowledge block may follow the context JSON — drop it
            if "=== ENTERPRISE KNOWLEDGE" in payload:
                payload = payload[:payload.index("=== ENTERPRISE KNOWLEDGE")]
            ctx = json.loads(payload.strip())
            kpis = ctx.get("kpis") or []
            if kpis and kpis[0].get("id"):
                evidence_ids = [kpis[0]["id"]]
        except Exception:  # noqa: BLE001 — mock must never fail on parsing
            pass
        return json.dumps({
            "executive_summary": "[mock] Executive summary generated from supplied analytics.",
            "portfolio_health": "[mock] Portfolio health assessment.",
            "key_insights": [{"title": "[mock] Insight", "detail": "From context.",
                              "statement_type": "fact", "evidence_ids": evidence_ids,
                              "supporting_metrics": [], "confidence": 0.9}],
            "root_causes": [{"problem": "[mock] Problem",
                             "possible_cause": "[mock] Possible cause (hypothesis).",
                             "statement_type": "hypothesis",
                             "supporting_evidence": "From context.",
                             "evidence_ids": evidence_ids,
                             "missing_evidence": "[mock] Segment-level data.",
                             "confidence": "medium"}],
            "risks": [{"risk": "[mock] Risk", "severity": "medium",
                       "evidence_ids": evidence_ids}],
            "opportunities": [{"opportunity": "[mock] Opportunity", "impact": "medium",
                               "evidence_ids": evidence_ids}],
            "recommendations": [{"action": "[mock] Action", "priority": 1,
                                 "evidence_ids": evidence_ids,
                                 "expected_impact": "high", "difficulty": "low",
                                 "timeline": "2 weeks"}],
            "priority_actions": ["[mock] Priority action"],
            "data_limitations": ["[mock] Customer behaviour cannot be analysed."],
            "management_commentary": "[mock] Management commentary.",
            "next_investigation_areas": ["[mock] Investigation area"],
            "confidence_explanation": "[mock] Confidence explanation.",
            "confidence": 0.9,
        })

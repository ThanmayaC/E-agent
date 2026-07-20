"""Executive report assembler.

Fixed structure, every time. The backend contributes ONLY deterministic facts
(KPI values, forecasts, schema, quality, signals). Every narrative section —
executive summary, insights, root causes, risks, opportunities,
recommendations, commentary — comes verbatim from the AI reasoning layer.
No template narrative exists in this module.
"""
from __future__ import annotations

from datetime import datetime, timezone

from app.domain.entities import (
    KPI, AIReport, AnalyticsSignal, DeterministicRecommendation, Forecast,
    QualityReport, Relationship, TableProfile, WorkbookInfo,
)

# provenance of every report section, so the report is auditable: which
# sections are deterministic facts, which are statistics, which are AI
# narrative, and which are labelled hypotheses
SECTION_PROVENANCE = {
    "observed_facts": ["management_summary", "dataset_summary", "kpi_analysis"],
    "statistical_findings": ["signals", "predictive_analytics"],
    "ai_interpretation": ["executive_summary", "business_insights",
                          "risk_analysis", "opportunity_analysis"],
    "hypotheses": ["root_cause_analysis"],
    "recommendations": ["recommendations", "deterministic_recommendations"],
    "confidence": ["report_confidence"],
    "data_limitations": ["data_limitations"],
    "required_additional_data": ["next_investigation_areas"],
}


class ReportAssembler:
    def assemble(
        self,
        project_name: str,
        files: list[WorkbookInfo],
        profiles: list[TableProfile],
        relationships: list[Relationship],
        kpis: list[KPI],
        signals: list[AnalyticsSignal],
        forecasts: list[Forecast],
        quality: QualityReport,
        health_score: float,
        ai: AIReport,
        business_context: dict,
        deterministic_recommendations: list[DeterministicRecommendation] | None = None,
        report_confidence: dict | None = None,
        report_version: int = 1,
    ) -> dict:
        return {
            "meta": {
                "project": project_name,
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "structure_version": "2.1",
                "report_version": report_version,
                "sections": SECTION_PROVENANCE,
                "ai": {"status": ai.status, "provider": ai.provider,
                       "model": ai.model, "error": ai.error,
                       "confidence": ai.confidence},
            },
            # ---- deterministic confidence model (documented formula) ---------
            "report_confidence": report_confidence or {},
            # ---- narrative: 100% AI-generated -------------------------------
            "executive_summary": {
                "overall_health_score": health_score,  # deterministic metric
                "summary": ai.executive_summary,
                "portfolio_health": ai.portfolio_health,
                "management_commentary": ai.management_commentary,
                "priority_actions": ai.priority_actions,
            },
            "business_insights": ai.key_insights,
            "root_cause_analysis": ai.root_causes,  # hypotheses only, never asserted causes
            "risk_analysis": ai.risks,
            "opportunity_analysis": ai.opportunities,
            "recommendations": ai.recommendations,
            # ---- rule-derived, evidence-cited (never LLM) --------------------
            "deterministic_recommendations": [
                r.model_dump() for r in (deterministic_recommendations or [])
            ],
            # ---- what this dataset cannot answer -----------------------------
            "data_limitations": {
                "deterministic": business_context.get("data_limitations", {}),
                "ai_statements": ai.data_limitations,
            },
            "next_investigation_areas": ai.next_investigation_areas,
            "confidence_explanation": ai.confidence_explanation,
            # ---- facts: 100% deterministic ----------------------------------
            "management_summary": {
                "portfolio_overview": business_context["portfolio_summary"],
                "overall_kpis": [
                    {"name": k.name, "current": k.current_value,
                     "previous": k.previous_value, "growth_pct": k.growth_pct,
                     "trend": k.trend, "unit": k.unit}
                    for k in kpis[:10]
                ],
                "growth": business_context["growth"],
            },
            "dataset_summary": {
                "files": [f.model_dump() for f in files],
                "tables": [
                    {"dataset_id": p.dataset_id, "name": p.name, "rows": p.row_count,
                     "columns": p.column_count, "entity": p.entity.value,
                     "kind": "fact" if p.is_fact else ("dimension" if p.is_dimension else "reference"),
                     "time_grain": p.time_grain.value if p.time_grain else None,
                     "description": p.description}
                    for p in profiles
                ],
                "relationships": len(relationships),
                "quality_score": quality.overall_score,
                "avg_semantic_confidence": round(
                    sum(p.confidence for p in profiles) / max(len(profiles), 1), 2),
            },
            "kpi_analysis": [
                {
                    "kpi_id": k.id, "name": k.name, "expression": k.expression,
                    "unit": k.unit, "current": k.current_value,
                    "previous": k.previous_value, "growth_pct": k.growth_pct,
                    "trend": k.trend, "sparkline": k.sparkline,
                    "sparkline_labels": k.sparkline_labels,
                    "forecast": self._forecast_row(k, forecasts),
                    "confidence": k.confidence,
                }
                for k in kpis
            ],
            "signals": [s.model_dump() for s in signals],
            "predictive_analytics": {
                "forecasts": [f.model_dump() for f in forecasts[:10]],
                "next_month": [
                    {"kpi": f.kpi_name, "expected": f.values[0] if f.values else None,
                     "range": [f.lower[0], f.upper[0]] if f.lower else None,
                     "confidence": f.confidence, "status": f.status,
                     "validation": f.validation}
                    for f in forecasts[:8]
                ],
                "next_quarter": [
                    {"kpi": f.kpi_name,
                     "expected": round(sum(f.values[:3]), 2) if len(f.values) >= 3 else None,
                     "confidence": f.confidence}
                    for f in forecasts[:8]
                ],
            },
            "appendix": {
                "schema": [
                    {"dataset": p.name,
                     "columns": [{"name": c.name, "type": c.semantic_type.value,
                                  "role": c.role.value, "concept": c.concept.value,
                                  "confidence": c.concept_confidence} for c in p.columns]}
                    for p in profiles
                ],
                "relationships": [r.model_dump() for r in relationships],
                "quality_report": quality.model_dump(),
                "business_context": business_context,
                "metadata": {"engine": "EDIP pipeline v2",
                             "narrative_source": "llm", "facts_source": "deterministic"},
            },
        }

    @staticmethod
    def _forecast_row(k: KPI, forecasts: list[Forecast]) -> dict | None:
        fc = next((f for f in forecasts if f.kpi_id == k.id), None)
        if fc and fc.values:
            return {"next": fc.values[0], "confidence": fc.confidence,
                    "method": fc.method, "status": fc.status}
        if fc:  # gated: no values on purpose — say why instead
            return {"next": None, "confidence": 0.0, "method": fc.method,
                    "status": fc.status, "validation": fc.validation}
        return None

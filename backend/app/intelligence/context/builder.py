"""Business Context Builder.

Converts pipeline analytics into a compact, structured JSON context for the
LLM. Never raw Excel, never DataFrames, never thousands of rows — only
aggregated facts. This is the single source of truth the AI reasons over.

Every fact carries a stable evidence id (`id` field): KPIs, signals, and
forecasts are citable, and the reasoning layer verifies that every generated
insight cites ids that actually exist in this context. The context also
carries deterministic `data_limitations` so the model states what CANNOT be
analysed instead of inventing unsupported explanations.
"""
from __future__ import annotations

from typing import Any

from app.domain.entities import (
    KPI, AnalyticsSignal, Forecast, QualityReport, Relationship, TableProfile,
)
from app.domain.enums import BusinessConcept, ColumnRole, SemanticType, SignalKind

# analysis dimensions the platform can check for deterministically: when the
# schema contains no column of these concepts, the corresponding analysis is
# impossible and the report must say so instead of speculating
ANALYSIS_DIMENSIONS: list[dict[str, Any]] = [
    {"dimension": "customer", "concepts": {BusinessConcept.CUSTOMER, BusinessConcept.USER},
     "impact": "Customer behaviour cannot be analysed: no customer-level data present."},
    {"dimension": "merchant", "concepts": {BusinessConcept.MERCHANT},
     "impact": "Merchant behaviour cannot be analysed: no merchant-level data present."},
    {"dimension": "geography", "concepts": {BusinessConcept.REGION},
     "impact": "Regional analysis unavailable: no geography columns present."},
    {"dimension": "product", "concepts": {BusinessConcept.PRODUCT},
     "impact": "Product-level analysis (including cannibalisation) cannot be "
               "performed: no product hierarchy present."},
    {"dimension": "channel", "concepts": {BusinessConcept.CHANNEL, BusinessConcept.CAMPAIGN},
     "impact": "Channel or campaign attribution cannot be analysed: no channel "
               "or campaign data present."},
]


class BusinessContextBuilder:
    def __init__(self, max_kpis: int = 12, max_signals: int = 10, history_tail: int = 12):
        self.max_kpis = max_kpis
        self.max_signals = max_signals
        self.history_tail = history_tail

    def build(
        self,
        project_name: str,
        profiles: list[TableProfile],
        relationships: list[Relationship],
        kpis: list[KPI],
        signals: list[AnalyticsSignal],
        forecasts: list[Forecast],
        quality: QualityReport,
        understanding: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        trended = [k for k in kpis if k.growth_pct is not None]
        anomalies = [s for s in signals if s.kind == SignalKind.ANOMALY]
        return {
            # how confidently the platform understood the data (assessment
            # facts + user-answered clarifications) — lets the model reason
            # confidence-aware and in the organization's own terms
            **({"understanding": understanding} if understanding else {}),
            "portfolio_summary": {
                "name": project_name,
                "datasets": len(profiles),
                "total_rows": sum(p.row_count for p in profiles),
                "entities": sorted({p.entity.value for p in profiles if p.entity.value != "Unknown"}),
                "kpis_tracked": len(kpis),
            },
            "schema": [
                {
                    "dataset": p.name,
                    "entity": p.entity.value,
                    "kind": "fact" if p.is_fact else ("dimension" if p.is_dimension else "reference"),
                    "rows": p.row_count,
                    "time_grain": p.time_grain.value if p.time_grain else None,
                    "columns": [
                        {"name": c.name, "concept": c.concept.value, "role": c.role.value}
                        for c in p.columns
                    ][:20],
                }
                for p in profiles[:15]
            ],
            "relationships": [
                {
                    "from": f"{r.from_dataset}.{r.from_column}",
                    "to": f"{r.to_dataset}.{r.to_column}",
                    "type": r.rel_type.value,
                    "cardinality": r.cardinality.value,
                    "value_overlap": r.overlap,
                    "confidence": r.confidence,
                }
                for r in sorted(relationships, key=lambda r: -r.confidence)[:15]
            ],
            "quality": {
                "id": "quality:overall",
                "overall_score": quality.overall_score,
                "issue_counts": self._issue_counts(quality),
                "worst_issues": [
                    {"id": f"quality:{i.kind}:{i.dataset_id}",
                     "kind": i.kind, "dataset": i.dataset_id, "column": i.column,
                     "count": i.count, "detail": i.detail}
                    for i in quality.issues
                    if i.severity.value in ("high", "critical")
                ][:5],
            },
            "kpis": [self._kpi(k) for k in kpis[: self.max_kpis]],
            # unavailable forecasts are NOT given to the model as numbers —
            # only the fact that no valid forecast exists, and why
            "forecast": [
                {
                    "id": f"forecast:{f.kpi_id}",
                    "kpi": f.kpi_name,
                    "method": f.method,
                    "next_period": f.values[0] if f.values else None,
                    "next_period_range": [f.lower[0], f.upper[0]] if f.lower else None,
                    "next_quarter_sum": round(sum(f.values[:3]), 2) if len(f.values) >= 3 else None,
                    "confidence": f.confidence,
                    "status": f.status,
                    **({"validation": f.validation} if f.validation else {}),
                }
                for f in forecasts[:8] if f.status != "unavailable"
            ],
            "forecasts_unavailable": [
                {"kpi": f.kpi_name, "reasons": f.validation}
                for f in forecasts[:8] if f.status == "unavailable"
            ],
            "data_limitations": self.limitations(profiles, kpis),
            "anomalies": [self._signal(s) for s in anomalies[:5]],
            "correlations": [
                self._signal(s) for s in signals if s.kind == SignalKind.CORRELATION
            ][:5],
            "cannibalization": [
                self._signal(s) for s in signals if s.kind == SignalKind.INVERSE_CORRELATION
            ][:5],
            "top_changes": sorted(
                ({"kpi": k.name, "growth_pct": k.growth_pct, "current": k.current_value}
                 for k in trended),
                key=lambda d: -abs(d["growth_pct"]),
            )[:8],
            "growth": {
                "avg_growth_pct": round(sum(k.growth_pct for k in trended) / len(trended), 2) if trended else None,
                "improving": [k.name for k in trended if k.growth_pct > 1][:6],
                "declining": [k.name for k in trended if k.growth_pct < -1][:6],
                "trends": [self._signal(s) for s in signals if s.kind == SignalKind.TREND][:6],
                "seasonality": [self._signal(s) for s in signals if s.kind == SignalKind.SEASONALITY][:4],
            },
            "executive_metrics": {
                "health_score": self.health_score(kpis, signals, quality),
                "high_strength_anomalies": len([s for s in anomalies if s.strength >= 0.7]),
                "concentration_signals": [
                    self._signal(s) for s in signals if s.kind == SignalKind.CONCENTRATION
                ][:4],
            },
        }

    # ------------------------------------------------------------- helpers
    def _kpi(self, k: KPI) -> dict[str, Any]:
        return {
            "id": k.id,
            "name": k.name,
            "expression": k.expression,
            "unit": k.unit,
            "current": k.current_value,
            "previous": k.previous_value,
            "growth_pct": k.growth_pct,
            "trend": k.trend,
            "history_tail": k.sparkline[-self.history_tail:],
            "history_labels": k.sparkline_labels[-self.history_tail:],
        }

    @staticmethod
    def _signal(s: AnalyticsSignal) -> dict[str, Any]:
        return {"id": s.id, "kind": s.kind.value, "kpi": s.kpi_name,
                "strength": s.strength, **s.stats}

    @staticmethod
    def limitations(profiles: list[TableProfile], kpis: list[KPI]) -> dict[str, Any]:
        """Deterministic dataset limitations: which analysis dimensions the
        uploaded data does and does not support. Purely schema facts — the
        reasoning layer uses them to say what CANNOT be analysed."""
        concepts = {c.concept for p in profiles for c in p.columns}
        concepts |= {p.entity for p in profiles}
        has_geo = any(c.semantic_type == SemanticType.GEO
                      for p in profiles for c in p.columns)
        segmentation_cols = [
            c.name for p in profiles for c in p.columns
            if c.role == ColumnRole.DIMENSION
        ]
        missing, available = [], []
        for dim in ANALYSIS_DIMENSIONS:
            present = bool(concepts & dim["concepts"]) or \
                (dim["dimension"] == "geography" and has_geo)
            (available if present else missing).append(
                {"dimension": dim["dimension"]} if present
                else {"dimension": dim["dimension"], "impact": dim["impact"]})
        if not segmentation_cols:
            missing.append({"dimension": "segmentation",
                            "impact": "Segment-level analysis unavailable: no "
                                      "categorical dimension columns present."})
        # external variables can never come from an internal upload
        missing.append({"dimension": "external_variables",
                        "impact": "External factors (market, competition, "
                                  "macroeconomics, pricing environment) are not in "
                                  "the dataset and cannot be assessed."})
        history = max((len(k.sparkline) for k in kpis), default=0)
        return {
            "available_dimensions": sorted(d["dimension"] for d in available),
            "missing_dimensions": missing,
            "observed_history_periods": history,
            "segmentation_columns": segmentation_cols[:10],
        }

    @staticmethod
    def _issue_counts(quality: QualityReport) -> dict[str, int]:
        counts: dict[str, int] = {}
        for i in quality.issues:
            counts[i.kind] = counts.get(i.kind, 0) + 1
        return counts

    @staticmethod
    def health_score(kpis: list[KPI], signals: list[AnalyticsSignal], quality: QualityReport) -> float:
        """Deterministic composite metric (a computed fact, not narrative)."""
        score = 70.0
        trended = [k for k in kpis if k.growth_pct is not None]
        if trended:
            avg_growth = sum(k.growth_pct for k in trended) / len(trended)
            score += max(min(avg_growth, 15), -25)
        score -= 4 * len([s for s in signals if s.kind == SignalKind.ANOMALY and s.strength >= 0.7])
        score += (quality.overall_score - 70) * 0.2
        return round(max(min(score, 98), 5), 1)

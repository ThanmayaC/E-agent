"""Deterministic recommendation engine.

Every recommendation here is derived BY RULE from a deterministic finding and
cites the evidence that triggered it — never from LLM narrative, never
generic. The rules map measurable conditions to data-remediation actions:

    high/critical data-quality issue      -> improve data quality (that issue)
    forecast confidence below threshold   -> collect more historical observations
    strong anomaly signal                 -> investigate the anomaly
    missing analysis dimension            -> provide the data that unlocks it

Business-strategy recommendations remain the job of the LLM reasoning layer,
which must ground them in cited evidence.
"""
from __future__ import annotations

from typing import Any

from app.domain.entities import (
    AnalyticsSignal, DeterministicRecommendation, Forecast, QualityReport,
)
from app.domain.enums import SignalKind

LOW_FORECAST_CONFIDENCE = 0.6
STRONG_ANOMALY = 0.7
MAX_RECOMMENDATIONS = 12


class RecommendationEngine:
    def derive(self, quality: QualityReport, forecasts: list[Forecast],
               signals: list[AnalyticsSignal],
               limitations: dict[str, Any]) -> list[DeterministicRecommendation]:
        recs: list[DeterministicRecommendation] = []
        recs += self._from_quality(quality)
        recs += self._from_forecasts(forecasts)
        recs += self._from_anomalies(signals)
        recs += self._from_limitations(limitations)
        recs.sort(key=lambda r: (r.priority, r.id))
        return recs[:MAX_RECOMMENDATIONS]

    # ------------------------------------------------------------- rules
    @staticmethod
    def _from_quality(quality: QualityReport) -> list[DeterministicRecommendation]:
        out = []
        seen: set[str] = set()
        for i in quality.issues:
            if i.severity.value not in ("high", "critical"):
                continue
            key = f"{i.kind}:{i.dataset_id}"
            if key in seen:
                continue
            seen.add(key)
            where = f"'{i.column}' in {i.dataset_id}" if i.column else i.dataset_id
            out.append(DeterministicRecommendation(
                id=f"rec:quality:{key}",
                action=f"Improve data quality: resolve {i.kind.replace('_', ' ')} "
                       f"in {where} ({i.count} occurrence(s)).",
                trigger=f"{i.severity.value}-severity {i.kind} issue detected",
                evidence_ids=[f"quality:{i.kind}:{i.dataset_id}"],
                priority=1 if i.severity.value == "critical" else 2))
        return out

    @staticmethod
    def _from_forecasts(forecasts: list[Forecast]) -> list[DeterministicRecommendation]:
        out = []
        for f in forecasts:
            if f.status == "ok" and f.confidence >= LOW_FORECAST_CONFIDENCE:
                continue
            reasons = "; ".join(f.validation) or \
                f"forecast confidence {f.confidence:.0%} is below {LOW_FORECAST_CONFIDENCE:.0%}"
            out.append(DeterministicRecommendation(
                id=f"rec:forecast:{f.kpi_id}",
                action=f"Collect additional historical observations for "
                       f"'{f.kpi_name}' to make its forecast reliable.",
                trigger=reasons,
                evidence_ids=[f"forecast:{f.kpi_id}"],
                priority=2))
        return out

    @staticmethod
    def _from_anomalies(signals: list[AnalyticsSignal]) -> list[DeterministicRecommendation]:
        out = []
        for s in signals:
            if s.kind != SignalKind.ANOMALY or s.strength < STRONG_ANOMALY:
                continue
            period = s.stats.get("period") or s.stats.get("label") or ""
            at = f" at {period}" if period else ""
            out.append(DeterministicRecommendation(
                id=f"rec:anomaly:{s.id}",
                action=f"Investigate the anomaly in '{s.kpi_name}'{at} "
                       f"(strength {s.strength:.2f}).",
                trigger=f"anomaly signal strength {s.strength:.2f} >= {STRONG_ANOMALY}",
                evidence_ids=[s.id],
                priority=1))
        return out

    @staticmethod
    def _from_limitations(limitations: dict[str, Any]) -> list[DeterministicRecommendation]:
        out = []
        for m in limitations.get("missing_dimensions", []):
            dim = m.get("dimension", "")
            if dim == "external_variables":
                continue  # cannot be remediated by an internal upload
            out.append(DeterministicRecommendation(
                id=f"rec:data:{dim}",
                action=f"Provide {dim}-level data to unlock the analysis that "
                       f"is currently unavailable.",
                trigger=m.get("impact", f"no {dim} data present"),
                evidence_ids=[],
                priority=3))
        return out

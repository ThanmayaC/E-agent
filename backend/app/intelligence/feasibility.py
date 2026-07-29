"""Analysis feasibility — what the supplied data can actually support.

The platform used to run every analysis it owned code for, then narrate the
result. That produces confident answers to questions the data cannot answer:
a period-over-period comparison against a three-day trailing bucket, a forecast
from a handful of points, a "root cause" for an artifact.

This module runs BEFORE any narrative and answers, per analysis type: is it
supported, what does it require, what was actually observed, and — when it is
not supported — why. Unsupported analyses are then withheld from the reasoning
context entirely, which is a stronger guarantee than instructing a model not to
mention them: it cannot narrate what it never received.

Thresholds are the ones the existing engines already enforce, named in one
place so the report can quote the requirement it failed.
"""
from __future__ import annotations

from typing import Any

from app.domain.entities import KPI, TableProfile
from app.domain.enums import ColumnRole
from app.intelligence.forecasting.engine import MIN_HISTORY
from app.intelligence.timeseries.detector import PeriodCoverage

# Minimum COMPLETE periods each analysis needs to be meaningful.
MIN_PERIODS_COMPARISON = 2      # current vs previous
MIN_PERIODS_TREND = 4           # a slope needs more than a segment
MIN_PERIODS_ANOMALY = 4         # baseline of >=3 plus the point under test
MIN_PERIODS_SEASONALITY = 8     # two cycles of the shortest period the engine fits
MIN_PERIODS_FORECAST_LOW = 4    # below this no forecast is emitted at all
MIN_PERIODS_FORECAST_OK = MIN_HISTORY


class AnalysisFeasibility:
    """Decides which analyses the supplied datasets can support."""

    def assess(self, profiles: list[TableProfile], kpis: list[KPI],
               coverage: dict[str, PeriodCoverage] | None = None) -> dict[str, Any]:
        coverage = coverage or {}
        if coverage:
            complete = max((c.complete_periods for c in coverage.values()), default=0)
            observed = max((c.periods for c in coverage.values()), default=0)
            grain = next((c.grain for c in coverage.values() if c.grain), "")
            excluded = [p.describe() for c in coverage.values() for p in c.excluded]
        else:
            # A resumed pipeline reloads KPIs from disk but not the in-memory
            # coverage, so reconstruct from the provenance each KPI carries.
            complete, observed, grain, excluded = self._from_kpis(kpis)
        has_measures = any(k.growth_pct is not None or k.current_value is not None
                           for k in kpis)
        dimensions = [f"{p.name}.{c.name}" for p in profiles for c in p.columns
                      if c.role == ColumnRole.DIMENSION and 1 < c.distinct_count <= 50]

        checks = [
            self._check("period_comparison", complete, MIN_PERIODS_COMPARISON, grain,
                        "compare the latest period against the one before it"),
            self._check("trend", complete, MIN_PERIODS_TREND, grain,
                        "fit a direction over time"),
            self._check("anomaly_detection", complete, MIN_PERIODS_ANOMALY, grain,
                        "score the latest period against a baseline"),
            self._check("seasonality", complete, MIN_PERIODS_SEASONALITY, grain,
                        "separate a repeating cycle from the trend"),
            self._check("forecast", complete, MIN_PERIODS_FORECAST_LOW, grain,
                        "project future periods"),
        ]
        forecast = next(c for c in checks if c["analysis"] == "forecast")
        if forecast["supported"] and complete < MIN_PERIODS_FORECAST_OK:
            forecast["qualified"] = True
            forecast["reason"] = (
                f"{complete} complete {grain} period(s) is enough to project but "
                f"below the {MIN_PERIODS_FORECAST_OK} this platform requires for a "
                f"trusted forecast — results are labelled low confidence")

        checks.append({
            "analysis": "segmentation",
            "supported": bool(dimensions),
            "requirement": "at least one categorical dimension column",
            "observed": f"{len(dimensions)} dimension column(s)",
            "reason": "" if dimensions else
                      "no categorical dimension column was detected, so results "
                      "cannot be broken down by segment",
            "detail": dimensions[:10],
        })
        checks.append({
            "analysis": "cross_dataset_comparison",
            "supported": len(profiles) > 1,
            "requirement": "two or more related datasets",
            "observed": f"{len(profiles)} dataset(s)",
            "reason": "" if len(profiles) > 1 else
                      "only one dataset was supplied, so nothing can be compared "
                      "across sources",
        })
        if not has_measures:
            for c in checks:
                if c["analysis"] in ("period_comparison", "trend", "anomaly_detection",
                                     "seasonality", "forecast"):
                    c["supported"] = False
                    c["reason"] = "no additive measure column was identified in this data"

        return {
            "grain": grain or "none",
            "periods_observed": observed,
            "complete_periods": complete,
            "excluded_partial_periods": excluded,
            "datasets": len(profiles),
            "checks": checks,
            "supported": sorted(c["analysis"] for c in checks if c["supported"]),
            "unsupported": sorted(c["analysis"] for c in checks if not c["supported"]),
        }

    @staticmethod
    def _from_kpis(kpis: list[KPI]) -> tuple[int, int, str, list[dict]]:
        """Rebuild coverage facts from the provenance stored on each KPI."""
        complete = max((int((k.calculation or {}).get("complete_periods", 0) or 0)
                        for k in kpis), default=0)
        if not complete:
            complete = max((len(k.sparkline) for k in kpis), default=0)
        grain = next((k.period_grain for k in kpis if k.period_grain), "")
        excluded: list[dict] = []
        seen: set[str] = set()
        for k in kpis:
            for item in (k.calculation or {}).get("excluded_periods", []) or []:
                label = item.get("period") if isinstance(item, dict) else str(item)
                if label and label not in seen:
                    seen.add(label)
                    excluded.append(item if isinstance(item, dict) else {"period": label})
        return complete, complete + len(excluded), grain, excluded

    @staticmethod
    def _check(analysis: str, complete: int, required: int, grain: str,
               purpose: str) -> dict[str, Any]:
        ok = complete >= required
        return {
            "analysis": analysis,
            "supported": ok,
            "requirement": f"{required} complete {grain or 'reporting'} period(s)",
            "observed": f"{complete} complete {grain or 'reporting'} period(s)",
            "reason": "" if ok else (
                f"cannot {purpose}: {complete} complete {grain or 'reporting'} "
                f"period(s) available, {required} required"),
        }


def supported(feasibility: dict[str, Any], analysis: str) -> bool:
    """Whether one named analysis may be presented at all."""
    return analysis in (feasibility.get("supported") or [])

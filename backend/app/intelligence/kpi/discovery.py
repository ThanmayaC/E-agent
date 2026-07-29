"""Automatic KPI discovery — no configuration.

Derives KPIs from measure columns, status columns (success/failure rates),
identifier counts, and time-series aggregates.
"""
from __future__ import annotations

import math
import re
import uuid

import pandas as pd

from app.domain.entities import KPI, TableProfile
from app.domain.enums import BusinessConcept, ColumnRole, SemanticType
from app.intelligence.semantics.ontology import METRIC_CONCEPTS
from app.intelligence.timeseries.detector import (
    PeriodCoverage, drop_partial, period_coverage, resample_series,
)

SUCCESS_TOKENS = {"success", "succeeded", "completed", "complete", "captured", "paid", "settled", "approved", "ok", "s"}
FAILURE_TOKENS = {"failure", "failed", "fail", "declined", "rejected", "error", "timeout", "cancelled", "canceled", "f"}


def _period_label(ts, rule: str) -> str:
    """Human-readable label for the period a KPI value describes."""
    if rule == "MS":
        return pd.Timestamp(ts).strftime("%Y-%m")
    if rule == "YS":
        return pd.Timestamp(ts).strftime("%Y")
    if rule == "QS":
        return str(pd.Period(ts, freq="Q"))
    return pd.Timestamp(ts).strftime("%Y-%m-%d")


class KPIDiscovery:
    def __init__(self) -> None:
        # Period coverage per dataset, so the report can explain which periods
        # were analysed and which were set aside.
        self.coverage: dict[str, PeriodCoverage] = {}

    def discover(self, profiles: list[TableProfile], frames: dict[str, pd.DataFrame]) -> list[KPI]:
        kpis: list[KPI] = []
        for p in profiles:
            df = frames.get(p.dataset_id)
            if df is None or df.empty:
                continue
            # Completeness depends only on the time column, so it is assessed
            # once per table and reused by every KPI derived from it.
            cov = (period_coverage(df, p.time_column)
                   if p.time_column and p.time_column in df else PeriodCoverage())
            self.coverage[p.dataset_id] = cov
            kpis.extend(self._measure_kpis(p, df, cov))
            kpis.extend(self._rate_kpis(p, df, cov))
            kpis.extend(self._entity_count_kpis(p, df, cov))
        return self._rank(self._deduplicate(kpis))

    @staticmethod
    def _deduplicate(kpis: list[KPI]) -> list[KPI]:
        """Collapse KPIs that measure the same thing twice.

        Several columns can identify the same entity — a payer's VPA and their
        mobile number both count customers — which otherwise yields two
        identical "Active Customers" rows. Identical measurements collapse to
        the most confident one; genuinely different ones keep their column in
        the name so the reader can tell them apart.
        """
        best: dict[tuple, KPI] = {}
        for k in kpis:
            key = (k.dataset_id, k.name, k.current_value, k.concept)
            existing = best.get(key)
            if existing is None or k.confidence > existing.confidence:
                best[key] = k
        survivors = list(best.values())

        by_name: dict[str, list[KPI]] = {}
        for k in survivors:
            by_name.setdefault(k.name, []).append(k)
        for name, group in by_name.items():
            if len(group) > 1:
                for k in group:
                    if k.column:
                        k.name = f"{name} ({k.column})"
        return survivors

    # -------------------------------------------------------- measure KPIs
    def _measure_kpis(self, p: TableProfile, df: pd.DataFrame,
                      cov: PeriodCoverage) -> list[KPI]:
        kpis = []
        for col in p.columns:
            if col.role != ColumnRole.MEASURE:
                continue
            values = pd.to_numeric(df[col.name], errors="coerce").dropna()
            if values.empty:
                continue
            concept = col.concept if col.concept in METRIC_CONCEPTS else BusinessConcept.VALUE
            unit = "%" if col.semantic_type == SemanticType.PERCENTAGE else (
                "currency" if col.semantic_type == SemanticType.CURRENCY else "")
            agg = "mean" if col.semantic_type == SemanticType.PERCENTAGE else "sum"
            kpi = KPI(
                id=uuid.uuid4().hex[:10],
                name=self._pretty(col.name, concept),
                concept=concept,
                dataset_id=p.dataset_id,
                expression=f"{agg.upper()}({col.name})",
                column=col.name,
                unit=unit,
                time_column=p.time_column,
                contributing_rows=int(len(values)),
                confidence=max(col.concept_confidence, 0.5),
            )
            self._fill_timeseries(kpi, p, df, col.name, agg, cov)
            self._finalize(kpi, p, cov, agg,
                           whole=float(values.mean() if agg == "mean" else values.sum()))
            kpis.append(kpi)
        return kpis

    # ----------------------------------------------------------- rate KPIs
    def _rate_kpis(self, p: TableProfile, df: pd.DataFrame,
                   cov: PeriodCoverage) -> list[KPI]:
        kpis = []
        for col in p.columns:
            if col.semantic_type != SemanticType.STATUS:
                continue
            lowered = df[col.name].dropna().astype(str).str.strip().str.lower()
            if lowered.empty:
                continue
            success = lowered.isin(SUCCESS_TOKENS)
            failure = lowered.isin(FAILURE_TOKENS)
            if not success.any() and not failure.any():
                continue
            rate = float(success.mean()) * 100 if success.any() else (1 - float(failure.mean())) * 100
            for name, value in [("Success Rate", rate), ("Failure Rate", 100 - rate)]:
                kpi = KPI(
                    id=uuid.uuid4().hex[:10],
                    name=f"{p.entity.value} {name}" if p.entity is not BusinessConcept.UNKNOWN else name,
                    concept=BusinessConcept.CONVERSION,
                    dataset_id=p.dataset_id,
                    expression=f"{name.upper().replace(' ', '_')}({col.name})",
                    column=col.name, unit="%",
                    time_column=p.time_column,
                    contributing_rows=int(len(lowered)),
                    confidence=0.8,
                )
                self._fill_rate_timeseries(kpi, p, df, col.name, cov,
                                           positive=(name == "Success Rate"))
                self._finalize(kpi, p, cov, "mean", whole=value)
                kpis.append(kpi)
        return kpis

    # ---------------------------------------------------- entity count KPIs
    def _entity_count_kpis(self, p: TableProfile, df: pd.DataFrame,
                           cov: PeriodCoverage) -> list[KPI]:
        kpis = []
        for col in p.columns:
            if col.semantic_type != SemanticType.IDENTIFIER or col.concept is BusinessConcept.UNKNOWN:
                continue
            if col.concept not in (BusinessConcept.CUSTOMER, BusinessConcept.MERCHANT, BusinessConcept.USER,
                                   BusinessConcept.TRANSACTION, BusinessConcept.ORDER, BusinessConcept.PRODUCT):
                continue
            distinct = int(df[col.name].nunique())
            noun = col.concept.value + ("s" if not col.concept.value.endswith("s") else "")
            # counting a dimension table by its signup/onboard date is a cohort
            # metric ("new per period"), not a running total
            cohort = bool(p.time_column) and bool(
                re.search(r"signup|onboard|creat|join|enrol|regist", p.time_column, re.I))
            if col.is_pk_candidate:
                name = f"New {noun} per period" if cohort else f"Total {noun}"
            else:
                name = f"Active {noun}"
            kpi = KPI(
                id=uuid.uuid4().hex[:10],
                name=name,
                concept=col.concept,
                dataset_id=p.dataset_id,
                expression=f"COUNT(DISTINCT {col.name})",
                column=col.name,
                time_column=p.time_column,
                contributing_rows=int(len(df)),
                confidence=col.concept_confidence,
            )
            if p.time_column and p.time_column in df:
                self._fill_distinct_timeseries(kpi, df, p.time_column, col.name, cov)
            self._finalize(kpi, p, cov, "distinct", whole=float(distinct))
            kpis.append(kpi)
        return kpis

    # ------------------------------------------------------------ helpers
    def _fill_timeseries(self, kpi: KPI, p: TableProfile, df: pd.DataFrame, col: str,
                         agg: str, cov: PeriodCoverage) -> None:
        if not p.time_column or p.time_column not in df:
            return
        series = resample_series(df, p.time_column, col, agg, coverage=cov,
                                 complete_only=True)
        self._apply_series(kpi, series, cov)

    def _fill_rate_timeseries(self, kpi: KPI, p: TableProfile, df: pd.DataFrame, col: str,
                              cov: PeriodCoverage, positive: bool) -> None:
        if not p.time_column or p.time_column not in df:
            return
        tokens = SUCCESS_TOKENS if positive else FAILURE_TOKENS
        temp = df[[p.time_column]].copy()
        temp["_hit"] = df[col].astype(str).str.strip().str.lower().isin(tokens).astype(float) * 100
        series = resample_series(temp, p.time_column, "_hit", agg="mean", coverage=cov,
                                 complete_only=True)
        self._apply_series(kpi, series, cov)

    def _fill_distinct_timeseries(self, kpi: KPI, df: pd.DataFrame, time_col: str,
                                  id_col: str, cov: PeriodCoverage) -> None:
        data = df[[time_col, id_col]].copy()
        data[time_col] = pd.to_datetime(data[time_col], errors="coerce", format="mixed")
        data = data.dropna()
        if data.empty:
            return
        rule = cov.rule or "MS"
        series = data.set_index(time_col).groupby(pd.Grouper(freq=rule))[id_col].nunique().astype(float)
        self._apply_series(kpi, drop_partial(series[series > 0], cov), cov)

    @staticmethod
    def _apply_series(kpi: KPI, series: pd.Series, cov: PeriodCoverage) -> None:
        """Attach the history. ``series`` holds COMPLETE periods only, so a
        period-over-period comparison here is always like-for-like."""
        if series.empty:
            return
        tail = series.tail(24)
        kpi.sparkline = [round(float(v), 2) for v in tail.tolist()]
        kpi.sparkline_labels = [idx.strftime("%Y-%m-%d") for idx in tail.index]
        kpi.period_grain = cov.grain
        kpi.excluded_periods = [pp.label for pp in cov.excluded]

        kpi.current_value = round(float(series.iloc[-1]), 2)
        kpi.current_period_label = _period_label(series.index[-1], cov.rule)
        kpi.basis = "period_over_period"

        if len(series) < 2:
            # One complete period is a measurement, never a comparison.
            kpi.comparison_unavailable_reason = (
                f"only {len(series)} complete {cov.grain} period is present; "
                f"a period-over-period comparison needs at least 2")
            return

        kpi.previous_value = round(float(series.iloc[-2]), 2)
        kpi.previous_period_label = _period_label(series.index[-2], cov.rule)
        if kpi.previous_value:
            kpi.growth_pct = round(
                (kpi.current_value - kpi.previous_value) / abs(kpi.previous_value) * 100, 2)
            kpi.trend = "up" if kpi.growth_pct > 1 else ("down" if kpi.growth_pct < -1 else "flat")
        else:
            kpi.comparison_unavailable_reason = (
                f"the previous period ({kpi.previous_period_label}) is zero, so a "
                f"percentage change is undefined")

    @staticmethod
    def _finalize(kpi: KPI, p: TableProfile, cov: PeriodCoverage, agg: str,
                  whole: float) -> None:
        """Guarantee every KPI carries a value and an explanation of what that
        value describes. Without a usable time axis the KPI falls back to a
        whole-dataset aggregate, and says so — it is never presented as a
        period comparison."""
        if kpi.current_value is None:
            kpi.current_value = round(float(whole), 2)
            kpi.basis = "whole_dataset"
            if not kpi.comparison_unavailable_reason:
                kpi.comparison_unavailable_reason = (
                    "no usable reporting period was detected in this dataset, so the "
                    "value covers all rows and cannot be compared over time"
                    if not p.time_column else
                    f"no complete {cov.grain or 'reporting'} period could be formed "
                    f"from '{p.time_column}'")

        kpi.calculation = {
            "expression": kpi.expression,
            "source": f"{p.name}.{kpi.column}" if kpi.column else p.name,
            "dataset_id": p.dataset_id,
            "aggregation": agg,
            "time_column": p.time_column or "",
            "period_grain": kpi.period_grain or "n/a",
            "basis": kpi.basis,
            "current_period": kpi.current_period_label or "all rows",
            "previous_period": kpi.previous_period_label or "n/a",
            "contributing_rows": kpi.contributing_rows,
            "complete_periods": cov.complete_periods,
            "excluded_periods": [pp.describe() for pp in cov.excluded],
            "growth_formula": ("(current - previous) / abs(previous) * 100"
                               if kpi.growth_pct is not None else "not computed"),
            "unavailable_reason": kpi.comparison_unavailable_reason,
        }

    @staticmethod
    def _pretty(col_name: str, concept: BusinessConcept) -> str:
        base = col_name.replace("_", " ").strip().title()
        if concept is not BusinessConcept.UNKNOWN and concept.value.lower() not in base.lower():
            return f"{concept.value} ({base})"
        return base

    @staticmethod
    def _rank(kpis: list[KPI]) -> list[KPI]:
        def key(k: KPI):
            has_ts = 1 if k.sparkline else 0
            magnitude = math.log10(1 + abs(k.current_value or 0))
            return (has_ts, round(k.confidence, 1), magnitude)
        return sorted(kpis, key=key, reverse=True)

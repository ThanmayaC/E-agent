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
from app.intelligence.timeseries.detector import resample_series

SUCCESS_TOKENS = {"success", "succeeded", "completed", "complete", "captured", "paid", "settled", "approved", "ok", "s"}
FAILURE_TOKENS = {"failure", "failed", "fail", "declined", "rejected", "error", "timeout", "cancelled", "canceled", "f"}


class KPIDiscovery:
    def discover(self, profiles: list[TableProfile], frames: dict[str, pd.DataFrame]) -> list[KPI]:
        kpis: list[KPI] = []
        for p in profiles:
            df = frames.get(p.dataset_id)
            if df is None or df.empty:
                continue
            kpis.extend(self._measure_kpis(p, df))
            kpis.extend(self._rate_kpis(p, df))
            kpis.extend(self._entity_count_kpis(p, df))
        return self._rank(kpis)

    # -------------------------------------------------------- measure KPIs
    def _measure_kpis(self, p: TableProfile, df: pd.DataFrame) -> list[KPI]:
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
                confidence=max(col.concept_confidence, 0.5),
            )
            self._fill_timeseries(kpi, p, df, col.name, agg)
            if kpi.current_value is None:
                kpi.current_value = round(float(values.mean() if agg == "mean" else values.sum()), 2)
            kpis.append(kpi)
        return kpis

    # ----------------------------------------------------------- rate KPIs
    def _rate_kpis(self, p: TableProfile, df: pd.DataFrame) -> list[KPI]:
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
                    current_value=round(value, 2),
                    confidence=0.8,
                )
                self._fill_rate_timeseries(kpi, p, df, col.name, positive=(name == "Success Rate"))
                kpis.append(kpi)
        return kpis

    # ---------------------------------------------------- entity count KPIs
    def _entity_count_kpis(self, p: TableProfile, df: pd.DataFrame) -> list[KPI]:
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
                current_value=float(distinct),
                confidence=col.concept_confidence,
            )
            if p.time_column and p.time_column in df:
                self._fill_distinct_timeseries(kpi, df, p.time_column, col.name)
            kpis.append(kpi)
        return kpis

    # ------------------------------------------------------------ helpers
    def _fill_timeseries(self, kpi: KPI, p: TableProfile, df: pd.DataFrame, col: str, agg: str) -> None:
        if not p.time_column or p.time_column not in df:
            return
        series = resample_series(df, p.time_column, col, agg)
        self._apply_series(kpi, series)

    def _fill_rate_timeseries(self, kpi: KPI, p: TableProfile, df: pd.DataFrame, col: str, positive: bool) -> None:
        if not p.time_column or p.time_column not in df:
            return
        tokens = SUCCESS_TOKENS if positive else FAILURE_TOKENS
        temp = df[[p.time_column]].copy()
        temp["_hit"] = df[col].astype(str).str.strip().str.lower().isin(tokens).astype(float) * 100
        series = resample_series(temp, p.time_column, "_hit", agg="mean")
        self._apply_series(kpi, series)

    def _fill_distinct_timeseries(self, kpi: KPI, df: pd.DataFrame, time_col: str, id_col: str) -> None:
        data = df[[time_col, id_col]].copy()
        data[time_col] = pd.to_datetime(data[time_col], errors="coerce", format="mixed")
        data = data.dropna()
        if data.empty:
            return
        series = data.set_index(time_col).groupby(pd.Grouper(freq="MS"))[id_col].nunique().astype(float)
        self._apply_series(kpi, series[series > 0])

    @staticmethod
    def _apply_series(kpi: KPI, series: pd.Series) -> None:
        if len(series) < 2:
            return
        kpi.sparkline = [round(float(v), 2) for v in series.tail(24).tolist()]
        kpi.sparkline_labels = [idx.strftime("%Y-%m-%d") for idx in series.tail(24).index]
        kpi.current_value = round(float(series.iloc[-1]), 2)
        kpi.previous_value = round(float(series.iloc[-2]), 2)
        if kpi.previous_value:
            kpi.growth_pct = round((kpi.current_value - kpi.previous_value) / abs(kpi.previous_value) * 100, 2)
            kpi.trend = "up" if kpi.growth_pct > 1 else ("down" if kpi.growth_pct < -1 else "flat")

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

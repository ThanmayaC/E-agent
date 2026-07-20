"""Column profiling and automatic data type / semantic type detection."""
from __future__ import annotations

import re

import numpy as np
import pandas as pd

from app.domain.entities import ColumnProfile, TableProfile
from app.domain.enums import ColumnRole, SemanticType
from app.intelligence.connectors.excel import ExtractedTable

CURRENCY_HINTS = re.compile(r"(amount|amt|value|revenue|price|cost|fee|gmv|spend|salary|charge|settle)", re.I)
PERCENT_HINTS = re.compile(r"(pct|percent|rate|ratio|share|%)", re.I)
ID_HINTS = re.compile(r"(^id$|_id$|^id_|_id_|_no$|_num$|number$|_code$|^code|uuid|guid)", re.I)
DATE_HINTS = re.compile(r"(date|_dt$|^dt_|time|month|year|week|day|period|timestamp)", re.I)
STATUS_HINTS = re.compile(r"(status|state|flag|result|outcome)", re.I)
GEO_HINTS = re.compile(r"(country|region|state|city|zone|territory|geo|location|pincode|zip)", re.I)
BOOL_VALUES = {"true", "false", "yes", "no", "y", "n", "0", "1"}
CURRENCY_SYMBOL = re.compile(r"^[\s]*[₹$€£¥]")


def normalize_name(name: str) -> str:
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", str(name))
    s = re.sub(r"[^0-9a-zA-Z]+", "_", s).strip("_").lower()
    return re.sub(r"_+", "_", s)


class ColumnProfiler:
    def __init__(self, sample_rows: int = 50000, pk_threshold: float = 0.99):
        self.sample_rows = sample_rows
        self.pk_threshold = pk_threshold

    def profile_table(self, table: ExtractedTable, dataset_id: str) -> TableProfile:
        df = table.df.head(self.sample_rows)
        columns = [self._profile_column(df, col) for col in df.columns]
        self._mark_primary_key(columns, len(df))
        return TableProfile(
            dataset_id=dataset_id,
            name=table.name,
            source_file=table.source_file,
            source_sheet=table.source_sheet,
            row_count=len(table.df),
            column_count=len(df.columns),
            columns=columns,
        )

    # ---------------------------------------------------------------- column
    def _profile_column(self, df: pd.DataFrame, col: str) -> ColumnProfile:
        series = df[col]
        coerced, sem_type = self._coerce(series, col)
        non_null = coerced.dropna()
        n = max(len(series), 1)
        distinct = int(non_null.nunique())
        profile = ColumnProfile(
            name=str(col),
            normalized_name=normalize_name(col),
            dtype=str(coerced.dtype),
            semantic_type=sem_type,
            null_count=int(series.isna().sum()),
            null_pct=round(float(series.isna().mean()) * 100, 2),
            distinct_count=distinct,
            unique_ratio=round(distinct / max(len(non_null), 1), 4),
            samples=[self._safe(v) for v in non_null.head(5).tolist()],
        )
        if pd.api.types.is_numeric_dtype(coerced) and len(non_null):
            profile.min_value = str(self._safe(non_null.min()))
            profile.max_value = str(self._safe(non_null.max()))
            profile.mean_value = round(float(non_null.mean()), 4)
            profile.std_value = round(float(non_null.std() or 0), 4)
        elif sem_type in (SemanticType.DATE, SemanticType.DATETIME) and len(non_null):
            profile.min_value = str(non_null.min())
            profile.max_value = str(non_null.max())
        profile.role = self._infer_role(profile)
        return profile

    def _coerce(self, series: pd.Series, col: str) -> tuple[pd.Series, SemanticType]:
        name = str(col)
        non_null = series.dropna()
        if non_null.empty:
            return series, SemanticType.UNKNOWN

        # datetimes
        if pd.api.types.is_datetime64_any_dtype(series):
            return series, self._date_or_datetime(series)
        if DATE_HINTS.search(name) or self._looks_datelike(non_null):
            parsed = pd.to_datetime(series, errors="coerce", format="mixed", dayfirst=False)
            if parsed.notna().mean() >= 0.7:
                return parsed, self._date_or_datetime(parsed)

        # numerics (incl. currency-formatted strings like "$1,200.50")
        numeric = pd.to_numeric(
            non_null.astype(str).str.replace(r"[₹$€£¥,\s]", "", regex=True).str.rstrip("%"),
            errors="coerce",
        )
        if numeric.notna().mean() >= 0.85:
            full = pd.to_numeric(
                series.astype(str).str.replace(r"[₹$€£¥,\s]", "", regex=True).str.rstrip("%"),
                errors="coerce",
            )
            has_pct = PERCENT_HINTS.search(name) or non_null.astype(str).str.endswith("%").mean() > 0.5
            has_currency = CURRENCY_HINTS.search(name) or non_null.astype(str).str.match(CURRENCY_SYMBOL.pattern).mean() > 0.5
            if ID_HINTS.search(name) and (full.dropna() % 1 == 0).all():
                return full, SemanticType.IDENTIFIER
            if has_pct:
                return full, SemanticType.PERCENTAGE
            if has_currency:
                return full, SemanticType.CURRENCY
            return full, SemanticType.MEASURE

        # booleans
        lowered = non_null.astype(str).str.strip().str.lower()
        if lowered.isin(BOOL_VALUES).all() and lowered.nunique() <= 2:
            return series, SemanticType.BOOLEAN

        # strings
        if ID_HINTS.search(name):
            return series, SemanticType.IDENTIFIER
        if STATUS_HINTS.search(name) and lowered.nunique() <= 20:
            return series, SemanticType.STATUS
        if GEO_HINTS.search(name):
            return series, SemanticType.GEO
        uniq = lowered.nunique() / len(lowered)
        if lowered.nunique() <= 50 or uniq < 0.05:
            return series, SemanticType.CATEGORY
        if uniq > 0.9 and lowered.str.match(r"^[A-Z0-9\-_/]+$", case=False).mean() > 0.8:
            return series, SemanticType.CODE
        return series, SemanticType.TEXT

    @staticmethod
    def _looks_datelike(non_null: pd.Series) -> bool:
        sample = non_null.astype(str).head(20)
        pattern = r"^\d{4}-\d{1,2}(-\d{1,2})?|^\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|^[A-Za-z]{3,9}[- ]\d{2,4}$"
        return sample.str.match(pattern).mean() > 0.6

    @staticmethod
    def _date_or_datetime(series: pd.Series) -> SemanticType:
        s = series.dropna()
        if len(s) and (s.dt.hour.fillna(0) != 0).any():
            return SemanticType.DATETIME
        return SemanticType.DATE

    @staticmethod
    def _infer_role(p: ColumnProfile) -> ColumnRole:
        if p.semantic_type == SemanticType.IDENTIFIER:
            return ColumnRole.ATTRIBUTE  # PK/FK assigned later
        if p.semantic_type in (SemanticType.DATE, SemanticType.DATETIME):
            return ColumnRole.TIME_DIMENSION
        if p.semantic_type in (SemanticType.MEASURE, SemanticType.CURRENCY, SemanticType.PERCENTAGE):
            return ColumnRole.MEASURE
        if p.semantic_type in (SemanticType.CATEGORY, SemanticType.STATUS, SemanticType.GEO, SemanticType.BOOLEAN):
            return ColumnRole.DIMENSION
        return ColumnRole.ATTRIBUTE

    def _mark_primary_key(self, columns: list[ColumnProfile], row_count: int) -> None:
        if row_count == 0:
            return
        for col in columns:
            if (
                col.semantic_type in (SemanticType.IDENTIFIER, SemanticType.CODE)
                and col.unique_ratio >= self.pk_threshold
                and col.null_pct < 1.0
            ):
                col.is_pk_candidate = True
                col.role = ColumnRole.PRIMARY_KEY

    @staticmethod
    def _safe(v):
        if isinstance(v, (np.integer,)):
            return int(v)
        if isinstance(v, (np.floating,)):
            return float(v)
        return str(v) if not isinstance(v, (int, float, str, bool)) else v

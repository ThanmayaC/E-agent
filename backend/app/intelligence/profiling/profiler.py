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
# Identifier hints must not depend on snake_case: real schemas write
# `purposecode`, `payerseqnum`, `prdmobile` with no separators, and an
# underscore-anchored pattern silently lets those through as "measures".
ID_HINTS = re.compile(
    r"(^id$|_id$|^id_|_id_|_no$|_num$|num$|number$|_code$|code$|^code|uuid|guid"
    r"|seq|mcc|mobile|msisdn|phone|msid|imei|vpa|refno|reference$|addr|mode$)", re.I)
# Names that genuinely denote something additive. Used to protect real
# measures from the low-cardinality heuristic below (an order `qty` of 1-20 is
# a measure; a `purposecode` of 13 values is not).
MEASURE_HINTS = re.compile(
    r"(amount|amt|qty|quantity|units?|count|total|sum|value|price|cost|fee|revenue"
    r"|spend|score|duration|seconds|minutes|hours|days|weight|size|balance|volume"
    r"|gmv|salary|charge|settle|income|profit|margin|discount|tax)", re.I)
# A numeric column with at most this many distinct values, and no measure-like
# name, is a coded dimension rather than something worth summing.
MAX_CODE_CARDINALITY = 50
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
        self._last_exclusion = ""

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
        self._last_exclusion = ""
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
        profile.exclusion_reason = self._last_exclusion
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
                hint = ID_HINTS.search(name).group(0)
                self._last_exclusion = (
                    f"name matches the identifier/code pattern '{hint}' and every "
                    f"value is a whole number — treated as an identifier, not summed")
                return full, SemanticType.IDENTIFIER
            if has_pct:
                return full, SemanticType.PERCENTAGE
            if has_currency:
                return full, SemanticType.CURRENCY
            # Not every number is a quantity. Summing phone numbers, category
            # codes or sequence numbers produces confident nonsense, so a
            # column must look additive before it is treated as a measure.
            demoted = self._non_additive(full.dropna(), name)
            if demoted is not None:
                sem_type, reason = demoted
                self._last_exclusion = reason
                return full, sem_type
            return full, SemanticType.MEASURE

        # booleans
        lowered = non_null.astype(str).str.strip().str.lower()
        if lowered.isin(BOOL_VALUES).all() and lowered.nunique() <= 2:
            return series, SemanticType.BOOLEAN

        # strings
        if ID_HINTS.search(name):
            self._last_exclusion = (
                f"name matches the identifier/code pattern "
                f"'{ID_HINTS.search(name).group(0)}' — treated as an identifier")
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
    def _non_additive(values: pd.Series, name: str) -> tuple[SemanticType, str] | None:
        """Decide whether a numeric column is really a measure.

        Returns the type to demote to plus the reason, or None to keep it as a
        measure. Deliberately conservative: anything whose *name* says it is a
        quantity stays a measure, so the heuristics below can only catch
        columns that look like identifiers or codes on both name and values.
        """
        if values.empty:
            return None
        distinct = int(values.nunique())
        if distinct <= 1:
            return (SemanticType.CATEGORY,
                    f"constant value ({values.iloc[0]!s}) — nothing to aggregate")

        integral = bool((values % 1 == 0).all())
        measure_named = bool(MEASURE_HINTS.search(name))

        if integral and not measure_named:
            lo, hi = float(values.min()), float(values.max())
            digits = len(str(int(abs(hi))))
            unique_ratio = distinct / max(len(values), 1)

            # Phone / MSISDN / account-style numbers: fixed long width, many
            # distinct values, and no arithmetic meaning.
            if 9 <= digits <= 15 and lo >= 1e8 and distinct > 50:
                return (SemanticType.IDENTIFIER,
                        f"{digits}-digit integers with {distinct:,} distinct values — "
                        f"an identifier (phone/account/reference), not a quantity")

            # Near-unique integers behave like keys, not amounts.
            if unique_ratio > 0.95 and distinct > 100:
                return (SemanticType.IDENTIFIER,
                        f"{unique_ratio:.0%} of values are unique — behaves like an "
                        f"identifier, not a quantity")

            # A small closed set of integers is a coded dimension.
            if distinct <= MAX_CODE_CARDINALITY:
                return (SemanticType.CATEGORY,
                        f"only {distinct} distinct integer value(s) and no "
                        f"quantity-like name — a coded dimension, not an additive measure")

        return None

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

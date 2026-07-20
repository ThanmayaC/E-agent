"""Data quality engine: nulls, duplicates, outliers, drift, invalid values."""
from __future__ import annotations

import pandas as pd

from app.domain.entities import QualityIssue, QualityReport, TableProfile
from app.domain.enums import ColumnRole, SemanticType, Severity


class QualityEngine:
    def __init__(self, outlier_zscore: float = 3.0):
        self.outlier_zscore = outlier_zscore

    def assess(self, profiles: list[TableProfile], frames: dict[str, pd.DataFrame]) -> QualityReport:
        issues: list[QualityIssue] = []
        per_dataset: dict[str, float] = {}
        for p in profiles:
            df = frames.get(p.dataset_id)
            ds_issues = self._assess_dataset(p, df)
            issues.extend(ds_issues)
            per_dataset[p.dataset_id] = self._score(ds_issues, p.row_count)
        overall = round(sum(per_dataset.values()) / max(len(per_dataset), 1), 1)
        return QualityReport(overall_score=overall, issues=issues, per_dataset=per_dataset)

    def _assess_dataset(self, p: TableProfile, df: pd.DataFrame | None) -> list[QualityIssue]:
        issues: list[QualityIssue] = []
        for col in p.columns:
            if col.null_pct > 30:
                issues.append(QualityIssue(
                    dataset_id=p.dataset_id, column=col.name, kind="missing_values",
                    severity=Severity.HIGH if col.null_pct > 60 else Severity.MEDIUM,
                    count=col.null_count, detail=f"{col.null_pct}% of values missing"))
            elif col.null_pct > 5:
                issues.append(QualityIssue(
                    dataset_id=p.dataset_id, column=col.name, kind="missing_values",
                    severity=Severity.LOW, count=col.null_count, detail=f"{col.null_pct}% missing"))

        if df is None or df.empty:
            return issues

        dup_count = int(df.duplicated().sum())
        if dup_count:
            severity = Severity.HIGH if dup_count / len(df) > 0.05 else Severity.LOW
            issues.append(QualityIssue(
                dataset_id=p.dataset_id, kind="duplicate_rows", severity=severity,
                count=dup_count, detail=f"{dup_count} exact duplicate rows ({dup_count / len(df):.1%})"))

        for col in p.columns:
            if col.name not in df:
                continue
            if col.role == ColumnRole.MEASURE and col.std_value:
                values = pd.to_numeric(df[col.name], errors="coerce").dropna()
                if len(values) > 10 and values.std() > 0:
                    z = ((values - values.mean()) / values.std()).abs()
                    outliers = int((z > self.outlier_zscore).sum())
                    if outliers:
                        issues.append(QualityIssue(
                            dataset_id=p.dataset_id, column=col.name, kind="outliers",
                            severity=Severity.MEDIUM if outliers / len(values) > 0.02 else Severity.INFO,
                            count=outliers, detail=f"{outliers} values beyond {self.outlier_zscore}σ"))
                if col.semantic_type == SemanticType.CURRENCY:
                    negatives = int((pd.to_numeric(df[col.name], errors="coerce") < 0).sum())
                    if negatives:
                        issues.append(QualityIssue(
                            dataset_id=p.dataset_id, column=col.name, kind="negative_amounts",
                            severity=Severity.MEDIUM, count=negatives,
                            detail=f"{negatives} negative monetary values (refunds or errors?)"))
            if col.semantic_type in (SemanticType.DATE, SemanticType.DATETIME):
                dates = pd.to_datetime(df[col.name], errors="coerce", format="mixed").dropna()
                future = int((dates > pd.Timestamp.now() + pd.Timedelta(days=1)).sum())
                if future:
                    issues.append(QualityIssue(
                        dataset_id=p.dataset_id, column=col.name, kind="future_dates",
                        severity=Severity.MEDIUM, count=future, detail=f"{future} dates in the future"))
            if col.semantic_type == SemanticType.IDENTIFIER and col.is_pk_candidate:
                dupes = int(df[col.name].dropna().duplicated().sum())
                if dupes:
                    issues.append(QualityIssue(
                        dataset_id=p.dataset_id, column=col.name, kind="duplicate_keys",
                        severity=Severity.HIGH, count=dupes,
                        detail=f"{dupes} duplicate values in primary-key candidate"))
            # mixed formats in text columns that mostly parse as numbers
            if col.semantic_type == SemanticType.TEXT:
                as_num = pd.to_numeric(df[col.name], errors="coerce").notna().mean()
                if 0.3 < as_num < 0.85:
                    issues.append(QualityIssue(
                        dataset_id=p.dataset_id, column=col.name, kind="inconsistent_format",
                        severity=Severity.MEDIUM, count=0,
                        detail=f"mixed numeric/text content ({as_num:.0%} numeric)"))
        return issues

    @staticmethod
    def _score(issues: list[QualityIssue], row_count: int) -> float:
        penalty = {"info": 0.5, "low": 2, "medium": 6, "high": 14, "critical": 25}
        score = 100.0 - sum(penalty.get(i.severity.value, 2) for i in issues)
        return round(max(score, 5.0), 1)

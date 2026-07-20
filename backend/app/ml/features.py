"""Feature Engineering & Feature Store (03-ml-platform.md §2).

Scope-appropriate by design (ADR-008): an internal store with
Feast-compatible semantics — definitions as code, hash-addressed offline
materialization, lineage metadata — not Feast itself.

``FeatureEngineer`` is a deterministic fit/transform object. Everything it
learns from the training frame (imputation medians, category maps, kept
columns) is state on the instance, so serializing the engineer next to the
model guarantees inference applies *exactly* the training transformations —
the signature-enforcement half of "fail fast on schema drift instead of
silently predicting garbage".
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path

import numpy as np
import pandas as pd

from app.core.logging import get_logger

logger = get_logger(__name__)

MAX_ONEHOT_CARDINALITY = 10   # above this a categorical is frequency-encoded
MAX_MISSING_RATE = 0.5        # columns emptier than this carry no signal
ID_UNIQUE_RATIO = 0.98        # near-unique non-numeric columns are identifiers


@dataclass
class FeatureMatrix:
    X: np.ndarray
    feature_names: list[str]
    y: np.ndarray | None = None
    target: str | None = None
    n_rows: int = 0
    transformations: list[dict] = field(default_factory=list)
    source_hash: str = ""


class FeatureEngineer:
    """Deterministic tabular feature builder. fit_transform() on the training
    frame, transform() at inference — the fitted state is the contract."""

    def __init__(self) -> None:
        self.fitted: bool = False
        self.input_columns: list[str] = []
        self.feature_names: list[str] = []
        self._plan: list[dict] = []          # per-column transformation plan
        self._medians: dict[str, float] = {}
        self._onehot: dict[str, list[str]] = {}
        self._freq: dict[str, dict[str, float]] = {}

    # ------------------------------------------------------------------ fit
    def fit_transform(self, df: pd.DataFrame, target: str | None = None) -> FeatureMatrix:
        y = None
        if target is not None:
            if target not in df.columns:
                raise ValueError(f"target column '{target}' not in frame")
            y = self._encode_target(df[target])
            df = df.drop(columns=[target])

        self._plan, self.input_columns = [], []
        for col in df.columns:
            s = df[col]
            decision = self._decide(col, s)
            self._plan.append(decision)
            if decision["action"] != "drop":
                self.input_columns.append(col)

        self.fitted = True
        X, names = self._apply(df)
        self.feature_names = names
        return FeatureMatrix(
            X=X, feature_names=names, y=y, target=target, n_rows=len(df),
            transformations=list(self._plan),
            source_hash=frame_hash(df))

    def transform(self, df: pd.DataFrame) -> FeatureMatrix:
        if not self.fitted:
            raise RuntimeError("FeatureEngineer.transform() before fit")
        missing = [c for c in self.input_columns if c not in df.columns]
        if missing:  # schema drift fails fast (03-ml-platform §3)
            raise ValueError(f"input schema mismatch — missing columns: {missing}")
        X, names = self._apply(df)
        return FeatureMatrix(X=X, feature_names=names, n_rows=len(df),
                             transformations=list(self._plan),
                             source_hash=frame_hash(df))

    # ------------------------------------------------------------ internals
    def _decide(self, col: str, s: pd.Series) -> dict:
        d: dict = {"column": col}
        missing = float(s.isna().mean())
        nunique = int(s.nunique(dropna=True))
        if missing > MAX_MISSING_RATE:
            d.update(action="drop", reason=f"missing rate {missing:.0%} > {MAX_MISSING_RATE:.0%}")
        elif nunique <= 1:
            d.update(action="drop", reason="constant column")
        elif pd.api.types.is_bool_dtype(s):
            d.update(action="bool_to_int")
        elif pd.api.types.is_numeric_dtype(s):
            self._medians[col] = float(s.median()) if nunique else 0.0
            d.update(action="numeric_median_impute", median=self._medians[col])
        elif pd.api.types.is_datetime64_any_dtype(s):
            d.update(action="datetime_expand", parts=["year", "month", "dayofweek"])
        elif nunique / max(len(s), 1) >= ID_UNIQUE_RATIO:
            d.update(action="drop", reason="identifier-like (near-unique)")
        elif nunique <= MAX_ONEHOT_CARDINALITY:
            cats = sorted(str(v) for v in s.dropna().unique())
            self._onehot[col] = cats
            d.update(action="one_hot", categories=cats)
        else:
            vc = s.astype(str).value_counts(normalize=True)
            self._freq[col] = {str(k): float(v) for k, v in vc.items()}
            d.update(action="frequency_encode", cardinality=nunique)
        return d

    def _apply(self, df: pd.DataFrame) -> tuple[np.ndarray, list[str]]:
        cols: list[np.ndarray] = []
        names: list[str] = []
        for d in self._plan:
            col, action = d["column"], d["action"]
            if action == "drop":
                continue
            s = df[col]
            if action == "bool_to_int":
                cols.append(s.fillna(False).astype(float).to_numpy())
                names.append(col)
            elif action == "numeric_median_impute":
                cols.append(pd.to_numeric(s, errors="coerce")
                            .fillna(self._medians[col]).to_numpy(dtype=float))
                names.append(col)
            elif action == "datetime_expand":
                dt = pd.to_datetime(s, errors="coerce")
                for part in d["parts"]:
                    cols.append(getattr(dt.dt, part).fillna(0).to_numpy(dtype=float))
                    names.append(f"{col}_{part}")
            elif action == "one_hot":
                sv = s.astype(str)
                for cat in d["categories"]:
                    cols.append((sv == cat).astype(float).to_numpy())
                    names.append(f"{col}={cat}")
            elif action == "frequency_encode":
                freq = self._freq[col]
                cols.append(s.astype(str).map(lambda v, f=freq: f.get(v, 0.0))
                            .to_numpy(dtype=float))
                names.append(f"{col}_freq")
        if not cols:
            return np.empty((len(df), 0)), []
        return np.column_stack(cols), names

    @staticmethod
    def _encode_target(s: pd.Series) -> np.ndarray:
        if pd.api.types.is_numeric_dtype(s) or pd.api.types.is_bool_dtype(s):
            return s.astype(float).to_numpy()
        cats = {v: i for i, v in enumerate(sorted(s.astype(str).unique()))}
        return s.astype(str).map(cats).to_numpy(dtype=float)


# ------------------------------------------------------------- feature store
def frame_hash(df: pd.DataFrame) -> str:
    """Content hash of a frame — identical inputs are never recomputed."""
    h = hashlib.sha256()
    h.update("|".join(map(str, df.columns)).encode())
    h.update(str(df.shape).encode())
    try:
        h.update(pd.util.hash_pandas_object(df, index=False).values.tobytes())
    except TypeError:  # unhashable cell types — fall back to a repr digest
        h.update(df.astype(str).to_csv(index=False).encode())
    return h.hexdigest()[:16]


class FeatureStore:
    """Hash-addressed offline store: materialized matrices per feature view,
    with lineage metadata (dataset → feature view → training set)."""

    def __init__(self, project_dir: Path):
        self._dir = Path(project_dir) / "features"
        self._dir.mkdir(parents=True, exist_ok=True)

    def materialize(self, view: str, df: pd.DataFrame,
                    engineer: FeatureEngineer | None = None,
                    target: str | None = None) -> tuple[FeatureMatrix, FeatureEngineer]:
        """Build (or reuse) the materialized matrix for a feature view."""
        key = f"{view}_{frame_hash(df)}_{target or 'none'}"
        npz, meta = self._dir / f"{key}.npz", self._dir / f"{key}.meta.json"
        engineer = engineer or FeatureEngineer()
        if npz.exists() and meta.exists() and engineer.fitted:
            data = np.load(npz, allow_pickle=False)
            info = json.loads(meta.read_text(encoding="utf-8"))
            logger.info("feature store hit: %s", key)
            return FeatureMatrix(
                X=data["X"], y=data["y"] if "y" in data.files else None,
                feature_names=info["feature_names"], target=info.get("target"),
                n_rows=int(info["n_rows"]),
                transformations=info["transformations"],
                source_hash=info["source_hash"]), engineer

        fm = engineer.fit_transform(df, target=target)
        arrays: dict = {"X": fm.X}
        if fm.y is not None:
            arrays["y"] = fm.y
        np.savez_compressed(npz, **arrays)
        meta.write_text(json.dumps({
            "view": view, "feature_names": fm.feature_names,
            "target": fm.target, "n_rows": fm.n_rows,
            "transformations": fm.transformations,
            "source_hash": fm.source_hash,
            "lineage": {"source_rows": len(df),
                        "source_columns": list(map(str, df.columns))},
            "materialized_at": datetime.now(UTC).isoformat(),
        }, ensure_ascii=False, default=str), encoding="utf-8")
        logger.info("feature store materialized: %s (%d×%d)",
                    key, fm.n_rows, len(fm.feature_names))
        return fm, engineer

    def views(self) -> list[dict]:
        out = []
        for meta in sorted(self._dir.glob("*.meta.json")):
            info = json.loads(meta.read_text(encoding="utf-8"))
            out.append({"view": info["view"], "n_rows": info["n_rows"],
                        "n_features": len(info["feature_names"]),
                        "target": info.get("target"),
                        "source_hash": info["source_hash"],
                        "materialized_at": info["materialized_at"]})
        return out

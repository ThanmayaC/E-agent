"""Tabular Model Selection Framework (03-ml-platform.md §5) — never hardcoded.

The same three-stage funnel as the time-series framework, applied to
entity-level prediction tasks (churn-style classification, growth-style
regression, segmentation):

    meta-features → eligibility gates → priors order candidates
        → cross-validated champion/challenger vs the dummy baseline

Evaluation is the only judge (§5.3): AUC-PR for classification (imbalance-
honest), MAE for regression, silhouette for segmentation. A candidate is
admitted only if it beats the baseline by the configured margin; ties go to
the simpler model. "No model admitted" is a normal, fully-traced outcome.

GBM libraries (XGBoost/LightGBM/CatBoost) keep their gates in the trace:
recorded as ineligible until a dataset clears the statistical floor AND the
library is installed — a 40-row sheet can never spawn a booster.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from app.core.logging import get_logger
from app.ml.features import ID_UNIQUE_RATIO, FeatureEngineer, FeatureMatrix

logger = get_logger(__name__)

MIN_ROWS = 40                # below this no candidate family is evaluated
MIN_CLASS_COUNT = 10         # each class must be representable in CV folds
GBM_ROW_FLOOR = 1000         # xgboost/lightgbm/catboost statistical floor
GBM_FEATURE_FLOOR = 5
FOREST_ROW_FLOOR = 200       # sklearn ensemble floor
SEGMENTATION_ROW_FLOOR = 100

# conservative name priors for representative enterprise targets — priors
# order the search for targets, they never invent one
CLASSIFICATION_TARGET_HINTS = re.compile(
    r"churn|attrit|retain|active|success|fail|convert|default|fraud|won|closed",
    re.IGNORECASE)
REGRESSION_TARGET_HINTS = re.compile(
    r"growth|revenue|sales|amount|value|spend|ltv|volume|profit|margin",
    re.IGNORECASE)


def _optional(module: str):
    try:
        return __import__(module)
    except ImportError:
        return None


@dataclass
class TaskSpec:
    task: str                      # classification | regression | segmentation
    target: str | None = None
    name: str = ""
    reason: str = ""


@dataclass
class TabularOutcome:
    task: TaskSpec
    model: object | None = None    # fitted champion (None = not admitted)
    model_name: str | None = None
    family: str = ""
    metrics: dict = field(default_factory=dict)
    trace: dict = field(default_factory=dict)


# ------------------------------------------------------------ task discovery
def discover_tasks(df: pd.DataFrame, max_tasks: int = 3) -> list[TaskSpec]:
    """Representative enterprise prediction tasks, discovered — never assumed.
    Binary outcome columns become classification candidates, metric-named
    numeric columns become regression candidates, and a wide-enough numeric
    frame is a segmentation candidate. Name hints only *order* candidates."""
    tasks: list[TaskSpec] = []
    n = len(df)

    binary_cols, numeric_cols = [], []
    for col in df.columns:
        s = df[col].dropna()
        nunique = s.nunique()
        if nunique == 2 and n and len(s) / n > 0.5:
            counts = s.value_counts()
            if int(counts.min()) >= MIN_CLASS_COUNT:
                binary_cols.append(col)
        elif pd.api.types.is_numeric_dtype(s) and nunique > 10:
            # near-unique integers are identifiers; continuous floats are
            # naturally unique and stay eligible
            if (pd.api.types.is_float_dtype(s)
                    or nunique / max(len(s), 1) < ID_UNIQUE_RATIO):
                numeric_cols.append(col)

    binary_cols.sort(key=lambda c: not CLASSIFICATION_TARGET_HINTS.search(c))
    for col in binary_cols[:1]:
        hinted = bool(CLASSIFICATION_TARGET_HINTS.search(col))
        tasks.append(TaskSpec(
            task="classification", target=col, name=f"predict_{_slug(col)}",
            reason=("target name matches enterprise outcome pattern" if hinted
                    else "binary outcome column with both classes represented")))

    hinted_numeric = [c for c in numeric_cols if REGRESSION_TARGET_HINTS.search(c)]
    for col in hinted_numeric[:1]:
        tasks.append(TaskSpec(
            task="regression", target=col, name=f"predict_{_slug(col)}",
            reason="numeric metric matching enterprise value pattern"))

    if n >= SEGMENTATION_ROW_FLOOR and len(numeric_cols) >= 3:
        tasks.append(TaskSpec(
            task="segmentation", name="entity_segmentation",
            reason=f"{n} rows × {len(numeric_cols)} numeric features"))
    return tasks[:max_tasks]


def _slug(col: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(col).lower()).strip("_")


# --------------------------------------------------------------- meta/gate
def tabular_meta_features(fm: FeatureMatrix, task: TaskSpec) -> dict:
    feats = {"n_rows": fm.n_rows, "n_features": len(fm.feature_names)}
    if fm.X.size:
        variances = fm.X.std(axis=0)
        feats["n_informative"] = int(np.sum(variances > 0))
    else:
        feats["n_informative"] = 0
    if task.task == "classification" and fm.y is not None and len(fm.y):
        _, counts = np.unique(fm.y, return_counts=True)
        feats["class_balance"] = round(float(counts.min() / counts.sum()), 4)
        feats["minority_count"] = int(counts.min())
    if task.task == "regression" and fm.y is not None and len(fm.y):
        mean = float(np.mean(fm.y))
        feats["target_cv"] = round(float(np.std(fm.y) / abs(mean)), 4) if mean else None
    return feats


class TabularSelectionFramework:
    """gates → priors → cross-validated champion/challenger. One per run."""

    def __init__(self, beat_margin: float = 0.05, random_state: int = 0):
        self.beat_margin = float(beat_margin)
        self.random_state = int(random_state)

    def run(self, df: pd.DataFrame, task: TaskSpec,
            engineer: FeatureEngineer | None = None
            ) -> tuple[TabularOutcome, FeatureEngineer]:
        engineer = engineer or FeatureEngineer()
        fm = engineer.fit_transform(df, target=task.target)
        outcome = TabularOutcome(task=task)
        feats = tabular_meta_features(fm, task)
        trace: dict = {"task": task.task, "target": task.target,
                       "name": task.name, "meta_features": feats,
                       "gates": {}, "candidates": [],
                       "verdict": "no_model_admitted", "reason": ""}
        outcome.trace = trace

        n, k = fm.n_rows, feats["n_informative"]
        if n < MIN_ROWS or k == 0:
            trace["reason"] = (f"{n} rows / {k} informative features below the "
                               f"{MIN_ROWS}-row floor — deterministic analytics "
                               "already serve the answer")
            return outcome, engineer
        if (task.task == "classification"
                and feats.get("minority_count", 0) < MIN_CLASS_COUNT):
            trace["reason"] = (f"minority class has {feats.get('minority_count', 0)} "
                               f"examples < {MIN_CLASS_COUNT} — cannot evaluate honestly")
            return outcome, engineer

        candidates = self._candidates(task, n, k, trace["gates"])
        if task.task == "segmentation":
            return self._run_segmentation(fm, outcome), engineer

        baseline_result = self._evaluate(self._baseline(task), fm, task)
        baseline_score = float(np.mean(baseline_result["primary"]))
        trace["baseline"] = {
            "name": "dummy_" + task.task,
            "metric": self._metric_name(task),
            "score": round(baseline_score, 6),
            "fold_std": round(float(np.std(baseline_result["primary"])), 6)}

        best = None
        for name, family, make in candidates:
            model = make()
            try:
                result = self._evaluate(model, fm, task)
            except Exception as exc:
                trace["candidates"].append({"name": name, "error": str(exc)[:200]})
                continue
            score = float(np.mean(result["primary"]))
            beats = self._beats(result, baseline_result, task)
            entry = {"name": name, "family": family,
                     "score": round(score, 6),
                     "fold_std": round(float(np.std(result["primary"])), 6),
                     "baseline_score": round(baseline_score, 6),
                     "beats_baseline": bool(beats)}
            if result["auc"] is not None:
                entry["roc_auc"] = round(float(np.mean(result["auc"])), 6)
            trace["candidates"].append(entry)
            if beats and (best is None or self._better(score, best[3], task)):
                best = (name, family, make, score)

        if best is None:
            trace["reason"] = (f"no candidate beat the dummy baseline by "
                               f"≥{self.beat_margin:.0%} on cross-validation — "
                               "baseline retained (the gate working is the feature)")
            return outcome, engineer

        name, family, make, score = best
        champion = make()
        champion.fit(fm.X, fm.y)
        trace["verdict"] = "model_admitted"
        trace["reason"] = (f"{name} beat dummy baseline "
                           f"({self._metric_name(task)} {score:.4f} vs "
                           f"{baseline_score:.4f}) on cross-validation")
        outcome.model = champion
        outcome.model_name = f"{task.name}:{name}"
        outcome.family = family
        outcome.metrics = {self._metric_name(task): round(score, 6),
                           "baseline": round(baseline_score, 6),
                           "improvement": self._improvement(score, baseline_score, task)}
        return outcome, engineer

    # ------------------------------------------------------------ candidates
    def _candidates(self, task: TaskSpec, n: int, k: int, gates: dict) -> list:
        from sklearn.ensemble import (
            GradientBoostingClassifier,
            GradientBoostingRegressor,
            RandomForestClassifier,
            RandomForestRegressor,
        )
        from sklearn.linear_model import LogisticRegression, Ridge
        rs = self.random_state
        clf = task.task == "classification"
        out: list = []

        gates["linear/logistic"] = "eligible (baseline family)"
        if clf:
            out.append(("logistic_regression", "linear",
                        lambda: LogisticRegression(max_iter=1000, random_state=rs)))
        else:
            out.append(("ridge_regression", "linear", lambda: Ridge(random_state=rs)))

        if n >= FOREST_ROW_FLOOR:
            gates["sklearn_ensemble"] = "eligible"
            if clf:
                out.append(("random_forest", "tree_ensemble",
                            lambda: RandomForestClassifier(n_estimators=100, random_state=rs)))
                out.append(("gradient_boosting", "tree_ensemble",
                            lambda: GradientBoostingClassifier(random_state=rs)))
            else:
                out.append(("random_forest", "tree_ensemble",
                            lambda: RandomForestRegressor(n_estimators=100, random_state=rs)))
                out.append(("gradient_boosting", "tree_ensemble",
                            lambda: GradientBoostingRegressor(random_state=rs)))
        else:
            gates["sklearn_ensemble"] = f"gated: {n} rows < {FOREST_ROW_FLOOR}"

        if n < GBM_ROW_FLOOR or k < GBM_FEATURE_FLOOR:
            gates["gbm_libraries"] = (f"gated: {n} rows / {k} informative features "
                                      f"below {GBM_ROW_FLOOR}×{GBM_FEATURE_FLOOR} floor")
        else:
            for lib, ctor in (("xgboost", "XGBClassifier" if clf else "XGBRegressor"),
                              ("lightgbm", "LGBMClassifier" if clf else "LGBMRegressor"),
                              ("catboost", "CatBoostClassifier" if clf else "CatBoostRegressor")):
                mod = _optional(lib)
                if mod is None:
                    gates[lib] = "gated: library not installed (lite profile)"
                    continue
                gates[lib] = "eligible"
                kwargs = {"random_state": rs}
                if lib == "catboost":
                    kwargs["verbose"] = 0
                out.append((lib, "gbm",
                            lambda m=mod, c=ctor, kw=kwargs: getattr(m, c)(**kw)))
        gates["deep_learning"] = ("gated: deep tabular models live in the Deep "
                                  "Learning Module behind their own gates")
        return out

    # ------------------------------------------------------------ evaluation
    @staticmethod
    def _metric_name(task: TaskSpec) -> str:
        return "auc_pr" if task.task == "classification" else "mae"

    def _baseline(self, task: TaskSpec):
        from sklearn.dummy import DummyClassifier, DummyRegressor
        if task.task == "classification":
            return DummyClassifier(strategy="prior")
        return DummyRegressor(strategy="mean")

    def _evaluate(self, model, fm: FeatureMatrix, task: TaskSpec) -> dict:
        """Per-fold cross-validated scores: {"primary": AUC-PR ↑ / MAE ↓,
        "auc": ROC-AUC folds (classification only — its exact 0.5 null is the
        significance gate; AP's null is biased above prevalence on small
        folds, so AP alone must never admit)."""
        from sklearn.model_selection import RepeatedKFold, RepeatedStratifiedKFold, cross_validate
        if task.task == "classification":
            _, counts = np.unique(fm.y, return_counts=True)
            folds = int(min(5, counts.min()))
            cv = RepeatedStratifiedKFold(n_splits=max(folds, 2), n_repeats=3,
                                         random_state=self.random_state)
            r = cross_validate(model, fm.X, fm.y, cv=cv,
                               scoring=["average_precision", "roc_auc"])
            # exact null SE of AUC (Mann-Whitney / Hanley-McNeil) from the
            # class counts — the significance gate is calibrated to the
            # dataset, not to optimistic fold-to-fold variance
            n1 = int(counts.min())
            n2 = int(counts.sum() - n1)
            null_se = float(np.sqrt((n1 + n2 + 1) / (12.0 * n1 * n2)))
            return {"primary": np.asarray(r["test_average_precision"]),
                    "auc": np.asarray(r["test_roc_auc"]),
                    "auc_null_se": null_se}
        cv = RepeatedKFold(n_splits=min(5, fm.n_rows), n_repeats=3,
                           random_state=self.random_state)
        r = cross_validate(model, fm.X, fm.y, cv=cv,
                           scoring=["neg_mean_absolute_error"])
        return {"primary": -np.asarray(r["test_neg_mean_absolute_error"]),
                "auc": None}

    def _beats(self, result: dict, baseline_result: dict,
               task: TaskSpec) -> bool:
        """Margin AND overlap-aware uncertainty (§5.3): the improvement must
        clear the configured relative margin, and — for classification — the
        ROC-AUC must sit significantly above its exact 0.5 null. CV noise
        never admits a model."""
        folds, baseline_folds = result["primary"], baseline_result["primary"]
        score, baseline = float(np.mean(folds)), float(np.mean(baseline_folds))
        # conservative: repeated-CV folds overlap, so treat only the number
        # of distinct splits as independent when estimating the SE
        k = max(min(len(folds), len(baseline_folds)) // 3, 1)
        if task.task == "classification":  # higher is better
            if score - baseline <= abs(baseline) * self.beat_margin:
                return False
            auc = result["auc"]
            fold_se = float(np.sqrt(np.var(auc) / max(len(auc) // 3, 1)))
            threshold = max(2.58 * result["auc_null_se"], 1.96 * fold_se)
            return float(np.mean(auc)) - 0.5 > threshold
        if baseline <= 0:                  # perfect baseline cannot be beaten
            return False
        diff = baseline - score
        se = float(np.sqrt(np.var(folds) / k + np.var(baseline_folds) / k))
        return diff > baseline * self.beat_margin and diff > 1.96 * se

    @staticmethod
    def _better(score: float, incumbent: float, task: TaskSpec) -> bool:
        return score > incumbent if task.task == "classification" else score < incumbent

    @staticmethod
    def _improvement(score: float, baseline: float, task: TaskSpec) -> float | None:
        if baseline == 0:
            return None
        if task.task == "classification":
            return round(score / baseline - 1, 4)
        return round(1 - score / baseline, 4)

    # ---------------------------------------------------------- segmentation
    def _run_segmentation(self, fm: FeatureMatrix,
                          outcome: TabularOutcome) -> TabularOutcome:
        """KMeans with silhouette-selected k. The baseline is 'no segments';
        a clustering is admitted only when its silhouette clears a floor —
        weak structure stays unsegmented."""
        from sklearn.cluster import KMeans
        from sklearn.metrics import silhouette_score
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler
        trace = outcome.trace
        trace["gates"]["kmeans"] = "eligible"
        scaler = StandardScaler().fit(fm.X)
        X = scaler.transform(fm.X)
        sample = X[: min(len(X), 2000)]
        best = None
        for k in range(2, min(8, fm.n_rows // 20) + 1):
            km = KMeans(n_clusters=k, n_init=10, random_state=self.random_state)
            labels = km.fit_predict(sample)
            sil = float(silhouette_score(sample, labels))
            trace["candidates"].append({"name": f"kmeans_k{k}",
                                        "silhouette": round(sil, 4)})
            if best is None or sil > best[1]:
                best = (k, sil)
        if best is None or best[1] < 0.20:
            trace["reason"] = ("no cluster count reached silhouette ≥ 0.20 — "
                               "the entities do not segment; none imposed")
            return outcome
        k, sil = best
        # scaler travels inside the model so inference replays training scaling
        model = make_pipeline(
            StandardScaler(),
            KMeans(n_clusters=k, n_init=10, random_state=self.random_state))
        model.fit(fm.X)
        sizes = np.bincount(model[-1].labels_).tolist()
        trace["verdict"] = "model_admitted"
        trace["reason"] = f"kmeans k={k} silhouette {sil:.3f} on standardized features"
        outcome.model = model
        outcome.model_name = f"{outcome.task.name}:kmeans_k{k}"
        outcome.family = "clustering"
        outcome.metrics = {"silhouette": round(sil, 6), "k": k,
                           "segment_sizes": sizes}
        return outcome

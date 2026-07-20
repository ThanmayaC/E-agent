"""Model explainability (03-ml-platform.md §4, §7).

SHAP is the preferred method for tree models when the library is installed;
the deterministic fallbacks (standardized linear coefficients, permutation
importance) keep every admitted model explainable in the lite profile.
A prediction without an explanation is rejected by the ledger, so this
module must always return one — the method used is part of the record.
"""
from __future__ import annotations

import numpy as np

from app.core.logging import get_logger

logger = get_logger(__name__)

TOP_FEATURES = 10

try:  # optional heavy dependency — absence is a recorded, normal state
    import shap  # type: ignore
    _HAS_SHAP = True
except ImportError:
    shap = None
    _HAS_SHAP = False


def shap_available() -> bool:
    return _HAS_SHAP


def explain_model(model, X: np.ndarray, y: np.ndarray | None,
                  feature_names: list[str], task: str) -> dict:
    """Return {"method", "top_features": [{"feature", "importance"}, ...]}.

    Never raises: an explainer failure degrades to the next method and the
    failure is recorded on the result.
    """
    errors: list[str] = []
    for fn in (_try_shap, _try_coefficients, _try_permutation):
        try:
            result = fn(model, X, y, feature_names, task)
        except Exception as exc:  # degrade, never crash the pipeline
            errors.append(f"{fn.__name__}: {str(exc)[:120]}")
            result = None
        if result is not None:
            if errors:
                result["degraded_from"] = errors
            return result
    return {"method": "unavailable", "top_features": [], "errors": errors}


def _rank(names: list[str], importances: np.ndarray) -> list[dict]:
    order = np.argsort(-np.abs(importances))[:TOP_FEATURES]
    return [{"feature": names[i], "importance": round(float(importances[i]), 6)}
            for i in order if np.abs(importances[i]) > 0]


def _try_shap(model, X, y, feature_names, task) -> dict | None:
    if not _HAS_SHAP or not hasattr(model, "feature_importances_"):
        return None
    sample = X[: min(len(X), 200)]
    values = shap.TreeExplainer(model).shap_values(sample)
    if isinstance(values, list):  # per-class list for classifiers
        values = values[-1]
    if values.ndim == 3:
        values = values[..., -1]
    mean_abs = np.abs(values).mean(axis=0)
    return {"method": "shap_tree", "top_features": _rank(feature_names, mean_abs)}


def _try_coefficients(model, X, y, feature_names, task) -> dict | None:
    coef = getattr(model, "coef_", None)
    if coef is None:
        return None
    coef = np.asarray(coef)
    if coef.ndim > 1:
        coef = coef[0]
    scale = X.std(axis=0)
    return {"method": "standardized_coefficients",
            "top_features": _rank(feature_names, coef * scale)}


def _try_permutation(model, X, y, feature_names, task) -> dict | None:
    if y is None:
        # unsupervised (segmentation): variance of cluster centers per feature
        centers = getattr(model, "cluster_centers_", None)
        if centers is None and hasattr(model, "steps"):  # sklearn Pipeline
            centers = getattr(model.steps[-1][1], "cluster_centers_", None)
        if centers is None:
            return None
        return {"method": "cluster_center_dispersion",
                "top_features": _rank(feature_names, np.asarray(centers).std(axis=0))}
    from sklearn.inspection import permutation_importance
    sample = min(len(X), 500)
    r = permutation_importance(model, X[:sample], y[:sample],
                               n_repeats=5, random_state=0)
    return {"method": "permutation_importance",
            "top_features": _rank(feature_names, r.importances_mean)}

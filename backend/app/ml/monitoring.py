"""Model Monitoring (03-ml-platform.md §6) — drift, decay, retraining verdict.

Deterministic, dependency-light stand-in for the Evidently jobs: Population
Stability Index per feature against the training reference distribution,
plus performance decay when ground truth arrives. A verdict of
``should_retrain`` enqueues the retraining pipeline, which re-runs the
*selection framework* — regime changes may change the winning family, so
retraining is never a blind refit.
"""
from __future__ import annotations

import numpy as np

from app.core.logging import get_logger

logger = get_logger(__name__)

PSI_BINS = 10
DRIFT_THRESHOLD = 0.2       # standard PSI rule of thumb: >0.2 = significant
DECAY_THRESHOLD = 0.25      # relative error growth vs training metric


def reference_stats(X: np.ndarray, feature_names: list[str]) -> dict:
    """Training-time distribution snapshot stored on the model card —
    deciles per feature, so live traffic can be compared without keeping
    the training set."""
    stats = {}
    for i, name in enumerate(feature_names):
        col = X[:, i]
        edges = np.quantile(col, np.linspace(0, 1, PSI_BINS + 1))
        stats[name] = {"bin_edges": [float(e) for e in edges],
                       "mean": round(float(col.mean()), 6),
                       "std": round(float(col.std()), 6)}
    return stats


def psi(reference: dict, col: np.ndarray) -> float:
    """Population Stability Index of a live column vs its reference deciles."""
    edges = np.asarray(reference["bin_edges"], dtype=float)
    edges = np.unique(edges)
    if len(edges) < 3 or len(col) == 0:
        return 0.0
    expected = np.full(len(edges) - 1, 1.0 / (len(edges) - 1))
    counts, _ = np.histogram(col, bins=edges)
    # clip live values outside the training range into the edge bins
    counts[0] += int(np.sum(col < edges[0]))
    counts[-1] += int(np.sum(col > edges[-1]))
    actual = counts / max(counts.sum(), 1)
    eps = 1e-4
    return float(np.sum((actual - expected)
                        * np.log((actual + eps) / (expected + eps))))


class ModelMonitor:
    def __init__(self, drift_threshold: float = DRIFT_THRESHOLD,
                 decay_threshold: float = DECAY_THRESHOLD):
        self.drift_threshold = float(drift_threshold)
        self.decay_threshold = float(decay_threshold)

    def assess_drift(self, card: dict, X_live: np.ndarray,
                     feature_names: list[str]) -> dict:
        ref = card.get("reference_stats") or {}
        per_feature = {}
        for i, name in enumerate(feature_names):
            if name in ref:
                per_feature[name] = round(psi(ref[name], X_live[:, i]), 4)
        drifted = {k: v for k, v in per_feature.items()
                   if v > self.drift_threshold}
        score = round(float(np.mean(list(per_feature.values()))), 4) if per_feature else 0.0
        return {"drift_score": score, "per_feature_psi": per_feature,
                "drifted_features": sorted(drifted, key=drifted.get, reverse=True),
                "drift_detected": bool(drifted) or score > self.drift_threshold}

    def assess_decay(self, card: dict, y_true: np.ndarray,
                     y_pred: np.ndarray) -> dict:
        """Error growth vs the training-time metric once actuals arrive."""
        task = card.get("task", "")
        live_mae = float(np.mean(np.abs(np.asarray(y_true, dtype=float)
                                        - np.asarray(y_pred, dtype=float))))
        trained = card.get("metrics", {}).get("mae")
        result = {"live_mae": round(live_mae, 6), "training_mae": trained,
                  "task": task, "decayed": False}
        if isinstance(trained, (int, float)) and trained > 0:
            growth = live_mae / trained - 1
            result["error_growth"] = round(growth, 4)
            result["decayed"] = growth > self.decay_threshold
        return result

    def verdict(self, drift: dict | None = None, decay: dict | None = None) -> dict:
        reasons = []
        if drift and drift.get("drift_detected"):
            reasons.append(f"feature drift (PSI score {drift['drift_score']}, "
                           f"{len(drift['drifted_features'])} features > threshold)")
        if decay and decay.get("decayed"):
            reasons.append(f"performance decay (error growth "
                           f"{decay.get('error_growth')})")
        return {"should_retrain": bool(reasons), "reasons": reasons}

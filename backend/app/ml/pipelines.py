"""Training / Inference / Retraining pipelines (03-ml-platform.md §4, §6).

Typed pipeline classes over the tabular selection framework:

    TrainingPipeline.run(df, task) -> TrainingResult
      resolve features (FeatureStore, hash-addressed)
        → Tabular Selection Framework (gates → priors → CV champion/challenger)
        → explainability artifacts (SHAP or deterministic fallback)
        → register (ModelRegistry card + Evidence Ledger control-plane row)

    InferencePipeline.run(name, df) -> predictions + ml_prediction evidence
      load version → enforce signature → predict → explain → evidence payloads

    RetrainingPipeline.maybe_retrain(...) re-runs the *selection framework*
      when the monitor's verdict demands it — never a blind refit.

A prediction without model_version + explanation is rejected by the ledger —
the ML analogue of the anti-hallucination rule — so both are attached here,
at the only place predictions are produced.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd

from app.core.logging import get_logger
from app.ml.explain import explain_model
from app.ml.features import FeatureStore
from app.ml.monitoring import ModelMonitor, reference_stats
from app.ml.registry import ModelRegistry, RegisteredModel
from app.ml.tabular import TabularSelectionFramework, TaskSpec, discover_tasks

logger = get_logger(__name__)

MAX_EVIDENCE_ROWS = 100      # per-entity predictions cited in evidence


@dataclass
class TrainingResult:
    task: TaskSpec
    registered: RegisteredModel | None = None   # None = no model admitted
    trace: dict = field(default_factory=dict)


class TrainingPipeline:
    """select → train → evaluate → explain → register."""

    def __init__(self, project_dir: Path, ledger=None, project_id: str = "",
                 run_id: str = "", beat_margin: float = 0.05,
                 mlflow_uri: str = ""):
        self.project_dir = Path(project_dir)
        self.store = FeatureStore(self.project_dir)
        self.registry = ModelRegistry(self.project_dir, mlflow_uri=mlflow_uri)
        self.framework = TabularSelectionFramework(beat_margin=beat_margin)
        self.ledger = ledger
        self.project_id, self.run_id = project_id, run_id

    def run(self, df: pd.DataFrame, task: TaskSpec) -> TrainingResult:
        outcome, engineer = self.framework.run(df, task)
        result = TrainingResult(task=task, trace=outcome.trace)
        if outcome.model is None:
            return result  # "no model admitted" is a normal, traced outcome

        fm = engineer.transform(df.drop(columns=[task.target])
                                if task.target else df)
        explanation = explain_model(
            outcome.model, fm.X,
            engineer._encode_target(df[task.target]) if task.target else None,
            fm.feature_names, task.task)
        outcome.trace["explanation"] = explanation

        limitations = []
        if fm.n_rows < 500:
            limitations.append(f"trained on {fm.n_rows} rows — collect more "
                               "history before relying on this model")
        registered = self.registry.register(
            name=task.name, model=outcome.model, engineer=engineer,
            task=task.task, family=outcome.family, metrics=outcome.metrics,
            selection_trace=outcome.trace,
            reference_stats=reference_stats(fm.X, fm.feature_names),
            limitations=limitations)
        if self.ledger is not None:
            self.ledger.register_model(
                self.project_id, self.run_id, name=task.name,
                family=outcome.family, task=task.task,
                metrics=outcome.metrics, selection_trace=outcome.trace)
        result.registered = registered
        return result

    def run_discovered(self, df: pd.DataFrame,
                       max_tasks: int = 3) -> list[TrainingResult]:
        """Discover representative enterprise tasks on the frame and train
        each — gates decide what actually gets a model."""
        return [self.run(df, task) for task in discover_tasks(df, max_tasks)]


class InferencePipeline:
    """load version → enforce signature → predict → evidence payloads."""

    def __init__(self, project_dir: Path):
        self.registry = ModelRegistry(Path(project_dir))
        self.monitor = ModelMonitor()

    def run(self, name: str, df: pd.DataFrame,
            version: int | None = None) -> dict:
        model, engineer, card = self.registry.load(name, version=version)
        target = card["selection_trace"].get("target")
        if target and target in df.columns:
            df = df.drop(columns=[target])
        fm = engineer.transform(df)  # raises on schema drift — by design

        task = card["task"]
        if task == "classification" and hasattr(model, "predict_proba"):
            values = model.predict_proba(fm.X)[:, -1]
        else:
            values = model.predict(fm.X)

        drift = self.monitor.assess_drift(card, fm.X, fm.feature_names)
        model_version = f"{card['name']}@{card['version']}"
        payload = {
            "id": f"ml:{card['name']}:v{card['version']}",
            "task": task, "target": target,
            "model_version": model_version,
            "n_entities": int(len(values)),
            "summary": self._summarize(task, values),
            "sample": [round(float(v), 6) for v in values[:MAX_EVIDENCE_ROWS]],
            "explanation": card["selection_trace"].get("explanation")
                           or {"method": card.get("explainability")},
            "backtest": card["metrics"],
            "limitations": card.get("limitations", []),
            "drift": {"score": drift["drift_score"],
                      "detected": drift["drift_detected"]},
        }
        return {"predictions": np.asarray(values), "evidence": payload,
                "card": card, "drift": drift}

    @staticmethod
    def _summarize(task: str, values: np.ndarray) -> dict:
        v = np.asarray(values, dtype=float)
        if task == "classification":
            return {"mean_probability": round(float(v.mean()), 4),
                    "high_risk_count": int(np.sum(v >= 0.5))}
        if task == "segmentation":
            uniq, counts = np.unique(v.astype(int), return_counts=True)
            return {"segments": {int(k): int(c)
                                 for k, c in zip(uniq, counts, strict=True)}}
        return {"mean": round(float(v.mean()), 4),
                "p10": round(float(np.quantile(v, 0.1)), 4),
                "p90": round(float(np.quantile(v, 0.9)), 4)}


class RetrainingPipeline:
    """Monitor verdict → full re-selection (02 §6.4 retraining graph)."""

    def __init__(self, training: TrainingPipeline):
        self.training = training
        self.monitor = ModelMonitor()

    def maybe_retrain(self, name: str, df: pd.DataFrame,
                      y_true: np.ndarray | None = None) -> dict:
        inference = InferencePipeline(self.training.project_dir)
        result = inference.run(name, df)
        drift = result["drift"]
        decay = None
        if y_true is not None:
            decay = self.monitor.assess_decay(result["card"], y_true,
                                              result["predictions"])
        verdict = self.monitor.verdict(drift=drift, decay=decay)
        out = {"verdict": verdict, "drift": drift, "decay": decay,
               "retrained": None}
        if verdict["should_retrain"]:
            trace = result["card"]["selection_trace"]
            task = TaskSpec(task=result["card"]["task"],
                            target=trace.get("target"), name=name,
                            reason="retraining: " + "; ".join(verdict["reasons"]))
            out["retrained"] = self.training.run(df, task)
            logger.info("retraining triggered for %s: %s", name,
                        verdict["reasons"])
        return out

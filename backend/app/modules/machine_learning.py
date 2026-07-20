"""Machine Learning Module (SDS §2.3) — status: implemented.

The full ML platform of 03-ml-platform.md behind one facade:

- Model Selection Framework — time-series (``ModelSelectionFramework``) and
  tabular (``TabularSelectionFramework``): meta-features → eligibility gates
  → priors → champion/challenger vs the deterministic/dummy baseline, fully
  traced. "No model admitted" is a normal outcome.
- Feature Engineering & Feature Store — deterministic fit/transform with
  hash-addressed offline materialization and lineage.
- Training / Inference / Retraining pipelines — representative enterprise
  tasks (churn-style classification, growth-style regression, segmentation)
  discovered from the data, never assumed.
- Model Registry — versions, stages (Production requires human approval),
  signatures, model cards; MLflow as an optional mirror.
- Explainability — SHAP when installed, deterministic fallbacks otherwise.
- Monitoring — PSI drift + performance decay → retraining verdict.

GBM libraries (XGBoost/LightGBM/CatBoost) are optional: their eligibility
gates are recorded in every trace and open only when the data clears the
statistical floor AND the library is installed.
"""
from app.ml.explain import explain_model, shap_available
from app.ml.features import FeatureEngineer, FeatureMatrix, FeatureStore
from app.ml.monitoring import ModelMonitor, psi, reference_stats
from app.ml.pipelines import InferencePipeline, RetrainingPipeline, TrainingPipeline, TrainingResult
from app.ml.registry import ModelRegistry, RegisteredModel
from app.ml.selection import ModelSelectionFramework, SelectionOutcome, meta_features
from app.ml.tabular import TabularOutcome, TabularSelectionFramework, TaskSpec, discover_tasks, tabular_meta_features

__all__ = [
    "ModelSelectionFramework", "SelectionOutcome", "meta_features",
    "TabularSelectionFramework", "TabularOutcome", "TaskSpec",
    "discover_tasks", "tabular_meta_features",
    "FeatureEngineer", "FeatureMatrix", "FeatureStore",
    "TrainingPipeline", "InferencePipeline", "RetrainingPipeline",
    "TrainingResult", "ModelRegistry", "RegisteredModel",
    "ModelMonitor", "psi", "reference_stats",
    "explain_model", "shap_available",
]

"""ML platform contract (03-ml-platform.md §2–§6): features, tabular
selection, registry, pipelines, monitoring.

Same doctrine as the time-series framework: gates → priors → evaluation,
"no model admitted" is a normal outcome, a prediction always carries
model_version + explanation, Production promotion requires a human approver.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from app.ml.features import FeatureEngineer, FeatureStore
from app.ml.monitoring import ModelMonitor, reference_stats
from app.ml.pipelines import InferencePipeline, RetrainingPipeline, TrainingPipeline
from app.ml.registry import ModelRegistry
from app.ml.tabular import MIN_ROWS, TabularSelectionFramework, TaskSpec, discover_tasks


def _churn_frame(n=400, seed=0) -> pd.DataFrame:
    """Learnable churn-style data: churn depends on inactivity + spend."""
    rng = np.random.default_rng(seed)
    inactivity = rng.integers(0, 120, n)
    spend = rng.gamma(2.0, 500, n)
    logit = 0.05 * inactivity - 0.002 * spend - 1.5
    churned = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)
    return pd.DataFrame({
        "customer_id": [f"C{i:05d}" for i in range(n)],
        "days_inactive": inactivity,
        "monthly_spend": spend,
        "order_count": rng.poisson(20, n),
        "region": rng.choice(["north", "south", "east", "west"], n),
        "churned": churned,
    })


# ------------------------------------------------------- feature engineering
def test_feature_engineer_is_deterministic_and_typed():
    df = _churn_frame()
    eng = FeatureEngineer()
    fm = eng.fit_transform(df, target="churned")
    assert fm.y is not None and set(np.unique(fm.y)) == {0.0, 1.0}
    # identifier dropped, categorical one-hot, numerics kept
    assert not any(n.startswith("customer_id") for n in fm.feature_names)
    assert "region=north" in fm.feature_names
    assert "days_inactive" in fm.feature_names
    actions = {d["column"]: d["action"] for d in fm.transformations}
    assert actions["customer_id"] == "drop"
    # transform() replays the fit exactly
    fm2 = eng.transform(df.drop(columns=["churned"]))
    assert np.allclose(fm.X, fm2.X)


def test_feature_engineer_fails_fast_on_schema_drift():
    df = _churn_frame()
    eng = FeatureEngineer()
    eng.fit_transform(df, target="churned")
    with pytest.raises(ValueError, match="schema mismatch"):
        eng.transform(df.drop(columns=["churned", "days_inactive"]))


def test_feature_store_materializes_with_lineage(tmp_path):
    store = FeatureStore(tmp_path)
    fm, eng = store.materialize("customers", _churn_frame(), target="churned")
    (view,) = store.views()
    assert view["view"] == "customers"
    assert view["n_rows"] == 400 and view["target"] == "churned"
    # cache hit path returns the identical matrix
    fm2, _ = store.materialize("customers", _churn_frame(), engineer=eng,
                               target="churned")
    assert np.allclose(fm.X, fm2.X)


# ----------------------------------------------------------- task discovery
def test_discover_tasks_finds_enterprise_targets():
    tasks = discover_tasks(_churn_frame())
    kinds = {t.task: t for t in tasks}
    assert kinds["classification"].target == "churned"
    assert kinds["regression"].target == "monthly_spend"
    assert "segmentation" in kinds


def test_discover_tasks_on_uninformative_frame_is_empty():
    df = pd.DataFrame({"id": range(20), "note": [f"n{i}" for i in range(20)]})
    assert discover_tasks(df) == []


# --------------------------------------------------------- tabular selection
def test_small_frame_admits_nothing():
    fw = TabularSelectionFramework()
    out, _ = fw.run(_churn_frame(n=MIN_ROWS - 5),
                    TaskSpec(task="classification", target="churned", name="churn"))
    assert out.model is None
    assert "floor" in out.trace["reason"] or "minority" in out.trace["reason"]


def test_learnable_signal_admits_model_with_full_trace():
    fw = TabularSelectionFramework()
    out, eng = fw.run(_churn_frame(),
                      TaskSpec(task="classification", target="churned",
                               name="churn"))
    assert out.model is not None
    assert out.trace["verdict"] == "model_admitted"
    assert out.metrics["auc_pr"] > out.metrics["baseline"]
    gates = out.trace["gates"]
    assert "gated" in gates["gbm_libraries"]  # 400 rows < 1000 floor
    assert any(c.get("beats_baseline") for c in out.trace["candidates"])


def test_pure_noise_keeps_the_baseline():
    rx, ry = np.random.default_rng(1), np.random.default_rng(1001)
    df = pd.DataFrame({"x1": rx.normal(size=300), "x2": rx.normal(size=300),
                       "y": ry.integers(0, 2, 300)})
    fw = TabularSelectionFramework()
    out, _ = fw.run(df, TaskSpec(task="classification", target="y", name="noise"))
    assert out.model is None
    assert out.trace["verdict"] == "no_model_admitted"


def test_segmentation_gates_on_structure():
    rng = np.random.default_rng(2)
    # two well-separated blobs → admitted
    blob = np.vstack([rng.normal(0, 0.5, (100, 3)), rng.normal(8, 0.5, (100, 3))])
    df = pd.DataFrame(blob, columns=["a", "b", "c"])
    fw = TabularSelectionFramework()
    out, _ = fw.run(df, TaskSpec(task="segmentation", name="segments"))
    assert out.model is not None
    assert out.metrics["k"] == 2


# ------------------------------------------------- registry & pipelines
def test_training_to_inference_roundtrip(tmp_path):
    training = TrainingPipeline(tmp_path)
    df = _churn_frame()
    result = training.run(df, TaskSpec(task="classification",
                                       target="churned", name="churn"))
    assert result.registered is not None
    assert result.registered.stage == "Staging"
    assert result.trace["explanation"]["method"] != "unavailable"

    inference = InferencePipeline(tmp_path)
    out = inference.run("churn", df)
    ev = out["evidence"]
    # the ML anti-hallucination rule: version + explanation always attached
    assert ev["model_version"] == "churn@1"
    assert ev["explanation"]["top_features"]
    assert ev["n_entities"] == len(df)
    assert 0 <= ev["summary"]["mean_probability"] <= 1


def test_inference_rejects_schema_drift(tmp_path):
    training = TrainingPipeline(tmp_path)
    df = _churn_frame()
    training.run(df, TaskSpec(task="classification", target="churned",
                              name="churn"))
    with pytest.raises(ValueError, match="schema mismatch"):
        InferencePipeline(tmp_path).run("churn", df.drop(columns=["monthly_spend"]))


def test_production_promotion_requires_human_approval(tmp_path):
    training = TrainingPipeline(tmp_path)
    training.run(_churn_frame(), TaskSpec(task="classification",
                                          target="churned", name="churn"))
    registry = ModelRegistry(tmp_path)
    with pytest.raises(PermissionError):
        registry.promote("churn", 1, "Production")
    card = registry.promote("churn", 1, "Production", approved_by="cto@corp")
    assert card["stage"] == "Production"
    assert card["approvals"][-1]["by"] == "cto@corp"
    # a second promoted version archives the first
    training.run(_churn_frame(seed=3), TaskSpec(task="classification",
                                                target="churned", name="churn"))
    registry.promote("churn", 2, "Production", approved_by="cto@corp")
    stages = {c["version"]: c["stage"] for c in registry.list("churn")}
    assert stages == {1: "Archived", 2: "Production"}


# ------------------------------------------------------------- monitoring
def test_monitor_flags_drift_and_triggers_retraining(tmp_path):
    training = TrainingPipeline(tmp_path)
    df = _churn_frame()
    training.run(df, TaskSpec(task="classification", target="churned",
                              name="churn"))
    monitor = ModelMonitor()
    _, eng, card = ModelRegistry(tmp_path).load("churn")
    same = monitor.assess_drift(card, eng.transform(
        df.drop(columns=["churned"])).X, eng.feature_names)
    assert not same["drift_detected"]

    drifted = df.copy()
    drifted["days_inactive"] = drifted["days_inactive"] + 500  # regime change
    live = eng.transform(drifted.drop(columns=["churned"]))
    moved = monitor.assess_drift(card, live.X, eng.feature_names)
    assert moved["drift_detected"]
    assert "days_inactive" in moved["drifted_features"]

    outcome = RetrainingPipeline(training).maybe_retrain("churn", drifted)
    assert outcome["verdict"]["should_retrain"]
    assert outcome["retrained"] is not None  # full re-selection ran


def test_reference_stats_shape():
    X = np.random.default_rng(0).normal(size=(100, 2))
    stats = reference_stats(X, ["a", "b"])
    assert set(stats) == {"a", "b"}
    assert len(stats["a"]["bin_edges"]) == 11

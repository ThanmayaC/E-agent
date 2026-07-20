# 03 · ML Platform & Neural Networks

The ML platform exists to answer one question with enterprise rigor:
**"which model, if any, earns the right to add evidence to this project?"**
Deterministic analytics remain the baseline; a model is admitted only when it
demonstrably beats that baseline under evaluation, and its predictions enter
the same Evidence Ledger as everything else — versioned, explained, and
citable.

## 1. Platform components

```
                     ┌─────────────────────────────────────────────┐
                     │                ML PLATFORM                   │
                     │                                             │
  DuckDB/Parquet ───▶│  FEATURE STORE          MODEL REGISTRY      │
  (data plane)       │  feature views,         MLflow: versions,   │
                     │  definitions-as-code,   stages, signatures, │
                     │  materialization,       model cards         │
                     │  lineage                                    │
                     │        │                      ▲             │
                     │        ▼                      │             │
                     │  TRAINING PIPELINES ──────────┘             │
                     │  (Celery jobs)                              │
                     │  select → train → backtest → explain →      │
                     │  register → (human approval) → promote      │
                     │        │                                    │
                     │        ▼                                    │
                     │  INFERENCE PIPELINES                        │
                     │  load Production version → predict →        │
                     │  SHAP/attention → ml_prediction EVIDENCE    │
                     │        │                                    │
                     │        ▼                                    │
                     │  MONITORING                                 │
                     │  Evidently drift + performance decay        │
                     │  → retraining graph trigger                 │
                     └─────────────────────────────────────────────┘
                              │ experiment tracking: MLflow
                              │ observability: OTel + Prometheus
```

## 2. Feature Store

Scope-appropriate by design (ADR-008): an internal store with Feast-compatible
interfaces, not Feast itself, until online serving at scale exists.

- **Definitions as code**: `ml/features/definitions/*.py` declare feature
  views (entity, source view/SQL over DuckDB, transformations, freshness).
  Reviewed like code, versioned like code.
- **Offline store**: materialized Parquet per project + feature view, hash-
  addressed so identical inputs are never recomputed (caching for free).
- **Point-in-time correctness**: time-join utilities prevent label leakage in
  training sets — non-negotiable for churn/LTV.
- **Lineage**: every materialization emits OpenLineage events
  (dataset → feature view → training set → model version).
- **Reuse**: features discovered by the deterministic layer (KPIs, quality
  stats, graph centralities, entity embeddings) are *first-class feature
  sources* — the platform's understanding feeds its models.

## 3. Model Registry, versioning, experiment tracking

MLflow (self-hosted, Postgres backend, artifacts on S3/MinIO):

- **Experiments**: every training run logs params, metrics, data hashes,
  feature view versions, git SHA.
- **Registry**: `None → Staging → Production → Archived` stage transitions;
  promotion to Production always passes a human-approval interrupt (02 §6.4).
- **Signatures**: enforced input/output schemas — inference fails fast on
  schema drift instead of silently predicting garbage.
- **Model cards**: generated per version — intended use, training window,
  eval scores vs baseline, known limitations, explainability method. The
  card's URI is attached to every `ml_prediction` evidence record.

## 4. Training & inference pipelines

Training runs on Celery workers (never in the API process), orchestrated as
typed pipeline classes:

```
TrainingPipeline.run(spec: TrainingSpec) -> RegisteredModel
  1. resolve feature views (point-in-time training set)
  2. Model Selection Framework → candidate list (§5)
  3. per candidate: fit → evaluate (§6) with time budget
  4. champion/challenger verdict vs deterministic baseline AND current champion
  5. explainability artifacts (SHAP summary / TFT importances)
  6. register in MLflow + model card; emit lineage
  7. request promotion approval (interrupt) if it beat the champion
```

Inference is synchronous-fast (ONNX/CPU for deep models) and always ends by
writing evidence:

```
InferencePipeline.run(model_version, entities) -> list[Evidence]
  Evidence(kind="ml_prediction",
           payload={target, horizon, value, interval, entity_id},
           model_version="churn@7",
           explanation={"shap_top": [...], "baseline_delta": ...},
           lineage=[feature_view_ids, dataset_ids])
```

**A prediction without model_version + explanation is rejected by the
ledger.** This is the ML analogue of the anti-hallucination rule.

## 5. Model Selection Framework (never hardcoded)

A three-stage funnel: **gates → priors → evaluation**. The rules the business
suggested (small→linear, medium→XGBoost, sequential→LSTM, long series→TFT)
become *priors that order the search*, never verdicts.

### 5.1 Meta-features (computed deterministically per task)

`n_rows, n_entities, n_features, feature types, missing rate, class balance,
series length, seasonality strength (STL), trend strength, intermittency,
exogenous covariate count, hierarchy depth, graph density`.

### 5.2 Eligibility gates (hard, statistical)

| Candidate family | Admitted only if |
|---|---|
| Linear/logistic, ETS/ARIMA | always eligible (baseline family) |
| XGBoost / LightGBM | ≥ 1 000 rows; ≥ 5 informative features |
| LSTM / DeepAR | ≥ 50 series steps × ≥ 20 entities, or ≥ 500 steps single-series |
| Temporal Fusion Transformer | ≥ 100 steps, multi-series, exogenous covariates present |
| Autoencoder anomaly | ≥ 10 000 transaction rows |
| Entity embeddings | categorical cardinality ≥ 50 with co-occurrence structure |
| GNN (future, behind interface) | graph density + labeled outcomes sufficient |

Gates exist so a 40-row Excel sheet can never spawn a transformer. Failing all
non-baseline gates is a **normal outcome**: the deterministic engine already
serves the answer, and the ML Agent records "no model admitted — insufficient
data" as a limitation evidence record (which the Recommendation Agent turns
into "collect more history").

### 5.3 Evaluation (the only judge)

- Tabular: nested CV, metric per task (AUC-PR for churn imbalance, pinball
  loss for quantile LTV).
- Time series: rolling-origin backtests, MASE + interval coverage — coverage
  matters because forecast gates consume intervals.
- **Champion/challenger**: a candidate is selected only if it beats (a) the
  deterministic baseline and (b) the incumbent, by a configured margin with
  overlap-aware uncertainty. Ties go to the simpler model (explainability and
  cost are tie-breakers, in that order).
- The full selection trace (meta-features, gates passed, scores, verdict) is
  stored on the run and rendered in the Models console — auditable AutoML,
  not a black box.

## 6. Monitoring, automatic retraining, governance

- **Evidently** jobs compare live feature/prediction distributions against
  training reference per model version → drift score.
- Decay triggers (drift > τ, coverage collapse, error growth vs actuals when
  ground truth arrives) enqueue the retraining graph (02 §6.4). Retraining
  re-runs the *selection framework*, not just refit — regime changes may
  change the winning family.
- Governance: promotion requires human approval; every Production transition
  is an audit record; models are project-scoped unless explicitly published
  as enterprise models.

## 7. Neural network architecture (only where justified)

| Module | Architecture | Genuine value / when the gate opens | Baseline it must beat |
|---|---|---|---|
| **Merchant growth prediction** | TFT (quantile heads) | Many merchant series + exogenous signals (category, region, fees); TFT shares strength across series and exposes variable importances | Per-series gated linear+seasonal (v2 engine) |
| **Customer churn** | GBM first; MLP with entity embeddings only at ≥ ~50k customers | Embeddings capture high-cardinality merchant/category interactions GBMs one-hot poorly | XGBoost |
| **Customer lifetime value** | Two-stage (BG/NBD-style probabilistic baseline → deep quantile regressor) | LTV needs distributions, not points; quantile heads feed confidence-aware recommendations | Probabilistic baseline |
| **Entity embeddings** (merchant/product/customer) | Skip-gram over co-transaction sequences or matrix factorization | Embeddings feed: semantic mapping similarity, KG link prediction, churn/LTV features, vector search over entities | Frequency/recency features |
| **Time-series DL** (long/multi-series) | LSTM/DeepAR → TFT per gates | Only family that handles hundreds of correlated series with covariates; quantile output keeps forecast validation gates intact | ETS/ARIMA + v2 gated trend |
| **Anomaly autoencoder** | Denoising AE on transaction feature vectors | Catches multivariate anomalies z-scores miss (odd *combinations*); reconstruction error → anomaly evidence with per-feature contributions | Z-score/IQR signals (kept — AE supplements) |
| **GNN** (future) | GraphSAGE on the KG | Fraud/risk propagation once labeled outcomes exist; interface reserved (`ml/models/graph/`), not built speculatively | Graph centrality features |

Implementation notes: PyTorch + pytorch-forecasting (TFT/DeepAR are solved
problems — no bespoke research code); CPU-friendly defaults + ONNX export;
quantile losses everywhere a downstream gate consumes intervals; explanations
extracted at inference (SHAP for trees, variable-selection weights for TFT,
reconstruction contributions for AE) and stored on the evidence record.

## 8. How ML output reaches the executive (end-to-end honesty)

```
TFT forecast for merchant M ──▶ ml_prediction evidence (interval, importances,
                                 model card v7, backtest coverage 91%)
        ──▶ forecast gates re-applied (poor coverage → low_confidence label)
        ──▶ Root Cause / Report agents may cite ev:… ids — verifier enforces
        ──▶ report renders: "STATISTICAL FINDING — churn model (v7, AUC-PR .81)
             ranks 214 customers high-risk; top driver: 60-day inactivity
             [ev:a4f2…]" with confidence and model card link
```

The executive never sees "AI predicts churn will rise." They see a versioned,
evaluated, explained, evidence-backed statement — or a labelled limitation
saying why no such statement can be made.

# V10.0 — Enterprise Intelligence, Trust & Natural UX

V10.0 is not about more features. It makes the platform behave like an
**experienced enterprise analyst**: it prefers deterministic analytics and real
ML over the LLM, explains *why* not just *what*, abstains when the evidence is
weak, and speaks in business language — never exposing the internal
simulation/generation clock.

## Multi-level intelligence

The platform no longer depends on a single LLM. Answers are assembled through
layers, and the LLM only ever *synthesises* what the lower layers have already
grounded:

1. **Deterministic** — KPIs, aggregations, statistics, business rules (the
   executive/ecosystem/evolution layers). No hallucination possible.
2. **ML (`app/ml_models`)** — real scikit-learn models trained on the cubes:
   - **Forecasting** — ridge regression on time + weekly seasonality + lag
     features, backtested (accuracy / MAPE) with a 95% confidence band.
   - **Anomaly detection** — IsolationForest over daily operating metrics.
   - **Segmentation** — KMeans over merchant behaviour (with silhouette).
   - **Churn** — RandomForest propensity over merchant health/growth.
   - **Failure** — GradientBoosting over per-bank reliability signals.
   Every prediction is tagged with **model, version, confidence, features and
   metrics (incl. feature importances)** — nothing is a black box.
3. **Knowledge graph & evidence** — relationships and supporting facts.
4. **Retrieval** — only the relevant documents (the workspace understanding +
   unified search), never the whole corpus.
5. **LLM** — used last, to phrase the answer, after context/evidence/KPIs/ML have
   been collected.

## Insight engine — explains WHY (`app/analyst/insights.py`)

Insights never restate a KPI. Each carries: root cause, impact, confidence (with
label), supporting evidence, alternative explanations, business risks,
recommended actions, expected ROI, implementation complexity, dependencies,
owner, priority — plus the **source layer and model** that produced it. A
**confidence gate** (floor 55%) flags low-evidence insights, and the shared
`gate()` returns *"I don't have enough verified evidence"* rather than
fabricating. Generators self-suppress when nothing is materially wrong (e.g. no
bank is actually at risk), so the analyst doesn't manufacture concern.

## Hide the internal timeline (`app/analyst/timeline.py`)

`BusinessTimeline` maps the technical clock onto the business calendar and
rewrites "Day 178 / Week 26 / Phase 2 / day_178" into "yesterday / last 30 days
/ December 2026". It is applied to copilot answers at the API boundary, so end
users see business timelines, not the generator's.

## Continuous learning (`app/analyst/learning.py`)

A file-backed store records what the user accepts/rejects, which questions recur,
and which files/dashboards are used — then re-ranks recommendations by learned
preference. No model is retrained; the system simply learns the user's taste.
Feedback is captured from the Insights cards (Accept / Dismiss).

## Performance (`app/analyst/cache.py`)

A TTL + LRU **semantic cache** (normalised query key) serves repeated
searches without recomputation and reports hit/miss stats. ML models are
memoised on the corpus signature, so they retrain only when the data changes.

## Surfaces & APIs

- **`/intelligence`** (frontend) — Insights (with feedback), Forecast (confidence
  band), Anomalies, Segments, Churn, Failure; every card shows model · version ·
  confidence · features.
- **API** — `/ml`, `/ml/models`, `/ml/forecast`, `/ml/anomalies`,
  `/ml/segments`, `/ml/churn`, `/ml/failure`, `/insights`, `/learning`,
  `/learning/feedback`, `/cache`.

## Honest constraints

- `xgboost` / `lightgbm` / `prophet` are not installed; sklearn equivalents
  (GradientBoosting, Ridge) are used.
- The simulated enterprise is currently healthy, so failure/churn risks read low
  and churn uses a propensity label — this is honest, not a defect: the models
  report the real state of the data.

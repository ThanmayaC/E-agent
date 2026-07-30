# Enterprise AI Orchestrator (V11)

The chat is no longer a single RAG call. Every question is now **understood,
classified, and routed** to the reasoning engines that actually own the answer,
and their outputs are merged into the evidence the LLM narrates. This is the
correction to the platform's central bug: a KPI-over-time question ("show UPI
trends from July 1 to July 20") was answered "no evidence found" because it was
sent to document retrieval, when a trend is *computed from the KPI series*, not
found in a document.

## What was already there (audited, reused — not rewritten)

The copilot pipeline was already an orchestrator in shape:
`intent → plan → context → evidence → (LLM | deterministic) → validate →
actions → remember` (`app/copilot/copilot.py`). Intent detection
(`copilot/intent.py`, 15 deterministic intents), the request planner
(`copilot/planner.py`), the grounding validator (`copilot/validator.py`), and
the multi-provider LLM router (`copilot/router.py`) were all in place.

The gap was **which facts reached the evidence set**: KPIs/forecasts were read
from empty per-project artifacts, and the real engines built in later milestones
— the analytics cubes (`executive/ecosystem.py`, `executive/evolution.py`), the
scikit-learn models (`ml_models/service.py`), and the insight engine
(`analyst/insights.py`) — were never wired into chat.

## The orchestration layer (`app/orchestrator/`)

Additive and modular. Each engine is independent and wraps a capability the
platform already owns; the orchestrator decides which run.

| File | Role |
|------|------|
| `base.py` | The `Engine` contract, `EngineRequest`, `EngineResult`, `EvidenceItem`. `timed()` runs an engine, times it, and turns any failure into an honest status. |
| `classifier.py` | `QueryClassifier` — intent → engine **categories** (analytics/knowledge/forecast/ml/recommendation/report/dashboard), plus **time-range** detection ("July 1 to July 20", "last 30 days") and **KPI**/entity extraction. Deterministic. |
| `engines/analytics.py` | **Analytics Engine** — KPI time series over the window the question names, from `daily_metrics`. Reports first→last, mean, min/max, % change, direction, and the equivalent SQL. *This is the Phase 11 fix.* |
| `engines/knowledge.py` | **Knowledge Engine** — RAG over the document corpus (reuses document intelligence). One engine among several, not the default. |
| `engines/ml.py` | **ML Engine** — anomaly / segmentation / churn / failure models, selected by the question. Each result carries its model card. |
| `engines/forecast.py` | **Forecast Engine** — the Ridge forecaster with backtest accuracy and confidence band. |
| `engines/recommendation.py` | **Recommendation Engine** — insight engine + executive recommendations, with confidence and the hallucination gate. |
| `engines/report.py` | **Report Engine** — existing reports surfaced by real title (Phase 10). |
| `router.py` | `EngineRouter` — selects engines via `can_handle` and runs them **in parallel**. |
| `orchestrator.py` | `EnterpriseOrchestrator` — `classify → route → run → merge`, plus the execution graph and observability record. |
| `__init__.py` | `build_orchestrator(container)` wires each engine to the layer it federates; `build_entity_vocab` reads banks/PSPs/merchants/products from the cubes. |

## Integration

`EnterpriseCopilot.chat()` runs the orchestrator after intent+plan (LLM answers
only), merges its engine evidence into the existing `Evidence` set (deduped by
id, so the validator still grounds every number), and attaches an
`orchestration` observability block to the answer. Off → the copilot behaves
exactly as before.

- Wired in the container as `self.ai_orchestrator`, after the ML/insight layers,
  gated by `settings.orchestrator_enabled` (`EDIP_ORCHESTRATOR_ENABLED`,
  default **on**, reversible). *Note: distinct from `self.orchestrator`, the
  pre-existing LangGraph/workflow orchestrator.*
- API: `GET /api/v1/copilot/orchestration?q=…` returns the classification, the
  engines it would run, and each engine's SQL / model / retrieved documents /
  timing (Phase 14). No `q` → the registered engines and categories.
- Frontend: a collapsible **"How this was answered"** panel on each answer
  (`pages/AIAssistant.jsx`) — intent, route, execution graph, and per-engine
  status/latency/SQL/model.

## Phase coverage

1 Intent ✓ (reused) · 2 Classification ✓ (`classifier.py`) · 3 Planner ✓ ·
4 Router ✓ (parallel) · 5 Analytics Engine ✓ · 6 Knowledge Engine ✓ ·
7 ML Engine ✓ · 8 Context Builder ✓ (evidence merge) · 9 LLM narrates a closed
set ✓ (reused) · 10 Source presentation ✓ · 11 Time-series reasoning ✓ ·
12 Hybrid ✓ · 13 Execution graph ✓ · 14 Observability ✓ · 15 Optimisation ✓
(engine selection avoids needless RAG/LLM; parallel execution; cube reads are
mtime-memoised).

## Verification

- `tests/unit/test_orchestrator.py` — 12 tests (classification routing, windowed
  trend computation, router selection, engine error handling, graph).
- Live: "Show UPI trends from July 1 to July 20" → the Analytics Engine returns
  the July series (Success Rate 99.49→99.98%, Technical Declines −96.4%, Volume
  −2.9%) with pseudo-SQL; the LLM narrates it; validation verdict **verified**.
  Previously: "no evidence found".

## Regenerate / toggle

Set `EDIP_ORCHESTRATOR_ENABLED=false` to fall back to the prior per-intent
evidence behaviour. The engines read the analytics cubes directly — no Brain
re-ingestion is needed for them.

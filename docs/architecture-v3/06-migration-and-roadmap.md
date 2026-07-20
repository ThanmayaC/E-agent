# 06 · Migration Plan & Implementation Roadmap

## 1. Module disposition

### 1.1 Retained (the deterministic core is the asset — do not rewrite)

| v2 module | v3 seat | Change |
|---|---|---|
| `intelligence/connectors/**` | Ingest node tools | none |
| `intelligence/dedup`, `profiling`, `timeseries` | Ingest/Understanding tools | none |
| `intelligence/semantics/**` (incl. embedding tier) | Understanding tools | embedder upgraded, logic kept |
| `intelligence/relationships` | Understanding tool | none |
| `intelligence/kpi`, `analytics`, `analytics/signals` | Quant Engine node | none |
| `intelligence/quality` | Quality node | none |
| `intelligence/forecasting` (validation gates) | Quant Engine node | gates also applied to ML forecasts |
| `intelligence/confidence` (assessor + report_confidence) | Confidence Gate node | formula extended with ML-evaluation term |
| `intelligence/recommendations` (rules engine) | Recommendation Agent tool | none |
| `agents/reasoning.py::_verify_evidence` + statement typing | `evidence/verifier.py` | persistence added, logic identical |
| `agents/prompt_generator.py` (evidence contract prompt) | agent prompt templates | split per agent, contract unchanged |
| `reports/generator.py`, `reports/markdown.py` | Assembler node | new sections only |
| `llm/**` (6 providers + factory) | LLM Gateway core | gateway wrapper added |
| `knowledge/store.py` (terms/rules/clarifications) | Knowledge service | Postgres persistence |
| `domain/**` | shared | extended (Evidence, Statement, plans) |
| Frontend pages (all 16) | Experience plane | v2 client swap; new consoles added |
| Delete-project semantics | extended per 04 §3 | more stores to purge |
| Test suite (34 tests incl. anti-hallucination contract) | golden tests | kept green throughout |

### 1.2 Rewritten / replaced

| v2 module | Replaced by | Reason |
|---|---|---|
| `workflows/analysis.py` (imperative pipeline) | LangGraph `graphs/analysis.py` | branching/interrupt/retry/parallelism/resume must be declarative and checkpointed |
| `workflows/engine.py` (workflow registry scaffold) | LangGraph graphs + Celery beat | superseded by real orchestration |
| `agents/base.py` agent framework + copilot/report_writer/specialists | `orchestration/agents/*` | LangGraph nodes with typed state replace the bespoke observe/plan/execute loop |
| `repositories/artifact_store.py` (JSON files as DB) | Postgres control plane + S3 + **compat facade** | concurrency, audit, RBAC, retention impossible on JSON files |
| `intelligence/graph/knowledge_graph.py` (NetworkX payload) | `knowledge/graph/` GraphStore (Kùzu/Neo4j) | persistence, Cypher reasoning, scale |
| `intelligence/embeddings/vector_store.py` (JSON vectors) | `knowledge/vectors/` (Qdrant/pgvector) | filtering, isolation, scale |
| `memory/manager.py` | scoped memory services (02 §4) | aligns memory with run/project/enterprise scopes |
| `tools/**` registry | `orchestration/tools/**` | typed tools with scope enforcement |

### 1.3 New

Evidence Ledger persistence · ML platform (features, selection, training,
inference, monitoring, explainability) · neural model families · retraining
graph · OIDC/RBAC/audit/lineage · OpenTelemetry stack · API v2 + SSE · new
frontend consoles · deployment profiles.

## 2. Migration plan (strangler — the platform never stops working)

Ground rules: `main` stays releasable; the 34-test suite (including the
anti-hallucination contract tests) passes at every merge; each phase ends
with the **golden-run harness** — replay recorded v2 analysis runs through
the new path and diff evidence, statements, and report structure.

**Phase A — Foundations (no behavior change).**
Introduce Postgres + Alembic, object store, DI profiles, OTel scaffolding.
Dual-write: artifact facade writes JSON (as today) *and* control-plane rows.
v1 API reads JSON. Exit: dual-write parity checker green on golden projects.

**Phase B — Evidence Ledger.**
Extract ledger + verifier from v2 inline logic; context builder writes
evidence records; statements + citations persisted. v1 endpoints served from
ledger through the facade. Exit: `/report/audit` output byte-compatible with
v2 for golden runs.

**Phase C — LangGraph strangler.**
Rebuild the pipeline as the analysis graph wrapping existing engines as
nodes; clarification gate becomes `interrupt()`; Postgres checkpointer; SSE
run events. The v2 imperative workflow remains behind a feature flag
(`orchestrator=legacy|langgraph`) until parity holds. Exit: golden runs
identical; pause/resume verified; flag defaults to `langgraph`; legacy
workflow deleted one release later.

**Phase D — Reasoning agents.**
Split the single report prompt into Planner / Root Cause / Recommendation /
Report agents; Supervisor with pass logic and repair loops. Mock-provider
tests extended per agent. Exit: verification failure rate ≤ v2 baseline on
golden runs; report structure unchanged for v1 consumers.

**Phase E — Knowledge services swap.**
GraphStore (Kùzu) and Qdrant behind existing interfaces; backfill per project
from stored profiles/relationships (re-run graph build); copilot upgraded to
RAG with retrieval evidence. Exit: graph/vector queries serve both API
versions; JSON stores removed.

**Phase F — ML platform.**
Feature store + MLflow + selection framework + first two model families
(gated GBM tabular, TFT/LSTM time series) + Evidently + retraining graph +
Models console. Exit: champion/challenger beats deterministic baseline on at
least one golden dataset *or* correctly declines to admit a model (both are
passing outcomes — the gate working is the feature).

**Phase G — Enterprise hardening.**
OIDC/RBAC/audit/lineage enforced; deletion extended to all stores; frontend
consoles (Run Graph, Evidence Explorer, Prompt Inspector, Lineage); v1 API
enters deprecation window (2 releases) once the UI is fully on v2.

Rollback: every phase is flag-gated; dual-write until Phase E means JSON
artifacts remain a functional fallback through Phases A–D.

## 3. Implementation roadmap

| Sprint(s) | Deliverable | Exit criterion |
|---|---|---|
| 1–2 | Phase A foundations | parity checker green; OTel traces visible |
| 3–4 | Phase B ledger | audit endpoint parity; citations queryable in SQL |
| 5–7 | Phase C LangGraph | golden-run parity; interrupt/resume demo; flag flipped |
| 8–9 | Phase D agents | multi-agent runs; verification metrics dashboarded |
| 10–11 | Phase E graph+vectors | Kùzu/Qdrant live; RAG copilot with citations |
| 12–15 | Phase F ML platform | registered, explained, gated models producing evidence; drift-triggered retraining demo |
| 16–18 | Phase G enterprise | SSO login; RBAC enforced; consoles shipped; v1 deprecation notice |

Team-shaped: phases A–C are platform-engineer work; D is AI-engineer work;
E–F parallelizable across two tracks; G is full-stack + security review.

## 4. Risks & mitigations

| Risk | Mitigation |
|---|---|
| LangGraph parity bugs corrupt trust | golden-run diff harness gates every merge; legacy flag until proven |
| Agent sprawl / cost explosion | 8-agent cap by ADR; Planner budgets + Supervisor circuit breaker; cost per run on the dashboard from Phase A |
| ML admitted without value | eligibility gates + champion/challenger vs deterministic baseline; "no model" is a first-class, reportable outcome |
| Verification weakened during refactor | contract tests (unsupported-fact downgrade, hypothesis forcing, citation resolution) are release-blocking |
| Ops burden for small deployments | lite profile (embedded Kùzu, pgvector, local disk) is a permanent, tested target — not an afterthought |

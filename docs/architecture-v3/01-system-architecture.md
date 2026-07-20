# 01 · System Architecture

## 1. Complete architecture

v3 is organized as five planes. Components communicate only through typed
contracts (Pydantic models + the Evidence Ledger), never through shared
in-process state — this is what allows every plane to scale independently.

```
                                 ┌──────────────────────────────┐
                                 │        EXPERIENCE PLANE      │
                                 │  React SPA · consoles · SSE  │
                                 └──────────────┬───────────────┘
                                                │ HTTPS (OIDC bearer)
                                 ┌──────────────▼───────────────┐
                                 │          API PLANE           │
                                 │ FastAPI v2 · RBAC middleware │
                                 │ v1 compatibility facade      │
                                 └──────┬───────────────┬───────┘
                              commands  │               │ queries
                                        ▼               ▼
 ┌──────────────────────────────────────────────┐   ┌──────────────────────────┐
 │              REASONING PLANE                 │   │      CONTROL PLANE       │
 │                                              │   │  Postgres:               │
 │  LangGraph runtime (checkpointed, resumable) │   │   projects, runs, events │
 │  ┌─────────────────────────────────────────┐ │   │   statements, citations  │
 │  │ Agents: Supervisor · Planner · Data     │ │   │   evidence index, models │
 │  │ Understanding · ML · Root Cause ·       │◄┼───┤   users/roles, audit,    │
 │  │ Recommendation · Report · Copilot       │ │   │   lineage, approvals     │
 │  ├─────────────────────────────────────────┤ │   │  LangGraph checkpointer  │
 │  │ Deterministic nodes: Ingest · Quality · │ │   └──────────────────────────┘
 │  │ Quant Engine · Graph Build · Index ·    │ │
 │  │ Confidence Gate · Verifier · Assembler  │ │   ┌──────────────────────────┐
 │  ├─────────────────────────────────────────┤ │   │       DATA PLANE         │
 │  │ Tools: SQL · features · registry ·      │ │   │  DuckDB per project      │
 │  │ graph query · vector search · knowledge │ │   │  Parquet on S3/MinIO     │
 │  └─────────────────────────────────────────┘ │   │  uploads, artifacts      │
 │        │              │              │       │   └──────────────────────────┘
 │        ▼              ▼              ▼       │
 │  ┌──────────┐  ┌────────────┐  ┌──────────┐ │   ┌──────────────────────────┐
 │  │ ML       │  │ Knowledge  │  │ LLM      │ │   │     EVIDENCE LEDGER      │
 │  │ Platform │  │ Services   │  │ Gateway  │ │   │  append-only typed facts │
 │  │ MLflow · │  │ Kùzu/Neo4j │  │ provider-│◄┼───┤  content-hashed ids      │
 │  │ features │  │ Qdrant ·   │  │ agnostic │ │   │  Postgres index +        │
 │  │ Evidently│  │ RAG        │  │ (exists) │ │   │  Parquet payloads        │
 │  └──────────┘  └────────────┘  └──────────┘ │   └──────────────────────────┘
 └──────────────────────────────────────────────┘
        Celery workers (training, long jobs) · Redis (queue, cache)
 ────────────────────────────────────────────────────────────────────────────
  FOUNDATIONS: OpenTelemetry traces · Prometheus metrics · OpenLineage lineage
               OIDC/Keycloak authn · Vault secrets · structured audit logging
```

### 1.1 The Evidence Ledger (new subsystem, promoted from v2's inline ids)

The single most important structure in the platform. An append-only store of
**evidence records**:

```python
class Evidence(BaseModel):
    id: str                  # "ev:" + content hash — stable, deduplicating
    project_id: str
    run_id: str
    kind: EvidenceKind       # kpi | signal | forecast | quality_issue |
                             # ml_prediction | graph_finding | retrieval |
                             # limitation | clarification_answer
    payload: dict            # the typed fact itself (KPI values, z-scores…)
    producer: str            # "quant.signals", "ml.churn.v3", "graph.paths"
    model_version: str | None    # set when produced by a registered model
    explanation: dict | None     # SHAP values / attention weights / rule trace
    lineage: list[str]       # upstream evidence/dataset ids
    created_at: datetime
```

Rules:
- **Producers** (deterministic engines, ML inference, graph reasoning) may
  only expose results by writing evidence.
- **Consumers** (LLM agents) receive evidence, never raw data; every generated
  statement carries `evidence_ids`; the deterministic Verifier rejects or
  downgrades uncited claims (v2 behaviour, now enforced at ledger level).
- **Statements** (LLM outputs) are stored with their citations in the control
  plane (`statements`, `citations` tables) — this is what makes every report
  auditable and every hallucination structurally impossible to present as fact.

### 1.2 Component inventory

| Component | Plane | Carries over from v2? |
|---|---|---|
| Connectors (Excel/CSV/PDF/Word/SQL/API) | Reasoning (tools) | Yes — unchanged |
| Profiler, semantics, relationships, KPI discovery, signals, quality, forecast gates | Reasoning (deterministic nodes) | Yes — wrapped as nodes |
| Confidence assessor + clarification gate | Reasoning (gate node + interrupt) | Yes — re-seated on LangGraph |
| Evidence verification | Reasoning (Verifier node) | Yes — extended to ledger |
| Report assembler + markdown | Reasoning (Assembler node) | Yes |
| LLM provider layer (ollama/openai/azure/anthropic/gemini/mock) | LLM Gateway | Yes — becomes gateway with cost metering |
| Orchestration (`workflows/analysis.py`) | — | **Replaced** by LangGraph graph |
| Artifact JSON store | — | **Replaced** by control plane + object store (facade kept for v1 API) |
| NetworkX graph | Knowledge services | **Replaced** by GraphStore (Kùzu default) |
| JSON vector store | Knowledge services | **Replaced** by Qdrant adapter |
| ML platform, feature store, registry, monitoring | ML platform | **New** |
| AuthN/Z, audit, lineage, telemetry | Foundations | **New** |

---

## 2. Why this shape (summary — full ADRs in 07)

- **Five planes** because the failure modes differ: reasoning is stateless and
  horizontally scalable; control demands ACID and audit; data demands columnar
  throughput. Fusing them (v2's JSON-files-as-database) caps concurrency and
  makes RBAC/audit impossible.
- **Ledger between planes** because "no unsupported statements" must be an
  *architectural invariant*, not a prompt instruction. The prompt asks; the
  Verifier + ledger *enforce*.
- **LangGraph** because the platform's real control flow is a graph with
  branches (confidence gate), interrupts (human answers), retries, parallel
  fan-out (quality ∥ analytics ∥ graph ∥ indexing), and re-entry (supervisor
  ordering another pass). v2 encodes this in imperative Python; LangGraph makes
  it declarative, checkpointed, resumable, and observable.

---

## 3. Technology stack (each with its enterprise purpose)

| Layer | Technology | Justified purpose (not popularity) |
|---|---|---|
| Orchestration | **LangGraph** | Typed shared state, Postgres checkpointing, native `interrupt()` for human-in-the-loop, per-node retry policy, parallel branches. Exactly matches the pause/resume clarification flow we already ship. |
| Agent LLMs | Existing provider layer → **LLM Gateway** | Provider-agnostic (ollama/openai/azure/anthropic/gemini) already built; gateway adds token/cost metering, prompt logging, response caching. |
| Control DB | **PostgreSQL 16** | ACID metadata, concurrent runs, RBAC/audit/lineage tables, LangGraph checkpointer backend, pgvector fallback. The JSON artifact store cannot do concurrent multi-user audit. |
| Analytical engine | **DuckDB + Parquet** (keep) | Columnar, embedded, zero-ops, already proven in v2 for Excel-scale to multi-GB analytics. Parquet on object store adds durability + lineage. |
| Object storage | **S3 / MinIO** | Uploads, artifacts, model binaries, Parquet. MinIO self-hosted = same API as AWS S3 for cloud deployment. |
| Queue / jobs | **Celery + Redis** (keep) | Already integrated. Training jobs, scheduled retraining, report generation off the request path. |
| Vector DB | **Qdrant** (pgvector as degraded mode) | Payload-filtered ANN (org/project isolation *inside* the index), hybrid search, snapshots. JSON vector file cannot filter, scale, or isolate tenants. |
| Knowledge graph | **Kùzu** embedded (default) / **Neo4j** (enterprise option) | Cypher property graph with typed schema. Kùzu = embedded, zero-ops, columnar (fits our deployment model); Neo4j adapter for orgs that mandate it. NetworkX kept only as in-memory algorithm library (centrality, communities). |
| Experiment tracking / registry | **MLflow** | Industry standard, self-hostable, model versioning + stage transitions + signature enforcement + artifact storage. Building a registry by hand is undifferentiated heavy lifting. |
| Classical ML | **scikit-learn, XGBoost, LightGBM, statsmodels** | The champion/challenger baseline family. Statistical rigor before deep learning. |
| Deep learning | **PyTorch + pytorch-forecasting** | LSTM/DeepAR and Temporal Fusion Transformer with quantile heads (native prediction intervals → forecast gates keep working); entity embeddings; autoencoder anomaly. ONNX export for CPU inference. |
| Drift / model monitoring | **Evidently** | Data + prediction drift reports as code, feeds automatic retraining triggers. |
| Explainability | **SHAP** (trees), attention/variable-importance (TFT) | Explanations are *required fields* on ml_prediction evidence — a prediction without explanation is rejected by the ledger. |
| Observability | **OpenTelemetry + Prometheus + Grafana** (LangSmith optional) | Traces: run → agent → tool → LLM call spans. Metrics: latency, token cost, verification failure rate, drift. |
| Lineage | **OpenLineage** events | Dataset → feature → model → evidence → statement chain, queryable for audit ("which upload produced this recommendation?"). |
| AuthN | **OIDC (Keycloak / Entra ID)** | Enterprise SSO; the platform never stores passwords. |
| Secrets | **Vault / cloud KMS** (env-var fallback) | Provider keys, DB credentials out of config files. |
| API | **FastAPI** (keep) + SSE | Already proven; v2 API adds streaming run events and RBAC dependency injection. |
| Frontend | **React + Vite + Tailwind + ECharts + React Flow** (keep) | React Flow already renders the knowledge graph; it will render agent execution graphs. No rewrite — extension. |

Deliberately **not** adopted (and why): Kafka (no event volume yet — Redis
streams suffice until multi-source streaming lands), Spark (DuckDB covers the
data plane at this scale; revisit >100 GB), Kubernetes-only deployment (ship
docker-compose profiles; k8s manifests provided but not required), Feast
(feature store interfaces are Feast-compatible so we can adopt it when online
serving at scale is needed — ADR-008).

---

## 4. Data flow

### 4.1 Ingest → decision (the platform's core loop)

```
 upload (xlsx/csv/pdf/…)
    │
    ▼
 [Ingest node]  connectors → raw tables → Parquet snapshot (S3)     lineage: dataset ids
    │
    ▼
 [Data Understanding Agent]                                          evidence: schema facts
    profiler → semantics → relationships (tools)                     + limitation records
    LLM resolves ambiguity or drafts clarifications
    │
    ▼
 [fan-out — parallel]
    ├─ [Quality node]        → quality_issue evidence
    ├─ [Quant Engine node]   → kpi / signal / forecast evidence (gated)
    ├─ [Graph Build node]    → knowledge graph upsert + graph_finding evidence
    └─ [Index node]          → embeddings → Qdrant collections
    │
    ▼
 [Confidence Gate node]  deterministic scoring → below threshold?
    │                         │ yes → interrupt() → human answers → resume
    ▼ no
 [ML Agent]  model selection framework → feature store → train/infer
    │        → ml_prediction evidence (+ SHAP, + model version)
    ▼
 [Root Cause Agent ∥ Recommendation Agent]                           statements (draft)
    graph paths + vector precedents + drilldown SQL as tools
    │
    ▼
 [Verifier node]  deterministic: citations resolve? types legal?     statements (verified/
    uncited facts → downgraded hypotheses                             downgraded)
    │
    ▼
 [Report Agent] → [Assembler node] → executive report + dashboard artifacts
    │
    ▼
 [Supervisor]  confidence sufficient? another pass? human sign-off?
    │
    ▼
 READY  (report, evidence explorer, copilot all live)
```

### 4.2 Storage touch-points per stage

| Stage | Reads | Writes |
|---|---|---|
| Ingest | uploads (S3) | Parquet snapshot, DuckDB tables, `datasets` rows, lineage events |
| Understanding | DuckDB samples | evidence (schema, limitations), clarification questions |
| Quality/Quant/Graph/Index | DuckDB | evidence records, graph upserts, Qdrant points |
| ML | feature store views | MLflow runs/models, ml_prediction evidence |
| Reasoning agents | **evidence ledger only** | statements + citations (control plane) |
| Verifier | statements + ledger index | verification verdicts, downgrades, audit rows |
| Report | verified statements + evidence | report artifact (S3), `reports` row, version++ |

The reasoning agents' read set — *ledger only* — is the anti-hallucination
contract expressed as a data-flow constraint.

---

## 5. Folder structure (monorepo)

```
edip/
├── backend/
│   ├── app/
│   │   ├── main.py                     # app factory, telemetry bootstrap
│   │   ├── core/                       # settings, DI container, logging
│   │   │   ├── config.py
│   │   │   ├── container.py
│   │   │   ├── security/               # OIDC, RBAC, audit middleware
│   │   │   └── telemetry/              # OTel setup, metrics, cost meter
│   │   ├── domain/                     # Pydantic entities & enums (kept, extended)
│   │   │   ├── entities.py
│   │   │   ├── evidence.py             # Evidence, Statement, Citation
│   │   │   └── enums.py
│   │   ├── api/
│   │   │   ├── v1/                     # compatibility facade (existing routes)
│   │   │   └── v2/                     # runs, evidence, models, graph, vectors,
│   │   │       │                       #   copilot (SSE), admin, auth
│   │   ├── orchestration/              # ── LangGraph runtime ──
│   │   │   ├── state.py                # AnalysisState, CopilotState schemas
│   │   │   ├── graphs/
│   │   │   │   ├── analysis.py         # main graph assembly
│   │   │   │   ├── copilot.py          # interactive graph
│   │   │   │   └── retraining.py       # drift → retrain graph
│   │   │   ├── agents/                 # the 8 true agents
│   │   │   │   ├── supervisor.py
│   │   │   │   ├── planner.py
│   │   │   │   ├── understanding.py
│   │   │   │   ├── ml.py
│   │   │   │   ├── root_cause.py
│   │   │   │   ├── recommendation.py
│   │   │   │   ├── report.py
│   │   │   │   └── copilot.py
│   │   │   ├── nodes/                  # deterministic nodes
│   │   │   │   ├── ingest.py
│   │   │   │   ├── quality.py
│   │   │   │   ├── quant.py            # analytics + signals + forecasts
│   │   │   │   ├── graph_build.py
│   │   │   │   ├── index.py
│   │   │   │   ├── confidence_gate.py
│   │   │   │   ├── verifier.py
│   │   │   │   └── assembler.py
│   │   │   └── tools/                  # typed tools exposed to agents
│   │   │       ├── sql.py, features.py, registry.py,
│   │   │       ├── graph_query.py, vector_search.py, knowledge.py
│   │   ├── intelligence/               # deterministic engines (KEPT from v2)
│   │   │   ├── connectors/ profiling/ semantics/ relationships/
│   │   │   ├── kpi/ analytics/ quality/ forecasting/ confidence/
│   │   │   ├── recommendations/ context/ dedup/ timeseries/
│   │   ├── evidence/                   # ── Evidence Ledger ──
│   │   │   ├── ledger.py               # append, index, resolve, hash ids
│   │   │   ├── verifier.py             # deterministic verification (from v2)
│   │   │   └── statements.py           # statement/citation persistence
│   │   ├── ml/                         # ── ML platform ──
│   │   │   ├── features/               # feature store (views, definitions, lineage)
│   │   │   ├── selection/              # model selection framework
│   │   │   ├── training/               # pipelines (celery tasks)
│   │   │   ├── inference/
│   │   │   ├── models/                 # model families: tabular, ts_classical,
│   │   │   │                           #   ts_deep (LSTM/TFT), embeddings, autoencoder
│   │   │   ├── evaluation/             # backtests, champion/challenger
│   │   │   ├── monitoring/             # Evidently drift, retrain triggers
│   │   │   └── explain/                # SHAP / attention extraction
│   │   ├── knowledge/                  # enterprise knowledge (kept) + services
│   │   │   ├── store.py                # terms, rules, clarifications (kept)
│   │   │   ├── graph/                  # GraphStore iface, kuzu_store, neo4j_store,
│   │   │   │                           #   reasoning.py (paths, motifs, centrality)
│   │   │   └── vectors/                # VectorStore iface, qdrant_store, collections
│   │   ├── llm/                        # provider layer (kept) + gateway.py
│   │   ├── repositories/               # control-plane repos (SQLAlchemy),
│   │   │                               #   object_store.py, artifact facade (v1 compat)
│   │   ├── workers/                    # celery app + task modules
│   │   └── reports/                    # assembler + renderers (kept, extended)
│   ├── alembic/                        # control-plane migrations
│   ├── tests/                          # unit / integration / golden-run
│   └── pyproject.toml
├── frontend/
│   └── src/
│       ├── api/                        # v2 client + SSE hooks
│       ├── pages/                      # existing pages + RunGraph, Evidence,
│       │                               #   Models, PromptInspector, Lineage
│       └── components/
├── deploy/
│   ├── docker-compose.yml              # full stack profile
│   ├── docker-compose.lite.yml         # embedded profile (Kùzu, pgvector, no MinIO)
│   └── k8s/                            # optional manifests
└── docs/architecture-v3/               # this document set
```

Two deployment profiles are a hard requirement: **lite** (single container +
Postgres; Kùzu embedded, pgvector, local disk) for evaluation and small teams,
and **full** (Qdrant, MinIO, Keycloak, Grafana) for enterprise. Same code,
adapters chosen by config — this is why every external system sits behind an
interface (`GraphStore`, `VectorStore`, `ObjectStore`, `FeatureStore`).

# 05 · Platform Engineering — Backend, API, Data, Security, Frontend, Observability, Performance

## 1. Backend redesign

The backend reorganizes from "pipeline + helpers" into four clearly bounded
runtime roles (all from one codebase, selected by entrypoint):

| Process | Runs | Scaling |
|---|---|---|
| `api` | FastAPI v2 + v1 facade, SSE event streaming | horizontal, stateless |
| `orchestrator` | LangGraph runs (analysis/copilot/retraining graphs) | horizontal; state in Postgres checkpoints |
| `worker` | Celery: training, materialization, drift jobs, deletion | horizontal, queue-partitioned (`ml`, `io`, `default`) |
| `beat` | schedules: drift scans, retention, report refresh | single |

Key structural changes from v2:

1. **`orchestration/` replaces `workflows/`** — the imperative script becomes
   graphs + agents + nodes + tools (02). The intelligence engines under
   `app/intelligence/**` are **kept as-is** and wrapped as nodes/tools; they
   are the platform's crown jewels, not its debt.
2. **`evidence/` is a new bounded context** — ledger, verifier, statements.
   v2's inline evidence ids and `_verify_evidence` migrate here unchanged in
   spirit, gaining persistence and lineage.
3. **Repositories split**: control-plane repos (SQLAlchemy/Postgres), object
   store repo (S3), and a legacy `ArtifactStore` facade that keeps every v1
   endpoint working during migration (06 §2).
4. **LLM Gateway**: the existing provider layer gains a gateway wrapper —
   request/response logging, token & cost metering, response caching (hash of
   messages+model), provider failover. Agents depend on the gateway, never on
   providers.
5. **DI container** (exists) extends to bind interfaces → adapters per
   deployment profile (lite/full).

## 2. API redesign

`/api/v2` — resource-oriented, run-centric, streaming-first. `/api/v1`
remains as a facade over the same services (zero breakage for the current UI
during migration).

### Core resources

| Method | Path | Purpose |
|---|---|---|
| POST | `/v2/projects` / GET `/v2/projects` | project lifecycle (+ RBAC scoping) |
| DELETE | `/v2/projects/{id}` | full deletion per 04 §3 (async job + audit) |
| POST | `/v2/projects/{id}/files` | upload (multipart, presigned-URL option) |
| POST | `/v2/projects/{id}/runs` | start a run `{graph: analysis\|refresh, params}` |
| GET | `/v2/runs/{run_id}` | run state, pass count, budgets, approvals |
| GET | `/v2/runs/{run_id}/events` | **SSE**: node lifecycle, agent tokens, progress |
| GET | `/v2/runs/{run_id}/graph` | execution graph (nodes, edges, status, timings) for the UI |
| GET | `/v2/runs/{run_id}/interrupts` | pending human inputs (clarifications, sign-offs) |
| POST | `/v2/runs/{run_id}/resume` | submit answers/approvals → `Command(resume)` |

### Evidence & reasoning (the audit surface)

| Method | Path | Purpose |
|---|---|---|
| GET | `/v2/projects/{id}/evidence?kind=&producer=` | ledger query |
| GET | `/v2/evidence/{eid}` | one record + lineage + consumers ("which statements cite this?") |
| GET | `/v2/projects/{id}/statements?type=&verification=` | all AI statements with citations |
| GET | `/v2/projects/{id}/reports/latest` · `/reports/{version}` | versioned reports |
| GET | `/v2/projects/{id}/limitations` | deterministic data limitations |
| POST | `/v2/projects/{id}/copilot` | streaming grounded chat (citations inline) |

### ML, graph, vectors, admin

| Method | Path | Purpose |
|---|---|---|
| GET | `/v2/projects/{id}/models` · `/models/{name}/versions` | registry view, cards, metrics |
| POST | `/v2/models/{name}/versions/{v}/promote` | promotion (approval-gated) |
| GET | `/v2/projects/{id}/features` | feature views + freshness |
| POST | `/v2/projects/{id}/graph/query` | parameterized Cypher templates (not raw Cypher from UI) |
| POST | `/v2/projects/{id}/vectors/search` | filtered similarity search |
| GET | `/v2/projects/{id}/lineage?node=` | OpenLineage graph slice |
| GET | `/v2/admin/audit` · `/admin/costs` · `/admin/usage` | governance consoles |

Conventions: cursor pagination, `Idempotency-Key` on POSTs, RFC 7807 problem
details, ETags on reports, per-org rate limits at the gateway.

## 3. Database redesign

Polyglot by plane — each store does the one job it is best at (ADR-007):

| Store | Role |
|---|---|
| **PostgreSQL** | control plane (below) + LangGraph checkpoints + MLflow backend |
| **DuckDB** (per project) | analytical tables, drilldown SQL, previews |
| **Parquet on S3/MinIO** | immutable dataset snapshots, feature materializations, artifacts, model binaries |
| **Qdrant** | vector collections (04 §2) |
| **Kùzu/Neo4j** | knowledge graph (04 §1) |
| **Redis** | queues, response cache, rate limits, SSE fan-out pub/sub |

### Control-plane schema (Postgres, principal tables)

```
orgs(id, name, settings)
users(id, org_id, subject, email, display_name)          -- subject = OIDC sub
roles(user_id, org_id, project_id NULL, role)             -- owner|analyst|viewer|admin
projects(id, org_id, name, status, created_by, created_at, deleted_at)
datasets(id, project_id, name, parquet_uri, duckdb_table, schema_hash, row_count, lineage_run)
runs(id, project_id, graph, status, passes, budget_tokens, cost_usd,
     started_at, finished_at, triggered_by)
run_events(id, run_id, seq, node, event, payload_jsonb, at)      -- SSE source + replay
interrupts(id, run_id, node, kind, payload_jsonb, resolved_by, resolved_at)
evidence(id, project_id, run_id, kind, producer, payload_jsonb,
         model_version, explanation_jsonb, content_hash UNIQUE, created_at)
evidence_lineage(evidence_id, upstream_type, upstream_id)
statements(id, run_id, section, statement_type, text, confidence,
           verification, rejected_ids_jsonb)
citations(statement_id, evidence_id)                              -- the audit join
reports(project_id, version, uri, confidence_jsonb, generated_at, approved_by)
models(id, org_id, project_id NULL, name, task, current_stage)    -- mirror of MLflow
model_metrics(model_id, version, metric, value, window, at)
feature_views(id, project_id, name, definition_hash, freshness_at)
approvals(id, kind, subject_id, requested_at, decided_by, decision, reason)
audit_log(id, org_id, actor, action, resource, before_jsonb, after_jsonb, at, ip)
lineage_events(id, ol_event_jsonb, at)                            -- OpenLineage feed
```

`statements` × `citations` × `evidence` is the platform's constitutional
core: every AI sentence, its type, its verification verdict, and exactly which
deterministic facts it rests on — queryable with one join.

Retention: `run_events` partitioned monthly; evidence payloads over size
threshold spill to Parquet with the row keeping the URI.

## 4. Security

| Requirement | Design |
|---|---|
| **Authentication** | OIDC (Keycloak self-hosted or Entra ID/Okta). API validates JWTs; no local passwords. Service-to-service via client-credentials. |
| **RBAC** | Roles: `org_admin`, `project_owner`, `analyst`, `viewer` + capability flags (approve models, answer clarifications, delete projects). Enforced as FastAPI dependencies **and** re-checked in the tool layer — an agent inherits the *run initiator's* scope, so a prompt injection cannot widen access. |
| **Audit** | Every mutating action + every approval + every LLM call (prompt hash, model, cost) → `audit_log`. Append-only, exportable to SIEM. |
| **Data lineage** | OpenLineage events at every hop (upload → dataset → feature → model → evidence → statement → report); surfaced in the Lineage console; answers "which upload produced this recommendation?" in one query. |
| **Encryption** | TLS everywhere; Postgres + object store encryption at rest; per-org S3 prefixes with distinct keys (KMS). |
| **Secrets** | Vault or cloud secret manager; env-var fallback for lite profile; no secrets in config files or the DB. |
| **Project isolation** | project_id scoping in control plane, per-project DuckDB files, payload-filtered vectors, provenance-scoped graph, prefix-scoped object storage. Tenant claims flow through the whole tool chain. |
| **LLM-specific** | Prompt-injection containment: tools validate arguments against the caller's scope; retrieved content is data, never instructions (already the platform's doctrine); egress allow-list for LLM providers; PII redaction hook in the gateway (pluggable). |

## 5. Frontend redesign

Keep the stack (React/Vite/Tailwind/ECharts/React Flow) and every existing
page; add the operational consoles that make the platform *feel* like an
enterprise AI product. New v2 API client with SSE hooks.

| Console | Content | Source |
|---|---|---|
| **Run Graph** (new) | live LangGraph execution: nodes light up, timings, retries, pass count; click node → inputs/outputs/logs; interrupt nodes render the approval UI inline | `/runs/{id}/graph` + SSE (React Flow — already a dependency) |
| **Evidence Explorer** (new) | ledger browser: filter by kind/producer/run; evidence detail shows payload, lineage graph, model card, *and every statement citing it* (reverse citations) | `/evidence` |
| **Confidence Dashboard** (upgrade) | deterministic report confidence with component drill-down (formula visualization), per-category understanding, verification pass/fail rates over time | `/reports`, `/statements` |
| **Models** (new) | registry: versions, stages, eval vs baseline, drift charts, feature importance (SHAP summary), promote button (approval-gated) | `/models`, `/model_metrics` |
| **Knowledge Graph Explorer** (upgrade) | existing React Flow view + Cypher-template query bar, path highlighting from graph_finding evidence | `/graph/query` |
| **Prompt Inspector** (new) | per LLM call: rendered prompt, evidence supplied, raw response, validation/verification outcome, tokens & cost (analyst+ role only) | gateway logs |
| **Lineage** (new) | upload → report chain visualization | `/lineage` |
| **Workflow visualization** (upgrade) | run history, schedules, retraining runs, budgets | `/runs` |

Existing Projects page keeps v2.1 features (delete + confirm, upload progress,
duration, report version/timestamp, confidence badge) and adds run-centric
status (pass count, pending approvals).

## 6. Observability

- **OpenTelemetry traces**: `run → node → agent → tool → llm_call` span tree;
  span attributes carry run_id/project_id/model/token counts; exported OTLP
  (Grafana Tempo / vendor).
- **Metrics (Prometheus)**: run duration by graph/node; LLM latency, token
  and **cost per run/org/provider**; verification failure rate (the platform's
  north-star quality metric); forecast gate outcomes; drift scores; queue
  depth; cache hit rates.
- **Logs**: structured JSON with trace ids. Dedicated streams: prompt log
  (gateway), evidence log (ledger appends), confidence log (gate decisions),
  agent decision log (supervisor/planner rationales).
- **Failure analysis**: every failed run stores its state snapshot +
  offending node + last-good checkpoint → one-click replay from checkpoint in
  the Run Graph console.
- **LangSmith** (optional flag) for teams that want hosted trace UX; OTel
  remains the system of record.

## 7. Performance

| Requirement | Design |
|---|---|
| Parallel agents | LangGraph fan-out (quality ∥ quant ∥ graph ∥ index); Root Cause ∥ Recommendation; asyncio for I/O-bound tools |
| Caching | content-hash everything: dataset snapshots (skip re-profiling unchanged files), feature materializations, LLM gateway response cache, embedding cache keyed by chunk hash |
| Incremental analysis | `refresh` graph variant: schema hash unchanged → reuse understanding + mappings, recompute only quant + downstream; new file appended → delta ingest + affected-evidence invalidation via lineage |
| Background jobs | training, indexing, deletion, drift scans on Celery; API never blocks |
| Streaming | SSE run events; token streaming for copilot and report narration; Redis pub/sub fan-out across API replicas |
| Async processing | FastAPI async endpoints; async DB drivers; DuckDB reads via thread pool executor |
| Budgets | Planner-assigned token/time budgets per agent; Supervisor aborts pass 3+; cost circuit breaker per org/day |

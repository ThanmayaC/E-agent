# REST API Reference

Base URL: `/api/v1` · Interactive docs: `http://localhost:8000/docs` (OpenAPI/Swagger)

## Projects & pipeline

| Method | Path | Description |
|---|---|---|
| POST | `/projects` | Create a project. Body: `{"name": "Q3 Portfolio"}` |
| GET | `/projects` | List projects (newest first) |
| GET | `/projects/{id}` | Project state incl. files and stage runs |
| POST | `/projects/{id}/files` | Multipart upload (`files`): `.xlsx .xlsm .xls .csv`, many at once |
| POST | `/projects/{id}/analyze` | Start the 18-stage pipeline (202 Accepted) |
| GET | `/projects/{id}/status` | `{status, stages:[{stage, status, started_at, ...}]}` |

## Artifacts (available once status = `ready`)

| Method | Path | Returns |
|---|---|---|
| GET | `/projects/{id}/datasets` | Table profiles: rows, columns, entity, fact/dimension, merge lineage |
| GET | `/projects/{id}/datasets/{dsId}/preview?limit=50` | `{columns, rows}` sample |
| GET | `/projects/{id}/semantics` | Semantic layer: column → concept/type/role/canonical/confidence |
| GET | `/projects/{id}/relationships` | Detected joins with cardinality, overlap, evidence |
| GET | `/projects/{id}/graph` | Knowledge graph `{nodes, edges, stats}` (React Flow ready) |
| GET | `/projects/{id}/kpis` | Discovered KPIs with sparklines, growth, forecast |
| GET | `/projects/{id}/signals` | Deterministic statistical signals (numeric facts only) |
| GET | `/projects/{id}/context` | Compact business-context JSON — the only payload sent to the LLM |
| GET | `/projects/{id}/ai-report` | Full structured LLM output (all narrative sections) |
| GET | `/projects/{id}/insights` | AI-generated: key insights, root causes, risks, opportunities |
| GET | `/projects/{id}/predictions` | Forecasts with intervals and method |
| GET | `/projects/{id}/recommendations` | AI-generated recommendations + priority actions |
| GET | `/projects/{id}/quality` | Quality report: score, per-dataset scores, issues |
| GET | `/projects/{id}/breakdowns` | Auto-generated measure × dimension aggregates |
| GET | `/projects/{id}/report` | Fixed-structure executive report (JSON) |
| GET | `/projects/{id}/report/markdown` | Same report rendered as Markdown |

## Copilot & analytics

| Method | Path | Description |
|---|---|---|
| POST | `/projects/{id}/copilot/chat` | Body `{"question": "Why did growth slow?"}` → `{answer, intent, sources, kpis, insights}` |
| POST | `/projects/{id}/query` | Body `{"sql": "SELECT ..."}` — read-only SELECT against the project's DuckDB warehouse |

## Runtime Dashboard (autonomous execution layer)

Everything the platform does on its own is observable and controllable here.

| Method | Path | Description |
|---|---|---|
| GET | `/runtime` | Is the agent autonomous now: scheduler, events, queue, triggers, goals, plans, decisions, approval policy |
| GET | `/runtime/activity` | Autonomous Activities: running workflows, recent runs/actions/events/executions, pending approvals |
| GET | `/runtime/scheduler` | Heartbeat status: ticks, jobs by kind, runs, failures, degraded jobs |
| POST | `/runtime/scheduler/start` · `/stop` | Start (idempotent: startup jobs, then ticks) or stop the heartbeat |
| GET | `/runtime/jobs` | Every job: kind, cadence, dependencies, retry policy, last/next run, failures |
| POST | `/runtime/jobs/{name}/run` | Run a job now, outside its schedule |
| PATCH | `/runtime/jobs/{name}` | `{"enabled": false}` — disable a job without removing it |
| GET | `/runtime/events` | Event stream (`?kind=`, `?project_id=`) + stats + live subscriptions |
| GET | `/runtime/executions` | Job execution history (`?job=`) with duration, attempts, result |
| GET | `/runtime/actions` | The action queue (`?status=`, `?kind=`, `?project_id=`) |
| POST | `/runtime/actions` | Queue an action manually |
| GET | `/runtime/queue` | Execution centre: stats, approval policy, pending, in-flight, recent |
| POST | `/runtime/actions/{id}/approve` · `/reject` | The human approval layer. Body `{"by": "cfo", "reason": ""}` |
| POST | `/runtime/actions/{id}/execute` · `/retry` | Execute an approved action now; retry a failed one (approval is not re-asked) |
| GET | `/runtime/goals` | Objectives with KPI attainment and progress |
| POST | `/runtime/goals` | Define an objective — the platform plans it and starts immediately |
| GET | `/runtime/goals/{id}` | One goal with its active plan |
| PATCH | `/runtime/goals/{id}` | `{"status": "paused"}` |
| POST | `/runtime/goals/{id}/measure` | Record a KPI measurement: `{"kpi": "revenue", "value": 120}` |
| GET | `/runtime/metrics` | Metric names a KPI can point at, with current values |
| GET | `/runtime/plans` | Plans (`?status=`, `?goal_id=`) with every step and its state |
| POST | `/runtime/plans/{id}/advance` · `/replan` | Move a plan forward; revise it |
| GET | `/runtime/decisions` | Every autonomous decision with its full pipeline trace |
| GET | `/runtime/triggers` | Rule-based automation, with fire counts |
| POST | `/runtime/triggers` | Add a rule (no deploy). See the condition language below |
| PATCH | `/runtime/triggers/{id}` · DELETE | Enable/disable or remove a rule |

### Trigger rule contract

```json
{
  "name": "health_drop_creates_task",
  "event": "PortfolioChanged",
  "action": "create_task",
  "conditions": [{"field": "health_change", "op": "lte", "value": -5}],
  "params": {"title": "Review the decline in portfolio health", "priority": 1}
}
```

`event` must be a known event kind; `action` must name a registered handler,
which always routes through the Action Queue — a rule can never execute
arbitrary code or bypass approval. `field` is a dotted path into the event
payload (`risk.severity`); `op` is one of `eq ne gt gte lt lte contains in
exists not_exists abs_gte`. All conditions must hold (AND); no conditions
fires on the event alone.

## Knowledge Synchronization (connected enterprise systems)

| Method | Path | Description |
|---|---|---|
| GET | `/sources` | Every configured source + the kind catalogue. **Never returns a credential** |
| POST | `/sources` | Connect a system. Auth by reference only — see below |
| GET | `/sources/status` | Connected Systems: health, freshness, sync stats |
| POST | `/sources/sync` | Manual refresh (`?source_id=`, `?full=true` forces a full re-read) |
| GET | `/sources/{id}` | One source with its sync history |
| PATCH | `/sources/{id}` | `{"enabled": false}` or `{"cadence": "daily"}` |
| POST | `/sources/{id}/health` | Re-check health now |
| DELETE | `/sources/{id}` | Disconnect |
| GET | `/search` | Unified search (`?q=`, `?surfaces=knowledge,tasks`) |
| GET | `/search/enterprise` | Unified search + the surface catalogue |
| GET | `/organization` | Organization Overview (business framing) |
| GET | `/organization/entities` | Entities (`?kind=`, `?owner=`, `?q=`) |
| GET | `/organization/entities/{id}` | One entity with history and relationships |
| GET | `/organization/relationships` | Links with evidence (`?kind=`, `?min_confidence=`) |
| GET | `/organization/refreshes` | Refresh pipeline history, stage by stage |

### Connecting a source

```json
{
  "name": "warehouse", "kind": "postgresql", "cadence": "hourly",
  "auth": {"kind": "env", "ref": "EDIP_WAREHOUSE_URL"},
  "options": {"tables": ["orders", "customers"]}
}
```

`kind` ∈ postgresql · sqlserver · mysql · oracle · csv · excel · rest_api ·
sharepoint · outlook · teams. The Microsoft kinds register as *awaiting
integration* (V2) and never sync.

**The platform never stores credentials.** Pass a reference (`{"kind": "env",
"ref": "VAR_NAME"}`), never a value — a secret in `auth`, or a credentialed URL
in `location`, is rejected with 422.

## Product Intelligence & Strategy

| Method | Path | Description |
|---|---|---|
| GET | `/product` | Executive product view: portfolio position, attention, opportunities |
| GET | `/product/catalog` | Every product (`?status=`, `?lifecycle=`, `?owner=`) |
| POST | `/product/catalog` | Register a product (they are also discovered automatically) |
| POST | `/product/catalog/sync` | Rebuild from the organizational model; reattach KPIs/reports |
| GET | `/product/catalog/{id}` | One product: record, health, review, recommendations, alerts |
| PATCH | `/product/catalog/{id}` | `{"lifecycle": "mature"}` |
| GET | `/product/health` | Every product's scores, with reasons and evidence |
| POST | `/product/health/evaluate` | Re-score now (`?product_id=` for one) |
| GET | `/product/growth` | Growth findings (`?kind=cannibalization`, `?product_id=`) |
| GET | `/product/reviews` | Structured product reviews |
| POST | `/product/reviews` | Generate (`?product_id=`, `?register=true` → Review Center) |
| GET | `/product/recommendations` | Strategic recommendations (`?play=`, `?status=`) |
| POST | `/product/recommendations` | Re-derive (`?route=false` to skip the Decision Engine) |
| PATCH | `/product/recommendations/{id}` | `{"status": "accepted"}` |
| GET | `/product/portfolio` | Portfolio health, risk, growth, ranking, investment priority |
| GET | `/product/scenarios` | Past scenarios + the levers that can be asked about |
| POST | `/product/scenarios` | `{"lever": "customer_growth", "change_pct": 15}` |
| GET | `/product/kpis` | Business/growth/operational/portfolio KPIs + thresholds |
| POST | `/product/kpis/monitor` | Check thresholds now |
| POST | `/product/kpis/thresholds` | Give one KPI its own rule (no deploy) |
| GET | `/product/kpis/alerts` | Breaches (`?severity=critical`) |
| GET | `/product/briefs` | Executive briefs + the kinds available |
| POST | `/product/briefs/{kind}` | board_brief · monthly_review · quarterly_strategy · risk_summary · growth_summary · decision_pack |
| GET | `/product/strategy` | Portfolio intelligence + open recommendations |

### Scenario contract

Levers: `customer_growth` · `merchant_failures` · `merchant_engagement` ·
`transaction_volume` · `revenue` · `feature_launch`.

Every projection is applied to **real** KPI values and inherits the confidence
of the **real** forecast beneath it (including the Forecasting Module's
validation gate: `low_confidence` and `unavailable` carry through). A scenario
over a KPI the platform has never measured returns `projections: []` with
`"cannot be simulated"` and names what is missing — it does not invent a
baseline. Every result lists its `assumptions`.

### Executive surface additions

| Method | Path | Description |
|---|---|---|
| GET | `/manager/organization` | Organization Overview for the executive |
| GET | `/manager/search` | One question across everything the organization knows |
| GET | `/manager/products` | The executive product view |
| GET | `/manager/product-reviews` | Latest product review per product |

## Enterprise Data Sources (V2.1 — Admin only)

The Enterprise Connector Framework. Administrators configure a source once;
the Runtime synchronizes it from then on. Managers never see these endpoints —
see [CONNECTOR_FRAMEWORK.md](CONNECTOR_FRAMEWORK.md).

| Method | Path | Description |
|---|---|---|
| GET | `/connectors` | Overview: sources, health, catalogue |
| GET | `/connectors/catalogue` | Connector kinds: available, unavailable, planned |
| GET | `/connectors/sources` | Configured sources (`?kind=` `?health=`) |
| POST | `/connectors/sources` | Register — `{"name", "kind", "location", "auth", "cadence", "options"}` |
| GET | `/connectors/sources/{id}` | One source with runs, failures, packages |
| PATCH | `/connectors/sources/{id}` | Edit · `{"enabled": false}` · `{"cadence": "daily"}` |
| DELETE | `/connectors/sources/{id}` | Disconnect (ingested knowledge is kept) |
| POST | `/connectors/sources/{id}/test` | Test connection — always answers, never 500s |
| POST | `/connectors/sources/{id}/discover` | Enumerate items (metadata only) |
| POST | `/connectors/sources/{id}/health` | Assess health now |
| POST | `/connectors/sources/{id}/sync` | Manual sync (`?full=true` forces a full re-read) |
| POST | `/connectors/sync` | Manual sync of every enabled source |
| GET | `/connectors/runs` | Sync history (`?connector_id=`) |
| GET | `/connectors/failures` | Failures with errors and attempt counts |
| GET | `/connectors/packages` | Knowledge Package catalogue (metadata + checksums) |

**Credentials are never accepted or returned.** `auth` takes a reference —
`{"kind": "env", "ref": "EDIP_WAREHOUSE_URL"}` — and the API refuses a secret
value in `auth` or a credentialed connection string in `location` (422).

Connector kinds in V2.1: `folder` · `excel` · `csv` · `postgresql`. Planned
kinds are listed in the catalogue and rejected at registration with the reason.

## Enterprise AI Operating Layer (V2.2 — Admin only)

Agent Registry, Tool Registry, Prompt Registry, Evaluation, Governance,
Memory Lifecycle, Workflow Registry, and Observability. Managers never see
these — see [AI_OPERATING_LAYER.md](AI_OPERATING_LAYER.md).

| Method | Path | Description |
|---|---|---|
| GET | `/ops/observability` | Whole dashboard: one verdict + every section |
| GET | `/ops/observability/{section}` | One section (e.g. `agent_health`, `llm_usage`) |
| GET | `/ops/agents` | Agent catalogue + health (`?capability=` `?brain_role=`) |
| GET | `/ops/agents/{id}` | One agent with descriptor and health |
| POST | `/ops/agents/{id}/run` | Execute an agent — gated by its execution policy |
| GET | `/ops/tools` | Tool catalogue with specs, permissions, and status |
| GET | `/ops/prompts` | Prompt catalogue (`?domain=`) |
| GET | `/ops/prompts/{id}` | One prompt with template, versions, change history |
| GET | `/ops/evaluation` | Evaluators + acceptance metrics |
| GET | `/ops/evaluation/history` | Recent verdicts (`?decision=`) |
| GET | `/ops/governance` | RBAC, policies, security, retention |
| GET | `/ops/governance/audit` | Audit log (`?action=` `?actor=`) |
| GET | `/ops/governance/model-usage` | LLM usage log + summary |
| POST | `/ops/governance/assign` | `{"principal", "role"}` — audited |
| GET | `/ops/memory/lifecycle` | Freshness, versions, archived events, expiry |
| GET | `/ops/memory/freshness` | Freshness per knowledge class |
| GET | `/ops/memory/evolution` | Relationship evolution (`?hours=`) |
| GET | `/ops/workflows` | Declared autonomous workflows (`?trigger=` `?tag=`) |
| POST | `/ops/workflows/{id}/run` | Execute a declared workflow |

Governance and evaluation can be disabled (`EDIP_GOVERNANCE_ENABLED=false`,
`EDIP_EVALUATION_ENABLED=false`) to return the platform to V2.1 behaviour.

## Health

| Method | Path |
|---|---|
| GET | `/health` |

### Executive report contract

`GET /report` always returns exactly these sections:
`meta` (incl. `ai.status/provider/model`), `executive_summary` (deterministic
health score + AI summary, portfolio health, priority actions, commentary),
`business_insights[]`, `root_cause_analysis[]`, `risk_analysis[]`,
`opportunity_analysis[]`, `recommendations[]` — all AI-generated — plus the
deterministic `management_summary`, `dataset_summary`, `kpi_analysis[]`,
`signals[]`, `predictive_analytics`, `appendix` (incl. the exact
`business_context` sent to the model).

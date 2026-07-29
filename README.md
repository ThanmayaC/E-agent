# EAPIP — Enterprise Autonomous Product Intelligence Platform

The foundation for a **Digital Product Manager**: specialized intelligence
engines, agents, enterprise knowledge, memory, a workflow engine, a tool
layer, and a provider-agnostic LLM layer. Upload enterprise data sources —
Excel, CSV, PDF, Word, SQL databases, REST APIs — and the platform discovers
datasets, understands schemas and business meaning, links related data,
detects KPIs, builds a semantic model and knowledge graph, runs analytics,
predicts trends, and has its agents write a fixed-format executive report
with a grounded copilot on top. **Zero manual mapping**: no column
definitions, no join configuration, no metric setup.

```
Enterprise Intelligence Engine (connectors + analytics — facts only)
→ Enterprise Knowledge (terminology · rules · clarifications · history)
→ Specialized Agents (prompt generator · report writer · copilot · analysts · portfolio · manager · planner)
→ Enterprise Workflow Engine (full analysis · daily cycle · background intelligence · monitoring)
→ Autonomous Execution Layer (scheduler · event bus · triggers · goals · planning · decisions · action queue)
→ Knowledge Synchronization Layer (source registry · incremental sync · organizational model · relationships · refresh pipeline · enterprise search)
→ Product Intelligence Layer (catalog · health · growth · strategy · KPIs · scenarios · portfolio · executive briefs)
→ Enterprise Connector Framework (connector interface · registry · Knowledge Packages · Enterprise Sync Service)
→ Enterprise AI Operating Layer (agent · tool · prompt · workflow registries · evaluation · governance · memory lifecycle · observability)
```

The LLM is one component — it is never the application. Every agent reasons
through `Observe → Understand → Plan → Choose Tools → Execute → Verify →
Learn`, and clarifications you provide once are remembered forever.

**Enterprise Agent is proactive, not reactive.** It does not wait to be
asked: when it starts, it observes enterprise systems, learns, plans,
executes workflows, monitors outcomes, and improves — continuously, on its
own heartbeat. The manager reviews, approves, communicates, and makes
strategic decisions while the agent does the operational work. Anything that
reaches outside the business (email, meetings, business rules, automation)
passes through a human approval layer first, and anything the agent is not
confident about escalates on its own.

## What it does automatically

- **Multi-source ingestion (connectors)** — Excel (every sheet including
  hidden, merged cells, multiple tables per sheet, messy headers, corrupt
  sheets skipped gracefully), CSV/TSV, PDF tables (optional `pdfplumber`),
  Word tables (optional `python-docx`), SQL databases (`*.sqlsource.json`
  descriptor), REST APIs (`*.apisource.json` descriptor). New sources are new
  `DataConnector`s — no other layer changes.
- **Schema inference** — data types, identifiers, currencies, percentages,
  statuses, geo, primary-key candidates, measures vs dimensions, facts vs
  dimension tables.
- **Business meaning** — `cust_id`, `customer_no`, `cid`, `consumer` all map to
  **Customer** via an extensible ontology + fuzzy matching; every column gets a
  concept, role, canonical name, and confidence.
- **Relationships** — foreign keys across files *even with different column
  names* (`MID` ↔ `merchant_id`), shared dimensions, date alignments — proven
  by value overlap, not just names.
- **Duplicate/partition handling** — monthly/yearly partitions and snapshots
  detected by schema signature and merged into logical datasets.
- **KPIs** — revenue, volume, success/failure rates, distinct entity counts,
  growth, retention-style rates — with sparklines, MoM growth, and trend.
- **Statistical signals (deterministic)** — trends, anomalies (σ-shocks),
  seasonality, Pareto concentration, correlations and inverse-correlation
  (cannibalization) candidates — pure numeric facts, no narrative.
- **Predictions** — trend + seasonal forecasts with confidence intervals.
- **AI reasoning (LLM-generated)** — a Business Context Builder condenses all
  analytics into one compact JSON; the LLM reasons over it as PM / strategy
  consultant / data scientist / analyst and returns structured JSON:
  executive summary, key insights, root causes, risks, opportunities,
  recommendations, priority actions, management commentary. No rule-based or
  templated narrative exists anywhere in the codebase.
- **Executive report** — fixed structure every time: deterministic fact
  sections + AI narrative sections, JSON + Markdown.
- **Copilot agent** — "Why did growth slow?", "Compare March vs April",
  "Predict next quarter" — retrieval over analytics → generated prompt → LLM
  → grounded answer with cited facts, remembered in conversation memory so
  follow-ups resolve references.
- **Enterprise knowledge & memory** — terminology, business rules, and
  clarifications taught once (Knowledge Explorer or API) are injected into
  every future reasoning prompt; report and decision history accumulate.
- **Workflow engine** — the analysis pipeline is a registered workflow with
  persisted run history, alongside autonomous step chains that run with no
  user present: `daily_cycle` (refresh portfolio → analyse new data → update
  the Enterprise Brain → daily brief → tasks → recommendations → queue
  communications), `background_intelligence`, and `monitoring`.
- **Autonomous operation (no user required)** — an Enterprise Scheduler
  (startup / interval / cron / event jobs, dependency ordering, retries,
  failure recovery) is the heartbeat; an Event Bus lets modules announce
  instead of calling each other; configurable trigger rules turn events into
  work ("if portfolio risk increases, generate a task"); background jobs keep
  knowledge, memory, portfolio, predictions, risks, opportunities, and
  recommendations current on their own.
- **Goals the platform works toward** — define an objective with KPIs,
  targets, and a deadline; the Planning Engine breaks it into executable
  steps, advances them on the heartbeat, measures progress from the
  platform's own metrics, and **replans automatically** when a goal stalls or
  its deadline closes in.
- **Decisions you can audit** — every recommendation runs
  `evidence → confidence → priority → approval? → execute → monitor → learn`,
  with each stage recorded. Uncited recommendations are trusted less;
  low-confidence ones escalate to a human.
- **Continuous knowledge synchronization** — connect databases (PostgreSQL,
  SQL Server, MySQL, Oracle), files, and REST APIs once; the platform then
  syncs them incrementally (only changed records, by content fingerprint),
  maintains a unified organizational model (products, customers, merchants,
  banks, teams, reports, KPIs — each with identity, aliases, ownership, and
  history), keeps their relationships current, and refreshes organizational
  knowledge without anyone pressing anything. **Credentials are never stored**:
  sources authenticate by reference to an environment variable, resolved in
  memory at sync time. SharePoint, Outlook, and Teams are registered as
  interfaces awaiting their V2 providers.
- **Enterprise search** — one query across knowledge, memory, projects,
  reports, tasks, portfolio, business rules, clarifications, recommendations,
  and the organizational model. Nothing is reindexed; each surface is searched
  by the component that owns it.
- **Enterprise Product Manager** — a product catalogue built from the
  organizational model; eight evidence-based scores per product (health,
  growth, risk, stability, adoption, revenue, satisfaction, merchant
  engagement), each citing the KPIs and signals behind it; growth intelligence
  (opportunities, decline, emerging trends, cannibalization, cross-sell,
  portfolio gaps, expansion); strategic recommendations with business impact,
  effort, and dependencies; KPI threshold monitoring; deterministic "what if"
  scenarios; portfolio ranking with investment priority; and executive briefs
  (board, monthly, quarterly, risk, growth, decision pack).
- **It says "unknown" rather than guessing** — a product the platform cannot
  measure scores *unknown*, not zero, and says what is missing. A scenario over
  an unmeasured KPI refuses to estimate. Scenario confidence is inherited from
  the real forecast beneath it, never asserted. Every judgement cites its
  evidence, and one that cannot cite is not made.
- **Human approval layer** — every communication, workflow, approval, and
  automation enters one Action Queue
  (`pending_approval → approved → executed`, or `rejected`). External-effect
  actions always need a human; internal reversible work does not. Trigger
  rules and the Decision Engine can only *queue* actions, so nothing routes
  around approval.

## Quick start

```bash
docker compose up --build -d      # UI on :3000, API on :8000/docs
```

or locally (no external services needed):

```bash
cd backend && pip install -r requirements.txt && uvicorn app.main:app --port 8000
cd frontend && npm install && npm run dev          # :5173
```

Generate demo workbooks: `cd backend && python scripts/generate_sample_data.py`
then upload `sample_data/*.xlsx` in the UI.

**Synthetic enterprise (V3.0):** one deterministic command generates an entire
fictional organization — *NPCI (Synthetic Demonstration) / UPI Products* — and
one connected business week of its activity:

```bash
python generate_enterprise.py --days 7 --seed 2026
```

This writes `enterprise_data/` (master data + `day_01`…`day_07` + `scenarios`):
employees, products, merchants, banks, PSPs, Outlook threads, Teams
conversations, meetings, RCAs, SOPs, BRDs/PRDs, Excel KPI workbooks, daily and
executive reports, decisions and tasks — all one company, all cross-referenced,
with a single KPI source of truth (a UPI Autopay mandate-failure incident that
is detected Monday and resolved by Friday). The same seed always produces the
same organization; a different seed a different but internally consistent one.

Ingest it into the Brain (reuses the existing sync → document-intelligence →
Brain pipeline, no backend change):

```bash
cd backend && python scripts/bootstrap_enterprise_demo.py
```

Then ask a cross-source question — *"Why did UPI Autopay success dip this week
and what did we do about it?"* — and the answer combines the incident record,
the RCA, the KPI numbers, the decision, and the SOP. See
[docs/SYNTHETIC_ENTERPRISE.md](docs/SYNTHETIC_ENTERPRISE.md) and
[docs/ENTERPRISE_BRAIN.md](docs/ENTERPRISE_BRAIN.md).

## Stack

**Backend** Python 3.11 · FastAPI (async) · Pandas · DuckDB · OpenPyXL ·
NetworkX · SQLAlchemy · Pydantic v2 · Jinja2 · optional: pgvector, Redis+Celery,
sentence-transformers, Polars/PyArrow.
**Frontend** React 18 · Vite · Tailwind (dark enterprise theme) · Apache
ECharts · React Flow · TanStack Table · Framer Motion · ShadCN-style local UI
primitives.
**LLM layer** provider-agnostic (`app/llm/`): Ollama (default for local dev —
qwen3 / llama3 / gemma3 / mistral / deepseek, any installed model), OpenAI,
Azure OpenAI, Anthropic, Gemini, or a company enterprise gateway — selected by
`EDIP_LLM_PROVIDER` alone. Chat, JSON mode, streaming, retry, timeout,
temperature and max tokens supported across providers. With no provider, AI
sections report `unavailable`; deterministic analytics keep working.

## Repository layout

```
backend/
  app/core          settings (EDIP_* env), logging, DI container
  app/domain        entities & enums (pure, no dependencies)
  app/llm           provider abstraction: base_provider, ollama, openai,
                    azure_openai, anthropic, gemini, enterprise, factory
  app/intelligence  Intelligence Engine (facts only): connectors (excel, csv,
                    pdf, word, sql, rest_api), profiling, semantics, dedup,
                    relationships, timeseries, kpi, quality, graph, embeddings,
                    analytics (+signals), forecasting, context builder,
                    engine.py facade
  app/knowledge     persistent enterprise knowledge store
  app/memory        working / conversation / business / organizational memory
  app/agents        base loop + prompt generator, reasoning engine, report
                    writer, copilot, schema/business analysts, portfolio,
                    manager, planner
  app/tools         tool registry: vector search, artifact lookup, analytics
                    SQL, knowledge search, report markdown (+ planned tools)
  app/modules       canonical SDS module namespace — one facade per
                    Enterprise Agent module (see docs/SDS_MODULE_MAP.md)
  app/workflows     workflow engine + full-analysis + autonomous chains
                    (daily_cycle, background_intelligence, monitoring)
  app/runtime       autonomous execution layer: scheduler (heartbeat), event
                    bus, triggers, goals, planning, decisions, action queue +
                    approval layer, background intelligence, decision
                    intelligence (V2.4: observe → propose → rank → decide →
                    learn — the Brain deciding, not just informing)
  app/sync          knowledge synchronization: data-source registry (auth by
                    reference), incremental sync engine, organizational model,
                    relationship engine, refresh pipeline, enterprise search
  app/connectors    enterprise connector framework (V2.1): connector
                    interface + lifecycle, dynamic registry, Unified
                    Knowledge Package, Enterprise Sync Service, and the
                    folder/excel/csv/postgresql connectors
  app/prompts       prompt registry (V2.2): every LLM prompt, versioned and
                    owned, in per-domain modules — none embedded in code
  app/evaluation    evaluation layer (V2.2): grounding · citation · policy ·
                    formatting · confidence · duplicates → accept/regenerate/
                    approve/reject
  app/governance    governance (V2.2): RBAC, approval/knowledge/retention/
                    security policies, audit + model-usage logs
  app/observability enterprise observability (V2.2): Admin-only operational
                    dashboard composed from every layer's status
  app/product       product intelligence: evidence gatherer, catalog, health,
                    growth, strategy, reviews, KPI intelligence, scenarios,
                    portfolio intelligence, executive briefs
  app/reports       report assembler (facts + AI narrative) + markdown
  app/repositories  artifact store (JSON docs + DuckDB warehouse)
  app/api/v1        REST routers (projects, artifacts, knowledge, platform,
                    brain, manager, runtime, sync, product, copilot,
                    documents, connectors)
  app/workers       optional Celery tasks
  scripts/          sample data generator; Enterprise Brain bootstrap
                    (registers enterprise_data/ folders + ingests them)
generate_enterprise.py   V3.0 synthetic enterprise generator (root): builds
                    enterprise_data/ — one NPCI UPI Products company, one week
enterprise_data/    generated synthetic organization (master + day_01..07 +
                    scenarios); the corpus the Enterprise Brain ingests
  tests/            unit + full end-to-end integration suite
frontend/src        Executive Experience: business-only workspace (Home,
                    Executive Dashboard, Portfolio, Reports, AI Copilot,
                    Tasks, Decisions, Notifications, Settings) + gated Admin
                    Console (runtime, brain, scheduler, jobs, sync, knowledge,
                    logs, diagnostics, models) + per-project analyst workbench
                    (see docs/EXECUTIVE_EXPERIENCE.md)
docs/               ARCHITECTURE.md (diagrams) · API.md · INSTALLATION.md ·
                    EXECUTIVE_EXPERIENCE.md (frontend)
```

## Documentation

- [Installation guide](docs/INSTALLATION.md)
- [Architecture, sequence & ER diagrams](docs/ARCHITECTURE.md)
- [API reference](docs/API.md) — plus live Swagger at `/docs`
- [Executive Experience](docs/EXECUTIVE_EXPERIENCE.md) — the production UI: executive workspace, Admin Console, routes
- [Enterprise Brain](docs/ENTERPRISE_BRAIN.md) — V2.3: the synthetic enterprise corpus, ingestion, cross-source Q&A, and the autonomous daily cycle
- [Decision Intelligence](docs/DECISION_INTELLIGENCE.md) — V2.4: the Brain reasoning about the organization and proposing decisions proactively — lifecycle, decision graph, ranking, learning, reports, and the executive workspace
- [Synthetic Enterprise](docs/SYNTHETIC_ENTERPRISE.md) — V3.0: the deterministic NPCI UPI Products generator, its one-week storyline, and ingestion
- [Executive Intelligence](docs/EXECUTIVE_INTELLIGENCE.md) — V3.1: connecting the Brain into an AI-Product-Head layer — executive brief, priorities, KPI intelligence, ranked decisions, the business-entity graph, and the reasoning Copilot

## Testing

```bash
cd backend
pytest            # 13 unit tests + full pipeline integration test
```

The integration test uploads five deliberately messy workbooks (with a mock
LLM provider) and asserts: partitions merged, `Cust_ID → Customer` inferred,
`MID ↔ merchant_id` FK found, KPIs with time series, deterministic signals
carry stats only (no narrative fields), the business context stays compact,
the AI report is structured JSON, the fixed report shape is intact, the
copilot returns grounded answers with cited facts, and SQL stays read-only.

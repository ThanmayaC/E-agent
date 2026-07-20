# SDS Module Map — Enterprise Agent

The SDS defines twenty permanent modules. This document is the authoritative
mapping between those modules and the repository, maintained as the
migration progresses.

**Canonical namespace:** `backend/app/modules/` — one facade per SDS module.
Code that needs a module's public interface imports `app.modules.<name>`.
Facades re-export the existing implementations (strangler-fig): nothing was
rewritten or moved in Phase 1; implementations migrate behind the facades in
later phases without changing callers.

The machine-readable registry is `app.modules.MODULES`; the guard test is
`tests/unit/test_sds_modules.py`.

## Module → implementation

| # | SDS Module | Facade | Backed by (today) | Status |
|---|------------|--------|-------------------|--------|
| 1 | Supervisor | `app.modules.supervisor` | `orchestration/agents.py` (supervisor entry/exit nodes, repair routing) | implemented |
| 2 | Planner | `app.modules.planner` | `orchestration/agents.py` (ExecutionPlan node), `agents/specialists.py` (`PlannerAgent`), `runtime/planning.py` (goal → plan → replan) | implemented |
| 3 | Observation | `app.modules.observation` | `intelligence/connectors/` (Excel, CSV, PDF, Word, SQL, REST) | implemented |
| 4 | Data Intelligence | `app.modules.data_intelligence` | `intelligence/semantics`, `dedup`, `relationships`, `confidence`, `context` | implemented |
| 5 | Schema Intelligence | `app.modules.schema_intelligence` | `intelligence/profiling`, `intelligence/timeseries` | implemented |
| 6 | Analytics | `app.modules.analytics` | `intelligence/analytics` (+signals), `kpi`, `quality` | implemented |
| 7 | Machine Learning | `app.modules.machine_learning` | `ml/selection.py` (Model Selection Framework) | partial |
| 8 | Deep Learning | `app.modules.deep_learning` | `intelligence/embeddings` (embedders, vector stores) | partial |
| 9 | Knowledge | `app.modules.knowledge` | `knowledge/store.py`, `intelligence/graph` | implemented |
| 10 | Memory | `app.modules.memory` | `memory/manager.py` (working/conversation/business/organizational) | partial |
| 11 | Forecasting | `app.modules.forecasting` | `intelligence/forecasting` | implemented |
| 12 | Evidence Verification | `app.modules.evidence_verification` | `evidence/` (ledger + extraction), verifier node in orchestration | implemented |
| 13 | Recommendation | `app.modules.recommendation` | `intelligence/recommendations` (rule-derived, evidence-cited) | implemented |
| 14 | Report Generation | `app.modules.report_generation` | `reports/` (assembler, markdown), `agents/report_writer.py` | implemented |
| 15 | Portfolio | `app.modules.portfolio` | `manager/portfolio.py` (executive view), `product/portfolio.py` (product portfolio intelligence), `agents/specialists.py` (`PortfolioAgent`) | implemented |
| 16 | Manager | `app.modules.manager` | `agents/specialists.py` (`ManagerAgent`), `reasoning.py`, `prompt_generator.py`, `copilot.py` | partial |
| 17 | Document Intelligence | `app.modules.document_intelligence` | `intelligence/connectors/pdf.py`, `word.py` (table extraction) | partial |
| 18 | Communication | `app.modules.communication` | `tools/planned.py` (Email/Calendar registered, not executable) | planned |
| 19 | Workflow | `app.modules.workflow` | `workflows/` (engine, full_analysis, autonomous chains: daily_cycle · background_intelligence · monitoring, planned registry, schedules) | implemented |
| 20 | Automation | `app.modules.automation` | `runtime/` (scheduler, triggers, action queue, background intelligence, AutonomyRuntime) over `workflows/engine.py` | implemented |

## Cross-cutting infrastructure (not SDS modules — kept as-is)

| Package | Role | Disposition |
|---------|------|-------------|
| `app/orchestration/` | LangGraph: graph assembly, nodes, state, checkpointing, clarification gate | keep — orchestration only, no analytics (per SDS) |
| `app/llm/` | Provider-agnostic LLM layer (Ollama/OpenAI/Azure/Anthropic/Gemini/enterprise) | keep — consumed by reasoning/report/copilot |
| `app/agents/base.py` | Shared agent loop (Observe → … → Learn), `AgentRequest/Result` | keep — framework, not a module |
| `app/tools/` | Tool registry (built-in + planned) | keep — capability layer used across modules |
| `app/core/` | Settings, logging, DI container | keep |
| `app/domain/` | Pure entities and enums | keep |
| `app/db/control.py` | Control-plane ORM (ledger tables) | keep — owned by Evidence Verification |
| `app/repositories/` | Artifact store (JSON docs + DuckDB warehouse) | keep — persistence, dual-write with ledger |
| `app/runtime/` | Autonomous execution layer: scheduler (heartbeat), event bus, trigger engine, goal engine, planning engine, decision engine, action queue + approval layer, background intelligence | keep — the Automation Module's implementation; Planner and Workflow consume it |
| `app/sync/` | Enterprise Knowledge Synchronization Layer: data-source registry (auth by reference, never by value), incremental sync engine, organizational model, relationship engine, knowledge refresh pipeline, enterprise search | keep — feeds the Knowledge and Memory Modules from connected systems; reads sources through the existing connectors |
| `app/product/` | Product Intelligence & Strategic Decision Layer: evidence gatherer, product catalog, health, growth, strategy, reviews, KPI intelligence, scenarios, portfolio intelligence, executive briefs | keep — sits ABOVE the Brain; computes no analytics, routes strategy through the runtime's Decision Engine |
| `app/api/v1/` | FastAPI routers — APIs only, no business logic | keep |
| `app/intelligence/engine.py` | `IntelligenceEngine` facade over deterministic capabilities | keep — internal composition root for graph nodes |
| `app/workers/` | Optional Celery tasks | keep — becomes Automation's execution substrate |

## Notes and decisions

- **No physical moves in Phase 1.** Moving `app/intelligence/*` wholesale
  would churn every import for zero behavior gain. The facades fix the
  module boundaries first; physical relocation happens opportunistically
  when a module is next touched (Phase 2+), one module at a time, keeping
  the project runnable at every step.
- **Data vs Schema Intelligence split:** structural discovery (profiling,
  time-series detection) is Schema Intelligence; business meaning,
  relationships, dedup, confidence/clarifications, and business context are
  Data Intelligence, per SDS §2.1 responsibilities.
- **Ontology location:** the business ontology currently lives inside
  `MeaningDetector` (Data Intelligence). SDS assigns ontology to the
  Knowledge Module — extracting it into `app/knowledge` is a Phase 3 item.
- **Three planning surfaces:** the graph planner node (run-level),
  `PlannerAgent` (goal routing), and `PlanningEngine` (business objective →
  durable plan → replan) are all Planner Module responsibilities. They
  operate at different altitudes and are intentionally distinct today;
  consolidation under one interface remains a Phase 5 item.
- **Autonomy is bounded by approval:** the Action Queue is the single
  execution centre. Trigger rules and the Decision Engine can only *queue*
  actions, never perform them, so no automation path bypasses the human
  approval layer. Communication kinds (email, meetings, messaging) have no
  executor by design — V2 providers register there, and the approval trail
  already works without them.
- **Nothing was removed.** No duplicate business logic was found that
  required deletion; the only duplication is the intentional dual-write
  (artifact store + evidence ledger) documented in `evidence/ledger.py`.

## Phase roadmap alignment

- **Phase 1 (this change):** module namespace + map + guard test. ✔
- **Phase 2:** complete ML (features, segmentation, registry, monitoring)
  and DL (sequence models) behind `machine_learning` / `deep_learning`.
- **Phase 3:** ontology into Knowledge; project/strategic/learning memory
  layers into Memory.
- **Phase 4:** prompt engine / recommendation / report depth (already
  seeded; extend behind existing facades).
- **Phase 5:** planner consolidation, approval routing beyond the
  confidence gate.
- **Phase 6:** Communication (flip planned tools to available), Document
  Intelligence beyond tables, Portfolio cross-project analytics.
- **Phase 11 (this change) — the Enterprise AI Operating Layer (V2.2).** The
  operational layers *around* the intelligence, the Brain still at the centre.
  A capability-discoverable **Agent Registry** whose catalogue maps the SDS's
  named agents onto workflows and layers that already exist (nothing
  reimplemented); a **Tool Registry** with per-tool capability, permissions,
  and input/output schema; a **Prompt Registry** that pulls every LLM prompt
  out of business logic into versioned, owned domain modules; an **Evaluation**
  panel (grounding, citation, evidence completeness, policy, formatting,
  confidence, duplicates, business rules) that delegates to the V1 checkers and
  yields accept/regenerate/approve/reject; a **Governance** authority (RBAC,
  connector/prompt/approval/knowledge/retention/security policies, audit
  through the existing control-plane table, model-usage logs) that fails closed
  and is advisory until installed; a **Memory Lifecycle** giving the Brain
  freshness, versions, history, evolution, and expiry without deleting
  anything; an **Autonomous Workflow Registry** declaring trigger/inputs/agents/
  tools/outputs/approval/schedule over the existing Workflow Engine; **REST +
  Webhook** communication adapters; and an Admin-only **Observability**
  dashboard composed from every layer's own status. No new Runtime, Scheduler,
  orchestrator, or Brain. Backward compatible: `EDIP_GOVERNANCE_ENABLED=false`
  and `EDIP_EVALUATION_ENABLED=false` return the platform to V2.1 behaviour. ✔
- **Phase 10 — the Enterprise Connector Framework (V2.1).** A uniform
  connector interface (initialize → connect → test → discover → sync →
  incremental_sync → fetch → health → disconnect), a dynamic registry, the
  Unified Knowledge Package, and the Enterprise Sync Service — folder, Excel,
  CSV, and PostgreSQL connectors on the existing scheduler and bus, feeding the
  existing Document Intelligence pipeline. Managers never configure a source. ✔
- **Phase 9 — the Product Intelligence & Strategic Decision
  Layer.** The platform became an Enterprise Product Manager: a product
  catalogue over the Organizational Model, eight evidence-based health scores
  per product, growth intelligence (reusing the Analytics module's own
  `INVERSE_CORRELATION` cannibalization signal), strategic recommendations
  routed through the existing Decision Engine, KPI threshold monitoring,
  deterministic scenario simulation over existing forecasts, portfolio
  intelligence with investment priority, and executive briefs. It computes no
  analytics and creates no second scheduler, bus, or approval path. Backward
  compatible: `EDIP_PRODUCT_ENABLED=false` stops the recalculation and every
  surface still answers on demand. ✔
- **Phase 8 — the Enterprise Knowledge Synchronization Layer.** The Brain now
  learns from the enterprise, not only from analyses: the data-source registry
  (credentials by reference, never stored), incremental delta synchronization,
  the organizational model, the relationship engine, the knowledge refresh
  pipeline, and unified enterprise search — all on the existing scheduler and
  event bus. `EDIP_SYNC_ENABLED=false` stops the refresh; surfaces still
  answer. ✔
- **Phase 7 — the autonomous execution layer.** Automation
  became real: the Enterprise Scheduler is the beat process the roadmap
  called for, and the Workflow Module gained autonomous step chains. The
  platform now observes, learns, plans, executes, monitors, and improves on
  its own heartbeat; the manager reviews, approves, communicates, and
  decides strategy. Backward compatible: `EDIP_AUTONOMY_ENABLED=false`
  stops the ticking and every pre-existing surface behaves exactly as
  before. ✔

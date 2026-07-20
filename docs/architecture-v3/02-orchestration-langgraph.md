# 02 · LangGraph Orchestration & Agents

## 1. Why LangGraph is the backbone (and what it replaces)

v2's `workflows/analysis.py` is an imperative 18-stage script. It already
*needs* graph semantics — it has a mid-pipeline pause (clarification gate), an
early-exit branch, stage status streaming, and re-runs. LangGraph gives those
semantics natively:

| v2 mechanism (hand-built) | v3 LangGraph primitive |
|---|---|
| `state.status = "awaiting_clarification"; return` | `interrupt()` + Postgres checkpoint |
| Re-run whole pipeline after answers | `graph.invoke(Command(resume=answers), config)` — resumes *at the gate* |
| `_marker()` stage streaming | node lifecycle events → SSE `run_events` |
| try/except per stage | per-node `retry_policy` + error edges |
| implicit sequential stages | explicit edges, parallel fan-out branches |
| one hardcoded pipeline | Planner-emitted execution plan; conditional edges |

## 2. State schema

One typed state object flows through the graph. Large payloads (DataFrames,
Parquet) never enter state — state carries **references and evidence ids**;
data stays in the data plane. This keeps checkpoints small and resumable.

```python
class AnalysisState(TypedDict):
    project_id: str
    run_id: str
    plan: ExecutionPlan | None          # Planner output: steps, required agents,
                                        #   ML candidates, budgets
    dataset_refs: list[DatasetRef]      # DuckDB table + Parquet URI + schema hash
    profiles: list[TableProfile]        # compact — kept in state
    evidence_ids: list[str]             # ledger ids produced so far
    understanding: UnderstandingAssessment | None
    pending_clarifications: list[ClarificationQuestion]
    ml_results: list[MLResultRef]       # model version + prediction evidence ids
    draft_statements: list[Statement]   # LLM outputs awaiting verification
    verified_statements: list[Statement]
    report_ref: str | None
    passes: int                         # supervisor-ordered analysis passes
    approvals: dict[str, ApprovalState] # clarification / report / model gates
    errors: list[NodeError]
    telemetry: RunTelemetry             # tokens, cost, timings (aggregated)
```

Checkpointer: `PostgresSaver` (control plane). Every node boundary is durable —
a killed worker resumes mid-run; a human answer arriving three days later
resumes the same run at the same node with the same state.

## 3. Graph topology

```
                              START
                                │
                        ┌───────▼────────┐
                        │   SUPERVISOR   │  (entry: validates request, hydrates
                        └───────┬────────┘   project context, opens run record)
                                │
                        ┌───────▼────────┐
                        │    PLANNER     │  emits ExecutionPlan
                        └───────┬────────┘
                                │
                        ┌───────▼────────┐
                        │  INGEST node   │  connectors → dedup → Parquet/DuckDB
                        └───────┬────────┘
                                │
                        ┌───────▼──────────────┐
                        │ DATA UNDERSTANDING   │  tools: profiler, semantics,
                        │ AGENT                │  relationships; LLM only for
                        └───────┬──────────────┘  ambiguity resolution
                                │
              ┌─────────────────┼──────────────────┬───────────────┐
              ▼                 ▼                  ▼               ▼          (parallel)
      ┌───────────────┐ ┌──────────────┐  ┌──────────────┐ ┌────────────┐
      │ QUALITY node  │ │ QUANT ENGINE │  │ GRAPH BUILD  │ │ INDEX node │
      │               │ │ node         │  │ node         │ │ (vectors)  │
      └───────┬───────┘ └──────┬───────┘  └──────┬───────┘ └─────┬──────┘
              └─────────────────┴────────┬───────┴───────────────┘
                                         ▼
                              ┌────────────────────┐
                              │ CONFIDENCE GATE    │──── below threshold &
                              │ node               │     open questions?
                              └─────────┬──────────┘          │
                                        │ ok                  ▼
                                        │            ┌─────────────────┐
                                        │            │ interrupt() ──▶ │ human answers
                                        │            │ resume ◀─────── │ (API/UI)
                                        │            └────────┬────────┘
                                        │◀────────────────────┘
                              ┌─────────▼──────────┐
                              │     ML AGENT       │  conditional: plan.ml_candidates
                              └─────────┬──────────┘  ≠ ∅ and data gates pass
                                        │
                         ┌──────────────┴──────────────┐        (parallel)
                         ▼                             ▼
              ┌────────────────────┐        ┌─────────────────────┐
              │  ROOT CAUSE AGENT  │        │ RECOMMENDATION AGENT│
              └─────────┬──────────┘        └──────────┬──────────┘
                        └──────────────┬───────────────┘
                                       ▼
                             ┌──────────────────┐
                             │  VERIFIER node   │  deterministic — never an LLM
                             └────────┬─────────┘
                                      │  fail-rate > τ ──▶ back to offending agent
                                      ▼                    (max 2 repair loops)
                             ┌──────────────────┐
                             │   REPORT AGENT   │
                             └────────┬─────────┘
                                      ▼
                             ┌──────────────────┐
                             │  ASSEMBLER node  │  fixed-structure report + dashboards
                             └────────┬─────────┘
                                      ▼
                             ┌──────────────────┐     needs another pass?
                             │    SUPERVISOR    │────▶ (re-enter at Planner,
                             └────────┬─────────┘      passes+1, max 2)
                                      │ accept          optional: report sign-off
                                      ▼                 interrupt()
                                     END
```

Copilot runs as a **separate, lighter graph** (`graphs/copilot.py`):
`question → retrieval (vectors + graph + SQL tools) → grounded answer →
verifier → stream`. It shares tools and the ledger but not the heavyweight
analysis state.

A third graph (`graphs/retraining.py`) is triggered by the drift monitor:
`drift event → ML Agent (re-selection allowed) → evaluation → model approval
interrupt() → promote`.

## 4. Cross-cutting agent mechanics

| Concern | Mechanism |
|---|---|
| **Memory** | Three scopes. *Run memory*: the checkpointed state. *Project memory*: control-plane records + project vector collection (past reports/insights). *Enterprise memory*: knowledge store (terms, rules, answered clarifications) + global collections. Agents receive scoped memory via context hydration, never by trawling the DB. |
| **Retries** | Per-node `RetryPolicy`: deterministic nodes retry on infrastructure errors only (×3, exponential); LLM agents retry on schema-invalid output (×2) with the validator error injected into the retry prompt; provider failover (primary → fallback) lives in the LLM Gateway, not in agents. |
| **Branching** | Conditional edges driven by typed state predicates (`plan.ml_candidates`, `gate.unanswered`, `verifier.fail_rate`). No agent parses another agent's prose to decide routing — routing reads structured state. |
| **Human approval** | `interrupt()` nodes: clarification gate (always), report sign-off (config `require_report_approval`), model promotion (always, per governance). Each interrupt persists an approval record (who, when, what) in the control plane. |
| **Timeouts/budgets** | The Planner assigns token/time budgets per agent; the Supervisor enforces run-level budget; the cost meter (gateway) provides the actuals. |
| **Isolation** | Every tool call is scoped by `project_id` claims — a tool physically cannot read another project's data (RBAC enforced in the tool layer, not just the API). |

## 5. Agent roster and responsibilities

**Disposition rule (ADR-002):** an LLM agent exists only where there is
judgement — planning, ambiguity resolution, hypothesis generation, narration,
or routing. Deterministic capability = node; callable capability = tool;
shared context = memory/service. 18 candidates → 8 agents.

### 5.1 The eight agents

| Agent | Type | Responsibility | Tools | HITL |
|---|---|---|---|---|
| **Supervisor** | Rules-first + LLM for tie-breaks | Owns the run: validates request, decides which subgraphs are required, judges whether confidence is sufficient, orders repair loops or a second analysis pass (max 2), triggers human approvals, closes the run. | run inspection, budget meter, approval issuance | Issues interrupts |
| **Planner** | LLM (structured output) | Converts dataset shape + project goal + enterprise knowledge into a typed `ExecutionPlan`: steps, ML candidates with justification, budgets, expected evidence kinds. Plans are stored — auditable and diffable across runs. | schema summary, knowledge store, model catalog | — |
| **Data Understanding** | Hybrid | Runs profiler/semantics/relationship tools (deterministic), then uses the LLM strictly to resolve ambiguity (competing revenue columns, unknown datasets) or draft clarification questions. Merges v2's schema + semantic + relationship stages under one reasoning locus because they share context and failure modes. | profiler, semantic mapper, relationship detector, knowledge lookup | Feeds gate |
| **ML** | Hybrid | Executes the Model Selection Framework (03 §5): checks statistical gates, runs champion/challenger evaluation, trains via pipelines, registers models, produces `ml_prediction` evidence with explanations. LLM used only to summarize the *selection rationale* into the plan record. | feature store, selection framework, training/inference pipelines, MLflow registry | Model promotion interrupt |
| **Root Cause** | LLM | Generates **hypotheses only** over ledger evidence: drills down via SQL tool, walks graph paths (`transacts_with`, `belongs_to`) for structural explanations, recalls precedents from the vector store ("similar decline in project X"). Every hypothesis: possible cause, supporting evidence ids, missing evidence, confidence. Inherits v2's forbidden-inference prompt contract. | drilldown SQL, graph_query, vector_search, ledger read | — |
| **Recommendation** | Hybrid | Merges the deterministic rules engine output (v2, kept — quality/forecast/anomaly/limitation triggers) with LLM recommendations that must cite evidence ids; dedupes; ranks by priority and evidence strength. | rules engine, ledger read | — |
| **Report** | LLM | Narrates verified statements into the fixed report structure. Never introduces new claims (Verifier runs *before* it; Assembler validates it introduced no uncited ids). Emits dashboard spec (which charts matter this run). | ledger read, verified statements | Optional sign-off interrupt |
| **Copilot** | LLM | Interactive Q&A on the separate graph: retrieval-grounded (RAG), SQL, graph queries; answers carry citations; verifier post-checks every response before streaming completes. | vector_search, sql, graph_query, ledger read | — |

### 5.2 Requested agents that are deliberately *not* LLM agents

| Requested | Disposition | Why |
|---|---|---|
| Project Context Agent | **Memory service** (state hydration) | Fetching context involves zero decisions. A service call; agent overhead adds latency and a failure mode, no value. |
| Schema / Semantic Mapping / Relationship agents | Merged into **Data Understanding Agent** as tools | Three sequential steps over the same context; separate agents would just pass messages. One reasoning locus, three deterministic tools. |
| Data Quality Agent | **Quality node** (deterministic) | Quality checks are rules over data. Its *output* informs Supervisor and Recommendation decisions — the intelligence is in the consumers. |
| Analytics / Forecast agents | **Quant Engine node** | KPI discovery, signals, and gated forecasting are pure computation — the platform's deterministic core. Making them "agents" would put an LLM in front of arithmetic. |
| Deep Learning Agent | Folded into **ML Agent** | Deep learning is a model family the selection framework may choose, not a separate responsibility. Two agents would fight over the same decision. |
| Knowledge Graph Agent | **Graph Build node** + `graph_query` tool | Building the graph is deterministic; reasoning over it is a tool invoked by Root Cause/Copilot. |
| Vector Search Agent | `vector_search` tool | Retrieval is a call, not a colleague. |
| Evidence Verification Agent | **Verifier node — deterministic, by design** | The component that *catches* LLM errors must not itself be an LLM (ADR-004). v2's `_verify_evidence` logic, promoted to the ledger. |
| Dashboard Agent | **Assembler node** + Report Agent's dashboard spec | Dashboards are deterministic views over artifacts. The only judgement — which charts matter — belongs to the Report Agent. |

## 6. Sequence diagrams

### 6.1 Full analysis run (happy path)

```
UI          API(v2)      Supervisor   Planner   Understanding  fan-out nodes   Gate     ML       RC/Rec     Verifier  Report/Asm
│ POST /runs   │             │           │           │              │            │        │         │           │         │
│──────────────▶ create run  │           │           │              │            │        │         │           │         │
│              │─────────────▶ validate  │           │              │            │        │         │           │         │
│ SSE /events  │             │──────────▶ plan       │              │            │        │         │           │         │
│◀─────────────│             │           │──────────▶ profile+map   │            │        │         │           │         │
│  node events │             │           │           │─────────────▶ ∥ quality   │        │         │           │         │
│  stream…     │             │           │           │              │ ∥ quant    │        │         │           │         │
│              │             │           │           │              │ ∥ graph    │        │         │           │         │
│              │             │           │           │              │ ∥ index    │        │         │           │         │
│              │             │           │           │              │───────────▶ score   │         │           │         │
│              │             │           │           │              │            │ ok────▶ select/  │           │         │
│              │             │           │           │              │            │        │ train   │           │         │
│              │             │           │           │              │            │        │────────▶ hypothesize│         │
│              │             │           │           │              │            │        │         │──────────▶ verify   │
│              │             │           │           │              │            │        │         │           │────────▶ narrate+
│              │             │◀──────────────────────────────────────────────────────────────────────────────────────────│ assemble
│              │             │ accept → close run                                                                          │
│◀─ run ready ─│             │                                                                                             │
```

### 6.2 Clarification interrupt & resume (no guessing, ever)

```
Gate node        LangGraph runtime        Control plane        UI / analyst
│ score < τ &        │                        │                     │
│ open questions     │                        │                     │
│──interrupt()──────▶│ checkpoint state       │                     │
│                    │───────────────────────▶│ run: awaiting_input │
│                    │                        │◀────────────────────│ GET /runs/{id}/interrupts
│                    │                        │  questions+options  │
│                    │                        │◀────────────────────│ POST answers (audited)
│                    │◀── Command(resume) ────│                     │
│◀─ resume at gate ──│  (answers → knowledge  │                     │
│ re-score, proceed  │   store: never asked   │                     │
│                    │   again, org-wide)     │                     │
```

### 6.3 Copilot question (RAG + verification)

```
User        Copilot graph      Tools                      Verifier      Stream
│ question      │                │                           │            │
│───────────────▶ retrieve ──────▶ vector_search (reports,   │            │
│               │                │ glossary, insights)       │            │
│               │ drill ─────────▶ sql / graph_query         │            │
│               │ draft answer + citations                   │            │
│               │───────────────────────────────────────────▶ resolve ids │
│               │                            verified/downgraded          │
│◀──────────────│◀──────────────────────────────────────────│── tokens ──▶│
│  answer + evidence chips + confidence                                   │
```

### 6.4 Drift → automatic retraining (governed)

```
Monitor(Evidently)   Retraining graph      ML Agent        MLflow       Human
│ drift > threshold      │                    │               │            │
│────trigger────────────▶│ open run           │               │            │
│                        │───────────────────▶ re-select      │            │
│                        │                    │ (framework may │            │
│                        │                    │  change family)│            │
│                        │                    │ train+backtest─▶ log runs   │
│                        │                    │ challenger beats champion?  │
│                        │  interrupt(): model promotion ────────────────▶ │ approve
│                        │◀──────────────────────────────────────────────── │
│                        │                    │ promote stage ─▶ Production │
│                        │ next analysis run uses new version; old predictions
│                        │ remain in ledger tagged with their model_version
```

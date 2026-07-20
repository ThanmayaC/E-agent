# 07 · Architecture Decision Log

Every major decision, its alternatives, and why the alternative lost.
Format: context → decision → justification → consequences.

---

**ADR-001 — Keep the deterministic-first, evidence-verified core; redesign around it, not over it.**
*Alternatives:* full rewrite; LLM-centric agents computing analytics.
*Justification:* the profiler/semantics/KPI/signals/gates/verifier stack is
the platform's differentiator and is proven by contract tests. LLM-computed
analytics reintroduce the exact hallucination class the platform exists to
eliminate. Rewriting working deterministic code adds risk with zero
capability gain. *Consequence:* v3 is an orchestration, persistence, ML, and
governance redesign; the intelligence engines migrate intact.

**ADR-002 — Eight true agents; everything else is a node, tool, or service.**
*Alternatives:* the requested 18-agent roster, one-agent-per-pipeline-stage.
*Justification:* an agent is warranted only where judgement exists (planning,
ambiguity resolution, hypothesis generation, narration, routing). Wrapping a
deterministic profiler in an LLM agent adds latency, cost, and a
nondeterministic failure mode to a solved problem — agentic costume, not
agentic architecture. Merged/demoted candidates are documented in 02 §5.2.
*Consequence:* fewer prompts to govern, budget enforcement is tractable, and
the run graph stays legible to humans.

**ADR-003 — LangGraph as the orchestration backbone.**
*Alternatives:* keep imperative pipeline; Airflow/Prefect; CrewAI/AutoGen.
*Justification:* the control flow already *is* a stateful graph with a
human-in-the-loop pause (v2's clarification gate), retries, branching, and
re-entry. LangGraph provides checkpointed state, `interrupt()`/resume,
per-node retry, and parallel branches natively. Airflow/Prefect orchestrate
batch DAGs, not conversational interrupts with typed shared state.
CrewAI/AutoGen optimize for free-form agent chatter — the opposite of this
platform's typed-state, deterministic-routing doctrine. *Consequence:* the
awaiting-clarification flow becomes durable and resumable at the exact node;
run events stream naturally; a new orchestration dependency must be pinned
and integration-tested.

**ADR-004 — The Evidence Verifier is deterministic. It is never an LLM.**
*Alternatives:* LLM-as-judge verification; self-critique loops.
*Justification:* the component that catches probabilistic errors must not
itself be probabilistic — an LLM judge can hallucinate a verification.
Citation resolution against a content-hashed ledger is exact, cheap, and
auditable. LLM self-critique may *precede* verification as a quality pass,
but the gate is code. *Consequence:* verification failure rate becomes a
trustworthy platform KPI; repair loops route back to agents with exact,
machine-generated error messages.

**ADR-005 — Evidence Ledger as a first-class subsystem (append-only, content-hashed, cited).**
*Alternatives:* keep evidence ids inline in context JSON (v2); free-form RAG.
*Justification:* "no unsupported statements" must be enforceable at the data
layer: statements/citations/evidence as relational rows make every report
auditable with one join and make lineage queryable. Content-hash ids
deduplicate and make evidence tamper-evident. Registering retrieval chunks as
evidence closes the RAG loophole (retrieved-but-unverifiable context).
*Consequence:* modest write amplification; total auditability; ML and graph
outputs join the same trust fabric as KPIs.

**ADR-006 — Kùzu embedded as default graph store; Neo4j as enterprise adapter; NetworkX demoted to algorithm library.**
*Alternatives:* Neo4j only; keep NetworkX-in-JSON.
*Justification:* NetworkX-in-JSON cannot persist incrementally, query
declaratively, or scale; mandating Neo4j imposes a server dependency on every
small deployment. Kùzu gives Cypher + embedded operation (fits the lite
profile); the `GraphStore` interface keeps Neo4j a config choice.
*Consequence:* two adapters to maintain; graph reasoning (paths, motifs,
communities) becomes a citable evidence producer.

**ADR-007 — Polyglot persistence by plane: Postgres control / DuckDB+Parquet data / Qdrant vectors / Kùzu graph.**
*Alternatives:* Postgres-for-everything; keep JSON artifact files.
*Justification:* JSON files as a database preclude concurrency, RBAC, audit,
and retention — disqualifying for enterprise. Postgres-for-everything forces
row-store analytics and mediocre ANN at scale. Each engine here is best-in-
class for its access pattern, and DuckDB/Celery/Redis are already proven in
v2. *Consequence:* more moving parts — mitigated by the two deployment
profiles (lite collapses to Postgres+pgvector+Kùzu embedded) and by
interfaces over every store.

**ADR-008 — Internal feature store with Feast-compatible interfaces; MLflow adopted outright.**
*Alternatives:* adopt Feast now; build a bespoke registry.
*Justification:* asymmetric build-vs-buy: a registry/tracking server is
undifferentiated heavy lifting where MLflow is the standard — adopt. Feast's
value (online serving, streaming sources) is not yet needed at Excel-to-
Parquet scale — but point-in-time correctness *is*, so we build the thin
offline layer with Feast-shaped interfaces to keep adoption a refactor, not a
rewrite. *Consequence:* minimal ops now; a documented graduation path.

**ADR-009 — Model Selection Framework: gates → priors → champion/challenger. Nothing hardcoded, including neural networks.**
*Alternatives:* fixed size→algorithm mapping; full AutoML (auto-sklearn/FLAML).
*Justification:* fixed mappings are wrong at the margins and unauditable;
black-box AutoML is unexplainable to governance. Eligibility gates encode
statistical honesty (no transformer on 40 rows), priors encode expert
knowledge (the requested mapping, as search order), and rolling-backtest
evaluation is the only judge. "No model admitted" is a passing outcome that
becomes a limitation + recommendation. *Consequence:* every model in
production carries its selection trace; compute spent on evaluation is
bounded by Planner budgets.

**ADR-010 — Neural networks admitted per use case, never as replacement for deterministic analytics.**
*Alternatives:* deep-learning-first forecasting; no deep learning.
*Justification:* the evidence contract requires intervals and explanations —
so TFT/DeepAR with quantile heads (intervals feed the existing forecast
gates) and SHAP/attention artifacts are the only admissible forms.
Embeddings, multi-series forecasting, and multivariate anomaly detection are
places where deterministic methods measurably plateau; single short series
and small tabular data are not. *Consequence:* PyTorch enters the stack
behind the selection gates; CPU/ONNX inference keeps deployments light.

**ADR-011 — Predictions are evidence: model outputs enter the ledger with version, card, and explanation, or not at all.**
*Alternatives:* separate "ML results" surface consumed directly by the UI/LLM.
*Justification:* a second, unverified channel into narration would fork the
trust model — the exact defect the platform exists to prevent. One fabric:
the churn score is citable, auditable, and lineage-traceable exactly like a
KPI. *Consequence:* the ledger schema carries `model_version` and
`explanation`; inference without explainability artifacts is rejected.

**ADR-012 — Human-in-the-loop as checkpointed graph interrupts (clarifications, report sign-off, model promotion).**
*Alternatives:* v2's status-flag pause + full re-run; fire-and-forget approvals.
*Justification:* v2 proved the doctrine (never guess); LangGraph makes it
durable — resume at the exact node days later, with the approval recorded
(who/when/what) in the control plane for audit. Model promotion approval is a
governance requirement, not a UX flourish. *Consequence:* three interrupt
points instrumented; approvals become queryable compliance artifacts.

**ADR-013 — OIDC + RBAC enforced in the tool layer, not only at the API edge.**
*Alternatives:* API-gateway-only authorization.
*Justification:* agents execute tools autonomously; if authorization lives
only at the HTTP edge, a prompt-injected agent could reach beyond its
project. Scoping every tool call to the run initiator's claims makes
privilege escalation structurally impossible rather than prompt-discouraged.
*Consequence:* tool signatures carry scope context; slight overhead per call;
defense-in-depth consistent with the platform's injection doctrine.

**ADR-014 — Strangler migration with golden-run parity gates; v1 API preserved via facade until the UI completes v2 adoption.**
*Alternatives:* big-bang rewrite; long-lived v3 branch.
*Justification:* the platform has users, working tests, and a trust contract
today. Golden-run diffs (evidence, statements, report structure) convert
"refactor safely" from intention to a merge gate. A long-lived branch would
rot against the moving deterministic core. *Consequence:* temporary
dual-write cost (Phases A–D); zero downtime; every phase independently
shippable and reversible by flag.

# EDIP v3 — Enterprise Multi-Agent Decision Intelligence Platform

**Status:** Proposed target architecture (v3) · **Baseline:** v2.1 (deterministic-first pipeline, evidence-verified LLM narration)
**Owner:** Chief AI Architect · **Authors:** Principal AI Architecture review

This document set is the complete redesign of EDIP into an enterprise
multi-agent decision-intelligence platform in the class of Palantir Foundry,
Databricks, and Microsoft Fabric — while keeping the one property that makes
this platform different from "a dashboard with ChatGPT attached":

> **Every statement the platform emits is either deterministic evidence or a
> labelled, verified, citation-bearing interpretation of that evidence.**

v3 does not weaken that contract. It industrializes it.

---

## Reading map — the 20 requested outputs

| # | Requested output | Where |
|---|---|---|
| 1 | Complete new architecture | [01-system-architecture.md](01-system-architecture.md) §1–2 |
| 2 | Folder structure | [01-system-architecture.md](01-system-architecture.md) §5 |
| 3 | LangGraph architecture | [02-orchestration-langgraph.md](02-orchestration-langgraph.md) §1–4 |
| 4 | Agent responsibilities | [02-orchestration-langgraph.md](02-orchestration-langgraph.md) §5 |
| 5 | ML platform architecture | [03-ml-platform.md](03-ml-platform.md) §1–6 |
| 6 | Neural network architecture | [03-ml-platform.md](03-ml-platform.md) §7–8 |
| 7 | Knowledge graph architecture | [04-knowledge-and-retrieval.md](04-knowledge-and-retrieval.md) §1 |
| 8 | Vector database architecture | [04-knowledge-and-retrieval.md](04-knowledge-and-retrieval.md) §2 |
| 9 | Data flow | [01-system-architecture.md](01-system-architecture.md) §4 |
| 10 | Sequence diagrams | [02-orchestration-langgraph.md](02-orchestration-langgraph.md) §6 |
| 11 | Technology stack | [01-system-architecture.md](01-system-architecture.md) §3 |
| 12 | Backend redesign | [05-platform-engineering.md](05-platform-engineering.md) §1 |
| 13 | Frontend redesign | [05-platform-engineering.md](05-platform-engineering.md) §5 |
| 14 | API redesign | [05-platform-engineering.md](05-platform-engineering.md) §2 |
| 15 | Database redesign | [05-platform-engineering.md](05-platform-engineering.md) §3 |
| 16 | Migration plan | [06-migration-and-roadmap.md](06-migration-and-roadmap.md) §2 |
| 17 | Implementation roadmap | [06-migration-and-roadmap.md](06-migration-and-roadmap.md) §3 |
| 18 | Modules retained | [06-migration-and-roadmap.md](06-migration-and-roadmap.md) §1.1 |
| 19 | Modules rewritten | [06-migration-and-roadmap.md](06-migration-and-roadmap.md) §1.2 |
| 20 | Decision justifications | [07-decision-log.md](07-decision-log.md) (ADR-001 … ADR-014) |

Security, observability, and performance requirements are covered in
[05-platform-engineering.md](05-platform-engineering.md) §4, §6, §7.

---

## The five design principles of v3

**P1 — Evidence is the spine, not a feature.**
v2 introduced evidence ids, statement types, and deterministic verification.
v3 promotes this into a first-class subsystem: the **Evidence Ledger**. Every
producer — deterministic analytics, ML models, graph reasoning, retrieval —
writes typed, immutable, id-carrying evidence records. Every consumer (LLM
narration, recommendations, reports, copilot) must cite ledger ids, and a
deterministic verifier enforces it. ML predictions do not bypass this: a
neural forecast is evidence *with a model card and explanation attached*, or
it does not exist.

**P2 — Agents only where decisions live.**
An "agent" that deterministically runs a profiler is a function with expensive
overhead. v3 defines **8 true agents** (they plan, choose, judge, or narrate)
and executes everything else as deterministic LangGraph nodes and tools. This
is the difference between an agentic architecture and an agentic costume.
(See ADR-002 for the full disposition of the 18 candidate agents.)

**P3 — Deterministic first, ML second, LLM last.**
Statistics that can be computed are computed. ML models are admitted only when
a champion/challenger evaluation proves lift over the deterministic baseline.
The LLM narrates, hypothesizes (labelled), and plans — it never computes, and
its every claim is checked against the ledger.

**P4 — Control plane / data plane / reasoning plane separation.**
Metadata, runs, audit, RBAC, lineage → Postgres (control plane). Tabular
analytics → DuckDB + Parquet (data plane). Agents, tools, LLM, models →
reasoning plane, stateless workers reading/writing the other two planes.
This is what makes the platform horizontally scalable and auditable.

**P5 — Humans are a node type, not an afterthought.**
The v2 clarification gate ("pause instead of guessing") becomes a native
LangGraph `interrupt()`: clarifications, report sign-off, and model promotion
are checkpointed human-approval nodes with full resume semantics.

---

## What v3 is at a glance

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  EXPERIENCE      React consoles: Runs · Evidence · Models · Graph · Copilot │
├─────────────────────────────────────────────────────────────────────────────┤
│  API             FastAPI v2 (OIDC, RBAC, SSE streaming) + v1 compat facade  │
├─────────────────────────────────────────────────────────────────────────────┤
│  ORCHESTRATION   LangGraph: Supervisor · Planner · 6 specialist agents      │
│                  + deterministic nodes, checkpointed in Postgres,           │
│                  human-approval interrupts, parallel fan-out                │
├──────────────────────────┬──────────────────────────┬───────────────────────┤
│  INTELLIGENCE            │  ML PLATFORM             │  KNOWLEDGE SERVICES   │
│  connectors, profiling,  │  feature store, MLflow   │  knowledge graph      │
│  semantics, KPIs,        │  registry, training/     │  (Kùzu/Neo4j),        │
│  signals, quality,       │  inference pipelines,    │  vector DB (Qdrant),  │
│  forecast gates,         │  model selection,        │  enterprise knowledge,│
│  confidence, verifier    │  drift monitoring, SHAP  │  RAG services         │
├──────────────────────────┴──────────────────────────┴───────────────────────┤
│  EVIDENCE LEDGER   typed, immutable, citable facts — the only reasoning I/O │
├─────────────────────────────────────────────────────────────────────────────┤
│  DATA & CONTROL    Postgres · DuckDB/Parquet · S3/MinIO · Redis · Celery    │
├─────────────────────────────────────────────────────────────────────────────┤
│  FOUNDATIONS       OpenTelemetry · Prometheus · OpenLineage · OIDC · Vault  │
└─────────────────────────────────────────────────────────────────────────────┘
```

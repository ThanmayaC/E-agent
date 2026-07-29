# EnterpriseAI v4 — Desktop Work-Automation Platform

**Status:** Proposed target architecture (v4) · **Baseline:** v3.1 (web platform, per the [`architecture-v3/`](../architecture-v3/) set and the shipped v2.1→v3.1 milestones)
**Deliverable:** `EnterpriseAI.exe` — a production-grade Windows desktop application installed on employee laptops
**Owner:** Principal Enterprise Architect · **Authors:** Enterprise Architecture review

---

## What changes, and what does not

v1→v3.1 built a **web application** that *understands* an enterprise: the Enterprise
Brain, Knowledge Graph, Memory Engine, Decision Intelligence, Executive Copilot, the
Synthetic Enterprise Generator, and a clean layered FastAPI backend + React frontend.

v4 does **not** discard any of it. It does two things:

1. **Repackages** the platform from a shared web deployment into an **independent,
   per-laptop desktop application** — one install per employee, operating on *that
   person's* Outlook, Teams, files, and permissions, with no central database required
   in v1.
2. **Adds a work-automation superstructure** on top of the existing intelligence so the
   product *does work* — creates and edits documents, updates spreadsheets, drafts and
   (with approval) sends mail — instead of only answering questions.

> **The Enterprise Brain stops being the whole product and becomes one internal
> reasoning service.** It reasons; it never touches Outlook, Excel, or the filesystem.
> A new **Action Engine** does that, under a **Task Planner**, a **Context Manager**, a
> **Workflow Engine**, and an **Approval Engine**.

The single most important enabling fact from the existing codebase: **configuration is
already 100% environment-driven (`EDIP_*`) with a "lite profile"** — SQLite control
plane, in-memory/file vector store, local-file connectors, Ollama/local LLM, every layer
independently `*_ENABLED`. That lite profile *is* the desktop profile. We are not
rewriting the backend; we are **embedding it as a local sidecar** and building the
desktop shell, connectors, and automation engines around it.

---

## Reading map — the 25 requested deliverables

| # | Deliverable | Where |
|---|-------------|-------|
| 1 | Complete production architecture | [01-system-architecture.md](01-system-architecture.md) §1–3 |
| 2 | Folder structure | [01-system-architecture.md](01-system-architecture.md) §6 |
| 3 | Module responsibilities | [01-system-architecture.md](01-system-architecture.md) §4 · [06-brain-services-and-intelligence.md](06-brain-services-and-intelligence.md) |
| 4 | Data flow diagrams | [07-flows-and-class-model.md](07-flows-and-class-model.md) §1 |
| 5 | Sequence diagrams | [07-flows-and-class-model.md](07-flows-and-class-model.md) §2 |
| 6 | Component diagrams | [01-system-architecture.md](01-system-architecture.md) §2 |
| 7 | Class relationships | [07-flows-and-class-model.md](07-flows-and-class-model.md) §3 |
| 8 | Technology stack | [01-system-architecture.md](01-system-architecture.md) §5 |
| 9 | Connector architecture | [05-workflow-connectors-plugins.md](05-workflow-connectors-plugins.md) §2–4 |
| 10 | Desktop runtime architecture | [02-desktop-runtime-and-packaging.md](02-desktop-runtime-and-packaging.md) §1–3 |
| 11 | Authentication flow | [03-security-and-auth.md](03-security-and-auth.md) §1–2 |
| 12 | Context Manager design | [04-context-planner-action.md](04-context-planner-action.md) §1 |
| 13 | Planner design | [04-context-planner-action.md](04-context-planner-action.md) §2 |
| 14 | Action Engine design | [04-context-planner-action.md](04-context-planner-action.md) §3 |
| 15 | Workflow Engine design | [05-workflow-connectors-plugins.md](05-workflow-connectors-plugins.md) §1 |
| 16 | Plugin architecture | [05-workflow-connectors-plugins.md](05-workflow-connectors-plugins.md) §5 |
| 17 | Security architecture | [03-security-and-auth.md](03-security-and-auth.md) §3–6 |
| 18 | Deployment architecture | [02-desktop-runtime-and-packaging.md](02-desktop-runtime-and-packaging.md) §4 |
| 19 | Packaging strategy | [02-desktop-runtime-and-packaging.md](02-desktop-runtime-and-packaging.md) §5–6 |
| 20 | Development roadmap | [08-delivery-migration-readiness.md](08-delivery-migration-readiness.md) §2 |
| 21 | Migration plan from the existing project | [08-delivery-migration-readiness.md](08-delivery-migration-readiness.md) §1 |
| 22 | Risk analysis | [08-delivery-migration-readiness.md](08-delivery-migration-readiness.md) §3 |
| 23 | Performance strategy | [08-delivery-migration-readiness.md](08-delivery-migration-readiness.md) §4 |
| 24 | Scalability strategy | [08-delivery-migration-readiness.md](08-delivery-migration-readiness.md) §5 |
| 25 | Production-readiness checklist | [08-delivery-migration-readiness.md](08-delivery-migration-readiness.md) §6 |

Cross-cutting: the **Approval Engine** and **human-in-the-loop** are in
[05-workflow-connectors-plugins.md](05-workflow-connectors-plugins.md) §1.4; **Role
Agents** and the **AI provider abstraction** in
[06-brain-services-and-intelligence.md](06-brain-services-and-intelligence.md) §4–5;
key **justifications** are recorded as ADRs in [09-decision-log.md](09-decision-log.md).

---

## The seven design principles of v4

**P1 — Reason and act are separate planes.** The Brain (and every intelligence engine)
produces *evidence and plans*. The Action Engine *executes* them against Outlook, Excel,
Word, and files. Neither can do the other's job. This is the invariant that makes the
platform safe to install on ten thousand laptops.

**P2 — Every side-effect is a planned, verifiable, reversible Action.** No engine writes
to a user's data directly. All writes flow through the Action Engine as typed Actions
that carry a *pre-image* for rollback and a *post-condition* for verification, and are
recorded in a per-laptop audit ledger.

**P3 — The evidence contract is preserved.** v2's rule — *every emitted statement is
either deterministic evidence or a labelled, citation-bearing interpretation verified
against the Evidence Ledger* — carries forward unchanged. Automation does not get to
hallucinate the number it writes into a cell.

**P4 — Least data, least privilege, on-device by default.** The Context Manager
discovers *only what the current task needs*; it never indexes the whole PC. Microsoft
Graph is reached with narrowly-scoped OAuth (delegated, per-user). Approved folders
only. Tokens live in the OS keystore; the Brain's stores live encrypted on the local
disk. Nothing leaves the laptop unless the user's own enterprise service is the
destination.

**P5 — Independent installs, no central dependency (v1).** Each `EnterpriseAI.exe`
operates on local resources and the enterprise services *that user* can reach. There is
no shared database, no shared queue, no server to stand up. (v2+ optional central control
is designed for, not required — see [08](08-delivery-migration-readiness.md) §5.)

**P6 — Additive layering, disable-able to prior behaviour.** Continues the codebase's
existing discipline: extend registries, keep v1 method signatures, gate every new layer
behind an `EDIP_*_ENABLED` flag, never duplicate the Runtime/Scheduler/Brain, expose a
`status()` dict per layer. Every v4 subsystem can be turned off back to v3.1 behaviour.

**P7 — It should feel like Office / VS Code.** Native window, tabbed workspace, dockable
panels, command palette, global search, notifications, dark mode, accessibility,
offline-tolerant. The web UI is retained as a debug/admin surface, not the product.

---

## v4 at a glance

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  ENTERPRISE DESKTOP RUNTIME   Tauri shell · WebView2 · command palette ·       │
│                               tabs · dockable panels · tray · notifications    │
├──────────────────────────────────────────────────────────────────────────────┤
│  AUTHENTICATION LAYER         MSAL delegated OAuth · token cache in DPAPI /     │
│                               Windows Credential Manager · no passwords stored  │
├──────────────────────────────────────────────────────────────────────────────┤
│  ROLE MANAGEMENT              role profile → workflows · permissions · prompts ·│
│                               dashboards · tool allow-list (extends Governance) │
├──────────────────────────────────────────────────────────────────────────────┤
│  TASK PLANNER                 intent → steps → resources → connectors → plan    │
│                               (LangGraph plan graph; reuses reasoning + evidence)│
├──────────────────────────────────────────────────────────────────────────────┤
│  CONTEXT MANAGER              task-scoped discovery: only the mail/chats/files/  │
│                               workbook/prior reports this task needs            │
├───────────────────────────┬─────────────────────────┬──────────────────────────┤
│  ENTERPRISE BRAIN          │  KNOWLEDGE GRAPH        │  MEMORY ENGINE           │
│  (reason/plan/summarize,   │  business entities:     │  files/convos/reports/  │
│   business+doc under-      │  products·projects·KPIs·│  entities·prefs·current  │
│   standing) — REASONS ONLY │  incidents·people·docs  │  task·prior executions   │
├───────────────────────────┴─────────────────────────┴──────────────────────────┤
│  DECISION INTELLIGENCE        priority · risk · impact · confidence · approval  │
├──────────────────────────────────────────────────────────────────────────────┤
│  ACTION ENGINE                create·edit·move·rename·delete·version·update·    │
│                               export·generate·verify·ROLLBACK (only writer)     │
├──────────────────────────────────────────────────────────────────────────────┤
│  WORKFLOW ENGINE              sequential·parallel·conditional·retry·compensate· │
│                               approvals·scheduling·human-in-the-loop·templates  │
├──────────────────────────────────────────────────────────────────────────────┤
│  APPROVAL ENGINE              configurable policies gating external/destructive │
│                               actions before the Action Engine executes them    │
├──────────────────────────────────────────────────────────────────────────────┤
│  CONNECTOR FRAMEWORK          pluggable: MS Graph (Mail·Calendar·Teams·OneDrive·│
│                               SharePoint·Profile) · Office (Word·Excel·PPT·PDF) │
│                               · Local Files · SQLite · REST · CSV/JSON          │
├──────────────────────────────────────────────────────────────────────────────┤
│  LOCAL DATA & OBSERVABILITY   SQLite control+audit · file/embedded vector store │
│                               · OS keystore · encrypted stores · telemetry/logs │
└──────────────────────────────────────────────────────────────────────────────┘
```

Layers **Enterprise Brain → Knowledge Graph → Memory → Decision Intelligence** are the
**existing** codebase (`backend/app/brain`, `app/knowledge`, `app/memory`,
`app/runtime/intelligence.py`, `app/executive`) running *unchanged in intent*, now
addressed as internal services rather than the top-level product. Everything above and
below them is new v4 superstructure, most of which **reuses existing registries**
(`app/connectors`, `app/workflows`, `app/governance`, `app/runtime`).

Continue to [01-system-architecture.md](01-system-architecture.md).

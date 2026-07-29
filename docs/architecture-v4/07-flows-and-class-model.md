# 07 — Data Flow, Sequence Diagrams & Class Model

> Deliverables covered: **#4** data flow diagrams · **#5** sequence diagrams · **#7** class
> relationships.

---

## 1. Data flow (deliverable #4)

### 1.1 End-to-end: from enterprise apps to completed work

```mermaid
flowchart TB
    subgraph Sources["Enterprise apps (this user)"]
        Mail["Outlook"]; Teams; Cal["Calendar"]; Drive["OneDrive/SharePoint"]; Files["Approved local files"]
    end
    Mail & Teams & Cal & Drive & Files -->|read/watch delta| CF["Connector Framework"]
    CF -->|Knowledge Packages| DP["Document Intelligence\n(parse · chunk · embed)"]
    DP --> KStore["Knowledge Store + Vector store"]
    DP --> KG["Knowledge Graph (entities)"]
    KStore & KG --> Brain["Enterprise Brain"]
    Brain --> DI["Decision Intelligence"]

    User(["User task"]) --> Planner
    Planner -->|discover| Ctx["Context Manager"]
    Ctx -->|scoped queries| CF
    Ctx -->|evidence-tagged bundle| Ledger[("Evidence Ledger")]
    Ctx --> Brain
    Brain -->|proposals + evidence ids| Planner
    DI -->|risk/impact/confidence| Planner
    Planner -->|Plan = DAG of Actions| WE["Workflow Engine"]
    WE --> AP["Approval Engine"]
    AP -->|approved| AE["Action Engine"]
    AE -->|journal pre-image| Audit[("Audit Ledger")]
    AE -->|write + verify| CF
    CF -->|effects| Sources
    AE -->|result| Audit
    AE -->|current-task state| Mem["Memory"]
```

**Two directions through one framework:** knowledge flows *up* (read/watch → Brain);
work flows *down* (Plan → Action Engine → write). The Evidence Ledger and Audit Ledger are
the two immutable records that make every claim and every effect accountable.

### 1.2 Trust/data-boundary view

```mermaid
flowchart LR
    subgraph OnDevice["On-device (never leaves unless user opts in)"]
        Core["Core: Brain·Graph·Memory·Planner·Actions"]
        Local["SQLite · vector · knowledge · audit"]
        LocalLLM["Local model (Ollama)"]
    end
    subgraph UserCloud["The user's own enterprise services"]
        Graph["Microsoft 365 (delegated)"]
    end
    subgraph OptIn["Opt-in only"]
        CloudLLM["Cloud AI provider\n(redacted prompts)"]
        Fleet["Fleet control plane\n(telemetry/policy)"]
    end
    Core <--> Graph
    Core --> Local
    Core --> LocalLLM
    Core -. opt-in .-> CloudLLM
    Core -. opt-in .-> Fleet
```

---

## 2. Sequence diagrams (deliverable #5)

### 2.1 "Update the Weekly Report" (the flagship flow)

```mermaid
sequenceDiagram
    autonumber
    participant U as User
    participant UI as Workspace
    participant PL as Task Planner
    participant CM as Context Manager
    participant BR as Enterprise Brain
    participant DI as Decision Intelligence
    participant WE as Workflow Engine
    participant AP as Approval Engine
    participant AE as Action Engine
    participant XL as Excel connector
    participant WD as Word connector
    participant OL as Outlook connector

    U->>UI: "Update the Weekly Report"
    UI->>PL: plan(intent, role)
    PL->>PL: understand_intent (confidence ok)
    PL->>CM: discover(task, budget)
    CM->>XL: read KPI workbook
    CM->>OL: recent related threads
    CM-->>PL: TaskContext (evidence-tagged)
    PL->>BR: summarize_changes(context)
    BR-->>PL: narrative + evidence ids
    PL->>DI: score(plan)
    DI-->>PL: risk/impact/confidence, approval hints
    PL-->>WE: Plan [read→summarize→draft_report→verify→draft_email(gate)]
    WE->>AE: EDIT/GENERATE Word report
    AE->>WD: capture pre-image → write (tracked) → re-read verify
    AE-->>WE: report v+1 (verified)
    WE->>AE: SEND email (approval_required)
    AE->>AP: request approval (draft + evidence + preview)
    AP->>UI: approval request
    UI->>U: review draft
    U-->>UI: Approve
    UI-->>AP: approved (this action, this session)
    AP-->>AE: proceed
    AE->>OL: send
    AE-->>WE: sent (audited)
    WE-->>UI: done — report updated, email sent
```

### 2.2 Autonomous overnight cadence (no user present)

```mermaid
sequenceDiagram
    autonumber
    participant SC as Scheduler (in-process)
    participant SY as Sync/Connectors
    participant BR as Brain
    participant DI as Decision Intelligence
    participant PL as Planner
    participant WE as Workflow Engine
    participant AP as Approval Engine
    participant Q as Approval inbox

    SC->>SY: nightly sync (delta read Mail/Teams/Files)
    SY->>BR: knowledge refresh
    BR->>DI: observe → propose (e.g. "draft status email")
    DI->>PL: proposal + confidence
    PL->>WE: Plan (draft-only steps)
    WE->>AP: gate SEND action
    AP->>Q: queue draft for morning approval (no auto-send)
    Note over Q: user arrives, reviews Approval Center, approves/edits
```

External effects are **drafted, never auto-sent** while unattended — the Approval Engine
holds them (existing "queued until approved" behaviour).

### 2.3 Crash mid-edit → safe recovery

```mermaid
sequenceDiagram
    autonumber
    participant AE as Action Engine
    participant J as Audit Journal
    participant Core as Core (restart)
    participant WD as Word connector
    AE->>J: append {EDIT report, pre-image} = in-flight
    AE->>WD: begin write
    Note over AE,WD: 💥 Core crashes mid-write
    Core->>J: scan in-flight entries on startup
    Core->>WD: read current state
    alt post-condition not met
        Core->>WD: restore pre-image (rollback)
        Core->>J: mark rolled_back
    else already applied
        Core->>J: mark committed
    end
    Core-->>AE: resume plan at next Step
```

---

## 3. Class relationships (deliverable #7)

```mermaid
classDiagram
    class Container {
        +settings: Settings
        +brain: EnterpriseBrain
        +planner: TaskPlanner
        +context: ContextManager
        +actions: ActionEngine
        +approvals: ApprovalEngine
        +workflows: WorkflowEngine
        +connectors: ConnectorFramework
        +roles: RoleManager
        +identity: IdentityService
    }

    class TaskPlanner {
        +plan(Intent, RoleProfile) Plan
        +replan(Plan, StepFailure) Plan
        +status() dict
    }
    class ContextManager {
        +discover(TaskSpec, ContextBudget) TaskContext
        +refine(TaskSpec, feedback) TaskContext
    }
    class EnterpriseBrain {
        +reason(TaskContext) Reasoning
        +summarize(TaskContext) Summary
    }
    class DecisionIntelligence {
        +score(Plan) DecisionScore
    }
    class WorkflowEngine {
        +run(id, WorkflowContext) WorkflowRun
        +resume(run_id, Decision) WorkflowRun
        +compensate(run_id)
    }
    class ApprovalEngine {
        +gate(Action, evidence) Decision
    }
    class ActionEngine {
        +execute(Action) ActionResult
        +rollback(action_id)
        +verify(action_id) VerificationResult
    }
    class ConnectorFramework {
        +register(Connector)
        +read(SourceQuery) Records
        +write(Action) WriteResult
    }
    class Connector {
        <<interface>>
        +capabilities: set~Capability~
        +scopes: set~str~
        +health() HealthStatus
        +read(SourceQuery)
        +write(Action)
    }
    class RoleManager {
        +profile(user) RoleProfile
    }
    class IdentityService {
        +login() Account
        +token(scopes) AccessToken
    }
    class Plan { +steps: Step[] }
    class Step { +kind; +action: Action; +approval_required }
    class Action {
        +kind: ActionKind
        +target: ResourceRef
        +evidence: str[]
        +reversible: bool
        +approval_required: bool
    }

    Container --> TaskPlanner
    Container --> ContextManager
    Container --> EnterpriseBrain
    Container --> DecisionIntelligence
    Container --> WorkflowEngine
    Container --> ApprovalEngine
    Container --> ActionEngine
    Container --> ConnectorFramework
    Container --> RoleManager
    Container --> IdentityService

    TaskPlanner --> ContextManager : requests context
    TaskPlanner --> EnterpriseBrain : reasons via
    TaskPlanner --> DecisionIntelligence : scores via
    TaskPlanner --> Plan : produces
    Plan "1" *-- "many" Step
    Step --> Action
    WorkflowEngine --> ApprovalEngine : gates
    WorkflowEngine --> ActionEngine : executes
    ApprovalEngine --> DecisionIntelligence : policy inputs
    ActionEngine --> ConnectorFramework : writes via
    ConnectorFramework o-- Connector : registry of
    ContextManager --> ConnectorFramework : reads via
    RoleManager --> ApprovalEngine : supplies policy
    IdentityService --> ConnectorFramework : supplies tokens
```

**Dependency direction (enforced by the DI Container as the only composition root):** the
Planner depends on the reasoning services and produces a Plan; the Workflow Engine depends
on the Approval and Action Engines; the Action Engine depends only on the Connector
Framework. **No reasoning class depends on a connector or the Action Engine** — the
reason/act separation (P1) is a compile-time property of the class graph, not a convention.

Continue to [08-delivery-migration-readiness.md](08-delivery-migration-readiness.md).

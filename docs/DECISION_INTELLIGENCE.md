# Decision Intelligence (V2.4)

V2.4 transforms the Enterprise Brain from an **information system** into a
**decision system**. The Brain no longer waits to be asked: it continuously
reasons about the organization and proactively proposes the actions that
require attention, each as a first-class, remembered decision.

Nothing here is a new framework, registry, or runtime. The layer
(`app/runtime/intelligence.py`, `DecisionIntelligence`) **reuses** what the
platform already owns:

| It needs to… | It reuses… |
| --- | --- |
| Observe | the Event Bus (live) + the Scheduler (the periodic sweep) |
| Execute an approved decision | the existing **Decision Engine → Action Queue → executors** |
| Remember decisions | the **KnowledgeStore** (`record_decision`, learning events) |
| Represent the Decision Graph | the **Enterprise Knowledge Graph** (`graph.py`) |
| Surface to executives | the **Executive Workspace** (Home) |

`EDIP_DECISION_INTELLIGENCE_ENABLED=false` returns the platform to V2.3
behaviour exactly: the Decision Engine still executes recommendations;
nothing observes or proposes, and every API still answers.

## The loop

```
Observe  → Propose        → Rank                → Decide            → Learn
(signals)  (lifecycle rec)  (7 transparent       (approve/reject/    (organizational
                            factors)              modify)             memory)
                                                       │
                                        approved ──────┘
                                                       ▼
                                        Decision Engine → Action Queue → executor
```

### 1. Observe — proactive detection

Two paths funnel into the same `propose`:

- **Live** — bus subscriptions turn events into candidate decisions the
  moment they happen: `AnomalyDetected`, `RiskIncreased`,
  `KPIThresholdCrossed`, `GrowthRiskDetected`,
  `PredictionConfidenceDropped`, and a health-erosion rule on
  `PortfolioChanged`.
- **Sweep** — the `decision_observe` scheduler job (every 15 min by default)
  runs every detector: KPI deterioration, repeated RCAs, conflicting SOPs,
  meeting decisions without follow-up tasks, missed (overdue) action items,
  delayed (unanswered) decisions, and knowledge gaps. Detectors are
  independent — one failing is recorded and never stops the sweep — and the
  sweep also retires stale proposals.

Repeated RCAs and conflicting SOPs are found by **clustering document titles
on shared content words**, not exact-title matching, so the third RCA about
"settlement failures" is caught even when the titles differ ("…in March" vs
"…(repeat)").

Every observation is recorded as a **signal** and, unless an equivalent
decision is already open, becomes a candidate decision. Observing the same
condition twice is repetition, not a new finding — it does not duplicate.

Example mappings (`SIGNAL_PLAYBOOK`):

| Observation | Candidate decision |
| --- | --- |
| Revenue / KPI declining | Investigate the deterioration in {subject} |
| Settlement failures increasing | Escalate the increase to Operations |
| Repeated RCA | Recommend an SOP review |
| Meeting decision recorded | Create follow-up tasks |
| Growth risk detected | Recommend mitigation |

### 2. The decision lifecycle

Every candidate is a full record, stored in `data/runtime/decision_records.json`:

`decision_id · priority · confidence · reasoning · evidence_ids ·
affected_products · affected_teams · expected_impact · owner · status ·
dependencies · strategic_weight · historical_success · created_by ·
created_at · updated_at · history[]`

Statuses: **proposed → modified → approved → rejected → executed → expired →
cancelled**. Each transition appends to `history` (status, timestamp, actor,
note). An equivalent *open* decision (`proposed·modified·approved`) is never
proposed twice.

### 3. Rank — show only the highest-value decisions

`rank()` scores open decisions on seven transparent factors, weighted by
`RANKING_WEIGHTS` (impact 0.25, urgency 0.20, confidence 0.15, evidence 0.15,
history 0.10, risk 0.10, strategic 0.05). Every ranked record carries its
`factors` breakdown, so "why is this first?" is answered by data.

### 4. Decide — reuse the execution pipeline

Approving a decision does **not** re-implement execution: it calls the
Decision Engine's `decide()`, which runs the evidence → confidence → priority
→ approval → execute pipeline and queues the action. The record links to the
engine decision (`engine_decision_id`, `queued_action_id`), so the two trails
reference each other. When the queued action executes, the decision moves to
`executed`; the same monitor that closes engine decisions closes these.

### 5. Learn — organizational memory, no retraining

Every transition is a learning event, and each creation is registered as an
organizational decision in the KnowledgeStore. Ranking's **historical-success
factor** is the Laplace-smoothed approval record of past decisions of the
same *kind*: two rejected escalations lower every future escalation's rank.
No model is retrained — only organizational memory is consulted, exactly as
the milestone requires.

## The Decision Graph

The Decision Graph **is** the Enterprise Knowledge Graph. Each decision is a
`decision` node; its relations use the SDS vocabulary:

- `decision —affects→ product`
- `decision —depends_on→ <dependency>`
- `decision —implements→ rca` (repeated-RCA decisions)
- `decision —updates→ sop` (SOP-review decisions)
- `decision —creates→ action` (once executed)

Edges are written through the graph's own `batch()` API. Reasoning across
decision history is then just graph traversal — no separate store.

## Decision reports

`report(period)` composes **daily**, **weekly**, and **monthly** summaries
over the decision records: counts by status, decisions decided/executed, and
**effectiveness** (execution rate, approval-vs-rejection confidence, success
by kind) plus **recommendation outcomes** from the Decision Engine. The
`decision_daily_report` scheduler job publishes `DecisionReportGenerated`
each evening.

## Executive Workspace

The homepage (`frontend/src/pages/Home.jsx`) is no longer a passive
dashboard. Fed by `GET /runtime/intelligence/brief`, it leads with what
requires attention: **Top Decisions** (ranked, approve/reject inline),
**Recommended Actions**, Today's Executive Brief, Critical Risks, Pending
Approvals, and **Organizational Changes**. Approving a decision from Home
executes it through the Decision Engine.

## API

All under `/api/v1`. See [API.md](API.md) for the full table.

```
GET   /runtime/intelligence                    status
POST  /runtime/intelligence/observe            run the sweep now
GET   /runtime/intelligence/brief              executive workspace brief
GET   /runtime/intelligence/decisions          lifecycle records (?status=, ?kind=)
POST  /runtime/intelligence/decisions          propose manually
GET   /runtime/intelligence/decisions/{id}     one record
PATCH /runtime/intelligence/decisions/{id}     {status, by, note}
GET   /runtime/intelligence/recommendations    ranked, with factor breakdowns
GET   /runtime/intelligence/signals            observations (?kind=)
GET   /runtime/intelligence/reports/{period}   daily | weekly | monthly
```

## Configuration

| Setting | Default | Meaning |
| --- | --- | --- |
| `EDIP_DECISION_INTELLIGENCE_ENABLED` | `true` | Off = V2.3 behaviour exactly |
| `EDIP_DECISION_OBSERVE_INTERVAL_SECONDS` | `900` | Proactive sweep cadence |
| `EDIP_DECISION_REPORT_CRON` | `0 18 * * *` | Daily decision summary |
| `EDIP_DECISION_TTL_DAYS` | `14` | Unanswered proposals expire after this |

## Backward compatibility

- New event kinds (`SignalDetected`, `DecisionProposed`,
  `DecisionStatusChanged`, `DecisionReportGenerated`) and store sections
  (`decision_records`, `signals`) are **additive**.
- No existing signature changed; the Decision Engine, Action Queue, Knowledge
  Graph, and Workspace are consumed through their existing public interfaces.
- Full backend suite green (572 tests); frontend build green.

## Tests

`backend/tests/unit/test_decision_intelligence.py` — the lifecycle, dedupe,
graph edges, ranking, learning-from-history, every detector, the sweep
surviving a failing detector, reports, the brief, and the API surface end to
end through the real container.

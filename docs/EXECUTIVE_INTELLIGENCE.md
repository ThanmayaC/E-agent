# Executive Intelligence & Integration (V3.1)

V3.1 does not add data or change the Enterprise Brain. It **connects** the
intelligence the Brain already holds — the ingested NPCI UPI corpus, its KPI
workbooks, decisions, incidents, RCAs, SOPs and reports — into an executive
operating layer, so the workspace behaves like an AI Product Head rather than
a document-search interface.

Everything is additive: every existing API is preserved, and when no
enterprise is generated the layer runs empty and every surface behaves exactly
as before.

## The layer — `app/executive/`

- **`EnterpriseReader`** recovers the *structured* facts from the generated
  `enterprise_data/` tree: the KPI weekly series (from the workbook, the numeric
  source of truth), the bank/PSP/merchant performance sheets, the master data
  (products, banks, PSPs, merchants, employees), and the narrative artifacts
  (decisions, incidents, RCAs, SOPs, reports, meetings, tasks) parsed from their
  front-matter. Results are cached by the corpus's newest mtime, so a
  re-ingested or regenerated enterprise is reflected automatically.

- **`ExecutiveIntelligence`** reasons over those facts, deterministically and
  without hallucination (every number traces to the workbook):

  | Output | What it produces |
  | --- | --- |
  | `kpi_intelligence()` | Composite health (portfolio, operational, customer, merchant, growth, risk) + a card per KPI: value, change vs previous day, trend, **why it changed**, the cause, and a recommended action |
  | `executive_brief()` | Business summary, critical events, major decisions, risk assessment, products/banks/merchants at risk, customer impact, recommended actions, upcoming deadlines, priorities, confidence |
  | `priorities()` | Ranked Monday-morning priorities with reason, impact, confidence, and evidence — e.g. *"Monitor ICICI Bank recovery — Recent Sev-2 incident — High — 96%"* |
  | `recommendations()` | Ranked recommendations: title, reason, supporting evidence, business impact, confidence, owner, timeline, dependencies, status |
  | `decisions()` | Each decision **enhanced** (problem, alternatives considered, reason selected, expected/actual impact, affected products/banks/merchants/customers, confidence, business value, learning) and **ranked** by an executive-priority score |
  | `risks()` | Top operational risks, banks at risk, products at risk, merchants to follow up |
  | `patterns()` | Recurring bank, incident, merchants, KPI, and recommendation — the week's memory |
  | `build_business_graph(graph)` | Expands the knowledge graph into a business-entity graph |

## Business-entity knowledge graph

At startup the layer expands the document-centric graph into a **business**
graph using the enterprise graph's public `relate()` API — no Brain change.
Typed nodes for **employee, team, department, product, bank, PSP, merchant,
KPI, incident, decision, SOP, report** are joined by business relationships
(`OWNS`, `REPORTS_TO`, `WORKS_ON`, `AFFECTS`, `RESOLVES`, `CAUSED_BY`,
`INVOLVES`, `HAS_KPI`, `MONITORS`, `USES`, `GENERATED_FOR`, `REFERENCES`, …).
The graph grows from ~63 document nodes to **~206 nodes / ~389 edges** — the
Graph Explorer becomes a map of the organization, not just its documents.

## How the surfaces light up

- **Executive Dashboard & Cockpit** — the manager workspace and daily brief
  are enriched *additively*: when the platform runs the ingested enterprise
  (no analysis projects), empty panels are filled from the executive layer
  (portfolio health, critical risks, recommendations, recent decisions,
  products at risk). Real project data always wins; only blanks are filled.
- **Executive Brief** (`/brief`, new) — the flagship AI-Product-Head page:
  business summary, six health scores, ranked priorities, KPI intelligence
  cards (each with *why it changed*), decisions ranked by impact (with an
  explainable panel), recommendations, and risks. **Auto-refreshes** every 20s,
  as does the Cockpit — no manual reload.
- **Executive Copilot** — the executive summary is always in the Copilot's
  business context, and the executive facts (incident, KPI health, ranked
  decisions, priorities, recommendations, banks at risk) are admissible
  evidence, so the model **reasons** and the validator grounds the figures it
  quotes. This is what lets the Copilot answer structured questions without
  hallucination.

## API — `/api/v1/executive/*`

```
GET /executive                 status + how much enterprise it sees
GET /executive/brief           the daily executive brief
GET /executive/priorities      ranked priorities
GET /executive/recommendations ranked recommendations
GET /executive/kpis            KPI intelligence (health + per-KPI cards)
GET /executive/decisions       enhanced, ranked decisions
GET /executive/risks           top risks, banks/products at risk, merchant follow-ups
GET /executive/patterns        recurring-signal memory
```

## Success criteria — all answered by reasoning

Every question in the milestone is answered by the Copilot, grounded, no
hallucination:

- *What happened this week?* → the Sev-2 Autopay incident, 98.29% → 99.38% recovery.
- *What should I prioritize Monday morning?* → monitor ICICI recovery, review the failover decision, adopt failover rail-wide.
- *What recommendations do you have?* → bank-failover, maintenance-window awareness, resilience KPI.
- *Which decision had the biggest impact?* → DEC-2026-0713-01 (business impact 90, customer 92).
- *Should we continue the rollout?* → yes — recovery verified to 99.38%.
- *What alternatives did we have?* → the three considered, with the selected one.
- *Which products / banks / merchants need attention?* → UPI Autopay; ICICI Bank; FlixStream, EduPrime, PowerPay Utilities, InsureWell.
- *What are the top operational risks?* → single-sponsor-bank concentration on ICICI.
- *Which KPI should I monitor tomorrow?* → Autopay Registrations (health 37, worsening).

## Configuration & compatibility

- `EDIP_ENTERPRISE_DATA_DIR` overrides the corpus location (default:
  `enterprise_data/` at the repo root).
- No existing API changed or was removed; no Brain, generator, or corpus
  change. The full backend test suite stays green.

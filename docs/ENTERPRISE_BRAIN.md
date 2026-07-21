# Enterprise Brain — Demonstration (V2.3)

V2.3 does not add architecture. Every layer it exercises — the Enterprise Brain,
the Document Intelligence pipeline, the organizational model, the knowledge
graph, the autonomous scheduler, the copilot, and the Outlook/Teams adapters —
already existed. V2.3 makes the Brain **come alive** on a realistic,
cross-referencing synthetic organization and proves it can answer questions that
span documents, meetings, emails, Excel, RCAs, SOPs, Teams, and reports rather
than retrieving a single file.

## What it demonstrates

1. A **synthetic enterprise** — ~6 months of a fintech payments company's
   activity: SOPs, RCAs, policies, meeting notes, decision logs, action items,
   product docs, BRDs, roadmaps, executive/weekly/monthly/merchant/risk reports,
   email threads, Teams conversations, and Excel KPI workbooks — every document
   naturally referencing the others.
2. The **Enterprise Brain ingesting** that corpus on its ordinary heartbeat:
   parse → chunk → embed → observe entities → link → build context.
3. **Cross-source Q&A** — one question pulls passages from an RCA, the incident
   meeting, a Teams thread, the KPI numbers, the decision log, and the SOP, and
   the answer cites each source it stood on.
4. An **autonomous daily cycle** that ingests new documents/emails/Teams,
   briefs the executive, decides on recommendations, and queues email and Teams
   drafts for approval — every simulated day, with no manual step.
5. An **executive workspace** that shows the morning brief, what completed
   overnight, pending approvals, recent decisions, and an Ask-the-Brain bar —
   review-and-approve only, no manual report generation or uploads.

## Running the demo

From `backend/` (the same environment as the tests):

```bash
python scripts/bootstrap_enterprise_demo.py
```

This one command:

1. generates the corpus under `sample_data/enterprise/` (deterministic, seed 42);
2. registers each folder as a document source (auth-free, local);
3. forces one synchronization so the whole pipeline runs immediately instead of
   waiting for the 15-minute heartbeat.

Everything is persisted to disk (sync store, document store, vector collections,
organizational model, knowledge graph), so a backend started afterwards loads a
Brain that already knows the whole organization. Re-running is safe — sources
are skipped if already registered and documents re-sync by content hash.

Then start the platform and ask the Brain (Home page, or `POST
/api/v1/copilot/chat`):

> *"Why did settlement success dip in March and what did we do about it?"*

The answer combines the RCA, the incident-bridge meeting, the KPI workbook, the
decision log, the SOP, and the BRD — a genuinely cross-source answer.

## The corpus

`scripts/generate_enterprise_corpus.py` writes parser-supported files (`.md`,
`.xlsx`) into a folder tree whose sub-folders map onto the platform's existing
document source kinds:

| Folder | Source kind | Entity kind | Contents |
|--------|-------------|-------------|----------|
| `sops/` | `sop_repository` | `sop` | Standard operating procedures |
| `rcas/` | `rca_repository` | `rca` | Root-cause analyses |
| `policies/` | `policy_repository` | `policy` | Enterprise policies |
| `meetings/` | `meeting_notes` | `meeting` | Meeting notes, decision logs, action items, **email threads, Teams conversations** |
| `product/` | `product_documents` | `document` | Product one-pagers, BRDs, roadmaps |
| `reports/` | `document_folder` | `document` | Executive, weekly, monthly, merchant, risk reports |
| `kpis/` | `document_folder` | `document` | KPI & merchant Excel workbooks |

**Emails and Teams as documents.** Reading a live Microsoft 365 account requires
a Graph credential (see below). For the credential-free demo, synthetic email
threads and Teams conversations are written as markdown under `meetings/` with
clear `From:/To:/Channel:` headers, so they parse, chunk, embed, and become
searchable `meeting` entities — the Brain answers over "emails" and "Teams"
exactly as it does over any other document.

**Connectedness is the point.** A single narrative spine runs through the whole
corpus: a March settlement success-rate dip (98.7% → 94.2%). The RCA cites the
SOP it exposed, the incident bridge meeting, the KPI that fell, the decision
taken, and the BRD that fixed it; the meeting notes, Teams thread, email
escalation, weekly report, and monthly executive report all reference the same
event by name. Those natural-language cross-references are what the chunk
embeddings stitch back together at question time.

## How ingestion reaches the Brain

The demo uses the platform's ordinary pipeline end to end — nothing bespoke:

```
folder source (registered)
  → SynchronizationEngine.sync      (catalog scan, per-file content hash → delta)
  → DocumentIntelligence.process_sync
        parse (.md/.xlsx/…) → chunk → embed into the "_documents" collection
        → observe each file as an entity (sop/rca/policy/meeting/document)
  → OrganizationalModel               (entities mirrored into the knowledge graph)
  → RelationshipEngine                (cross-entity links)
  → EnterpriseContextBuilder          (unified context rebuilt)
```

Drop a new file into a registered folder and the next `knowledge_refresh` tick
(≤15 min) picks it up by content-hash diff — no re-upload, no re-index.

## Cross-source Q&A

The copilot already gathers **evidence before the model reasons**; V2.3 makes
document passages part of that evidence:

- **`EnterpriseSearch` gains a `documents` surface** (`app/sync/search.py`) that
  searches the `_documents` chunk collection, so SOPs/RCAs/meetings/reports are
  reachable from `/api/v1/search` and from copilot evidence at once.
- **The evidence collector gains a `document_chunks` collector**
  (`app/copilot/evidence.py`) that adds each retrieved passage as citable
  evidence, keyed by its document id. (It also fixes a latent bug where the
  stored search engine shadowed the enterprise-search collector, so
  enterprise-search evidence silently never arrived.)
- **The knowledge-seeking routes** — `question`, `analysis`, `explanation`,
  `report` — now compose `document_chunks` + `search_results` with KPIs,
  knowledge, and relationships (`app/copilot/planner.py`), so an ordinary
  executive question is answered across sources by default.
- **The validator counts numbers inside a retrieved passage as sourced**
  (`Evidence.numbers()`): a figure written in a document chunk the model was
  shown is evidence, not an invention.

The honesty contract is unchanged: with no LLM provider the answer degrades to
the cited evidence list rather than fabricating a narrative, and any figure the
model cannot source is still rejected.

## Autonomous daily cycle

The `daily_cycle` chain (`app/workflows/autonomous.py`) now begins by ingesting
the day's new sources, then runs unchanged:

```
process_new_sources → refresh_portfolio → analyse_new_data → update_brain
  → generate_daily_brief → create_tasks → generate_recommendations
  → queue_communications
```

- **`process_new_sources`** triggers the sync refresh and reports how many new
  documents/emails/Teams messages were ingested (announced as `SourcesProcessed`
  on the event bus), so the brief and recommendations that follow are computed
  over today's corpus.
- **`queue_communications`** drafts the brief as **both** an email (to the
  executive) and a Teams announcement (to the team) every cycle. Both are
  drafts: they wait in the Action Queue and are sent only on human approval.

## Outlook & Teams (read)

The V2 adapters were outbound-only (draft/send/post). V2.3 adds **read**, using
the existing `GraphClient` — additive methods, outbound unchanged and still
approval-gated:

- `OutlookEmailAdapter.read_messages` / `search_messages` / `get_message`
- `TeamsMessagingAdapter.read_channels` / `read_messages`

Exposed read-only at `/api/v1/manager/outlook/*` and `/api/v1/manager/teams/*`.
They activate when `EDIP_MS_GRAPH_AUTH` is set (a bearer token, or
`tenant:client_id:client_secret`); with no credential they report a clear
`unavailable` reason and the platform behaves exactly as before. Credentials are
resolved from the environment at call time and never stored. The live demo runs
on the synthetic email/Teams corpus; connect a real account by setting the
credential and registering an `outlook`/`teams` source.

## Executive workspace

`Home` (`frontend/src/pages/Home.jsx`) is the manager's front door: a greeting,
the **Ask Enterprise Brain** bar, **Today's Executive Brief** (composed
overnight), **Completed Overnight** (workflows, reports, drafts awaiting
approval), **Pending Approvals** (with Approve/Reject), **Recent Decisions**, and
the day's tasks, alerts, reports, and opportunities. There is no manual
report-generation or upload control — the executive reviews and approves; the
agent does the operational work.

## Files

- **New:** `backend/scripts/generate_enterprise_corpus.py`,
  `backend/scripts/bootstrap_enterprise_demo.py`, this document.
- **Changed:** `app/sync/search.py` (documents surface),
  `app/copilot/evidence.py` (document_chunks + shadow fix + sourced numbers),
  `app/copilot/planner.py` (cross-source routes),
  `app/communication/adapters.py` (Outlook/Teams read),
  `app/api/v1/manager.py` (read endpoints),
  `app/workflows/autonomous.py` (process_new_sources + Teams draft),
  `app/runtime/events.py` (`SourcesProcessed`),
  `frontend/src/pages/Home.jsx` (brief / overnight / decisions sections).

# 04 · Knowledge Graph & Vector Retrieval

Two complementary memories: the **knowledge graph** answers *structural*
questions ("which merchants belong to the acquirer whose settlement volume
fell?"), the **vector store** answers *similarity* questions ("have we seen a
pattern like this before?"). Both are retrieval surfaces for agents — neither
generates narrative — and both write findings into the Evidence Ledger when
they surface something citable.

## 1. Enterprise Knowledge Graph

### 1.1 Storage architecture

`GraphStore` interface with two adapters (chosen by config, ADR-006):

- **Kùzu (default)** — embedded, columnar, Cypher. Zero operational cost,
  fits the lite profile, fast analytical graph queries.
- **Neo4j (enterprise option)** — for organizations that mandate a server
  graph DB, need Bloom-style exploration, or multi-app graph sharing.

NetworkX is retained *only* as an in-memory algorithm library (centrality,
community detection) executed over subgraph exports — not as the store.

### 1.2 Schema (typed property graph)

```
 (:Customer)-[:USES]->(:Product)
 (:Customer)-[:TRANSACTS_WITH]->(:Merchant)
 (:Merchant)-[:BELONGS_TO]->(:Category)
 (:Merchant)-[:CONNECTED_TO]->(:PSP)
 (:Merchant)-[:LOCATED_IN]->(:Region)          // ontology addition: geography
 (:PSP)-[:SUPPORTS]->(:Product)
 (:Bank)-[:OWNS]->(:Issuer)  (:Bank)-[:OWNS]->(:Acquirer)
 (:Transaction)-[:ISSUED_BY]->(:Issuer)
 (:Transaction)-[:ACQUIRED_BY]->(:Acquirer)
 (:Transaction)-[:FAILED_AT]->(:PSP|:Acquirer)  // failure attribution
 (:Transaction)-[:OF_PRODUCT]->(:Product)
 (:KPI)-[:MEASURES]->(entity)                   // analytical overlay
 (:Signal)-[:OBSERVED_ON]->(:KPI)
 (:Evidence)-[:DERIVED_FROM]->(node)            // ledger cross-links
```

Node/edge properties carry provenance (`source_dataset`, `run_id`,
`confidence`) so graph facts are as auditable as tabular ones. Transactions
are stored **aggregated** (per merchant × product × period) above a volume
threshold — the raw rows stay in DuckDB; the graph holds structure, not bulk.

### 1.3 Construction

The Graph Build node (deterministic) upserts per run:
entities from profile/semantic output → nodes; detected relationships +
FK-resolved transaction links → edges; KPI/Signal overlay from the quant
engine. Idempotent by natural keys; superseded edges are closed with
`valid_to` (bitemporal-lite) so "the graph as of last month's report" remains
reconstructible.

### 1.4 Reasoning support (what "the graph supports reasoning" means concretely)

Exposed via the `graph_query` tool (used chiefly by Root Cause and Copilot):

| Operation | Question it answers | Output |
|---|---|---|
| k-hop neighborhood | "what surrounds this declining merchant?" | subgraph → context |
| path finding | "how is the KPI drop connected to PSP X?" | paths → `graph_finding` evidence |
| centrality / concentration | "which acquirer is a single point of failure?" | ranked nodes → evidence |
| community detection | "do failing merchants cluster by category/PSP?" | clusters → evidence |
| motif checks | "customers whose transactions failed at the same PSP ≥3× this month" | matches → evidence |
| GraphRAG retrieval | serialize the relevant subgraph as structured context for Root Cause | text+ids, citable |

Every reasoning output that reaches an agent is first written as
`graph_finding` evidence — so a root-cause hypothesis citing a graph path
cites a **ledger id**, and the Verifier can check it like any KPI.

## 2. Vector Database

### 2.1 Storage architecture

`VectorStore` interface → **Qdrant** (default; snapshots, payload filtering,
hybrid search) or **pgvector** (lite profile, one less container). The
existing embedder abstraction is kept; default model upgraded to a
multilingual sentence-transformer (bge-m3 class), pluggable per deployment.

**Isolation is structural**: every point carries `{org_id, project_id}`
payload and every query filters on them — cross-project leakage is impossible
at the query layer, and project deletion is a filtered point-delete plus
collection compaction.

### 2.2 Collections

| Collection | Content | Serves |
|---|---|---|
| `reports` | past report sections (chunked, with statement ids) | copilot RAG, "what changed since last quarter", precedent recall |
| `insights` | historical verified statements + their evidence ids | Root Cause precedent search ("this pattern seen before") |
| `glossary` | business terms, aliases, rules from the knowledge store | semantic mapping boost, copilot grounding in org language |
| `docs` | product documentation, uploaded PDFs/Word | copilot RAG |
| `entities` | merchant/product descriptions + learned entity embeddings (03 §7) | semantic similarity, dedup, cold-start mapping |
| `schemas` | column/dataset signatures | clarification reuse, cross-project schema matching |

### 2.3 RAG contract (retrieval is evidence too)

Retrieval results injected into any prompt are first registered as
`retrieval` evidence (source id, chunk hash, score). The agent cites those
ids; the Verifier resolves them. **RAG therefore cannot smuggle unverifiable
context into narration** — retrieved-but-uncited text never upgrades a
statement's verification status. This closes the classic RAG loophole where
"grounded" means "something vaguely similar was in the prompt."

### 2.4 Retrieval pipeline (copilot & root cause)

```
query → embed → Qdrant (filtered: org, project, collection routing)
      → rerank (cross-encoder, optional full profile)
      → register retrieval evidence
      → context assembly (token-budgeted, id-tagged chunks)
      → agent → statements with citations → Verifier
```

## 3. Deletion semantics (project delete, extended from v2)

`DELETE /projects/{id}` must remove, atomically per store, with an audit
record:

| Store | Action |
|---|---|
| Object storage | uploads, Parquet snapshots, artifacts, cached model binaries prefix-deleted |
| DuckDB | project database file removed |
| Control plane | runs, events, statements, citations, evidence index rows (cascade) |
| Qdrant | filtered point delete on `project_id` across all collections |
| Graph store | project-scoped subgraph delete (provenance property) |
| MLflow | project experiments archived; project-scoped models deleted |
| Temp/cache | Redis keys by prefix, feature materializations |

**Preserved**: enterprise knowledge (terms, rules, answered clarifications
keyed by schema signature) and enterprise-published models — organizational
learning survives project lifecycle, exactly as in v2.

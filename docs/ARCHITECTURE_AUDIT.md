# Enterprise Product Intelligence Platform — Architecture Audit & Rebuild Roadmap
*Principal-architect review. Phase 1 deliverable: audit + dependency graph + sequenced plan.*

## 0. The honest framing (read this first)

This is **~54,000 lines of code** (backend ~44,300 LOC / 38 Python packages;
frontend 53 pages + 11 components / ~9,700 JSX LOC) with real layered
intelligence already in place. A single-pass "rebuild everything" is neither
achievable nor safe — and a big-bang rewrite of a working 54K-LOC system is the
one thing a principal architect should *not* recommend. The professional path is
a **strangler-pattern refactor**: keep the platform running, replace weak modules
behind stable interfaces, validate each increment against real runtime data.

Your brief also contains a real tension: *"do not preserve poor implementations"*
(this prompt) vs. *"do not break existing / preserve APIs"* (the previous Phase-2
brief). The resolution is the strangler pattern — which this codebase already uses
(`EDIP_ORCHESTRATOR=langgraph|legacy` in `core/container.py`). We extend that
discipline, we don't abandon it.

**What is already strong** (verified by reading, this session and prior):
- KPI discovery already emits Formula + Source + period basis + `comparison_unavailable_reason`; single-period fabrication is already guarded (`intelligence/kpi/discovery.py`).
- Forecasting already gates on variance, `MIN_HISTORY=12`, and <4-point series (`intelligence/forecasting/engine.py`).
- The report prompt already forbids invented comparisons/causes (`prompts/domains/reports.py`).
- Evidence collection is budgeted per kind; the copilot has intent → plan → context → evidence → prompt → validate → actions (`copilot/`).
- A knowledge graph, evidence collector, response validator, and multi-provider LLM abstraction already exist.

**What is genuinely weak or wrong** (the real targets — see §3):
1. **Dataset is future-dated** (starts 2026-06-22, runs 180 days into Dec 2026). Your brief forbids future data; today is 2026-07-29. *Correctness bug, highest priority.*
2. **RAG is embedding-similarity + keyword search only** — no BM25/hybrid, no cross-encoder rerank, no HyDE, no GraphRAG, no CRAG/self-reflection.
3. **NPCI product model is UPI-sub-features only** — missing the real portfolio (RuPay, IMPS, NACH, AePS, Bharat Connect/BBPS, NETC FASTag, UPI 123Pay, etc.).
4. **Config loading was broken** (root `.env` ignored from `backend/` cwd) — fixed this session; symptomatic of config/observability debt.
5. **LLM latency** on local CPU (qwen3:14b @ 3.1 tok/s) — mitigated this session (prompt budgeting −57%, model switch to gemma4:e4b ~25 tok/s, client timeout).

---

## 1. Backend dependency graph (measured, not asserted)

Cross-package dependents (how many modules import each package):

```
core          ██████████████████████████ 124   ← foundation hub (config, container, logging, DI)
domain         ██████ 31                        ← shared models/DTOs
intelligence   ███ 17                           ← KPI, forecasting, profiling, relationships, embeddings, graph
knowledge      ██ 14                            ← knowledge store
repositories   ██ 10
communication  █ 8      agents 7   memory 7     tools 6   reports 5
sync 4  ml 4  evidence 4  documents 4  workflows 4  llm 3  manager 3 runtime 3 analyst 3
executive 1  workspace 1  ml_models 1  governance 1  observability 1
```

Layering (clean, mostly acyclic):

```
                    ┌─────────────── api/ (routers, 3.5K LOC) ───────────────┐
                    │        copilot   executive   workspace   product        │
   orchestration ───┤        manager   runtime     reports     communication  │
                    │           │          │           │            │         │
   intelligence ────┼── kpi  forecasting  profiling  relationships  graph  embeddings
   knowledge/RAG ───┤   documents(chunk/parse/store)   evidence   agents/prompts
   data plane ──────┤   connectors   sync   repositories   db   ml / ml_models
   foundation ──────┴── core (config, container DI, logging)   domain (models)
```

Largest packages by LOC: `runtime` 3.9K · `intelligence` 3.9K · `api` 3.5K ·
`product` 3.4K · `sync` 3.0K · `connectors` 2.8K · `copilot` 2.7K · `executive` 2.2K.

Observations:
- **`core` is a healthy hub** (DI container composes everything) — good.
- **`runtime` + `product` + `sync` are heavy** and overlap with `executive`/`manager` in responsibility — candidate consolidation, not rebuild.
- No obvious cyclic package dependencies surfaced; the DI container is the single composition root.

---

## 2. Module-by-module scorecard

Legend: 🟢 solid · 🟡 adequate, needs upgrade · 🔴 weak/gap vs. your brief.

| Area | Module(s) | Score | Note |
|---|---|---|---|
| Config / DI | `core` | 🟡 | Container DI good; `.env` loading was broken (fixed). Needs a settings audit — many `EDIP_*` were silently defaulting. |
| Dataset generator | `generate_enterprise.py` | 🔴 | **Future-dated**; rich patterns exist but violate "never future"; timeline must be Jan 2026→today. |
| Documents | `documents/`, generator emitters | 🟡 | Chunk/parse/store solid; generated docs are structured but short (Phase-3 asks multi-page). |
| Knowledge graph | `intelligence/graph`, `knowledge` | 🟡 | Exists; entity/relationship coverage is partial vs. Phase-4 entity list. |
| RAG retrieval | `intelligence/embeddings`, `documents/store`, `workspace/search`, `copilot/evidence` | 🔴 | Dense-ish + keyword only. No BM25/hybrid, rerank, HyDE, GraphRAG, CRAG. **Biggest Phase-5 gap.** |
| Context engine | `copilot/context`, `agents/prompt_generator` | 🟡 | Context builder + prompt budgeting (added) good; not yet a full "context package" (contradictions, missing-info, definitions) per Phase-6. |
| LLM layer | `llm/`, `copilot/router` | 🟢 | Multi-provider + fallback + budgeting + observability (added). Solid. |
| Forecasting | `intelligence/forecasting` | 🟡 | Ridge + seasonality/variance/history gates. No changepoint detection, no driver attribution (Phase-7). |
| Business reasoning | `executive`, `analyst/insights`, `copilot` | 🟡 | Insight engine with evidence/confidence exists; RCA/opportunity/next-areas partially covered. |
| NPCI products | `generate_enterprise.py` PRODUCTS | 🔴 | UPI-only sub-features; not the real NPCI portfolio (Phase-9). |
| Reports | `reports/generator`, `prompts/domains/reports` | 🟡 | Evidence-grounded, anti-fabrication; structure is good but not McKinsey-depth (Phase-11). |
| Dashboards/UI | `frontend/src/pages/*` (53) | 🟡 | Functional, themed, 8-item nav; not yet Power-BI/Foundry-grade drill-down/cross-filter (Phase-10). |
| Validation | `copilot/validator`, `evidence` | 🟢 | Response validator + confidence gate + citations exist. |

**Dead code / duplication / fake data — findings so far** (needs one focused pass to be exhaustive):
- Responsibility overlap: `executive` vs `manager` vs `product` vs `runtime/intelligence` all compute executive-ish views. Consolidation candidate.
- Legacy vs. langgraph orchestrators both present (intentional strangler flag) — fine, but the legacy path is a cleanup candidate once langgraph is default-proven.
- No fabricated-output generators found in the AI path (the anti-fabrication contracts hold); the "fake data" risk is the **synthetic dataset itself being future-dated**, not fake AI outputs.

---

## 3. The 12 phases → reality map

| Phase | Requested | Reality | Effort |
|---|---|---|---|
| 1 Audit | this doc | ✅ delivered | — |
| 2 Dataset | Jan 2026→today, story-rich, no future | Generator is rich but **future-dated & UPI-only** | **M** (high value, do first) |
| 3 Documents | multi-page, cross-referenced | Structured but short | M |
| 4 Knowledge graph | full entity/rel coverage | Partial exists | M |
| 5 RAG (hybrid/rerank/HyDE/GraphRAG/CRAG) | SOTA techniques | **Only dense+keyword today** | **L** (biggest lift) |
| 6 Context engine | full context package | Partial (budgeted context) | M |
| 7 Forecasting | changepoints/drivers/CI | Gated ridge; no changepoints | M |
| 8 Business reasoning | PM-grade, evidence-cited | Mostly exists | S–M |
| 9 NPCI alignment | real portfolio | **Wrong product model** | S (do with Phase 2) |
| 10 Dashboards | Foundry/Power-BI grade | Functional only | **L** |
| 11 Reports | McKinsey depth | Good, not deep | M |
| 12 Validation | end-to-end coherence | Partial | M |

Effort: S≈days, M≈1–2 weeks, L≈3–6 weeks each, at focused pace. Full program ≈ **3–5 months**.

---

## 4. Recommended execution order (highest leverage first)

Everything downstream (documents → KG → RAG → context → reports → dashboards)
derives from the **dataset**. Fix the source of truth first, then the retrieval
brain, then the surfaces.

1. **Increment 1 — Data foundation (Phase 2 + 9).** Retime the generator to
   **Jan 1 2026 → 2026-07-29 (today)**, never future; align to the **real NPCI
   product portfolio**; keep/extend the story-rich patterns (already good). This
   is concrete, correctness-critical, and unblocks everything. *Recommended start.*
2. **Increment 2 — RAG upgrade (Phase 5 + 6).** Add BM25 + hybrid fusion,
   cross-encoder reranking, and a real context-package builder. Biggest quality lever for the AI.
3. **Increment 3 — Documents + KG (Phase 3 + 4).** Richer multi-page docs and fuller entity/relationship extraction (feeds GraphRAG).
4. **Increment 4 — Forecasting + reasoning (Phase 7 + 8 + 11).** Changepoints, driver attribution, deeper reports.
5. **Increment 5 — Dashboards (Phase 10).** Drill-down/cross-filter surfaces once the intelligence beneath is upgraded.
6. **Increment 6 — Validation & polish (Phase 12).**

Each increment ends with validation against real runtime data (no placeholders,
no future dates, citations present) before the next begins.

---

## 5. Immediate recommendation

Start **Increment 1 (dataset retiming + NPCI portfolio)** — it's the root of the
data lineage, it's a real correctness fix (future-dated data), and it's the
foundation every later phase reads from. I can execute it now and validate end to
end (generate → ingest → reports show Jan–Jul 2026 only, correct products).

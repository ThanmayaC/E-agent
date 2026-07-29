# Enterprise AI Platform — Pipeline Root-Cause Audit

Scope: production-hardening of the existing pipeline. No redesign; architecture
preserved. Every change is additive/targeted.

Pipeline traced: Frontend → Conversation → API → Enterprise Brain → Context
Builder → Evidence/RAG → Prompt Builder → LLM Router → Provider → Report/Response.

---

## 1. The headline bottleneck — measured, not assumed

Ollama was **not** the primary fault; an **unbudgeted prompt** was.

Measured on a realistic copilot request (12 evidence kinds × 10 items):

| Stage | Before | After |
|---|---|---|
| Copilot prompt size | **41,564 chars ≈ 10,391 tokens** | **17,784 chars ≈ 4,446 tokens** (−57%) |
| Evidence serialized | all 120 items, uncapped | budgeted to 12,000 chars, rest dropped + logged |
| Business context | full dict, uncapped | capped to 6,000 chars, largest keys dropped + marked |
| Worst-case hang on failure | `retries=2` × `timeout=180s` = **up to ~9 min**, retrying the *same* oversized prompt | budgeted prompt + client abort at **150 s**, UI always recovers |
| LLM observability | none | prompt chars, ~tokens, `num_predict`, latency, tokens_in/out logged every call + captured on provider |

Root cause: `agents/prompt_generator.py::enterprise_copilot_prompt` did
`json.dumps(evidence)` + `json.dumps(business_context)` with **no size budget**.
That ~10k-token prompt fed to `qwen3:14b` on CPU with `num_predict=4096` reliably
exceeded the 180 s timeout; `base_provider.chat()` then re-sent the **identical
oversized prompt** twice more before raising “failed after 3 attempts: timed
out”. The frontend `fetch` had **no client timeout**, so the UI waited on the
hung request indefinitely → “Assistant is working…” forever.

---

## 2. Root cause of every reported symptom

| # | Symptom | Root cause | Status |
|---|---|---|---|
| 1 | Stuck on “Assistant is working…” | Backend hangs in retry loop (see §1) **and** frontend `fetch` had no timeout, so `finally { setBusy(false) }` never ran. | **Fixed** |
| 2 | “ollama failed after 3 attempts: timed out” | Oversized prompt + heavy model + `num_predict=4096` exceed `timeout_s`; retries re-send the same oversized prompt. | **Fixed** (prompt budgeted; observability added). Config tuning recommended (§5). |
| 3 | Invalid comparisons / forecasts / health on a single dataset | Investigated: the **deterministic layer already guards this correctly** — `intelligence/kpi/discovery.py::_apply_series` sets `comparison_unavailable_reason` and leaves `previous_value`/`growth_pct` unset when `<2` complete periods; `forecasting/engine.py` requires ≥4 points (`MIN_HISTORY=12`); the report prompt (`prompts/domains/reports.py`) already forbids inventing comparisons. Residual fabrication was the local model mis-following a 10k-token prompt — directly improved by the budget fix (smaller, clearer prompt). `calculation{}` already carries Formula + Source + Assumptions per KPI. | **Verified sound**; improved indirectly. |
| 4 | Project cards: Invalid Date, 0 files, wrong confidence, duplicate delete dialog, stale values | **Not yet investigated** (frontend project-management path). | **Open** (§5) |
| 5 | UI values not reflecting backend state | Same class as #4; plus the admin blank-page issue fixed in the prior session (`Stat` object-render crash + error boundary). | Partially addressed; §5 |
| 6/7 | Diagnostics | Provider now captures `last_call` (model, prompt_chars, tokens, latency); a dedicated diagnostics **page** is not yet built. | **Backend hook added; page open** (§5) |

---

## 3. Exact files modified

| File | Change |
|---|---|
| `backend/app/agents/prompt_generator.py` | Added `DEFAULT_EVIDENCE_BUDGET_CHARS`/`DEFAULT_CONTEXT_BUDGET_CHARS`, `_budget_evidence()`, `_cap_json()`; `enterprise_copilot_prompt` now budgets evidence + business context before serialization and **logs** kept/dropped counts, context size, prompt size & est. tokens. |
| `backend/app/llm/ollama_provider.py` | `_chat_once` now times the call, logs prompt size + `num_predict` + latency + token counts, and records `self.last_call{}` for diagnostics. |
| `backend/app/llm/base_provider.py` | Added `self.last_call`; `chat()` retry loop logs per-attempt latency + prompt size and includes prompt size in the final error. |
| `frontend/src/api/client.js` | `request()` now uses `AbortController` with a default 60 s timeout (configurable per call); returns a clear “Request timed out” error so callers’ `catch/finally` always run. `copilotChat` uses a 150 s ceiling. |
| `frontend/src/pages/AIAssistant.jsx` | Replaced the static “Assistant is working…” with a staged `WorkingIndicator` (Initializing → Building context → Retrieving evidence → Calling AI → Generating report) + elapsed timer. Existing `try/catch/finally` already cleared `busy` on success/failure — now the timeout guarantees it on hangs too. |

Prior session (context): `frontend/src/pages/admin/AdminOverview.jsx`,
`frontend/src/components/ui.jsx` (`Stat` guard), `frontend/src/components/ErrorBoundary.jsx`
(+ wired into both layouts) — fixed the whole-app blank on `/admin`.

---

## 4. Before vs After (behavioural)

- **Prompt**: 10,391 → 4,446 tokens (−57%); evidence now budgeted, over-budget
  context dropped and marked (`_omitted_for_budget`) instead of sent whole.
- **Failure mode**: an unreachable/slow model now surfaces within 150 s at the
  UI (clear timeout message) instead of an indefinite spinner; server logs show
  exactly where time went (prompt size, per-attempt latency, model latency).
- **Observability**: every LLM call logs `model / prompt chars / ~tokens /
  num_predict / latency / tokens_in / tokens_out`; the prompt builder logs
  evidence kept-vs-dropped and final prompt size.
- **Single-dataset reports**: confirmed the deterministic guards hold; KPIs
  already expose Formula/Source/period basis/unavailable-reason.

---

## 5. Remaining improvements (prioritized)

1. **Config tuning (fast win, no code):** set a lighter default model and smaller
   generation budget for local runs, e.g. `EDIP_LLM_MODEL=qwen2.5:7b-instruct`
   (or `qwen3:4b`), `EDIP_LLM_MAX_TOKENS=1536`, `EDIP_LLM_TIMEOUT_S=90`,
   `EDIP_LLM_RETRIES=1`. The copilot answer JSON does not need 4096 output tokens;
   this alone roughly halves generation time on CPU.
2. **Runtime Diagnostics page (item #7):** add `GET /copilot/diagnostics`
   returning `router.describe()` + `provider.last_call` + brain/RAG status + jobs
   + queue size, and a `/admin/diagnostics`-style panel. The provider hook
   (`last_call`) is already in place to feed it.
3. **Project Management metadata (item #6):** trace `GET /projects` → the project
   card component; fix Invalid Date (missing/ISO-mismatched `created_at`), 0 files
   (file count not populated on the list payload), confidence source, and the
   duplicate delete dialog (likely a double-mounted modal / unguarded click).
4. **True streaming stages (optional):** the staged indicator is time-based. For
   real per-stage progress, stream stage events from `/copilot/chat` (SSE) — a
   larger change, deferred deliberately per “no unnecessary features”.
5. **Context-budget from settings:** wire `enterprise_copilot_prompt`’s budgets
   to a `settings.llm_max_prompt_chars` so ops can tune without code.

---

## 6. Not started (separate deliverable)

**LoRA/QLoRA fine-tuning project** for the local Ollama Qwen model (dataset
generation + training scripts + configs). This is a self-contained project, not a
change to the running platform, and is best delivered on its own so it gets full
attention. Recommended next session.

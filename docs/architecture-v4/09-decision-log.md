# 09 — Architecture Decision Log

Each ADR records a decision, its context, the alternatives weighed, and its consequences.
These are the justifications behind the v4 architecture.

---

### ADR-001 — Reuse the Python backend as an embedded sidecar (do not rewrite)

**Decision.** Ship the existing `backend/` (FastAPI + ~38k lines of tested intelligence)
unchanged as a local **Core sidecar**, rather than porting the Brain/Graph/Memory/Decision
logic to a desktop-native language.

**Alternatives.** (a) Rewrite in C#/.NET for a first-class Windows app. (b) Rewrite in
Rust inside the shell. (c) Embed Python.

**Why (c).** The intelligence is the crown jewel and is already correct, evidence-verified,
and covered by 572+ tests. A rewrite would risk regressions and cost quarters for no user
benefit. The config is already env-driven with a lite profile that runs serverless — it
*wants* to be embedded. **Consequence:** we bundle a Python runtime (PyInstaller), accept a
larger installer and a process boundary, and gain a shippable product in a fraction of the
time with the intelligence preserved.

---

### ADR-002 — Tauri (not Electron) for the desktop shell

**Decision.** Use Tauri 2 (Rust + system WebView2).

**Alternatives.** Electron (bundled Chromium); .NET MAUI/WPF WebView; native Win UI.

**Why Tauri.** ~10 MB shell vs Electron's ~150 MB Chromium; uses the WebView2 already
present on Windows 11; native, audited secrets/updater/IPC; smaller attack surface for a
security-sensitive enterprise app; first-class sidecar supervision. **Consequence:** we
depend on WebView2 runtime (evergreen, standard on Win 11; bootstrappable on 10) and write
a small amount of Rust for shell/secrets/updater.

---

### ADR-003 — Reuse the existing React frontend, restyled as a workspace

**Decision.** Keep `frontend/` and its component library; add a `shell/` (tabs, dock,
command palette) and `workspace/` (role dashboards, approval center) rather than building a
new UI.

**Why.** The premium component set, pages, charts, and API client already exist and are
polished. **Consequence:** the web UI remains buildable (useful as a debug/admin surface);
desktop-specific chrome is additive.

---

### ADR-004 — MSAL delegated OAuth; never handle passwords

**Decision.** Each user signs in with MSAL delegated OAuth via the Windows broker; the app
acts as the user.

**Alternatives.** Application permissions (app-only) with a central service principal;
storing user credentials.

**Why delegated.** It caps blast radius to what the user can already access, needs no
central service, supports SSO/MFA/conditional access, and never touches a password (a hard
product rule). **Consequence:** IT does a one-time app registration + admin consent;
features requiring broad app-only access are out of scope for v1.

---

### ADR-005 — Secrets in Windows Credential Manager + DPAPI at rest

**Decision.** Tokens and API keys live in Credential Manager; local data stores are
DPAPI-encrypted (SQLCipher optional under fleet policy).

**Why.** OS-native, per-user, hardware-tied protection with no custom crypto to get wrong;
matches least-privilege and "no secrets in files/logs." **Consequence:** secrets are
bound to the Windows user profile (correct for a per-user app); cross-machine roaming of
secrets is intentionally not supported.

---

### ADR-006 — LangGraph for plans and human-in-the-loop

**Decision.** Build the Task Planner and multi-step workflows on LangGraph (already
integrated, `orchestrator=langgraph`), using checkpointing and `interrupt()` for approvals.

**Why.** Checkpointed graphs give free crash-resume; `interrupt()` is exactly HITL; the
codebase already runs it with an imperative fallback for the lite profile.
**Consequence:** LangGraph is a dependency in the full profile; the imperative fallback
keeps the app working if it's absent.

---

### ADR-007 — Ship with least-privilege default role (`viewer`), not `administrator`

**Decision.** The employee build defaults `governance_default_role` to `viewer`; roles are
assigned via wizard/Entra claims.

**Why.** The dev default (`administrator`, every gate open) is unsafe for distribution.
**Consequence:** shipped builds are locked-down by default; the open dev behaviour remains
available in development configs.

---

### ADR-008 — File-backed graph & vector stores per laptop; servers optional

**Decision.** Default to NetworkX file graph + file/sqlite vector store; Neo4j/pgvector are
opt-in for the fleet profile.

**Why.** One user's business-entity graph and embeddings don't justify a graph/vector
server on a laptop; the file stores already exist and are disk-durable.
**Consequence:** single-user scale is the design point; fleet-scale shared knowledge uses
the optional central profile (ADR-009).

---

### ADR-009 — One Core, two deployment profiles (lite / fleet) by config only

**Decision.** The same Core runs per-laptop (SQLite/file/local-LLM) or against shared
infra (Postgres/pgvector/Neo4j/OTLP) purely via `EDIP_*` config — no code fork.

**Why.** Preserves the entire v3 web architecture as the opt-in fleet profile while
meeting the v1 "no central dependency" requirement. **Consequence:** we maintain one
codebase and test both profiles; the fleet profile is a supported deployment, not a
separate product.

---

### ADR-010 — Synthetic Enterprise Generator moves to `tools/demo/` (not shipped)

**Decision.** `generate_enterprise.py` + `app/executive` reading `enterprise_data/` become
a developer/QA/sales-demo package, excluded from the employee build.

**Why.** Employees run on their *real* M365 data; synthetic data would confuse the product.
It remains invaluable for testing, evals, and demos. **Consequence:** the executive-
intelligence *reasoning* stays in the product; only the synthetic *data source* is
dev-only. Tests that depend on the corpus run in CI, not on user machines.

---

### ADR-011 — Signed MSIX + Tauri delta updates, managed via Intune/SCCM

**Decision.** Distribute as a signed MSIX; auto-update via signed Tauri deltas; IT manages
rollout/pinning.

**Why.** MSIX is the modern, per-user, IT-manageable Windows packaging; signing satisfies
SmartScreen/AV and Intune validation; delta updates keep bandwidth low across a large
fleet. **Consequence:** an EV code-signing cert and an update-manifest host are
prerequisites for GA.

---

### ADR-012 — The Action Engine is the sole writer; every side-effect is journaled

**Decision.** No engine writes to Outlook/Office/files except the Action Engine, and every
write captures a pre-image, verifies a post-condition, and is journaled for rollback.

**Why.** This is the safety foundation for installing automation on thousands of laptops
(P1/P2); it turns "the AI did something wrong" from data loss into a logged, reversible
event. **Consequence:** all write paths funnel through one typed, deliberately small
component — more indirection, vastly more safety and auditability.

---

### ADR-013 — Additive layering with `EDIP_*_ENABLED` flags (continue the codebase's discipline)

**Decision.** Every v4 subsystem is added around the existing ones, gated by a flag, with
v3.1 as the always-reachable fallback and regression baseline.

**Why.** It is how V2.1–V3.1 were shipped safely; it keeps the platform releasable and
reversible at every phase. **Consequence:** slightly more configuration surface, bought
back by continuous shippability and a clean rollback story.

---

### ADR-014 — On-device AI by default; cloud is explicit opt-in

**Decision.** Default AI provider is local (Ollama); cloud/enterprise providers require
explicit configuration and a pre-egress redaction pass; machine policy can forbid cloud.

**Why.** Privacy, offline capability, and data-residency by default for enterprise data on
personal-adjacent laptops (P4). **Consequence:** planning quality on weak hardware is
bounded by the local model; the provider abstraction + fallback chain mitigate this where
policy permits.

---

Back to the [README reading map](README.md).

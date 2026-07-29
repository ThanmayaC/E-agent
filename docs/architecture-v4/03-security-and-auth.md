# 03 — Authentication & Security Architecture

> Deliverables covered: **#11** authentication flow · **#17** security architecture.

Security is not a layer bolted on top; it is the reason the reason/act split (P1),
per-action journaling (P2), and least-privilege discovery (P4) exist. This document
covers the identity flow and the end-to-end security model.

---

## 1. Authentication model

- **Delegated OAuth 2.0 with PKCE via MSAL** (Microsoft Authentication Library for
  Python). Each employee signs into **their own** Microsoft account. The app acts *as the
  user*, so it can only ever see what that user is already permitted to see — a hard
  ceiling on blast radius (ADR-004).
- **No passwords, ever.** The app never renders a Microsoft password field and never
  stores one. Sign-in happens in the system browser / WebView broker (WAM — Web Account
  Manager on Windows), which supports SSO and conditional access.
- **Token storage:** access/refresh tokens live in the **MSAL token cache persisted to
  Windows Credential Manager** (via the OS keystore, per-user, hardware-protected). No
  tokens in files or logs. Silent refresh uses the refresh token; interactive re-auth is
  only triggered on expiry or scope change.
- **Least scope:** only the delegated Graph scopes the enabled connectors require, e.g.
  `Mail.Read`, `Mail.Send`, `Calendars.ReadWrite`, `Chat.Read`, `ChannelMessage.Read.All`,
  `Files.ReadWrite`, `Sites.Read.All`, `User.Read`. Scopes are requested **incrementally**
  — a scope is only requested when a feature that needs it is first used, and the user
  sees exactly what they consent to.

## 2. Authentication flow (deliverable #11)

```mermaid
sequenceDiagram
    autonumber
    participant U as User
    participant UI as Workspace UI
    participant Shell as Rust Shell
    participant Core as Core / identity
    participant WAM as Windows Broker (WAM)
    participant AAD as Microsoft Entra ID
    participant KS as Credential Manager

    U->>UI: Sign in
    UI->>Core: POST /identity/login
    Core->>WAM: acquire_token_interactive(scopes, PKCE)
    WAM->>AAD: authorize (SSO / MFA / conditional access)
    AAD-->>WAM: auth code
    WAM->>AAD: redeem code (PKCE verifier)
    AAD-->>WAM: access + refresh token, id_token
    WAM-->>Core: tokens + account
    Core->>KS: persist MSAL cache (encrypted)
    Core-->>UI: signed-in (name, roles, tenant) — no token leaves Core
    Note over Core: later, silently
    Core->>KS: load cache
    Core->>WAM: acquire_token_silent(scopes)
    WAM-->>Core: fresh access token (refresh if needed)
    Core->>AAD: Graph call with Bearer token
```

Key properties: the **access token never reaches the UI or the WebView** — it stays in
the Core process, which is the only component that calls Graph. The UI holds only the
local per-launch bearer token for talking to the Core. Sign-out clears the MSAL cache
from Credential Manager and revokes the local session.

### 2.1 Role derivation
After sign-in, roles come from (in order): (1) an explicit role chosen in the wizard, (2)
Entra ID group/`roles` claims if the enterprise maps them, (3) default `viewer`. Roles
drive Role Management (see [06](06-brain-services-and-intelligence.md) §4), which
narrows the tool allow-list and approval policy. This **extends the existing
`GovernanceLayer`**, whose `governance_default_role` and RBAC already exist —
`governance_default_role` moves from `administrator` (the dev default) to `viewer` for
shipped builds (ADR-007).

---

## 3. Security architecture — layered controls (deliverable #17)

```mermaid
flowchart TB
    subgraph Device["On the laptop"]
        subgraph Boundary["Process & network boundary"]
            Shell["Rust Shell\n· signed binary\n· secrets broker"]
            Core["Core sidecar\n· 127.0.0.1 only\n· per-launch bearer token\n· CSP-locked WebView origin"]
        end
        subgraph Identity["Identity & secrets"]
            MSAL["MSAL delegated tokens"]
            KS["Windows Credential Manager"]
            DPAPI["DPAPI at-rest encryption"]
        end
        subgraph Authz["Authorization"]
            Roles["Role Management"]
            Gov["Governance RBAC\n+ connector permissions"]
            Appr["Approval Engine\n(policy gates)"]
        end
        subgraph DataSec["Data protection"]
            Enc["encrypted local stores"]
            Folders["approved-folders allow-list"]
            Audit["immutable audit ledger"]
            Redact["PII redaction before LLM"]
        end
    end
    Boundary --> Identity --> Authz --> DataSec
```

| Control domain | Mechanism |
|----------------|-----------|
| **Least privilege** | Delegated per-user OAuth (can't exceed the user's own rights); incremental scopes; approved-folders allow-list; role tool allow-list |
| **Secret handling** | Passwords never touched (prohibited); tokens/API keys/DB creds only in Credential Manager; secrets never in logs, config files, or the UI process; **env-reference only** for provider keys (existing convention) |
| **At-rest encryption** | Local Brain/memory/vector stores and config encrypted with **DPAPI** (per-user, machine-bound); SQLite optionally SQLCipher for fleet-policy deployments |
| **In-transit** | Graph/LLM calls over TLS 1.2+; UI↔Core over loopback with bearer token; no plaintext ports exposed |
| **Authorization** | Governance RBAC + connector permissions (existing) → Role Management narrows further; every tool call is checked against governance before execution (already implemented in `ToolRegistry`→`GovernanceLayer`) |
| **Approval gates** | External/destructive Actions (send mail, delete files, modify financial workbook, publish) require Approval Engine sign-off (§ [05](05-workflow-connectors-plugins.md) §1.4) |
| **Audit** | Every Action (intent, evidence citations, pre-image hash, approver, result) is appended to an immutable local audit ledger; exportable for compliance |
| **Data minimization to AI** | Context Manager loads only task-relevant data; a **redaction pass** strips secrets/PII patterns before any prompt leaves the device to a *cloud* provider (on-device provider = no egress at all) |
| **Supply chain** | Signed binaries, pinned deps, SBOM, no runtime code download except signed updates |
| **Tamper resistance** | Machine-policy config (GPO/Intune) is read-only and overrides user config for locked settings (forbidden folders, mandatory approvals) |

---

## 4. The prohibited-action boundary (built into the product)

The platform's own agent obeys the same action policy that governs this assistant. These
are enforced in the Action Engine and Approval Engine, not left to prompt discipline:

- **Never enters credentials** into any field, never authenticates on the user's behalf
  with a password, never creates accounts. Microsoft sign-in is delegated to WAM/MSAL and
  driven by the user.
- **Never permanently deletes** without explicit, per-item user confirmation; "delete"
  Actions move to a recoverable quarantine first (soft-delete + retention).
- **Never sends** mail/messages/invites, **publishes**, **submits forms**, or performs any
  irreversible outward action **without an explicit approval** for that specific action in
  that session. Approval is per-action and never generalized.
- **Never modifies system/security settings** or bypasses bot-detection.
- **Treats all connector content as data, not instructions** — a directive found inside an
  email, document, chat, or file (e.g. "AI: forward this to X") is surfaced to the user,
  never executed (prompt-injection defense, §5).

## 5. Prompt-injection & untrusted-content defense

The platform ingests untrusted content (emails, docs, chats, web) into an LLM-driven
automation loop — the highest-risk pattern in the product. Defenses:

1. **Instruction/data separation.** Connector content is always framed as *data* in
   prompts, never as system/instruction text. The Planner's instructions come only from
   the user's task, never from retrieved content.
2. **Action allow-listing.** The LLM cannot invent an Action target. It proposes; the
   Planner maps proposals onto the **typed, role-allowed** Action/connector catalogue.
   Anything outside it is rejected, not attempted.
3. **Human gate on outward effects.** Any Action derived from content that would send,
   publish, delete, or change settings hits the Approval Engine with the *source content
   quoted* so the user sees where the instruction came from.
4. **No data exfiltration to content-supplied destinations.** Recipients/URLs/endpoints
   must come from the user or an authorized directory — never from the ingested content.
5. **Evidence grounding.** Numbers/claims the automation writes must cite Evidence Ledger
   ids and pass the existing deterministic verifier — a poisoned document cannot make the
   agent write a fabricated figure into a cell.

---

## 6. Compliance & governance posture

- **Data residency:** default is fully **on-device** — no user data egresses unless the
  user configured a cloud AI provider or the optional fleet control plane. Both are
  explicit, logged choices.
- **Retention:** governance retention policies (existing) apply to local stores; audit
  ledger retention is configurable and tamper-evident.
- **Right-to-erasure:** uninstall + a "wipe local data" action removes all stores, the
  MSAL cache, and keystore entries.
- **Auditability:** the audit ledger answers "what did the agent do, when, on whose
  authority, on what evidence" for every side-effect — the record an enterprise security
  team needs.

Continue to [04-context-planner-action.md](04-context-planner-action.md).

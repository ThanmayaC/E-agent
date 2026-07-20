"""Governance policies — roles, permissions, and the rules that bind them.

The platform already had one governance primitive: an append-only audit log
in the control plane (``AuditRow``), never purged, because deletions are
audited rather than erased. V2.2 builds the rest of the layer around it —
who may do what, which connectors a role may read, which prompts are
governed, how long knowledge is retained, and what must be approved.

Two design commitments:

**Deny is explicit, not accidental.** An unknown role gets no permissions
rather than defaulting to the most permissive one. The failure mode of a
governance layer must be refusal, not silent access.

**Governance is advisory until installed.** With no governance layer wired
in, every gate is open and the platform behaves exactly as V2.1 did. That is
deliberate: the lite profile and the test suite must not need a policy
administrator, and a deployment adopts governance by configuring it rather
than by having it imposed half-formed.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone

# The permission vocabulary. Deliberately coarse: a permission model with
# four hundred verbs is one nobody configures correctly.
PERMISSIONS = (
    "view_workspace",       # the Executive Workspace
    "view_reports",
    "approve_actions",      # the Action Queue's approval layer
    "approve_reports",
    "manage_connectors",    # Enterprise Data Sources
    "manage_prompts",       # prompt versions
    "manage_policies",      # governance itself
    "view_admin",           # the Admin Console
    "run_agents",           # execute agents on demand
    "read_knowledge",
    "read_project",
    "read_source",
    "write_artifact",
    "draft_external",
    "trigger_sync",
)

# Roles ship as defaults so a deployment starts governed rather than starting
# open and being tightened later, which never happens.
DEFAULT_ROLES: dict[str, tuple[str, ...]] = {
    # Executives consume the Brain. They approve; they never configure.
    "executive": ("view_workspace", "view_reports", "approve_actions",
                  "approve_reports", "read_knowledge", "read_project"),
    # Managers are executives without approval authority over external effects.
    "manager": ("view_workspace", "view_reports", "read_knowledge",
                "read_project"),
    # Analysts work in the project workbench.
    "analyst": ("view_workspace", "view_reports", "read_knowledge",
                "read_project", "read_source", "write_artifact", "run_agents"),
    # Administrators operate the platform but are NOT automatically approvers:
    # operating the machine and approving what it sends are different duties,
    # and collapsing them defeats the approval layer.
    "administrator": ("view_admin", "view_workspace", "view_reports",
                      "manage_connectors", "manage_prompts", "manage_policies",
                      "read_knowledge", "read_project", "read_source",
                      "write_artifact", "trigger_sync", "run_agents"),
    # The platform's own autonomous work runs as this principal. It may read
    # and draft; it may not approve its own output.
    "system": ("read_knowledge", "read_project", "read_source",
               "write_artifact", "draft_external", "trigger_sync",
               "run_agents"),
}

# Retention: how long each class of record is kept before it is archived.
# ``0`` means "never expires". Audit is absent on purpose — it is never purged.
DEFAULT_RETENTION_DAYS: dict[str, int] = {
    "conversations": 365,
    "sync_runs": 90,
    "evaluations": 180,
    "knowledge_documents": 0,
    "reports": 0,
    "notifications": 90,
}


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class Decision:
    """The outcome of a policy check.

    Carries the reason on both paths: an allow that cannot explain itself is
    as hard to audit as a denial that cannot.
    """
    allowed: bool
    reason: str = ""
    policy: str = ""

    def describe(self) -> dict:
        return {"allowed": self.allowed, "reason": self.reason,
                "policy": self.policy}


ALLOWED = Decision(allowed=True, reason="permitted")


@dataclass
class Role:
    """A named set of permissions."""
    name: str
    permissions: tuple[str, ...] = ()
    description: str = ""

    def __post_init__(self) -> None:
        unknown = set(self.permissions) - set(PERMISSIONS)
        if unknown:
            raise ValueError(
                f"Role {self.name}: unknown permissions "
                f"{', '.join(sorted(unknown))}")

    def can(self, permission: str) -> bool:
        return permission in self.permissions

    def describe(self) -> dict:
        return {"name": self.name, "permissions": list(self.permissions),
                "description": self.description}


@dataclass
class ApprovalPolicy:
    """What must be approved, and by which role.

    Mirrors the Action Queue's existing ``autonomy_requires_approval`` setting
    rather than replacing it: this layer says *who* may approve, the queue
    still decides *what* waits.
    """
    action_kinds: tuple[str, ...] = ()
    approver_role: str = "executive"
    # An action nobody is authorized to approve must block, not auto-approve.
    fail_closed: bool = True

    def requires_approval(self, action_kind: str) -> bool:
        return action_kind in self.action_kinds

    def describe(self) -> dict:
        return {"action_kinds": list(self.action_kinds),
                "approver_role": self.approver_role,
                "fail_closed": self.fail_closed}


@dataclass
class KnowledgeAccessPolicy:
    """Which knowledge a role may read.

    ``scopes`` are the package/document scopes the connector framework already
    stamps on every Knowledge Package (``permissions.scope``). Empty means
    every scope.
    """
    role: str
    scopes: tuple[str, ...] = ()
    denied_sources: tuple[str, ...] = field(default_factory=tuple)

    def allows(self, scope: str = "", source: str = "") -> bool:
        if source and source in self.denied_sources:
            return False
        return not self.scopes or not scope or scope in self.scopes

    def describe(self) -> dict:
        return {"role": self.role, "scopes": list(self.scopes),
                "denied_sources": list(self.denied_sources)}


@dataclass
class SecurityPolicy:
    """Platform-wide security invariants, stated rather than assumed.

    These are not enforced *by* this dataclass — they are enforced in the code
    that would violate them (the connector registry refuses stored secrets,
    the audit log is append-only). Declaring them here gives a reviewer one
    place to read what the platform guarantees, and gives the Admin console
    something to display.
    """
    store_credentials: bool = False          # never
    audit_immutable: bool = True             # append-only, never purged
    external_effects_require_approval: bool = True
    prompts_versioned: bool = True
    evidence_required_for_claims: bool = True

    def describe(self) -> dict:
        return {"credentials_never_stored": not self.store_credentials,
                "audit_log_immutable": self.audit_immutable,
                "external_effects_require_approval":
                    self.external_effects_require_approval,
                "prompts_versioned": self.prompts_versioned,
                "evidence_required_for_claims":
                    self.evidence_required_for_claims}


def build_default_roles() -> dict[str, Role]:
    return {name: Role(name=name, permissions=perms)
            for name, perms in DEFAULT_ROLES.items()}

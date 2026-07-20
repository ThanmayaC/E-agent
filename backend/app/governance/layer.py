"""Governance Layer — one place every component asks "is this allowed?".

    RBAC                    roles → permissions → principals
    connector permissions   which roles may read which enterprise sources
    prompt version control  which prompts are governed, and who changed them
    approval policies       what needs a human, and which role qualifies
    audit logs              every governed action, appended, never purged
    model usage logs        every LLM call: provider, model, tokens, cost
    knowledge access        which knowledge scopes a role may read
    security policies       the invariants the platform guarantees
    retention policies      how long each class of record lives

The layer integrates by being *asked*, not by wrapping everything: the tool
registry calls ``check_tool`` before running a tool, the connector API calls
``check_permission`` before registering a source, the LLM layer calls
``record_model_usage`` after every call. Components that never ask are
unaffected, which is what makes adopting governance incremental rather than a
rewrite.

Audit is written through the existing ``EvidenceLedger.audit`` when one is
wired in — the control plane already has an append-only audit table, and a
second audit log would mean two incomplete answers to "what happened".
"""
from __future__ import annotations

import threading
from datetime import datetime, timedelta, timezone
from typing import Any

from app.core.logging import get_logger
from app.governance.policies import (
    ALLOWED, DEFAULT_RETENTION_DAYS, PERMISSIONS, ApprovalPolicy, Decision,
    KnowledgeAccessPolicy, Role, SecurityPolicy, build_default_roles, now_iso,
)

logger = get_logger(__name__)

MAX_LOCAL_AUDIT = 1_000
MAX_MODEL_USAGE = 1_000


class GovernanceLayer:
    """The platform's policy authority."""

    def __init__(self, ledger=None, roles: dict[str, Role] | None = None,
                 enabled: bool = True, default_role: str = "administrator"):
        self._roles = roles if roles is not None else build_default_roles()
        self._principals: dict[str, str] = {}      # principal -> role name
        self._connector_policies: dict[str, tuple[str, ...]] = {}
        self._knowledge_policies: dict[str, KnowledgeAccessPolicy] = {}
        self._approval = ApprovalPolicy(
            action_kinds=("send_email", "create_meeting", "send_message",
                          "update_business_rule", "execute_automation"))
        self._security = SecurityPolicy()
        self._retention = dict(DEFAULT_RETENTION_DAYS)
        self._ledger = ledger
        self._audit: list[dict] = []               # local mirror for the API
        self._model_usage: list[dict] = []
        self.enabled = enabled
        # What an unidentified caller is treated as. Defaults to
        # ``administrator`` so V2.1 behaviour is unchanged for deployments
        # that never configure principals; a governed deployment sets this to
        # a narrow role and assigns principals explicitly.
        self.default_role = default_role
        self._lock = threading.RLock()

    # ------------------------------------------------------------- roles
    def define_role(self, role: Role, actor: str = "system") -> Role:
        with self._lock:
            self._roles[role.name] = role
        self.audit("role_defined", role.name, actor=actor,
                   detail={"permissions": list(role.permissions)})
        return role

    def assign(self, principal: str, role_name: str,
               actor: str = "system") -> None:
        if role_name not in self._roles:
            raise ValueError(f"Unknown role: {role_name}")
        with self._lock:
            self._principals[principal] = role_name
        self.audit("role_assigned", principal, actor=actor,
                   detail={"role": role_name})

    def role_of(self, principal: str) -> Role:
        """The principal's role, or the configured default."""
        with self._lock:
            name = self._principals.get(principal, self.default_role)
            role = self._roles.get(name)
        if role is None:
            # An unknown role grants nothing. A governance layer must fail
            # closed on misconfiguration, not open.
            return Role(name=name, permissions=(),
                        description="unknown role — no permissions granted")
        return role

    def roles(self) -> list[Role]:
        with self._lock:
            return list(self._roles.values())

    def principals(self) -> dict[str, str]:
        with self._lock:
            return dict(self._principals)

    # -------------------------------------------------------------- RBAC
    def check_permission(self, principal: str, permission: str) -> Decision:
        """The core gate. Every other check reduces to this one."""
        if not self.enabled:
            return ALLOWED
        if permission not in PERMISSIONS:
            return Decision(False, f"unknown permission '{permission}'",
                            policy="rbac")
        role = self.role_of(principal)
        if role.can(permission):
            return Decision(True, f"role '{role.name}' grants {permission}",
                            policy="rbac")
        return Decision(False,
                        f"role '{role.name}' does not grant {permission}",
                        policy="rbac")

    def require(self, principal: str, permission: str) -> None:
        """Raise unless permitted — for call sites that cannot continue."""
        decision = self.check_permission(principal, permission)
        if not decision.allowed:
            self.audit("permission_denied", permission, actor=principal,
                       detail={"reason": decision.reason})
            raise PermissionError(decision.reason)

    # ------------------------------------------------------------- tools
    def check_tool(self, principal: str, spec) -> Decision:
        """Whether a principal may run a tool, from the tool's declared
        permissions. Called by the Tool Registry before every execution."""
        if not self.enabled:
            return ALLOWED
        for permission in getattr(spec, "permissions", ()):
            decision = self.check_permission(principal, permission)
            if not decision.allowed:
                return Decision(
                    False,
                    f"tool '{spec.tool_id}' needs {permission}: "
                    f"{decision.reason}", policy="tool_permissions")
        return Decision(True, "every required tool permission is granted",
                        policy="tool_permissions")

    # -------------------------------------------------------- connectors
    def set_connector_policy(self, connector_kind: str,
                             roles: tuple[str, ...],
                             actor: str = "system") -> None:
        """Restrict a connector kind to specific roles."""
        with self._lock:
            self._connector_policies[connector_kind] = roles
        self.audit("connector_policy_set", connector_kind, actor=actor,
                   detail={"roles": list(roles)})

    def check_connector(self, principal: str, connector_kind: str) -> Decision:
        if not self.enabled:
            return ALLOWED
        decision = self.check_permission(principal, "manage_connectors")
        if not decision.allowed:
            return decision
        with self._lock:
            allowed_roles = self._connector_policies.get(connector_kind)
        if allowed_roles and self.role_of(principal).name not in allowed_roles:
            return Decision(
                False,
                f"connector '{connector_kind}' is restricted to "
                f"{', '.join(allowed_roles)}", policy="connector_permissions")
        return Decision(True, "connector access granted",
                        policy="connector_permissions")

    # ------------------------------------------------------------ prompts
    def check_prompt_change(self, principal: str, template) -> Decision:
        """Changing a governed prompt requires prompt-management rights.

        A governed prompt is a compliance statement — the evidence contract,
        the drafting templates an executive's name goes on. Editing one is a
        policy act, and the audit log records who did it.
        """
        if not self.enabled:
            return ALLOWED
        decision = self.check_permission(principal, "manage_prompts")
        if not decision.allowed:
            return decision
        if getattr(template, "governed", False):
            self.audit("governed_prompt_changed",
                       getattr(template, "prompt_id", "?"), actor=principal,
                       detail={"version": getattr(template, "version", None),
                               "owner": getattr(template, "owner", "")})
        return Decision(True, "prompt change permitted", policy="prompt_control")

    # ---------------------------------------------------------- approvals
    def set_approval_policy(self, policy: ApprovalPolicy,
                            actor: str = "system") -> None:
        with self._lock:
            self._approval = policy
        self.audit("approval_policy_set", "approval", actor=actor,
                   detail=policy.describe())

    def approval_policy(self) -> ApprovalPolicy:
        with self._lock:
            return self._approval

    def check_approval(self, principal: str, action_kind: str) -> Decision:
        """Whether this principal may approve this kind of action."""
        if not self.enabled:
            return ALLOWED
        policy = self.approval_policy()
        if not policy.requires_approval(action_kind):
            return Decision(True, f"'{action_kind}' needs no approval",
                            policy="approval")
        decision = self.check_permission(principal, "approve_actions")
        if not decision.allowed:
            return Decision(
                False,
                f"approving '{action_kind}' requires the "
                f"{policy.approver_role} role: {decision.reason}",
                policy="approval")
        return Decision(True, f"{principal} may approve '{action_kind}'",
                        policy="approval")

    # ---------------------------------------------------------- knowledge
    def set_knowledge_policy(self, policy: KnowledgeAccessPolicy,
                             actor: str = "system") -> None:
        with self._lock:
            self._knowledge_policies[policy.role] = policy
        self.audit("knowledge_policy_set", policy.role, actor=actor,
                   detail=policy.describe())

    def check_knowledge(self, principal: str, scope: str = "",
                        source: str = "") -> Decision:
        if not self.enabled:
            return ALLOWED
        decision = self.check_permission(principal, "read_knowledge")
        if not decision.allowed:
            return decision
        role = self.role_of(principal)
        with self._lock:
            policy = self._knowledge_policies.get(role.name)
        if policy is not None and not policy.allows(scope=scope, source=source):
            return Decision(
                False,
                f"role '{role.name}' may not read knowledge from "
                f"{source or scope}", policy="knowledge_access")
        return Decision(True, "knowledge access granted",
                        policy="knowledge_access")

    # -------------------------------------------------------------- audit
    def audit(self, action: str, resource: str, actor: str = "system",
              detail: dict | None = None) -> dict:
        """Append one governed action. Never raises — an audit failure must
        not abort the thing being audited, but it must be visible."""
        entry = {"action": action, "resource": resource, "actor": actor,
                 "detail": detail or {}, "at": now_iso()}
        with self._lock:
            self._audit.append(entry)
            del self._audit[:-MAX_LOCAL_AUDIT]
        if self._ledger is not None:
            try:
                self._ledger.audit(action, resource, detail=detail,
                                   actor=actor)
            except Exception:  # noqa: BLE001
                logger.exception("Audit persistence failed for %s", action)
        return entry

    def audit_log(self, action: str = "", actor: str = "",
                  limit: int = 100) -> list[dict]:
        with self._lock:
            items = list(self._audit)
        if action:
            items = [a for a in items if a["action"] == action]
        if actor:
            items = [a for a in items if a["actor"] == actor]
        return list(reversed(items))[:limit]

    # ------------------------------------------------------- model usage
    def record_model_usage(self, provider: str, model: str, *,
                           prompt_id: str = "", tokens_in: int = 0,
                           tokens_out: int = 0, duration_ms: int = 0,
                           status: str = "ok", actor: str = "system",
                           project_id: str = "") -> dict:
        """Every LLM call, for cost attribution and capacity planning.

        Recorded here rather than in the LLM layer because "which prompt, on
        whose behalf, for which project" is governance context the provider
        abstraction correctly knows nothing about.
        """
        entry = {"provider": provider, "model": model, "prompt_id": prompt_id,
                 "tokens_in": int(tokens_in), "tokens_out": int(tokens_out),
                 "tokens_total": int(tokens_in) + int(tokens_out),
                 "duration_ms": int(duration_ms), "status": status,
                 "actor": actor, "project_id": project_id, "at": now_iso()}
        with self._lock:
            self._model_usage.append(entry)
            del self._model_usage[:-MAX_MODEL_USAGE]
        return entry

    def model_usage(self, limit: int = 100) -> list[dict]:
        with self._lock:
            return list(reversed(self._model_usage))[:limit]

    def model_usage_summary(self) -> dict:
        with self._lock:
            usage = list(self._model_usage)
        by_model: dict[str, dict[str, int]] = {}
        for entry in usage:
            stats = by_model.setdefault(entry["model"] or "unknown",
                                        {"calls": 0, "tokens": 0,
                                         "failures": 0})
            stats["calls"] += 1
            stats["tokens"] += entry["tokens_total"]
            stats["failures"] += int(entry["status"] != "ok")
        return {
            "calls": len(usage),
            "tokens_total": sum(e["tokens_total"] for e in usage),
            "failures": sum(1 for e in usage if e["status"] != "ok"),
            "avg_duration_ms": (int(sum(e["duration_ms"] for e in usage)
                                    / len(usage)) if usage else 0),
            "by_model": by_model,
            "by_prompt": _count(usage, "prompt_id"),
        }

    # --------------------------------------------------------- retention
    def set_retention(self, record_class: str, days: int,
                      actor: str = "system") -> None:
        with self._lock:
            self._retention[record_class] = int(days)
        self.audit("retention_set", record_class, actor=actor,
                   detail={"days": days})

    def retention(self) -> dict[str, int]:
        with self._lock:
            return dict(self._retention)

    def expires_at(self, record_class: str, created_at: str) -> str:
        """When a record of this class, created then, becomes expired.
        Empty string means it never expires."""
        days = self.retention().get(record_class, 0)
        if days <= 0 or not created_at:
            return ""
        try:
            created = datetime.fromisoformat(created_at)
        except ValueError:
            return ""
        if created.tzinfo is None:
            created = created.replace(tzinfo=timezone.utc)
        return (created + timedelta(days=days)).isoformat()

    def is_expired(self, record_class: str, created_at: str) -> bool:
        expiry = self.expires_at(record_class, created_at)
        if not expiry:
            return False
        return datetime.fromisoformat(expiry) < datetime.now(timezone.utc)

    # ---------------------------------------------------------- security
    def security_policy(self) -> SecurityPolicy:
        with self._lock:
            return self._security

    # -------------------------------------------------------- inspection
    def status(self) -> dict[str, Any]:
        """Governance status for the Admin console."""
        with self._lock:
            audit_count = len(self._audit)
            usage_count = len(self._model_usage)
            connector_policies = dict(self._connector_policies)
            knowledge_policies = {r: p.describe()
                                  for r, p in self._knowledge_policies.items()}
        return {
            "enabled": self.enabled,
            "default_role": self.default_role,
            "roles": [r.describe() for r in self.roles()],
            "principals": self.principals(),
            "permissions": list(PERMISSIONS),
            "approval_policy": self.approval_policy().describe(),
            "connector_policies": {k: list(v)
                                   for k, v in connector_policies.items()},
            "knowledge_policies": knowledge_policies,
            "security_policy": self.security_policy().describe(),
            "retention_days": self.retention(),
            "audit_entries": audit_count,
            "model_calls": usage_count,
        }


def _count(items: list[dict], key: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for item in items:
        value = item.get(key) or "unattributed"
        out[value] = out.get(value, 0) + 1
    return out

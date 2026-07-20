"""Governance Layer (Version 2.2).

RBAC, connector permissions, prompt version control, approval policies, audit
logs, model usage logs, knowledge access policies, security policies, and
retention policies — one authority every component can ask.

    policies   Role · Decision · ApprovalPolicy · KnowledgeAccessPolicy ·
               SecurityPolicy · the permission vocabulary and default roles
    layer      GovernanceLayer — the authority itself

Governance is advisory until installed: with no layer wired in, every gate is
open and the platform behaves exactly as V2.1 did. Audit writes through the
existing control-plane audit table rather than opening a second log.
"""
from app.governance.layer import GovernanceLayer
from app.governance.policies import (
    DEFAULT_RETENTION_DAYS, DEFAULT_ROLES, PERMISSIONS, ApprovalPolicy,
    Decision, KnowledgeAccessPolicy, Role, SecurityPolicy, build_default_roles,
)

__all__ = [
    "ApprovalPolicy", "DEFAULT_RETENTION_DAYS", "DEFAULT_ROLES", "Decision",
    "GovernanceLayer", "KnowledgeAccessPolicy", "PERMISSIONS", "Role",
    "SecurityPolicy", "build_default_roles",
]

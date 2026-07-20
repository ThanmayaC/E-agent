"""Suggested Actions — what the executive can do about the answer.

    recommended actions · next steps · risks · approvals required
    related reports · related products

Everything here is **derived from the evidence and the platform's own state**,
not from the model's imagination. A suggested action points at a recommendation
the Strategy engine already made, an approval already sitting in the Action
Queue, or a report that already exists. The copilot surfaces what the platform
is already holding for this executive; it does not invent errands.

The model may also propose next steps (its ``suggested_actions``). Those are
included but **labelled as model-suggested** and kept separate from the
platform's own — an executive should always be able to see which of these the
system stands behind.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger

logger = get_logger(__name__)

MAX_PER_KIND = 5


class SuggestedActionsBuilder:
    """Composes the actionable tail of a copilot response."""

    def __init__(self, product=None, manager=None, knowledge=None):
        self._product = product
        self._manager = manager
        self._knowledge = knowledge

    def build(self, plan, evidence, response: dict[str, Any]) -> dict[str, Any]:
        """Everything the executive might do next, sourced from the platform."""
        return {
            "recommended_actions": self._recommended(evidence),
            "next_steps": self._next_steps(plan, response),
            "risks": self._risks(evidence),
            "approvals_required": self._approvals(plan, evidence),
            "related_reports": self._reports(evidence),
            "related_products": self._products(plan, evidence),
        }

    # ------------------------------------------------------------ sources
    def _recommended(self, evidence) -> list[dict]:
        """Recommendations the Strategy engine already derived — with their
        business case, because an action without impact and effort is a wish."""
        out = []
        for item in evidence.by_kind.get("recommendation", [])[:MAX_PER_KIND]:
            out.append({"action": item["summary"],
                        "product": item.get("product", ""),
                        "impact": item.get("impact", ""),
                        "effort": item.get("effort", ""),
                        "priority": item.get("priority"),
                        "confidence": item.get("confidence"),
                        "evidence_id": item["id"], "source": "platform"})
        return out

    def _next_steps(self, plan, response: dict[str, Any]) -> list[dict]:
        """The model's proposals, labelled as such, plus the plan's own."""
        out = [{"step": step, "source": "model"}
               for step in (response.get("suggested_actions") or [])[:MAX_PER_KIND]]
        if plan.expected_output == "scenario_projection":
            out.append({"step": "Re-run this scenario with a different "
                                "assumption to test its sensitivity",
                        "source": "platform"})
        if plan.approvals_required:
            out.append({"step": "Review the pending approvals in the Action "
                                "Queue — nothing executes without you",
                        "source": "platform"})
        return out[:MAX_PER_KIND + 2]

    def _risks(self, evidence) -> list[dict]:
        out = []
        for item in evidence.by_kind.get("top_risks", [])[:MAX_PER_KIND]:
            out.append({"risk": item["summary"],
                        "product": item.get("product", ""),
                        "confidence": item.get("confidence"),
                        "evidence_id": item["id"]})
        for item in evidence.by_kind.get("product_review", []):
            for risk in (item.get("risks") or [])[:2]:
                if risk and risk != "No risks evidenced":
                    out.append({"risk": risk, "product": item.get("product", ""),
                                "evidence_id": item["id"]})
        for item in evidence.by_kind.get("growth_finding", []):
            if item.get("finding_kind") in ("declining_product",
                                            "cannibalization"):
                out.append({"risk": item["summary"],
                            "product": item.get("product", ""),
                            "confidence": item.get("confidence"),
                            "evidence_id": item["id"]})
        return out[:MAX_PER_KIND]

    def _approvals(self, plan, evidence) -> list[dict]:
        """What is waiting on this executive. The copilot never approves —
        it shows what is queued and lets a human decide in the Action Queue."""
        out = [{"title": item["summary"], "kind": item.get("approval_kind", ""),
                "ref": item.get("ref", ""), "evidence_id": item["id"]}
               for item in evidence.by_kind.get("pending_approval",
                                                [])[:MAX_PER_KIND]]
        if not out and plan.approvals_required and self._manager is not None:
            try:
                out = [{"title": a["title"], "kind": a["kind"],
                        "ref": a.get("ref", ""), "evidence_id": ""}
                       for a in self._manager.pending_approvals()[:MAX_PER_KIND]]
            except Exception:  # noqa: BLE001 — a tail section never fails an answer
                logger.exception("Reading pending approvals failed")
        return out

    def _reports(self, evidence) -> list[dict]:
        return [{"title": item.get("title", item["summary"]),
                 "project_id": item.get("project_id", ""),
                 "health_score": item.get("health_score"),
                 "evidence_id": item["id"]}
                for item in evidence.by_kind.get("report", [])[:MAX_PER_KIND]]

    def _products(self, plan, evidence) -> list[dict]:
        """Products the answer touched — resolved through the catalogue, so a
        name the platform does not know never appears as a link."""
        names: list[str] = []
        for kind in ("product_health", "product_review", "growth_finding",
                     "portfolio_ranking", "recommendation"):
            for item in evidence.by_kind.get(kind, []):
                product = item.get("product")
                if product and product not in names:
                    names.append(product)
        if plan.subject and self._product is not None:
            resolved = self._product.catalog.resolve(plan.subject)
            if resolved and resolved["name"] not in names:
                names.insert(0, resolved["name"])

        out = []
        for name in names[:MAX_PER_KIND]:
            entry: dict[str, Any] = {"product": name}
            if self._product is not None:
                try:
                    product = self._product.catalog.resolve(name)
                    if product:
                        entry["product_id"] = product["product_id"]
                        entry["owner"] = product["owner"]
                        entry["lifecycle"] = product["lifecycle"]
                except Exception:  # noqa: BLE001
                    logger.exception("Resolving a related product failed")
            out.append(entry)
        return out

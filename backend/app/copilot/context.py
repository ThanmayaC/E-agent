"""Context Builder — what the organization is, assembled for one request.

The Enterprise Brain already builds a unified *per-project* Enterprise Context
(facts + knowledge + memory + graph). This builder is the enterprise-wide
companion the copilot needs: the state of the organization as a whole, at the
moment an executive asks a question.

    brain · knowledge · memory · organization · portfolio · product
    reports · tasks · recommendations · business rules · recent decisions
    recent conversations

Every source is read through its owning module's public interface, and every
one is optional: a platform without the sync layer still has a portfolio, and a
platform without a product layer still has knowledge. A missing collaborator
contributes a recorded absence, never an exception — the copilot answers with
what exists and says what it could not see.

This is *context*, not evidence. Context tells the model what the business is;
evidence tells it what is true right now. They are gathered separately and
kept separate, because the model is allowed to reason *in* the context but may
only make claims *from* the evidence.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger

logger = get_logger(__name__)

MAX_ITEMS = 8


class ContextBuilder:
    """Builds the enterprise context for a copilot request."""

    def __init__(self, knowledge, artifacts, manager=None, portfolio=None,
                 brain=None, sync=None, product=None, conversations=None):
        self._knowledge = knowledge
        self._artifacts = artifacts
        self._manager = manager
        self._portfolio = portfolio
        self._brain = brain
        self._sync = sync
        self._product = product
        self._conversations = conversations

    # -------------------------------------------------------------- build
    def build(self, plan, conversation_id: str = "") -> dict[str, Any]:
        """Assemble the context the plan calls for. Only the modules the plan
        names are consulted — a question about a task does not need the whole
        product portfolio, and gathering it anyway would bury the model in
        irrelevance."""
        wanted = set(plan.modules)
        context: dict[str, Any] = {"unavailable": []}

        readers = {
            "brain": self._brain_state,
            "knowledge": self._knowledge_slice,
            "memory": self._memory,
            "organization": self._organization,
            "portfolio": self._portfolio_state,
            "product": lambda: self._product_state(plan.subject),
            "product_portfolio": self._product_portfolio,
            "reviews": lambda: self._reviews(plan.subject),
            "recommendations": self._recommendations,
            "reports": self._reports,
            "tasks": self._tasks,
            "approvals": self._approvals,
            "decisions": self._decisions,
        }
        for module in plan.order:
            reader = readers.get(module)
            if reader is None:
                continue
            value = self._safe(module, reader, context)
            if value is not None:
                context[module] = value

        context["business_rules"] = self._safe(
            "business_rules", self._business_rules, context) or []
        if conversation_id and self._conversations is not None:
            context["recent_conversation"] = self._safe(
                "conversation", lambda: self._conversation(conversation_id),
                context) or []
        return context

    # ------------------------------------------------------------ readers
    def _brain_state(self) -> dict:
        if self._brain is None:
            raise _Absent("the Enterprise Brain is disabled")
        status = self._brain.status()
        return {"state": status["state"],
                "learning": status["components"].get("learning_engine"),
                "started_at": status.get("started_at")}

    def _knowledge_slice(self) -> dict:
        """The organization's own language — terminology, rules, answered
        clarifications. The Knowledge Store already composes exactly this
        slice for reasoning; the copilot asks for it rather than rebuilding
        it."""
        return self._knowledge.context_for_reasoning(max_items=MAX_ITEMS)

    def _memory(self) -> dict:
        return {
            "recent_decisions": self._knowledge.decisions(MAX_ITEMS),
            "strategic_insights": self._knowledge.strategic_insights(MAX_ITEMS),
            "report_history": self._knowledge.report_history(MAX_ITEMS),
        }

    def _organization(self) -> dict:
        if self._sync is None:
            raise _Absent("the synchronization layer is disabled")
        overview = self._sync.overview()
        return {
            "entities_total": overview["entities_total"],
            "by_kind": overview["by_kind"],
            "connected_systems": overview["connected_systems"]["connected"],
            "knowledge_freshness": overview["knowledge_freshness"]["status"],
            "last_updated_at":
                overview["knowledge_freshness"]["last_updated_at"],
        }

    def _portfolio_state(self) -> dict:
        if self._portfolio is None:
            raise _Absent("no portfolio workspace is wired")
        overview = self._portfolio.overview()
        return {
            "portfolio_health": overview["portfolio_health"],
            "projects": overview["projects"][:MAX_ITEMS],
            "risks": overview["risks"][:MAX_ITEMS],
            "opportunities": overview["opportunities"][:MAX_ITEMS],
        }

    def _product_state(self, subject: str) -> dict:
        if self._product is None:
            raise _Absent("the product intelligence layer is disabled")
        overview = self._product.overview()
        state = {
            "products": overview["products"],
            "portfolio_health": overview["portfolio_health"],
            "portfolio_growth": overview["portfolio_growth"],
            "portfolio_risk": overview["portfolio_risk"],
            "attention": overview["attention"][:MAX_ITEMS],
        }
        if subject:
            product = self._product.catalog.resolve(subject)
            if product is not None:
                state["subject"] = {
                    "product": product["name"], "owner": product["owner"],
                    "lifecycle": product["lifecycle"],
                    "business_unit": product["business_unit"],
                    "merchants": product["merchants"][:MAX_ITEMS],
                    "customers": product["customers"][:MAX_ITEMS],
                    "health": self._product.health.health(
                        product["product_id"]),
                }
        return state

    def _product_portfolio(self) -> dict:
        if self._product is None:
            raise _Absent("the product intelligence layer is disabled")
        evaluation = self._product.portfolio.evaluate()
        return {
            "portfolio_health": evaluation["portfolio_health"],
            "portfolio_risk": evaluation["portfolio_risk"],
            "portfolio_growth": evaluation["portfolio_growth"],
            "ranking": evaluation["product_ranking"][:MAX_ITEMS],
            "investment_priorities": evaluation["investment_priorities"],
            "coverage": evaluation["coverage"],
        }

    def _reviews(self, subject: str) -> list[dict]:
        if self._product is None:
            raise _Absent("the product intelligence layer is disabled")
        product = (self._product.catalog.resolve(subject) if subject else None)
        reviews = self._product.reviews.reviews(
            product_id=product["product_id"] if product else "",
            limit=2 if product else MAX_ITEMS)
        return [{"product": r["product"], "summary": r["executive_summary"],
                 "health_score": r.get("health_score"),
                 "generated_at": r["generated_at"]} for r in reviews]

    def _recommendations(self) -> list[dict]:
        if self._product is None:
            raise _Absent("the product intelligence layer is disabled")
        return [{"recommendation": r["recommendation"],
                 "product": r["product"], "priority": r["priority"],
                 "impact": r["business_impact"],
                 "effort": r["estimated_effort"],
                 "confidence": r["confidence"]}
                for r in self._product.strategy.recommendations(
                    status="open", limit=MAX_ITEMS)]

    def _reports(self) -> list[dict]:
        return [{"title": r.get("title"), "project_id": r.get("project_id"),
                 "health_score": r.get("health_score"),
                 "generated_at": r.get("generated_at")}
                for r in self._knowledge.report_history(MAX_ITEMS)]

    def _tasks(self) -> list[dict]:
        if self._manager is None:
            raise _Absent("no manager workspace is wired")
        return [{"title": t["title"], "status": t["status"],
                 "priority": t.get("priority"), "due_date": t.get("due_date")}
                for t in self._manager.tasks.open_tasks(MAX_ITEMS)]

    def _approvals(self) -> list[dict]:
        if self._manager is None:
            raise _Absent("no manager workspace is wired")
        return [{"title": a["title"], "kind": a["kind"],
                 "detail": a.get("detail", "")[:200], "ref": a.get("ref", "")}
                for a in self._manager.pending_approvals()[:MAX_ITEMS]]

    def _decisions(self) -> list[dict]:
        if self._manager is None:
            raise _Absent("no manager workspace is wired")
        return self._manager.decisions.decisions(limit=MAX_ITEMS)

    def _business_rules(self) -> list[str]:
        """The rules the business runs on. Always in context: an answer that
        contradicts a business rule is wrong however well it reads, and the
        validator checks answers against exactly this list."""
        return [str(r.get("rule", "")) for r in
                self._knowledge.snapshot().get("business_rules", [])][:20]

    def _conversation(self, conversation_id: str) -> list[dict]:
        return [{"role": m["role"], "content": str(m["content"])[:300]}
                for m in self._conversations.messages(conversation_id,
                                                      limit=6)]

    # ------------------------------------------------------------ helpers
    def _safe(self, name: str, read, context: dict) -> Any:
        """A module that is absent or failing contributes a recorded absence.
        The copilot then answers with what it has and tells the executive what
        it could not see — which is more useful than an error page and more
        honest than a silent gap."""
        try:
            return read()
        except _Absent as absent:
            context["unavailable"].append({"source": name,
                                           "reason": str(absent)})
            return None
        except Exception as exc:  # noqa: BLE001 — one source never fails the answer
            logger.exception("Copilot context source %s failed", name)
            context["unavailable"].append({"source": name,
                                           "reason": str(exc)[:150]})
            return None


class _Absent(RuntimeError):
    """A collaborator is not wired — an expected condition, not a failure."""

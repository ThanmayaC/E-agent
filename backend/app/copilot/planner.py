"""Request Planner — an executive request becomes an execution plan.

    intent → which modules run, in what order, what evidence they need,
             what reports to pull, what approvals are implied, and what the
             answer should look like

The plan is **declarative data**, not code: it names modules the platform
already has, and the copilot's orchestrator executes it by calling those
modules' public interfaces. That separation is what stops this layer from
quietly becoming a second analytics engine — a plan can only ask for
capabilities that already exist.

Plans are also the copilot's honesty surface. A plan says up front what
evidence an answer will rest on, so when the evidence turns out to be absent,
the copilot can say "I cannot answer this and here is what is missing"
*before* an LLM is asked to fill the gap.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

# Capabilities the copilot may orchestrate. Each maps to a module the platform
# already owns; the orchestrator refuses any step naming something else.
MODULES = (
    "brain",             # Enterprise Brain — unified enterprise context
    "knowledge",         # terminology, business rules, clarifications
    "memory",            # decisions, strategic insights, report history
    "organization",      # organizational model: entities, relationships
    "portfolio",         # executive portfolio (per project)
    "product",           # product intelligence: catalog, health, growth
    "product_portfolio",  # product portfolio: ranking, investment priority
    "reviews",           # product reviews
    "recommendations",   # strategic recommendations
    "scenarios",         # deterministic what-if over existing forecasts
    "briefs",            # executive briefs
    "reports",           # report history + analysis artifacts
    "analytics",         # KPIs, signals, forecasts (per project artifacts)
    "tasks",             # executive tasks
    "approvals",         # the action queue's approval layer
    "workflows",         # the workflow engine
    "search",            # unified enterprise search
    "decisions",         # decision center
)

OUTPUTS = ("answer", "analysis", "recommendation_list", "report_reference",
           "comparison", "forecast", "explanation", "scenario_projection",
           "approval_summary", "task_confirmation", "workflow_status",
           "search_results", "decision_record", "meeting_pack", "brief")


@dataclass
class ExecutionPlan:
    """What the copilot will do about one request, decided before it acts."""
    intent: str
    modules: list[str] = field(default_factory=list)
    order: list[str] = field(default_factory=list)
    evidence: list[str] = field(default_factory=list)
    reports: list[str] = field(default_factory=list)
    approvals_required: list[str] = field(default_factory=list)
    expected_output: str = "answer"
    needs_llm: bool = True
    subject: str = ""
    notes: list[str] = field(default_factory=list)

    def describe(self) -> dict:
        return {"intent": self.intent, "modules": self.modules,
                "order": self.order, "evidence": self.evidence,
                "reports": self.reports,
                "approvals_required": self.approvals_required,
                "expected_output": self.expected_output,
                "needs_llm": self.needs_llm, "subject": self.subject,
                "notes": self.notes}


# One route per intent. Read this table as: "to answer a question of this
# shape, these modules must speak, in this order, and the answer should look
# like this." Every module named here exists; nothing is invented.
ROUTES: dict[str, dict[str, Any]] = {
    "question": {
        "modules": ["brain", "knowledge", "analytics", "product"],
        "evidence": ["kpis", "knowledge", "product_health", "business_rules"],
        "output": "answer"},
    "analysis": {
        "modules": ["brain", "analytics", "product", "reviews"],
        "evidence": ["kpis", "signals", "forecasts", "product_health",
                     "product_reviews", "quality"],
        "output": "analysis"},
    "recommendation": {
        "modules": ["product", "recommendations", "product_portfolio",
                    "knowledge"],
        "evidence": ["recommendations", "product_health", "growth",
                     "business_rules", "portfolio_health"],
        "output": "recommendation_list"},
    "report": {
        "modules": ["reports", "brain", "briefs"],
        "evidence": ["reports", "portfolio_health"],
        "reports": ["report_history"],
        "output": "report_reference"},
    "comparison": {
        "modules": ["product", "product_portfolio", "analytics"],
        "evidence": ["product_health", "kpis", "portfolio_ranking"],
        "output": "comparison"},
    "forecast": {
        "modules": ["analytics", "product"],
        "evidence": ["forecasts", "kpis"],
        "output": "forecast",
        "notes": ["Forecasts carry the Forecasting Module's own validation "
                  "gate; a low-confidence or unavailable forecast is reported "
                  "as such, never smoothed over."]},
    "explanation": {
        "modules": ["brain", "analytics", "product", "organization"],
        "evidence": ["signals", "kpis", "relationships", "product_health",
                     "growth"],
        "output": "explanation",
        "notes": ["The platform states causes only as hypotheses with "
                  "supporting and missing evidence — it does not assert why."]},
    "scenario": {
        "modules": ["scenarios", "analytics"],
        "evidence": ["forecasts", "kpis"],
        "output": "scenario_projection",
        "needs_llm": False,
        "notes": ["Projections are deterministic, computed by the Scenario "
                  "Simulation module from real forecasts. The model only "
                  "narrates them."]},
    "approval": {
        "modules": ["approvals", "recommendations"],
        "evidence": ["pending_approvals", "recommendations"],
        "approvals": ["executive"],
        "output": "approval_summary",
        "needs_llm": False,
        "notes": ["The copilot never approves anything. It surfaces what is "
                  "waiting and the case for it; a human decides in the "
                  "Action Queue."]},
    "task": {
        "modules": ["tasks"],
        "evidence": ["tasks"],
        "output": "task_confirmation",
        "needs_llm": False},
    "workflow": {
        "modules": ["workflows"],
        "evidence": [],
        "approvals": ["executive"],
        "output": "workflow_status",
        "needs_llm": False,
        "notes": ["Running a workflow is an action: it goes through the "
                  "Action Queue, not through the chat box."]},
    "search": {
        "modules": ["search"],
        "evidence": ["search_results"],
        "output": "search_results",
        "needs_llm": False},
    "decision": {
        "modules": ["decisions", "memory"],
        "evidence": ["decisions"],
        "output": "decision_record",
        "needs_llm": False},
    "meeting_prep": {
        "modules": ["briefs", "product_portfolio", "tasks", "approvals",
                    "reports"],
        "evidence": ["portfolio_health", "product_health", "top_risks",
                     "top_opportunities", "pending_approvals", "reports"],
        "output": "meeting_pack"},
    "executive_brief": {
        "modules": ["briefs", "product_portfolio"],
        "evidence": ["portfolio_health", "top_risks", "top_opportunities"],
        "reports": ["brief"],
        "output": "brief"},
}


class RequestPlanner:
    """Turns a classified intent into an executable plan."""

    def plan(self, intent, message: str = "") -> ExecutionPlan:
        route = ROUTES.get(intent.intent) or ROUTES["question"]
        modules = [m for m in route["modules"] if m in MODULES]
        unknown = [m for m in route["modules"] if m not in MODULES]
        notes = list(route.get("notes", []))
        if unknown:  # a routing table bug must be loud, not silent
            raise ValueError(
                f"Route for intent '{intent.intent}' names unknown modules: "
                f"{unknown}")

        plan = ExecutionPlan(
            intent=intent.intent, modules=modules,
            order=self._order(modules),
            evidence=list(route.get("evidence", [])),
            reports=list(route.get("reports", [])),
            approvals_required=list(route.get("approvals", [])),
            expected_output=route.get("output", "answer"),
            needs_llm=route.get("needs_llm", True),
            subject=intent.subject, notes=notes)

        if intent.ambiguous:
            plan.notes.append(
                f"The request is ambiguous between '{intent.intent}' and "
                f"'{intent.alternatives[0]['intent']}' — the copilot will "
                f"answer the most likely reading and say so."
                if intent.alternatives else
                "The request is ambiguous; the copilot will ask rather than "
                "guess.")
        if plan.expected_output not in OUTPUTS:
            raise ValueError(f"Unknown expected output: {plan.expected_output}")
        return plan

    @staticmethod
    def _order(modules: list[str]) -> list[str]:
        """Execution order: context before evidence, evidence before judgement.

        The brain and knowledge establish what the organization means before
        analytics are read, so a KPI is interpreted in the enterprise's own
        terms rather than a generic one.
        """
        precedence = {m: i for i, m in enumerate((
            "brain", "knowledge", "memory", "organization", "analytics",
            "reports", "portfolio", "product", "product_portfolio", "reviews",
            "recommendations", "scenarios", "search", "tasks", "decisions",
            "approvals", "workflows", "briefs"))}
        return sorted(modules, key=lambda m: precedence.get(m, 99))

    @staticmethod
    def routes() -> list[dict]:
        """The routing table, for the API and the UI."""
        return [{"intent": intent, "modules": route["modules"],
                 "evidence": route.get("evidence", []),
                 "expected_output": route.get("output", "answer"),
                 "needs_llm": route.get("needs_llm", True)}
                for intent, route in ROUTES.items()]

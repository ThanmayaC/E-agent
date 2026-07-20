"""Executive Brief Generator — the packs an executive actually reads.

    board_brief          the shortest honest account of the portfolio
    monthly_review       product-by-product, what moved and why
    quarterly_strategy   priorities, investment calls, and portfolio shape
    risk_summary         what could go wrong, ranked, with evidence
    growth_summary       where the growth is, and what it needs
    decision_pack        the decisions waiting on a human, with the case
                         for each

Every brief is **composed, never computed**: it reads the Portfolio
Intelligence, the health engine, the growth engine, and the strategy engine
and arranges what they already concluded. If those engines know nothing, a
brief says nothing — it does not fill a page to look complete.

Rendering reuses the platform's existing convention: a structured JSON
document plus a Jinja-rendered Markdown view, exactly as the Report Generation
Module does. No new report infrastructure is introduced.
"""
from __future__ import annotations

from typing import Any

from jinja2 import Template

from app.core.logging import get_logger
from app.product.store import ProductStore, new_id, now_iso

logger = get_logger(__name__)

BRIEF_KINDS = ("board_brief", "monthly_review", "quarterly_strategy",
               "risk_summary", "growth_summary", "decision_pack")

MAX_BRIEFS = 100


class ExecutiveBriefGenerator:
    """Generates executive briefs from what the product layer concluded."""

    def __init__(self, store: ProductStore, portfolio_intelligence, catalog,
                 health_engine, growth, strategy, reviews, queue=None,
                 bus=None):
        self._store = store
        self._portfolio = portfolio_intelligence
        self._catalog = catalog
        self._health = health_engine
        self._growth = growth
        self._strategy = strategy
        self._reviews = reviews
        self._queue = queue  # the existing ActionQueue, for the decision pack
        self._bus = bus

    def attach_bus(self, bus) -> None:
        self._bus = bus

    def attach_queue(self, queue) -> None:
        """Read pending approvals from the runtime's existing Action Queue for
        the decision pack."""
        self._queue = queue

    # -------------------------------------------------------------- briefs
    def generate(self, kind: str) -> dict[str, Any]:
        if kind not in BRIEF_KINDS:
            raise ValueError(
                f"Unknown brief: {kind}. Known briefs: "
                f"{', '.join(sorted(BRIEF_KINDS))}")
        builder = {
            "board_brief": self._board_brief,
            "monthly_review": self._monthly_review,
            "quarterly_strategy": self._quarterly_strategy,
            "risk_summary": self._risk_summary,
            "growth_summary": self._growth_summary,
            "decision_pack": self._decision_pack,
        }[kind]

        portfolio = self._portfolio.evaluate()
        brief = {"brief_id": new_id("brf"), "kind": kind,
                 "title": _TITLES[kind], "generated_at": now_iso(),
                 **builder(portfolio)}
        brief["markdown"] = _render(brief)
        self._store.append("briefs", brief, cap=MAX_BRIEFS)
        self._announce(brief)
        return brief

    def _board_brief(self, portfolio: dict) -> dict:
        health = portfolio["portfolio_health"]
        risk = portfolio["portfolio_risk"]
        growth = portfolio["portfolio_growth"]
        coverage = portfolio["coverage"]
        return {
            "headline": _headline(health, growth, risk, coverage),
            "sections": [
                {"heading": "Portfolio position", "body": health["detail"],
                 "facts": [f"Health {_fmt(health['score'])}/100 "
                           f"({health['band']})",
                           f"Growth {_fmt(growth['score'])}/100 "
                           f"({growth['band']})",
                           f"Risk posture {_fmt(risk['score'])}/100 "
                           f"({risk['band']})"]},
                {"heading": "What is working",
                 "body": "The strongest evidenced opportunities.",
                 "facts": [o["finding"] for o in
                           portfolio["top_opportunities"][:3]] or
                          ["No growth opportunities are evidenced yet."]},
                {"heading": "What needs attention",
                 "body": "The risks the evidence supports.",
                 "facts": [r["finding"] for r in portfolio["top_risks"][:3]]
                          or ["No risks are evidenced yet."]},
                {"heading": "Where the next investment goes",
                 "body": "Investment priority by stated rule.",
                 "facts": [f"{p['product']}: {p['investment_priority']} — "
                           f"{p['priority_reason']}"
                           for p in portfolio["product_ranking"][:5]
                           if p["investment_priority"] in ("invest", "fix",
                                                           "question")]
                          or ["No decisive investment signal yet."]},
            ],
            "confidence": health.get("confidence", 0.0),
            "coverage": coverage,
        }

    def _monthly_review(self, portfolio: dict) -> dict:
        sections = []
        for entry in portfolio["product_ranking"][:12]:
            review = self._reviews.latest(entry["product_id"])
            body = (review["executive_summary"] if review
                    else f"{entry['product']} has not been reviewed yet.")
            facts = []
            if review:
                facts = ([s["strength"] for s in review["strengths"][:2]]
                         + [w["weakness"] for w in review["weaknesses"][:2]])
            sections.append({"heading": f"{entry['rank']}. {entry['product']} "
                                        f"— {_fmt(entry['health_score'])}/100",
                             "body": body, "facts": facts})
        return {
            "headline": f"Monthly product review across "
                        f"{portfolio['coverage']['products']} product(s); "
                        f"{portfolio['coverage']['measured']} measured.",
            "sections": sections or [{"heading": "No products",
                                      "body": "The catalogue is empty.",
                                      "facts": []}],
            "confidence": portfolio["portfolio_health"].get("confidence", 0.0),
            "coverage": portfolio["coverage"],
        }

    def _quarterly_strategy(self, portfolio: dict) -> dict:
        priorities = portfolio["investment_priorities"]
        recommendations = self._strategy.recommendations(status="open",
                                                         limit=10)
        return {
            "headline": f"Quarterly strategy: "
                        f"{priorities.get('invest', 0)} product(s) to invest "
                        f"in, {priorities.get('fix', 0)} to fix, "
                        f"{priorities.get('question', 0)} to question.",
            "sections": [
                {"heading": "Portfolio shape",
                 "body": "Products by lifecycle stage.",
                 "facts": [f"{stage}: {count}" for stage, count in
                           portfolio["coverage"]["by_lifecycle"].items()]},
                {"heading": "Investment priorities",
                 "body": "Every product, by the stated investment rule.",
                 "facts": [f"{p['product']}: {p['investment_priority']} — "
                           f"{p['priority_reason']}"
                           for p in portfolio["product_ranking"][:10]]},
                {"heading": "Strategic plays",
                 "body": "Recommendations derived from measured evidence.",
                 "facts": [f"{r['recommendation']} "
                           f"(priority {r['priority']}, {r['estimated_effort']} "
                           f"effort, {r['confidence']:.0%} confidence)"
                           for r in recommendations] or
                          ["No strategic plays are evidenced yet."]},
            ],
            "confidence": portfolio["portfolio_health"].get("confidence", 0.0),
            "coverage": portfolio["coverage"],
        }

    def _risk_summary(self, portfolio: dict) -> dict:
        risk = portfolio["portfolio_risk"]
        at_risk = [p for p in portfolio["product_ranking"]
                   if p["band"] == "at_risk"]
        return {
            "headline": f"Portfolio risk is {risk['band']}: "
                        f"{risk['products_at_risk']} product(s) at risk, "
                        f"{risk['declining_products']} declining.",
            "sections": [
                {"heading": "Top risks", "body": "Ranked by evidence strength.",
                 "facts": [f"{r['finding']} ({r['confidence']:.0%} confidence)"
                           for r in portfolio["top_risks"]] or
                          ["No risks are evidenced."]},
                {"heading": "Products at risk",
                 "body": "Health below the watch threshold.",
                 "facts": [f"{p['product']}: {_fmt(p['health_score'])}/100 — "
                           f"{p['priority_reason']}" for p in at_risk] or
                          ["No product is below the watch threshold."]},
                {"heading": "Structural risk",
                 "body": "Concentration and cannibalization.",
                 "facts": [f"Concentration signals: {risk['concentration']}",
                           f"Cannibalization signals: "
                           f"{risk['cannibalization_signals']}"]},
            ],
            "confidence": portfolio["portfolio_health"].get("confidence", 0.0),
            "coverage": portfolio["coverage"],
        }

    def _growth_summary(self, portfolio: dict) -> dict:
        growth = portfolio["portfolio_growth"]
        return {
            "headline": f"Portfolio growth is {growth['band']}: "
                        f"{growth['growing_products']} product(s) growing, "
                        f"{growth['opportunities']} opportunit(y/ies) open.",
            "sections": [
                {"heading": "Top opportunities",
                 "body": "Ranked by evidence strength.",
                 "facts": [f"{o['finding']} ({o['confidence']:.0%} confidence)"
                           for o in portfolio["top_opportunities"]] or
                          ["No growth opportunities are evidenced."]},
                {"heading": "Emerging trends",
                 "body": "Sustained trends the analytics detected.",
                 "facts": [f"{growth['emerging_trends']} trend signal(s) "
                           f"across the portfolio",
                           f"{growth['cross_sell']} cross-sell opportunit"
                           f"(y/ies) into proven audiences"]},
                {"heading": "Growth leaders",
                 "body": "Products with the strongest measured growth.",
                 "facts": [f"{p['product']}: growth "
                           f"{_fmt(p['growth_score'])}/100"
                           for p in portfolio["product_ranking"][:5]
                           if isinstance(p.get("growth_score"), (int, float))]
                          or ["No product carries growth evidence."]},
            ],
            "confidence": portfolio["portfolio_health"].get("confidence", 0.0),
            "coverage": portfolio["coverage"],
        }

    def _decision_pack(self, portfolio: dict) -> dict:
        """What is waiting on a human, with the case for each — read from the
        Action Queue that already holds them."""
        pending = []
        if self._queue is not None:
            pending = self._queue.pending_approvals(limit=20)
        recommendations = self._strategy.recommendations(status="open",
                                                         limit=10)
        return {
            "headline": f"{len(pending)} decision(s) await approval; "
                        f"{len(recommendations)} strategic recommendation(s) "
                        f"are open.",
            "sections": [
                {"heading": "Awaiting your approval",
                 "body": "Queued by the platform; nothing executes without "
                         "you.",
                 "facts": [f"{a['title']} ({a['kind'].replace('_', ' ')}, "
                           f"priority {a['priority']})" for a in pending] or
                          ["Nothing is waiting on you."]},
                {"heading": "Recommended decisions",
                 "body": "Each carries impact, effort, and evidence.",
                 "facts": [f"{r['recommendation']} — impact: "
                           f"{r['business_impact']} "
                           f"({r['estimated_effort']} effort)"
                           for r in recommendations] or
                          ["No recommendations are open."]},
                {"heading": "Portfolio context",
                 "body": "The position these decisions are made in.",
                 "facts": [f"Health "
                           f"{_fmt(portfolio['portfolio_health']['score'])}"
                           f"/100",
                           f"{portfolio['portfolio_risk']['products_at_risk']} "
                           f"product(s) at risk"]},
            ],
            "confidence": portfolio["portfolio_health"].get("confidence", 0.0),
            "coverage": portfolio["coverage"],
        }

    def _announce(self, brief: dict) -> None:
        if self._bus is None:
            return
        try:
            self._bus.publish("ReportGenerated", {
                "kind": brief["kind"], "title": brief["title"],
                "brief_id": brief["brief_id"],
                "confidence": brief["confidence"]},
                source="executive_briefs")
        except Exception:  # noqa: BLE001
            logger.exception("Brief event publication failed")

    # ---------------------------------------------------------------- read
    def briefs(self, kind: str = "", limit: int = 20) -> list[dict]:
        items = self._store.read("briefs")
        if kind:
            items = [b for b in items if b["kind"] == kind]
        return list(reversed(items))[:limit]

    def latest(self, kind: str) -> dict | None:
        found = self.briefs(kind=kind, limit=1)
        return found[0] if found else None

    @staticmethod
    def kinds() -> list[dict]:
        return [{"kind": k, "title": _TITLES[k]} for k in BRIEF_KINDS]


_TITLES = {
    "board_brief": "Board Brief",
    "monthly_review": "Monthly Product Review",
    "quarterly_strategy": "Quarterly Strategy Review",
    "risk_summary": "Risk Summary",
    "growth_summary": "Growth Summary",
    "decision_pack": "Executive Decision Pack",
}

# Same convention as the Report Generation Module: a Jinja template over the
# structured document, so the JSON stays the source and the Markdown is a view.
_TEMPLATE = Template("""# {{ b.title }}
_Generated {{ b.generated_at }} · confidence {{ '%.0f%%' % (b.confidence * 100) }} · {{ b.coverage.measured }}/{{ b.coverage.products }} product(s) measured_

{{ b.headline }}
{% for s in b.sections %}
## {{ s.heading }}
{{ s.body }}
{% for f in s.facts %}
- {{ f }}
{%- endfor %}
{% endfor %}
---
_Every statement above is derived from measured evidence. Where the platform
holds no evidence, the section says so rather than estimating._
""")


def _render(brief: dict) -> str:
    return _TEMPLATE.render(b=brief).strip()


def _fmt(score: float | None) -> str:
    return "—" if score is None else f"{score:.0f}"


def _headline(health: dict, growth: dict, risk: dict, coverage: dict) -> str:
    if health["score"] is None:
        return (f"The portfolio holds {coverage['products']} product(s), none "
                f"measurable yet — connect product data to make the portfolio "
                f"assessable.")
    return (f"Portfolio health is {health['score']:.0f}/100 ({health['band']}), "
            f"growth is {growth['band']}, risk is {risk['band']}. "
            f"{coverage['measured']} of {coverage['products']} product(s) "
            f"carry enough evidence to be scored.")

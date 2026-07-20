"""Product Intelligence Layer — composition root and runtime integration.

Assembles the catalogue, health, growth, strategy, reviews, KPI intelligence,
scenarios, portfolio intelligence, and briefs, then registers refresh jobs on
the **existing** Enterprise Scheduler. No new scheduler, no new event bus, no
new approval path: this layer sits above the Enterprise Brain and consumes the
runtime that is already there.

Jobs:

    startup_products      build the catalogue from the Organizational Model
    product_health        re-score every product (interval)
    product_intelligence  growth findings → strategic recommendations →
                          reviews (interval; the layer's heartbeat)
    kpi_monitor           watch KPI thresholds and raise work (interval)
    refresh_on_knowledge  knowledge synchronized → recalculate (event)
    refresh_on_report     an analysis produced a report → recalculate (event)
    refresh_on_portfolio  portfolio moved → recalculate (event)
    board_brief           the weekly board brief (cron)
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.product.briefs import ExecutiveBriefGenerator
from app.product.catalog import ProductCatalog
from app.product.evidence import EvidenceGatherer
from app.product.growth import GrowthIntelligenceEngine
from app.product.health import ProductHealthEngine
from app.product.kpis import KPIIntelligence
from app.product.portfolio import PortfolioIntelligence
from app.product.reviews import ProductReviewEngine
from app.product.scenarios import ScenarioSimulation
from app.product.store import ProductStore
from app.product.strategy import StrategicRecommendationEngine

logger = get_logger(__name__)


class ProductIntelligenceLayer:
    """The Enterprise Product Manager, assembled over the Enterprise Brain."""

    def __init__(self, settings, store, knowledge, sync=None, tasks=None,
                 notifications=None, reviews_center=None):
        self.settings = settings
        self.store = ProductStore(settings.product_dir)
        self.gatherer = EvidenceGatherer(store, knowledge)

        organization = getattr(sync, "organization", None)
        relationships = getattr(sync, "relationships", None)
        self.catalog = ProductCatalog(
            self.store, organization=organization,
            relationships=relationships, knowledge=knowledge,
            artifacts=store)
        self.health = ProductHealthEngine(self.store, self.catalog,
                                          self.gatherer)
        self.growth = GrowthIntelligenceEngine(self.catalog, self.health,
                                               self.gatherer)
        self.strategy = StrategicRecommendationEngine(
            self.store, self.catalog, self.health, self.growth, self.gatherer)
        self.reviews = ProductReviewEngine(self.store, self.catalog,
                                           self.health, self.growth,
                                           self.strategy,
                                           reviews_center=reviews_center)
        self.kpis = KPIIntelligence(self.store, self.catalog, self.health,
                                    self.gatherer, tasks=tasks,
                                    notifications=notifications)
        self.scenarios = ScenarioSimulation(self.store, self.catalog,
                                            self.gatherer)
        self.portfolio = PortfolioIntelligence(self.catalog, self.health,
                                               self.growth, self.strategy)
        self.briefs = ExecutiveBriefGenerator(
            self.store, self.portfolio, self.catalog, self.health,
            self.growth, self.strategy, self.reviews)
        self._bus = None

    # ------------------------------------------------------------- wiring
    def attach_runtime(self, bus, decisions=None, queue=None) -> None:
        """Connect to the autonomy runtime: announce on its bus, route
        recommendations through its Decision Engine, and read its Action
        Queue for the decision pack. Called by the runtime, which owns all
        three — this layer is built before it."""
        self._bus = bus
        for component in (self.catalog, self.health, self.growth,
                          self.strategy, self.reviews, self.kpis,
                          self.scenarios, self.portfolio, self.briefs):
            component.attach_bus(bus)
        if decisions is not None:
            self.strategy.attach_decisions(decisions)
        if queue is not None:
            self.briefs.attach_queue(queue)

    def register_jobs(self, scheduler, JobDefinition, RetryPolicy) -> None:
        """Register product work on the existing Enterprise Scheduler. The
        classes are passed in so this layer never imports the runtime."""
        settings = self.settings
        retry = RetryPolicy(attempts=2, backoff_seconds=5.0)

        scheduler.register(JobDefinition(
            "startup_products",
            "Build the product catalogue from the organizational model",
            "startup", self.build_catalog, retry=retry,
            tags=["startup", "product"]))
        scheduler.register(JobDefinition(
            "product_health", "Re-score every product against the evidence",
            "interval", self.health.evaluate_all,
            interval_seconds=settings.product_health_interval_seconds,
            depends_on=["startup_products"], retry=retry,
            tags=["product", "health"]))
        scheduler.register(JobDefinition(
            "product_intelligence",
            "Refresh growth findings, strategy, and product reviews",
            "interval", self.refresh,
            interval_seconds=settings.product_refresh_interval_seconds,
            depends_on=["product_health"], retry=RetryPolicy(attempts=1),
            tags=["product", "strategy"]))
        scheduler.register(JobDefinition(
            "kpi_monitor", "Watch business KPIs against their thresholds",
            "interval", self.kpis.monitor,
            interval_seconds=settings.product_kpi_interval_seconds,
            depends_on=["product_health"], retry=retry,
            tags=["product", "kpi"]))

        # Recalculate when the facts beneath the products move. These are the
        # SDS triggers: knowledge synchronization, analytics completion,
        # forecast completion, portfolio updates.
        for name, event, description in (
                ("refresh_on_knowledge", "KnowledgeUpdated",
                 "Recalculate product intelligence after knowledge "
                 "synchronization"),
                ("refresh_on_report", "ReportGenerated",
                 "Recalculate product intelligence after an analysis "
                 "completes"),
                ("refresh_on_portfolio", "PortfolioChanged",
                 "Recalculate product intelligence after the portfolio "
                 "moves")):
            scheduler.register(JobDefinition(
                name, description, "event", self.recalculate, event=event,
                retry=retry, tags=["product", "event"]))

        scheduler.register(JobDefinition(
            "board_brief", "Generate the board brief",
            "cron", lambda: self.briefs.generate("board_brief"),
            cron=settings.product_brief_cron, retry=retry,
            tags=["product", "brief"]))

    # --------------------------------------------------------------- jobs
    def build_catalog(self) -> dict[str, Any]:
        """Discover products from the organizational model and resolve their
        KPIs, reports, and relationships."""
        discovered = self.catalog.sync_from_organization()
        attached = self.catalog.sync_kpis_and_reports()
        return {**discovered, **attached, "products": self.catalog.stats()}

    def refresh(self) -> dict[str, Any]:
        """The layer's heartbeat: growth → strategy → reviews."""
        growth = self.growth.analyse()
        strategy = self.strategy.generate()
        reviews = self.reviews.review_all()
        return {"findings": growth["by_kind"],
                "recommendations": strategy["generated"],
                "routed": strategy["routed_to_decisions"],
                "reviews": reviews["reviewed"]}

    def recalculate(self) -> dict[str, Any]:
        """Full recalculation after the underlying facts changed: the
        catalogue may have new products, and every score rests on evidence
        that just moved."""
        catalog = self.build_catalog()
        health = self.health.evaluate_all()
        refreshed = self.refresh()
        kpis = self.kpis.monitor()
        return {"catalog": catalog.get("products", {}),
                "health": health, "intelligence": refreshed,
                "kpis_breached": kpis["kpis_breached"]}

    # ------------------------------------------------------------- status
    def status(self) -> dict[str, Any]:
        """Runtime status for the product intelligence layer."""
        return {
            "catalog": self.catalog.stats(),
            "health": {
                "evaluated": len(self.health.all_health()),
                "unscored": sum(1 for h in self.health.all_health()
                                if h["health_score"] is None),
            },
            "recommendations": self.strategy.stats(),
            "kpi_alerts": len(self.kpis.alerts(limit=500)),
            "reviews": len(self.reviews.reviews(limit=500)),
        }

    def overview(self) -> dict[str, Any]:
        """The executive product view — business framing only, no internals."""
        portfolio = self.portfolio.evaluate()
        catalog = self.catalog.stats()
        return {
            "products": {
                "total": catalog["total"], "active": catalog["active"],
                "by_lifecycle": catalog["by_lifecycle"],
                "measured": portfolio["coverage"]["measured"],
                "unmeasured": portfolio["coverage"]["unmeasured"],
            },
            "portfolio_health": portfolio["portfolio_health"],
            "portfolio_growth": portfolio["portfolio_growth"],
            "portfolio_risk": portfolio["portfolio_risk"],
            "top_products": portfolio["product_ranking"][:5],
            "attention": [p for p in portfolio["product_ranking"]
                          if p["investment_priority"] in ("fix", "question")
                          ][:5],
            "top_opportunities": portfolio["top_opportunities"][:3],
            "top_risks": portfolio["top_risks"][:3],
            "open_recommendations": self.strategy.recommendations(
                status="open", limit=5),
            "kpi_alerts": self.kpis.alerts(limit=5),
        }

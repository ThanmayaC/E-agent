"""Product Intelligence & Strategic Decision Layer.

The layer that turns an autonomous enterprise platform into an Enterprise
Product Manager. It sits **above** the Enterprise Brain and consumes it —
it computes no analytics, trains no models, and stores no facts of its own.

    evidence        the facts a product judgement may stand on, gathered from
                    existing artifacts — the guard that keeps this layer
                    evidence-based rather than imaginative
    catalog         enterprise products, with relationships resolved from the
                    Organizational Model
    health          eight evidence-based scores per product
    growth          opportunities, decline, trends, cannibalization,
                    cross-sell, gaps, expansion
    reviews         structured, cited product reviews
    strategy        business recommendations, routed through the existing
                    Decision Engine for approval
    kpis            business/growth/operational/portfolio KPI monitoring
    scenarios       deterministic what-if over existing forecasts
    portfolio       portfolio health, risk, growth, ranking, investment
    briefs          board brief, reviews, strategy, risk, growth, decisions
    product_runtime composition root, wired into the autonomy runtime's jobs
"""
from app.product.briefs import BRIEF_KINDS, ExecutiveBriefGenerator
from app.product.catalog import LIFECYCLES, ProductCatalog
from app.product.evidence import EvidenceGatherer, ProductEvidence
from app.product.growth import FINDING_KINDS, GrowthIntelligenceEngine
from app.product.health import DIMENSIONS, ProductHealthEngine
from app.product.kpis import CATEGORIES, KPIIntelligence
from app.product.portfolio import PRIORITIES, PortfolioIntelligence
from app.product.product_runtime import ProductIntelligenceLayer
from app.product.reviews import ProductReviewEngine
from app.product.scenarios import LEVERS, ScenarioSimulation
from app.product.store import ProductStore
from app.product.strategy import PLAYS, StrategicRecommendationEngine

__all__ = [
    "BRIEF_KINDS", "CATEGORIES", "DIMENSIONS", "FINDING_KINDS", "LEVERS",
    "LIFECYCLES", "PLAYS", "PRIORITIES", "EvidenceGatherer",
    "ExecutiveBriefGenerator", "GrowthIntelligenceEngine", "KPIIntelligence",
    "PortfolioIntelligence", "ProductCatalog", "ProductEvidence",
    "ProductHealthEngine", "ProductIntelligenceLayer", "ProductReviewEngine",
    "ProductStore", "ScenarioSimulation", "StrategicRecommendationEngine",
]

"""Analytics Module (SDS §2.2).

Deterministic analytics — facts only, no narrative: KPI discovery, the
DuckDB analytics warehouse with dimension breakdowns, statistical signal
detection (trends, anomalies, seasonality, Pareto, correlations), and data
quality assessment.
"""
from app.intelligence.analytics.engine import AnalyticsEngine
from app.intelligence.analytics.signals import SignalEngine
from app.intelligence.kpi.discovery import KPIDiscovery
from app.intelligence.quality.engine import QualityEngine

__all__ = ["AnalyticsEngine", "SignalEngine", "KPIDiscovery", "QualityEngine"]

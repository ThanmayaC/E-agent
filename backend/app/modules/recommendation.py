"""Recommendation Module (SDS §2.7).

Deterministic, rule-derived recommendations that cite the evidence that
triggered them (data quality, forecast confidence, anomalies, missing
dimensions). Business-strategy recommendations are LLM-narrated by the
reasoning layer but always grounded in verified evidence.
"""
from app.intelligence.recommendations.engine import RecommendationEngine

__all__ = ["RecommendationEngine"]

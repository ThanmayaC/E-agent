"""Executive Intelligence layer (V3.1).

Connects the intelligence the Enterprise Brain already holds — the ingested
NPCI UPI corpus, its KPI workbooks, decisions, incidents, RCAs, SOPs and
reports — into executive-grade outputs: a daily brief, Monday-morning
priorities, ranked recommendations, KPI intelligence, and enhanced/ranked
decisions. It adds no data and changes no Brain architecture; it reads what
exists and reasons over it deterministically.
"""
from app.executive.ecosystem import EcosystemIntelligence, EcosystemReader
from app.executive.evolution import EvolutionIntelligence
from app.executive.intelligence import ExecutiveIntelligence
from app.executive.reader import EnterpriseReader

__all__ = ["ExecutiveIntelligence", "EnterpriseReader",
           "EcosystemIntelligence", "EcosystemReader",
           "EvolutionIntelligence"]

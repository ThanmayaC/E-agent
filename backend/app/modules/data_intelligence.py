"""Data Intelligence Module (SDS §2.1).

Business understanding of observed data: semantic meaning (ontology + fuzzy
+ embedding matching), duplicate/partition merging, business relationship
discovery, confidence scoring with clarification generation, and business
context generation (the compact factual JSON reasoning agents consume).
"""
from app.intelligence.confidence.assessor import ConfidenceAssessor
from app.intelligence.context.builder import BusinessContextBuilder
from app.intelligence.dedup.merger import DatasetMerger
from app.intelligence.relationships.detector import RelationshipDetector
from app.intelligence.semantics.meaning import MeaningDetector

__all__ = ["ConfidenceAssessor", "BusinessContextBuilder", "DatasetMerger",
           "RelationshipDetector", "MeaningDetector"]

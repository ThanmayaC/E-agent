"""Automatic relationship detection across datasets.

Detects foreign keys, shared dimensions, and date alignments even when column
names differ, using concept equality, name similarity, and value overlap.
"""
from __future__ import annotations

import uuid
from difflib import SequenceMatcher

import pandas as pd

from app.domain.entities import Relationship, TableProfile
from app.domain.enums import BusinessConcept, Cardinality, ColumnRole, RelationshipType, SemanticType


class RelationshipDetector:
    def __init__(self, overlap_threshold: float = 0.60, sample_size: int = 20000):
        self.overlap_threshold = overlap_threshold
        self.sample_size = sample_size

    def detect(
        self,
        profiles: list[TableProfile],
        frames: dict[str, pd.DataFrame],
    ) -> list[Relationship]:
        rels: list[Relationship] = []
        for i, left in enumerate(profiles):
            for right in profiles[i + 1:]:
                rels.extend(self._pairwise(left, right, frames))
        # FK columns get their role updated
        fk_cols = {(r.from_dataset, r.from_column) for r in rels if r.rel_type == RelationshipType.FOREIGN_KEY}
        for p in profiles:
            for c in p.columns:
                if (p.dataset_id, c.name) in fk_cols and c.role != ColumnRole.PRIMARY_KEY:
                    c.role = ColumnRole.FOREIGN_KEY
        return rels

    # ------------------------------------------------------------ internal
    def _pairwise(self, a: TableProfile, b: TableProfile, frames: dict[str, pd.DataFrame]) -> list[Relationship]:
        rels: list[Relationship] = []
        for ca in a.columns:
            for cb in b.columns:
                candidate = self._match_score(ca, cb)
                if candidate == 0:
                    continue
                overlap = self._value_overlap(frames.get(a.dataset_id), frames.get(b.dataset_id), ca.name, cb.name)
                if overlap is None:
                    continue
                if ca.semantic_type in (SemanticType.DATE, SemanticType.DATETIME):
                    if overlap >= 0.3:
                        rels.append(self._make(a, ca, b, cb, RelationshipType.DATE_ALIGNMENT, overlap,
                                               candidate * 0.6 + overlap * 0.3, "shared time axis"))
                    continue
                if overlap < self.overlap_threshold:
                    continue
                rel_type, card = self._type_and_cardinality(ca, cb)
                confidence = round(min(0.99, candidate * 0.45 + overlap * 0.55), 3)
                evidence = f"name similarity + {overlap:.0%} value overlap"
                if ca.concept == cb.concept and ca.concept is not BusinessConcept.UNKNOWN:
                    evidence = f"both map to concept '{ca.concept.value}', {overlap:.0%} value overlap"
                rels.append(self._make(a, ca, b, cb, rel_type, overlap, confidence, evidence, card))
        return self._dedupe(rels)

    @staticmethod
    def _match_score(ca, cb) -> float:
        """0 = not a candidate; otherwise a prior in (0, 1]."""
        joinable = {SemanticType.IDENTIFIER, SemanticType.CODE, SemanticType.CATEGORY,
                    SemanticType.GEO, SemanticType.DATE, SemanticType.DATETIME, SemanticType.STATUS}
        if ca.semantic_type not in joinable or cb.semantic_type not in joinable:
            return 0.0
        if ca.concept is not BusinessConcept.UNKNOWN and ca.concept == cb.concept:
            return 1.0
        name_sim = SequenceMatcher(None, ca.normalized_name, cb.normalized_name).ratio()
        if name_sim >= 0.75:
            return name_sim
        # different names, same type family: allow value overlap to decide, weak prior
        if ca.semantic_type == cb.semantic_type and ca.semantic_type in (SemanticType.IDENTIFIER, SemanticType.CODE):
            return 0.4
        return 0.0

    def _value_overlap(self, df_a, df_b, col_a: str, col_b: str) -> float | None:
        if df_a is None or df_b is None or col_a not in df_a or col_b not in df_b:
            return None
        va = set(df_a[col_a].dropna().astype(str).str.strip().head(self.sample_size))
        vb = set(df_b[col_b].dropna().astype(str).str.strip().head(self.sample_size))
        if not va or not vb:
            return None
        smaller, larger = (va, vb) if len(va) <= len(vb) else (vb, va)
        return len(smaller & larger) / len(smaller)  # containment, robust to size skew

    @staticmethod
    def _type_and_cardinality(ca, cb) -> tuple[RelationshipType, Cardinality]:
        if ca.is_pk_candidate and cb.is_pk_candidate:
            return RelationshipType.FOREIGN_KEY, Cardinality.ONE_TO_ONE
        if ca.is_pk_candidate or cb.is_pk_candidate:
            return RelationshipType.FOREIGN_KEY, Cardinality.ONE_TO_MANY
        if ca.semantic_type in (SemanticType.CATEGORY, SemanticType.GEO, SemanticType.STATUS):
            return RelationshipType.SHARED_DIMENSION, Cardinality.MANY_TO_MANY
        return RelationshipType.FOREIGN_KEY, Cardinality.MANY_TO_MANY

    def _make(self, a, ca, b, cb, rel_type, overlap, confidence, evidence,
              card: Cardinality = Cardinality.MANY_TO_MANY) -> Relationship:
        # orient FK edges: "many" side points to "one" side
        if rel_type == RelationshipType.FOREIGN_KEY and cb.is_pk_candidate and not ca.is_pk_candidate:
            src, sc, dst, dc = a, ca, b, cb
        elif rel_type == RelationshipType.FOREIGN_KEY and ca.is_pk_candidate and not cb.is_pk_candidate:
            src, sc, dst, dc = b, cb, a, ca
        else:
            src, sc, dst, dc = a, ca, b, cb
        return Relationship(
            id=uuid.uuid4().hex[:12],
            from_dataset=src.dataset_id, from_column=sc.name,
            to_dataset=dst.dataset_id, to_column=dc.name,
            rel_type=rel_type, cardinality=card,
            overlap=round(overlap, 3), confidence=round(confidence, 3), evidence=evidence,
        )

    @staticmethod
    def _dedupe(rels: list[Relationship]) -> list[Relationship]:
        """Keep only the strongest edge per dataset pair per type."""
        best: dict[tuple, Relationship] = {}
        for r in rels:
            key = (r.from_dataset, r.to_dataset, r.rel_type)
            if key not in best or r.confidence > best[key].confidence:
                best[key] = r
        return list(best.values())

"""Business meaning detection.

Maps every column to a business concept using the ontology:
exact alias match → token match → fuzzy match → semantic-similarity match
(embeddings). Also classifies each table as fact/dimension and assigns its
dominant entity.

The embeddings tier lets the platform recognize column names that share no
tokens with any alias (e.g. "purchaser" → Customer) — the semantic-similarity
requirement — while the deterministic tiers above keep confident matches
exact and stable. It is optional: without an embedder the detector behaves
exactly as the lexical-only version did.
"""
from __future__ import annotations

from difflib import SequenceMatcher
from typing import TYPE_CHECKING

from app.domain.entities import ColumnProfile, SemanticMapping, TableProfile
from app.domain.enums import BusinessConcept, ColumnRole, SemanticType
from app.intelligence.profiling.profiler import normalize_name
from app.intelligence.semantics.ontology import CONCEPT_ALIASES, ENTITY_CONCEPTS, METRIC_CONCEPTS

if TYPE_CHECKING:
    from app.intelligence.embeddings.embedder import Embedder


class MeaningDetector:
    def __init__(self, fuzzy_threshold: float = 0.82,
                 embedder: "Embedder | None" = None,
                 semantic_threshold: float = 0.60):
        self.fuzzy_threshold = fuzzy_threshold
        self.embedder = embedder
        self.semantic_threshold = semantic_threshold
        # flatten alias -> concept for O(1) exact lookups
        self._alias_index: dict[str, BusinessConcept] = {}
        for concept, aliases in CONCEPT_ALIASES.items():
            for alias in aliases:
                self._alias_index.setdefault(normalize_name(alias), concept)
        # lazily-built alias embedding matrix for the semantic tier
        self._alias_vectors: list[list[float]] | None = None
        self._alias_concepts: list[BusinessConcept] = []

    # ---------------------------------------------------------------- API
    def annotate(self, tables: list[TableProfile]) -> list[SemanticMapping]:
        mappings: list[SemanticMapping] = []
        for table in tables:
            for col in table.columns:
                concept, confidence = self.detect(col)
                col.concept = concept
                col.concept_confidence = round(confidence, 3)
                mappings.append(SemanticMapping(
                    dataset_id=table.dataset_id,
                    column=col.name,
                    concept=concept,
                    semantic_type=col.semantic_type,
                    role=col.role,
                    canonical_name=self._canonical(col, concept),
                    confidence=round(confidence, 3),
                ))
            self._classify_table(table)
        return mappings

    # ----------------------------------------------------------- column
    def detect(self, col: ColumnProfile) -> tuple[BusinessConcept, float]:
        name = col.normalized_name

        if name in self._alias_index:
            return self._alias_index[name], 0.98

        # token containment: "merchant_txn_value" contains alias "txn_value"
        best, best_score = BusinessConcept.UNKNOWN, 0.0
        tokens = set(name.split("_"))
        for alias, concept in self._alias_index.items():
            alias_tokens = set(alias.split("_"))
            if alias_tokens <= tokens:
                score = 0.85 + 0.1 * (len(alias_tokens) / max(len(tokens), 1))
                if score > best_score:
                    best, best_score = concept, score
        if best is not BusinessConcept.UNKNOWN:
            return best, min(best_score, 0.95)

        # fuzzy: cid ~ cust_id
        for alias, concept in self._alias_index.items():
            ratio = SequenceMatcher(None, name, alias).ratio()
            if ratio >= self.fuzzy_threshold and ratio > best_score:
                best, best_score = concept, ratio * 0.85

        if best is not BusinessConcept.UNKNOWN:
            return best, best_score

        # semantic similarity (embeddings): catches names that share no tokens
        # with any alias. Softer signal than the lexical tiers, so it is scored
        # below them and only fires when clearly above the configured threshold.
        concept, sim = self._semantic_match(name)
        if concept is not BusinessConcept.UNKNOWN:
            return concept, round(sim * 0.9, 3)

        # type-driven fallback
        if col.semantic_type in (SemanticType.DATE, SemanticType.DATETIME):
            return BusinessConcept.DATE, 0.6
        if col.semantic_type == SemanticType.CURRENCY:
            return BusinessConcept.REVENUE, 0.5
        if col.semantic_type == SemanticType.STATUS:
            return BusinessConcept.STATUS, 0.6
        if col.semantic_type == SemanticType.GEO:
            return BusinessConcept.REGION, 0.6
        return BusinessConcept.UNKNOWN, 0.0

    # ------------------------------------------------------- semantic tier
    def _ensure_alias_vectors(self) -> None:
        """Embed every ontology alias once (cheap; ~300 short strings), keeping
        the concept each vector votes for. Vectors are L2-normalized by the
        embedder, so cosine similarity is a plain dot product."""
        if self._alias_vectors is not None or self.embedder is None:
            return
        aliases, concepts = [], []
        for concept, alias_list in CONCEPT_ALIASES.items():
            for alias in alias_list:
                aliases.append(alias.replace("_", " "))
                concepts.append(concept)
        self._alias_vectors = self.embedder.embed(aliases)
        self._alias_concepts = concepts

    def _semantic_match(self, name: str) -> tuple[BusinessConcept, float]:
        if self.embedder is None:
            return BusinessConcept.UNKNOWN, 0.0
        # very short names carry almost no semantic signal and are prone to
        # spurious similarity (especially with hashing embedders) — the exact
        # and fuzzy alias tiers already handle known short codes like "mid"
        if len(name) < 4:
            return BusinessConcept.UNKNOWN, 0.0
        self._ensure_alias_vectors()
        if not self._alias_vectors:
            return BusinessConcept.UNKNOWN, 0.0
        query = self.embedder.embed([name.replace("_", " ")])[0]
        best, best_sim = BusinessConcept.UNKNOWN, 0.0
        for vec, concept in zip(self._alias_vectors, self._alias_concepts):
            sim = sum(a * b for a, b in zip(query, vec))
            if sim > best_sim:
                best, best_sim = concept, sim
        if best_sim >= self.semantic_threshold:
            return best, best_sim
        return BusinessConcept.UNKNOWN, 0.0

    @staticmethod
    def _canonical(col: ColumnProfile, concept: BusinessConcept) -> str:
        if concept is BusinessConcept.UNKNOWN:
            return col.normalized_name
        if col.role == ColumnRole.PRIMARY_KEY or col.semantic_type == SemanticType.IDENTIFIER:
            return f"{concept.value} Identifier"
        if col.role == ColumnRole.MEASURE:
            return f"{concept.value} (Metric)"
        if col.role == ColumnRole.TIME_DIMENSION:
            return "Time Dimension"
        return concept.value

    # ------------------------------------------------------------ table
    @staticmethod
    def _classify_table(table: TableProfile) -> None:
        measures = [c for c in table.columns if c.role == ColumnRole.MEASURE]
        dates = [c for c in table.columns if c.role == ColumnRole.TIME_DIMENSION]
        pks = [c for c in table.columns if c.is_pk_candidate]

        table.is_fact = bool(measures) and (bool(dates) or table.row_count > 500)
        table.is_dimension = bool(pks) and not table.is_fact

        entity_votes: dict[BusinessConcept, float] = {}
        for c in table.columns:
            if c.concept in ENTITY_CONCEPTS:
                weight = 2.0 if c.is_pk_candidate else 1.0
                entity_votes[c.concept] = entity_votes.get(c.concept, 0) + weight * c.concept_confidence
        if entity_votes:
            table.entity = max(entity_votes, key=entity_votes.get)  # type: ignore[arg-type]

        if dates:
            table.time_column = dates[0].name
        if pks:
            table.primary_key = pks[0].name

        known = sum(1 for c in table.columns if c.concept is not BusinessConcept.UNKNOWN)
        table.confidence = round(known / max(len(table.columns), 1), 3)
        role = "fact" if table.is_fact else ("dimension" if table.is_dimension else "reference")
        metric_names = sorted({c.concept.value for c in measures if c.concept in METRIC_CONCEPTS})
        table.description = (
            f"{role.title()} table for {table.entity.value}"
            + (f" with metrics: {', '.join(metric_names)}" if metric_names else "")
            + (f", tracked over time ({table.time_column})" if table.time_column else "")
        )

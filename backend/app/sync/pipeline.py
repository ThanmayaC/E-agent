"""Knowledge Refresh Pipeline — data changed, so knowledge changes.

    Synchronize → Observation → Knowledge Update → Memory Update
      → Relationship Update → Embeddings Update → Enterprise Context Update
      → Ready

The pipeline is **incremental by construction**. Nothing here rebuilds: each
stage consumes the sync delta and touches only what moved. A refresh with an
empty delta short-circuits to ``ready`` having done no work, which is what
lets this run every hour against every connected system.

History is preserved, never overwritten: the Knowledge Store journals every
mutation (``knowledge_versions``), entities carry their own history, and
relationships accumulate observations. A refresh adds a version; it does not
replace the past.

Degradation is per-stage. A failing embeddings backend must not cost the
organization its knowledge update, so every stage records its own outcome and
the pipeline reports ``degraded`` rather than failing — the Enterprise Brain's
existing contract ("learning degrades, it never fails"), applied to sync.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.core.logging import get_logger
from app.sync.store import SyncStore, new_id, now_iso

logger = get_logger(__name__)

STAGES = ("synchronize", "observation", "document_intelligence",
          "knowledge_update", "memory_update", "relationship_update",
          "embeddings_update", "enterprise_context_update", "ready")

MAX_REFRESH_EVENTS = 200
# Embedding the whole organization on every refresh would be a rebuild. Only
# entities the refresh actually touched are re-embedded.
MAX_EMBED_PER_REFRESH = 500


@dataclass
class RefreshResult:
    refresh_id: str
    trigger: str
    status: str = "running"          # running | ready | degraded | failed
    stages: list[dict] = field(default_factory=list)
    changed_records: int = 0
    started_at: str = ""
    finished_at: str = ""

    def describe(self) -> dict:
        return {"refresh_id": self.refresh_id, "trigger": self.trigger,
                "status": self.status, "stages": self.stages,
                "changed_records": self.changed_records,
                "started_at": self.started_at, "finished_at": self.finished_at}


class KnowledgeRefreshPipeline:
    """Turns a synchronization into updated organizational knowledge."""

    def __init__(self, store: SyncStore, sync_engine, registry, organization,
                 relationships, knowledge, brain=None, artifacts=None,
                 embedder=None, vector_store_for=None, bus=None,
                 documents=None):
        self._store = store
        self._sync = sync_engine
        self._registry = registry
        self._org = organization
        self._relationships = relationships
        self._knowledge = knowledge
        self._brain = brain
        self._artifacts = artifacts
        self._embedder = embedder
        self._vector_store_for = vector_store_for
        self._bus = bus
        self._documents = documents  # DocumentIntelligence (V2), optional

    def attach_bus(self, bus) -> None:
        """Announce completed refreshes on the enterprise event bus."""
        self._bus = bus

    # ------------------------------------------------------------- refresh
    def refresh(self, source_id: str = "", trigger: str = "scheduled",
                force_full: bool = False) -> RefreshResult:
        """Run the pipeline. With ``source_id`` it refreshes one system;
        without, every system that is due."""
        result = RefreshResult(refresh_id=new_id("rfr"), trigger=trigger,
                               started_at=now_iso())

        # 1. Synchronize ---------------------------------------------------
        results = self._stage(result, "synchronize", lambda: self._synchronize(
            source_id, force_full))
        deltas, sources = _collect(results)
        result.changed_records = sum(
            d.changed_count for d in deltas) if deltas else 0

        if not deltas or result.changed_records == 0:
            # Nothing moved: the correct amount of work is none.
            self._stage(result, "ready",
                        lambda: {"skipped": "no changes to learn from"})
            result.status = "ready"
            return self._finish(result)

        # 2. Observation ---------------------------------------------------
        self._stage(result, "observation",
                    lambda: self._observe(sources, deltas))
        # 2b. Document Intelligence (V2) -------------------------------------
        self._stage(result, "document_intelligence",
                    lambda: self._process_documents(sources, deltas))
        # 3. Knowledge Update ----------------------------------------------
        self._stage(result, "knowledge_update",
                    lambda: self._update_knowledge(sources, result))
        # 4. Memory Update -------------------------------------------------
        self._stage(result, "memory_update", self._update_memory)
        # 5. Relationship Update -------------------------------------------
        self._stage(result, "relationship_update",
                    lambda: self._update_relationships(sources, deltas))
        # 6. Embeddings Update ---------------------------------------------
        self._stage(result, "embeddings_update", self._update_embeddings)
        # 7. Enterprise Context Update -------------------------------------
        self._stage(result, "enterprise_context_update", self._update_context)
        # 8. Ready ---------------------------------------------------------
        self._stage(result, "ready", lambda: {
            "entities": self._org.counts(),
            "relationships": self._relationships.stats()["total"]})

        failed = [s for s in result.stages if s["status"] == "failed"]
        result.status = "degraded" if failed else "ready"
        return self._finish(result)

    # -------------------------------------------------------------- stages
    def _synchronize(self, source_id: str, force_full: bool) -> Any:
        if source_id:
            return [self._sync.sync(source_id, force_full=force_full)]
        return [self._sync.sync(s["source_id"], force_full=force_full)
                for s in self._registry.due()]

    def _observe(self, sources: list[str], deltas: list) -> dict:
        """Observation: what entities do the changed records reveal?"""
        totals = {"discovered": 0, "updated": 0}
        for source_name, source_deltas in _by_source(sources, deltas):
            counts = self._org.observe_from_sync(source_name, source_deltas)
            totals["discovered"] += counts["discovered"]
            totals["updated"] += counts["updated"]
        return totals

    def _process_documents(self, sources: list[str], deltas: list) -> dict:
        """Document Intelligence: parse, chunk, embed, and version every new
        or updated document the sync just detected. Tabular sources pass
        through untouched — only 'documents' tables are consumed."""
        if self._documents is None:
            return {"skipped": "document intelligence disabled"}
        totals = {"ingested": 0, "updated": 0, "archived": 0, "failed": 0,
                  "chunks": 0}
        for source_name, source_deltas in _by_source(sources, deltas):
            if not any(d.table == "documents" for d in source_deltas):
                continue
            source = self._registry.by_name(source_name)
            if source is None:
                continue
            counts = self._documents.process_sync(source, source_deltas)
            for key in totals:
                totals[key] += counts.get(key, 0)
        return totals

    def _update_knowledge(self, sources: list[str],
                          result: RefreshResult) -> dict:
        """Knowledge Update: record what the organization now knows, and that
        it learned it. Entity definitions are written by the organizational
        model's mirror; this stage records the learning event that makes the
        refresh auditable — the same contract the Brain uses after analysis."""
        self._knowledge.record_learning_event(
            "knowledge_synchronization", source="sync_pipeline",
            details={"refresh_id": result.refresh_id,
                     "sources": sources,
                     "changed_records": result.changed_records,
                     "entities": self._org.counts()})
        return {"learning_event": "recorded",
                "knowledge_versions":
                    self._knowledge.stats().get("knowledge_versions", 0)}

    def _update_memory(self) -> dict:
        """Memory Update: organizational memory reflects the new model."""
        if self._brain is None:
            return {"skipped": "brain disabled"}
        return {"memory": self._brain.synchronizer.stats()}

    def _update_relationships(self, sources: list[str],
                              deltas: list) -> dict:
        totals = {"ownership": 0, "association": 0}
        for source_name, source_deltas in _by_source(sources, deltas):
            counts = self._relationships.detect_from_sync(source_name,
                                                          source_deltas)
            totals["ownership"] += counts["ownership"]
            totals["association"] += counts["association"]
        totals.update(self._relationships.detect_cross_domain())
        if self._artifacts is not None:
            totals.update(self._relationships.detect_dependencies(
                self._artifacts))
        return totals

    def _update_embeddings(self) -> dict:
        """Embeddings Update: the organizational model becomes searchable by
        meaning. Only entities touched since the last refresh are embedded —
        re-embedding everything would be the rebuild this layer exists to
        avoid."""
        if self._embedder is None or self._vector_store_for is None:
            return {"skipped": "embeddings unavailable"}
        entities = self._org.entities(limit=MAX_EMBED_PER_REFRESH)
        if not entities:
            return {"embedded": 0}
        texts = [_entity_text(e) for e in entities]
        vectors = self._embedder.embed(texts)
        store = self._vector_store_for("_organization")
        store.upsert(
            [e["entity_id"] for e in entities], vectors,
            [{"kind": "organization_entity", "entity_kind": e["kind"],
              "name": e["name"], "entity_id": e["entity_id"],
              "text": text} for e, text in zip(entities, texts)])
        store.persist()
        return {"embedded": len(entities)}

    def _update_context(self) -> dict:
        """Enterprise Context Update: every project's unified context is
        rebuilt so the next prompt sees the new organization. The Brain owns
        context building — this stage asks it, it does not reimplement it."""
        if self._brain is None or self._artifacts is None:
            return {"skipped": "brain disabled"}
        rebuilt = 0
        for pid in self._artifacts.list_projects():
            if not self._artifacts.exists(pid, "business_context"):
                continue
            try:
                self._brain.build_enterprise_context(pid)
                rebuilt += 1
            except Exception:  # noqa: BLE001 — one project never fails the refresh
                logger.exception("Enterprise context rebuild failed for %s", pid)
        return {"contexts_rebuilt": rebuilt}

    # -------------------------------------------------------------- runner
    def _stage(self, result: RefreshResult, name: str, run) -> Any:
        """Run one stage, recording its outcome. A stage that fails degrades
        the refresh; it never stops the stages after it, because knowledge the
        platform *can* update should be updated."""
        record = {"stage": name, "status": "running", "at": now_iso()}
        try:
            outcome = run()
            record["status"] = "completed"
            record["detail"] = _small(outcome)
            return outcome
        except Exception as exc:  # noqa: BLE001 — see docstring
            logger.exception("Knowledge refresh stage %s failed", name)
            record["status"] = "failed"
            record["error"] = str(exc)[:300]
            return None
        finally:
            result.stages.append(record)

    def _finish(self, result: RefreshResult) -> RefreshResult:
        result.finished_at = now_iso()
        try:
            self._store.append("refresh_events", result.describe(),
                               cap=MAX_REFRESH_EVENTS)
        except Exception:  # noqa: BLE001 — history is observability, not truth
            logger.exception("Refresh history persistence failed")
        if self._bus is not None:
            try:
                self._bus.publish("KnowledgeUpdated", {
                    "source": "knowledge_refresh_pipeline",
                    "refresh_id": result.refresh_id,
                    "status": result.status,
                    "changed_records": result.changed_records},
                    source="sync_pipeline")
            except Exception:  # noqa: BLE001
                logger.exception("Refresh event publication failed")
        logger.info("Knowledge refresh %s: %s (%d changed records)",
                    result.refresh_id, result.status, result.changed_records)
        return result

    # ---------------------------------------------------------------- read
    def events(self, limit: int = 20) -> list[dict]:
        return list(reversed(self._store.read("refresh_events")))[:limit]

    def freshness(self) -> dict[str, Any]:
        """Knowledge Freshness: when did the organization last learn, and is
        anything stale?"""
        events = self._store.read("refresh_events")
        last = events[-1] if events else None
        sources = self._registry.sources()
        stale = [s["name"] for s in sources
                 if s["capability"] == "native" and s["enabled"]
                 and s["health"] in ("degraded", "unreachable")]
        return {
            "last_refresh_at": last["finished_at"] if last else "",
            "last_refresh_status": last["status"] if last else "never",
            "refreshes_recorded": len(events),
            "sources_stale": stale,
            "is_fresh": bool(last and last["status"] == "ready" and not stale),
        }


# --------------------------------------------------------------- utilities
def _collect(results) -> tuple[list, list[str]]:
    """Flatten sync results into (deltas, source names aligned per delta)."""
    if not results:
        return [], []
    deltas, sources = [], []
    for result in results:
        if result.status != "completed":
            continue
        for delta in result.deltas:
            deltas.append(delta)
            sources.append(result.source_name)
    return deltas, sources


def _by_source(sources: list[str], deltas: list):
    """Group deltas by the source that produced them."""
    grouped: dict[str, list] = {}
    for source_name, delta in zip(sources, deltas):
        grouped.setdefault(source_name, []).append(delta)
    return grouped.items()


def _entity_text(entity: dict) -> str:
    """The sentence that represents an entity to the embedder."""
    parts = [entity["kind"], entity["name"]]
    if entity["aliases"]:
        parts.append("also known as " + ", ".join(entity["aliases"][:5]))
    if entity["owner"]:
        parts.append(f"owned by {entity['owner']}")
    if entity["sources"]:
        parts.append("seen in " + ", ".join(entity["sources"][:3]))
    return " · ".join(parts)


def _small(value: Any) -> Any:
    """Stage details are persisted and served — keep them bounded."""
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, str):
        return value[:200]
    if isinstance(value, dict):
        return {k: _small(v) for k, v in list(value.items())[:12]}
    if isinstance(value, (list, tuple)):
        return [_small(v) for v in list(value)[:10]]
    return str(value)[:200]

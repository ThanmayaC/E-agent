"""Enterprise Knowledge Synchronization Layer.

The Enterprise Brain learns from analyses. This layer keeps it learning from
the *enterprise*: once databases, documents, and (in V2) communication systems
are connected, organizational knowledge updates continuously, with nobody
pressing anything.

    registry       Enterprise Data Source Registry — what is connected, how to
                   authenticate (by reference, never by value), how healthy it
                   is, how often it refreshes, and where its sync got to
    reader         reads a source through the connectors that already exist —
                   no second implementation of anything
    engine         Synchronization Engine — first/delta sync by record
                   fingerprint, versioned, retried, resumable
    organization   Organizational Model — the enterprise's entities, each with
                   identity, relationships, ownership, and history
    relationships  Relationship Engine — ownership, dependencies, hierarchies,
                   associations, and cross-domain links, all evidenced
    pipeline       Knowledge Refresh Pipeline — sync → observation → knowledge
                   → memory → relationships → embeddings → context → ready
    search         Enterprise Search — one query across every surface
    sync_runtime   composition root, wired into the autonomy runtime's jobs
"""
from app.sync.engine import SyncDelta, SyncResult, SynchronizationEngine
from app.sync.organization import ENTITY_KINDS, OrganizationalModel
from app.sync.pipeline import KnowledgeRefreshPipeline
from app.sync.reader import SourceReader
from app.sync.registry import SOURCE_KINDS, DataSourceRegistry
from app.sync.relationships import RELATIONSHIP_KINDS, RelationshipEngine
from app.sync.search import SURFACES, EnterpriseSearch
from app.sync.store import SyncStore
from app.sync.sync_runtime import SynchronizationLayer

__all__ = [
    "ENTITY_KINDS", "RELATIONSHIP_KINDS", "SOURCE_KINDS", "SURFACES",
    "DataSourceRegistry", "EnterpriseSearch", "KnowledgeRefreshPipeline",
    "OrganizationalModel", "RelationshipEngine", "SourceReader", "SyncDelta",
    "SyncResult", "SyncStore", "SynchronizationEngine", "SynchronizationLayer",
]

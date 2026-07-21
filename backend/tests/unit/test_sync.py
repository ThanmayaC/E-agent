"""Enterprise Knowledge Synchronization Layer — registry, incremental sync,
organizational model, relationships, refresh pipeline, and enterprise search.

The engine is driven directly against real CSV files on disk rather than a
mocked connector: incremental synchronization is a claim about what happens
when a file actually changes, and a fake source cannot falsify it.
"""
from __future__ import annotations

import pandas as pd
import pytest

from app.intelligence.connectors import build_registry as build_connectors
from app.knowledge.store import KnowledgeStore
from app.sync.engine import SynchronizationEngine
from app.sync.organization import OrganizationalModel
from app.sync.pipeline import KnowledgeRefreshPipeline
from app.sync.reader import SourceReader
from app.sync.registry import DataSourceRegistry, SecretNotConfigured
from app.sync.relationships import RelationshipEngine
from app.sync.search import EnterpriseSearch
from app.sync.store import SyncStore

MERCHANTS = pd.DataFrame({
    "merchant_id": ["M001", "M002", "M003"],
    "name": ["North Coffee", "South Bakery", "East Grocers"],
    "owner": ["Dana K", "Dana K", "Ravi P"],
    "bank": ["First National", "First National", "Metro Bank"],
})


@pytest.fixture()
def sync_dir(tmp_path):
    return SyncStore(tmp_path / "sync")


@pytest.fixture()
def knowledge(tmp_path):
    return KnowledgeStore(tmp_path / "knowledge")


@pytest.fixture()
def merchants_csv(tmp_path):
    path = tmp_path / "data" / "merchants.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    MERCHANTS.to_csv(path, index=False)
    return path


@pytest.fixture()
def registry(sync_dir):
    return DataSourceRegistry(sync_dir)


@pytest.fixture()
def engine(sync_dir, registry):
    reader = SourceReader(build_connectors())
    return SynchronizationEngine(sync_dir, registry, reader)


@pytest.fixture()
def organization(sync_dir, knowledge):
    return OrganizationalModel(sync_dir, knowledge=knowledge)


@pytest.fixture()
def relationships(sync_dir, organization):
    return RelationshipEngine(sync_dir, organization)


def _register_csv(registry, path, name="merchants"):
    return registry.register(name, "csv", location=str(path), cadence="hourly")


# ---------------------------------------------------------------- registry
def test_the_source_catalogue_covers_the_sds_systems(registry):
    kinds = {k["kind"]: k for k in registry.kinds()}

    assert {"postgresql", "sqlserver", "mysql", "oracle", "csv", "excel",
            "rest_api", "sharepoint", "outlook", "teams"} <= set(kinds)
    assert kinds["postgresql"]["available"] is True
    # V2: Microsoft 365 connects natively through Graph, and the document
    # repositories are first-class sources.
    for microsoft in ("sharepoint", "outlook", "teams"):
        assert kinds[microsoft]["available"] is True
        assert kinds[microsoft]["connector"] == "graph"
    for repository in ("sop_repository", "rca_repository", "meeting_notes",
                       "product_documents", "document_folder", "onedrive"):
        assert kinds[repository]["available"] is True
        assert kinds[repository]["family"] == "documents"


def test_a_registered_source_never_stores_its_credential(registry, monkeypatch):
    monkeypatch.setenv("TEST_PG_URL", "postgresql://user:hunter2@db/prod")
    source = registry.register("warehouse", "postgresql",
                               auth={"kind": "env", "ref": "TEST_PG_URL"})

    serialized = str(source)
    assert "hunter2" not in serialized, "a credential reached the registry"
    assert source["auth"] == {"kind": "env", "ref": "TEST_PG_URL",
                              "configured": True}


def test_a_credential_pasted_into_location_is_rejected(registry):
    with pytest.raises(ValueError, match="looks like it contains credentials"):
        registry.register("bad", "postgresql",
                          location="postgresql://user:pw@host/db")


def test_a_secret_value_in_auth_is_rejected(registry):
    with pytest.raises(ValueError, match="must not carry a secret value"):
        registry.register("bad", "postgresql",
                          auth={"kind": "env", "ref": "X",
                                "password": "hunter2"})


def test_an_unset_auth_reference_reads_as_unconfigured(registry):
    source = registry.register("warehouse", "postgresql",
                               auth={"kind": "env", "ref": "NOT_SET_ANYWHERE"})

    assert source["health"] == "unconfigured"
    assert source["auth"]["configured"] is False


def test_a_graph_source_requires_a_credential_reference(registry):
    # V2: Microsoft 365 sources are native but never anonymous — a
    # registration without an auth reference is refused with instructions.
    with pytest.raises(ValueError, match="Microsoft Graph"):
        registry.register("intranet", "sharepoint")

    source = registry.register(
        "intranet", "sharepoint",
        auth={"kind": "env", "ref": "NOT_SET_ANYWHERE"})
    assert source["capability"] == "native"
    assert source["health"] == "unconfigured"


def test_duplicate_source_names_are_rejected(registry, merchants_csv):
    _register_csv(registry, merchants_csv)
    with pytest.raises(ValueError, match="already registered"):
        _register_csv(registry, merchants_csv)


def test_unknown_kinds_and_cadences_are_rejected(registry):
    with pytest.raises(ValueError, match="Unknown source kind"):
        registry.register("x", "mongodb")
    with pytest.raises(ValueError, match="Unknown refresh cadence"):
        registry.register("x", "csv", cadence="fortnightly")


# ------------------------------------------------------ incremental sync
def test_first_sync_reports_every_record_as_added(registry, engine,
                                                  merchants_csv):
    source = _register_csv(registry, merchants_csv)
    result = engine.sync(source["source_id"])

    assert result.status == "completed"
    assert result.mode == "first"
    assert result.version == 1
    assert result.changed_records == 3
    assert len(result.deltas[0].added) == 3


def test_a_second_sync_with_no_changes_does_nothing(registry, engine,
                                                    merchants_csv):
    source = _register_csv(registry, merchants_csv)
    engine.sync(source["source_id"])
    result = engine.sync(source["source_id"])

    assert result.mode == "delta"
    assert result.version == 2
    assert result.changed_records == 0, "an unchanged source reported changes"
    assert result.deltas[0].unchanged == 3


def test_only_the_changed_record_syncs(registry, engine, merchants_csv):
    source = _register_csv(registry, merchants_csv)
    engine.sync(source["source_id"])

    changed = MERCHANTS.copy()
    changed.loc[changed["merchant_id"] == "M002", "owner"] = "Ravi P"
    changed.to_csv(merchants_csv, index=False)
    result = engine.sync(source["source_id"])

    delta = result.deltas[0]
    assert len(delta.changed) == 1, "a delta sync re-read unchanged records"
    assert delta.changed[0]["record"]["merchant_id"] == "M002"
    assert delta.unchanged == 2
    assert not delta.added and not delta.removed


def test_added_and_removed_records_are_detected(registry, engine,
                                                merchants_csv):
    source = _register_csv(registry, merchants_csv)
    engine.sync(source["source_id"])

    frame = MERCHANTS[MERCHANTS["merchant_id"] != "M003"].copy()
    frame.loc[len(frame)] = ["M004", "West Deli", "Ravi P", "Metro Bank"]
    frame.to_csv(merchants_csv, index=False)
    result = engine.sync(source["source_id"])

    delta = result.deltas[0]
    assert [a["record"]["merchant_id"] for a in delta.added] == ["M004"]
    assert len(delta.removed) == 1
    assert "M003" in delta.removed[0]


def test_force_full_resyncs_everything(registry, engine, merchants_csv):
    source = _register_csv(registry, merchants_csv)
    engine.sync(source["source_id"])
    result = engine.sync(source["source_id"], force_full=True)

    assert result.mode == "first"
    assert len(result.deltas[0].added) == 3


def test_a_failed_sync_is_recorded_and_never_raises(registry, engine,
                                                    tmp_path):
    source = registry.register("missing", "csv",
                               location=str(tmp_path / "nope.csv"))
    result = engine.sync(source["source_id"])

    assert result.status == "failed"
    assert "does not exist" in result.error
    stored = registry.get(source["source_id"])
    assert stored["sync_state"] == "failed"
    assert stored["consecutive_failures"] == 1


def test_a_failed_sync_preserves_the_last_good_state(registry, engine,
                                                     merchants_csv):
    """A failure must not destroy fingerprints — the next sync resumes with a
    delta rather than re-learning the whole source."""
    source = _register_csv(registry, merchants_csv)
    engine.sync(source["source_id"])
    merchants_csv.unlink()
    engine.sync(source["source_id"])          # fails
    MERCHANTS.to_csv(merchants_csv, index=False)  # the system comes back
    result = engine.sync(source["source_id"])

    assert result.status == "completed"
    assert result.mode == "delta"
    assert result.changed_records == 0, "a recovered source re-synced everything"


def test_repeated_failures_degrade_then_mark_the_source_unreachable(
        registry, engine, tmp_path):
    source = registry.register("missing", "csv",
                               location=str(tmp_path / "nope.csv"))
    engine.sync(source["source_id"])
    assert registry.check_health(source["source_id"])["health"] == "degraded"

    engine.sync(source["source_id"])
    engine.sync(source["source_id"])
    assert registry.check_health(source["source_id"])["health"] == "unreachable"


def test_a_graph_source_without_its_secret_fails_cleanly(registry, engine):
    # V2: an M365 source whose credential env var is unset fails with the
    # configuration message, never a stack trace — same contract as SQL.
    source = registry.register(
        "intranet", "sharepoint",
        auth={"kind": "env", "ref": "NOT_SET_ANYWHERE"})
    result = engine.sync(source["source_id"])

    assert result.status == "failed"
    assert "NOT_SET_ANYWHERE" in result.error


def test_a_sql_source_without_its_secret_fails_cleanly(registry, engine):
    source = registry.register("warehouse", "postgresql",
                               auth={"kind": "env", "ref": "NOT_SET_ANYWHERE"})
    registry.set_enabled(source["source_id"], True)
    result = engine.sync(source["source_id"])

    assert result.status == "failed"
    assert "NOT_SET_ANYWHERE" in result.error


def test_only_due_sources_are_synced(registry, engine, merchants_csv):
    source = _register_csv(registry, merchants_csv)
    assert registry.due(), "a never-synced source should be due"

    engine.sync(source["source_id"])
    assert not registry.due(), "a just-synced hourly source is not due again"


def test_manual_cadence_is_never_due(registry, merchants_csv):
    registry.register("m", "csv", location=str(merchants_csv),
                      cadence="manual")
    assert registry.due() == []


# ------------------------------------------------- organizational model
def test_entities_carry_identity_ownership_and_history(organization):
    entity, created = organization.observe(
        "merchant", "North Coffee", source="pos", aliases=["M001"],
        owner="Dana K", owner_source="pos.owner")

    assert created is True
    assert entity["entity_id"] == "merchant:north_coffee"
    assert "m001" in entity["aliases"]
    assert entity["owner"] == "Dana K"
    assert entity["history"][0]["change"] == "discovered"


def test_observing_a_known_entity_enriches_it_without_duplicating(organization):
    organization.observe("merchant", "North Coffee", source="pos")
    entity, changed = organization.observe("merchant", "North Coffee",
                                           source="crm", aliases=["MID-1"])

    assert changed is True
    assert len(organization.entities(kind="merchant")) == 1
    assert entity["sources"] == ["pos", "crm"]
    assert "mid_1" in entity["aliases"]


def test_an_unchanged_observation_reports_no_change(organization):
    organization.observe("merchant", "North Coffee", source="pos")
    _, changed = organization.observe("merchant", "North Coffee", source="pos")

    assert changed is False, "an idempotent observation reported a change"


def test_an_owner_change_is_recorded_in_history(organization):
    organization.observe("merchant", "North Coffee", owner="Dana K")
    entity, _ = organization.observe("merchant", "North Coffee", owner="Ravi P")

    changes = [h for h in entity["history"] if h["change"] == "owner_changed"]
    assert changes and "Dana K → Ravi P" in changes[0]["detail"]


def test_an_entity_resolves_by_any_alias(organization):
    organization.observe("merchant", "North Coffee", aliases=["M001", "MID-1"])

    assert organization.resolve("M001")["name"] == "North Coffee"
    assert organization.resolve("mid-1")["name"] == "North Coffee"
    assert organization.resolve("Unknown Ltd") is None


def test_unknown_entity_kinds_are_rejected(organization):
    with pytest.raises(ValueError, match="Unknown entity kind"):
        organization.observe("spaceship", "Enterprise")


def test_entities_are_derived_from_a_sync_delta(registry, engine,
                                                organization, merchants_csv):
    source = _register_csv(registry, merchants_csv)
    result = engine.sync(source["source_id"])
    counts = organization.observe_from_sync("merchants", result.deltas)

    assert counts["discovered"] == 3
    names = {e["name"] for e in organization.entities(kind="merchant")}
    assert names == {"North Coffee", "South Bakery", "East Grocers"}
    assert organization.resolve("North Coffee")["owner"] == "Dana K"


def test_a_table_with_no_business_meaning_contributes_nothing(organization):
    class _Delta:
        table = "tmp_export_20260716"
        columns = ["col_a", "col_b"]
        added = [{"key": "k", "record": {"col_a": 1, "col_b": 2}}]
        changed: list = []

    counts = organization.observe_from_sync("junk", [_Delta()])

    assert counts["discovered"] == 0, "the model invented an entity"
    assert organization.entities() == []


# --------------------------------------------------------- relationships
def test_ownership_and_associations_are_detected_from_a_sync(
        registry, engine, organization, relationships, merchants_csv):
    source = _register_csv(registry, merchants_csv)
    result = engine.sync(source["source_id"])
    organization.observe_from_sync("merchants", result.deltas)
    # The bank column names banks the model has not met yet.
    for bank in ("First National", "Metro Bank"):
        organization.observe("bank", bank, source="merchants")
    found = relationships.detect_from_sync("merchants", result.deltas)

    assert found["ownership"] > 0
    owner = organization.resolve("Dana K", kind="employee")
    assert owner is not None, "the owner column did not become an employee"
    links = relationships.relationships(entity_id=owner["entity_id"])
    assert any(l["kind"] == "ownership" for l in links)
    assert any(l["kind"] == "association" for l in
               relationships.relationships(kind="association"))


def test_a_relationship_carries_its_evidence_and_strengthens_when_reobserved(
        organization, relationships):
    organization.observe("customer", "Acme")
    organization.observe("product", "Widget")
    first, _ = relationships.relate("customer:acme", "product:widget",
                                    "association", evidence="co-occur in pos",
                                    confidence=0.6)
    second, _ = relationships.relate("customer:acme", "product:widget",
                                     "association", evidence="co-occur in pos",
                                     confidence=0.6)

    assert first["evidence"] == "co-occur in pos"
    assert second["observations"] == 2
    assert second["confidence"] > first["confidence"]
    assert len(relationships.relationships()) == 1, "the edge was duplicated"


def test_confidence_never_reaches_certainty(organization, relationships):
    organization.observe("customer", "Acme")
    organization.observe("product", "Widget")
    for _ in range(30):
        link, _ = relationships.relate("customer:acme", "product:widget",
                                       "association", confidence=0.6)

    assert link["confidence"] <= 0.95


def test_meaningless_pairings_are_not_associated(organization, relationships):
    """A report and a bank co-occurring is not a business association — noise
    in a knowledge graph gets reasoned over."""
    organization.observe("report", "Q3 review")
    organization.observe("bank", "Metro Bank")
    entities = [organization.get("report:q3_review"),
                organization.get("bank:metro_bank")]
    found = relationships._detect_associations(entities, "src", "t")

    assert found == 0
    assert relationships.relationships() == []


def test_an_entity_cannot_relate_to_itself(relationships):
    with pytest.raises(ValueError, match="cannot relate to itself"):
        relationships.relate("merchant:a", "merchant:a", "association")


def test_cross_domain_links_the_same_entity_across_systems(organization,
                                                           relationships):
    organization.observe("merchant", "North Coffee", source="pos")
    organization.observe("merchant", "North Coffee", source="crm")
    outcome = relationships.detect_cross_domain()

    assert outcome["cross_domain_entities"] == 1
    entity = organization.resolve("North Coffee")
    assert entity["attributes"]["cross_domain_sources"] == ["pos", "crm"]


def test_an_entity_in_one_system_is_not_cross_domain(organization,
                                                     relationships):
    organization.observe("merchant", "North Coffee", source="pos")
    assert relationships.detect_cross_domain()["cross_domain_entities"] == 0


# ------------------------------------------------------ refresh pipeline
@pytest.fixture()
def pipeline(sync_dir, engine, registry, organization, relationships,
             knowledge):
    return KnowledgeRefreshPipeline(sync_dir, engine, registry, organization,
                                    relationships, knowledge)


def test_the_pipeline_runs_every_stage_and_ends_ready(pipeline, registry,
                                                      merchants_csv):
    _register_csv(registry, merchants_csv)
    result = pipeline.refresh(trigger="test")

    assert result.status == "ready", result.stages
    stages = [s["stage"] for s in result.stages]
    assert stages == ["synchronize", "observation", "document_intelligence",
                      "knowledge_update", "memory_update",
                      "relationship_update", "embeddings_update",
                      "enterprise_context_update", "ready"]
    assert all(s["status"] == "completed" for s in result.stages)


def test_a_refresh_with_no_changes_does_no_work(pipeline, registry,
                                                merchants_csv):
    _register_csv(registry, merchants_csv)
    pipeline.refresh()
    result = pipeline.refresh(force_full=False)

    assert result.status == "ready"
    assert result.changed_records == 0
    assert [s["stage"] for s in result.stages] == ["synchronize", "ready"], \
        "an unchanged refresh rebuilt knowledge"


def test_a_scheduled_refresh_skips_sources_that_are_not_due(
        pipeline, registry, merchants_csv):
    """The cadence is the contract: a scheduled refresh syncs what is due and
    nothing else, however often the heartbeat calls it."""
    _register_csv(registry, merchants_csv)
    pipeline.refresh()

    changed = MERCHANTS.copy()
    changed.loc[0, "name"] = "North Coffee Roasters"
    changed.to_csv(merchants_csv, index=False)
    result = pipeline.refresh()  # scheduled: the hourly source is not due yet

    assert result.changed_records == 0
    assert [s["stage"] for s in result.stages] == ["synchronize", "ready"]


def test_a_refresh_records_a_learning_event_and_preserves_versions(
        pipeline, registry, knowledge, merchants_csv):
    source = _register_csv(registry, merchants_csv)
    pipeline.refresh(source_id=source["source_id"])
    versions_after_first = knowledge.stats()["knowledge_versions"]

    changed = MERCHANTS.copy()
    changed.loc[0, "name"] = "North Coffee Roasters"
    changed.to_csv(merchants_csv, index=False)
    pipeline.refresh(source_id=source["source_id"], trigger="manual")

    events = [e for e in knowledge.learning_history(20)
              if e["event"] == "knowledge_synchronization"]
    assert len(events) == 2, "the refresh was not recorded as learning"
    assert knowledge.stats()["knowledge_versions"] > versions_after_first, \
        "knowledge was overwritten instead of versioned"


def test_a_failing_stage_degrades_the_refresh_without_stopping_it(
        pipeline, registry, merchants_csv, monkeypatch):
    _register_csv(registry, merchants_csv)
    monkeypatch.setattr(pipeline, "_update_relationships",
                        lambda *a, **k: (_ for _ in ()).throw(
                            RuntimeError("graph is down")))
    result = pipeline.refresh()

    assert result.status == "degraded"
    stages = {s["stage"]: s for s in result.stages}
    assert stages["relationship_update"]["status"] == "failed"
    assert stages["enterprise_context_update"]["status"] == "completed", \
        "one failed stage stopped the stages after it"
    assert stages["ready"]["status"] == "completed"


def test_freshness_reports_stale_systems(pipeline, registry, engine, tmp_path):
    source = registry.register("broken", "csv",
                               location=str(tmp_path / "gone.csv"))
    engine.sync(source["source_id"])
    registry.check_health(source["source_id"])
    freshness = pipeline.freshness()

    assert "broken" in freshness["sources_stale"]
    assert freshness["is_fresh"] is False


# ---------------------------------------------------- enterprise search
@pytest.fixture()
def search(knowledge, organization, relationships, tmp_path):
    from app.repositories.artifact_store import ArtifactStore
    artifacts = ArtifactStore(tmp_path / "projects")
    artifacts.save("proj_1", "state", {"project_id": "proj_1",
                                       "name": "Merchant Analytics",
                                       "status": "ready"})
    knowledge.add_rule("Merchant fees are capped at 2%", scope="global")
    knowledge.add_term("Merchant", "A business that accepts payments")
    knowledge.record_recommendation("Review merchant fee structure",
                                    priority=1)
    knowledge.remember_clarification("What is a merchant?",
                                     "A business accepting payments")
    knowledge.record_report("proj_1", "Merchant Analytics — report v1", 72.0)
    organization.observe("merchant", "North Coffee", source="pos",
                         aliases=["M001"])
    return EnterpriseSearch(knowledge, artifacts, organization, relationships)


def test_one_query_reaches_every_surface(search):
    outcome = search.search("merchant")
    surfaces = {hit["surface"] for hit in outcome["results"]}

    assert {"knowledge", "business_rules", "recommendations",
            "clarifications", "projects", "reports"} <= surfaces
    assert outcome["total"] > 0
    assert not outcome["unavailable"]


def test_search_finds_an_entity_by_its_alias(search):
    outcome = search.search("M001")
    hits = [h for h in outcome["results"] if h["surface"] == "organization"]

    assert hits, "an alias search missed the entity it identifies"
    assert hits[0]["title"] == "North Coffee"
    assert hits[0]["matched"] == "alias"


def test_documents_surface_returns_chunk_passages(knowledge, organization,
                                                  relationships, tmp_path):
    """The documents surface reaches the *contents* of SOPs, RCAs, meetings,
    and reports — the retrieval that makes cross-source Brain Q&A possible."""
    from app.repositories.artifact_store import ArtifactStore

    class _Docs:
        def search(self, query, limit=8):
            return [{"payload": {
                "document_id": "d1", "document": "RCA-2026-03",
                "category": "rca", "source": "enterprise-rcas",
                "text": "Settlement success fell to 94.2% in March 2026."},
                "score": 0.8}]

    artifacts = ArtifactStore(tmp_path / "projects")
    engine = EnterpriseSearch(knowledge, artifacts, organization,
                              relationships, documents=_Docs())
    outcome = engine.search("settlement", surfaces=["documents"])

    assert outcome["surfaces_searched"] == ["documents"]
    hits = outcome["results"]
    assert hits and hits[0]["surface"] == "documents"
    assert hits[0]["ref"] == "d1"
    assert "rca" in hits[0]["detail"]


def test_exact_title_matches_outrank_buried_mentions(search):
    outcome = search.search("Merchant")
    top = outcome["results"][0]

    assert top["score"] >= 4
    assert top["matched"] in ("exact title", "title prefix", "title")


def test_search_can_be_scoped_to_surfaces(search):
    outcome = search.search("merchant", surfaces=["business_rules"])

    assert outcome["surfaces_searched"] == ["business_rules"]
    assert {h["surface"] for h in outcome["results"]} == {"business_rules"}


def test_a_query_with_no_usable_terms_returns_nothing_gracefully(search):
    outcome = search.search("a")

    assert outcome["results"] == []
    assert "at least" in outcome["note"]


def test_a_failing_surface_never_darkens_the_whole_search(search,
                                                          monkeypatch):
    monkeypatch.setattr(search, "_search_projects",
                        lambda terms: (_ for _ in ()).throw(
                            RuntimeError("artifact store is down")))
    outcome = search.search("merchant")

    assert outcome["total"] > 0, "one broken surface took down the search"
    assert outcome["unavailable"][0]["surface"] == "projects"
    assert "projects" not in outcome["surfaces_searched"]


def test_search_reports_which_surfaces_answer(search):
    surfaces = {s["surface"]: s for s in search.surfaces()}

    assert surfaces["tasks"]["available"] is False  # no task manager wired
    assert surfaces["knowledge"]["available"] is True

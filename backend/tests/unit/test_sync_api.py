"""The synchronization layer through the real app: connect a system, and
organizational knowledge updates without anyone doing anything else.

Drives the /sources, /search, and /organization surfaces against a container
with the scheduler running, which is the actual claim of this milestone.
"""
from __future__ import annotations

import os

import pandas as pd
import pytest
from fastapi.testclient import TestClient

MERCHANTS = pd.DataFrame({
    "merchant_id": ["M001", "M002", "M003"],
    "name": ["North Coffee", "South Bakery", "East Grocers"],
    "owner": ["Dana K", "Dana K", "Ravi P"],
})


@pytest.fixture(scope="module")
def data_dir(tmp_path_factory):
    return tmp_path_factory.mktemp("sync_api_data")


@pytest.fixture(scope="module")
def merchants_csv(tmp_path_factory):
    path = tmp_path_factory.mktemp("enterprise") / "merchants.csv"
    MERCHANTS.to_csv(path, index=False)
    return path


@pytest.fixture(scope="module")
def client(data_dir):
    os.environ["EDIP_DATA_DIR"] = str(data_dir)
    os.environ["EDIP_LLM_PROVIDER"] = "mock"
    from app.core import config, container
    config.get_settings.cache_clear()
    container.get_container.cache_clear()
    from app.main import create_app
    with TestClient(create_app()) as c:  # lifespan → brain, runtime, sync
        yield c
    config.get_settings.cache_clear()
    container.get_container.cache_clear()


@pytest.fixture(scope="module")
def source(client, merchants_csv):
    return client.post("/api/v1/sources", json={
        "name": "merchant_master", "kind": "csv",
        "location": str(merchants_csv), "cadence": "hourly",
        "description": "Merchant master data"}).json()


# --------------------------------------------------------------- sources
def test_the_source_catalogue_is_exposed(client):
    catalogue = {k["kind"]: k for k in
                 client.get("/api/v1/sources").json()["catalogue"]}

    assert {"postgresql", "sqlserver", "mysql", "oracle", "csv", "excel",
            "rest_api", "sharepoint", "outlook", "teams",
            "sop_repository", "rca_repository", "meeting_notes"} \
        <= set(catalogue)
    # V2: Microsoft 365 is native through Graph.
    assert catalogue["sharepoint"]["available"] is True


def test_registering_a_source_is_all_the_setup_there_is(client, source):
    assert source["kind"] == "csv"
    assert source["sync_state"] == "never_synced"
    assert source["enabled"] is True


def test_the_api_never_returns_a_credential(client, monkeypatch):
    os.environ["TEST_API_PG_URL"] = "postgresql://user:hunter2@db/prod"
    try:
        created = client.post("/api/v1/sources", json={
            "name": "warehouse_api", "kind": "postgresql",
            "auth": {"kind": "env", "ref": "TEST_API_PG_URL"}}).json()
        listed = client.get("/api/v1/sources").text
        detail = client.get(f"/api/v1/sources/{created['source_id']}").text

        assert "hunter2" not in listed
        assert "hunter2" not in detail
        assert created["auth"]["configured"] is True
    finally:
        os.environ.pop("TEST_API_PG_URL", None)


def test_a_credentialed_location_is_rejected_by_the_api(client):
    response = client.post("/api/v1/sources", json={
        "name": "leaky", "kind": "postgresql",
        "location": "postgresql://user:pw@host/db"})

    assert response.status_code == 422
    assert "credentials" in response.json()["detail"]


def test_a_graph_system_requires_a_credential_reference(client):
    # V2: SharePoint is native, but never anonymous.
    refused = client.post("/api/v1/sources", json={
        "name": "intranet", "kind": "sharepoint"})
    assert refused.status_code == 422
    assert "Microsoft Graph" in refused.json()["detail"]

    created = client.post("/api/v1/sources", json={
        "name": "intranet", "kind": "sharepoint",
        "auth": {"kind": "env", "ref": "NOT_SET_ANYWHERE"}}).json()
    assert created["capability"] == "native"
    assert created["health"] == "unconfigured"


def test_sources_status_reports_connected_systems(client, source):
    status = client.get("/api/v1/sources/status").json()

    assert status["total"] >= 1
    assert "by_health" in status and "freshness" in status
    # V2: the unconfigured Graph source shows as needing attention, not as
    # awaiting a future integration.
    assert status["needs_attention"] >= 1


# --------------------------------------------- synchronize end to end
def test_a_manual_sync_refreshes_organizational_knowledge(client, source):
    refresh = client.post(
        f"/api/v1/sources/sync?source_id={source['source_id']}").json()

    assert refresh["status"] == "ready", refresh["stages"]
    assert refresh["changed_records"] == 3
    stages = {s["stage"]: s["status"] for s in refresh["stages"]}
    assert stages["observation"] == "completed"
    assert stages["knowledge_update"] == "completed"
    assert stages["ready"] == "completed"


def test_the_organization_now_knows_the_merchants(client, source):
    entities = client.get("/api/v1/organization/entities?kind=merchant").json()
    names = {e["name"] for e in entities["entities"]}

    assert {"North Coffee", "South Bakery", "East Grocers"} <= names
    assert entities["counts"]["merchant"] >= 3


def test_entities_carry_ownership_and_provenance(client):
    entities = client.get(
        "/api/v1/organization/entities?q=north+coffee").json()["entities"]

    assert entities, "the merchant was not found by name"
    entity = entities[0]
    assert entity["owner"] == "Dana K"
    assert "merchant_master" in entity["sources"]
    assert entity["history"], "the entity carries no history"


def test_one_entity_exposes_its_history_and_relationships(client):
    entity = client.get(
        "/api/v1/organization/entities/merchant:north_coffee").json()

    assert entity["entity"]["name"] == "North Coffee"
    assert entity["history"][0]["change"] == "discovered"
    assert isinstance(entity["related"], list)


def test_ownership_relationships_were_detected(client):
    links = client.get(
        "/api/v1/organization/relationships?kind=ownership").json()

    assert links["relationships"], "no ownership was detected"
    assert links["relationships"][0]["evidence"], "a link without evidence"
    assert links["stats"]["total"] > 0


def test_a_second_sync_changes_nothing(client, source):
    refresh = client.post(
        f"/api/v1/sources/sync?source_id={source['source_id']}").json()

    assert refresh["changed_records"] == 0
    assert [s["stage"] for s in refresh["stages"]] == ["synchronize", "ready"]


def test_changing_the_source_updates_only_what_changed(client, source,
                                                       merchants_csv):
    changed = MERCHANTS.copy()
    changed.loc[changed["merchant_id"] == "M002", "owner"] = "Ravi P"
    changed.to_csv(merchants_csv, index=False)

    refresh = client.post(
        f"/api/v1/sources/sync?source_id={source['source_id']}").json()

    assert refresh["changed_records"] == 1
    assert refresh["stages"][0]["detail"], refresh["stages"][0]
    entity = client.get(
        "/api/v1/organization/entities/merchant:south_bakery").json()
    assert entity["entity"]["owner"] == "Ravi P", "the change did not land"
    assert any(h["change"] == "owner_changed"
               for h in entity["history"]), "the change was not historied"


def test_the_source_now_reports_healthy_and_versioned(client, source):
    stored = client.get(f"/api/v1/sources/{source['source_id']}").json()

    assert stored["source"]["health"] == "healthy"
    assert stored["source"]["sync_version"] >= 3
    assert stored["source"]["records_total"] == 3
    assert stored["runs"], "no sync history was recorded"


def test_refresh_history_records_every_stage(client):
    refreshes = client.get("/api/v1/organization/refreshes").json()

    assert refreshes["refreshes"], "no refresh history"
    assert refreshes["freshness"]["last_refresh_status"] in ("ready",
                                                             "degraded")


# ---------------------------------------------------------------- search
def test_enterprise_search_reaches_every_surface(client):
    outcome = client.get("/api/v1/search/enterprise?q=merchant").json()

    assert outcome["total"] > 0
    assert {"organization"} <= {h["surface"] for h in outcome["results"]}
    assert outcome["surfaces"], "the surface catalogue is missing"


def test_search_finds_an_entity_by_alias(client):
    outcome = client.get("/api/v1/search?q=M001").json()
    hits = [h for h in outcome["results"] if h["surface"] == "organization"]

    assert hits and hits[0]["title"] == "North Coffee"


def test_search_can_be_scoped(client):
    outcome = client.get(
        "/api/v1/search?q=merchant&surfaces=organization").json()

    assert outcome["surfaces_searched"] == ["organization"]


def test_an_empty_query_is_rejected(client):
    assert client.get("/api/v1/search?q=").status_code == 422


# --------------------------------------------------------- organization
def test_the_organization_overview_is_business_framed(client):
    overview = client.get("/api/v1/organization").json()

    assert overview["entities_total"] > 0
    assert overview["connected_systems"]["connected"] >= 1
    assert overview["knowledge_freshness"]["status"] in ("current",
                                                         "needs attention")
    statuses = {s["status"] for s in overview["connected_systems"]["systems"]}
    assert "connected" in statuses, statuses
    assert "needs credentials" in statuses  # the unconfigured Graph source


# ----------------------------------------------------- executive surface
def test_the_workspace_shows_the_organization_without_technical_detail(client):
    organization = client.get("/api/v1/manager/workspace").json()["organization"]

    assert organization["status"] == "active"
    assert organization["entities_total"] > 0
    assert organization["connected_systems"]["connected"] >= 1
    assert organization["recent_synchronizations"]
    # Business framing only: no fingerprints, vectors, or sync mechanics.
    assert "fingerprints" not in str(organization)
    assert "sync_version" not in str(organization)


def test_the_dashboard_shows_the_organization_strip(client):
    summary = client.get("/api/v1/manager/dashboard").json()[
        "organization_summary"]

    assert summary["status"] == "active"
    assert summary["business_entities"] > 0
    assert summary["connected_systems"] >= 1


def test_the_executive_can_search_the_organization(client):
    outcome = client.get("/api/v1/manager/search?q=north").json()

    assert outcome["total"] > 0


# -------------------------------------------------------- runtime wiring
def test_synchronization_jobs_run_on_the_existing_heartbeat(client):
    jobs = {j["name"]: j for j in client.get("/api/v1/runtime/jobs").json()}

    assert jobs["startup_organization"]["runs"] >= 1, \
        "the organizational model was not built at startup"
    assert jobs["knowledge_refresh"]["kind"] == "interval"
    assert jobs["refresh_on_import"]["event"] == "DatasetImported"
    assert jobs["organization_sweep"]["kind"] == "cron"


def test_the_runtime_reports_synchronization_status(client):
    status = client.get("/api/v1/runtime").json()["synchronization"]

    assert status["sources"]["total"] >= 1
    assert status["organization"]["merchant"] >= 3
    assert "freshness" in status


def test_synchronizing_announces_on_the_event_bus(client):
    kinds = {e["kind"] for e in
             client.get("/api/v1/runtime/events?limit=200").json()["events"]}

    assert "SourceSynchronized" in kinds
    assert "EntityDiscovered" in kinds
    assert "KnowledgeUpdated" in kinds

"""Version 2 — Document Intelligence: the unified document pipeline.

A folder of documents becomes a registered source; synchronization detects
new/updated/removed files by content hash; the pipeline parses, chunks,
versions, and feeds the Brain — and each document version is summarized
exactly once by the workflow library.
"""
from __future__ import annotations

import pytest

from app.documents.chunker import chunk_text
from app.documents.parser import DocumentParser
from app.documents.pipeline import DocumentIntelligence
from app.documents.store import DocumentStore
from app.sync.engine import SynchronizationEngine
from app.sync.pipeline import KnowledgeRefreshPipeline
from app.sync.reader import SourceReader
from app.sync.registry import DataSourceRegistry
from app.sync.store import SyncStore


# ------------------------------------------------------------------ chunker
def test_short_text_is_one_chunk():
    assert chunk_text("hello world") == ["hello world"]


def test_long_text_chunks_on_paragraphs_with_overlap():
    paragraphs = [f"Paragraph {i}. " + ("content " * 40) for i in range(10)]
    chunks = chunk_text("\n\n".join(paragraphs), target_chars=800, overlap=100)

    assert len(chunks) > 1
    assert all(len(c) <= 800 + 100 for c in chunks)
    assert "Paragraph 0" in chunks[0]
    assert "Paragraph 9" in chunks[-1]


def test_empty_text_produces_no_chunks():
    assert chunk_text("") == []


# ------------------------------------------------------------------- parser
def test_the_parser_reports_its_format_catalogue():
    formats = {f["format"]: f for f in DocumentParser.formats()}
    assert {"pdf", "docx", "pptx", "excel", "csv", "text", "ocr"} \
        <= set(formats)
    assert formats["csv"]["available"] is True
    assert formats["text"]["available"] is True


def test_markdown_and_csv_parse_without_optional_dependencies(tmp_path):
    parser = DocumentParser()
    md = tmp_path / "sop.md"
    md.write_text("# Refund SOP\n\nStep 1: verify the merchant.",
                  encoding="utf-8")
    csv = tmp_path / "list.csv"
    csv.write_text("id,name\n1,North Coffee\n", encoding="utf-8")

    assert "Refund SOP" in parser.parse(md).text
    assert "North Coffee" in parser.parse(csv).text


def test_an_unsupported_format_degrades_with_a_warning(tmp_path):
    parser = DocumentParser()
    weird = tmp_path / "binary.xyz"
    weird.write_bytes(b"\x00\x01")

    parsed = parser.parse(weird)
    assert not parsed.parsed
    assert parsed.warnings


# ----------------------------------------------------------- store/versions
def test_the_store_versions_documents_and_never_rewrites_history(tmp_path):
    store = DocumentStore(tmp_path)
    doc, is_new = store.upsert("sops", "sop_repository", "refunds.md",
                               "refunds.md", ".md", 100, "", "hash1",
                               "text v1", 1, "text", False, [], "added")
    assert is_new and doc["version"] == 1 and doc["category"] == "sop"

    same, is_new = store.upsert("sops", "sop_repository", "refunds.md",
                                "refunds.md", ".md", 100, "", "hash1",
                                "text v1", 1, "text", False, [], "changed")
    assert not is_new, "an unchanged hash must not create a version"

    updated, is_new = store.upsert("sops", "sop_repository", "refunds.md",
                                   "refunds.md", ".md", 120, "", "hash2",
                                   "text v2", 1, "text", False, [], "changed")
    assert is_new and updated["version"] == 2
    versions = store.versions(updated["document_id"])
    assert [v["version"] for v in versions] == [1, 2]

    archived = store.archive("sops", "refunds.md")
    assert archived["status"] == "archived"
    assert len(store.versions(updated["document_id"])) == 3  # removal logged


def test_the_workfeed_serves_each_version_once(tmp_path):
    store = DocumentStore(tmp_path)
    doc, _ = store.upsert("rcas", "rca_repository", "outage.md", "outage.md",
                          ".md", 50, "", "h1", "root cause", 1, "text",
                          False, [], "added")
    assert store.unprocessed("rca_summarization", "rca")
    store.mark_processed(doc["document_id"], "rca_summarization", 1)
    assert store.unprocessed("rca_summarization", "rca") == []

    store.upsert("rcas", "rca_repository", "outage.md", "outage.md",
                 ".md", 60, "", "h2", "updated cause", 1, "text",
                 False, [], "changed")
    assert store.unprocessed("rca_summarization", "rca"), \
        "a new version re-enters the workfeed"


# --------------------------------------------------- end-to-end via sync
@pytest.fixture()
def sync_bits(tmp_path):
    sync_store = SyncStore(tmp_path / "sync")
    registry = DataSourceRegistry(sync_store)
    reader = SourceReader(connectors=None)  # document sources need none
    engine = SynchronizationEngine(sync_store, registry, reader)
    documents = DocumentIntelligence(
        store=DocumentStore(tmp_path / "documents"),
        parser=DocumentParser())
    return registry, engine, documents


def _write_sop(folder, name, text):
    folder.mkdir(parents=True, exist_ok=True)
    (folder / name).write_text(text, encoding="utf-8")


def test_a_document_folder_synchronizes_and_versions(tmp_path, sync_bits):
    registry, engine, documents = sync_bits
    folder = tmp_path / "sops"
    _write_sop(folder, "refunds.md", "# Refund SOP\n\nVerify the merchant.")
    source = registry.register("sop_library", "sop_repository",
                               location=str(folder), cadence="hourly")

    result = engine.sync(source["source_id"])
    assert result.status == "completed" and result.mode == "first"
    counts = documents.process_sync(source, result.deltas)
    assert counts["ingested"] == 1

    stored = documents.documents(category="sop")[0]
    assert stored["parsed"] and stored["version"] == 1
    assert "Refund SOP" in stored["text_preview"]

    # An edit is a delta, and the delta is a new version.
    _write_sop(folder, "refunds.md", "# Refund SOP v2\n\nNew process.")
    result = engine.sync(source["source_id"])
    assert result.mode == "delta" and result.changed_records == 1
    counts = documents.process_sync(source, result.deltas)
    assert counts["updated"] == 1
    assert documents.documents(category="sop")[0]["version"] == 2

    # An unchanged folder costs nothing.
    result = engine.sync(source["source_id"])
    assert result.changed_records == 0


def test_the_refresh_pipeline_runs_document_intelligence(tmp_path, sync_bits):
    registry, engine, documents = sync_bits
    folder = tmp_path / "minutes"
    _write_sop(folder, "standup.md",
               "# Standup\n\nAction: Dana to review Q3 pricing.")
    registry.register("meeting_minutes", "meeting_notes",
                      location=str(folder), cadence="hourly")

    class _Knowledge:
        def record_learning_event(self, *a, **k): ...

    class _Org:
        def observe(self, **k): return {}, True
        def observe_from_sync(self, *a): return {"discovered": 0, "updated": 0}
        def counts(self): return {}
        def entities(self, limit=0): return []

    class _Rels:
        def detect_from_sync(self, *a): return {"ownership": 0,
                                                "association": 0}
        def detect_cross_domain(self): return {}
        def stats(self): return {"total": 0}

    pipeline = KnowledgeRefreshPipeline(
        SyncStore(tmp_path / "sync2"), engine, registry, _Org(), _Rels(),
        _Knowledge(), documents=documents)
    result = pipeline.refresh(trigger="test")

    stages = {s["stage"]: s["status"] for s in result.stages}
    assert stages["document_intelligence"] == "completed"
    assert documents.documents(category="meeting")

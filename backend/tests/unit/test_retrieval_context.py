"""Hybrid retrieval and the context-package assembler — the RAG→LLM path."""
from __future__ import annotations

from app.intelligence.retrieval import (
    ContextAssembler, HybridRetriever, RetrievedChunk, estimate_tokens,
)


def _chunk(cid, text, *, title="", ref="", kind="doc", score=1.0):
    return RetrievedChunk(
        id=cid, text=text,
        payload={"title": title or cid, "ref": ref or cid, "kind": kind,
                 "text": text},
        fused_score=score, rerank_score=score)


# --------------------------------------------------------------- budgeting
def test_package_respects_token_budget():
    chunks = [_chunk(f"c{i}", "settlement latency rose sharply. " * 60,
                     ref=f"doc-{i}", score=1.0 - i / 100)
              for i in range(10)]
    pkg = ContextAssembler(token_budget=300).assemble(chunks, query="latency")

    assert pkg.tokens <= 300
    assert pkg.passages, "budget must still admit passages"
    assert pkg.diagnostics["token_budget"] == 300


def test_partial_passage_is_truncated_not_dropped():
    long_text = ("Bank failover completed. " * 40) + "Final settlement figure is 42."
    pkg = ContextAssembler(token_budget=60, min_passage_tokens=10).assemble(
        [_chunk("c1", long_text)], query="failover")

    assert len(pkg.passages) == 1
    assert pkg.passages[0].truncated is True
    assert pkg.tokens <= 60
    assert pkg.diagnostics["truncated_passages"] == 1


# ------------------------------------------------------------- deduplication
def test_budget_is_never_exceeded_across_many_budgets():
    """Regression: truncation used to overshoot by a token or two because the
    ellipsis marker and estimate_tokens' round-up were unbudgeted."""
    chunks = [_chunk(f"c{i}", f"Passage {i}. " + "settlement detail. " * 25,
                     ref=f"doc-{i}", score=1.0 - i / 100) for i in range(12)]
    for budget in (50, 90, 120, 300, 512, 900, 1500):
        pkg = ContextAssembler(token_budget=budget).assemble(chunks, query="q")
        assert pkg.tokens <= budget, f"overran {budget}: got {pkg.tokens}"
        assert pkg.diagnostics["budget_utilisation"] <= 1.0


def test_near_duplicate_passages_are_dropped():
    text = "UPI success rate fell to 91 percent during the HDFC outage window."
    chunks = [_chunk("a", text, ref="rpt-1"),
              _chunk("b", text, ref="rpt-2"),          # exact repeat
              _chunk("c", "Merchant refunds were reconciled overnight.", ref="rpt-3")]
    pkg = ContextAssembler(token_budget=2000).assemble(chunks, query="outage")

    assert pkg.diagnostics["dropped_duplicate"] == 1
    assert [p.chunk_id for p in pkg.passages] == ["a", "c"]


def test_per_source_cap_preserves_diversity():
    chunks = [_chunk(f"a{i}", f"Incident detail number {i} about the gateway.",
                     ref="same-doc") for i in range(5)]
    chunks.append(_chunk("b1", "Independent corroboration from the ledger.",
                         ref="other-doc"))
    pkg = ContextAssembler(token_budget=4000, max_per_source=2).assemble(
        chunks, query="gateway")

    from_same = [p for p in pkg.passages if p.ref == "same-doc"]
    assert len(from_same) == 2
    assert any(p.ref == "other-doc" for p in pkg.passages)
    assert pkg.diagnostics["dropped_source_cap"] == 3
    assert pkg.diagnostics["distinct_sources"] == 2


# ------------------------------------------------------------------ citations
def test_markers_are_contiguous_and_resolvable():
    chunks = [_chunk(f"c{i}", f"Distinct finding about topic {i}.", ref=f"d{i}")
              for i in range(5)]
    pkg = ContextAssembler(token_budget=2000).assemble(chunks, query="topic")

    markers = [p.marker for p in pkg.passages]
    assert markers == list(range(1, len(pkg.passages) + 1))
    for m in markers:
        assert pkg.source_for(m) is not None
        assert f"[{m}]" in pkg.prompt


def test_cited_markers_extracts_only_real_citations():
    chunks = [_chunk(f"c{i}", f"Distinct finding about topic {i}.", ref=f"d{i}")
              for i in range(3)]
    pkg = ContextAssembler(token_budget=2000).assemble(chunks, query="topic")

    answer = "Success dipped [1] and recovered [3]. A hallucinated cite [99]."
    assert pkg.cited_markers(answer) == [1, 3]   # [99] is not in the package


# ------------------------------------------------------------------ ordering
def test_strongest_passages_sit_at_the_edges():
    chunks = [_chunk(f"c{i}", f"Finding number {i} is distinct prose.",
                     ref=f"d{i}", score=1.0 - i * 0.1) for i in range(5)]
    pkg = ContextAssembler(token_budget=4000).assemble(chunks, query="finding")

    scores = [p.score for p in pkg.passages]
    middle = len(scores) // 2
    assert max(scores[0], scores[-1]) > scores[middle]
    assert pkg.diagnostics["ordering"] == "edge_weighted"


# ------------------------------------------------------------------- degenerate
def test_empty_retrieval_yields_empty_package():
    pkg = ContextAssembler().assemble([], query="nothing")
    assert pkg.is_empty
    assert pkg.prompt == ""
    assert pkg.cited_markers("[1]") == []


def test_blank_chunks_are_skipped():
    pkg = ContextAssembler().assemble(
        [_chunk("a", "   "), _chunk("b", "Real content here.")], query="x")
    assert [p.chunk_id for p in pkg.passages] == ["b"]


def test_estimate_tokens_is_positive_and_monotonic():
    assert estimate_tokens("") >= 1
    assert estimate_tokens("a" * 400) > estimate_tokens("a" * 40)


# ------------------------------------------------- end-to-end retrieve→prompt
def test_retrieve_context_completes_the_rag_path():
    docs = [
        {"id": "inc-1", "title": "INC-2026-01", "kind": "incident", "ref": "INC-2026-01",
         "text": "UPI settlement failures spiked when the HDFC bank connector timed out."},
        {"id": "rpt-1", "title": "Daily report", "kind": "report", "ref": "RPT-D03",
         "text": "Daily volumes were nominal across all payment service providers."},
        {"id": "sop-1", "title": "Failover SOP", "kind": "sop", "ref": "SOP-014",
         "text": "On bank connector timeout, fail over to the secondary acquiring bank."},
    ]
    retriever = HybridRetriever.from_documents(docs)
    pkg = retriever.retrieve_context("bank connector timeout", top_k=3,
                                     token_budget=500)

    assert not pkg.is_empty
    assert "[1]" in pkg.prompt
    assert "cite the passages" in pkg.prompt          # grounding instruction
    assert pkg.diagnostics["retrieval"]["bm25_candidates"] > 0
    # the lexically matching sources must be present; the unrelated daily
    # report must not crowd them out
    ids = {p.chunk_id for p in pkg.passages}
    assert {"inc-1", "sop-1"} <= ids
    assert all(c["marker"] for c in pkg.citations())

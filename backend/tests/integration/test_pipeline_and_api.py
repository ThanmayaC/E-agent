"""End-to-end test: generate messy sample workbooks → upload via API →
run the full pipeline → assert every artifact and the fixed report exist."""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

BACKEND = Path(__file__).resolve().parents[2]


@pytest.fixture(scope="module")
def client(tmp_path_factory):
    data_dir = tmp_path_factory.mktemp("edip_data")
    import os
    os.environ["EDIP_DATA_DIR"] = str(data_dir)
    os.environ["EDIP_DEBUG"] = "false"
    os.environ["EDIP_LLM_PROVIDER"] = "mock"  # deterministic AI double for CI

    from app.core import config, container
    config.get_settings.cache_clear()
    container.get_container.cache_clear()
    from app.main import create_app
    return TestClient(create_app())


@pytest.fixture(scope="module")
def sample_dir(tmp_path_factory) -> Path:
    out = tmp_path_factory.mktemp("samples")
    subprocess.run([sys.executable, str(BACKEND / "scripts" / "generate_sample_data.py"), str(out)],
                   check=True, cwd=BACKEND)
    return out


def test_full_workflow(client: TestClient, sample_dir: Path):
    # create project
    resp = client.post("/api/v1/projects", json={"name": "Fintech Portfolio"})
    assert resp.status_code == 201
    pid = resp.json()["project_id"]

    # upload every sample workbook
    files = [("files", (f.name, f.read_bytes(),
                        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"))
             for f in sorted(sample_dir.glob("*.xlsx"))]
    resp = client.post(f"/api/v1/projects/{pid}/files", files=files)
    assert resp.status_code == 200
    assert len(resp.json()["uploaded"]) == 5

    # analyze (runs as a background task inside TestClient)
    resp = client.post(f"/api/v1/projects/{pid}/analyze")
    assert resp.status_code == 202
    for _ in range(120):
        status = client.get(f"/api/v1/projects/{pid}/status").json()
        if status["status"] in ("ready", "failed"):
            break
        time.sleep(1)
    assert status["status"] == "ready", str(status)[:2000]

    # datasets: partitions of transactions must be merged
    datasets = client.get(f"/api/v1/projects/{pid}/datasets").json()
    assert len(datasets) >= 4
    txn_ds = max(datasets, key=lambda d: d["row_count"])
    assert txn_ds["row_count"] > 10000
    assert len(txn_ds["merged_from"]) >= 2, "monthly partitions should be merged"

    # semantics: Cust_ID must map to Customer without any manual mapping
    semantics = client.get(f"/api/v1/projects/{pid}/semantics").json()
    cust = [m for m in semantics if m["column"].lower() in ("cust_id", "customer_no")]
    assert cust and all(m["concept"] == "Customer" for m in cust)

    # relationships across files with differing column names (MID vs merchant_id)
    rels = client.get(f"/api/v1/projects/{pid}/relationships").json()
    assert any({r["from_column"].lower(), r["to_column"].lower()} == {"mid", "merchant_id"}
               for r in rels), f"MID↔merchant_id FK not detected: {rels}"

    # KPIs, deterministic signals, forecasts, quality, graph
    kpis = client.get(f"/api/v1/projects/{pid}/kpis").json()
    assert any(k["sparkline"] for k in kpis)
    signals = client.get(f"/api/v1/projects/{pid}/signals").json()
    assert signals, "expected deterministic signals"
    for s in signals:  # facts only — numeric stats, no narrative fields
        assert "stats" in s and "title" not in s and "detail" not in s
    assert client.get(f"/api/v1/projects/{pid}/predictions").json()
    graph = client.get(f"/api/v1/projects/{pid}/graph").json()
    assert graph["stats"]["node_count"] > 20
    quality = client.get(f"/api/v1/projects/{pid}/quality").json()
    assert 0 < quality["overall_score"] <= 100

    # compact business context: the ONLY payload the LLM sees
    ctx = client.get(f"/api/v1/projects/{pid}/context").json()
    for key in ["portfolio_summary", "schema", "relationships", "quality", "kpis",
                "forecast", "anomalies", "correlations", "top_changes",
                "cannibalization", "growth", "executive_metrics"]:
        assert key in ctx, f"missing context key {key}"
    import json as _json
    assert len(_json.dumps(ctx)) < 100_000, "context must stay compact"

    # AI reasoning output: all narrative comes from the (mock) LLM
    ai = client.get(f"/api/v1/projects/{pid}/ai-report").json()
    assert ai["status"] == "ok" and ai["provider"] == "mock"
    assert ai["executive_summary"].startswith("[mock]")
    insights = client.get(f"/api/v1/projects/{pid}/insights").json()
    assert insights["key_insights"] and insights["status"] == "ok"
    recs = client.get(f"/api/v1/projects/{pid}/recommendations").json()
    assert recs["recommendations"] and recs["priority_actions"]

    # every context evidence item is citable; the dataset's limitations are explicit
    assert all("id" in k for k in ctx["kpis"])
    assert "data_limitations" in ctx and ctx["data_limitations"]["missing_dimensions"]

    # every AI statement is labelled and deterministically verified
    for insight in ai["key_insights"]:
        assert insight["statement_type"] in (
            "fact", "statistical_finding", "hypothesis", "unknown")
        assert insight["verification"] in ("evidence_verified", "unverified")
        if insight["statement_type"] in ("fact", "statistical_finding"):
            assert insight["evidence_ids"], "facts must cite evidence"
    for cause in ai["root_causes"]:
        assert cause["statement_type"] == "hypothesis", "causes are never asserted"
        assert "missing_evidence" in cause

    # audit trail: statements resolved to the deterministic evidence they cite
    audit = client.get(f"/api/v1/projects/{pid}/report/audit").json()
    assert audit["insights"] and audit["root_cause_hypotheses"]
    verified = [i for i in audit["insights"] if i["verification"] == "evidence_verified"]
    assert verified and verified[0]["evidence"], "cited evidence must resolve to items"

    # fixed executive report structure — always the same sections
    report = client.get(f"/api/v1/projects/{pid}/report").json()
    for section in ["executive_summary", "management_summary", "dataset_summary",
                    "kpi_analysis", "signals", "business_insights",
                    "root_cause_analysis", "opportunity_analysis", "risk_analysis",
                    "predictive_analytics", "recommendations", "appendix",
                    "report_confidence", "data_limitations",
                    "deterministic_recommendations"]:
        assert section in report, f"missing report section {section}"
    assert 0 <= report["executive_summary"]["overall_health_score"] <= 100
    assert report["executive_summary"]["summary"].startswith("[mock]")
    assert report["meta"]["ai"]["provider"] == "mock"
    # deterministic confidence model: documented formula + components
    assert 0 <= report["report_confidence"]["overall"] <= 1
    assert "formula" in report["report_confidence"]
    assert report["meta"]["report_version"] >= 1
    # rule-derived recommendations cite their trigger
    assert all(r["trigger"] for r in report["deterministic_recommendations"])
    # gated forecasts: unavailable ones never carry values
    for f in report["predictive_analytics"]["forecasts"]:
        if f["status"] == "unavailable":
            assert f["values"] == []

    md = client.get(f"/api/v1/projects/{pid}/report/markdown").json()["markdown"]
    assert "# Executive Report" in md and "## 10. Recommendations (AI)" in md

    # copilot: retrieval -> context -> LLM -> grounded answer
    resp = client.post(f"/api/v1/projects/{pid}/copilot/chat",
                       json={"question": "Which KPI is declining and why?"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok" and body["answer"]
    assert "sources" in body and "cited_facts" in body

    # ad-hoc SQL on the DuckDB warehouse
    resp = client.post(f"/api/v1/projects/{pid}/query",
                       json={"sql": f'SELECT COUNT(*) FROM "{txn_ds["dataset_id"]}"'})
    assert resp.status_code == 200
    assert resp.json()["rows"][0][0] == txn_ds["row_count"]

    # write queries rejected
    resp = client.post(f"/api/v1/projects/{pid}/query", json={"sql": "DROP TABLE x"})
    assert resp.status_code == 422


def _poll(client: TestClient, pid: str, *, until: tuple[str, ...]) -> str:
    for _ in range(120):
        status = client.get(f"/api/v1/projects/{pid}/status").json()["status"]
        if status in until:
            return status
        time.sleep(1)
    return status


def test_confidence_gate_pauses_then_resumes(client: TestClient):
    """An unintelligible dataset must NOT be guessed at: the pipeline pauses
    with a clarification question, and only proceeds once the user answers —
    after which the answer is remembered and never asked again."""
    import io
    import pandas as pd

    resp = client.post("/api/v1/projects", json={"name": "Mystery Data"})
    pid = resp.json()["project_id"]

    df = pd.DataFrame({"foo": ["a", "b", "c"] * 40, "bar": ["x", "y", "z"] * 40,
                       "ziz": list(range(120)), "qux": ["p", "q", "r", "s"] * 30})
    buf = io.BytesIO()
    df.to_excel(buf, index=False)
    client.post(f"/api/v1/projects/{pid}/files",
                files=[("files", ("mystery.xlsx", buf.getvalue(),
                        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"))])

    # analyze -> pauses instead of guessing
    client.post(f"/api/v1/projects/{pid}/analyze")
    assert _poll(client, pid, until=("awaiting_clarification", "ready", "failed")) \
        == "awaiting_clarification"

    # clarification questions are surfaced (never a hallucinated report)
    clar = client.get(f"/api/v1/projects/{pid}/clarifications").json()
    assert clar["confidence"] < clar["threshold"]
    assert clar["questions"], "expected at least one clarification question"
    assert client.get(f"/api/v1/projects/{pid}/ai-report").status_code == 404

    # answer -> pipeline resumes and reaches a full report
    answers = [{"question_id": q["id"], "answer": "Product catalog; ziz is the metric."}
               for q in clar["questions"]]
    resp = client.post(f"/api/v1/projects/{pid}/clarifications", json={"answers": answers})
    assert resp.status_code == 202
    assert _poll(client, pid, until=("ready", "failed")) == "ready"

    # the answer reached the LLM context and is remembered organization-wide
    ctx = client.get(f"/api/v1/projects/{pid}/context").json()
    assert ctx["understanding"]["clarifications"], "answer must be injected into context"
    assert client.get("/api/v1/knowledge").json()["clarifications"]

    # LangGraph orchestrator: the SAME checkpointed run pauses at the gate
    # and resumes in place — the control plane holds the durable trace
    from app.core.container import get_container
    if get_container().langgraph is not None:
        assert resp.json().get("resumed_run"), "answers must resume the paused run"
        runs = client.get(f"/api/v1/projects/{pid}/runs").json()
        assert runs and runs[0]["status"] == "ready"
        run_id = runs[0]["run_id"]
        events = client.get(f"/api/v1/projects/{pid}/runs/{run_id}/events").json()
        by_gate = [e["event"] for e in events if e["node"] == "confidence_gate"]
        assert "interrupt" in by_gate and "resumed" in by_gate
        # evidence + verified statements landed in the ledger
        assert client.get(f"/api/v1/projects/{pid}/evidence-ledger").json()
        stmts = client.get(f"/api/v1/projects/{pid}/statements").json()
        assert stmts and all("verification" in s for s in stmts)


def test_delete_project_removes_everything(client: TestClient):
    import io
    import pandas as pd

    resp = client.post("/api/v1/projects", json={"name": "Disposable"})
    pid = resp.json()["project_id"]
    df = pd.DataFrame({"Month": pd.date_range("2024-01-01", periods=6, freq="MS"),
                       "Revenue": [100, 110, 105, 120, 118, 130]})
    buf = io.BytesIO()
    df.to_excel(buf, index=False)
    client.post(f"/api/v1/projects/{pid}/files",
                files=[("files", ("r.xlsx", buf.getvalue(),
                        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"))])

    resp = client.delete(f"/api/v1/projects/{pid}")
    assert resp.status_code == 200
    assert resp.json()["status"] == "deleted"
    # gone from every surface: state, list, artifacts
    assert client.get(f"/api/v1/projects/{pid}").status_code == 404
    assert pid not in [p["project_id"] for p in client.get("/api/v1/projects").json()]
    assert client.get(f"/api/v1/projects/{pid}/report").status_code == 404
    # deleting a non-existent project is a clean 404
    assert client.delete(f"/api/v1/projects/{pid}").status_code == 404

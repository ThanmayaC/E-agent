"""Bootstrap the Enterprise Brain from the synthetic NPCI UPI corpus (V3.0).

One command turns the generated organization into a living Enterprise Brain:

    1. generate the enterprise (root generate_enterprise.py) if it is missing
    2. register each day/type folder (and master/) as a document source, using
       the source kind the INGEST_MANIFEST assigns so every document is
       categorised correctly (rca / sop-family / meeting / product / document)
    3. force one synchronization so the ordinary pipeline —
       sync -> parse -> chunk -> embed -> observe entities -> link -> context —
       runs immediately instead of waiting for the scheduler heartbeat

The corpus is the deterministic NPCI (Synthetic Demonstration) / UPI Products
week produced by ``generate_enterprise.py``. Because the document reader
recurses and a document's category is derived from its source kind, pointing
one source at each ``day_XX/<type>`` folder is all that is needed — no backend
change. Re-running is safe: registration is skipped when a source already
exists, and the sync re-syncs by content hash.

    # from the repository root:
    python generate_enterprise.py --days 7 --seed 2026
    cd backend && python scripts/bootstrap_enterprise_demo.py

Everything persists to disk (sync store, document store, vector collections,
organizational model, knowledge graph), so a backend started afterwards loads
a Brain that already knows the whole organization.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

# Make ``app`` importable when run as a plain script.
BACKEND = Path(__file__).resolve().parents[1]
REPO = BACKEND.parent
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

ENTERPRISE_DIR = REPO / "enterprise_data"
MANIFEST = ENTERPRISE_DIR / "INGEST_MANIFEST.json"
GENERATOR = REPO / "generate_enterprise.py"


def ensure_corpus() -> dict:
    """Generate the enterprise if it has not been generated yet, then load its
    ingestion manifest."""
    if not MANIFEST.exists():
        print("1. Generating the synthetic NPCI UPI enterprise (seed 2026) ...")
        subprocess.run([sys.executable, str(GENERATOR),
                        "--days", "7", "--seed", "2026"], check=True, cwd=REPO)
    else:
        print("1. Using existing enterprise_data/ (delete it to regenerate).")
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def _link_crossrefs(container) -> int:
    """Turn the corpus's declared references (enterprise_data/CROSSREF.json)
    into edges between the document nodes the ingestion pipeline created.

    Nodes are matched by their graph identity — kind (document category) plus
    label (the filename stem) — which the generator recorded for every
    artifact, so the two views line up without reproducing any internal id
    rule. All edges are written in one batch."""
    crossref_path = ENTERPRISE_DIR / "CROSSREF.json"
    if not crossref_path.exists():
        return 0
    crossref = json.loads(crossref_path.read_text(encoding="utf-8"))
    graph = container.enterprise_graph
    # Index every node by (kind, label) -> node id.
    index: dict[tuple[str, str], str] = {}
    for node in graph.payload(limit=0)["nodes"]:
        index[(node.get("kind", ""), str(node.get("label", "")))] = node["id"]

    def node_id(meta: dict) -> str:
        return index.get((meta["category"], meta["stem"]), "")

    added = 0
    with graph.batch() as g:
        for art_id, meta in crossref.items():
            src = node_id(meta)
            if not src:
                continue
            for ref in meta.get("refs", []):
                tgt_meta = crossref.get(ref)
                if not tgt_meta:
                    continue
                tgt = node_id(tgt_meta)
                if tgt and tgt != src:
                    g._relate(src, tgt, "references")  # noqa: SLF001
                    added += 1
    return added


def main() -> None:
    manifest = ensure_corpus()

    print("\n2. Building the platform container (Brain startup) ...")
    from app.core.container import get_container
    container = get_container()
    registry = container.sync.registry

    # The manifest lists every day/type folder with the source kind that gives
    # it the right document category. The master folder rides in as a document
    # folder so the org overview, storyline and CSVs are searchable too.
    sources_to_register = list(manifest["ingest_sources"])
    sources_to_register.append({
        "name": "npci-master",
        "kind": "document_folder",
        "location": manifest["master"],
        "description": "Master data, org overview, and the weekly KPI workbook",
    })

    print(f"\n3. Registering {len(sources_to_register)} document sources ...")
    registered: list[dict] = []
    existing = {s["name"]: s for s in registry.sources()}
    for spec in sources_to_register:
        if spec["name"] in existing:
            registered.append(existing[spec["name"]])
            continue
        source = registry.register(
            name=spec["name"], kind=spec["kind"], location=spec["location"],
            auth={"kind": "none"}, cadence="hourly",
            description=spec["description"])
        registered.append(source)
    print(f"   registered/loaded {len(registered)} sources "
          f"({manifest['organization']} / {manifest['department']})")

    print("\n4. Synchronizing - parse -> chunk -> embed -> observe -> link ...")
    total_changed = 0
    for source in registered:
        result = container.sync.refresh(source_id=source["source_id"],
                                        trigger="bootstrap")
        total_changed += result.get("changed_records", 0)
    print(f"   {total_changed} document record(s) changed across all sources")

    # Materialise the corpus's declared cross-references as knowledge-graph
    # edges. The ingestion pipeline creates a node per document; this links
    # them using the Refs each artifact declared, via the enterprise graph's
    # public relate() API (no backend change). Result: no isolated node.
    print("\n4b. Linking cross-references into the knowledge graph ...")
    edges = _link_crossrefs(container)
    print(f"   added {edges} reference edge(s) between documents")

    print("\n5. Enterprise Brain now holds:")
    docs = container.sync.documents.status() if container.sync.documents else {}
    org = container.sync.organization.counts()  # flat {kind: count}
    populated = {k: v for k, v in org.items() if v}
    graph = container.brain.statistics().get("graph", {}) if container.brain \
        else {}
    print(f"   documents indexed : {docs.get('documents', 0)}")
    if docs.get("by_category"):
        print(f"   by category       : "
              f"{', '.join(f'{k}:{v}' for k, v in sorted(docs['by_category'].items()))}")
    print(f"   entities observed : {sum(org.values())} "
          f"({', '.join(f'{k}:{v}' for k, v in sorted(populated.items()))})")
    print(f"   graph nodes/edges : {graph.get('node_count', 0)} / "
          f"{graph.get('edge_count', 0)}")
    print("\nDone. Start the backend and ask the Enterprise Brain a "
          "cross-source question, e.g.:")
    print('   "Why did UPI Autopay success dip this week and what did we do '
          'about it?"')


if __name__ == "__main__":
    main()

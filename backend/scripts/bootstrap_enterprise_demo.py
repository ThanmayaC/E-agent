"""Bootstrap the Enterprise Brain demonstration (V2.3).

One command turns the synthetic corpus into a living Enterprise Brain:

    1. generate the corpus (scripts/generate_enterprise_corpus.py)
    2. register each folder as a document source (auth-free, local)
    3. force one synchronization so the ordinary pipeline —
       sync -> parse -> chunk -> embed -> observe entities -> link -> context —
       runs immediately instead of waiting for the 15-minute heartbeat

Everything is persisted to disk (sync store, document store, vector
collections, organizational model, knowledge graph), so a backend started
afterwards loads a Brain that already knows the whole organization. Re-running
is safe: registration is skipped when a source already exists, and the sync
re-syncs by content hash.

    python scripts/bootstrap_enterprise_demo.py

Run from the ``backend`` directory (same environment as the tests).
"""
from __future__ import annotations

import sys
from pathlib import Path

# Make ``app`` and ``scripts`` importable when run as a plain script.
BACKEND = Path(__file__).resolve().parents[1]
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from scripts import generate_enterprise_corpus as corpus  # noqa: E402

# Each corpus folder -> the document source kind that assigns the right entity
# kind downstream. KPI/merchant workbooks ride in as documents too, so their
# numbers become searchable chunks the Brain can quote.
FOLDER_KINDS: dict[str, tuple[str, str]] = {
    "sops": ("sop_repository", "Standard Operating Procedures"),
    "rcas": ("rca_repository", "Root-Cause Analyses"),
    "policies": ("policy_repository", "Enterprise policies"),
    "meetings": ("meeting_notes",
                 "Meeting notes, decision logs, action items, emails, Teams"),
    "product": ("product_documents", "Product docs, BRDs, roadmaps"),
    "reports": ("document_folder",
                "Executive, weekly, monthly, merchant, and risk reports"),
    "kpis": ("document_folder", "KPI and merchant performance workbooks"),
}


def main() -> None:
    print("1. Generating synthetic enterprise corpus ...")
    corpus.main()
    root = corpus.OUT

    print("\n2. Building the platform container (Brain startup) ...")
    from app.core.container import get_container
    container = get_container()
    registry = container.sync.registry

    print("\n3. Registering document sources ...")
    sources: list[dict] = []
    existing_names = {s["name"] for s in registry.sources()}
    for folder, (kind, description) in FOLDER_KINDS.items():
        location = str((root / folder).resolve())
        name = f"enterprise-{folder}"
        if name in existing_names:
            source = next(s for s in registry.sources() if s["name"] == name)
            print(f"   - {name:<22} already registered")
        else:
            source = registry.register(
                name=name, kind=kind, location=location,
                auth={"kind": "none"}, cadence="hourly",
                description=description)
            print(f"   + {name:<22} {kind}")
        sources.append(source)

    print("\n4. Synchronizing - parse -> chunk -> embed -> observe -> link ...")
    for source in sources:
        result = container.sync.refresh(source_id=source["source_id"],
                                        trigger="bootstrap")
        changed = result.get("changed_records", 0)
        print(f"   - {source['name']:<22} {result.get('status'):<10} "
              f"{changed} record(s) changed")

    # 5. Report what the Brain now holds.
    print("\n5. Enterprise Brain now holds:")
    docs = container.sync.documents.status() if container.sync.documents else {}
    org = container.sync.organization.counts()  # flat {kind: count}
    populated = {k: v for k, v in org.items() if v}
    graph = container.brain.statistics().get("graph", {}) if container.brain \
        else {}
    print(f"   documents indexed : {docs.get('documents', 0)}")
    print(f"   entities observed : {sum(org.values())} "
          f"({', '.join(f'{k}:{v}' for k, v in sorted(populated.items()))})")
    print(f"   graph nodes/edges : {graph.get('node_count', 0)} / "
          f"{graph.get('edge_count', 0)}")
    print("\nDone. Start the backend and ask the Enterprise Brain a "
          "cross-source question, e.g.:")
    print("   \"Why did settlement success dip in March and what did we do "
          "about it?\"")


if __name__ == "__main__":
    main()

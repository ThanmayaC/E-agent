"""Relationship Engine — how the organization is wired, kept current.

The Data Intelligence Module already detects relationships *inside* a project
(foreign keys proven by value overlap). This engine works at the level above:
how the enterprise's *entities* relate, across systems and across projects.

    ownership       an entity belongs to a person or a team
    dependency      an entity needs another to function
    hierarchy       parent → child (department → team → employee)
    association     product ↔ customer, customer ↔ merchant, merchant ↔ bank
    cross_domain    the same entity seen in two systems — the link that makes
                    the model *one* organization instead of several

Relationships are **evidenced**, never assumed: each carries what produced it
(a shared record, a project graph, an ownership column) and a confidence. The
enterprise knowledge graph stores them; this engine detects, explains, and
keeps them fresh. Detection is incremental — it reads the sync delta, not the
world.
"""
from __future__ import annotations

from typing import Any

from app.core.logging import get_logger
from app.sync.organization import OrganizationalModel, owner_column_in
from app.sync.store import SyncStore, new_id, now_iso

logger = get_logger(__name__)

RELATIONSHIP_KINDS = ("ownership", "dependency", "hierarchy", "association",
                      "cross_domain")

# Which entity pairings are meaningful associations. An association between
# two unrelated kinds is noise, and noise in a knowledge graph is worse than
# a missing edge — it gets reasoned over.
ASSOCIATION_PAIRS = {
    frozenset(("customer", "product")), frozenset(("customer", "merchant")),
    frozenset(("merchant", "bank")), frozenset(("merchant", "product")),
    frozenset(("customer", "bank")), frozenset(("product", "kpi")),
    frozenset(("project", "report")), frozenset(("project", "kpi")),
    frozenset(("employee", "team")), frozenset(("team", "department")),
}

HIERARCHY_PAIRS = {("department", "team"), ("team", "employee"),
                   ("project", "report")}

MAX_RELATIONSHIPS = 20_000


class RelationshipEngine:
    def __init__(self, store: SyncStore, organization: OrganizationalModel,
                 graph=None, bus=None):
        self._store = store
        self._org = organization
        self._graph = graph
        self._bus = bus

    def attach_bus(self, bus) -> None:
        """Announce relationship discoveries on the enterprise event bus."""
        self._bus = bus

    # ------------------------------------------------------------- observe
    def relate(self, source_id: str, target_id: str, kind: str,
               evidence: str = "", confidence: float = 0.5,
               source_system: str = "") -> tuple[dict, bool]:
        """Record a relationship. Returns ``(relationship, changed)``.

        Idempotent: re-observing an existing relationship refreshes it and
        strengthens its confidence (seen twice is better evidence than seen
        once) without duplicating the edge.
        """
        if kind not in RELATIONSHIP_KINDS:
            raise ValueError(f"Unknown relationship kind: {kind}")
        if source_id == target_id:
            raise ValueError("An entity cannot relate to itself")
        relationship_id = f"{source_id}|{kind}|{target_id}"

        with self._store.mutate("relationships") as relationships:
            existing = next((r for r in relationships
                             if r["relationship_id"] == relationship_id), None)
            if existing is None:
                if len(relationships) >= MAX_RELATIONSHIPS:
                    raise ValueError(
                        f"Refusing to exceed {MAX_RELATIONSHIPS} relationships "
                        f"— the detector is producing noise")
                relationship = {
                    "relationship_id": relationship_id,
                    "internal_id": new_id("rel"),
                    "source": source_id, "target": target_id, "kind": kind,
                    "evidence": evidence[:300], "confidence": round(confidence, 3),
                    "source_system": source_system[:120], "observations": 1,
                    "first_seen": now_iso(), "last_seen": now_iso(),
                    "updated_at": now_iso(),
                }
                relationships.append(relationship)
                changed = True
            else:
                relationship = existing
                relationship["observations"] += 1
                relationship["last_seen"] = now_iso()
                # Corroboration raises confidence toward, never past, certainty.
                strengthened = min(
                    round(relationship["confidence"] + 0.05, 3), 0.95)
                changed = strengthened != relationship["confidence"]
                relationship["confidence"] = strengthened
                if evidence and evidence[:300] != relationship["evidence"]:
                    relationship["evidence"] = evidence[:300]
                    changed = True
                if changed:
                    relationship["updated_at"] = now_iso()

        if existing is None:
            self._mirror(relationship)
            self._announce(relationship)
        return relationship, changed

    # ------------------------------------------------------------- detect
    def detect_from_sync(self, source_name: str, deltas: list) -> dict[str, int]:
        """Detect relationships from the records a sync changed.

        Two signals, both deterministic and both evidenced:

        - **ownership** — a record naming an entity and an owner is an
          ownership claim from that system;
        - **association** — two entity-bearing columns on the same record mean
          those two entities co-occur in the business, e.g. a transaction row
          carrying both a customer and a merchant.
        """
        found = {"ownership": 0, "association": 0}
        for delta in deltas:
            for item in list(delta.added) + list(delta.changed):
                record = item["record"]
                entities = self._entities_in(record)
                if not entities:
                    continue
                found["ownership"] += self._detect_ownership(
                    record, entities, source_name, delta.table)
                found["association"] += self._detect_associations(
                    entities, source_name, delta.table)
        return found

    def _entities_in(self, record: dict) -> list[dict]:
        """Which known entities this record mentions. Resolution goes through
        the organizational model, so an alias in one system finds the entity
        another system named differently — that is the cross-system join."""
        seen: dict[str, dict] = {}
        for value in record.values():
            if value in (None, "") or isinstance(value, (bool, float)):
                continue
            text = str(value).strip()
            if not text or len(text) > 120:
                continue
            entity = self._org.resolve(text)
            if entity is not None:
                seen[entity["entity_id"]] = entity
        return list(seen.values())

    def _detect_ownership(self, record: dict, entities: list[dict],
                          source_name: str, table: str) -> int:
        owner_column = owner_column_in(list(record.keys()))
        if not owner_column:
            return 0
        owner_name = str(record.get(owner_column) or "").strip()
        if not owner_name:
            return 0
        owner, _ = self._org.observe(
            "employee", owner_name, source=source_name,
            attributes={"discovered_as": "owner"})
        count = 0
        for entity in entities:
            if entity["entity_id"] == owner["entity_id"]:
                continue
            _, changed = self.relate(
                owner["entity_id"], entity["entity_id"], "ownership",
                evidence=f"{table}.{owner_column} names {owner_name} as owner",
                confidence=0.7, source_system=source_name)
            count += 1 if changed else 0
        return count

    def _detect_associations(self, entities: list[dict], source_name: str,
                             table: str) -> int:
        count = 0
        for i, first in enumerate(entities):
            for second in entities[i + 1:]:
                pair = frozenset((first["kind"], second["kind"]))
                if pair not in ASSOCIATION_PAIRS:
                    continue
                kind = "hierarchy" if (first["kind"], second["kind"]) \
                    in HIERARCHY_PAIRS else "association"
                _, changed = self.relate(
                    first["entity_id"], second["entity_id"], kind,
                    evidence=f"co-occur in {source_name}.{table}",
                    confidence=0.6, source_system=source_name)
                count += 1 if changed else 0
        return count

    def detect_cross_domain(self) -> dict[str, int]:
        """The link that makes one organization out of many systems: the same
        entity observed in two different sources. Nothing is merged — the
        entity already *is* one record; this records that two systems agree it
        exists, which is what makes the model trustworthy."""
        linked = 0
        for entity in self._org.entities(limit=MAX_RELATIONSHIPS):
            if len(entity["sources"]) < 2:
                continue
            attributes = entity.get("attributes") or {}
            if attributes.get("cross_domain_sources") == entity["sources"]:
                continue  # already recorded for exactly this source set
            self._org.observe(
                entity["kind"], entity["name"],
                attributes={"cross_domain_sources": list(entity["sources"])})
            linked += 1
            if self._bus is not None:
                try:
                    self._bus.publish(
                        "RelationshipDiscovered",
                        {"kind": "cross_domain", "entity": entity["name"],
                         "entity_kind": entity["kind"],
                         "systems": entity["sources"]},
                        source="relationship_engine")
                except Exception:  # noqa: BLE001
                    logger.exception("Cross-domain event publication failed")
        return {"cross_domain_entities": linked}

    def detect_dependencies(self, store) -> dict[str, int]:
        """Project-level dependencies from what Data Intelligence proved: a
        detected foreign key between two datasets is a dependency between the
        entities they carry. Reuse, not re-detection."""
        found = 0
        for pid in store.list_projects():
            relationships = store.load(pid, "relationships", []) or []
            for link in relationships:
                if not isinstance(link, dict):
                    continue
                left = self._org.resolve(str(link.get("left_table", "")))
                right = self._org.resolve(str(link.get("right_table", "")))
                if left is None or right is None \
                        or left["entity_id"] == right["entity_id"]:
                    continue
                _, changed = self.relate(
                    left["entity_id"], right["entity_id"], "dependency",
                    evidence=f"foreign key {link.get('left_column')} → "
                             f"{link.get('right_column')} "
                             f"(overlap {link.get('overlap', '?')})",
                    confidence=float(link.get("confidence") or 0.7),
                    source_system=f"project:{pid}")
                found += 1 if changed else 0
        return {"dependencies": found}

    # -------------------------------------------------------------- mirror
    def _mirror(self, relationship: dict) -> None:
        if self._graph is None:
            return
        try:
            self._graph.relate(relationship["source"], relationship["target"],
                               kind=relationship["kind"],
                               confidence=relationship["confidence"],
                               evidence=relationship["evidence"])
        except Exception:  # noqa: BLE001 — mirroring degrades, never fails
            logger.exception("Graph mirror failed for %s",
                             relationship["relationship_id"])

    def _announce(self, relationship: dict) -> None:
        if self._bus is None:
            return
        try:
            self._bus.publish("RelationshipDiscovered",
                              {"kind": relationship["kind"],
                               "source": relationship["source"],
                               "target": relationship["target"],
                               "confidence": relationship["confidence"]},
                              source="relationship_engine")
        except Exception:  # noqa: BLE001
            logger.exception("Relationship event publication failed")

    # ---------------------------------------------------------------- read
    def relationships(self, kind: str = "", entity_id: str = "",
                      min_confidence: float = 0.0,
                      limit: int = 200) -> list[dict]:
        items = self._store.read("relationships")
        if kind:
            items = [r for r in items if r["kind"] == kind]
        if entity_id:
            items = [r for r in items
                     if r["source"] == entity_id or r["target"] == entity_id]
        if min_confidence:
            items = [r for r in items if r["confidence"] >= min_confidence]
        return sorted(items, key=lambda r: r["confidence"],
                      reverse=True)[:limit]

    def neighbourhood(self, entity_id: str) -> dict[str, Any]:
        """One entity and everything it is wired to — the business answer to
        "what does this touch?"."""
        entity = self._org.get(entity_id)
        if entity is None:
            return {}
        links = self.relationships(entity_id=entity_id, limit=200)
        out = []
        for link in links:
            other_id = (link["target"] if link["source"] == entity_id
                        else link["source"])
            other = self._org.get(other_id)
            out.append({
                "entity_id": other_id,
                "name": other["name"] if other else other_id,
                "kind": other["kind"] if other else "",
                "relationship": link["kind"],
                "direction": "outgoing" if link["source"] == entity_id
                else "incoming",
                "confidence": link["confidence"], "evidence": link["evidence"]})
        return {"entity": entity, "related": out}

    def stats(self) -> dict:
        items = self._store.read("relationships")
        by_kind: dict[str, int] = {}
        for r in items:
            by_kind[r["kind"]] = by_kind.get(r["kind"], 0) + 1
        return {"total": len(items), "by_kind": by_kind,
                "high_confidence": sum(1 for r in items
                                       if r["confidence"] >= 0.7),
                "systems": sorted({r["source_system"] for r in items
                                   if r["source_system"]})}

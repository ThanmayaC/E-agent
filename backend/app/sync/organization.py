"""Organizational Model — the unified model of what the enterprise *is*.

Not a data model: a business model. Products, customers, merchants, banks,
teams, departments, employees, reports, projects, meetings, business rules,
and KPIs, each with the four things the SDS requires:

    identity       a stable id, a canonical name, and the aliases it is known
                   by in different systems (``MID`` here, ``merchant_id``
                   there — one merchant)
    relationships  held in the enterprise knowledge graph, not duplicated here
    ownership      who owns it, and where that claim came from
    history        every change, appended, never overwritten

Entities are *observed*, never invented: each one is derived deterministically
from something the platform already has — a synced record, a semantic mapping,
a project artifact, a report, a business rule. Every entity carries the
sources it was seen in, so "where did this come from?" is always answerable.

Construction is incremental. ``observe`` upserts one entity and returns
whether anything actually changed, so a sync that touches nothing costs
nothing downstream.
"""
from __future__ import annotations

import re
import threading
from typing import Any

from app.core.logging import get_logger
from app.sync.store import SyncStore, new_id, now_iso

logger = get_logger(__name__)

# The SDS entity catalogue. Kinds are closed: an organizational model that
# accepts any string is a bag of nouns, not a model. The second row is the
# V2 additions — organizational memory of documents and communications:
# SOPs, RCAs, policies, decisions, emails, tasks, trends, and the generic
# document (relationships between entities live in the knowledge graph,
# as before).
ENTITY_KINDS = (
    "product", "customer", "merchant", "bank", "team", "department",
    "employee", "report", "project", "meeting", "business_rule", "kpi",
    "sop", "rca", "policy", "document", "decision", "email", "task", "trend",
)

# Business concepts (from the semantic layer / ontology) → entity kind. This
# is the bridge between "a column means Customer" and "the organization has
# customers".
CONCEPT_TO_KIND = {
    "customer": "customer", "merchant": "merchant", "product": "product",
    "bank": "bank", "employee": "employee", "team": "team",
    "department": "department", "account": "customer", "vendor": "merchant",
    "supplier": "merchant", "store": "merchant", "issuer": "bank",
    "acquirer": "bank", "sku": "product", "item": "product",
    # V2: documents and communications observed through synchronization.
    "sop": "sop", "rca": "rca", "policy": "policy", "email": "email",
    "decision": "decision", "task": "task", "trend": "trend",
}

# Column-name hints for ownership, checked against synced records.
OWNER_HINTS = ("owner", "owned_by", "manager", "responsible", "account_manager",
               "assigned_to", "lead", "head")

MAX_HISTORY = 40
MAX_ALIASES = 20
MAX_ENTITIES_PER_KIND = 5_000


class OrganizationalModel:
    """Builds and maintains the enterprise's entities."""

    def __init__(self, store: SyncStore, graph=None, knowledge=None, bus=None):
        self._store = store
        self._graph = graph          # EnterpriseKnowledgeGraph (relationships)
        self._knowledge = knowledge  # KnowledgeStore (entity definitions)
        self._bus = bus
        self._lock = threading.RLock()

    def attach_bus(self, bus) -> None:
        """Announce entity discoveries on the enterprise event bus."""
        self._bus = bus

    # ------------------------------------------------------------- observe
    def observe(self, kind: str, name: str, source: str = "",
                aliases: list[str] | None = None, owner: str = "",
                owner_source: str = "", attributes: dict | None = None,
                project_id: str = "") -> tuple[dict, bool]:
        """Record that an entity exists. Returns ``(entity, changed)``.

        Idempotent by identity: observing the same entity again enriches it
        (new alias, new source, an owner we did not know) and touches
        ``last_seen``, but reports ``changed=False`` when nothing is new — the
        signal the refresh pipeline uses to skip work.
        """
        if kind not in ENTITY_KINDS:
            raise ValueError(f"Unknown entity kind: {kind}")
        canonical = _canonical(name)
        if not canonical:
            raise ValueError("An entity needs a name")
        entity_id = f"{kind}:{canonical}"

        with self._store.mutate("entities") as entities:
            existing = next((e for e in entities
                             if e["entity_id"] == entity_id), None)
            if existing is None:
                if sum(1 for e in entities if e["kind"] == kind) \
                        >= MAX_ENTITIES_PER_KIND:
                    raise ValueError(
                        f"Too many '{kind}' entities — refusing to grow the "
                        f"organizational model past {MAX_ENTITIES_PER_KIND} "
                        f"per kind; this usually means an identifier column "
                        f"was mistaken for a business entity")
                entity = {
                    "entity_id": entity_id, "internal_id": new_id("ent"),
                    "kind": kind, "name": name.strip()[:200],
                    "canonical": canonical,
                    "aliases": _dedupe(aliases or [], canonical),
                    "owner": owner[:120], "owner_source": owner_source[:120],
                    "attributes": attributes or {},
                    "sources": [source] if source else [],
                    "projects": [project_id] if project_id else [],
                    "relationship_count": 0,
                    "history": [{"at": now_iso(), "change": "discovered",
                                 "source": source, "detail": f"first seen in "
                                                             f"{source or 'the platform'}"}],
                    "first_seen": now_iso(), "last_seen": now_iso(),
                    "updated_at": now_iso(),
                }
                entities.append(entity)
                changed = True
            else:
                entity = existing
                changed = self._enrich(entity, source, aliases, owner,
                                       owner_source, attributes, project_id)
                entity["last_seen"] = now_iso()

        if changed:
            self._mirror(entity)
            self._announce(entity, new=existing is None)
        return entity, changed

    def _enrich(self, entity: dict, source: str, aliases: list[str] | None,
                owner: str, owner_source: str, attributes: dict | None,
                project_id: str) -> bool:
        """Merge new observations into a known entity. Knowledge is added,
        never lost: an owner we already have is not overwritten by an empty
        one, and history records every real change."""
        changed = False

        for alias in _dedupe(aliases or [], entity["canonical"]):
            if alias not in entity["aliases"] \
                    and len(entity["aliases"]) < MAX_ALIASES:
                entity["aliases"].append(alias)
                self._note(entity, "alias_added", source, alias)
                changed = True

        if source and source not in entity["sources"]:
            entity["sources"].append(source)
            self._note(entity, "source_added", source,
                       f"also seen in {source}")
            changed = True

        if project_id and project_id not in entity["projects"]:
            entity["projects"].append(project_id)
            changed = True

        if owner and owner != entity["owner"]:
            previous = entity["owner"]
            entity["owner"] = owner[:120]
            entity["owner_source"] = owner_source[:120]
            self._note(entity, "owner_changed", source,
                       f"{previous or 'unowned'} → {owner}")
            changed = True

        for key, value in (attributes or {}).items():
            if entity["attributes"].get(key) != value:
                entity["attributes"][key] = value
                changed = True

        if changed:
            entity["updated_at"] = now_iso()
        return changed

    def _note(self, entity: dict, change: str, source: str,
              detail: str) -> None:
        entity["history"].append({"at": now_iso(), "change": change,
                                  "source": source, "detail": detail[:200]})
        entity["history"] = entity["history"][-MAX_HISTORY:]

    # ------------------------------------------------- construction sources
    def observe_from_sync(self, source_name: str, deltas: list) -> dict[str, int]:
        """Derive entities from the records a sync actually changed.

        Only added/changed records are inspected — that is the whole point of
        the delta. A table named ``merchants`` whose columns mean Merchant
        contributes merchants; a table nobody can interpret contributes
        nothing, which is correct: this model would rather be small and true
        than large and invented.
        """
        discovered, updated = 0, 0
        for delta in deltas:
            kind = _kind_for_table(delta.table)
            if kind is None:
                continue
            name_column = _name_column(delta.columns, kind)
            if name_column is None:
                continue
            owner_column = owner_column_in(delta.columns)
            for item in list(delta.added) + list(delta.changed):
                record = item["record"]
                name = record.get(name_column)
                if not name or not str(name).strip():
                    continue
                _, changed = self.observe(
                    kind, str(name), source=source_name,
                    aliases=_aliases_from(record, name_column),
                    owner=str(record.get(owner_column) or "")
                    if owner_column else "",
                    owner_source=f"{source_name}.{owner_column}"
                    if owner_column else "",
                    attributes={"table": delta.table})
                if changed:
                    if item in delta.added:
                        discovered += 1
                    else:
                        updated += 1
        return {"discovered": discovered, "updated": updated}

    def observe_from_semantics(self, project_id: str, project_name: str,
                               semantic_layer: dict) -> dict[str, int]:
        """Derive entities from what the semantic layer already inferred:
        a column meaning ``Customer`` proves the organization has customers.

        This is the reuse seam — the Data Intelligence Module did the
        inference, the organizational model just records the consequence.
        """
        discovered = 0
        mappings = (semantic_layer or {}).get("mappings") or []
        for mapping in mappings:
            concept = str(mapping.get("concept", "")).strip().lower()
            kind = CONCEPT_TO_KIND.get(concept)
            if kind is None:
                continue
            canonical = (mapping.get("canonical") or mapping.get("column")
                         or concept)
            _, changed = self.observe(
                kind, str(canonical), source=f"project:{project_name}",
                aliases=[str(mapping.get("column", ""))],
                attributes={"concept": concept,
                            "confidence": mapping.get("confidence")},
                project_id=project_id)
            discovered += 1 if changed else 0
        return {"discovered": discovered}

    def observe_platform_entities(self, store, knowledge, tasks=None
                                  ) -> dict[str, int]:
        """The organization includes the platform's own business objects:
        every project, every report, every business rule, every KPI. These
        are entities the executive already recognises, so the organizational
        model would be lying by omission without them."""
        counts = {"project": 0, "report": 0, "business_rule": 0, "kpi": 0}

        for pid in store.list_projects():
            state = store.load(pid, "state") or {}
            if not state:
                continue
            _, changed = self.observe(
                "project", state.get("name", pid), source="platform",
                attributes={"status": state.get("status"),
                            "report_version": state.get("report_version")},
                project_id=pid)
            counts["project"] += 1 if changed else 0

            for kpi in (store.load(pid, "kpis", []) or [])[:50]:
                if not isinstance(kpi, dict):
                    continue
                name = kpi.get("name") or kpi.get("kpi")
                if not name:
                    continue
                _, changed = self.observe(
                    "kpi", str(name), source="platform",
                    attributes={"unit": kpi.get("unit"),
                                "trend": kpi.get("trend")},
                    project_id=pid)
                counts["kpi"] += 1 if changed else 0

        for report in knowledge.report_history(100):
            _, changed = self.observe(
                "report", report.get("title", ""), source="platform",
                attributes={"health_score": report.get("health_score")},
                project_id=report.get("project_id", ""))
            counts["report"] += 1 if changed else 0

        for rule in knowledge.snapshot().get("business_rules", []):
            text = str(rule.get("rule", "")).strip()
            if text:
                _, changed = self.observe(
                    "business_rule", text[:120], source="platform",
                    attributes={"scope": rule.get("scope")})
                counts["business_rule"] += 1 if changed else 0

        return counts

    # -------------------------------------------------------------- mirror
    def _mirror(self, entity: dict) -> None:
        """Mirror the entity into the enterprise knowledge graph and the
        knowledge store's entity definitions — the graph owns relationships,
        the knowledge store owns definitions, and this model owns identity,
        ownership, and history. Nothing is duplicated; each is told once."""
        if self._graph is not None:
            try:
                self._graph.upsert_node(
                    entity["entity_id"], kind=entity["kind"],
                    label=entity["name"],
                    project_id=(entity["projects"] or [""])[0],
                    owner=entity["owner"] or None)
            except Exception:  # noqa: BLE001 — mirroring degrades, never fails
                logger.exception("Graph mirror failed for %s",
                                 entity["entity_id"])
        if self._knowledge is not None and entity["kind"] in (
                "product", "customer", "merchant", "bank"):
            try:
                self._knowledge.define_entity(
                    entity["name"], entity["kind"],
                    f"{entity['kind'].title()} observed in "
                    f"{', '.join(entity['sources'][:3]) or 'the platform'}",
                    source="organizational_model",
                    project_id=(entity["projects"] or [""])[0])
            except Exception:  # noqa: BLE001
                logger.exception("Knowledge mirror failed for %s",
                                 entity["entity_id"])

    def _announce(self, entity: dict, new: bool) -> None:
        if self._bus is None:
            return
        try:
            self._bus.publish(
                "EntityDiscovered" if new else "EntityUpdated",
                {"entity_id": entity["entity_id"], "kind": entity["kind"],
                 "name": entity["name"], "owner": entity["owner"]},
                project_id=(entity["projects"] or [""])[0],
                source="organizational_model")
        except Exception:  # noqa: BLE001
            logger.exception("Entity event publication failed")

    # ---------------------------------------------------------------- read
    def entities(self, kind: str = "", owner: str = "", query: str = "",
                 project_id: str = "", limit: int = 200) -> list[dict]:
        items = self._store.read("entities")
        if kind:
            items = [e for e in items if e["kind"] == kind]
        if owner:
            items = [e for e in items if e["owner"] == owner]
        if project_id:
            items = [e for e in items if project_id in e["projects"]]
        if query:
            # Canonicalize the query the same way names and aliases are
            # stored, so "North Coffee" finds `north_coffee` — a caller
            # searching by the name they can see must not be defeated by the
            # separator this model happens to store identities with.
            needle = _canonical(query)
            items = [e for e in items
                     if needle and (needle in e["canonical"]
                                    or any(needle in a for a in e["aliases"]))]
        return sorted(items, key=lambda e: e["last_seen"], reverse=True)[:limit]

    def get(self, entity_id: str) -> dict | None:
        return self._store.get("entities", "entity_id", entity_id)

    def resolve(self, name: str, kind: str = "") -> dict | None:
        """Find an entity by any name it is known by — the identity question:
        is ``MID`` the same merchant as ``merchant_id``?"""
        needle = _canonical(name)
        for entity in self._store.read("entities"):
            if kind and entity["kind"] != kind:
                continue
            if entity["canonical"] == needle or needle in entity["aliases"]:
                return entity
        return None

    def counts(self) -> dict[str, int]:
        """Business Entity Count, by kind."""
        counts = {kind: 0 for kind in ENTITY_KINDS}
        for entity in self._store.read("entities"):
            counts[entity["kind"]] = counts.get(entity["kind"], 0) + 1
        return counts

    def overview(self) -> dict[str, Any]:
        """Organization Overview — business framing, no technical internals."""
        entities = self._store.read("entities")
        counts = self.counts()
        owned = [e for e in entities if e["owner"]]
        return {
            "entities_total": len(entities),
            "by_kind": {k: v for k, v in counts.items() if v},
            "owned": len(owned),
            "unowned": len(entities) - len(owned),
            "owners": sorted({e["owner"] for e in owned})[:20],
            "sources": sorted({s for e in entities for s in e["sources"]}),
            "recently_discovered": [
                {"name": e["name"], "kind": e["kind"],
                 "first_seen": e["first_seen"],
                 "sources": e["sources"]}
                for e in sorted(entities, key=lambda e: e["first_seen"],
                                reverse=True)[:10]],
            "recently_changed": [
                {"name": e["name"], "kind": e["kind"],
                 "change": e["history"][-1]["change"] if e["history"] else "",
                 "at": e["updated_at"]}
                for e in sorted(entities, key=lambda e: e["updated_at"],
                                reverse=True)[:10]],
        }

    def history(self, entity_id: str) -> list[dict]:
        entity = self.get(entity_id)
        return entity["history"] if entity else []


# --------------------------------------------------------------- utilities
def _canonical(name: str) -> str:
    return re.sub(r"[^0-9a-z]+", "_", str(name).strip().lower()).strip("_")


def _dedupe(aliases: list[str], canonical: str) -> list[str]:
    out: list[str] = []
    for alias in aliases:
        value = _canonical(alias)
        if value and value != canonical and value not in out:
            out.append(value)
    return out[:MAX_ALIASES]


def _kind_for_table(table: str) -> str | None:
    """Map a synced table name to an entity kind by its business noun."""
    name = _canonical(table)
    for concept, kind in CONCEPT_TO_KIND.items():
        if name == concept or name == f"{concept}s" \
                or name.startswith(f"{concept}_") \
                or name.endswith(f"_{concept}") \
                or name.endswith(f"_{concept}s"):
            return kind
    return None


def _name_column(columns: list[str], kind: str) -> str | None:
    """The column naming the entity: a ``name``-ish column, else the kind's
    own identifier column."""
    lowered = {str(c).strip().lower(): str(c) for c in columns}
    for candidate in ("name", f"{kind}_name", f"{kind}", "title", "subject",
                      "label", "description"):
        if candidate in lowered:
            return lowered[candidate]
    for candidate in (f"{kind}_id", f"{kind}_code", "id", "code"):
        if candidate in lowered:
            return lowered[candidate]
    return None


def owner_column_in(columns: list[str]) -> str | None:
    """The column that names an owner, if the record has one. Shared with the
    Relationship Engine, which reads ownership from the same signal."""
    lowered = {str(c).strip().lower(): str(c) for c in columns}
    for hint in OWNER_HINTS:
        if hint in lowered:
            return lowered[hint]
    return None


def _aliases_from(record: dict, name_column: str) -> list[str]:
    """Other identifiers on the same record are aliases of the same thing —
    this is what lets ``MID`` and ``merchant_id`` resolve to one merchant."""
    aliases = []
    for column, value in record.items():
        name = str(column).strip().lower()
        if column == name_column or value in (None, ""):
            continue
        if name.endswith("_id") or name.endswith("_code") or name in (
                "id", "code", "mid", "sku", "uuid", "guid", "number"):
            aliases.append(str(value))
    return aliases[:5]

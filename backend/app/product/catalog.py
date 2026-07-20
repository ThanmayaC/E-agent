"""Product Catalog — the enterprise's products, as a product manager sees them.

A product is the unit an Enterprise Product Manager actually manages, and it
already half-exists elsewhere: the Organizational Model knows *that* products
exist (it observes them from synced systems and semantic layers), the
Knowledge Store knows the reports about them, and the analytics artifacts know
their KPIs. This catalogue is the product-management view over those facts —
identity, owner, business unit, lifecycle, status, dependencies, and the
merchants, customers, and reports each product touches.

It **derives, never duplicates**. Associations are read from the Relationship
Engine's graph on every sync; the catalogue stores the resolved view, and the
Organizational Model remains the single source of truth for what exists and
how it is wired. A product the model has never seen cannot be invented here.
"""
from __future__ import annotations

import re
from typing import Any

from app.core.logging import get_logger
from app.product.store import ProductStore, new_id, now_iso

logger = get_logger(__name__)

# Where a product is in its life. Lifecycle is a management fact, not a
# derivable one — the platform infers a default and the manager corrects it.
LIFECYCLES = ("concept", "launch", "growth", "mature", "decline",
              "sunset")
STATUSES = ("active", "paused", "retired")

MAX_ASSOCIATIONS = 50
MAX_HISTORY = 40


class ProductCatalog:
    """Maintains enterprise products and their organizational relationships."""

    def __init__(self, store: ProductStore, organization=None,
                 relationships=None, knowledge=None, artifacts=None,
                 bus=None):
        self._store = store
        self._org = organization
        self._relationships = relationships
        self._knowledge = knowledge
        self._artifacts = artifacts
        self._bus = bus

    def attach_bus(self, bus) -> None:
        self._bus = bus

    # ------------------------------------------------------------- catalog
    def upsert(self, name: str, owner: str = "", description: str = "",
               business_unit: str = "", lifecycle: str = "",
               status: str = "active", dependencies: list[str] | None = None,
               source: str = "manual", entity_id: str = "",
               project_id: str = "") -> tuple[dict, bool]:
        """Add or update a product. Returns ``(product, changed)``.

        Idempotent by name: re-registering a known product enriches it rather
        than duplicating it, and reports whether anything actually moved.
        """
        if lifecycle and lifecycle not in LIFECYCLES:
            raise ValueError(f"Unknown lifecycle: {lifecycle}")
        if status not in STATUSES:
            raise ValueError(f"Unknown product status: {status}")
        canonical = _canonical(name)
        if not canonical:
            raise ValueError("A product needs a name")
        product_id = f"product:{canonical}"

        with self._store.mutate("products") as products:
            existing = next((p for p in products
                             if p["product_id"] == product_id), None)
            if existing is None:
                product = {
                    "product_id": product_id, "internal_id": new_id("prd"),
                    "name": name.strip()[:200], "canonical": canonical,
                    "owner": owner[:120], "description": description[:800],
                    "business_unit": business_unit[:120],
                    "lifecycle": lifecycle or "growth", "status": status,
                    "dependencies": list(dependencies or [])[:MAX_ASSOCIATIONS],
                    "entity_id": entity_id or f"product:{canonical}",
                    "kpis": [], "merchants": [], "customers": [],
                    "reports": [], "projects": [project_id] if project_id else [],
                    "sources": [source] if source else [],
                    "history": [{"at": now_iso(), "change": "registered",
                                 "detail": f"registered from {source}"}],
                    "created_at": now_iso(), "updated_at": now_iso(),
                }
                products.append(product)
                changed = True
            else:
                product = existing
                changed = self._enrich(product, owner, description,
                                       business_unit, lifecycle, status,
                                       dependencies, source, project_id)

        if changed:
            self._announce(product, new=existing is None)
        return product, changed

    def _enrich(self, product: dict, owner: str, description: str,
                business_unit: str, lifecycle: str, status: str,
                dependencies: list[str] | None, source: str,
                project_id: str) -> bool:
        """Merge new information without losing what is already known: an
        empty field never overwrites a populated one."""
        changed = False
        for field, value in (("owner", owner[:120] if owner else ""),
                             ("description", description[:800]),
                             ("business_unit", business_unit[:120]),
                             ("lifecycle", lifecycle)):
            if value and product.get(field) != value:
                previous = product.get(field)
                product[field] = value
                self._note(product, f"{field}_changed",
                           f"{previous or 'unset'} → {value}")
                changed = True
        if status and product["status"] != status:
            self._note(product, "status_changed",
                       f"{product['status']} → {status}")
            product["status"] = status
            changed = True
        for dependency in (dependencies or []):
            if dependency not in product["dependencies"] \
                    and len(product["dependencies"]) < MAX_ASSOCIATIONS:
                product["dependencies"].append(dependency)
                changed = True
        if source and source not in product["sources"]:
            product["sources"].append(source)
            changed = True
        if project_id and project_id not in product["projects"]:
            product["projects"].append(project_id)
            changed = True
        if changed:
            product["updated_at"] = now_iso()
        return changed

    def _note(self, product: dict, change: str, detail: str) -> None:
        product["history"].append({"at": now_iso(), "change": change,
                                   "detail": detail[:200]})
        product["history"] = product["history"][-MAX_HISTORY:]

    def set_lifecycle(self, product_id: str, lifecycle: str) -> dict | None:
        if lifecycle not in LIFECYCLES:
            raise ValueError(f"Unknown lifecycle: {lifecycle}")
        product = self._require(product_id)
        with self._store.mutate("products") as products:
            for stored in products:
                if stored["product_id"] == product_id:
                    self._note(stored, "lifecycle_changed",
                               f"{stored['lifecycle']} → {lifecycle}")
                    stored["lifecycle"] = lifecycle
                    stored["updated_at"] = now_iso()
                    return stored
        return product

    def retire(self, product_id: str) -> dict | None:
        self._require(product_id)
        product, _ = self.upsert(self.get(product_id)["name"],
                                 status="retired", source="manual")
        return product

    # -------------------------------------------------- discovery from org
    def sync_from_organization(self) -> dict[str, int]:
        """Discover products from the Organizational Model and resolve every
        product's relationships from the Relationship Engine.

        This is the reuse seam: the model already observed products, merchants,
        customers, and reports from connected systems, and the relationship
        engine already wired them together with evidence. The catalogue asks;
        it does not re-detect.
        """
        if self._org is None:
            return {"discovered": 0, "linked": 0, "skipped": "no model"}
        discovered, linked = 0, 0
        for entity in self._org.entities(kind="product", limit=500):
            sources = entity.get("sources") or []
            observed_in = (f"Product observed in {', '.join(sources[:3])}"
                           if sources else "")
            _, changed = self.upsert(
                entity["name"], owner=entity.get("owner", ""),
                description=observed_in, source="organizational_model",
                entity_id=entity["entity_id"],
                project_id=(entity.get("projects") or [""])[0])
            discovered += 1 if changed else 0
            if self._link(entity["entity_id"]):
                linked += 1
        return {"discovered": discovered, "linked": linked}

    def _link(self, entity_id: str) -> bool:
        """Resolve one product's merchants, customers, and dependencies from
        the relationship graph."""
        if self._relationships is None:
            return False
        neighbourhood = self._relationships.neighbourhood(entity_id)
        related = neighbourhood.get("related") or []
        if not related:
            return False
        merchants = _names(related, "merchant")
        customers = _names(related, "customer")
        dependencies = [r["name"] for r in related
                        if r["relationship"] == "dependency"][:MAX_ASSOCIATIONS]
        owner = next((r["name"] for r in related
                      if r["relationship"] == "ownership"
                      and r["direction"] == "incoming"), "")

        product_id = f"product:{entity_id.split(':', 1)[-1]}"
        with self._store.mutate("products") as products:
            for product in products:
                if product["product_id"] != product_id:
                    continue
                changed = False
                for field, values in (("merchants", merchants),
                                      ("customers", customers),
                                      ("dependencies", dependencies)):
                    if values and product[field] != values:
                        product[field] = values[:MAX_ASSOCIATIONS]
                        changed = True
                if owner and not product["owner"]:
                    product["owner"] = owner[:120]
                    changed = True
                if changed:
                    product["updated_at"] = now_iso()
                return changed
        return False

    def sync_kpis_and_reports(self) -> dict[str, int]:
        """Attach each product's KPIs and reports from the artifacts and the
        Knowledge Store. A product's KPIs are the KPIs of the projects that
        analyse it — discovered by the KPI module, never redefined here."""
        if self._artifacts is None:
            return {"products_updated": 0}
        updated = 0
        for product in self.products():
            kpis = self._kpis_for(product)
            reports = self._reports_for(product)
            with self._store.mutate("products") as products:
                for stored in products:
                    if stored["product_id"] != product["product_id"]:
                        continue
                    if kpis and stored["kpis"] != kpis:
                        stored["kpis"] = kpis
                        stored["updated_at"] = now_iso()
                        updated += 1
                    if reports and stored["reports"] != reports:
                        stored["reports"] = reports
                        stored["updated_at"] = now_iso()
        return {"products_updated": updated}

    def _kpis_for(self, product: dict) -> list[dict]:
        """KPIs from the product's projects, plus any KPI whose name mentions
        the product — the honest join available without a product dimension
        in the source data."""
        out: list[dict] = []
        seen: set[str] = set()
        for pid in product["projects"] or self._artifacts.list_projects():
            for kpi in (self._artifacts.load(pid, "kpis", []) or []):
                if not isinstance(kpi, dict):
                    continue
                name = str(kpi.get("name", ""))
                if not name or name in seen:
                    continue
                if product["projects"] or _mentions(name, product["canonical"]):
                    seen.add(name)
                    out.append({"name": name, "kpi_id": kpi.get("id", ""),
                                "project_id": pid,
                                "current_value": kpi.get("current_value"),
                                "growth_pct": kpi.get("growth_pct"),
                                "trend": kpi.get("trend", "flat"),
                                "unit": kpi.get("unit", "")})
        return out[:MAX_ASSOCIATIONS]

    def _reports_for(self, product: dict) -> list[dict]:
        if self._knowledge is None:
            return []
        out = []
        for report in self._knowledge.report_history(100):
            if report.get("project_id") in product["projects"] \
                    or _mentions(str(report.get("title", "")),
                                 product["canonical"]):
                out.append({"title": report.get("title", ""),
                            "project_id": report.get("project_id", ""),
                            "health_score": report.get("health_score"),
                            "generated_at": report.get("generated_at", "")})
        return out[-MAX_ASSOCIATIONS:]

    # --------------------------------------------------------------- read
    def products(self, status: str = "", lifecycle: str = "",
                 owner: str = "", business_unit: str = "",
                 limit: int = 200) -> list[dict]:
        items = self._store.read("products")
        if status:
            items = [p for p in items if p["status"] == status]
        if lifecycle:
            items = [p for p in items if p["lifecycle"] == lifecycle]
        if owner:
            items = [p for p in items if p["owner"] == owner]
        if business_unit:
            items = [p for p in items if p["business_unit"] == business_unit]
        return sorted(items, key=lambda p: p["name"])[:limit]

    def get(self, product_id: str) -> dict | None:
        return self._store.get("products", "product_id", product_id)

    def resolve(self, name: str) -> dict | None:
        return self.get(f"product:{_canonical(name)}")

    def _require(self, product_id: str) -> dict:
        product = self.get(product_id)
        if product is None:
            raise KeyError(f"Unknown product: {product_id}")
        return product

    def stats(self) -> dict[str, Any]:
        products = self._store.read("products")
        by_lifecycle: dict[str, int] = {}
        by_unit: dict[str, int] = {}
        for p in products:
            by_lifecycle[p["lifecycle"]] = by_lifecycle.get(p["lifecycle"], 0) + 1
            if p["business_unit"]:
                by_unit[p["business_unit"]] = by_unit.get(p["business_unit"], 0) + 1
        return {
            "total": len(products),
            "active": sum(1 for p in products if p["status"] == "active"),
            "retired": sum(1 for p in products if p["status"] == "retired"),
            "by_lifecycle": by_lifecycle, "by_business_unit": by_unit,
            "owned": sum(1 for p in products if p["owner"]),
            "with_kpis": sum(1 for p in products if p["kpis"]),
            "merchants_linked": sum(len(p["merchants"]) for p in products),
            "customers_linked": sum(len(p["customers"]) for p in products),
        }

    def _announce(self, product: dict, new: bool) -> None:
        if self._bus is None:
            return
        try:
            self._bus.publish(
                "ProductRegistered" if new else "ProductUpdated",
                {"product_id": product["product_id"], "name": product["name"],
                 "lifecycle": product["lifecycle"], "owner": product["owner"]},
                source="product_catalog")
        except Exception:  # noqa: BLE001 — announcing never fails the catalogue
            logger.exception("Product event publication failed")


# --------------------------------------------------------------- utilities
def _canonical(name: str) -> str:
    return re.sub(r"[^0-9a-z]+", "_", str(name).strip().lower()).strip("_")


def _names(related: list[dict], kind: str) -> list[str]:
    return [r["name"] for r in related if r["kind"] == kind][:MAX_ASSOCIATIONS]


def _mentions(text: str, canonical: str) -> bool:
    return canonical.replace("_", " ") in str(text).strip().lower()

"""The ecosystem graph and MCC explorer — relationships, from transactions.

The Ecosystem workspace is not another dashboard; it is a graph of how the
payment network actually connects. Every node (a product, a bank, a PSP, an MCC
category, a region) and every edge (payer-bank → PSP, product → MCC) is measured
from the raw transactions in the current slice, so the picture is of the real
network in that window, not a stored diagram. Node intelligence — details,
neighbours, trend, forecast, recommendations — is composed from the same
analytics and ML the rest of the platform uses, so a node's story matches its
product page to the rupee.
"""
from __future__ import annotations

from app.warehouse.filters import Filters

# The node families the graph draws, each backed by a transaction column.
_NODE_DIMS = {
    "product": ("product_code", "product"),
    "bank": ("payer_bank", "bank"),
    "psp": ("payer_psp", "psp"),
    "mcc_category": ("mcc_category", "mcc_category"),
    "region": ("region", "region"),
}


def build_graph(analytics, f: Filters, *, top_banks: int = 10,
                top_psps: int = 10, top_mcc: int = 10) -> dict:
    """Nodes + weighted edges of transaction flow for the slice."""
    a = analytics
    f = a.resolve(f)
    products = a.by_dimension(f, "product", limit=20, with_growth=True)
    banks = a.by_dimension(f, "bank", limit=top_banks)
    psps = a.by_dimension(f, "psp", limit=top_psps)
    mccs = a.by_dimension(f, "mcc_category", limit=top_mcc)

    catalog = {p["product_code"]: p for p in a.products()}
    nodes: list[dict] = []

    def _node(nid, ntype, label, row, **extra):
        nodes.append({
            "id": f"{ntype}:{nid}", "node_id": str(nid), "type": ntype,
            "label": label, "attempts": row.get("attempts"),
            "value_inr": row.get("value_inr"),
            "success_rate": row.get("success_rate"),
            "share_pct": row.get("share_pct"),
            "growth_pct": row.get("growth_pct"), **extra})

    for p in products:
        meta = catalog.get(p["name"], {})
        _node(p["name"], "product",
              meta.get("product_name", p["name"]), p,
              family=meta.get("product_family"))
    for b in banks:
        _node(b["name"], "bank", b["name"], b)
    for p in psps:
        _node(p["name"], "psp", p["name"], p)
    for mc in mccs:
        _node(mc["name"], "mcc_category", mc["name"], mc)

    where, params = f.where()
    edges: list[dict] = []
    # product → mcc_category flow
    prod_codes = [p["name"] for p in products]
    if prod_codes:
        marks = ", ".join("?" for _ in prod_codes)
        for r in a.wh.query(f"""
                SELECT product_code AS src, mcc_category AS dst, count(*) AS n,
                       round(sum(amount_inr) FILTER (WHERE status='SUCCESS'),0) AS value
                FROM attempts WHERE {where} AND product_code IN ({marks})
                  AND mcc_category IS NOT NULL
                GROUP BY 1,2 HAVING count(*) > 100
                ORDER BY n DESC LIMIT 120""", params + prod_codes,
                label="ecosystem.edge.prod_mcc"):
            edges.append({"source": f"product:{r['src']}",
                          "target": f"mcc_category:{r['dst']}",
                          "weight": r["n"], "value_inr": r["value"],
                          "kind": "product-mcc"})
    # bank → psp flow
    bank_names = [b["name"] for b in banks]
    if bank_names:
        marks = ", ".join("?" for _ in bank_names)
        for r in a.wh.query(f"""
                SELECT payer_bank AS src, payer_psp AS dst, count(*) AS n
                FROM attempts WHERE {where} AND payer_bank IN ({marks})
                  AND payer_psp IS NOT NULL
                GROUP BY 1,2 HAVING count(*) > 100
                ORDER BY n DESC LIMIT 120""", params + bank_names,
                label="ecosystem.edge.bank_psp"):
            edges.append({"source": f"bank:{r['src']}",
                          "target": f"psp:{r['dst']}",
                          "weight": r["n"], "kind": "bank-psp"})
    return {"window": {"start": f.start, "end": f.end},
            "nodes": nodes, "edges": edges,
            "counts": {"nodes": len(nodes), "edges": len(edges)}}


def node_detail(analytics, ml, f: Filters, node_type: str,
                node_id: str) -> dict:
    """Everything the node drawer shows for one entity."""
    if node_type not in _NODE_DIMS:
        raise ValueError(f"unknown node type: {node_type}")
    col, filt_field = _NODE_DIMS[node_type]
    a = analytics
    nf = f.with_(**{filt_field: node_id})
    kpis = a.kpis(nf)
    daily = a.daily_series(nf)
    detail = {
        "type": node_type, "id": node_id,
        "window": a.resolve(nf).describe(),
        "kpis": kpis,
        "daily": daily,
        "neighbours": _neighbours(a, nf, node_type),
        "top_mccs": a.by_dimension(nf, "mcc_subcategory", limit=8),
    }
    if node_type == "product":
        detail["banks"] = a.by_dimension(nf, "bank", limit=8)
        detail["psps"] = a.by_dimension(nf, "psp", limit=8)
    if ml is not None and getattr(ml, "available", False):
        detail["forecast"] = ml.run(nf, target="attempts", horizon=14)
    return detail


def _neighbours(a, nf: Filters, node_type: str) -> dict:
    """The other families this node connects to, ranked by shared volume."""
    out = {}
    plan = {"product": ["bank", "psp", "mcc_category"],
            "bank": ["psp", "product", "mcc_category"],
            "psp": ["bank", "product", "mcc_category"],
            "mcc_category": ["product", "bank", "psp"],
            "region": ["product", "bank", "psp"]}.get(node_type, [])
    for dim in plan:
        try:
            out[dim] = a.by_dimension(nf, dim, limit=6, with_growth=False)
        except ValueError:
            pass
    return out


# ----------------------------------------------------------------------- mcc
def mcc_overview(analytics, f: Filters) -> dict:
    """Every MCC category and subcategory with distribution, value and growth."""
    a = analytics
    f = a.resolve(f)
    categories = a.by_dimension(f, "mcc_category", limit=40)
    subcats = a.by_dimension(f, "mcc_subcategory", limit=60)
    catalog = a.mccs()
    return {"window": {"start": f.start, "end": f.end},
            "categories": categories, "subcategories": subcats,
            "catalog": catalog,
            "totals": {"categories": len(categories),
                       "mcc_codes": len(catalog)}}


def mcc_detail(analytics, ml, f: Filters, mcc_code: str) -> dict:
    """One MCC (code or subcategory): behaviour, products, banks, PSPs, forecast."""
    a = analytics
    # Accept either a numeric MCC code or a subcategory label.
    field = "mcc" if mcc_code.isdigit() else "mcc_subcategory"
    mf = f.with_(**{field: mcc_code})
    catalog = {str(m.get("mcc")): m for m in a.mccs()}
    detail = {
        "mcc": mcc_code,
        "reference": catalog.get(mcc_code),
        "window": a.resolve(mf).describe(),
        "kpis": a.kpis(mf),
        "daily": a.daily_series(mf),
        "products": a.by_dimension(mf, "product", limit=12),
        "banks": a.by_dimension(mf, "bank", limit=10),
        "psps": a.by_dimension(mf, "psp", limit=10),
        "merchants": a.by_dimension(mf, "merchant_name", limit=12),
        "adjustments": a.adjustments(mf),
    }
    if ml is not None and getattr(ml, "available", False):
        detail["forecast"] = ml.run(mf, target="attempts", horizon=14)
    return detail

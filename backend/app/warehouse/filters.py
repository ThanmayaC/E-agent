"""Query filters shared by every analytics surface.

One place builds the WHERE clause, so a product dashboard, an MCC drill-down
and an AI evidence lookup all slice the raw transactions identically — and an
answer can always be reproduced from the filter that produced it.
"""
from __future__ import annotations

from dataclasses import dataclass, field, fields

# Columns a caller may filter on, mapped to their SQL column.
_DIMENSIONS = {
    "product": "product_code",
    "product_family": "product_family",
    "payment_type": "payment_type",
    "bank": "payer_bank",
    "payee_bank": "payee_bank",
    "psp": "payer_psp",
    "payee_psp": "payee_psp",
    "merchant": "merchant_id",
    "mcc": "mcc",
    "mcc_category": "mcc_category",
    "mcc_subcategory": "mcc_subcategory",
    "region": "region",
    "state": "state",
    "city": "city",
    "segment": "customer_segment",
    "device": "device",
    "channel": "channel",
    "status": "status",
    "failure_bucket": "failure_bucket",
    "merchant_tier": "merchant_tier",
    "customer": "customer_id",
    "mandate": "mandate_id",
}


@dataclass
class Filters:
    """A slice of the transaction corpus. Every field is optional."""
    start: str | None = None
    end: str | None = None
    product: str | None = None
    product_family: str | None = None
    payment_type: str | None = None
    bank: str | None = None
    payee_bank: str | None = None
    psp: str | None = None
    payee_psp: str | None = None
    merchant: str | None = None
    mcc: str | None = None
    mcc_category: str | None = None
    mcc_subcategory: str | None = None
    region: str | None = None
    state: str | None = None
    city: str | None = None
    segment: str | None = None
    device: str | None = None
    channel: str | None = None
    status: str | None = None
    failure_bucket: str | None = None
    merchant_tier: str | None = None
    customer: str | None = None
    mandate: str | None = None
    last_days: int | None = None

    def where(self, *, alias: str = "") -> tuple[str, list]:
        """SQL predicate + positional parameters."""
        p = f"{alias}." if alias else ""
        clauses: list[str] = []
        params: list = []
        if self.start:
            clauses.append(f"{p}txn_date >= ?")
            params.append(self.start)
        if self.end:
            clauses.append(f"{p}txn_date <= ?")
            params.append(self.end)
        for f in fields(self):
            if f.name in ("start", "end", "last_days"):
                continue
            val = getattr(self, f.name)
            if val in (None, "", "all", "ALL"):
                continue
            col = _DIMENSIONS[f.name]
            if isinstance(val, (list, tuple, set)):
                vals = list(val)
                if not vals:
                    continue
                marks = ", ".join("?" for _ in vals)
                clauses.append(f"{p}{col} IN ({marks})")
                params.extend(vals)
            else:
                clauses.append(f"{p}{col} = ?")
                params.append(val)
        return (" AND ".join(clauses) if clauses else "1=1"), params

    def describe(self) -> dict:
        """Human-readable view of the slice — attached to every AI answer so
        the evidence behind a number is never ambiguous."""
        out = {}
        for f in fields(self):
            v = getattr(self, f.name)
            if v not in (None, "", "all", "ALL"):
                out[f.name] = v
        return out

    def with_(self, **kw) -> "Filters":
        data = {f.name: getattr(self, f.name) for f in fields(self)}
        data.update(kw)
        return Filters(**data)

    @classmethod
    def from_query(cls, **kw) -> "Filters":
        allowed = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in kw.items()
                      if k in allowed and v not in (None, "")})


def clamp_window(start: str | None, end: str | None, corpus: tuple[str, str],
                 last_days: int | None = None) -> tuple[str, str]:
    """Resolve a requested window against what the corpus actually holds."""
    from datetime import date, timedelta
    c_start, c_end = corpus
    if last_days and c_end:
        try:
            e = date.fromisoformat(c_end)
            return str(max(date.fromisoformat(c_start),
                           e - timedelta(days=last_days - 1))), c_end
        except (ValueError, TypeError):
            pass
    return start or c_start, end or c_end

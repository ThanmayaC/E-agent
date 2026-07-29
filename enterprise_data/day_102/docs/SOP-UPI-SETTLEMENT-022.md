---
id: SOP-UPI-SETTLEMENT-022
type: sop
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-16T16:30:00
---

# SOP-UPI-SETTLEMENT-022 — Settlement recovery SOP

**SOP ID:** SOP-UPI-SETTLEMENT-022  ·  **Owner:** Harsh Nanda
**Applies to:** Merchant Products and related flows

## Purpose
Standard operating procedure for handling a merchant settlement delay, first codified after
INC-2026-20.

## Procedure
1. Confirm the failure signature on the affected entity (Kotak Mahindra Bank-class).
2. Apply mitigation (failover / retry tuning / merchant comms as applicable).
3. Open an incident and start recovery monitoring.
4. Draft the RCA and decision; validate recovery in the daily report.

## References
Derived from RCA-2026-20 and decision DEC-2026-20.

Refs: INC-2026-20, RCA-2026-20, DEC-2026-20

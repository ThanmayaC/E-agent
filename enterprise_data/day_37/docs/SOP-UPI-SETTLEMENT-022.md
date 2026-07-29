---
id: SOP-UPI-SETTLEMENT-022
type: sop
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-28T16:30:00
---

# SOP-UPI-SETTLEMENT-022 — Settlement recovery SOP

**SOP ID:** SOP-UPI-SETTLEMENT-022  ·  **Owner:** Harsh Nanda
**Applies to:** Merchant Products and related flows

## Purpose
Standard operating procedure for handling a merchant settlement delay, first codified after
INC-2026-02.

## Procedure
1. Confirm the failure signature on the affected entity (Axis Bank-class).
2. Apply mitigation (failover / retry tuning / merchant comms as applicable).
3. Open an incident and start recovery monitoring.
4. Draft the RCA and decision; validate recovery in the daily report.

## References
Derived from RCA-2026-02 and decision DEC-2026-02.

Refs: INC-2026-02, RCA-2026-02, DEC-2026-02

---
id: SOP-UPI-BANK-FAILOVER-014
type: sop
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-25T16:30:00
---

# SOP-UPI-BANK-FAILOVER-014 — Bank failover & retry SOP

**SOP ID:** SOP-UPI-BANK-FAILOVER-014  ·  **Owner:** Harsh Nanda
**Applies to:** UPI Core and related flows

## Purpose
Standard operating procedure for handling a bank timeout / 5xx spike, first codified after
INC-2026-01.

## Procedure
1. Confirm the failure signature on the affected entity (Union Bank of India-class).
2. Apply mitigation (failover / retry tuning / merchant comms as applicable).
3. Open an incident and start recovery monitoring.
4. Draft the RCA and decision; validate recovery in the daily report.

## References
Derived from RCA-2026-01 and decision DEC-2026-01.

Refs: INC-2026-01, RCA-2026-01, DEC-2026-01

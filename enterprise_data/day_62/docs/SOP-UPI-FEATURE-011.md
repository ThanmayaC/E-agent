---
id: SOP-UPI-FEATURE-011
type: sop
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-22T16:30:00
---

# SOP-UPI-FEATURE-011 — Feature degradation SOP

**SOP ID:** SOP-UPI-FEATURE-011  ·  **Owner:** Harsh Nanda
**Applies to:** UPI Core and related flows

## Purpose
Standard operating procedure for handling a feature-level degradation, first codified after
INC-2026-28.

## Procedure
1. Confirm the failure signature on the affected entity (Collect Requests-class).
2. Apply mitigation (failover / retry tuning / merchant comms as applicable).
3. Open an incident and start recovery monitoring.
4. Draft the RCA and decision; validate recovery in the daily report.

## References
Derived from RCA-2026-28 and decision DEC-2026-28.

Refs: INC-2026-28, RCA-2026-28, DEC-2026-28

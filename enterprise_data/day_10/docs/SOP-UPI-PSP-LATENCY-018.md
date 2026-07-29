---
id: SOP-UPI-PSP-LATENCY-018
type: sop
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-01T16:30:00
---

# SOP-UPI-PSP-LATENCY-018 — PSP latency handling SOP

**SOP ID:** SOP-UPI-PSP-LATENCY-018  ·  **Owner:** Harsh Nanda
**Applies to:** UPI Core and related flows

## Purpose
Standard operating procedure for handling a PSP callback latency increase, first codified after
INC-2026-13.

## Procedure
1. Confirm the failure signature on the affected entity (YONO SBI-class).
2. Apply mitigation (failover / retry tuning / merchant comms as applicable).
3. Open an incident and start recovery monitoring.
4. Draft the RCA and decision; validate recovery in the daily report.

## References
Derived from RCA-2026-13 and decision DEC-2026-13.

Refs: INC-2026-13, RCA-2026-13, DEC-2026-13

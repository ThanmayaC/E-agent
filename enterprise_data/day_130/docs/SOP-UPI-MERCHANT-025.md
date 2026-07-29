---
id: SOP-UPI-MERCHANT-025
type: sop
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-29T16:30:00
---

# SOP-UPI-MERCHANT-025 — Merchant decline triage SOP

**SOP ID:** SOP-UPI-MERCHANT-025  ·  **Owner:** Harsh Nanda
**Applies to:** UPI Credit and related flows

## Purpose
Standard operating procedure for handling a merchant decline-rate spike, first codified after
INC-2026-24.

## Procedure
1. Confirm the failure signature on the affected entity (TravelGo, InsureWell-class).
2. Apply mitigation (failover / retry tuning / merchant comms as applicable).
3. Open an incident and start recovery monitoring.
4. Draft the RCA and decision; validate recovery in the daily report.

## References
Derived from RCA-2026-24 and decision DEC-2026-24.

Refs: INC-2026-24, RCA-2026-24, DEC-2026-24

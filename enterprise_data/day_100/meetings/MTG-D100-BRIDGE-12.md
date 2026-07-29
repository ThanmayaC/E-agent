---
id: MTG-D100-BRIDGE-12
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-29T09:30:00
---

# Incident Bridge — Merchant Products merchant settlement delay (Sev-3)

**Meeting ID:** MTG-D100-BRIDGE-12  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 29 Sep 2026 09:30 IST
**Incident:** INC-2026-12

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Sunil Pillai (Merchant Products Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-12.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 99.98% (up 0.89 vs Mon 28 Sep),
  Technical Declines at 0.31%. Regression is confined to Merchant Products on State Bank of India.
- Sunil confirmed the merchant settlement delay; unrelated flows are green.
- Meera noted Customer Complaints 1,377,
  Merchant Complaints 222.

## Decisions
- Treat INC-2026-12 as Sev-3.
- RCA RCA-2026-12 to be drafted by EOD next day; permanent fix under DEC-2026-12.

## Action items
- [ ] Sunil Pillai: lead investigation for INC-2026-12.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D100-DAILY.

Refs: INC-2026-12, RCA-2026-12, DEC-2026-12, RPT-D100-DAILY, TEAMS-D100-BRIDGE-12

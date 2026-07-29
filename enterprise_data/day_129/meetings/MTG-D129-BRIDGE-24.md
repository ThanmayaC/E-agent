---
id: MTG-D129-BRIDGE-24
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-28T09:30:00
---

# Incident Bridge — UPI Credit merchant decline-rate spike (Sev-3)

**Meeting ID:** MTG-D129-BRIDGE-24  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 28 Oct 2026 09:30 IST
**Incident:** INC-2026-24

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Kavya Nanda (UPI Credit Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-24.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 98.41% (down 1.57 vs Tue 27 Oct),
  Technical Declines at 0.32% (down 0.05 vs Tue 27 Oct). Regression is confined to UPI Credit on TravelGo, InsureWell.
- Kavya confirmed the merchant decline-rate spike; unrelated flows are green.
- Meera noted Customer Complaints 1,185,
  Merchant Complaints 194.

## Decisions
- Treat INC-2026-24 as Sev-3.
- RCA RCA-2026-24 to be drafted by EOD next day; permanent fix under DEC-2026-24.

## Action items
- [ ] Kavya Nanda: lead investigation for INC-2026-24.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D129-DAILY.

Refs: INC-2026-24, RCA-2026-24, DEC-2026-24, RPT-D129-DAILY, TEAMS-D129-BRIDGE-24

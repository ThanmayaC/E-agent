---
id: MTG-D126-BRIDGE-05
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-25T09:30:00
---

# Incident Bridge — UPI Credit bank timeout / 5xx spike (Sev-2)

**Meeting ID:** MTG-D126-BRIDGE-05  ·  **Type:** Incident Bridge (Sev-2)
**Room:** Virtual Bridge A  ·  **Start:** 25 Oct 2026 09:30 IST
**Incident:** INC-2026-05

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Kavya Nanda (UPI Credit Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-05.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 98.22% (down 1.56 vs Sat 24 Oct),
  Technical Declines at 0.58% (up 0.3 vs Sat 24 Oct). Regression is confined to UPI Credit on Union Bank of India.
- Kavya confirmed the bank timeout / 5xx spike; unrelated flows are green.
- Meera noted Customer Complaints 1,831,
  Merchant Complaints 229.

## Decisions
- Treat INC-2026-05 as Sev-2.
- RCA RCA-2026-05 to be drafted by EOD next day; permanent fix under DEC-2026-05.

## Action items
- [ ] Kavya Nanda: lead investigation for INC-2026-05.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D126-DAILY.

Refs: INC-2026-05, RCA-2026-05, DEC-2026-05, RPT-D126-DAILY, TEAMS-D126-BRIDGE-05

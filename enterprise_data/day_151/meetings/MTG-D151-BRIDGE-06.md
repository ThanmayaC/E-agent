---
id: MTG-D151-BRIDGE-06
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-19T09:30:00
---

# Incident Bridge — UPI Credit fraud / risk spike (Sev-2)

**Meeting ID:** MTG-D151-BRIDGE-06  ·  **Type:** Incident Bridge (Sev-2)
**Room:** Virtual Bridge A  ·  **Start:** 19 Nov 2026 09:30 IST
**Incident:** INC-2026-06

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Kavya Nanda (UPI Credit Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-06.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 99.92% (down 0.06 vs Wed 18 Nov),
  Technical Declines at 0.25%. Regression is confined to UPI Credit on HDFC MobileBanking.
- Kavya confirmed the fraud / risk spike; unrelated flows are green.
- Meera noted Customer Complaints 1,288,
  Merchant Complaints 96.

## Decisions
- Treat INC-2026-06 as Sev-2.
- RCA RCA-2026-06 to be drafted by EOD next day; permanent fix under DEC-2026-06.

## Action items
- [ ] Kavya Nanda: lead investigation for INC-2026-06.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D151-DAILY.

Refs: INC-2026-06, RCA-2026-06, DEC-2026-06, RPT-D151-DAILY, TEAMS-D151-BRIDGE-06

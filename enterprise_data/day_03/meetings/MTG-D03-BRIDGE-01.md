---
id: MTG-D03-BRIDGE-01
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-24T09:30:00
---

# Incident Bridge — UPI Core bank timeout / 5xx spike (Sev-2)

**Meeting ID:** MTG-D03-BRIDGE-01  ·  **Type:** Incident Bridge (Sev-2)
**Room:** Virtual Bridge A  ·  **Start:** 24 Jun 2026 09:30 IST
**Incident:** INC-2026-01

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Deepak Ghosh (UPI Core Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-01.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 97.39% (down 1.96 vs Tue 23 Jun),
  Technical Declines at 0.92% (up 0.47 vs Tue 23 Jun). Regression is confined to UPI Core on Union Bank of India.
- Deepak confirmed the bank timeout / 5xx spike; unrelated flows are green.
- Meera noted Customer Complaints 3,286,
  Merchant Complaints 434.

## Decisions
- Treat INC-2026-01 as Sev-2.
- RCA RCA-2026-01 to be drafted by EOD next day; permanent fix under DEC-2026-01.

## Action items
- [ ] Deepak Ghosh: lead investigation for INC-2026-01.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D03-DAILY.

Refs: INC-2026-01, RCA-2026-01, DEC-2026-01, RPT-D03-DAILY, TEAMS-D03-BRIDGE-01

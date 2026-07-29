---
id: MTG-D61-BRIDGE-28
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-21T09:30:00
---

# Incident Bridge — UPI Core feature-level degradation (Sev-3)

**Meeting ID:** MTG-D61-BRIDGE-28  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 21 Aug 2026 09:30 IST
**Incident:** INC-2026-28

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Deepak Ghosh (UPI Core Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-28.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 98.93% (down 0.87 vs Thu 20 Aug),
  Technical Declines at 0.53% (up 0.17 vs Thu 20 Aug). Regression is confined to UPI Core on Collect Requests.
- Deepak confirmed the feature-level degradation; unrelated flows are green.
- Meera noted Customer Complaints 1,898,
  Merchant Complaints 155.

## Decisions
- Treat INC-2026-28 as Sev-3.
- RCA RCA-2026-28 to be drafted by EOD next day; permanent fix under DEC-2026-28.

## Action items
- [ ] Deepak Ghosh: lead investigation for INC-2026-28.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D61-DAILY.

Refs: INC-2026-28, RCA-2026-28, DEC-2026-28, RPT-D61-DAILY, TEAMS-D61-BRIDGE-28

---
id: MTG-D34-BRIDGE-27
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-25T09:30:00
---

# Incident Bridge — UPI Core PSP callback latency increase (Sev-3)

**Meeting ID:** MTG-D34-BRIDGE-27  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 25 Jul 2026 09:30 IST
**Incident:** INC-2026-27

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Deepak Ghosh (UPI Core Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-27.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 99.17% (down 0.26 vs Fri 24 Jul),
  Technical Declines at 0.52% (up 0.12 vs Fri 24 Jul). Regression is confined to UPI Core on Amazon Pay.
- Deepak confirmed the PSP callback latency increase; unrelated flows are green.
- Meera noted Customer Complaints 2,109,
  Merchant Complaints 178.

## Decisions
- Treat INC-2026-27 as Sev-3.
- RCA RCA-2026-27 to be drafted by EOD next day; permanent fix under DEC-2026-27.

## Action items
- [ ] Deepak Ghosh: lead investigation for INC-2026-27.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D34-DAILY.

Refs: INC-2026-27, RCA-2026-27, DEC-2026-27, RPT-D34-DAILY, TEAMS-D34-BRIDGE-27

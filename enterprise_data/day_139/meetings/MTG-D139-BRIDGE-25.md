---
id: MTG-D139-BRIDGE-25
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-07T09:30:00
---

# Incident Bridge — UPI Lite X PSP callback latency increase (Sev-3)

**Meeting ID:** MTG-D139-BRIDGE-25  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 07 Nov 2026 09:30 IST
**Incident:** INC-2026-25

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Deepak Patel (UPI Lite X Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-25.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 99.65% (down 0.24 vs Fri 06 Nov),
  Technical Declines at 0.35% (up 0.08 vs Fri 06 Nov). Regression is confined to UPI Lite X on BHIM.
- Deepak confirmed the PSP callback latency increase; unrelated flows are green.
- Meera noted Customer Complaints 1,280,
  Merchant Complaints 103.

## Decisions
- Treat INC-2026-25 as Sev-3.
- RCA RCA-2026-25 to be drafted by EOD next day; permanent fix under DEC-2026-25.

## Action items
- [ ] Deepak Patel: lead investigation for INC-2026-25.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D139-DAILY.

Refs: INC-2026-25, RCA-2026-25, DEC-2026-25, RPT-D139-DAILY, TEAMS-D139-BRIDGE-25

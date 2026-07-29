---
id: MTG-D09-BRIDGE-13
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-30T09:30:00
---

# Incident Bridge — UPI Core PSP callback latency increase (Sev-3)

**Meeting ID:** MTG-D09-BRIDGE-13  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 30 Jun 2026 09:30 IST
**Incident:** INC-2026-13

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Deepak Ghosh (UPI Core Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-13.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 99.72% (down 0.26 vs Mon 29 Jun),
  Technical Declines at 0.58% (up 0.14 vs Mon 29 Jun). Regression is confined to UPI Core on YONO SBI.
- Deepak confirmed the PSP callback latency increase; unrelated flows are green.
- Meera noted Customer Complaints 2,390,
  Merchant Complaints 200.

## Decisions
- Treat INC-2026-13 as Sev-3.
- RCA RCA-2026-13 to be drafted by EOD next day; permanent fix under DEC-2026-13.

## Action items
- [ ] Deepak Ghosh: lead investigation for INC-2026-13.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D09-DAILY.

Refs: INC-2026-13, RCA-2026-13, DEC-2026-13, RPT-D09-DAILY, TEAMS-D09-BRIDGE-13

---
id: MTG-D70-BRIDGE-23
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-30T09:30:00
---

# Incident Bridge — UPI Core PSP callback latency increase (Sev-3)

**Meeting ID:** MTG-D70-BRIDGE-23  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 30 Aug 2026 09:30 IST
**Incident:** INC-2026-23

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Deepak Ghosh (UPI Core Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-23.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 99.92% (up 0.42 vs Sat 29 Aug),
  Technical Declines at 0.46% (up 0.11 vs Sat 29 Aug). Regression is confined to UPI Core on BHIM.
- Deepak confirmed the PSP callback latency increase; unrelated flows are green.
- Meera noted Customer Complaints 1,779,
  Merchant Complaints 147.

## Decisions
- Treat INC-2026-23 as Sev-3.
- Handle as a short operational issue; recovery monitoring only.

## Action items
- [ ] Deepak Ghosh: lead investigation for INC-2026-23.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D70-DAILY.

Refs: INC-2026-23, RPT-D70-DAILY, TEAMS-D70-BRIDGE-23

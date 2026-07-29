---
id: MTG-D85-BRIDGE-14
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-14T09:30:00
---

# Incident Bridge — UPI Autopay PSP callback latency increase (Sev-3)

**Meeting ID:** MTG-D85-BRIDGE-14  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 14 Sep 2026 09:30 IST
**Incident:** INC-2026-14

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Rekha Joshi (UPI Autopay Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-14.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 99.02% (up 0.24 vs Sun 13 Sep),
  Technical Declines at 0.43% (up 0.1 vs Sun 13 Sep). Regression is confined to UPI Autopay on Axis Mobile.
- Rekha confirmed the PSP callback latency increase; unrelated flows are green.
- Meera noted Customer Complaints 1,651,
  Merchant Complaints 136.

## Decisions
- Treat INC-2026-14 as Sev-3.
- RCA RCA-2026-14 to be drafted by EOD next day; permanent fix under DEC-2026-14.

## Action items
- [ ] Rekha Joshi: lead investigation for INC-2026-14.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D85-DAILY.

Refs: INC-2026-14, RCA-2026-14, DEC-2026-14, RPT-D85-DAILY, TEAMS-D85-BRIDGE-14

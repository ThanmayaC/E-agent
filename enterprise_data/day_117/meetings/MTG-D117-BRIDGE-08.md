---
id: MTG-D117-BRIDGE-08
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-16T09:30:00
---

# Incident Bridge — UPI Core PSP callback latency increase (Sev-3)

**Meeting ID:** MTG-D117-BRIDGE-08  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 16 Oct 2026 09:30 IST
**Incident:** INC-2026-08

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Deepak Ghosh (UPI Core Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-08.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 99.25% (down 0.1 vs Thu 15 Oct),
  Technical Declines at 0.39% (up 0.1 vs Thu 15 Oct). Regression is confined to UPI Core on CRED.
- Deepak confirmed the PSP callback latency increase; unrelated flows are green.
- Meera noted Customer Complaints 1,459,
  Merchant Complaints 114.

## Decisions
- Treat INC-2026-08 as Sev-3.
- RCA RCA-2026-08 to be drafted by EOD next day; permanent fix under DEC-2026-08.

## Action items
- [ ] Deepak Ghosh: lead investigation for INC-2026-08.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D117-DAILY.

Refs: INC-2026-08, RCA-2026-08, DEC-2026-08, RPT-D117-DAILY, TEAMS-D117-BRIDGE-08

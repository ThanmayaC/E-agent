---
id: MTG-D11-BRIDGE-16
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-02T09:30:00
---

# Incident Bridge — UPI Lite X PSP callback latency increase (Sev-3)

**Meeting ID:** MTG-D11-BRIDGE-16  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 02 Jul 2026 09:30 IST
**Incident:** INC-2026-16

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Deepak Patel (UPI Lite X Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-16.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 98.08% (down 0.32 vs Wed 01 Jul),
  Technical Declines at 0.63% (up 0.1 vs Wed 01 Jul). Regression is confined to UPI Lite X on Paytm.
- Deepak confirmed the PSP callback latency increase; unrelated flows are green.
- Meera noted Customer Complaints 2,519,
  Merchant Complaints 200.

## Decisions
- Treat INC-2026-16 as Sev-3.
- RCA RCA-2026-16 to be drafted by EOD next day; permanent fix under DEC-2026-16.

## Action items
- [ ] Deepak Patel: lead investigation for INC-2026-16.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D11-DAILY.

Refs: INC-2026-16, RCA-2026-16, DEC-2026-16, RPT-D11-DAILY, TEAMS-D11-BRIDGE-16

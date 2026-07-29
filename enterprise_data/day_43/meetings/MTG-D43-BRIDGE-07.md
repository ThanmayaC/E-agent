---
id: MTG-D43-BRIDGE-07
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-03T09:30:00
---

# Incident Bridge — Merchant Products merchant settlement delay (Sev-3)

**Meeting ID:** MTG-D43-BRIDGE-07  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 03 Aug 2026 09:30 IST
**Incident:** INC-2026-07

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Sunil Pillai (Merchant Products Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-07.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 98.73% (down 0.97 vs Sun 02 Aug),
  Technical Declines at 0.39% (up 0.01 vs Sun 02 Aug). Regression is confined to Merchant Products on Yes Bank.
- Sunil confirmed the merchant settlement delay; unrelated flows are green.
- Meera noted Customer Complaints 1,796,
  Merchant Complaints 302.

## Decisions
- Treat INC-2026-07 as Sev-3.
- Handle as a short operational issue; recovery monitoring only.

## Action items
- [ ] Sunil Pillai: lead investigation for INC-2026-07.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D43-DAILY.

Refs: INC-2026-07, RPT-D43-DAILY, TEAMS-D43-BRIDGE-07

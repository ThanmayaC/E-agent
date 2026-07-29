---
id: MTG-D36-BRIDGE-02
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-27T09:30:00
---

# Incident Bridge — Merchant Products merchant settlement delay (Sev-2)

**Meeting ID:** MTG-D36-BRIDGE-02  ·  **Type:** Incident Bridge (Sev-2)
**Room:** Virtual Bridge A  ·  **Start:** 27 Jul 2026 09:30 IST
**Incident:** INC-2026-02

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Sunil Pillai (Merchant Products Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-02.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 99.97% (up 1.45 vs Sun 26 Jul),
  Technical Declines at 0.44% (down 0.04 vs Sun 26 Jul). Regression is confined to Merchant Products on Axis Bank.
- Sunil confirmed the merchant settlement delay; unrelated flows are green.
- Meera noted Customer Complaints 2,151,
  Merchant Complaints 405.

## Decisions
- Treat INC-2026-02 as Sev-2.
- RCA RCA-2026-02 to be drafted by EOD next day; permanent fix under DEC-2026-02.

## Action items
- [ ] Sunil Pillai: lead investigation for INC-2026-02.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D36-DAILY.

Refs: INC-2026-02, RCA-2026-02, DEC-2026-02, RPT-D36-DAILY, TEAMS-D36-BRIDGE-02

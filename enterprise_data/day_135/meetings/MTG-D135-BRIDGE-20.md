---
id: MTG-D135-BRIDGE-20
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-03T09:30:00
---

# Incident Bridge — Merchant Products merchant settlement delay (Sev-3)

**Meeting ID:** MTG-D135-BRIDGE-20  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 03 Nov 2026 09:30 IST
**Incident:** INC-2026-20

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Sunil Pillai (Merchant Products Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-20.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 99.21% (up 0.2 vs Mon 02 Nov),
  Technical Declines at 0.27%. Regression is confined to Merchant Products on Bank of Baroda.
- Sunil confirmed the merchant settlement delay; unrelated flows are green.
- Meera noted Customer Complaints 1,170,
  Merchant Complaints 187.

## Decisions
- Treat INC-2026-20 as Sev-3.
- Handle as a short operational issue; recovery monitoring only.

## Action items
- [ ] Sunil Pillai: lead investigation for INC-2026-20.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D135-DAILY.

Refs: INC-2026-20, RPT-D135-DAILY, TEAMS-D135-BRIDGE-20

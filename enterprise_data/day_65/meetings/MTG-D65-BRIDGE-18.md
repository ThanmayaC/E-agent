---
id: MTG-D65-BRIDGE-18
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-25T09:30:00
---

# Incident Bridge — UPI Autopay merchant decline-rate spike (Sev-3)

**Meeting ID:** MTG-D65-BRIDGE-18  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 25 Aug 2026 09:30 IST
**Incident:** INC-2026-18

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Rekha Joshi (UPI Autopay Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-18.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 98.95% (up 0.04 vs Mon 24 Aug),
  Technical Declines at 0.36% (up 0.01 vs Mon 24 Aug). Regression is confined to UPI Autopay on MetroRide, QuickBite.
- Rekha confirmed the merchant decline-rate spike; unrelated flows are green.
- Meera noted Customer Complaints 1,437,
  Merchant Complaints 242.

## Decisions
- Treat INC-2026-18 as Sev-3.
- Handle as a short operational issue; recovery monitoring only.

## Action items
- [ ] Rekha Joshi: lead investigation for INC-2026-18.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D65-DAILY.

Refs: INC-2026-18, RPT-D65-DAILY, TEAMS-D65-BRIDGE-18

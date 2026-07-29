---
id: MTG-D128-BRIDGE-13
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-12T09:30:00
---

# Incident Bridge — UPI Credit merchant decline-rate spike (Sev-3)

**Meeting ID:** MTG-D128-BRIDGE-13  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 12 May 2026 09:30 IST
**Incident:** INC-2026-13

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Ishaan Verma (UPI Credit Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-13.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 99.63% (down 0.06 vs Mon 11 May),
  Technical Declines at 0.34%. Regression is confined to UPI Credit on TravelGo, InsureWell.
- Ishaan confirmed the merchant decline-rate spike; unrelated flows are green.
- Ishaan noted Customer Complaints 1,181,
  Merchant Complaints 195.

## Decisions
- Treat INC-2026-13 as Sev-3.
- RCA RCA-2026-13 to be drafted by EOD next day; permanent fix under DEC-2026-13.

## Action items
- [ ] Ishaan Verma: lead investigation for INC-2026-13.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D128-DAILY.

Refs: INC-2026-13, RCA-2026-13, DEC-2026-13, RPT-D128-DAILY, TEAMS-D128-BRIDGE-13

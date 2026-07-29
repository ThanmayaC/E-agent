---
id: MTG-D151-BRIDGE-06
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-04T09:30:00
---

# Incident Bridge — UPI International bank timeout / 5xx spike (Sev-2)

**Meeting ID:** MTG-D151-BRIDGE-06  ·  **Type:** Incident Bridge (Sev-2)
**Room:** Virtual Bridge A  ·  **Start:** 04 Jun 2026 09:30 IST
**Incident:** INC-2026-06

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Sunil Pillai (UPI International Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-06.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 99.21% (down 0.2 vs Wed 03 Jun),
  Technical Declines at 0.63% (up 0.32 vs Wed 03 Jun). Regression is confined to UPI International on Punjab National Bank.
- Sunil confirmed the bank timeout / 5xx spike; unrelated flows are green.
- Ishaan noted Customer Complaints 1,795,
  Merchant Complaints 226.

## Decisions
- Treat INC-2026-06 as Sev-2.
- RCA RCA-2026-06 to be drafted by EOD next day; permanent fix under DEC-2026-06.

## Action items
- [ ] Sunil Pillai: lead investigation for INC-2026-06.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D151-DAILY.

Refs: INC-2026-06, RCA-2026-06, DEC-2026-06, RPT-D151-DAILY, TEAMS-D151-BRIDGE-06

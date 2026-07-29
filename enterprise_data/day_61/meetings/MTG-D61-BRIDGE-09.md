---
id: MTG-D61-BRIDGE-09
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-06T09:30:00
---

# Incident Bridge — Merchant Products merchant settlement delay (Sev-3)

**Meeting ID:** MTG-D61-BRIDGE-09  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 06 Mar 2026 09:30 IST
**Incident:** INC-2026-09

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Deepak Rao (Merchant Products Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-09.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 99.94% (up 1.69 vs Thu 05 Mar),
  Technical Declines at 0.44%. Regression is confined to Merchant Products on Bank of Baroda.
- Deepak confirmed the merchant settlement delay; unrelated flows are green.
- Ishaan noted Customer Complaints 1,996,
  Merchant Complaints 308.

## Decisions
- Treat INC-2026-09 as Sev-3.
- Handle as a short operational issue; recovery monitoring only.

## Action items
- [ ] Deepak Rao: lead investigation for INC-2026-09.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D61-DAILY.

Refs: INC-2026-09, RPT-D61-DAILY, TEAMS-D61-BRIDGE-09

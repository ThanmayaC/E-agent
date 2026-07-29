---
id: MTG-D138-BRIDGE-25
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-22T09:30:00
---

# Incident Bridge — Merchant Products merchant settlement delay (Sev-3)

**Meeting ID:** MTG-D138-BRIDGE-25  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 22 May 2026 09:30 IST
**Incident:** INC-2026-25

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Deepak Rao (Merchant Products Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-25.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 99.23% (up 0.05 vs Thu 21 May),
  Technical Declines at 0.33%. Regression is confined to Merchant Products on ICICI Bank.
- Deepak confirmed the merchant settlement delay; unrelated flows are green.
- Ishaan noted Customer Complaints 1,260,
  Merchant Complaints 206.

## Decisions
- Treat INC-2026-25 as Sev-3.
- Handle as a short operational issue; recovery monitoring only.

## Action items
- [ ] Deepak Rao: lead investigation for INC-2026-25.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D138-DAILY.

Refs: INC-2026-25, RPT-D138-DAILY, TEAMS-D138-BRIDGE-25

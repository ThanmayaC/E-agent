---
id: MTG-D101-BRIDGE-20
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-15T09:30:00
---

# Incident Bridge — Merchant Products merchant settlement delay (Sev-3)

**Meeting ID:** MTG-D101-BRIDGE-20  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 15 Apr 2026 09:30 IST
**Incident:** INC-2026-20

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Deepak Rao (Merchant Products Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-20.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 99.25% (down 0.07 vs Tue 14 Apr),
  Technical Declines at 0.38% (up 0.01 vs Tue 14 Apr). Regression is confined to Merchant Products on Kotak Mahindra Bank.
- Deepak confirmed the merchant settlement delay; unrelated flows are green.
- Ishaan noted Customer Complaints 1,511,
  Merchant Complaints 249.

## Decisions
- Treat INC-2026-20 as Sev-3.
- RCA RCA-2026-20 to be drafted by EOD next day; permanent fix under DEC-2026-20.

## Action items
- [ ] Deepak Rao: lead investigation for INC-2026-20.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D101-DAILY.

Refs: INC-2026-20, RCA-2026-20, DEC-2026-20, RPT-D101-DAILY, TEAMS-D101-BRIDGE-20

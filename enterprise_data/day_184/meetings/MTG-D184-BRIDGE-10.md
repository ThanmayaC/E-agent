---
id: MTG-D184-BRIDGE-10
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-07T09:30:00
---

# Incident Bridge — UPI 123Pay feature-level degradation (Sev-3)

**Meeting ID:** MTG-D184-BRIDGE-10  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 07 Jul 2026 09:30 IST
**Incident:** INC-2026-10

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Kavya Nanda (UPI 123Pay Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-10.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 99.04% (down 0.94 vs Mon 06 Jul),
  Technical Declines at 0.41% (up 0.13 vs Mon 06 Jul). Regression is confined to UPI 123Pay on UPI 123Pay.
- Kavya confirmed the feature-level degradation; unrelated flows are green.
- Ishaan noted Customer Complaints 1,181,
  Merchant Complaints 91.

## Decisions
- Treat INC-2026-10 as Sev-3.
- RCA RCA-2026-10 to be drafted by EOD next day; permanent fix under DEC-2026-10.

## Action items
- [ ] Kavya Nanda: lead investigation for INC-2026-10.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D184-DAILY.

Refs: INC-2026-10, RCA-2026-10, DEC-2026-10, RPT-D184-DAILY, TEAMS-D184-BRIDGE-10

---
id: MTG-D92-BRIDGE-04
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-06T09:30:00
---

# Incident Bridge — UPI Core bank timeout / 5xx spike (Sev-2)

**Meeting ID:** MTG-D92-BRIDGE-04  ·  **Type:** Incident Bridge (Sev-2)
**Room:** Virtual Bridge A  ·  **Start:** 06 Apr 2026 09:30 IST
**Incident:** INC-2026-04

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Deepak Ghosh (UPI Core Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-04.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 98.17% (down 1.81 vs Sun 05 Apr),
  Technical Declines at 0.8% (up 0.41 vs Sun 05 Apr). Regression is confined to UPI Core on State Bank of India.
- Deepak confirmed the bank timeout / 5xx spike; unrelated flows are green.
- Ishaan noted Customer Complaints 2,365,
  Merchant Complaints 308.

## Decisions
- Treat INC-2026-04 as Sev-2.
- RCA RCA-2026-04 to be drafted by EOD next day; permanent fix under DEC-2026-04.

## Action items
- [ ] Deepak Ghosh: lead investigation for INC-2026-04.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D92-DAILY.

Refs: INC-2026-04, RCA-2026-04, DEC-2026-04, RPT-D92-DAILY, TEAMS-D92-BRIDGE-04

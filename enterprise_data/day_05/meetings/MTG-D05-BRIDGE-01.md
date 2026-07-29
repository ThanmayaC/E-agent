---
id: MTG-D05-BRIDGE-01
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-09T09:30:00
---

# Incident Bridge — UPI Core bank timeout / 5xx spike (Sev-2)

**Meeting ID:** MTG-D05-BRIDGE-01  ·  **Type:** Incident Bridge (Sev-2)
**Room:** Virtual Bridge A  ·  **Start:** 09 Jan 2026 09:30 IST
**Incident:** INC-2026-01

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Deepak Ghosh (UPI Core Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-01.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 98.72% (down 1.26 vs Thu 08 Jan),
  Technical Declines at 1.11% (up 0.56 vs Thu 08 Jan). Regression is confined to UPI Core on Punjab National Bank.
- Deepak confirmed the bank timeout / 5xx spike; unrelated flows are green.
- Ishaan noted Customer Complaints 3,596,
  Merchant Complaints 482.

## Decisions
- Treat INC-2026-01 as Sev-2.
- RCA RCA-2026-01 to be drafted by EOD next day; permanent fix under DEC-2026-01.

## Action items
- [ ] Deepak Ghosh: lead investigation for INC-2026-01.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D05-DAILY.

Refs: INC-2026-01, RCA-2026-01, DEC-2026-01, RPT-D05-DAILY, TEAMS-D05-BRIDGE-01

---
id: MTG-D109-BRIDGE-23
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-23T09:30:00
---

# Incident Bridge — UPI Core merchant decline-rate spike (Sev-3)

**Meeting ID:** MTG-D109-BRIDGE-23  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 23 Apr 2026 09:30 IST
**Incident:** INC-2026-23

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Deepak Ghosh (UPI Core Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-23.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 98.55% (down 0.88 vs Wed 22 Apr),
  Technical Declines at 0.37%. Regression is confined to UPI Core on PowerPay Utilities, MetroRide.
- Deepak confirmed the merchant decline-rate spike; unrelated flows are green.
- Ishaan noted Customer Complaints 1,283,
  Merchant Complaints 214.

## Decisions
- Treat INC-2026-23 as Sev-3.
- RCA RCA-2026-23 to be drafted by EOD next day; permanent fix under DEC-2026-23.

## Action items
- [ ] Deepak Ghosh: lead investigation for INC-2026-23.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D109-DAILY.

Refs: INC-2026-23, RCA-2026-23, DEC-2026-23, RPT-D109-DAILY, TEAMS-D109-BRIDGE-23

---
id: MTG-D55-BRIDGE-16
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-28T09:30:00
---

# Incident Bridge — UPI Core fraud / risk spike (Sev-3)

**Meeting ID:** MTG-D55-BRIDGE-16  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 28 Feb 2026 09:30 IST
**Incident:** INC-2026-16

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Deepak Ghosh (UPI Core Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-16.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 98.21% (down 0.13 vs Fri 27 Feb),
  Technical Declines at 0.47% (down 0.03 vs Fri 27 Feb). Regression is confined to UPI Core on Navi.
- Deepak confirmed the fraud / risk spike; unrelated flows are green.
- Ishaan noted Customer Complaints 2,083,
  Merchant Complaints 177.

## Decisions
- Treat INC-2026-16 as Sev-3.
- Handle as a short operational issue; recovery monitoring only.

## Action items
- [ ] Deepak Ghosh: lead investigation for INC-2026-16.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D55-DAILY.

Refs: INC-2026-16, RPT-D55-DAILY, TEAMS-D55-BRIDGE-16

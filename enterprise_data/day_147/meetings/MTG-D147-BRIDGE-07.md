---
id: MTG-D147-BRIDGE-07
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-31T09:30:00
---

# Incident Bridge — UPI Lite X merchant decline-rate spike (Sev-3)

**Meeting ID:** MTG-D147-BRIDGE-07  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 31 May 2026 09:30 IST
**Incident:** INC-2026-07

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Deepak Patel (UPI Lite X Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-07.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 99.2% (up 0.16 vs Sat 30 May),
  Technical Declines at 0.33% (down 0.02 vs Sat 30 May). Regression is confined to UPI Lite X on MetroRide, QuickBite.
- Deepak confirmed the merchant decline-rate spike; unrelated flows are green.
- Ishaan noted Customer Complaints 1,133,
  Merchant Complaints 178.

## Decisions
- Treat INC-2026-07 as Sev-3.
- Handle as a short operational issue; recovery monitoring only.

## Action items
- [ ] Deepak Patel: lead investigation for INC-2026-07.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D147-DAILY.

Refs: INC-2026-07, RPT-D147-DAILY, TEAMS-D147-BRIDGE-07

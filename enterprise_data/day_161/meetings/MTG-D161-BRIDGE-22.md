---
id: MTG-D161-BRIDGE-22
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-29T09:30:00
---

# Incident Bridge — UPI Lite X bank timeout / 5xx spike (Sev-3)

**Meeting ID:** MTG-D161-BRIDGE-22  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 29 Nov 2026 09:30 IST
**Incident:** INC-2026-22

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Deepak Patel (UPI Lite X Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-22.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 98.92% (down 1.06 vs Sat 28 Nov),
  Technical Declines at 0.4% (up 0.15 vs Sat 28 Nov). Regression is confined to UPI Lite X on Bank of Baroda.
- Deepak confirmed the bank timeout / 5xx spike; unrelated flows are green.
- Meera noted Customer Complaints 1,294,
  Merchant Complaints 153.

## Decisions
- Treat INC-2026-22 as Sev-3.
- Handle as a short operational issue; recovery monitoring only.

## Action items
- [ ] Deepak Patel: lead investigation for INC-2026-22.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D161-DAILY.

Refs: INC-2026-22, RPT-D161-DAILY, TEAMS-D161-BRIDGE-22

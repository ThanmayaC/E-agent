---
id: MTG-D114-BRIDGE-11
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-28T09:30:00
---

# Incident Bridge — UPI Lite bank timeout / 5xx spike (Sev-3)

**Meeting ID:** MTG-D114-BRIDGE-11  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 28 Apr 2026 09:30 IST
**Incident:** INC-2026-11

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Yash Gupta (UPI Lite Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-11.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 99.9% (up 0.41 vs Mon 27 Apr),
  Technical Declines at 0.58% (up 0.22 vs Mon 27 Apr). Regression is confined to UPI Lite on Bank of Baroda.
- Yash confirmed the bank timeout / 5xx spike; unrelated flows are green.
- Ishaan noted Customer Complaints 1,802,
  Merchant Complaints 218.

## Decisions
- Treat INC-2026-11 as Sev-3.
- Handle as a short operational issue; recovery monitoring only.

## Action items
- [ ] Yash Gupta: lead investigation for INC-2026-11.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D114-DAILY.

Refs: INC-2026-11, RPT-D114-DAILY, TEAMS-D114-BRIDGE-11

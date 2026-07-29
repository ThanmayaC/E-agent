---
id: MTG-D18-BRIDGE-24
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-22T09:30:00
---

# Incident Bridge — UPI Lite feature-level degradation (Sev-3)

**Meeting ID:** MTG-D18-BRIDGE-24  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 22 Jan 2026 09:30 IST
**Incident:** INC-2026-24

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Yash Gupta (UPI Lite Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-24.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 98.71% (up 0.37 vs Wed 21 Jan),
  Technical Declines at 0.76% (up 0.24 vs Wed 21 Jan). Regression is confined to UPI Lite on UPI Lite.
- Yash confirmed the feature-level degradation; unrelated flows are green.
- Ishaan noted Customer Complaints 2,598,
  Merchant Complaints 214.

## Decisions
- Treat INC-2026-24 as Sev-3.
- RCA RCA-2026-24 to be drafted by EOD next day; permanent fix under DEC-2026-24.

## Action items
- [ ] Yash Gupta: lead investigation for INC-2026-24.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D18-DAILY.

Refs: INC-2026-24, RCA-2026-24, DEC-2026-24, RPT-D18-DAILY, TEAMS-D18-BRIDGE-24

---
id: MTG-D144-BRIDGE-14
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-28T09:30:00
---

# Incident Bridge — UPI Lite PSP callback latency increase (Sev-3)

**Meeting ID:** MTG-D144-BRIDGE-14  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 28 May 2026 09:30 IST
**Incident:** INC-2026-14

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Yash Gupta (UPI Lite Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-14.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 99.98% (up 0.39 vs Wed 27 May),
  Technical Declines at 0.42% (up 0.1 vs Wed 27 May). Regression is confined to UPI Lite on BHIM.
- Yash confirmed the PSP callback latency increase; unrelated flows are green.
- Ishaan noted Customer Complaints 1,378,
  Merchant Complaints 112.

## Decisions
- Treat INC-2026-14 as Sev-3.
- RCA RCA-2026-14 to be drafted by EOD next day; permanent fix under DEC-2026-14.

## Action items
- [ ] Yash Gupta: lead investigation for INC-2026-14.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D144-DAILY.

Refs: INC-2026-14, RCA-2026-14, DEC-2026-14, RPT-D144-DAILY, TEAMS-D144-BRIDGE-14

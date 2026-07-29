---
id: MTG-D78-BRIDGE-12
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-23T09:30:00
---

# Incident Bridge — QR Payments PSP callback latency increase (Sev-3)

**Meeting ID:** MTG-D78-BRIDGE-12  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 23 Mar 2026 09:30 IST
**Incident:** INC-2026-12

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Rekha Rao (QR Payments Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-12.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 98.71% (down 0.92 vs Sun 22 Mar),
  Technical Declines at 0.59% (up 0.09 vs Sun 22 Mar). Regression is confined to QR Payments on BHIM.
- Rekha confirmed the PSP callback latency increase; unrelated flows are green.
- Ishaan noted Customer Complaints 2,049,
  Merchant Complaints 158.

## Decisions
- Treat INC-2026-12 as Sev-3.
- Handle as a short operational issue; recovery monitoring only.

## Action items
- [ ] Rekha Rao: lead investigation for INC-2026-12.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D78-DAILY.

Refs: INC-2026-12, RPT-D78-DAILY, TEAMS-D78-BRIDGE-12

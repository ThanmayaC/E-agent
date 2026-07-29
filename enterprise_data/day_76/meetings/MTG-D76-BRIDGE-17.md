---
id: MTG-D76-BRIDGE-17
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-21T09:30:00
---

# Incident Bridge — QR Payments PSP callback latency increase (Sev-3)

**Meeting ID:** MTG-D76-BRIDGE-17  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 21 Mar 2026 09:30 IST
**Incident:** INC-2026-17

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Rekha Rao (QR Payments Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-17.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 98.4% (down 1.55 vs Fri 20 Mar),
  Technical Declines at 0.55% (up 0.14 vs Fri 20 Mar). Regression is confined to QR Payments on YONO SBI.
- Rekha confirmed the PSP callback latency increase; unrelated flows are green.
- Ishaan noted Customer Complaints 1,931,
  Merchant Complaints 158.

## Decisions
- Treat INC-2026-17 as Sev-3.
- RCA RCA-2026-17 to be drafted by EOD next day; permanent fix under DEC-2026-17.

## Action items
- [ ] Rekha Rao: lead investigation for INC-2026-17.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D76-DAILY.

Refs: INC-2026-17, RCA-2026-17, DEC-2026-17, RPT-D76-DAILY, TEAMS-D76-BRIDGE-17

---
id: MTG-D52-BRIDGE-22
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-25T09:30:00
---

# Incident Bridge — UPI Credit PSP callback latency increase (Sev-3)

**Meeting ID:** MTG-D52-BRIDGE-22  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 25 Feb 2026 09:30 IST
**Incident:** INC-2026-22

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Ishaan Verma (UPI Credit Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-22.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 99.29%,
  Technical Declines at 0.61% (up 0.16 vs Tue 24 Feb). Regression is confined to UPI Credit on Navi.
- Ishaan confirmed the PSP callback latency increase; unrelated flows are green.
- Ishaan noted Customer Complaints 2,328,
  Merchant Complaints 181.

## Decisions
- Treat INC-2026-22 as Sev-3.
- RCA RCA-2026-22 to be drafted by EOD next day; permanent fix under DEC-2026-22.

## Action items
- [ ] Ishaan Verma: lead investigation for INC-2026-22.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D52-DAILY.

Refs: INC-2026-22, RCA-2026-22, DEC-2026-22, RPT-D52-DAILY, TEAMS-D52-BRIDGE-22

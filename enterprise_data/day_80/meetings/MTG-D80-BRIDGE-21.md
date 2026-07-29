---
id: MTG-D80-BRIDGE-21
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-25T09:30:00
---

# Incident Bridge — UPI Credit feature-level degradation (Sev-3)

**Meeting ID:** MTG-D80-BRIDGE-21  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 25 Mar 2026 09:30 IST
**Incident:** INC-2026-21

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Ishaan Verma (UPI Credit Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-21.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 99.56% (up 0.38 vs Tue 24 Mar),
  Technical Declines at 0.6% (up 0.11 vs Tue 24 Mar). Regression is confined to UPI Credit on RuPay Credit on UPI.
- Ishaan confirmed the feature-level degradation; unrelated flows are green.
- Ishaan noted Customer Complaints 1,916,
  Merchant Complaints 155.

## Decisions
- Treat INC-2026-21 as Sev-3.
- RCA RCA-2026-21 to be drafted by EOD next day; permanent fix under DEC-2026-21.

## Action items
- [ ] Ishaan Verma: lead investigation for INC-2026-21.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D80-DAILY.

Refs: INC-2026-21, RCA-2026-21, DEC-2026-21, RPT-D80-DAILY, TEAMS-D80-BRIDGE-21

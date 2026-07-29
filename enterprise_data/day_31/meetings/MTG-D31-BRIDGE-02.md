---
id: MTG-D31-BRIDGE-02
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-04T09:30:00
---

# Incident Bridge — UPI Autopay fraud / risk spike (Sev-2)

**Meeting ID:** MTG-D31-BRIDGE-02  ·  **Type:** Incident Bridge (Sev-2)
**Room:** Virtual Bridge A  ·  **Start:** 04 Feb 2026 09:30 IST
**Incident:** INC-2026-02

## Attendees
- Harsh Nanda (Head of Product Operations)
- Lakshmi Agarwal (Product Analytics Lead)
- Rekha Joshi (UPI Autopay Lead)
- Neha Singh (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Ishaan Sharma (Customer Experience Lead)
- Meera Nair (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-02.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Lakshmi presented the sweep: Success Rate at 98.61% (down 0.93 vs Tue 03 Feb),
  Technical Declines at 0.49% (down 0.01 vs Tue 03 Feb). Regression is confined to UPI Autopay on HDFC MobileBanking.
- Rekha confirmed the fraud / risk spike; unrelated flows are green.
- Ishaan noted Customer Complaints 2,525,
  Merchant Complaints 203.

## Decisions
- Treat INC-2026-02 as Sev-2.
- RCA RCA-2026-02 to be drafted by EOD next day; permanent fix under DEC-2026-02.

## Action items
- [ ] Rekha Joshi: lead investigation for INC-2026-02.
- [ ] Lakshmi Agarwal: complaint + KPI breakdown into RPT-D31-DAILY.

Refs: INC-2026-02, RCA-2026-02, DEC-2026-02, RPT-D31-DAILY, TEAMS-D31-BRIDGE-02

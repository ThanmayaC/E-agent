---
id: MTG-D166-BRIDGE-21
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-04T09:30:00
---

# Incident Bridge — QR Payments feature-level degradation (Sev-3)

**Meeting ID:** MTG-D166-BRIDGE-21  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 04 Dec 2026 09:30 IST
**Incident:** INC-2026-21

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Deepak Rao (QR Payments Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-21.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 99.93% (down 0.05 vs Thu 03 Dec),
  Technical Declines at 0.36% (up 0.12 vs Thu 03 Dec). Regression is confined to QR Payments on QR Payments.
- Deepak confirmed the feature-level degradation; unrelated flows are green.
- Meera noted Customer Complaints 1,156,
  Merchant Complaints 89.

## Decisions
- Treat INC-2026-21 as Sev-3.
- RCA RCA-2026-21 to be drafted by EOD next day; permanent fix under DEC-2026-21.

## Action items
- [ ] Deepak Rao: lead investigation for INC-2026-21.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D166-DAILY.

Refs: INC-2026-21, RCA-2026-21, DEC-2026-21, RPT-D166-DAILY, TEAMS-D166-BRIDGE-21

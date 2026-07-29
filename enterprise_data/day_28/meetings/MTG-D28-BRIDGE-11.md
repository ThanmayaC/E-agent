---
id: MTG-D28-BRIDGE-11
type: meeting
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-19T09:30:00
---

# Incident Bridge — UPI Credit PSP callback latency increase (Sev-3)

**Meeting ID:** MTG-D28-BRIDGE-11  ·  **Type:** Incident Bridge (Sev-3)
**Room:** Virtual Bridge A  ·  **Start:** 19 Jul 2026 09:30 IST
**Incident:** INC-2026-11

## Attendees
- Harsh Nanda (Head of Product Operations)
- Farhan Subramanian (Product Analytics Lead)
- Kavya Nanda (UPI Credit Lead)
- Sanjay Patel (PSP Integration Lead)
- Harsh Pillai (Vice President, Risk & Compliance)
- Meera Nair (Customer Experience Lead)
- Meera Bhat (Merchant Success Lead)

## Agenda
1. Confirm scope and severity of INC-2026-11.
2. Establish the working hypothesis.
3. Assign investigation owners and immediate mitigations.

## Discussion
- Farhan presented the sweep: Success Rate at 99.04% (down 0.76 vs Sat 18 Jul),
  Technical Declines at 0.54% (up 0.13 vs Sat 18 Jul). Regression is confined to UPI Credit on CRED.
- Kavya confirmed the PSP callback latency increase; unrelated flows are green.
- Meera noted Customer Complaints 2,173,
  Merchant Complaints 181.

## Decisions
- Treat INC-2026-11 as Sev-3.
- Handle as a short operational issue; recovery monitoring only.

## Action items
- [ ] Kavya Nanda: lead investigation for INC-2026-11.
- [ ] Farhan Subramanian: complaint + KPI breakdown into RPT-D28-DAILY.

Refs: INC-2026-11, RPT-D28-DAILY, TEAMS-D28-BRIDGE-11

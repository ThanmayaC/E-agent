---
id: INC-2026-21
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-25T09:00:00
---

# Incident Record — INC-2026-21 UPI Credit feature-level degradation

**Incident ID:** INC-2026-21  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Credit  ·  **Commander:** Harsh Nanda
**Detected:** 25 Mar 2026 08:30 IST (morning KPI sweep)

## Summary
A feature-level degradation on RuPay Credit on UPI degraded UPI Credit. Success Rate at
99.56%, Technical Declines 0.6%,
Response Time p95 702 ms. Customer Complaints
1,916, Merchant Complaints 155.

## Impact
Impact concentrated on the UPI Credit path.
Expected active window: 25 Mar - 28 Mar.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Credit.
- 08:30 — anomaly flagged by KPI sweep (RPT-D80-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-21.
Permanent fix tracked as DEC-2026-21.

Refs: upi_kpis_month.xlsx, RPT-D80-DAILY, RCA-2026-21, DEC-2026-21, TEAMS-D80-MON

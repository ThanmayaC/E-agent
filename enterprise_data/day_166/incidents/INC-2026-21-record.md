---
id: INC-2026-21
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-04T09:00:00
---

# Incident Record — INC-2026-21 QR Payments feature-level degradation

**Incident ID:** INC-2026-21  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** QR Payments  ·  **Commander:** Harsh Nanda
**Detected:** 04 Dec 2026 08:30 IST (morning KPI sweep)

## Summary
A feature-level degradation on QR Payments degraded QR Payments. Success Rate at
99.93%, Technical Declines 0.36%,
Response Time p95 584 ms. Customer Complaints
1,156, Merchant Complaints 89.

## Impact
Impact concentrated on the QR Payments path.
Expected active window: 04 Dec - 08 Dec.

## Timeline (day 1)
- 06:25 — first elevated failures on QR Payments.
- 08:30 — anomaly flagged by KPI sweep (RPT-D166-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-21.
Permanent fix tracked as DEC-2026-21.

Refs: upi_kpis_month.xlsx, RPT-D166-DAILY, RCA-2026-21, DEC-2026-21, TEAMS-D166-MON

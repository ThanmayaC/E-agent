---
id: INC-2026-24
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-22T09:00:00
---

# Incident Record — INC-2026-24 UPI Lite feature-level degradation

**Incident ID:** INC-2026-24  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Lite  ·  **Commander:** Harsh Nanda
**Detected:** 22 Jan 2026 08:30 IST (morning KPI sweep)

## Summary
A feature-level degradation on UPI Lite degraded UPI Lite. Success Rate at
98.71%, Technical Declines 0.76%,
Response Time p95 787 ms. Customer Complaints
2,598, Merchant Complaints 214.

## Impact
Impact concentrated on the UPI Lite path.
Expected active window: 22 Jan - 24 Jan.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Lite.
- 08:30 — anomaly flagged by KPI sweep (RPT-D18-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-24.
Permanent fix tracked as DEC-2026-24.

Refs: upi_kpis_month.xlsx, RPT-D18-DAILY, RCA-2026-24, DEC-2026-24, TEAMS-D18-MON

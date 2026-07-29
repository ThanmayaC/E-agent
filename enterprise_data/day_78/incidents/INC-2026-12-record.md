---
id: INC-2026-12
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-23T09:00:00
---

# Incident Record — INC-2026-12 QR Payments PSP callback latency increase

**Incident ID:** INC-2026-12  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** QR Payments  ·  **Commander:** Harsh Nanda
**Detected:** 23 Mar 2026 08:30 IST (morning KPI sweep)

## Summary
A PSP callback latency increase on BHIM degraded QR Payments. Success Rate at
98.71%, Technical Declines 0.59%,
Response Time p95 768 ms. Customer Complaints
2,049, Merchant Complaints 158.

## Impact
Impact concentrated on the QR Payments path.
Expected active window: 23 Mar - 24 Mar.

## Timeline (day 1)
- 06:25 — first elevated failures on QR Payments.
- 08:30 — anomaly flagged by KPI sweep (RPT-D78-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause being triaged as a short operational issue.

Refs: upi_kpis_month.xlsx, RPT-D78-DAILY, TEAMS-D78-MON

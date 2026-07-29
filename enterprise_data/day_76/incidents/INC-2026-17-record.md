---
id: INC-2026-17
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-21T09:00:00
---

# Incident Record — INC-2026-17 QR Payments PSP callback latency increase

**Incident ID:** INC-2026-17  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** QR Payments  ·  **Commander:** Harsh Nanda
**Detected:** 21 Mar 2026 08:30 IST (morning KPI sweep)

## Summary
A PSP callback latency increase on YONO SBI degraded QR Payments. Success Rate at
98.4%, Technical Declines 0.55%,
Response Time p95 747 ms. Customer Complaints
1,931, Merchant Complaints 158.

## Impact
Impact concentrated on the QR Payments path.
Expected active window: 21 Mar - 23 Mar.

## Timeline (day 1)
- 06:25 — first elevated failures on QR Payments.
- 08:30 — anomaly flagged by KPI sweep (RPT-D76-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-17.
Permanent fix tracked as DEC-2026-17.

Refs: upi_kpis_month.xlsx, RPT-D76-DAILY, RCA-2026-17, DEC-2026-17, TEAMS-D76-MON

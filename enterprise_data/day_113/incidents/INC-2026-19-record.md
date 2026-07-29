---
id: INC-2026-19
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-12T09:00:00
---

# Incident Record — INC-2026-19 UPI Lite fraud / risk spike

**Incident ID:** INC-2026-19  ·  **Severity:** Sev-3  ·  **Status:** Investigating
**Product:** UPI Lite  ·  **Commander:** Harsh Nanda
**Detected:** 12 Oct 2026 08:30 IST (morning KPI sweep)

## Summary
A fraud / risk spike on WhatsApp Pay degraded UPI Lite. Success Rate at
99.91%, Technical Declines 0.29%,
Response Time p95 594 ms. Customer Complaints
1,397, Merchant Complaints 118.

## Impact
Impact concentrated on the UPI Lite path.
Expected active window: 12 Oct - 16 Oct.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Lite.
- 08:30 — anomaly flagged by KPI sweep (RPT-D113-DAILY).
- 09:30 — incident bridge convened; Sev-3 confirmed.

Root cause under investigation — see RCA-2026-19.
Permanent fix tracked as DEC-2026-19.

Refs: upi_kpis_month.xlsx, RPT-D113-DAILY, RCA-2026-19, DEC-2026-19, TEAMS-D113-MON

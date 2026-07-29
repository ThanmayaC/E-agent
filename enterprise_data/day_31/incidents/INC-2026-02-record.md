---
id: INC-2026-02
type: incident
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-04T09:00:00
---

# Incident Record — INC-2026-02 UPI Autopay fraud / risk spike

**Incident ID:** INC-2026-02  ·  **Severity:** Sev-2  ·  **Status:** Investigating
**Product:** UPI Autopay  ·  **Commander:** Harsh Nanda
**Detected:** 04 Feb 2026 08:30 IST (morning KPI sweep)

## Summary
A fraud / risk spike on HDFC MobileBanking degraded UPI Autopay. Success Rate at
98.61%, Technical Declines 0.49%,
Response Time p95 716 ms. Customer Complaints
2,525, Merchant Complaints 203.

## Impact
Impact concentrated on the UPI Autopay path.
Expected active window: 04 Feb - 08 Feb.

## Timeline (day 1)
- 06:25 — first elevated failures on UPI Autopay.
- 08:30 — anomaly flagged by KPI sweep (RPT-D31-DAILY).
- 09:30 — incident bridge convened; Sev-2 confirmed.

Root cause under investigation — see RCA-2026-02.
Permanent fix tracked as DEC-2026-02.

Refs: upi_kpis_month.xlsx, RPT-D31-DAILY, RCA-2026-02, DEC-2026-02, TEAMS-D31-MON

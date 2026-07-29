---
id: RPT-D148-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-16T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 16 Nov 2026)

**Report ID:** RPT-D148-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 16 Nov 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 148 of 180)

## Transaction summary
The rail processed 951.4M UPI transactions on Monday — the Monday ramp-up after the weekend — up 1.0M on the same day last week. Success landed at 99.5% and settlement at 99.09%, held back by live issues on FamApp, IndusInd Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 951.4  (▲149.0 d/d, ▲1.0 w/w, ▲206.5 m/m)
- **Success Rate:** 99.5%  (▲0.93 d/d, ▼0.26 w/w, ▼0.1 m/m)
- **Settlement Success:** 99.09%  (▼0.5 d/d, ▼0.89 w/w, ▼0.34 m/m)
- **Technical Declines:** 0.26%  (▼0.03 w/w, ▼0.19 m/m)
- **Business Declines:** 0.21%  (▼0.05 d/d, ▲0.07 w/w, ▲0.01 m/m)
- **Customer Complaints:** 1,201  (▼153 d/d, ▲104 w/w, ▼741 m/m)
- **Merchant Complaints:** 111  (▼13 d/d, ▲9 w/w, ▼100 m/m)
- **Fraud Alerts:** 878  (▼106 d/d, ▲137 w/w, ▼173 m/m)
- **Risk Score:** 30  (▼6 d/d, ▲10 w/w, ▼1 m/m)
- **Response Time:** 562 ms  (▲3 d/d, ▼27 w/w, ▼180 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 305.9 | 99.5% |
| HDFC Bank | 105.0 | 99.55% |
| Bank of Baroda | 75.5 | 99.64% |
| Union Bank of India | 65.5 | 99.43% |
| ICICI Bank | 58.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 453.9 | 99.14% | 231 ms |
| Google Pay | 310.8 | 99.17% | 316 ms |
| Paytm | 76.8 | 99.06% | 192 ms |
| Navi | 35.1 | 99.17% | 225 ms |
| SuperMoney | 18.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 356.8 |
| Person to Person | 337.7 |
| QR Payments | 90.4 |
| UPI Lite | 45.7 |
| UPI Autopay | 31.4 |

## Failure analysis
- INC-2026-17 — merchant settlement delay on IndusInd Bank (day 4 of 4); see RCA-2026-17.
- INC-2026-26 — fraud / risk spike on FamApp (day 2 of 3); see RCA-2026-26.

## Recommendations
Stay on the open incidents: keep recovery monitoring on FamApp, IndusInd Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D148-MON) and any meetings/emails on 16 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D148-MON, RPT-D147-DAILY, INC-2026-17, INC-2026-26, RCA-2026-17, RCA-2026-26

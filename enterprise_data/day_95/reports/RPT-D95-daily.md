---
id: RPT-D95-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-09T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 09 Apr 2026)

**Report ID:** RPT-D95-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 09 Apr 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 95 of 206)

## Transaction summary
The rail processed 704.9M UPI transactions on Thursday — a steady mid-week day — up 0.2M on the same day last week. Success landed at 98.57% and settlement at 99.98%, held back by live issues on State Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 704.9  (▼5.8 d/d, ▲0.2 w/w, ▼91.0 m/m)
- **Success Rate:** 98.57%  (▲0.26 d/d, ▼0.21 w/w, ▼0.56 m/m)
- **Settlement Success:** 99.98%  (▲0.34 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.45%  (▼0.07 d/d, ▲0.05 w/w, ▼0.1 m/m)
- **Business Declines:** 0.19%  (▼0.05 m/m)
- **Customer Complaints:** 1,538  (▼165 d/d, ▲118 w/w, ▼604 m/m)
- **Merchant Complaints:** 170  (▼30 d/d, ▲19 w/w, ▼64 m/m)
- **Fraud Alerts:** 905  (▼2 d/d, ▼17 w/w, ▼255 m/m)
- **Risk Score:** 25  (▼1 w/w, ▼9 m/m)
- **Response Time:** 650 ms  (▼20 d/d, ▲7 w/w, ▼103 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 229.4 | 99.32% |
| HDFC Bank | 75.4 | 99.42% |
| Bank of Baroda | 54.2 | 99.26% |
| Union Bank of India | 47.6 | 99.63% |
| Axis Bank | 43.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 336.7 | 99.51% | 198 ms |
| Google Pay | 230.5 | 99.35% | 241 ms |
| Paytm | 55.9 | 99.53% | 201 ms |
| Navi | 25.9 | 99.53% | 304 ms |
| SuperMoney | 13.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 260.8 |
| Person to Person | 250.2 |
| QR Payments | 67.0 |
| UPI Lite | 33.8 |
| UPI Autopay | 23.3 |

## Failure analysis
- INC-2026-04 — bank timeout / 5xx spike on State Bank of India (day 4 of 4); see RCA-2026-04.

## Recommendations
Stay on the open incident: keep recovery monitoring on State Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D95-MON) and any meetings/emails on 09 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D95-MON, RPT-D94-DAILY, INC-2026-04, RCA-2026-04

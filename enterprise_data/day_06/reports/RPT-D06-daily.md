---
id: RPT-D06-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-10T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 10 Jan 2026)

**Report ID:** RPT-D06-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 10 Jan 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 6 of 206)

## Transaction summary
The rail processed 589.9M UPI transactions on Saturday — a lighter Saturday — the first day in the window. Success landed at 98.82% and settlement at 99.98%, held back by live issues on Punjab National Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 589.9  (▼68.7 d/d, ▼206.0 m/m)
- **Success Rate:** 98.82%  (▲0.1 d/d, ▼0.31 m/m)
- **Settlement Success:** 99.98%  (▲1.12 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.88%  (▼0.23 d/d, ▲0.33 m/m)
- **Business Declines:** 0.24%
- **Customer Complaints:** 2,983  (▼613 d/d, ▲841 m/m)
- **Merchant Complaints:** 389  (▼93 d/d, ▲155 m/m)
- **Fraud Alerts:** 1,139  (▼10 d/d, ▼21 m/m)
- **Risk Score:** 34
- **Response Time:** 828 ms  (▼50 d/d, ▲75 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 192.0 | 99.67% |
| HDFC Bank | 63.1 | 99.42% |
| Bank of Baroda | 45.4 | 99.26% |
| Union Bank of India | 39.8 | 99.63% |
| Axis Bank | 36.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 281.8 | 99.51% | 198 ms |
| Google Pay | 192.9 | 99.35% | 241 ms |
| Paytm | 46.8 | 99.53% | 201 ms |
| Navi | 21.7 | 99.53% | 304 ms |
| SuperMoney | 11.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 218.3 |
| Person to Person | 209.4 |
| QR Payments | 56.0 |
| UPI Lite | 28.3 |
| UPI Autopay | 19.5 |

## Failure analysis
- INC-2026-01 — bank timeout / 5xx spike on Punjab National Bank (day 2 of 4); see RCA-2026-01.

## Recommendations
Stay on the open incident: keep recovery monitoring on Punjab National Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D06-MON) and any meetings/emails on 10 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D06-MON, RPT-D05-DAILY, INC-2026-01, RCA-2026-01

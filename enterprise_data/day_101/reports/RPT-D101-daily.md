---
id: RPT-D101-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-15T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 15 Apr 2026)

**Report ID:** RPT-D101-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 15 Apr 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 101 of 206)

## Transaction summary
The rail processed 709.8M UPI transactions on Wednesday — a steady mid-week day — down 0.9M on the same day last week. Success landed at 99.25% and settlement at 98.65%, held back by live issues on Kotak Mahindra Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 709.8  (▼1.0 d/d, ▼0.9 w/w, ▼86.1 m/m)
- **Success Rate:** 99.25%  (▼0.07 d/d, ▲0.94 w/w, ▲0.12 m/m)
- **Settlement Success:** 98.65%  (▼1.33 d/d, ▼1.33 w/w, ▼1.3 m/m)
- **Technical Declines:** 0.38%  (▲0.01 d/d, ▼0.14 w/w, ▼0.17 m/m)
- **Business Declines:** 0.24%  (▲0.05 d/d, ▲0.05 w/w)
- **Customer Complaints:** 1,511  (▲159 d/d, ▼192 w/w, ▼631 m/m)
- **Merchant Complaints:** 249  (▲107 d/d, ▲49 w/w, ▲15 m/m)
- **Fraud Alerts:** 904  (▲6 d/d, ▼3 w/w, ▼256 m/m)
- **Risk Score:** 25  (▼9 m/m)
- **Response Time:** 629 ms  (▲1 d/d, ▼41 w/w, ▼124 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 231.0 | 99.67% |
| HDFC Bank | 75.9 | 99.42% |
| Bank of Baroda | 54.6 | 99.26% |
| Union Bank of India | 47.9 | 99.63% |
| Axis Bank | 43.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 339.0 | 99.51% | 198 ms |
| Google Pay | 232.1 | 99.35% | 241 ms |
| Paytm | 56.3 | 99.53% | 201 ms |
| Navi | 26.1 | 99.53% | 304 ms |
| SuperMoney | 13.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 262.6 |
| Person to Person | 252.0 |
| QR Payments | 67.4 |
| UPI Lite | 34.1 |
| UPI Autopay | 23.4 |

## Failure analysis
- INC-2026-20 — merchant settlement delay on Kotak Mahindra Bank (day 1 of 3); see RCA-2026-20.

## Recommendations
Stay on the open incident: keep recovery monitoring on Kotak Mahindra Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D101-MON) and any meetings/emails on 15 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D101-MON, RPT-D100-DAILY, INC-2026-20, RCA-2026-20

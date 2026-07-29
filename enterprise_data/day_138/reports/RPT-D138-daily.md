---
id: RPT-D138-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-22T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 22 May 2026)

**Report ID:** RPT-D138-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 22 May 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 138 of 206)

## Transaction summary
The rail processed 708.8M UPI transactions on Friday — a steady mid-week day — down 15.4M on the same day last week. Success landed at 99.23% and settlement at 99.89%, held back by live issues on ICICI Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 708.8  (▼20.2 d/d, ▼15.4 w/w, ▼87.1 m/m)
- **Success Rate:** 99.23%  (▲0.05 d/d, ▼0.75 w/w, ▲0.1 m/m)
- **Settlement Success:** 99.89%  (▼0.09 d/d, ▼0.09 w/w, ▼0.06 m/m)
- **Technical Declines:** 0.33%  (▼0.22 m/m)
- **Business Declines:** 0.22%  (▲0.05 d/d, ▲0.04 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,260  (▲133 d/d, ▲85 w/w, ▼882 m/m)
- **Merchant Complaints:** 206  (▲91 d/d, ▲74 w/w, ▼28 m/m)
- **Fraud Alerts:** 822  (▲1 d/d, ▼18 w/w, ▼338 m/m)
- **Risk Score:** 22  (▼1 w/w, ▼12 m/m)
- **Response Time:** 593 ms  (▼1 d/d, ▼8 w/w, ▼160 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 230.7 | 99.67% |
| HDFC Bank | 75.8 | 99.42% |
| Bank of Baroda | 54.5 | 99.26% |
| Union Bank of India | 47.8 | 99.63% |
| Axis Bank | 43.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 338.6 | 99.51% | 198 ms |
| Google Pay | 231.8 | 99.35% | 241 ms |
| Paytm | 56.2 | 99.53% | 201 ms |
| Navi | 26.1 | 99.53% | 304 ms |
| SuperMoney | 13.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 262.3 |
| Person to Person | 251.6 |
| QR Payments | 67.3 |
| UPI Lite | 34.0 |
| UPI Autopay | 23.4 |

## Failure analysis
- INC-2026-25 — merchant settlement delay on ICICI Bank (day 1 of 2); see INC-2026-25.

## Recommendations
Stay on the open incident: keep recovery monitoring on ICICI Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D138-MON) and any meetings/emails on 22 May.

Refs: upi_kpis_month.xlsx, TEAMS-D138-MON, RPT-D137-DAILY, INC-2026-25

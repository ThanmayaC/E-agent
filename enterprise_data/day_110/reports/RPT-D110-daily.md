---
id: RPT-D110-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-24T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 24 Apr 2026)

**Report ID:** RPT-D110-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 24 Apr 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 110 of 206)

## Transaction summary
The rail processed 703.8M UPI transactions on Friday — a steady mid-week day — up 0.6M on the same day last week. Success landed at 99.98% and settlement at 99.31%, held back by live issues on PowerPay Utilities, MetroRide (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 703.8  (▼6.1 d/d, ▲0.6 w/w, ▼92.1 m/m)
- **Success Rate:** 99.98%  (▲1.43 d/d, ▲0.74 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.31%  (▼0.67 d/d, ▼0.67 w/w, ▼0.64 m/m)
- **Technical Declines:** 0.36%  (▼0.01 d/d, ▼0.01 w/w, ▼0.19 m/m)
- **Business Declines:** 0.23%  (▼0.03 d/d, ▲0.03 w/w, ▼0.01 m/m)
- **Customer Complaints:** 1,287  (▲4 d/d, ▼109 w/w, ▼855 m/m)
- **Merchant Complaints:** 184  (▼30 d/d, ▲9 w/w, ▼50 m/m)
- **Fraud Alerts:** 880  (▲10 d/d, ▼8 w/w, ▼280 m/m)
- **Risk Score:** 24  (▼1 w/w, ▼10 m/m)
- **Response Time:** 620 ms  (▼6 d/d, ▼14 w/w, ▼133 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 229.1 | 99.67% |
| HDFC Bank | 75.2 | 99.42% |
| Bank of Baroda | 54.2 | 99.26% |
| Union Bank of India | 47.5 | 99.63% |
| Axis Bank | 43.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 336.2 | 99.51% | 198 ms |
| Google Pay | 230.2 | 99.35% | 241 ms |
| Paytm | 55.8 | 99.53% | 201 ms |
| Navi | 25.9 | 99.53% | 304 ms |
| SuperMoney | 13.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 260.4 |
| Person to Person | 249.8 |
| QR Payments | 66.9 |
| UPI Lite | 33.8 |
| UPI Autopay | 23.2 |

## Failure analysis
- INC-2026-23 — merchant decline-rate spike on PowerPay Utilities, MetroRide (day 2 of 4); see RCA-2026-23.

## Recommendations
Stay on the open incident: keep recovery monitoring on PowerPay Utilities, MetroRide and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D110-MON) and any meetings/emails on 24 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D110-MON, RPT-D109-DAILY, INC-2026-23, RCA-2026-23

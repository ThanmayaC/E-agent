---
id: RPT-D111-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-25T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 25 Apr 2026)

**Report ID:** RPT-D111-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 25 Apr 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 111 of 206)

## Transaction summary
The rail processed 651.3M UPI transactions on Saturday — a lighter Saturday — up 10.9M on the same day last week. Success landed at 98.6% and settlement at 99.91%, held back by live issues on PowerPay Utilities, MetroRide (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 651.3  (▼52.5 d/d, ▲10.9 w/w, ▼144.6 m/m)
- **Success Rate:** 98.6%  (▼1.38 d/d, ▼0.54 w/w, ▼0.53 m/m)
- **Settlement Success:** 99.91%  (▲0.6 d/d, ▲0.66 w/w, ▼0.04 m/m)
- **Technical Declines:** 0.36%  (▼0.01 w/w, ▼0.19 m/m)
- **Business Declines:** 0.21%  (▼0.02 d/d, ▲0.02 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,287  (▼33 w/w, ▼855 m/m)
- **Merchant Complaints:** 160  (▼24 d/d, ▲22 w/w, ▼74 m/m)
- **Fraud Alerts:** 879  (▼1 d/d, ▼9 w/w, ▼281 m/m)
- **Risk Score:** 24  (▼1 w/w, ▼10 m/m)
- **Response Time:** 621 ms  (▲1 d/d, ▼8 w/w, ▼132 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 212.0 | 99.67% |
| HDFC Bank | 69.6 | 99.42% |
| Bank of Baroda | 50.1 | 99.26% |
| Union Bank of India | 43.9 | 99.63% |
| Axis Bank | 40.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 311.1 | 99.51% | 198 ms |
| Google Pay | 213.0 | 99.35% | 241 ms |
| Paytm | 51.7 | 99.53% | 201 ms |
| Navi | 23.9 | 99.53% | 304 ms |
| SuperMoney | 12.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 241.0 |
| Person to Person | 231.2 |
| QR Payments | 61.9 |
| UPI Lite | 31.3 |
| UPI Autopay | 21.5 |

## Failure analysis
- INC-2026-23 — merchant decline-rate spike on PowerPay Utilities, MetroRide (day 3 of 4); see RCA-2026-23.

## Recommendations
Stay on the open incident: keep recovery monitoring on PowerPay Utilities, MetroRide and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D111-MON) and any meetings/emails on 25 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D111-MON, RPT-D110-DAILY, INC-2026-23, RCA-2026-23

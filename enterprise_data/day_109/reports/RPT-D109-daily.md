---
id: RPT-D109-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-23T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 23 Apr 2026)

**Report ID:** RPT-D109-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 23 Apr 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 109 of 206)

## Transaction summary
The rail processed 709.9M UPI transactions on Thursday — a steady mid-week day — up 12.0M on the same day last week. Success landed at 98.55% and settlement at 99.98%, held back by live issues on PowerPay Utilities, MetroRide (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 709.9  (▲12.9 d/d, ▲12.0 w/w, ▼86.0 m/m)
- **Success Rate:** 98.55%  (▼0.88 d/d, ▼1.11 w/w, ▼0.58 m/m)
- **Settlement Success:** 99.98%  (▲0.94 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.37%  (▼0.18 m/m)
- **Business Declines:** 0.26%  (▲0.08 d/d, ▲0.04 w/w, ▲0.02 m/m)
- **Customer Complaints:** 1,283  (▼23 d/d, ▼157 w/w, ▼859 m/m)
- **Merchant Complaints:** 214  (▲79 d/d, ▲10 w/w, ▼20 m/m)
- **Fraud Alerts:** 870  (▼17 d/d, ▼25 w/w, ▼290 m/m)
- **Risk Score:** 24  (▼1 w/w, ▼10 m/m)
- **Response Time:** 626 ms  (▼4 d/d, ▼8 w/w, ▼127 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 231.1 | 99.67% |
| HDFC Bank | 75.9 | 99.42% |
| Bank of Baroda | 54.6 | 99.26% |
| Union Bank of India | 47.9 | 99.63% |
| Axis Bank | 43.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 339.1 | 99.51% | 198 ms |
| Google Pay | 232.2 | 99.35% | 241 ms |
| Paytm | 56.3 | 99.53% | 201 ms |
| Navi | 26.1 | 99.53% | 304 ms |
| SuperMoney | 13.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 262.7 |
| Person to Person | 252.0 |
| QR Payments | 67.4 |
| UPI Lite | 34.1 |
| UPI Autopay | 23.4 |

## Failure analysis
- INC-2026-23 — merchant decline-rate spike on PowerPay Utilities, MetroRide (day 1 of 4); see RCA-2026-23.

## Recommendations
Stay on the open incident: keep recovery monitoring on PowerPay Utilities, MetroRide and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D109-MON) and any meetings/emails on 23 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D109-MON, RPT-D108-DAILY, INC-2026-23, RCA-2026-23

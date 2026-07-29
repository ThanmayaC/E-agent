---
id: RPT-D128-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-12T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 12 May 2026)

**Report ID:** RPT-D128-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 12 May 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 128 of 206)

## Transaction summary
The rail processed 707.8M UPI transactions on Tuesday — a steady mid-week day — down 16.3M on the same day last week. Success landed at 99.63% and settlement at 99.98%, held back by live issues on TravelGo, InsureWell (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 707.8  (▲21.5 d/d, ▼16.3 w/w, ▼88.1 m/m)
- **Success Rate:** 99.63%  (▼0.06 d/d, ▲0.8 w/w, ▲0.5 m/m)
- **Settlement Success:** 99.98%  (▲1.07 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.34%  (▼0.01 w/w, ▼0.21 m/m)
- **Business Declines:** 0.25%  (▲0.07 d/d, ▲0.07 w/w, ▲0.01 m/m)
- **Customer Complaints:** 1,181  (▼32 d/d, ▼29 w/w, ▼961 m/m)
- **Merchant Complaints:** 195  (▲58 d/d, ▲68 w/w, ▼39 m/m)
- **Fraud Alerts:** 836  (▼8 d/d, ▼10 w/w, ▼324 m/m)
- **Risk Score:** 23  (▼11 m/m)
- **Response Time:** 605 ms  (▲2 w/w, ▼148 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 230.4 | 99.67% |
| HDFC Bank | 75.7 | 99.42% |
| Bank of Baroda | 54.5 | 99.26% |
| Union Bank of India | 47.7 | 99.63% |
| Axis Bank | 43.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 338.1 | 99.51% | 198 ms |
| Google Pay | 231.5 | 99.35% | 241 ms |
| Paytm | 56.1 | 99.53% | 201 ms |
| Navi | 26.0 | 99.53% | 304 ms |
| SuperMoney | 13.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 261.9 |
| Person to Person | 251.3 |
| QR Payments | 67.2 |
| UPI Lite | 34.0 |
| UPI Autopay | 23.4 |

## Failure analysis
- INC-2026-13 — merchant decline-rate spike on TravelGo, InsureWell (day 1 of 5); see RCA-2026-13.

## Recommendations
Stay on the open incident: keep recovery monitoring on TravelGo, InsureWell and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D128-MON) and any meetings/emails on 12 May.

Refs: upi_kpis_month.xlsx, TEAMS-D128-MON, RPT-D127-DAILY, INC-2026-13, RCA-2026-13

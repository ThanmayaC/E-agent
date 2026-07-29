---
id: RPT-D94-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-08T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 08 Apr 2026)

**Report ID:** RPT-D94-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 08 Apr 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 94 of 206)

## Transaction summary
The rail processed 710.7M UPI transactions on Wednesday — a steady mid-week day — up 15.1M on the same day last week. Success landed at 98.31% and settlement at 99.98%, held back by live issues on State Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 710.7  (▲19.6 d/d, ▲15.1 w/w, ▼85.2 m/m)
- **Success Rate:** 98.31%  (▼0.7 d/d, ▼1.48 w/w, ▼0.82 m/m)
- **Settlement Success:** 99.98%  (▲0.14 d/d, ▲1.26 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.52%  (▼0.12 d/d, ▲0.12 w/w, ▼0.03 m/m)
- **Business Declines:** 0.19%  (▼0.05 m/m)
- **Customer Complaints:** 1,703  (▼282 d/d, ▲262 w/w, ▼439 m/m)
- **Merchant Complaints:** 200  (▼44 d/d, ▲48 w/w, ▼34 m/m)
- **Fraud Alerts:** 907  (▼11 d/d, ▼22 w/w, ▼253 m/m)
- **Risk Score:** 25  (▼1 d/d, ▼1 w/w, ▼9 m/m)
- **Response Time:** 670 ms  (▼34 d/d, ▲20 w/w, ▼83 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 231.3 | 98.92% |
| HDFC Bank | 76.0 | 99.42% |
| Bank of Baroda | 54.7 | 99.26% |
| Union Bank of India | 47.9 | 99.63% |
| Axis Bank | 43.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 339.5 | 99.51% | 198 ms |
| Google Pay | 232.4 | 99.35% | 241 ms |
| Paytm | 56.4 | 99.53% | 201 ms |
| Navi | 26.1 | 99.53% | 304 ms |
| SuperMoney | 13.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 263.0 |
| Person to Person | 252.3 |
| QR Payments | 67.5 |
| UPI Lite | 34.1 |
| UPI Autopay | 23.5 |

## Failure analysis
- INC-2026-04 — bank timeout / 5xx spike on State Bank of India (day 3 of 4); see RCA-2026-04.

## Recommendations
Stay on the open incident: keep recovery monitoring on State Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D94-MON) and any meetings/emails on 08 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D94-MON, RPT-D93-DAILY, INC-2026-04, RCA-2026-04

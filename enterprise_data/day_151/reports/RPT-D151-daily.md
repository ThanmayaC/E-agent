---
id: RPT-D151-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-04T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 04 Jun 2026)

**Report ID:** RPT-D151-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 04 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 151 of 206)

## Transaction summary
The rail processed 745.8M UPI transactions on Thursday — a steady mid-week day — down 50.1M on the same day last week. Success landed at 99.21% and settlement at 99.5%, held back by live issues on Punjab National Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 745.8  (▲5.6 d/d, ▼50.1 w/w, ▼50.1 m/m)
- **Success Rate:** 99.21%  (▼0.2 d/d, ▼0.77 w/w, ▲0.08 m/m)
- **Settlement Success:** 99.5%  (▲0.56 d/d, ▲0.49 w/w, ▼0.45 m/m)
- **Technical Declines:** 0.63%  (▲0.32 d/d, ▲0.21 w/w, ▲0.08 m/m)
- **Business Declines:** 0.16%  (▼0.01 d/d, ▼0.01 w/w, ▼0.08 m/m)
- **Customer Complaints:** 1,795  (▲725 d/d, ▲417 w/w, ▼347 m/m)
- **Merchant Complaints:** 226  (▲117 d/d, ▲114 w/w, ▼8 m/m)
- **Fraud Alerts:** 787  (▼6 d/d, ▼24 w/w, ▼373 m/m)
- **Risk Score:** 21  (▼1 w/w, ▼13 m/m)
- **Response Time:** 662 ms  (▲90 d/d, ▼4 w/w, ▼91 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 242.8 | 99.67% |
| HDFC Bank | 79.7 | 99.42% |
| Bank of Baroda | 57.4 | 99.26% |
| Union Bank of India | 50.3 | 99.63% |
| Axis Bank | 46.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 356.2 | 99.51% | 198 ms |
| Google Pay | 243.9 | 99.35% | 241 ms |
| Paytm | 59.2 | 99.53% | 201 ms |
| Navi | 27.4 | 99.53% | 304 ms |
| SuperMoney | 14.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 275.9 |
| Person to Person | 264.8 |
| QR Payments | 70.9 |
| UPI Lite | 35.8 |
| UPI Autopay | 24.6 |

## Failure analysis
- INC-2026-06 — bank timeout / 5xx spike on Punjab National Bank (day 1 of 3); see RCA-2026-06.

## Recommendations
Stay on the open incident: keep recovery monitoring on Punjab National Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D151-MON) and any meetings/emails on 04 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D151-MON, RPT-D150-DAILY, INC-2026-06, RCA-2026-06

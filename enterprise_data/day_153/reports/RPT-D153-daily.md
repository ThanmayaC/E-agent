---
id: RPT-D153-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-06T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 06 Jun 2026)

**Report ID:** RPT-D153-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 06 Jun 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 153 of 206)

## Transaction summary
The rail processed 647.7M UPI transactions on Saturday — a lighter Saturday — down 153.8M on the same day last week. Success landed at 99.06% and settlement at 98.99%, held back by live issues on Punjab National Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 647.7  (▼85.4 d/d, ▼153.8 w/w, ▼148.2 m/m)
- **Success Rate:** 99.06%  (▲0.2 d/d, ▲0.02 w/w, ▼0.07 m/m)
- **Settlement Success:** 98.99%  (▼0.98 d/d, ▼0.29 w/w, ▼0.96 m/m)
- **Technical Declines:** 0.42%  (▼0.09 d/d, ▲0.07 w/w, ▼0.13 m/m)
- **Business Declines:** 0.16%  (▼0.01 w/w, ▼0.08 m/m)
- **Customer Complaints:** 1,292  (▼230 d/d, ▲109 w/w, ▼850 m/m)
- **Merchant Complaints:** 148  (▼34 d/d, ▲36 w/w, ▼86 m/m)
- **Fraud Alerts:** 786  (▲4 d/d, ▼23 w/w, ▼374 m/m)
- **Risk Score:** 21  (▼1 w/w, ▼13 m/m)
- **Response Time:** 609 ms  (▼26 d/d, ▼2 w/w, ▼144 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 210.8 | 99.67% |
| HDFC Bank | 69.2 | 99.42% |
| Bank of Baroda | 49.8 | 99.26% |
| Union Bank of India | 43.7 | 99.63% |
| Axis Bank | 39.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 309.4 | 99.51% | 198 ms |
| Google Pay | 211.8 | 99.35% | 241 ms |
| Paytm | 51.4 | 99.53% | 201 ms |
| Navi | 23.8 | 99.53% | 304 ms |
| SuperMoney | 12.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 239.6 |
| Person to Person | 229.9 |
| QR Payments | 61.5 |
| UPI Lite | 31.1 |
| UPI Autopay | 21.4 |

## Failure analysis
- INC-2026-06 — bank timeout / 5xx spike on Punjab National Bank (day 3 of 3); see RCA-2026-06.

## Recommendations
Stay on the open incident: keep recovery monitoring on Punjab National Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D153-MON) and any meetings/emails on 06 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D153-MON, RPT-D152-DAILY, INC-2026-06, RCA-2026-06

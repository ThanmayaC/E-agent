---
id: RPT-D115-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-29T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 29 Apr 2026)

**Report ID:** RPT-D115-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 29 Apr 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 115 of 206)

## Transaction summary
The rail processed 781.4M UPI transactions on Wednesday — the month-end surge as salary and bill-pay flows land — up 84.4M on the same day last week. Success landed at 99.3% and settlement at 99.55%, held back by live issues on Bank of Baroda (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 781.4  (▼10.6 d/d, ▲84.4 w/w, ▼14.5 m/m)
- **Success Rate:** 99.3%  (▼0.6 d/d, ▼0.13 w/w, ▲0.17 m/m)
- **Settlement Success:** 99.55%  (▲0.46 d/d, ▼0.43 w/w, ▼0.4 m/m)
- **Technical Declines:** 0.49%  (▼0.09 d/d, ▲0.12 w/w, ▼0.06 m/m)
- **Business Declines:** 0.18%  (▼0.06 m/m)
- **Customer Complaints:** 1,589  (▼213 d/d, ▲283 w/w, ▼553 m/m)
- **Merchant Complaints:** 183  (▼35 d/d, ▲48 w/w, ▼51 m/m)
- **Fraud Alerts:** 863  (▼6 d/d, ▼24 w/w, ▼297 m/m)
- **Risk Score:** 24  (▼10 m/m)
- **Response Time:** 647 ms  (▼31 d/d, ▲17 w/w, ▼106 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 254.3 | 99.67% |
| HDFC Bank | 83.5 | 99.42% |
| Bank of Baroda | 60.1 | 98.82% |
| Union Bank of India | 52.7 | 99.63% |
| Axis Bank | 48.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 373.2 | 99.51% | 198 ms |
| Google Pay | 255.5 | 99.35% | 241 ms |
| Paytm | 62.0 | 99.53% | 201 ms |
| Navi | 28.7 | 99.53% | 304 ms |
| SuperMoney | 15.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 289.1 |
| Person to Person | 277.4 |
| QR Payments | 74.2 |
| UPI Lite | 37.5 |
| UPI Autopay | 25.8 |

## Failure analysis
- INC-2026-11 — bank timeout / 5xx spike on Bank of Baroda (day 2 of 2); see INC-2026-11.

## Recommendations
Stay on the open incident: keep recovery monitoring on Bank of Baroda and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D115-MON) and any meetings/emails on 29 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D115-MON, RPT-D114-DAILY, INC-2026-11

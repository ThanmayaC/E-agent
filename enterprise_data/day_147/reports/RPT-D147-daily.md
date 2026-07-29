---
id: RPT-D147-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-31T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 31 May 2026)

**Report ID:** RPT-D147-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 31 May 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 147 of 206)

## Transaction summary
The rail processed 824.9M UPI transactions on Sunday — the month-end surge as salary and bill-pay flows land — up 224.6M on the same day last week. Success landed at 99.2% and settlement at 99.98%, held back by live issues on BHIM, MetroRide, QuickBite (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 824.9  (▲23.4 d/d, ▲224.6 w/w, ▲29.0 m/m)
- **Success Rate:** 99.2%  (▲0.16 d/d, ▼0.43 w/w, ▲0.07 m/m)
- **Settlement Success:** 99.98%  (▲0.7 d/d, ▲0.55 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.33%  (▼0.02 d/d, ▼0.22 m/m)
- **Business Declines:** 0.24%  (▲0.07 d/d, ▼0.06 w/w)
- **Customer Complaints:** 1,133  (▼50 d/d, ▼382 w/w, ▼1009 m/m)
- **Merchant Complaints:** 178  (▲66 d/d, ▲65 w/w, ▼56 m/m)
- **Fraud Alerts:** 803  (▼6 d/d, ▼291 w/w, ▼357 m/m)
- **Risk Score:** 21  (▼1 d/d, ▼20 w/w, ▼13 m/m)
- **Response Time:** 586 ms  (▼25 d/d, ▼2 w/w, ▼167 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 268.5 | 99.67% |
| HDFC Bank | 88.2 | 99.42% |
| Bank of Baroda | 63.5 | 99.26% |
| Union Bank of India | 55.6 | 99.63% |
| Axis Bank | 50.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 394.0 | 99.51% | 198 ms |
| Google Pay | 269.8 | 99.35% | 241 ms |
| Paytm | 65.4 | 99.53% | 201 ms |
| Navi | 30.3 | 99.53% | 304 ms |
| SuperMoney | 16.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 305.2 |
| Person to Person | 292.8 |
| QR Payments | 78.4 |
| UPI Lite | 39.6 |
| UPI Autopay | 27.2 |

## Failure analysis
- INC-2026-14 — PSP callback latency increase on BHIM (day 4 of 5); see RCA-2026-14.
- INC-2026-07 — merchant decline-rate spike on MetroRide, QuickBite (day 1 of 2); see INC-2026-07.

## Recommendations
Stay on the open incidents: keep recovery monitoring on BHIM, MetroRide, QuickBite and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D147-MON) and any meetings/emails on 31 May.

Refs: upi_kpis_month.xlsx, TEAMS-D147-MON, RPT-D146-DAILY, INC-2026-14, INC-2026-07, RCA-2026-14

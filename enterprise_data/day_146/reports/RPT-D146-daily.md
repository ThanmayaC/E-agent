---
id: RPT-D146-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-30T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 30 May 2026)

**Report ID:** RPT-D146-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 30 May 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 146 of 206)

## Transaction summary
The rail processed 801.5M UPI transactions on Saturday — the month-end surge as salary and bill-pay flows land — up 151.9M on the same day last week. Success landed at 99.04% and settlement at 99.28%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 801.5  (▼7.4 d/d, ▲151.9 w/w, ▲5.6 m/m)
- **Success Rate:** 99.04%  (▼0.58 d/d, ▲0.14 w/w, ▼0.09 m/m)
- **Settlement Success:** 99.28%  (▼0.22 d/d, ▼0.44 w/w, ▼0.67 m/m)
- **Technical Declines:** 0.35%  (▼0.03 d/d, ▲0.03 w/w, ▼0.2 m/m)
- **Business Declines:** 0.17%  (▼0.03 w/w, ▼0.07 m/m)
- **Customer Complaints:** 1,183  (▼85 d/d, ▼26 w/w, ▼959 m/m)
- **Merchant Complaints:** 112  (▼58 w/w, ▼122 m/m)
- **Fraud Alerts:** 809  (▲9 d/d, ▼13 w/w, ▼351 m/m)
- **Risk Score:** 22  (▼12 m/m)
- **Response Time:** 611 ms  (▼14 d/d, ▲20 w/w, ▼142 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 260.9 | 99.67% |
| HDFC Bank | 85.7 | 99.42% |
| Bank of Baroda | 61.7 | 99.26% |
| Union Bank of India | 54.1 | 99.63% |
| Axis Bank | 49.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 382.8 | 99.51% | 198 ms |
| Google Pay | 262.1 | 99.35% | 241 ms |
| Paytm | 63.6 | 99.53% | 201 ms |
| Navi | 29.5 | 99.53% | 304 ms |
| SuperMoney | 15.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 296.6 |
| Person to Person | 284.5 |
| QR Payments | 76.1 |
| UPI Lite | 38.5 |
| UPI Autopay | 26.4 |

## Failure analysis
- INC-2026-14 — PSP callback latency increase on BHIM (day 3 of 5); see RCA-2026-14.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D146-MON) and any meetings/emails on 30 May.

Refs: upi_kpis_month.xlsx, TEAMS-D146-MON, RPT-D145-DAILY, INC-2026-14, RCA-2026-14

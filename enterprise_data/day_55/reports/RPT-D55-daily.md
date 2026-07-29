---
id: RPT-D55-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-28T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 28 Feb 2026)

**Report ID:** RPT-D55-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 28 Feb 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 55 of 206)

## Transaction summary
The rail processed 767.6M UPI transactions on Saturday — the month-end surge as salary and bill-pay flows land — up 159.8M on the same day last week. Success landed at 98.21% and settlement at 99.62%, held back by live issues on Navi (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 767.6  (▼53.6 d/d, ▲159.8 w/w, ▼28.3 m/m)
- **Success Rate:** 98.21%  (▼0.13 d/d, ▼1.13 w/w, ▼0.92 m/m)
- **Settlement Success:** 99.62%  (▲0.66 d/d, ▼0.2 w/w, ▼0.33 m/m)
- **Technical Declines:** 0.47%  (▼0.03 d/d, ▲0.01 w/w, ▼0.08 m/m)
- **Business Declines:** 0.3%  (▲0.09 d/d, ▲0.09 w/w, ▲0.06 m/m)
- **Customer Complaints:** 2,083  (▲273 d/d, ▲355 w/w, ▼59 m/m)
- **Merchant Complaints:** 177  (▼3 d/d, ▼7 w/w, ▼57 m/m)
- **Fraud Alerts:** 1,203  (▲201 d/d, ▲173 w/w, ▲43 m/m)
- **Risk Score:** 43  (▲14 d/d, ▲13 w/w, ▲9 m/m)
- **Response Time:** 704 ms  (▼12 d/d, ▲5 w/w, ▼49 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 249.9 | 99.67% |
| HDFC Bank | 82.1 | 99.42% |
| Bank of Baroda | 59.1 | 99.26% |
| Union Bank of India | 51.8 | 99.63% |
| Axis Bank | 47.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 366.6 | 99.51% | 198 ms |
| Google Pay | 251.0 | 99.35% | 241 ms |
| Paytm | 60.9 | 99.53% | 201 ms |
| Navi | 28.2 | 98.83% | 494 ms |
| SuperMoney | 15.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 284.0 |
| Person to Person | 272.5 |
| QR Payments | 72.9 |
| UPI Lite | 36.8 |
| UPI Autopay | 25.3 |

## Failure analysis
- INC-2026-22 — PSP callback latency increase on Navi (day 4 of 4); see RCA-2026-22.
- INC-2026-16 — fraud / risk spike on Navi (day 1 of 2); see INC-2026-16.

## Recommendations
Stay on the open incidents: keep recovery monitoring on Navi and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D55-MON) and any meetings/emails on 28 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D55-MON, RPT-D54-DAILY, INC-2026-22, INC-2026-16, RCA-2026-22

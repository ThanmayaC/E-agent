---
id: RPT-D144-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-28T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 28 May 2026)

**Report ID:** RPT-D144-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 28 May 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 144 of 206)

## Transaction summary
The rail processed 795.9M UPI transactions on Thursday — the month-end surge as salary and bill-pay flows land — up 66.9M on the same day last week. Success landed at 99.98% and settlement at 99.01%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 795.9  (▲83.6 d/d, ▲66.9 w/w)
- **Success Rate:** 99.98%  (▲0.39 d/d, ▲0.8 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.01%  (▼0.97 d/d, ▼0.97 w/w, ▼0.94 m/m)
- **Technical Declines:** 0.42%  (▲0.1 d/d, ▲0.09 w/w, ▼0.13 m/m)
- **Business Declines:** 0.17%  (▼0.02 d/d, ▼0.07 m/m)
- **Customer Complaints:** 1,378  (▲221 d/d, ▲251 w/w, ▼764 m/m)
- **Merchant Complaints:** 112  (▼1 d/d, ▼3 w/w, ▼122 m/m)
- **Fraud Alerts:** 811  (▼48 d/d, ▼10 w/w, ▼349 m/m)
- **Risk Score:** 22  (▼3 d/d, ▼12 m/m)
- **Response Time:** 666 ms  (▲80 d/d, ▲72 w/w, ▼87 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 259.1 | 99.67% |
| HDFC Bank | 85.1 | 99.42% |
| Bank of Baroda | 61.3 | 99.26% |
| Union Bank of India | 53.7 | 99.63% |
| Axis Bank | 49.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 380.2 | 99.51% | 198 ms |
| Google Pay | 260.3 | 99.35% | 241 ms |
| Paytm | 63.1 | 99.53% | 201 ms |
| Navi | 29.3 | 99.53% | 304 ms |
| SuperMoney | 15.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 294.5 |
| Person to Person | 282.5 |
| QR Payments | 75.6 |
| UPI Lite | 38.2 |
| UPI Autopay | 26.3 |

## Failure analysis
- INC-2026-14 — PSP callback latency increase on BHIM (day 1 of 5); see RCA-2026-14.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D144-MON) and any meetings/emails on 28 May.

Refs: upi_kpis_month.xlsx, TEAMS-D144-MON, RPT-D143-DAILY, INC-2026-14, RCA-2026-14

---
id: RPT-D114-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-28T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 28 Apr 2026)

**Report ID:** RPT-D114-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 28 Apr 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 114 of 206)

## Transaction summary
The rail processed 792.0M UPI transactions on Tuesday — the month-end surge as salary and bill-pay flows land — up 90.7M on the same day last week. Success landed at 99.9% and settlement at 99.09%, held back by live issues on Bank of Baroda (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 792.0  (▲105.3 d/d, ▲90.7 w/w, ▼3.9 m/m)
- **Success Rate:** 99.9%  (▲0.41 d/d, ▼0.08 w/w, ▲0.77 m/m)
- **Settlement Success:** 99.09%  (▼0.34 d/d, ▼0.89 w/w, ▼0.86 m/m)
- **Technical Declines:** 0.58%  (▲0.22 d/d, ▲0.21 w/w, ▲0.03 m/m)
- **Business Declines:** 0.18%  (▼0.06 m/m)
- **Customer Complaints:** 1,802  (▲528 d/d, ▲492 w/w, ▼340 m/m)
- **Merchant Complaints:** 218  (▲86 d/d, ▲83 w/w, ▼16 m/m)
- **Fraud Alerts:** 869  (▼1 d/d, ▼17 w/w, ▼291 m/m)
- **Risk Score:** 24  (▼10 m/m)
- **Response Time:** 678 ms  (▲66 d/d, ▲53 w/w, ▼75 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 257.8 | 99.67% |
| HDFC Bank | 84.7 | 99.42% |
| Bank of Baroda | 61.0 | 98.54% |
| Union Bank of India | 53.4 | 99.63% |
| Axis Bank | 48.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 378.3 | 99.51% | 198 ms |
| Google Pay | 259.0 | 99.35% | 241 ms |
| Paytm | 62.8 | 99.53% | 201 ms |
| Navi | 29.1 | 99.53% | 304 ms |
| SuperMoney | 15.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 293.0 |
| Person to Person | 281.2 |
| QR Payments | 75.2 |
| UPI Lite | 38.0 |
| UPI Autopay | 26.1 |

## Failure analysis
- INC-2026-11 — bank timeout / 5xx spike on Bank of Baroda (day 1 of 2); see INC-2026-11.

## Recommendations
Stay on the open incident: keep recovery monitoring on Bank of Baroda and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D114-MON) and any meetings/emails on 28 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D114-MON, RPT-D113-DAILY, INC-2026-11

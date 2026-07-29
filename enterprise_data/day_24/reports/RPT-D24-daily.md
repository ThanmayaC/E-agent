---
id: RPT-D24-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-28T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 28 Jan 2026)

**Report ID:** RPT-D24-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 28 Jan 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 24 of 206)

## Transaction summary
The rail processed 759.5M UPI transactions on Wednesday — the month-end surge as salary and bill-pay flows land — up 90.1M on the same day last week. Success landed at 99.55% and settlement at 99.69%, held back by live issues on FamApp (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 759.5  (▲84.8 d/d, ▲90.1 w/w, ▼36.4 m/m)
- **Success Rate:** 99.55%  (▲0.23 d/d, ▲1.21 w/w, ▲0.42 m/m)
- **Settlement Success:** 99.69%  (▼0.29 d/d, ▲0.37 w/w, ▼0.26 m/m)
- **Technical Declines:** 0.51%  (▼0.01 w/w, ▼0.04 m/m)
- **Business Declines:** 0.29%  (▼0.05 d/d, ▲0.06 w/w, ▲0.05 m/m)
- **Customer Complaints:** 2,170  (▼178 d/d, ▲191 w/w, ▲28 m/m)
- **Merchant Complaints:** 210  (▲1 d/d, ▼8 w/w, ▼24 m/m)
- **Fraud Alerts:** 1,219  (▼105 d/d, ▲109 w/w, ▲59 m/m)
- **Risk Score:** 41  (▼7 d/d, ▲9 w/w, ▲7 m/m)
- **Response Time:** 728 ms  (▼7 d/d, ▼3 w/w, ▼25 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 247.2 | 99.67% |
| HDFC Bank | 81.2 | 99.42% |
| Bank of Baroda | 58.5 | 99.26% |
| Union Bank of India | 51.2 | 99.63% |
| Axis Bank | 46.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 362.8 | 99.51% | 198 ms |
| Google Pay | 248.4 | 99.35% | 241 ms |
| Paytm | 60.2 | 99.53% | 201 ms |
| Navi | 27.9 | 99.53% | 304 ms |
| SuperMoney | 14.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 281.0 |
| Person to Person | 269.6 |
| QR Payments | 72.2 |
| UPI Lite | 36.5 |
| UPI Autopay | 25.1 |

## Failure analysis
- INC-2026-15 — fraud / risk spike on FamApp (day 3 of 3); see RCA-2026-15.

## Recommendations
Stay on the open incident: keep recovery monitoring on FamApp and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D24-MON) and any meetings/emails on 28 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D24-MON, RPT-D23-DAILY, INC-2026-15, RCA-2026-15

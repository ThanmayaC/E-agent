---
id: RPT-D125-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-09T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 09 May 2026)

**Report ID:** RPT-D125-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 09 May 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 125 of 206)

## Transaction summary
The rail processed 640.1M UPI transactions on Saturday — a lighter Saturday — up 5.1M on the same day last week. Success landed at 99.62% and settlement at 99.88%, held back by live issues on AU Small Finance Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 640.1  (▼77.8 d/d, ▲5.1 w/w, ▼155.8 m/m)
- **Success Rate:** 99.62%  (▲0.03 d/d, ▼0.36 w/w, ▲0.49 m/m)
- **Settlement Success:** 99.88%  (▲0.18 d/d, ▲0.21 w/w, ▼0.07 m/m)
- **Technical Declines:** 0.34%  (▼0.01 d/d, ▼0.01 w/w, ▼0.21 m/m)
- **Business Declines:** 0.21%  (▼0.02 d/d, ▼0.02 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,288  (▼67 d/d, ▼90 w/w, ▼854 m/m)
- **Merchant Complaints:** 184  (▼35 d/d, ▼48 w/w, ▼50 m/m)
- **Fraud Alerts:** 842  (▼1 d/d, ▼24 w/w, ▼318 m/m)
- **Risk Score:** 23  (▼11 m/m)
- **Response Time:** 603 ms  (▼2 d/d, ▼8 w/w, ▼150 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 208.4 | 99.67% |
| HDFC Bank | 68.4 | 99.42% |
| Bank of Baroda | 49.3 | 99.26% |
| Union Bank of India | 43.2 | 99.63% |
| Axis Bank | 39.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 305.7 | 99.51% | 198 ms |
| Google Pay | 209.3 | 99.35% | 241 ms |
| Paytm | 50.8 | 99.53% | 201 ms |
| Navi | 23.5 | 99.53% | 304 ms |
| SuperMoney | 12.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 236.8 |
| Person to Person | 227.2 |
| QR Payments | 60.8 |
| UPI Lite | 30.7 |
| UPI Autopay | 21.1 |

## Failure analysis
- INC-2026-26 — merchant settlement delay on AU Small Finance Bank (day 2 of 4); see RCA-2026-26.

## Recommendations
Stay on the open incident: keep recovery monitoring on AU Small Finance Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D125-MON) and any meetings/emails on 09 May.

Refs: upi_kpis_month.xlsx, TEAMS-D125-MON, RPT-D124-DAILY, INC-2026-26, RCA-2026-26

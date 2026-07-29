---
id: RPT-D126-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-10T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 10 May 2026)

**Report ID:** RPT-D126-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 10 May 2026  ·  **Day archetype:** Sunday (quiet) · maintenance window
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 126 of 206)

## Transaction summary
The rail processed 586.7M UPI transactions on Sunday — a quiet Sunday with a scheduled maintenance window — up 2.0M on the same day last week. Success landed at 99.59% and settlement at 98.81%, held back by live issues on AU Small Finance Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 586.7  (▼53.4 d/d, ▲2.0 w/w, ▼209.2 m/m)
- **Success Rate:** 99.59%  (▼0.03 d/d, ▼0.39 w/w, ▲0.46 m/m)
- **Settlement Success:** 98.81%  (▼1.07 d/d, ▲0.11 w/w, ▼1.14 m/m)
- **Technical Declines:** 0.34%  (▼0.01 w/w, ▼0.21 m/m)
- **Business Declines:** 0.2%  (▼0.01 d/d, ▼0.01 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,230  (▼58 d/d, ▼74 w/w, ▼912 m/m)
- **Merchant Complaints:** 156  (▼28 d/d, ▼27 w/w, ▼78 m/m)
- **Fraud Alerts:** 843  (▲1 d/d, ▼7 w/w, ▼317 m/m)
- **Risk Score:** 23  (▼11 m/m)
- **Response Time:** 609 ms  (▲6 d/d, ▼8 w/w, ▼144 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 191.0 | 99.67% |
| HDFC Bank | 62.7 | 99.42% |
| Bank of Baroda | 45.2 | 99.26% |
| Union Bank of India | 39.6 | 99.63% |
| Axis Bank | 36.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 280.2 | 99.51% | 198 ms |
| Google Pay | 191.9 | 99.35% | 241 ms |
| Paytm | 46.5 | 99.53% | 201 ms |
| Navi | 21.6 | 99.53% | 304 ms |
| SuperMoney | 11.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 217.1 |
| Person to Person | 208.3 |
| QR Payments | 55.7 |
| UPI Lite | 28.2 |
| UPI Autopay | 19.4 |

## Failure analysis
- INC-2026-26 — merchant settlement delay on AU Small Finance Bank (day 3 of 4); see RCA-2026-26.

## Recommendations
Stay on the open incident: keep recovery monitoring on AU Small Finance Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D126-MON) and any meetings/emails on 10 May.

Refs: upi_kpis_month.xlsx, TEAMS-D126-MON, RPT-D125-DAILY, INC-2026-26, RCA-2026-26

---
id: RPT-D19-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-23T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 23 Jan 2026)

**Report ID:** RPT-D19-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 23 Jan 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 19 of 206)

## Transaction summary
The rail processed 655.7M UPI transactions on Friday — a steady mid-week day — down 7.3M on the same day last week. Success landed at 98.61% and settlement at 99.85%, held back by live issues on UPI Lite (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 655.7  (▼16.5 d/d, ▼7.3 w/w, ▼140.2 m/m)
- **Success Rate:** 98.61%  (▼0.1 d/d, ▼0.72 w/w, ▼0.52 m/m)
- **Settlement Success:** 99.85%  (▲0.39 d/d, ▼0.01 w/w, ▼0.1 m/m)
- **Technical Declines:** 0.67%  (▼0.09 d/d, ▲0.14 w/w, ▲0.12 m/m)
- **Business Declines:** 0.23%  (▼0.01 m/m)
- **Customer Complaints:** 2,345  (▼253 d/d, ▲320 w/w, ▲203 m/m)
- **Merchant Complaints:** 213  (▼1 d/d, ▼7 w/w, ▼21 m/m)
- **Fraud Alerts:** 1,091  (▼8 d/d, ▼33 w/w, ▼69 m/m)
- **Risk Score:** 32  (▼1 w/w, ▼2 m/m)
- **Response Time:** 763 ms  (▼24 d/d, ▲19 w/w, ▲10 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 213.4 | 99.67% |
| HDFC Bank | 70.1 | 99.42% |
| Bank of Baroda | 50.5 | 99.26% |
| Union Bank of India | 44.2 | 99.63% |
| Axis Bank | 40.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 313.2 | 99.51% | 198 ms |
| Google Pay | 214.4 | 99.35% | 241 ms |
| Paytm | 52.0 | 99.53% | 201 ms |
| Navi | 24.1 | 99.53% | 304 ms |
| SuperMoney | 12.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 242.6 |
| Person to Person | 232.8 |
| QR Payments | 62.3 |
| UPI Lite | 31.5 |
| UPI Autopay | 21.6 |

## Failure analysis
- INC-2026-24 — feature-level degradation on UPI Lite (day 2 of 3); see RCA-2026-24.

## Recommendations
Stay on the open incident: keep recovery monitoring on UPI Lite and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D19-MON) and any meetings/emails on 23 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D19-MON, RPT-D18-DAILY, INC-2026-24, RCA-2026-24

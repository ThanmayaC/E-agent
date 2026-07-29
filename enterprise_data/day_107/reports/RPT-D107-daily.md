---
id: RPT-D107-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-21T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 21 Apr 2026)

**Report ID:** RPT-D107-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 21 Apr 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 107 of 206)

## Transaction summary
The rail processed 701.3M UPI transactions on Tuesday — a steady mid-week day — down 9.5M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 701.3  (▲7.1 d/d, ▼9.5 w/w, ▼94.6 m/m)
- **Success Rate:** 99.98%  (▲0.66 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.23 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.37%  (▼0.18 m/m)
- **Business Declines:** 0.18%  (▼0.01 d/d, ▼0.01 w/w, ▼0.06 m/m)
- **Customer Complaints:** 1,310  (▼4 d/d, ▼42 w/w, ▼832 m/m)
- **Merchant Complaints:** 135  (▼2 d/d, ▼7 w/w, ▼99 m/m)
- **Fraud Alerts:** 886  (▲2 d/d, ▼12 w/w, ▼274 m/m)
- **Risk Score:** 24  (▼1 w/w, ▼10 m/m)
- **Response Time:** 625 ms  (▼3 w/w, ▼128 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 228.3 | 99.67% |
| HDFC Bank | 75.0 | 99.42% |
| Bank of Baroda | 54.0 | 99.26% |
| Union Bank of India | 47.3 | 99.63% |
| Axis Bank | 43.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 335.0 | 99.51% | 198 ms |
| Google Pay | 229.4 | 99.35% | 241 ms |
| Paytm | 55.6 | 99.53% | 201 ms |
| Navi | 25.8 | 99.53% | 304 ms |
| SuperMoney | 13.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 259.5 |
| Person to Person | 249.0 |
| QR Payments | 66.6 |
| UPI Lite | 33.7 |
| UPI Autopay | 23.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.37% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D107-MON) and any meetings/emails on 21 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D107-MON, RPT-D106-DAILY

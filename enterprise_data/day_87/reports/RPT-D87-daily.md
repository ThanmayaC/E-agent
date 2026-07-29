---
id: RPT-D87-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-01T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 01 Apr 2026)

**Report ID:** RPT-D87-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 01 Apr 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 87 of 206)

## Transaction summary
The rail processed 695.6M UPI transactions on Wednesday — a steady mid-week day — up 10.5M on the same day last week. Success held at 99.79% and settlement at 98.72%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 695.6  (▼91.9 d/d, ▲10.5 w/w, ▼100.3 m/m)
- **Success Rate:** 99.79%  (▲1.12 d/d, ▲0.23 w/w, ▲0.66 m/m)
- **Settlement Success:** 98.72%  (▼1.26 d/d, ▼0.22 w/w, ▼1.23 m/m)
- **Technical Declines:** 0.4%  (▲0.01 d/d, ▼0.2 w/w, ▼0.15 m/m)
- **Business Declines:** 0.19%  (▼0.01 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,441  (▲6 d/d, ▼475 w/w, ▼701 m/m)
- **Merchant Complaints:** 152  (▼3 w/w, ▼82 m/m)
- **Fraud Alerts:** 929  (▼10 d/d, ▼6 w/w, ▼231 m/m)
- **Risk Score:** 26  (▼1 w/w, ▼8 m/m)
- **Response Time:** 650 ms  (▼5 d/d, ▼52 w/w, ▼103 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 226.4 | 99.67% |
| HDFC Bank | 74.4 | 99.42% |
| Bank of Baroda | 53.5 | 99.26% |
| Union Bank of India | 46.9 | 99.63% |
| Axis Bank | 42.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 332.3 | 99.51% | 198 ms |
| Google Pay | 227.5 | 99.35% | 241 ms |
| Paytm | 55.2 | 99.53% | 201 ms |
| Navi | 25.6 | 99.53% | 304 ms |
| SuperMoney | 13.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 257.4 |
| Person to Person | 246.9 |
| QR Payments | 66.1 |
| UPI Lite | 33.4 |
| UPI Autopay | 23.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.4% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D87-MON) and any meetings/emails on 01 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D87-MON, RPT-D86-DAILY

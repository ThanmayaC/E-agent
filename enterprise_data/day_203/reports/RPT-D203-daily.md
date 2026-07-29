---
id: RPT-D203-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-26T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 26 Jul 2026)

**Report ID:** RPT-D203-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 26 Jul 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 203 of 206)

## Transaction summary
The rail processed 621.4M UPI transactions on Sunday — a quiet Sunday — up 5.0M on the same day last week. Success held at 99.28% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 621.4  (▼42.4 d/d, ▲5.0 w/w, ▼174.5 m/m)
- **Success Rate:** 99.28%  (▲0.09 d/d, ▲0.21 w/w, ▲0.15 m/m)
- **Settlement Success:** 99.98%  (▲0.27 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.25%  (▼0.01 w/w, ▼0.3 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 828  (▼9 d/d, ▼32 w/w, ▼1314 m/m)
- **Merchant Complaints:** 82  (▼1 d/d, ▼3 w/w, ▼152 m/m)
- **Fraud Alerts:** 698  (▲1 d/d, ▼5 w/w, ▼462 m/m)
- **Risk Score:** 18  (▼16 m/m)
- **Response Time:** 520 ms  (▼5 d/d, ▼7 w/w, ▼233 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 202.3 | 99.67% |
| HDFC Bank | 66.4 | 99.42% |
| Bank of Baroda | 47.8 | 99.26% |
| Union Bank of India | 41.9 | 99.63% |
| Axis Bank | 38.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 296.8 | 99.51% | 198 ms |
| Google Pay | 203.2 | 99.35% | 241 ms |
| Paytm | 49.3 | 99.53% | 201 ms |
| Navi | 22.8 | 99.53% | 304 ms |
| SuperMoney | 12.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 229.9 |
| Person to Person | 220.6 |
| QR Payments | 59.0 |
| UPI Lite | 29.8 |
| UPI Autopay | 20.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.25% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D203-MON) and any meetings/emails on 26 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D203-MON, RPT-D202-DAILY

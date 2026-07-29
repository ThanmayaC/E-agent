---
id: RPT-D03-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-07T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 07 Jan 2026)

**Report ID:** RPT-D03-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 07 Jan 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 3 of 206)

## Transaction summary
The rail processed 659.1M UPI transactions on Wednesday — a steady mid-week day — the first day in the window. Success held at 99.73% and settlement at 99.3%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 659.1  (▲7.3 d/d, ▼136.8 m/m)
- **Success Rate:** 99.73%  (▲0.01 d/d, ▲0.6 m/m)
- **Settlement Success:** 99.3%  (▼0.15 d/d, ▼0.65 m/m)
- **Technical Declines:** 0.55%
- **Business Declines:** 0.24%
- **Customer Complaints:** 2,126  (▲3 d/d, ▼16 m/m)
- **Merchant Complaints:** 235  (▲1 m/m)
- **Fraud Alerts:** 1,142  (▼7 d/d, ▼18 m/m)
- **Risk Score:** 34
- **Response Time:** 752 ms  (▼11 d/d, ▼1 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 214.5 | 99.67% |
| HDFC Bank | 70.5 | 99.42% |
| Bank of Baroda | 50.7 | 99.26% |
| Union Bank of India | 44.5 | 99.63% |
| Axis Bank | 40.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 314.8 | 99.51% | 198 ms |
| Google Pay | 215.5 | 99.35% | 241 ms |
| Paytm | 52.3 | 99.53% | 201 ms |
| Navi | 24.2 | 99.53% | 304 ms |
| SuperMoney | 12.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 243.9 |
| Person to Person | 234.0 |
| QR Payments | 62.6 |
| UPI Lite | 31.6 |
| UPI Autopay | 21.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.55% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D03-MON) and any meetings/emails on 07 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D03-MON, RPT-D02-DAILY

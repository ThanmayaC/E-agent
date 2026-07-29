---
id: RPT-D01-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-05T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 05 Jan 2026)

**Report ID:** RPT-D01-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 05 Jan 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 1 of 206)

## Transaction summary
The rail processed 795.9M UPI transactions on Monday — a campaign-driven high-volume day — the first day in the window. Success held at 99.13% and settlement at 99.95%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 795.9
- **Success Rate:** 99.13%
- **Settlement Success:** 99.95%
- **Technical Declines:** 0.55%
- **Business Declines:** 0.24%
- **Customer Complaints:** 2,142
- **Merchant Complaints:** 234
- **Fraud Alerts:** 1,160
- **Risk Score:** 34
- **Response Time:** 753 ms

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
- No incidents open. Technical declines are within the 0.55% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D01-MON) and any meetings/emails on 05 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D01-MON, ORG-OVERVIEW

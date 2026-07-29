---
id: RPT-D04-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-08T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 08 Jan 2026)

**Report ID:** RPT-D04-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 08 Jan 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 4 of 206)

## Transaction summary
The rail processed 643.1M UPI transactions on Thursday — a steady mid-week day — the first day in the window. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 643.1  (▼16.0 d/d, ▼152.8 m/m)
- **Success Rate:** 99.98%  (▲0.25 d/d, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.68 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.55%
- **Business Declines:** 0.24%
- **Customer Complaints:** 2,131  (▲5 d/d, ▼11 m/m)
- **Merchant Complaints:** 231  (▼4 d/d, ▼3 m/m)
- **Fraud Alerts:** 1,135  (▼7 d/d, ▼25 m/m)
- **Risk Score:** 34
- **Response Time:** 750 ms  (▼2 d/d, ▼3 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 209.3 | 99.67% |
| HDFC Bank | 68.8 | 99.42% |
| Bank of Baroda | 49.5 | 99.26% |
| Union Bank of India | 43.4 | 99.63% |
| Axis Bank | 39.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 307.2 | 99.51% | 198 ms |
| Google Pay | 210.3 | 99.35% | 241 ms |
| Paytm | 51.0 | 99.53% | 201 ms |
| Navi | 23.6 | 99.53% | 304 ms |
| SuperMoney | 12.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 237.9 |
| Person to Person | 228.3 |
| QR Payments | 61.1 |
| UPI Lite | 30.9 |
| UPI Autopay | 21.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.55% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D04-MON) and any meetings/emails on 08 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D04-MON, RPT-D03-DAILY

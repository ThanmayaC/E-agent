---
id: RPT-D43-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-16T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 16 Feb 2026)

**Report ID:** RPT-D43-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 16 Feb 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 43 of 206)

## Transaction summary
The rail processed 668.1M UPI transactions on Monday — the Monday ramp-up after the weekend — up 23.6M on the same day last week. Success held at 98.87% and settlement at 98.81%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 668.1  (▲113.9 d/d, ▲23.6 w/w, ▼127.8 m/m)
- **Success Rate:** 98.87%  (▲0.32 d/d, ▼0.08 w/w, ▼0.26 m/m)
- **Settlement Success:** 98.81%  (▼1.17 d/d, ▲0.1 w/w, ▼1.14 m/m)
- **Technical Declines:** 0.47%  (▼0.01 w/w, ▼0.08 m/m)
- **Business Declines:** 0.22%  (▼0.03 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,766  (▼12 d/d, ▼170 w/w, ▼376 m/m)
- **Merchant Complaints:** 190  (▼6 w/w, ▼44 m/m)
- **Fraud Alerts:** 1,034  (▼14 d/d, ▼100 w/w, ▼126 m/m)
- **Risk Score:** 30  (▼6 w/w, ▼4 m/m)
- **Response Time:** 707 ms  (▼2 d/d, ▼8 w/w, ▼46 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 217.5 | 99.67% |
| HDFC Bank | 71.4 | 99.42% |
| Bank of Baroda | 51.4 | 99.26% |
| Union Bank of India | 45.1 | 99.63% |
| Axis Bank | 41.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 319.1 | 99.51% | 198 ms |
| Google Pay | 218.5 | 99.35% | 241 ms |
| Paytm | 53.0 | 99.53% | 201 ms |
| Navi | 24.6 | 99.53% | 304 ms |
| SuperMoney | 13.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 247.2 |
| Person to Person | 237.2 |
| QR Payments | 63.5 |
| UPI Lite | 32.1 |
| UPI Autopay | 22.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.47% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D43-MON) and any meetings/emails on 16 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D43-MON, RPT-D42-DAILY

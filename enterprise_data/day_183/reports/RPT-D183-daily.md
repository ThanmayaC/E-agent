---
id: RPT-D183-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-06T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 06 Jul 2026)

**Report ID:** RPT-D183-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 06 Jul 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 183 of 206)

## Transaction summary
The rail processed 718.7M UPI transactions on Monday — the Monday ramp-up after the weekend — down 112.8M on the same day last week. Success held at 99.98% and settlement at 99.68%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 718.7  (▲98.0 d/d, ▼112.8 w/w, ▼77.2 m/m)
- **Success Rate:** 99.98%  (▲0.18 d/d, ▲0.43 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.68%  (▲0.05 d/d, ▲0.53 w/w, ▼0.27 m/m)
- **Technical Declines:** 0.28%  (▲0.01 d/d, ▼0.01 w/w, ▼0.27 m/m)
- **Business Declines:** 0.15%  (▼0.01 w/w, ▼0.09 m/m)
- **Customer Complaints:** 907  (▼5 d/d, ▼41 w/w, ▼1235 m/m)
- **Merchant Complaints:** 92  (▼2 w/w, ▼142 m/m)
- **Fraud Alerts:** 737  (▲6 d/d, ▼2 w/w, ▼423 m/m)
- **Risk Score:** 19  (▼15 m/m)
- **Response Time:** 538 ms  (▼10 d/d, ▼11 w/w, ▼215 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 233.9 | 99.67% |
| HDFC Bank | 76.8 | 99.42% |
| Bank of Baroda | 55.3 | 99.26% |
| Union Bank of India | 48.5 | 99.63% |
| Axis Bank | 44.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 343.3 | 99.51% | 198 ms |
| Google Pay | 235.0 | 99.35% | 241 ms |
| Paytm | 57.0 | 99.53% | 201 ms |
| Navi | 26.4 | 99.53% | 304 ms |
| SuperMoney | 14.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 265.9 |
| Person to Person | 255.1 |
| QR Payments | 68.3 |
| UPI Lite | 34.5 |
| UPI Autopay | 23.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.28% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D183-MON) and any meetings/emails on 06 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D183-MON, RPT-D182-DAILY

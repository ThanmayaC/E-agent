---
id: RPT-D135-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-19T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 19 May 2026)

**Report ID:** RPT-D135-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 19 May 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 135 of 206)

## Transaction summary
The rail processed 716.0M UPI transactions on Tuesday — a steady mid-week day — up 8.2M on the same day last week. Success held at 99.73% and settlement at 99.41%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 716.0  (▲22.5 d/d, ▲8.2 w/w, ▼79.9 m/m)
- **Success Rate:** 99.73%  (▲0.83 d/d, ▲0.1 w/w, ▲0.6 m/m)
- **Settlement Success:** 99.41%  (▲0.44 d/d, ▼0.57 w/w, ▼0.54 m/m)
- **Technical Declines:** 0.33%  (▼0.01 w/w, ▼0.22 m/m)
- **Business Declines:** 0.17%  (▼0.08 w/w, ▼0.07 m/m)
- **Customer Complaints:** 1,143  (▲1 d/d, ▼38 w/w, ▼999 m/m)
- **Merchant Complaints:** 117  (▼1 d/d, ▼78 w/w, ▼117 m/m)
- **Fraud Alerts:** 816  (▼14 d/d, ▼20 w/w, ▼344 m/m)
- **Risk Score:** 22  (▼1 w/w, ▼12 m/m)
- **Response Time:** 589 ms  (▼8 d/d, ▼16 w/w, ▼164 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 233.1 | 99.67% |
| HDFC Bank | 76.6 | 99.42% |
| Bank of Baroda | 55.1 | 99.26% |
| Union Bank of India | 48.3 | 99.63% |
| Axis Bank | 44.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 342.0 | 99.51% | 198 ms |
| Google Pay | 234.2 | 99.35% | 241 ms |
| Paytm | 56.8 | 99.53% | 201 ms |
| Navi | 26.3 | 99.53% | 304 ms |
| SuperMoney | 14.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 264.9 |
| Person to Person | 254.2 |
| QR Payments | 68.0 |
| UPI Lite | 34.4 |
| UPI Autopay | 23.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.33% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D135-MON) and any meetings/emails on 19 May.

Refs: upi_kpis_month.xlsx, TEAMS-D135-MON, RPT-D134-DAILY

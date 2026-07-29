---
id: RPT-D15-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-19T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 19 Jan 2026)

**Report ID:** RPT-D15-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 19 Jan 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 15 of 206)

## Transaction summary
The rail processed 643.2M UPI transactions on Monday — the Monday ramp-up after the weekend — down 1.1M on the same day last week. Success held at 98.78% and settlement at 99.48%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 643.2  (▲104.0 d/d, ▼1.1 w/w, ▼152.7 m/m)
- **Success Rate:** 98.78%  (▼0.25 d/d, ▼0.35 m/m)
- **Settlement Success:** 99.48%  (▼0.5 d/d, ▼0.5 w/w, ▼0.47 m/m)
- **Technical Declines:** 0.52%  (▼0.11 w/w, ▼0.03 m/m)
- **Business Declines:** 0.23%  (▼0.01 w/w, ▼0.01 m/m)
- **Customer Complaints:** 2,032  (▼9 d/d, ▼259 w/w, ▼110 m/m)
- **Merchant Complaints:** 220  (▼1 d/d, ▼48 w/w, ▼14 m/m)
- **Fraud Alerts:** 1,103  (▼2 d/d, ▼25 w/w, ▼57 m/m)
- **Risk Score:** 33  (▲1 d/d, ▼1 w/w, ▼1 m/m)
- **Response Time:** 741 ms  (▼6 d/d, ▼23 w/w, ▼12 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 209.4 | 99.67% |
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
| Person to Merchant | 238.0 |
| Person to Person | 228.3 |
| QR Payments | 61.1 |
| UPI Lite | 30.9 |
| UPI Autopay | 21.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.52% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D15-MON) and any meetings/emails on 19 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D15-MON, RPT-D14-DAILY

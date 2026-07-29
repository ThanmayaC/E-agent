---
id: RPT-D155-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-08T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 08 Jun 2026)

**Report ID:** RPT-D155-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 08 Jun 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 155 of 206)

## Transaction summary
The rail processed 699.9M UPI transactions on Monday — the Monday ramp-up after the weekend — down 0.2M on the same day last week. Success held at 99.78% and settlement at 99.51%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 699.9  (▲99.0 d/d, ▼0.2 w/w, ▼96.0 m/m)
- **Success Rate:** 99.78%  (▲0.67 d/d, ▲0.28 w/w, ▲0.65 m/m)
- **Settlement Success:** 99.51%  (▼0.22 d/d, ▼0.23 w/w, ▼0.44 m/m)
- **Technical Declines:** 0.3%  (▼0.02 w/w, ▼0.25 m/m)
- **Business Declines:** 0.16%  (▼0.05 w/w, ▼0.08 m/m)
- **Customer Complaints:** 1,036  (▼16 d/d, ▼61 w/w, ▼1106 m/m)
- **Merchant Complaints:** 106  (▲1 d/d, ▼46 w/w, ▼128 m/m)
- **Fraud Alerts:** 780  (▼8 d/d, ▼11 w/w, ▼380 m/m)
- **Risk Score:** 21  (▼13 m/m)
- **Response Time:** 573 ms  (▼1 d/d, ▼17 w/w, ▼180 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 227.8 | 99.67% |
| HDFC Bank | 74.8 | 99.42% |
| Bank of Baroda | 53.9 | 99.26% |
| Union Bank of India | 47.2 | 99.63% |
| Axis Bank | 43.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 334.3 | 99.51% | 198 ms |
| Google Pay | 228.9 | 99.35% | 241 ms |
| Paytm | 55.5 | 99.53% | 201 ms |
| Navi | 25.7 | 99.53% | 304 ms |
| SuperMoney | 13.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 259.0 |
| Person to Person | 248.5 |
| QR Payments | 66.5 |
| UPI Lite | 33.6 |
| UPI Autopay | 23.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D155-MON) and any meetings/emails on 08 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D155-MON, RPT-D154-DAILY

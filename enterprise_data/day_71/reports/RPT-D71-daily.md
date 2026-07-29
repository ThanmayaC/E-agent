---
id: RPT-D71-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-16T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 16 Mar 2026)

**Report ID:** RPT-D71-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 16 Mar 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 71 of 206)

## Transaction summary
The rail processed 680.8M UPI transactions on Monday — the Monday ramp-up after the weekend — down 167.9M on the same day last week. Success held at 99.41% and settlement at 99.37%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 680.8  (▲115.4 d/d, ▼167.9 w/w, ▼115.1 m/m)
- **Success Rate:** 99.41%  (▲0.91 d/d, ▼0.39 w/w, ▲0.28 m/m)
- **Settlement Success:** 99.37%  (▼0.61 d/d, ▲0.61 w/w, ▼0.58 m/m)
- **Technical Declines:** 0.42%  (▼0.01 w/w, ▼0.13 m/m)
- **Business Declines:** 0.2%  (▼0.04 m/m)
- **Customer Complaints:** 1,554  (▲7 d/d, ▼35 w/w, ▼588 m/m)
- **Merchant Complaints:** 163  (▼1 d/d, ▼5 w/w, ▼71 m/m)
- **Fraud Alerts:** 962  (▼9 d/d, ▼20 w/w, ▼198 m/m)
- **Risk Score:** 27  (▼1 w/w, ▼7 m/m)
- **Response Time:** 665 ms  (▼8 d/d, ▼16 w/w, ▼88 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 221.6 | 99.67% |
| HDFC Bank | 72.8 | 99.42% |
| Bank of Baroda | 52.4 | 99.26% |
| Union Bank of India | 45.9 | 99.63% |
| Axis Bank | 41.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 325.2 | 99.51% | 198 ms |
| Google Pay | 222.6 | 99.35% | 241 ms |
| Paytm | 54.0 | 99.53% | 201 ms |
| Navi | 25.0 | 99.53% | 304 ms |
| SuperMoney | 13.3 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 251.9 |
| Person to Person | 241.7 |
| QR Payments | 64.7 |
| UPI Lite | 32.7 |
| UPI Autopay | 22.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.42% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D71-MON) and any meetings/emails on 16 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D71-MON, RPT-D70-DAILY

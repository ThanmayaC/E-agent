---
id: RPT-D159-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-12T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 12 Jun 2026)

**Report ID:** RPT-D159-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 12 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 159 of 206)

## Transaction summary
The rail processed 739.4M UPI transactions on Friday — a steady mid-week day — up 6.3M on the same day last week. Success held at 99.25% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 739.4  (▲3.3 d/d, ▲6.3 w/w, ▼56.5 m/m)
- **Success Rate:** 99.25%  (▼0.58 d/d, ▲0.39 w/w, ▲0.12 m/m)
- **Settlement Success:** 99.98%  (▲0.01 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.3%  (▼0.21 w/w, ▼0.25 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 1,021  (▲4 d/d, ▼501 w/w, ▼1121 m/m)
- **Merchant Complaints:** 103  (▼1 d/d, ▼79 w/w, ▼131 m/m)
- **Fraud Alerts:** 769  (▼4 d/d, ▼13 w/w, ▼391 m/m)
- **Risk Score:** 21  (▼13 m/m)
- **Response Time:** 565 ms  (▼6 d/d, ▼70 w/w, ▼188 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 240.7 | 99.67% |
| HDFC Bank | 79.1 | 99.42% |
| Bank of Baroda | 56.9 | 99.26% |
| Union Bank of India | 49.9 | 99.63% |
| Axis Bank | 45.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 353.2 | 99.51% | 198 ms |
| Google Pay | 241.8 | 99.35% | 241 ms |
| Paytm | 58.7 | 99.53% | 201 ms |
| Navi | 27.2 | 99.53% | 304 ms |
| SuperMoney | 14.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 273.6 |
| Person to Person | 262.5 |
| QR Payments | 70.2 |
| UPI Lite | 35.5 |
| UPI Autopay | 24.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D159-MON) and any meetings/emails on 12 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D159-MON, RPT-D158-DAILY

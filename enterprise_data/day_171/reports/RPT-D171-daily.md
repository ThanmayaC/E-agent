---
id: RPT-D171-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-24T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 24 Jun 2026)

**Report ID:** RPT-D171-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 24 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 171 of 206)

## Transaction summary
The rail processed 726.3M UPI transactions on Wednesday — a steady mid-week day — down 25.1M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 726.3  (▼17.4 d/d, ▼25.1 w/w, ▼69.6 m/m)
- **Success Rate:** 99.98%  (▲1.03 d/d, ▲0.62 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.22 d/d, ▲0.28 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.29%  (▼0.01 w/w, ▼0.26 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 970  (▼26 w/w, ▼1172 m/m)
- **Merchant Complaints:** 98  (▼3 w/w, ▼136 m/m)
- **Fraud Alerts:** 747  (▼10 d/d, ▼21 w/w, ▼413 m/m)
- **Risk Score:** 20  (▼14 m/m)
- **Response Time:** 558 ms  (▲3 d/d, ▲1 w/w, ▼195 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 236.4 | 99.67% |
| HDFC Bank | 77.7 | 99.42% |
| Bank of Baroda | 55.9 | 99.26% |
| Union Bank of India | 49.0 | 99.63% |
| Axis Bank | 44.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 346.9 | 99.51% | 198 ms |
| Google Pay | 237.5 | 99.35% | 241 ms |
| Paytm | 57.6 | 99.53% | 201 ms |
| Navi | 26.7 | 99.53% | 304 ms |
| SuperMoney | 14.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 268.7 |
| Person to Person | 257.8 |
| QR Payments | 69.0 |
| UPI Lite | 34.9 |
| UPI Autopay | 24.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.29% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D171-MON) and any meetings/emails on 24 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D171-MON, RPT-D170-DAILY

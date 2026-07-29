---
id: RPT-D199-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-22T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 22 Jul 2026)

**Report ID:** RPT-D199-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 22 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 199 of 206)

## Transaction summary
The rail processed 756.4M UPI transactions on Wednesday — a steady mid-week day — down 6.0M on the same day last week. Success held at 99.98% and settlement at 99.2%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 756.4  (▼12.3 d/d, ▼6.0 w/w, ▼39.5 m/m)
- **Success Rate:** 99.98%  (▲0.58 d/d, ▲0.44 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.2%  (▼0.78 d/d, ▼0.78 w/w, ▼0.75 m/m)
- **Technical Declines:** 0.26%  (▼0.01 w/w, ▼0.29 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 848  (▲2 d/d, ▼26 w/w, ▼1294 m/m)
- **Merchant Complaints:** 84  (▼1 d/d, ▼4 w/w, ▼150 m/m)
- **Fraud Alerts:** 703  (▲5 d/d, ▼6 w/w, ▼457 m/m)
- **Risk Score:** 18  (▼1 w/w, ▼16 m/m)
- **Response Time:** 529 ms  (▲2 d/d, ▼1 w/w, ▼224 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 246.2 | 99.67% |
| HDFC Bank | 80.9 | 99.42% |
| Bank of Baroda | 58.2 | 99.26% |
| Union Bank of India | 51.0 | 99.63% |
| Axis Bank | 46.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 361.3 | 99.51% | 198 ms |
| Google Pay | 247.4 | 99.35% | 241 ms |
| Paytm | 60.0 | 99.53% | 201 ms |
| Navi | 27.8 | 99.53% | 304 ms |
| SuperMoney | 14.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 279.9 |
| Person to Person | 268.5 |
| QR Payments | 71.9 |
| UPI Lite | 36.3 |
| UPI Autopay | 25.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.26% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D199-MON) and any meetings/emails on 22 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D199-MON, RPT-D198-DAILY

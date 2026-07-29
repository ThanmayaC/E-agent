---
id: RPT-D195-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-18T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 18 Jul 2026)

**Report ID:** RPT-D195-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 18 Jul 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 195 of 206)

## Transaction summary
The rail processed 674.1M UPI transactions on Saturday — a lighter Saturday — up 14.1M on the same day last week. Success held at 99.98% and settlement at 99.75%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 674.1  (▼87.0 d/d, ▲14.1 w/w, ▼121.8 m/m)
- **Success Rate:** 99.98%  (▲0.06 d/d, ▲0.85 m/m)
- **Settlement Success:** 99.75%  (▼0.18 d/d, ▼0.23 w/w, ▼0.2 m/m)
- **Technical Declines:** 0.27%  (▲0.01 d/d, ▼0.01 w/w, ▼0.28 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 863  (▼4 d/d, ▼49 w/w, ▼1279 m/m)
- **Merchant Complaints:** 87  (▼2 w/w, ▼147 m/m)
- **Fraud Alerts:** 704  (▼9 d/d, ▼23 w/w, ▼456 m/m)
- **Risk Score:** 18  (▼1 d/d, ▼1 w/w, ▼16 m/m)
- **Response Time:** 528 ms  (▼8 d/d, ▼10 w/w, ▼225 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 219.4 | 99.67% |
| HDFC Bank | 72.1 | 99.42% |
| Bank of Baroda | 51.9 | 99.26% |
| Union Bank of India | 45.5 | 99.63% |
| Axis Bank | 41.5 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 322.0 | 99.51% | 198 ms |
| Google Pay | 220.5 | 99.35% | 241 ms |
| Paytm | 53.5 | 99.53% | 201 ms |
| Navi | 24.8 | 99.53% | 304 ms |
| SuperMoney | 13.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 249.4 |
| Person to Person | 239.3 |
| QR Payments | 64.0 |
| UPI Lite | 32.4 |
| UPI Autopay | 22.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.27% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D195-MON) and any meetings/emails on 18 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D195-MON, RPT-D194-DAILY

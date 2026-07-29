---
id: RPT-D181-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-04T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 04 Jul 2026)

**Report ID:** RPT-D181-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 04 Jul 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 181 of 206)

## Transaction summary
The rail processed 673.2M UPI transactions on Saturday — a lighter Saturday — up 12.5M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 673.2  (▼73.5 d/d, ▲12.5 w/w, ▼122.7 m/m)
- **Success Rate:** 99.98%  (▲1.02 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.31 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.28%  (▼0.27 m/m)
- **Business Declines:** 0.15%  (▼0.01 w/w, ▼0.09 m/m)
- **Customer Complaints:** 919  (▼2 d/d, ▼23 w/w, ▼1223 m/m)
- **Merchant Complaints:** 92  (▼2 d/d, ▼3 w/w, ▼142 m/m)
- **Fraud Alerts:** 734  (▼3 d/d, ▼6 w/w, ▼426 m/m)
- **Risk Score:** 19  (▼1 w/w, ▼15 m/m)
- **Response Time:** 540 ms  (▼8 d/d, ▼11 w/w, ▼213 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 219.1 | 99.67% |
| HDFC Bank | 72.0 | 99.42% |
| Bank of Baroda | 51.8 | 99.26% |
| Union Bank of India | 45.4 | 99.63% |
| Axis Bank | 41.5 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 321.6 | 99.51% | 198 ms |
| Google Pay | 220.2 | 99.35% | 241 ms |
| Paytm | 53.4 | 99.53% | 201 ms |
| Navi | 24.8 | 99.53% | 304 ms |
| SuperMoney | 13.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 249.1 |
| Person to Person | 239.0 |
| QR Payments | 64.0 |
| UPI Lite | 32.3 |
| UPI Autopay | 22.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.28% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D181-MON) and any meetings/emails on 04 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D181-MON, RPT-D180-DAILY

---
id: RPT-D47-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-20T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 20 Feb 2026)

**Report ID:** RPT-D47-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 20 Feb 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 47 of 206)

## Transaction summary
The rail processed 688.4M UPI transactions on Friday — a steady mid-week day — up 20.9M on the same day last week. Success held at 99.54% and settlement at 99.06%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 688.4  (▲21.7 d/d, ▲20.9 w/w, ▼107.5 m/m)
- **Success Rate:** 99.54%  (▲0.39 d/d, ▼0.44 w/w, ▲0.41 m/m)
- **Settlement Success:** 99.06%  (▼0.92 d/d, ▼0.92 w/w, ▼0.89 m/m)
- **Technical Declines:** 0.46%  (▼0.01 w/w, ▼0.09 m/m)
- **Business Declines:** 0.21%  (▼0.01 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,721  (▼8 d/d, ▼80 w/w, ▼421 m/m)
- **Merchant Complaints:** 187  (▲1 d/d, ▼7 w/w, ▼47 m/m)
- **Fraud Alerts:** 1,028  (▲8 d/d, ▼20 w/w, ▼132 m/m)
- **Risk Score:** 29  (▼1 d/d, ▼1 w/w, ▼5 m/m)
- **Response Time:** 696 ms  (▲2 d/d, ▼5 w/w, ▼57 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 224.1 | 99.67% |
| HDFC Bank | 73.6 | 99.42% |
| Bank of Baroda | 53.0 | 99.26% |
| Union Bank of India | 46.4 | 99.63% |
| Axis Bank | 42.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 328.8 | 99.51% | 198 ms |
| Google Pay | 225.1 | 99.35% | 241 ms |
| Paytm | 54.6 | 99.53% | 201 ms |
| Navi | 25.3 | 99.53% | 304 ms |
| SuperMoney | 13.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 254.7 |
| Person to Person | 244.4 |
| QR Payments | 65.4 |
| UPI Lite | 33.0 |
| UPI Autopay | 22.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.46% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D47-MON) and any meetings/emails on 20 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D47-MON, RPT-D46-DAILY

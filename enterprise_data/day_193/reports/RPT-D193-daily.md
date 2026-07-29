---
id: RPT-D193-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-16T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 16 Jul 2026)

**Report ID:** RPT-D193-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 16 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 193 of 206)

## Transaction summary
The rail processed 746.7M UPI transactions on Thursday — a steady mid-week day — down 157.1M on the same day last week. Success held at 99.55% and settlement at 99.53%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 746.7  (▼15.7 d/d, ▼157.1 w/w, ▼49.2 m/m)
- **Success Rate:** 99.55%  (▲0.01 d/d, ▼0.43 w/w, ▲0.42 m/m)
- **Settlement Success:** 99.53%  (▼0.45 d/d, ▲0.19 w/w, ▼0.42 m/m)
- **Technical Declines:** 0.26%  (▼0.01 d/d, ▼0.05 w/w, ▼0.29 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 865  (▼9 d/d, ▼134 w/w, ▼1277 m/m)
- **Merchant Complaints:** 87  (▼1 d/d, ▼3 w/w, ▼147 m/m)
- **Fraud Alerts:** 717  (▲8 d/d, ▼5 w/w, ▼443 m/m)
- **Risk Score:** 19  (▼15 m/m)
- **Response Time:** 537 ms  (▲7 d/d, ▼14 w/w, ▼216 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 243.1 | 99.67% |
| HDFC Bank | 79.8 | 99.42% |
| Bank of Baroda | 57.5 | 99.26% |
| Union Bank of India | 50.4 | 99.63% |
| Axis Bank | 46.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 356.7 | 99.51% | 198 ms |
| Google Pay | 244.2 | 99.35% | 241 ms |
| Paytm | 59.2 | 99.53% | 201 ms |
| Navi | 27.5 | 99.53% | 304 ms |
| SuperMoney | 14.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 276.3 |
| Person to Person | 265.1 |
| QR Payments | 70.9 |
| UPI Lite | 35.8 |
| UPI Autopay | 24.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.26% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D193-MON) and any meetings/emails on 16 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D193-MON, RPT-D192-DAILY

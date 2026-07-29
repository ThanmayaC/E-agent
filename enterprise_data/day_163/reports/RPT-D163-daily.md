---
id: RPT-D163-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-16T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 16 Jun 2026)

**Report ID:** RPT-D163-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 16 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 163 of 206)

## Transaction summary
The rail processed 721.5M UPI transactions on Tuesday — a steady mid-week day — down 13.7M on the same day last week. Success held at 99.27% and settlement at 99.0%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 721.5  (▼7.7 d/d, ▼13.7 w/w, ▼74.4 m/m)
- **Success Rate:** 99.27%  (▼0.01 d/d, ▼0.71 w/w, ▲0.14 m/m)
- **Settlement Success:** 99.0%  (▼0.98 d/d, ▼0.95 w/w, ▼0.95 m/m)
- **Technical Declines:** 0.3%  (▼0.01 w/w, ▼0.25 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 999  (▼9 d/d, ▼40 w/w, ▼1143 m/m)
- **Merchant Complaints:** 102  (▼3 w/w, ▼132 m/m)
- **Fraud Alerts:** 762  (▼9 d/d, ▼18 w/w, ▼398 m/m)
- **Risk Score:** 21  (▲1 d/d, ▼13 m/m)
- **Response Time:** 564 ms  (▼3 d/d, ▼12 w/w, ▼189 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 234.8 | 99.67% |
| HDFC Bank | 77.1 | 99.42% |
| Bank of Baroda | 55.5 | 99.26% |
| Union Bank of India | 48.7 | 99.63% |
| Axis Bank | 44.5 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 344.6 | 99.51% | 198 ms |
| Google Pay | 236.0 | 99.35% | 241 ms |
| Paytm | 57.2 | 99.53% | 201 ms |
| Navi | 26.5 | 99.53% | 304 ms |
| SuperMoney | 14.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 267.0 |
| Person to Person | 256.1 |
| QR Payments | 68.5 |
| UPI Lite | 34.6 |
| UPI Autopay | 23.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D163-MON) and any meetings/emails on 16 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D163-MON, RPT-D162-DAILY

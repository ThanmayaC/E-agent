---
id: RPT-D191-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-14T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 14 Jul 2026)

**Report ID:** RPT-D191-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 14 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 191 of 206)

## Transaction summary
The rail processed 743.6M UPI transactions on Tuesday — a steady mid-week day — down 13.0M on the same day last week. Success held at 99.19% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 743.6  (▲17.2 d/d, ▼13.0 w/w, ▼52.3 m/m)
- **Success Rate:** 99.19%  (▼0.36 d/d, ▲0.15 w/w, ▲0.06 m/m)
- **Settlement Success:** 99.98%  (▲0.3 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.27%  (▼0.14 w/w, ▼0.28 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 874  (▼307 w/w, ▼1268 m/m)
- **Merchant Complaints:** 87  (▼4 w/w, ▼147 m/m)
- **Fraud Alerts:** 713  (▼12 d/d, ▼12 w/w, ▼447 m/m)
- **Risk Score:** 19  (▼15 m/m)
- **Response Time:** 539 ms  (▲3 d/d, ▼45 w/w, ▼214 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 242.0 | 99.67% |
| HDFC Bank | 79.5 | 99.42% |
| Bank of Baroda | 57.2 | 99.26% |
| Union Bank of India | 50.2 | 99.63% |
| Axis Bank | 45.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 355.2 | 99.51% | 198 ms |
| Google Pay | 243.2 | 99.35% | 241 ms |
| Paytm | 59.0 | 99.53% | 201 ms |
| Navi | 27.3 | 99.53% | 304 ms |
| SuperMoney | 14.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 275.1 |
| Person to Person | 264.0 |
| QR Payments | 70.6 |
| UPI Lite | 35.7 |
| UPI Autopay | 24.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.27% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D191-MON) and any meetings/emails on 14 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D191-MON, RPT-D190-DAILY

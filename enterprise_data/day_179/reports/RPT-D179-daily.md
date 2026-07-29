---
id: RPT-D179-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-02T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 02 Jul 2026)

**Report ID:** RPT-D179-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 02 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 179 of 206)

## Transaction summary
The rail processed 729.9M UPI transactions on Thursday — a steady mid-week day — down 162.4M on the same day last week. Success held at 99.44% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 729.9  (▼22.6 d/d, ▼162.4 w/w, ▼66.0 m/m)
- **Success Rate:** 99.44%  (▼0.05 d/d, ▲0.55 w/w, ▲0.31 m/m)
- **Settlement Success:** 99.98%  (▲0.99 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.28%  (▼0.01 w/w, ▼0.27 m/m)
- **Business Declines:** 0.15%  (▼0.01 d/d, ▼0.01 w/w, ▼0.09 m/m)
- **Customer Complaints:** 933  (▲7 d/d, ▼20 w/w, ▼1209 m/m)
- **Merchant Complaints:** 94  (▼1 d/d, ▼3 w/w, ▼140 m/m)
- **Fraud Alerts:** 734  (▲1 d/d, ▼22 w/w, ▼426 m/m)
- **Risk Score:** 19  (▼1 w/w, ▼15 m/m)
- **Response Time:** 544 ms  (▼12 w/w, ▼209 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 237.6 | 99.67% |
| HDFC Bank | 78.0 | 99.42% |
| Bank of Baroda | 56.2 | 99.26% |
| Union Bank of India | 49.2 | 99.63% |
| Axis Bank | 45.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 348.6 | 99.51% | 198 ms |
| Google Pay | 238.7 | 99.35% | 241 ms |
| Paytm | 57.9 | 99.53% | 201 ms |
| Navi | 26.8 | 99.53% | 304 ms |
| SuperMoney | 14.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 270.1 |
| Person to Person | 259.1 |
| QR Payments | 69.3 |
| UPI Lite | 35.0 |
| UPI Autopay | 24.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.28% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D179-MON) and any meetings/emails on 02 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D179-MON, RPT-D178-DAILY

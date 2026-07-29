---
id: RPT-D25-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-29T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 29 Jan 2026)

**Report ID:** RPT-D25-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 29 Jan 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 25 of 206)

## Transaction summary
The rail processed 744.4M UPI transactions on Thursday — the month-end surge as salary and bill-pay flows land — up 72.2M on the same day last week. Success held at 99.93% and settlement at 99.86%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 744.4  (▼15.1 d/d, ▲72.2 w/w, ▼51.5 m/m)
- **Success Rate:** 99.93%  (▲0.38 d/d, ▲1.22 w/w, ▲0.8 m/m)
- **Settlement Success:** 99.86%  (▲0.17 d/d, ▲0.4 w/w, ▼0.09 m/m)
- **Technical Declines:** 0.5%  (▼0.01 d/d, ▼0.26 w/w, ▼0.05 m/m)
- **Business Declines:** 0.23%  (▼0.06 d/d, ▼0.01 m/m)
- **Customer Complaints:** 1,904  (▼266 d/d, ▼694 w/w, ▼238 m/m)
- **Merchant Complaints:** 209  (▼1 d/d, ▼5 w/w, ▼25 m/m)
- **Fraud Alerts:** 1,073  (▼146 d/d, ▼26 w/w, ▼87 m/m)
- **Risk Score:** 32  (▼9 d/d, ▼2 m/m)
- **Response Time:** 721 ms  (▼7 d/d, ▼66 w/w, ▼32 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 242.3 | 99.67% |
| HDFC Bank | 79.6 | 99.42% |
| Bank of Baroda | 57.3 | 99.26% |
| Union Bank of India | 50.2 | 99.63% |
| Axis Bank | 45.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 355.6 | 99.51% | 198 ms |
| Google Pay | 243.4 | 99.35% | 241 ms |
| Paytm | 59.0 | 99.53% | 201 ms |
| Navi | 27.4 | 99.53% | 304 ms |
| SuperMoney | 14.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 275.4 |
| Person to Person | 264.3 |
| QR Payments | 70.7 |
| UPI Lite | 35.7 |
| UPI Autopay | 24.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.5% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D25-MON) and any meetings/emails on 29 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D25-MON, RPT-D24-DAILY

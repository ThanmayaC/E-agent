---
id: RPT-D27-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-31T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 31 Jan 2026)

**Report ID:** RPT-D27-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 31 Jan 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 27 of 206)

## Transaction summary
The rail processed 755.1M UPI transactions on Saturday — the month-end surge as salary and bill-pay flows land — up 168.3M on the same day last week. Success held at 99.62% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 755.1  (▲15.3 d/d, ▲168.3 w/w, ▼40.8 m/m)
- **Success Rate:** 99.62%  (▼0.14 d/d, ▲1.1 w/w, ▲0.49 m/m)
- **Settlement Success:** 99.98%  (▲0.02 d/d, ▲0.31 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.5%  (▼0.09 w/w, ▼0.05 m/m)
- **Business Declines:** 0.23%  (▼0.01 m/m)
- **Customer Complaints:** 1,885  (▼42 d/d, ▼281 w/w, ▼257 m/m)
- **Merchant Complaints:** 204  (▼1 d/d, ▼9 w/w, ▼30 m/m)
- **Fraud Alerts:** 1,085  (▼1 d/d, ▼16 w/w, ▼75 m/m)
- **Risk Score:** 31  (▼1 d/d, ▼1 w/w, ▼3 m/m)
- **Response Time:** 721 ms  (▼2 d/d, ▼37 w/w, ▼32 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 245.8 | 99.67% |
| HDFC Bank | 80.7 | 99.42% |
| Bank of Baroda | 58.1 | 99.26% |
| Union Bank of India | 50.9 | 99.63% |
| Axis Bank | 46.5 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 360.7 | 99.51% | 198 ms |
| Google Pay | 246.9 | 99.35% | 241 ms |
| Paytm | 59.9 | 99.53% | 201 ms |
| Navi | 27.8 | 99.53% | 304 ms |
| SuperMoney | 14.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 279.4 |
| Person to Person | 268.1 |
| QR Payments | 71.7 |
| UPI Lite | 36.2 |
| UPI Autopay | 24.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.5% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D27-MON) and any meetings/emails on 31 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D27-MON, RPT-D26-DAILY

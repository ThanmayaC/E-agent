---
id: RPT-D75-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-20T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 20 Mar 2026)

**Report ID:** RPT-D75-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 20 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 75 of 206)

## Transaction summary
The rail processed 698.4M UPI transactions on Friday — a steady mid-week day — up 14.0M on the same day last week. Success held at 99.95% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 698.4  (▲1.3 d/d, ▲14.0 w/w, ▼97.5 m/m)
- **Success Rate:** 99.95%  (▲0.32 d/d, ▼0.02 w/w, ▲0.82 m/m)
- **Settlement Success:** 99.98%  (▲1.16 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.41%  (▼0.02 w/w, ▼0.14 m/m)
- **Business Declines:** 0.2%  (▼0.04 m/m)
- **Customer Complaints:** 1,531  (▲16 d/d, ▼29 w/w, ▼611 m/m)
- **Merchant Complaints:** 161  (▼4 w/w, ▼73 m/m)
- **Fraud Alerts:** 948  (▼14 d/d, ▼16 w/w, ▼212 m/m)
- **Risk Score:** 27  (▼1 w/w, ▼7 m/m)
- **Response Time:** 668 ms  (▲10 d/d, ▲3 w/w, ▼85 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 227.3 | 99.67% |
| HDFC Bank | 74.7 | 99.42% |
| Bank of Baroda | 53.7 | 99.26% |
| Union Bank of India | 47.1 | 99.63% |
| Axis Bank | 43.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 333.6 | 99.51% | 198 ms |
| Google Pay | 228.4 | 99.35% | 241 ms |
| Paytm | 55.4 | 99.53% | 201 ms |
| Navi | 25.7 | 99.53% | 304 ms |
| SuperMoney | 13.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 258.4 |
| Person to Person | 247.9 |
| QR Payments | 66.3 |
| UPI Lite | 33.5 |
| UPI Autopay | 23.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.41% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D75-MON) and any meetings/emails on 20 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D75-MON, RPT-D74-DAILY

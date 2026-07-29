---
id: RPT-D63-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-08T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 08 Mar 2026)

**Report ID:** RPT-D63-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 08 Mar 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 63 of 206)

## Transaction summary
The rail processed 567.2M UPI transactions on Sunday — a quiet Sunday — up 0.2M on the same day last week. Success held at 98.57% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 567.2  (▼59.3 d/d, ▲0.2 w/w, ▼228.7 m/m)
- **Success Rate:** 98.57%  (▼1.32 d/d, ▲0.17 w/w, ▼0.56 m/m)
- **Settlement Success:** 99.98%  (▲1.71 d/d, ▲1.19 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.43%  (▼0.02 w/w, ▼0.12 m/m)
- **Business Declines:** 0.2%  (▼0.04 d/d, ▼0.07 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,620  (▼124 d/d, ▼258 w/w, ▼522 m/m)
- **Merchant Complaints:** 169  (▼84 d/d, ▼9 w/w, ▼65 m/m)
- **Fraud Alerts:** 979  (▼12 d/d, ▼152 w/w, ▼181 m/m)
- **Risk Score:** 28  (▼10 w/w, ▼6 m/m)
- **Response Time:** 681 ms  (▲7 d/d, ▼2 w/w, ▼72 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 184.6 | 99.67% |
| HDFC Bank | 60.6 | 99.42% |
| Bank of Baroda | 43.7 | 99.26% |
| Union Bank of India | 38.3 | 99.63% |
| Axis Bank | 34.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 270.9 | 99.51% | 198 ms |
| Google Pay | 185.5 | 99.35% | 241 ms |
| Paytm | 45.0 | 99.53% | 201 ms |
| Navi | 20.9 | 99.53% | 304 ms |
| SuperMoney | 11.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 209.9 |
| Person to Person | 201.4 |
| QR Payments | 53.9 |
| UPI Lite | 27.2 |
| UPI Autopay | 18.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.43% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D63-MON) and any meetings/emails on 08 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D63-MON, RPT-D62-DAILY

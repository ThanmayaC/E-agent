---
id: RPT-D67-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-12T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 12 Mar 2026)

**Report ID:** RPT-D67-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 12 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 67 of 206)

## Transaction summary
The rail processed 671.9M UPI transactions on Thursday — a steady mid-week day — down 21.6M on the same day last week. Success held at 98.9% and settlement at 98.84%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 671.9  (▼155.9 d/d, ▼21.6 w/w, ▼124.0 m/m)
- **Success Rate:** 98.9%  (▲0.31 d/d, ▲0.65 w/w, ▼0.23 m/m)
- **Settlement Success:** 98.84%  (▼0.17 d/d, ▼1.14 w/w, ▼1.11 m/m)
- **Technical Declines:** 0.43%  (▼0.01 w/w, ▼0.12 m/m)
- **Business Declines:** 0.2%  (▼0.11 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,575  (▲3 d/d, ▼392 w/w, ▼567 m/m)
- **Merchant Complaints:** 166  (▼1 d/d, ▼6 w/w, ▼68 m/m)
- **Fraud Alerts:** 972  (▼9 d/d, ▼241 w/w, ▼188 m/m)
- **Risk Score:** 28  (▼15 w/w, ▼6 m/m)
- **Response Time:** 669 ms  (▼9 d/d, ▼18 w/w, ▼84 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 218.7 | 99.67% |
| HDFC Bank | 71.8 | 99.42% |
| Bank of Baroda | 51.7 | 99.26% |
| Union Bank of India | 45.3 | 99.63% |
| Axis Bank | 41.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 320.9 | 99.51% | 198 ms |
| Google Pay | 219.7 | 99.35% | 241 ms |
| Paytm | 53.3 | 99.53% | 201 ms |
| Navi | 24.7 | 99.53% | 304 ms |
| SuperMoney | 13.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 248.6 |
| Person to Person | 238.5 |
| QR Payments | 63.8 |
| UPI Lite | 32.3 |
| UPI Autopay | 22.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.43% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D67-MON) and any meetings/emails on 12 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D67-MON, RPT-D66-DAILY

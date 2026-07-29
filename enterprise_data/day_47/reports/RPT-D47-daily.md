---
id: RPT-D47-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-07T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 07 Aug 2026)

**Report ID:** RPT-D47-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 07 Aug 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 47 of 180)

## Transaction summary
The rail processed 806.9M UPI transactions on Friday — a steady mid-week day — down 86.4M on the same day last week. Success held at 98.68% and settlement at 99.9%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 806.9  (▼20.7 d/d, ▼86.4 w/w, ▲62.0 m/m)
- **Success Rate:** 98.68%  (▲0.05 d/d, ▼1.3 w/w, ▼0.92 m/m)
- **Settlement Success:** 99.9%  (▲0.13 d/d, ▼0.08 w/w, ▲0.47 m/m)
- **Technical Declines:** 0.37%  (▼0.01 d/d, ▼0.02 w/w, ▼0.08 m/m)
- **Business Declines:** 0.18%  (▼0.02 m/m)
- **Customer Complaints:** 1,578  (▲7 d/d, ▼42 w/w, ▼364 m/m)
- **Merchant Complaints:** 166  (▼1 d/d, ▼7 w/w, ▼45 m/m)
- **Fraud Alerts:** 939  (▲7 d/d, ▼13 w/w, ▼112 m/m)
- **Risk Score:** 27  (▼4 m/m)
- **Response Time:** 674 ms  (▼5 d/d, ▼5 w/w, ▼68 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 259.4 | 99.5% |
| HDFC Bank | 89.0 | 99.55% |
| Bank of Baroda | 64.0 | 99.64% |
| Union Bank of India | 55.6 | 99.43% |
| ICICI Bank | 49.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 385.0 | 99.14% | 231 ms |
| Google Pay | 263.6 | 99.17% | 316 ms |
| Paytm | 65.1 | 99.06% | 192 ms |
| Navi | 29.7 | 99.17% | 225 ms |
| SuperMoney | 15.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 302.6 |
| Person to Person | 286.4 |
| QR Payments | 76.7 |
| UPI Lite | 38.7 |
| UPI Autopay | 26.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.37% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D47-MON) and any meetings/emails on 07 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D47-MON, RPT-D46-DAILY

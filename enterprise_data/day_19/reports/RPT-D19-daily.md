---
id: RPT-D19-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-10T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 10 Jul 2026)

**Report ID:** RPT-D19-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 10 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 19 of 180)

## Transaction summary
The rail processed 772.5M UPI transactions on Friday — a steady mid-week day — down 5.0M on the same day last week. Success held at 99.31% and settlement at 99.63%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 772.5  (▼7.3 d/d, ▼5.0 w/w, ▲27.6 m/m)
- **Success Rate:** 99.31%  (▲0.51 d/d, ▼0.58 w/w, ▼0.29 m/m)
- **Settlement Success:** 99.63%  (▼0.35 d/d, ▲0.89 w/w, ▲0.2 m/m)
- **Technical Declines:** 0.42%  (▼0.12 w/w, ▼0.03 m/m)
- **Business Declines:** 0.19%  (▼0.01 m/m)
- **Customer Complaints:** 1,799  (▼5 d/d, ▼460 w/w, ▼143 m/m)
- **Merchant Complaints:** 190  (▼3 d/d, ▼8 w/w, ▼21 m/m)
- **Fraud Alerts:** 1,013  (▲11 d/d, ▼10 w/w, ▼38 m/m)
- **Risk Score:** 29  (▼1 w/w, ▼2 m/m)
- **Response Time:** 707 ms  (▼3 d/d, ▼90 w/w, ▼35 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 248.4 | 99.5% |
| HDFC Bank | 85.2 | 99.55% |
| Bank of Baroda | 61.3 | 99.64% |
| Union Bank of India | 53.2 | 99.43% |
| ICICI Bank | 47.6 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 368.5 | 99.14% | 231 ms |
| Google Pay | 252.3 | 99.17% | 316 ms |
| Paytm | 62.3 | 99.06% | 192 ms |
| Navi | 28.5 | 99.17% | 225 ms |
| SuperMoney | 15.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 289.7 |
| Person to Person | 274.2 |
| QR Payments | 73.4 |
| UPI Lite | 37.1 |
| UPI Autopay | 25.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.42% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D19-MON) and any meetings/emails on 10 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D19-MON, RPT-D18-DAILY

---
id: RPT-D31-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-22T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 22 Jul 2026)

**Report ID:** RPT-D31-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 22 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 31 of 180)

## Transaction summary
The rail processed 808.7M UPI transactions on Wednesday — a steady mid-week day — up 28.4M on the same day last week. Success held at 99.62% and settlement at 99.2%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 808.7  (▲18.9 d/d, ▲28.4 w/w, ▲63.8 m/m)
- **Success Rate:** 99.62%  (▼0.36 d/d, ▲0.2 w/w, ▲0.02 m/m)
- **Settlement Success:** 99.2%  (▼0.67 d/d, ▼0.64 w/w, ▼0.23 m/m)
- **Technical Declines:** 0.4%  (▼0.01 w/w, ▼0.05 m/m)
- **Business Declines:** 0.19%  (▲0.01 d/d, ▼0.01 m/m)
- **Customer Complaints:** 1,706  (▲6 d/d, ▼49 w/w, ▼236 m/m)
- **Merchant Complaints:** 180  (▼2 d/d, ▼6 w/w, ▼31 m/m)
- **Fraud Alerts:** 969  (▼7 d/d, ▼21 w/w, ▼82 m/m)
- **Risk Score:** 28  (▼1 d/d, ▼1 w/w, ▼3 m/m)
- **Response Time:** 690 ms  (▼4 d/d, ▼19 w/w, ▼52 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 260.0 | 99.5% |
| HDFC Bank | 89.2 | 99.55% |
| Bank of Baroda | 64.1 | 99.64% |
| Union Bank of India | 55.7 | 99.43% |
| ICICI Bank | 49.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 385.8 | 99.14% | 231 ms |
| Google Pay | 264.2 | 99.17% | 316 ms |
| Paytm | 65.2 | 99.06% | 192 ms |
| Navi | 29.8 | 99.17% | 225 ms |
| SuperMoney | 15.8 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 303.3 |
| Person to Person | 287.1 |
| QR Payments | 76.8 |
| UPI Lite | 38.8 |
| UPI Autopay | 26.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.4% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D31-MON) and any meetings/emails on 22 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D31-MON, RPT-D30-DAILY

---
id: RPT-D91-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-20T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 20 Sep 2026)

**Report ID:** RPT-D91-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 20 Sep 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 91 of 180)

## Transaction summary
The rail processed 735.9M UPI transactions on Sunday — a quiet Sunday — up 20.4M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 735.9  (▼54.8 d/d, ▲20.4 w/w, ▼9.0 m/m)
- **Success Rate:** 99.98%  (▲0.55 d/d, ▲1.2 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.22 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.32%  (▼0.01 w/w, ▼0.13 m/m)
- **Business Declines:** 0.16%  (▼0.04 m/m)
- **Customer Complaints:** 1,268  (▼22 d/d, ▼39 w/w, ▼674 m/m)
- **Merchant Complaints:** 131  (▼6 w/w, ▼80 m/m)
- **Fraud Alerts:** 838  (▼5 d/d, ▼10 w/w, ▼213 m/m)
- **Risk Score:** 23  (▼1 w/w, ▼8 m/m)
- **Response Time:** 622 ms  (▼4 d/d, ▼11 w/w, ▼120 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 236.6 | 99.5% |
| HDFC Bank | 81.2 | 99.55% |
| Bank of Baroda | 58.4 | 99.64% |
| Union Bank of India | 50.7 | 99.43% |
| ICICI Bank | 45.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 351.1 | 99.14% | 231 ms |
| Google Pay | 240.4 | 99.17% | 316 ms |
| Paytm | 59.4 | 99.06% | 192 ms |
| Navi | 27.1 | 99.17% | 225 ms |
| SuperMoney | 14.3 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 276.0 |
| Person to Person | 261.2 |
| QR Payments | 69.9 |
| UPI Lite | 35.3 |
| UPI Autopay | 24.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.32% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D91-MON) and any meetings/emails on 20 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D91-MON, RPT-D90-DAILY

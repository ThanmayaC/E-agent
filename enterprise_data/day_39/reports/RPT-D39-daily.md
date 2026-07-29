---
id: RPT-D39-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-30T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 30 Jul 2026)

**Report ID:** RPT-D39-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 30 Jul 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 39 of 180)

## Transaction summary
The rail processed 905.4M UPI transactions on Thursday — the month-end surge as salary and bill-pay flows land — up 123.8M on the same day last week. Success held at 99.6% and settlement at 99.42%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 905.4  (▼5.3 d/d, ▲123.8 w/w, ▲160.5 m/m)
- **Success Rate:** 99.6%  (▼0.38 d/d, ▲0.12 w/w)
- **Settlement Success:** 99.42%  (▼0.56 d/d, ▼0.56 w/w, ▼0.01 m/m)
- **Technical Declines:** 0.39%  (▼0.01 d/d, ▼0.01 w/w, ▼0.06 m/m)
- **Business Declines:** 0.18%  (▼0.03 d/d, ▼0.01 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,640  (▼156 d/d, ▼42 w/w, ▼302 m/m)
- **Merchant Complaints:** 174  (▼75 d/d, ▼5 w/w, ▼37 m/m)
- **Fraud Alerts:** 947  (▼18 d/d, ▼33 w/w, ▼104 m/m)
- **Risk Score:** 27  (▼1 d/d, ▼1 w/w, ▼4 m/m)
- **Response Time:** 682 ms  (▼5 d/d, ▼5 w/w, ▼60 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 291.1 | 99.5% |
| HDFC Bank | 99.9 | 99.55% |
| Bank of Baroda | 71.8 | 99.64% |
| Union Bank of India | 62.4 | 99.43% |
| ICICI Bank | 55.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 431.9 | 99.14% | 231 ms |
| Google Pay | 295.7 | 99.17% | 316 ms |
| Paytm | 73.0 | 99.06% | 192 ms |
| Navi | 33.4 | 99.17% | 225 ms |
| SuperMoney | 17.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 339.5 |
| Person to Person | 321.4 |
| QR Payments | 86.0 |
| UPI Lite | 43.5 |
| UPI Autopay | 29.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.39% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D39-MON) and any meetings/emails on 30 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D39-MON, RPT-D38-DAILY

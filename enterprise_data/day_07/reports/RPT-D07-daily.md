---
id: RPT-D07-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-28T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 28 Jun 2026)

**Report ID:** RPT-D07-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 28 Jun 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 7 of 180)

## Transaction summary
The rail processed 849.5M UPI transactions on Sunday — the month-end surge as salary and bill-pay flows land — the first day in the window. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 849.5  (▲183.6 d/d, ▲104.6 m/m)
- **Success Rate:** 99.98%  (▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.55 m/m)
- **Technical Declines:** 0.44%  (▼0.08 d/d, ▼0.01 m/m)
- **Business Declines:** 0.2%
- **Customer Complaints:** 1,905  (▼230 d/d, ▼37 m/m)
- **Merchant Complaints:** 204  (▼36 d/d, ▼7 m/m)
- **Fraud Alerts:** 1,036  (▲9 d/d, ▼15 m/m)
- **Risk Score:** 31  (▲1 d/d)
- **Response Time:** 730 ms  (▼20 d/d, ▼12 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 273.1 | 99.5% |
| HDFC Bank | 93.7 | 99.55% |
| Bank of Baroda | 67.4 | 99.64% |
| Union Bank of India | 58.5 | 99.43% |
| ICICI Bank | 52.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 405.3 | 99.14% | 231 ms |
| Google Pay | 277.5 | 99.17% | 316 ms |
| Paytm | 68.5 | 99.06% | 192 ms |
| Navi | 31.3 | 99.17% | 225 ms |
| SuperMoney | 16.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 318.6 |
| Person to Person | 301.6 |
| QR Payments | 80.7 |
| UPI Lite | 40.8 |
| UPI Autopay | 28.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.44% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D07-MON) and any meetings/emails on 28 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D07-MON, RPT-D06-DAILY

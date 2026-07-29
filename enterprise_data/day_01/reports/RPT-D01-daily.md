---
id: RPT-D01-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-22T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 22 Jun 2026)

**Report ID:** RPT-D01-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 22 Jun 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 1 of 180)

## Transaction summary
The rail processed 744.9M UPI transactions on Monday — the Monday ramp-up after the weekend — the first day in the window. Success held at 99.6% and settlement at 99.43%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 744.9
- **Success Rate:** 99.6%
- **Settlement Success:** 99.43%
- **Technical Declines:** 0.45%
- **Business Declines:** 0.2%
- **Customer Complaints:** 1,942
- **Merchant Complaints:** 211
- **Fraud Alerts:** 1,051
- **Risk Score:** 31
- **Response Time:** 742 ms

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 239.5 | 99.5% |
| HDFC Bank | 82.2 | 99.55% |
| Bank of Baroda | 59.1 | 99.64% |
| Union Bank of India | 51.3 | 99.43% |
| ICICI Bank | 45.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 355.4 | 99.14% | 231 ms |
| Google Pay | 243.3 | 99.17% | 316 ms |
| Paytm | 60.1 | 99.06% | 192 ms |
| Navi | 27.5 | 99.17% | 225 ms |
| SuperMoney | 14.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 279.3 |
| Person to Person | 264.4 |
| QR Payments | 70.8 |
| UPI Lite | 35.8 |
| UPI Autopay | 24.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.45% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D01-MON) and any meetings/emails on 22 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D01-MON, ORG-OVERVIEW

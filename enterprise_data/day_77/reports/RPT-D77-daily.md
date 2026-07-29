---
id: RPT-D77-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-06T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 06 Sep 2026)

**Report ID:** RPT-D77-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 06 Sep 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 77 of 180)

## Transaction summary
The rail processed 708.4M UPI transactions on Sunday — a quiet Sunday — down 232.8M on the same day last week. Success held at 99.19% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 708.4  (▼59.3 d/d, ▼232.8 w/w, ▼36.5 m/m)
- **Success Rate:** 99.19%  (▼0.76 d/d, ▼0.73 w/w, ▼0.41 m/m)
- **Settlement Success:** 99.98%  (▲0.67 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.33%  (▼0.01 d/d, ▼0.13 w/w, ▼0.12 m/m)
- **Business Declines:** 0.17%  (▼0.03 m/m)
- **Customer Complaints:** 1,358  (▼18 d/d, ▼421 w/w, ▼584 m/m)
- **Merchant Complaints:** 141  (▼2 d/d, ▼6 w/w, ▼70 m/m)
- **Fraud Alerts:** 870  (▼3 d/d, ▼16 w/w, ▼181 m/m)
- **Risk Score:** 24  (▼1 w/w, ▼7 m/m)
- **Response Time:** 638 ms  (▲2 d/d, ▼95 w/w, ▼104 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 227.8 | 99.5% |
| HDFC Bank | 78.2 | 99.55% |
| Bank of Baroda | 56.2 | 99.64% |
| Union Bank of India | 48.8 | 99.43% |
| ICICI Bank | 43.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 338.0 | 99.14% | 231 ms |
| Google Pay | 231.4 | 99.17% | 316 ms |
| Paytm | 57.1 | 99.06% | 192 ms |
| Navi | 26.1 | 99.17% | 225 ms |
| SuperMoney | 13.8 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 265.6 |
| Person to Person | 251.5 |
| QR Payments | 67.3 |
| UPI Lite | 34.0 |
| UPI Autopay | 23.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.33% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D77-MON) and any meetings/emails on 06 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D77-MON, RPT-D76-DAILY

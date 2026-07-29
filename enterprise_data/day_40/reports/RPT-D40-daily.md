---
id: RPT-D40-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-31T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 31 Jul 2026)

**Report ID:** RPT-D40-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 31 Jul 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 40 of 180)

## Transaction summary
The rail processed 893.3M UPI transactions on Friday — the month-end surge as salary and bill-pay flows land — up 78.1M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 893.3  (▼12.1 d/d, ▲78.1 w/w, ▲148.4 m/m)
- **Success Rate:** 99.98%  (▲0.38 d/d, ▲0.55 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.56 d/d, ▲1.15 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.39%  (▼0.01 w/w, ▼0.06 m/m)
- **Business Declines:** 0.18%  (▼0.02 m/m)
- **Customer Complaints:** 1,620  (▼20 d/d, ▼62 w/w, ▼322 m/m)
- **Merchant Complaints:** 173  (▼1 d/d, ▼5 w/w, ▼38 m/m)
- **Fraud Alerts:** 952  (▲5 d/d, ▼17 w/w, ▼99 m/m)
- **Risk Score:** 27  (▼1 w/w, ▼4 m/m)
- **Response Time:** 679 ms  (▼3 d/d, ▼17 w/w, ▼63 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 287.2 | 99.5% |
| HDFC Bank | 98.5 | 99.55% |
| Bank of Baroda | 70.8 | 99.64% |
| Union Bank of India | 61.5 | 99.43% |
| ICICI Bank | 55.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 426.2 | 99.14% | 231 ms |
| Google Pay | 291.8 | 99.17% | 316 ms |
| Paytm | 72.1 | 99.06% | 192 ms |
| Navi | 32.9 | 99.17% | 225 ms |
| SuperMoney | 17.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 335.0 |
| Person to Person | 317.1 |
| QR Payments | 84.9 |
| UPI Lite | 42.9 |
| UPI Autopay | 29.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.39% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D40-MON) and any meetings/emails on 31 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D40-MON, RPT-D39-DAILY

---
id: RPT-D123-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-22T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 22 Oct 2026)

**Report ID:** RPT-D123-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 22 Oct 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 123 of 180)

## Transaction summary
The rail processed 943.5M UPI transactions on Thursday — a steady mid-week day — up 14.0M on the same day last week. Success held at 99.98% and settlement at 99.82%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 943.5  (▼14.4 d/d, ▲14.0 w/w, ▲198.6 m/m)
- **Success Rate:** 99.98%  (▲0.63 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.82%  (▲0.9 d/d, ▲0.13 w/w, ▲0.39 m/m)
- **Technical Declines:** 0.28%  (▼0.01 w/w, ▼0.17 m/m)
- **Business Declines:** 0.15%  (▼0.01 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,094  (▼10 d/d, ▼77 w/w, ▼848 m/m)
- **Merchant Complaints:** 112  (▼4 w/w, ▼99 m/m)
- **Fraud Alerts:** 782  (▲11 d/d, ▼38 w/w, ▼269 m/m)
- **Risk Score:** 21  (▼3 w/w, ▼10 m/m)
- **Response Time:** 585 ms  (▲3 d/d, ▼12 w/w, ▼157 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 303.4 | 99.5% |
| HDFC Bank | 104.1 | 99.55% |
| Bank of Baroda | 74.8 | 99.64% |
| Union Bank of India | 65.0 | 99.43% |
| ICICI Bank | 58.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 450.1 | 99.14% | 231 ms |
| Google Pay | 308.2 | 99.17% | 316 ms |
| Paytm | 76.1 | 99.06% | 192 ms |
| Navi | 34.8 | 99.17% | 225 ms |
| SuperMoney | 18.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 353.8 |
| Person to Person | 334.9 |
| QR Payments | 89.6 |
| UPI Lite | 45.3 |
| UPI Autopay | 31.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.28% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D123-MON) and any meetings/emails on 22 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D123-MON, RPT-D122-DAILY

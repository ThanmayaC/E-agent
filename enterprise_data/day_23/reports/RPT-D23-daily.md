---
id: RPT-D23-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-14T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 14 Jul 2026)

**Report ID:** RPT-D23-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 14 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 23 of 180)

## Transaction summary
The rail processed 776.6M UPI transactions on Tuesday — a steady mid-week day — up 16.3M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 776.6  (▲11.3 d/d, ▲16.3 w/w, ▲31.7 m/m)
- **Success Rate:** 99.98%  (▲0.97 d/d, ▲1.5 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲1.28 d/d, ▲0.51 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.41%  (▼0.01 w/w, ▼0.04 m/m)
- **Business Declines:** 0.19%  (▼0.09 w/w, ▼0.01 m/m)
- **Customer Complaints:** 1,774  (▼7 d/d, ▼428 w/w, ▼168 m/m)
- **Merchant Complaints:** 188  (▲1 d/d, ▼7 w/w, ▼23 m/m)
- **Fraud Alerts:** 988  (▼7 d/d, ▼225 w/w, ▼63 m/m)
- **Risk Score:** 29  (▼16 w/w, ▼2 m/m)
- **Response Time:** 706 ms  (▼4 d/d, ▼5 w/w, ▼36 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 249.7 | 99.5% |
| HDFC Bank | 85.7 | 99.55% |
| Bank of Baroda | 61.6 | 99.64% |
| Union Bank of India | 53.5 | 99.43% |
| ICICI Bank | 47.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 370.5 | 99.14% | 231 ms |
| Google Pay | 253.7 | 99.17% | 316 ms |
| Paytm | 62.7 | 99.06% | 192 ms |
| Navi | 28.6 | 99.17% | 225 ms |
| SuperMoney | 15.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 291.2 |
| Person to Person | 275.7 |
| QR Payments | 73.8 |
| UPI Lite | 37.3 |
| UPI Autopay | 25.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.41% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D23-MON) and any meetings/emails on 14 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D23-MON, RPT-D22-DAILY

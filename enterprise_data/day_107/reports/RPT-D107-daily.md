---
id: RPT-D107-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-06T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 06 Oct 2026)

**Report ID:** RPT-D107-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 06 Oct 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 107 of 180)

## Transaction summary
The rail processed 935.3M UPI transactions on Tuesday — a steady mid-week day — down 94.4M on the same day last week. Success held at 98.81% and settlement at 99.91%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 935.3  (▼181.7 d/d, ▼94.4 w/w, ▲190.4 m/m)
- **Success Rate:** 98.81%  (▼0.4 d/d, ▼1.17 w/w, ▼0.79 m/m)
- **Settlement Success:** 99.91%  (▼0.07 d/d, ▲1.07 w/w, ▲0.48 m/m)
- **Technical Declines:** 0.3%  (▼0.01 w/w, ▼0.15 m/m)
- **Business Declines:** 0.15%  (▼0.05 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,172  (▼6 d/d, ▼205 w/w, ▼770 m/m)
- **Merchant Complaints:** 121  (▼101 w/w, ▼90 m/m)
- **Fraud Alerts:** 799  (▼11 d/d, ▼27 w/w, ▼252 m/m)
- **Risk Score:** 22  (▼1 w/w, ▼9 m/m)
- **Response Time:** 604 ms  (▼1 d/d, ▼7 w/w, ▼138 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 300.7 | 99.5% |
| HDFC Bank | 103.2 | 99.55% |
| Bank of Baroda | 74.2 | 99.64% |
| Union Bank of India | 64.4 | 99.43% |
| ICICI Bank | 57.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 446.2 | 99.14% | 231 ms |
| Google Pay | 305.5 | 99.17% | 316 ms |
| Paytm | 75.5 | 99.06% | 192 ms |
| Navi | 34.5 | 99.17% | 225 ms |
| SuperMoney | 18.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 350.7 |
| Person to Person | 332.0 |
| QR Payments | 88.9 |
| UPI Lite | 44.9 |
| UPI Autopay | 30.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D107-MON) and any meetings/emails on 06 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D107-MON, RPT-D106-DAILY

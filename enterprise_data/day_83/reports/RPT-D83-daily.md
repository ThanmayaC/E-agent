---
id: RPT-D83-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-12T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 12 Sep 2026)

**Report ID:** RPT-D83-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 12 Sep 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 83 of 180)

## Transaction summary
The rail processed 806.0M UPI transactions on Saturday — a lighter Saturday — up 38.3M on the same day last week. Success held at 99.81% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 806.0  (▼270.6 d/d, ▲38.3 w/w, ▲61.1 m/m)
- **Success Rate:** 99.81%  (▲0.65 d/d, ▼0.14 w/w, ▲0.21 m/m)
- **Settlement Success:** 99.98%  (▲0.87 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.33%  (▼0.01 w/w, ▼0.12 m/m)
- **Business Declines:** 0.16%  (▼0.01 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,333  (▲2 d/d, ▼43 w/w, ▼609 m/m)
- **Merchant Complaints:** 138  (▼1 d/d, ▼5 w/w, ▼73 m/m)
- **Fraud Alerts:** 850  (▼10 d/d, ▼23 w/w, ▼201 m/m)
- **Risk Score:** 24  (▼7 m/m)
- **Response Time:** 631 ms  (▼1 d/d, ▼5 w/w, ▼111 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 259.1 | 99.5% |
| HDFC Bank | 88.9 | 99.55% |
| Bank of Baroda | 63.9 | 99.64% |
| Union Bank of India | 55.5 | 99.43% |
| ICICI Bank | 49.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 384.5 | 99.14% | 231 ms |
| Google Pay | 263.3 | 99.17% | 316 ms |
| Paytm | 65.0 | 99.06% | 192 ms |
| Navi | 29.7 | 99.17% | 225 ms |
| SuperMoney | 15.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 302.2 |
| Person to Person | 286.1 |
| QR Payments | 76.6 |
| UPI Lite | 38.7 |
| UPI Autopay | 26.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.33% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D83-MON) and any meetings/emails on 12 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D83-MON, RPT-D82-DAILY

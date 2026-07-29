---
id: RPT-D67-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-27T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 27 Aug 2026)

**Report ID:** RPT-D67-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 27 Aug 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 67 of 180)

## Transaction summary
The rail processed 866.7M UPI transactions on Thursday — a steady mid-week day — up 37.8M on the same day last week. Success held at 99.96% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 866.7  (▼3.4 d/d, ▲37.8 w/w, ▲121.8 m/m)
- **Success Rate:** 99.96%  (▲0.04 d/d, ▲0.16 w/w, ▲0.36 m/m)
- **Settlement Success:** 99.98%  (▲0.99 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.35%  (▼0.01 w/w, ▼0.1 m/m)
- **Business Declines:** 0.17%  (▼0.04 d/d, ▼0.02 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,424  (▼24 d/d, ▼89 w/w, ▼518 m/m)
- **Merchant Complaints:** 150  (▼55 d/d, ▼35 w/w, ▼61 m/m)
- **Fraud Alerts:** 899  (▲2 d/d, ▼1 w/w, ▼152 m/m)
- **Risk Score:** 25  (▼1 w/w, ▼6 m/m)
- **Response Time:** 651 ms  (▲4 d/d, ▼6 w/w, ▼91 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 278.7 | 99.5% |
| HDFC Bank | 95.6 | 99.55% |
| Bank of Baroda | 68.7 | 99.64% |
| Union Bank of India | 59.7 | 99.43% |
| ICICI Bank | 53.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 413.5 | 99.14% | 231 ms |
| Google Pay | 283.1 | 99.17% | 316 ms |
| Paytm | 69.9 | 99.06% | 192 ms |
| Navi | 31.9 | 99.17% | 225 ms |
| SuperMoney | 16.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 325.0 |
| Person to Person | 307.7 |
| QR Payments | 82.3 |
| UPI Lite | 41.6 |
| UPI Autopay | 28.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.35% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D67-MON) and any meetings/emails on 27 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D67-MON, RPT-D66-DAILY

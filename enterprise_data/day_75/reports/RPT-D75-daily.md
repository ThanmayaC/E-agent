---
id: RPT-D75-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-04T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 04 Sep 2026)

**Report ID:** RPT-D75-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 04 Sep 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 75 of 180)

## Transaction summary
The rail processed 867.3M UPI transactions on Friday — a steady mid-week day — down 85.9M on the same day last week. Success held at 99.35% and settlement at 99.39%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 867.3  (▼11.6 d/d, ▼85.9 w/w, ▲122.4 m/m)
- **Success Rate:** 99.35%  (▲0.17 d/d, ▼0.25 w/w, ▼0.25 m/m)
- **Settlement Success:** 99.39%  (▼0.59 d/d, ▼0.51 w/w, ▼0.04 m/m)
- **Technical Declines:** 0.34%  (▼0.01 w/w, ▼0.11 m/m)
- **Business Declines:** 0.17%  (▼0.03 m/m)
- **Customer Complaints:** 1,383  (▼12 d/d, ▼42 w/w, ▼559 m/m)
- **Merchant Complaints:** 144  (▲1 d/d, ▼5 w/w, ▼67 m/m)
- **Fraud Alerts:** 868  (▼1 d/d, ▼18 w/w, ▼183 m/m)
- **Risk Score:** 24  (▼1 d/d, ▼1 w/w, ▼7 m/m)
- **Response Time:** 640 ms  (▲2 d/d, ▼10 w/w, ▼102 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 278.9 | 99.5% |
| HDFC Bank | 95.7 | 99.55% |
| Bank of Baroda | 68.8 | 99.64% |
| Union Bank of India | 59.7 | 99.43% |
| ICICI Bank | 53.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 413.8 | 99.14% | 231 ms |
| Google Pay | 283.3 | 99.17% | 316 ms |
| Paytm | 70.0 | 99.06% | 192 ms |
| Navi | 32.0 | 99.17% | 225 ms |
| SuperMoney | 16.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 325.2 |
| Person to Person | 307.9 |
| QR Payments | 82.4 |
| UPI Lite | 41.6 |
| UPI Autopay | 28.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.34% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D75-MON) and any meetings/emails on 04 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D75-MON, RPT-D74-DAILY

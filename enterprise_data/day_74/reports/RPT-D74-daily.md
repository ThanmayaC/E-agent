---
id: RPT-D74-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-03T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 03 Sep 2026)

**Report ID:** RPT-D74-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 03 Sep 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 74 of 180)

## Transaction summary
The rail processed 878.9M UPI transactions on Thursday — a steady mid-week day — up 12.2M on the same day last week. Success held at 99.18% and settlement at 99.98%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 878.9  (▲24.2 d/d, ▲12.2 w/w, ▲134.0 m/m)
- **Success Rate:** 99.18%  (▼0.8 d/d, ▼0.78 w/w, ▼0.42 m/m)
- **Settlement Success:** 99.98%  (▲1.06 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.34%  (▼0.01 w/w, ▼0.11 m/m)
- **Business Declines:** 0.17%  (▼0.03 m/m)
- **Customer Complaints:** 1,395  (▼7 d/d, ▼29 w/w, ▼547 m/m)
- **Merchant Complaints:** 143  (▼7 w/w, ▼68 m/m)
- **Fraud Alerts:** 869  (▼9 d/d, ▼30 w/w, ▼182 m/m)
- **Risk Score:** 25  (▼6 m/m)
- **Response Time:** 638 ms  (▼13 w/w, ▼104 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 282.6 | 99.5% |
| HDFC Bank | 97.0 | 99.55% |
| Bank of Baroda | 69.7 | 99.64% |
| Union Bank of India | 60.5 | 99.43% |
| ICICI Bank | 54.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 419.3 | 99.14% | 231 ms |
| Google Pay | 287.1 | 99.17% | 316 ms |
| Paytm | 70.9 | 99.06% | 192 ms |
| Navi | 32.4 | 99.17% | 225 ms |
| SuperMoney | 17.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 329.6 |
| Person to Person | 312.0 |
| QR Payments | 83.5 |
| UPI Lite | 42.2 |
| UPI Autopay | 29.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.34% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D74-MON) and any meetings/emails on 03 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D74-MON, RPT-D73-DAILY

---
id: RPT-D165-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-03T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 03 Dec 2026)

**Report ID:** RPT-D165-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 03 Dec 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 165 of 180)

## Transaction summary
The rail processed 1026.5M UPI transactions on Thursday — a steady mid-week day — up 0.7M on the same day last week. Success held at 99.98% and settlement at 99.48%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1026.5  (▼8.0 d/d, ▲0.7 w/w, ▲281.6 m/m)
- **Success Rate:** 99.98%  (▲0.38 m/m)
- **Settlement Success:** 99.48%  (▼0.5 d/d, ▼0.5 w/w, ▲0.05 m/m)
- **Technical Declines:** 0.24%  (▼0.01 w/w, ▼0.21 m/m)
- **Business Declines:** 0.13%  (▼0.07 m/m)
- **Customer Complaints:** 897  (▼2 d/d, ▼29 w/w, ▼1045 m/m)
- **Merchant Complaints:** 90  (▼3 w/w, ▼121 m/m)
- **Fraud Alerts:** 702  (▲4 d/d, ▼4 w/w, ▼349 m/m)
- **Risk Score:** 18  (▼1 d/d, ▼1 w/w, ▼13 m/m)
- **Response Time:** 538 ms  (▼3 d/d, ▼7 w/w, ▼204 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 330.0 | 99.5% |
| HDFC Bank | 113.2 | 99.55% |
| Bank of Baroda | 81.4 | 99.64% |
| Union Bank of India | 70.7 | 99.43% |
| ICICI Bank | 63.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 489.7 | 99.14% | 231 ms |
| Google Pay | 335.3 | 99.17% | 316 ms |
| Paytm | 82.8 | 99.06% | 192 ms |
| Navi | 37.8 | 99.17% | 225 ms |
| SuperMoney | 20.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 384.9 |
| Person to Person | 364.4 |
| QR Payments | 97.5 |
| UPI Lite | 49.3 |
| UPI Autopay | 33.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.24% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D165-MON) and any meetings/emails on 03 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D165-MON, RPT-D164-DAILY

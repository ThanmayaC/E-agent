---
id: RPT-D25-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-16T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 16 Jul 2026)

**Report ID:** RPT-D25-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 16 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 25 of 180)

## Transaction summary
The rail processed 779.1M UPI transactions on Thursday — a steady mid-week day — down 0.7M on the same day last week. Success held at 99.98% and settlement at 99.05%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 779.1  (▼1.2 d/d, ▼0.7 w/w, ▲34.2 m/m)
- **Success Rate:** 99.98%  (▲0.56 d/d, ▲1.18 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.05%  (▼0.79 d/d, ▼0.93 w/w, ▼0.38 m/m)
- **Technical Declines:** 0.41%  (▼0.01 w/w, ▼0.04 m/m)
- **Business Declines:** 0.19%  (▼0.01 m/m)
- **Customer Complaints:** 1,735  (▼20 d/d, ▼69 w/w, ▼207 m/m)
- **Merchant Complaints:** 187  (▲1 d/d, ▼6 w/w, ▼24 m/m)
- **Fraud Alerts:** 994  (▲4 d/d, ▼8 w/w, ▼57 m/m)
- **Risk Score:** 29  (▼2 m/m)
- **Response Time:** 700 ms  (▼9 d/d, ▼10 w/w, ▼42 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 250.5 | 99.5% |
| HDFC Bank | 86.0 | 99.55% |
| Bank of Baroda | 61.8 | 99.64% |
| Union Bank of India | 53.7 | 99.43% |
| ICICI Bank | 48.0 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 371.7 | 99.14% | 231 ms |
| Google Pay | 254.5 | 99.17% | 316 ms |
| Paytm | 62.9 | 99.06% | 192 ms |
| Navi | 28.7 | 99.17% | 225 ms |
| SuperMoney | 15.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 292.2 |
| Person to Person | 276.6 |
| QR Payments | 74.0 |
| UPI Lite | 37.4 |
| UPI Autopay | 25.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.41% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D25-MON) and any meetings/emails on 16 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D25-MON, RPT-D24-DAILY

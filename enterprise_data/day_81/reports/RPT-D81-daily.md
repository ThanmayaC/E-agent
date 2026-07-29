---
id: RPT-D81-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-10T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 10 Sep 2026)

**Report ID:** RPT-D81-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 10 Sep 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 81 of 180)

## Transaction summary
The rail processed 871.3M UPI transactions on Thursday — a steady mid-week day — down 7.6M on the same day last week. Success held at 99.34% and settlement at 98.89%; the softest bank was IndusInd Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 871.3  (▲4.1 d/d, ▼7.6 w/w, ▲126.4 m/m)
- **Success Rate:** 99.34%  (▲0.42 d/d, ▲0.16 w/w, ▼0.26 m/m)
- **Settlement Success:** 98.89%  (▼1.09 d/d, ▼1.09 w/w, ▼0.54 m/m)
- **Technical Declines:** 0.33%  (▼0.01 w/w, ▼0.12 m/m)
- **Business Declines:** 0.16%  (▼0.01 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,334  (▲4 d/d, ▼61 w/w, ▼608 m/m)
- **Merchant Complaints:** 138  (▼1 d/d, ▼5 w/w, ▼73 m/m)
- **Fraud Alerts:** 856  (▼9 d/d, ▼13 w/w, ▼195 m/m)
- **Risk Score:** 24  (▼1 w/w, ▼7 m/m)
- **Response Time:** 638 ms  (▲6 d/d, ▼104 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 280.1 | 99.5% |
| HDFC Bank | 96.1 | 99.55% |
| Bank of Baroda | 69.1 | 99.64% |
| Union Bank of India | 60.0 | 99.43% |
| ICICI Bank | 53.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 415.7 | 99.14% | 231 ms |
| Google Pay | 284.6 | 99.17% | 316 ms |
| Paytm | 70.3 | 99.06% | 192 ms |
| Navi | 32.1 | 99.17% | 225 ms |
| SuperMoney | 17.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 326.7 |
| Person to Person | 309.3 |
| QR Payments | 82.8 |
| UPI Lite | 41.8 |
| UPI Autopay | 28.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.33% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D81-MON) and any meetings/emails on 10 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D81-MON, RPT-D80-DAILY

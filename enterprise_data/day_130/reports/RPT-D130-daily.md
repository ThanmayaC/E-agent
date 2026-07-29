---
id: RPT-D130-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-29T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 29 Oct 2026)

**Report ID:** RPT-D130-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 29 Oct 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 130 of 180)

## Transaction summary
The rail processed 1088.8M UPI transactions on Thursday — the month-end surge as salary and bill-pay flows land — up 145.3M on the same day last week. Success landed at 99.65% and settlement at 99.98%, held back by live issues on TravelGo, InsureWell, Union Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1088.8  (▲20.7 d/d, ▲145.3 w/w, ▲343.9 m/m)
- **Success Rate:** 99.65%  (▲1.24 d/d, ▼0.33 w/w, ▲0.05 m/m)
- **Settlement Success:** 99.98%  (▲0.09 d/d, ▲0.16 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.29%  (▼0.03 d/d, ▲0.01 w/w, ▼0.16 m/m)
- **Business Declines:** 0.18%  (▼0.03 d/d, ▲0.03 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,123  (▼62 d/d, ▲29 w/w, ▼819 m/m)
- **Merchant Complaints:** 157  (▼37 d/d, ▲45 w/w, ▼54 m/m)
- **Fraud Alerts:** 760  (▲2 d/d, ▼22 w/w, ▼291 m/m)
- **Risk Score:** 21  (▼10 m/m)
- **Response Time:** 582 ms  (▼16 d/d, ▼3 w/w, ▼160 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 350.1 | 99.5% |
| HDFC Bank | 120.1 | 99.55% |
| Bank of Baroda | 86.4 | 99.64% |
| Union Bank of India | 75.0 | 99.28% |
| ICICI Bank | 67.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 519.4 | 99.14% | 231 ms |
| Google Pay | 355.6 | 99.17% | 316 ms |
| Paytm | 87.8 | 99.06% | 192 ms |
| Navi | 40.1 | 99.17% | 225 ms |
| SuperMoney | 21.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 408.3 |
| Person to Person | 386.5 |
| QR Payments | 103.4 |
| UPI Lite | 52.3 |
| UPI Autopay | 35.9 |

## Failure analysis
- INC-2026-05 — bank timeout / 5xx spike on Union Bank of India (day 5 of 5); see RCA-2026-05.
- INC-2026-24 — merchant decline-rate spike on TravelGo, InsureWell (day 2 of 5); see RCA-2026-24.

## Recommendations
Stay on the open incidents: keep recovery monitoring on TravelGo, InsureWell, Union Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D130-MON) and any meetings/emails on 29 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D130-MON, RPT-D129-DAILY, INC-2026-05, INC-2026-24, RCA-2026-05, RCA-2026-24

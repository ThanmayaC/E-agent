---
id: RPT-D127-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-26T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 26 Oct 2026)

**Report ID:** RPT-D127-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 26 Oct 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 127 of 180)

## Transaction summary
The rail processed 925.3M UPI transactions on Monday — the Monday ramp-up after the weekend — down 1.6M on the same day last week. Success landed at 98.78% and settlement at 98.89%, held back by live issues on Union Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 925.3  (▲143.9 d/d, ▼1.6 w/w, ▲180.4 m/m)
- **Success Rate:** 98.78%  (▲0.56 d/d, ▼0.51 w/w, ▼0.82 m/m)
- **Settlement Success:** 98.89%  (▼0.19 d/d, ▼1.09 w/w, ▼0.54 m/m)
- **Technical Declines:** 0.46%  (▼0.12 d/d, ▲0.16 w/w, ▲0.01 m/m)
- **Business Declines:** 0.15%  (▼0.05 m/m)
- **Customer Complaints:** 1,547  (▼284 d/d, ▲393 w/w, ▼395 m/m)
- **Merchant Complaints:** 183  (▼46 d/d, ▲69 w/w, ▼28 m/m)
- **Fraud Alerts:** 765  (▼9 d/d, ▼12 w/w, ▼286 m/m)
- **Risk Score:** 21  (▼10 m/m)
- **Response Time:** 636 ms  (▼46 d/d, ▲33 w/w, ▼106 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 297.5 | 99.5% |
| HDFC Bank | 102.1 | 99.55% |
| Bank of Baroda | 73.4 | 99.64% |
| Union Bank of India | 63.7 | 98.07% |
| ICICI Bank | 57.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 441.4 | 99.14% | 231 ms |
| Google Pay | 302.2 | 99.17% | 316 ms |
| Paytm | 74.6 | 99.06% | 192 ms |
| Navi | 34.1 | 99.17% | 225 ms |
| SuperMoney | 18.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 347.0 |
| Person to Person | 328.5 |
| QR Payments | 87.9 |
| UPI Lite | 44.4 |
| UPI Autopay | 30.5 |

## Failure analysis
- INC-2026-05 — bank timeout / 5xx spike on Union Bank of India (day 2 of 5); see RCA-2026-05.

## Recommendations
Stay on the open incident: keep recovery monitoring on Union Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D127-MON) and any meetings/emails on 26 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D127-MON, RPT-D126-DAILY, INC-2026-05, RCA-2026-05

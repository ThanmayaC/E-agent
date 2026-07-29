---
id: RPT-D161-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-29T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 29 Nov 2026)

**Report ID:** RPT-D161-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 29 Nov 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 161 of 180)

## Transaction summary
The rail processed 1137.2M UPI transactions on Sunday — the month-end surge as salary and bill-pay flows land — up 295.1M on the same day last week. Success landed at 98.92% and settlement at 99.07%, held back by live issues on Bank of Baroda (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1137.2  (▲19.3 d/d, ▲295.1 w/w, ▲392.3 m/m)
- **Success Rate:** 98.92%  (▼1.06 d/d, ▼1.06 w/w, ▼0.68 m/m)
- **Settlement Success:** 99.07%  (▼0.91 d/d, ▼0.91 w/w, ▼0.36 m/m)
- **Technical Declines:** 0.4%  (▲0.15 d/d, ▲0.15 w/w, ▼0.05 m/m)
- **Business Declines:** 0.13%  (▼0.02 w/w, ▼0.07 m/m)
- **Customer Complaints:** 1,294  (▲371 d/d, ▲293 w/w, ▼648 m/m)
- **Merchant Complaints:** 153  (▲61 d/d, ▲58 w/w, ▼58 m/m)
- **Fraud Alerts:** 708  (▼3 d/d, ▼45 w/w, ▼343 m/m)
- **Risk Score:** 19  (▼3 w/w, ▼12 m/m)
- **Response Time:** 597 ms  (▲53 d/d, ▲46 w/w, ▼145 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 365.6 | 99.5% |
| HDFC Bank | 125.5 | 99.55% |
| Bank of Baroda | 90.2 | 98.92% |
| Union Bank of India | 78.3 | 99.43% |
| ICICI Bank | 70.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 542.5 | 99.14% | 231 ms |
| Google Pay | 371.5 | 99.17% | 316 ms |
| Paytm | 91.7 | 99.06% | 192 ms |
| Navi | 41.9 | 99.17% | 225 ms |
| SuperMoney | 22.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 426.5 |
| Person to Person | 403.7 |
| QR Payments | 108.0 |
| UPI Lite | 54.6 |
| UPI Autopay | 37.5 |

## Failure analysis
- INC-2026-22 — bank timeout / 5xx spike on Bank of Baroda (day 1 of 2); see INC-2026-22.

## Recommendations
Stay on the open incident: keep recovery monitoring on Bank of Baroda and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D161-MON) and any meetings/emails on 29 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D161-MON, RPT-D160-DAILY, INC-2026-22

---
id: RPT-D100-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-29T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 29 Sep 2026)

**Report ID:** RPT-D100-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 29 Sep 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 100 of 180)

## Transaction summary
The rail processed 1029.7M UPI transactions on Tuesday — the month-end surge as salary and bill-pay flows land — up 128.3M on the same day last week. Success landed at 99.98% and settlement at 98.84%, held back by live issues on State Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1029.7  (▲2.1 d/d, ▲128.3 w/w, ▲284.8 m/m)
- **Success Rate:** 99.98%  (▲0.89 d/d, ▲0.47 w/w, ▲0.38 m/m)
- **Settlement Success:** 98.84%  (▼1.14 d/d, ▼0.43 w/w, ▼0.59 m/m)
- **Technical Declines:** 0.31%  (▼0.14 m/m)
- **Business Declines:** 0.2%  (▲0.03 d/d, ▲0.04 w/w)
- **Customer Complaints:** 1,377  (▲112 d/d, ▲121 w/w, ▼565 m/m)
- **Merchant Complaints:** 222  (▲97 d/d, ▲91 w/w, ▲11 m/m)
- **Fraud Alerts:** 826  (▼23 d/d, ▼8 w/w, ▼225 m/m)
- **Risk Score:** 23  (▼1 d/d, ▼8 m/m)
- **Response Time:** 611 ms  (▼2 d/d, ▼15 w/w, ▼131 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 331.1 | 98.78% |
| HDFC Bank | 113.6 | 99.55% |
| Bank of Baroda | 81.7 | 99.64% |
| Union Bank of India | 70.9 | 99.43% |
| ICICI Bank | 63.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 491.2 | 99.14% | 231 ms |
| Google Pay | 336.3 | 99.17% | 316 ms |
| Paytm | 83.1 | 99.06% | 192 ms |
| Navi | 37.9 | 99.17% | 225 ms |
| SuperMoney | 20.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 386.1 |
| Person to Person | 365.5 |
| QR Payments | 97.8 |
| UPI Lite | 49.4 |
| UPI Autopay | 34.0 |

## Failure analysis
- INC-2026-12 — merchant settlement delay on State Bank of India (day 1 of 5); see RCA-2026-12.

## Recommendations
Stay on the open incident: keep recovery monitoring on State Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D100-MON) and any meetings/emails on 29 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D100-MON, RPT-D99-DAILY, INC-2026-12, RCA-2026-12

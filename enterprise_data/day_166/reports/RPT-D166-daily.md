---
id: RPT-D166-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-04T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 04 Dec 2026)

**Report ID:** RPT-D166-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 04 Dec 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 166 of 180)

## Transaction summary
The rail processed 1011.2M UPI transactions on Friday — a steady mid-week day — up 10.2M on the same day last week. Success landed at 99.93% and settlement at 99.98%, held back by live issues on QR Payments (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1011.2  (▼15.3 d/d, ▲10.2 w/w, ▲266.3 m/m)
- **Success Rate:** 99.93%  (▼0.05 d/d, ▲0.65 w/w, ▲0.33 m/m)
- **Settlement Success:** 99.98%  (▲0.5 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.36%  (▲0.12 d/d, ▲0.12 w/w, ▼0.09 m/m)
- **Business Declines:** 0.13%  (▼0.01 w/w, ▼0.07 m/m)
- **Customer Complaints:** 1,156  (▲259 d/d, ▲230 w/w, ▼786 m/m)
- **Merchant Complaints:** 89  (▼1 d/d, ▼4 w/w, ▼122 m/m)
- **Fraud Alerts:** 694  (▼8 d/d, ▼18 w/w, ▼357 m/m)
- **Risk Score:** 18  (▼1 w/w, ▼13 m/m)
- **Response Time:** 584 ms  (▲46 d/d, ▲41 w/w, ▼158 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 325.1 | 99.5% |
| HDFC Bank | 111.6 | 99.55% |
| Bank of Baroda | 80.2 | 99.64% |
| Union Bank of India | 69.7 | 99.43% |
| ICICI Bank | 62.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 482.4 | 99.14% | 231 ms |
| Google Pay | 330.3 | 99.17% | 316 ms |
| Paytm | 81.6 | 99.06% | 192 ms |
| Navi | 37.3 | 99.17% | 225 ms |
| SuperMoney | 19.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 379.2 |
| Person to Person | 359.0 |
| QR Payments | 96.1 |
| UPI Lite | 48.5 |
| UPI Autopay | 33.4 |

## Failure analysis
- INC-2026-21 — feature-level degradation on QR Payments (day 1 of 5); see RCA-2026-21.

## Recommendations
Stay on the open incident: keep recovery monitoring on QR Payments and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D166-MON) and any meetings/emails on 04 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D166-MON, RPT-D165-DAILY, INC-2026-21, RCA-2026-21

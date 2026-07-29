---
id: RPT-D171-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-09T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 09 Dec 2026)

**Report ID:** RPT-D171-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 09 Dec 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 171 of 180)

## Transaction summary
The rail processed 1036.3M UPI transactions on Wednesday — a steady mid-week day — up 1.8M on the same day last week. Success landed at 99.98% and settlement at 99.75%, held back by live issues on Bank of Baroda (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1036.3  (▼13.7 d/d, ▲1.8 w/w, ▲291.4 m/m)
- **Success Rate:** 99.98%  (▲0.38 m/m)
- **Settlement Success:** 99.75%  (▲0.25 d/d, ▼0.23 w/w, ▲0.32 m/m)
- **Technical Declines:** 0.24%  (▼0.21 m/m)
- **Business Declines:** 0.17%  (▲0.04 d/d, ▲0.04 w/w, ▼0.03 m/m)
- **Customer Complaints:** 986  (▲87 d/d, ▲87 w/w, ▼956 m/m)
- **Merchant Complaints:** 156  (▲68 d/d, ▲66 w/w, ▼55 m/m)
- **Fraud Alerts:** 694  (▲7 d/d, ▼4 w/w, ▼357 m/m)
- **Risk Score:** 18  (▼1 w/w, ▼13 m/m)
- **Response Time:** 534 ms  (▼11 d/d, ▼7 w/w, ▼208 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 333.2 | 99.5% |
| HDFC Bank | 114.3 | 99.55% |
| Bank of Baroda | 82.2 | 98.92% |
| Union Bank of India | 71.4 | 99.43% |
| ICICI Bank | 63.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 494.4 | 99.14% | 231 ms |
| Google Pay | 338.5 | 99.17% | 316 ms |
| Paytm | 83.6 | 99.06% | 192 ms |
| Navi | 38.2 | 99.17% | 225 ms |
| SuperMoney | 20.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 388.6 |
| Person to Person | 367.9 |
| QR Payments | 98.4 |
| UPI Lite | 49.7 |
| UPI Autopay | 34.2 |

## Failure analysis
- INC-2026-15 — merchant settlement delay on Bank of Baroda (day 1 of 4); see RCA-2026-15.

## Recommendations
Stay on the open incident: keep recovery monitoring on Bank of Baroda and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D171-MON) and any meetings/emails on 09 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D171-MON, RPT-D170-DAILY, INC-2026-15, RCA-2026-15

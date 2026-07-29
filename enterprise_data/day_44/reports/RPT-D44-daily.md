---
id: RPT-D44-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-04T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 04 Aug 2026)

**Report ID:** RPT-D44-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 04 Aug 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 44 of 180)

## Transaction summary
The rail processed 808.4M UPI transactions on Tuesday — a steady mid-week day — down 108.2M on the same day last week. Success landed at 99.78% and settlement at 99.43%, held back by live issues on Yes Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 808.4  (▲32.5 d/d, ▼108.2 w/w, ▲63.5 m/m)
- **Success Rate:** 99.78%  (▲1.05 d/d, ▲1.14 w/w, ▲0.18 m/m)
- **Settlement Success:** 99.43%  (▼0.36 d/d, ▲1.11 w/w)
- **Technical Declines:** 0.38%  (▼0.01 d/d, ▼0.03 w/w, ▼0.07 m/m)
- **Business Declines:** 0.21%  (▼0.02 d/d, ▼0.03 w/w, ▲0.01 m/m)
- **Customer Complaints:** 1,726  (▼70 d/d, ▼201 w/w, ▼216 m/m)
- **Merchant Complaints:** 247  (▼55 d/d, ▼67 w/w, ▲36 m/m)
- **Fraud Alerts:** 949  (▲11 d/d, ▼6 w/w, ▼102 m/m)
- **Risk Score:** 27  (▼4 m/m)
- **Response Time:** 679 ms  (▲3 d/d, ▼24 w/w, ▼63 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 259.9 | 99.5% |
| HDFC Bank | 89.2 | 99.55% |
| Bank of Baroda | 64.1 | 99.64% |
| Union Bank of India | 55.7 | 99.43% |
| ICICI Bank | 49.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 385.7 | 99.14% | 231 ms |
| Google Pay | 264.1 | 99.17% | 316 ms |
| Paytm | 65.2 | 99.06% | 192 ms |
| Navi | 29.8 | 99.17% | 225 ms |
| SuperMoney | 15.8 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 303.1 |
| Person to Person | 287.0 |
| QR Payments | 76.8 |
| UPI Lite | 38.8 |
| UPI Autopay | 26.7 |

## Failure analysis
- INC-2026-07 — merchant settlement delay on Yes Bank (day 2 of 2); see INC-2026-07.

## Recommendations
Stay on the open incident: keep recovery monitoring on Yes Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D44-MON) and any meetings/emails on 04 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D44-MON, RPT-D43-DAILY, INC-2026-07

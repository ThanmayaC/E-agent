---
id: RPT-D135-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-03T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 03 Nov 2026)

**Report ID:** RPT-D135-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 03 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 135 of 180)

## Transaction summary
The rail processed 985.0M UPI transactions on Tuesday — a steady mid-week day — down 1.5M on the same day last week. Success landed at 99.21% and settlement at 99.98%, held back by live issues on Bank of Baroda (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 985.0  (▲38.3 d/d, ▼1.5 w/w, ▲240.1 m/m)
- **Success Rate:** 99.21%  (▲0.2 d/d, ▼0.77 w/w, ▼0.39 m/m)
- **Settlement Success:** 99.98%  (▲0.11 d/d, ▲0.26 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.27%  (▼0.1 w/w, ▼0.18 m/m)
- **Business Declines:** 0.19%  (▲0.05 d/d, ▲0.04 w/w, ▼0.01 m/m)
- **Customer Complaints:** 1,170  (▲134 d/d, ▼149 w/w, ▼772 m/m)
- **Merchant Complaints:** 187  (▲82 d/d, ▲36 w/w, ▼24 m/m)
- **Fraud Alerts:** 759  (▲1 d/d, ▼13 w/w, ▼292 m/m)
- **Risk Score:** 20  (▼1 w/w, ▼11 m/m)
- **Response Time:** 576 ms  (▼2 d/d, ▼41 w/w, ▼166 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 316.7 | 99.5% |
| HDFC Bank | 108.7 | 99.55% |
| Bank of Baroda | 78.1 | 98.92% |
| Union Bank of India | 67.9 | 99.43% |
| ICICI Bank | 60.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 469.9 | 99.14% | 231 ms |
| Google Pay | 321.7 | 99.17% | 316 ms |
| Paytm | 79.5 | 99.06% | 192 ms |
| Navi | 36.3 | 99.17% | 225 ms |
| SuperMoney | 19.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 369.4 |
| Person to Person | 349.7 |
| QR Payments | 93.6 |
| UPI Lite | 47.3 |
| UPI Autopay | 32.5 |

## Failure analysis
- INC-2026-20 — merchant settlement delay on Bank of Baroda (day 1 of 2); see INC-2026-20.

## Recommendations
Stay on the open incident: keep recovery monitoring on Bank of Baroda and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D135-MON) and any meetings/emails on 03 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D135-MON, RPT-D134-DAILY, INC-2026-20

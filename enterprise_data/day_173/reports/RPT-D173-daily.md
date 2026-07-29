---
id: RPT-D173-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-11T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 11 Dec 2026)

**Report ID:** RPT-D173-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 11 Dec 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 173 of 180)

## Transaction summary
The rail processed 1302.9M UPI transactions on Friday — a campaign-driven high-volume day — up 291.7M on the same day last week. Success landed at 99.18% and settlement at 99.88%, held back by live issues on Bank of Baroda (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1302.9  (▲250.2 d/d, ▲291.7 w/w, ▲558.0 m/m)
- **Success Rate:** 99.18%  (▼0.8 d/d, ▼0.75 w/w, ▼0.42 m/m)
- **Settlement Success:** 99.88%  (▲0.33 d/d, ▼0.1 w/w, ▲0.45 m/m)
- **Technical Declines:** 0.23%  (▼0.13 w/w, ▼0.22 m/m)
- **Business Declines:** 0.14%  (▼0.01 d/d, ▲0.01 w/w, ▼0.06 m/m)
- **Customer Complaints:** 893  (▼34 d/d, ▼263 w/w, ▼1049 m/m)
- **Merchant Complaints:** 110  (▼19 d/d, ▲21 w/w, ▼101 m/m)
- **Fraud Alerts:** 687  (▼5 d/d, ▼7 w/w, ▼364 m/m)
- **Risk Score:** 18  (▼13 m/m)
- **Response Time:** 540 ms  (▲5 d/d, ▼44 w/w, ▼202 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 418.9 | 99.5% |
| HDFC Bank | 143.7 | 99.55% |
| Bank of Baroda | 103.3 | 99.39% |
| Union Bank of India | 89.8 | 99.43% |
| ICICI Bank | 80.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 621.6 | 99.14% | 231 ms |
| Google Pay | 425.6 | 99.17% | 316 ms |
| Paytm | 105.1 | 99.06% | 192 ms |
| Navi | 48.0 | 99.17% | 225 ms |
| SuperMoney | 25.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 488.6 |
| Person to Person | 462.5 |
| QR Payments | 123.8 |
| UPI Lite | 62.5 |
| UPI Autopay | 43.0 |

## Failure analysis
- INC-2026-15 — merchant settlement delay on Bank of Baroda (day 3 of 4); see RCA-2026-15.

## Recommendations
Stay on the open incident: keep recovery monitoring on Bank of Baroda and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D173-MON) and any meetings/emails on 11 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D173-MON, RPT-D172-DAILY, INC-2026-15, RCA-2026-15

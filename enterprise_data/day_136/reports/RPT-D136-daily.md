---
id: RPT-D136-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-04T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 04 Nov 2026)

**Report ID:** RPT-D136-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 04 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 136 of 180)

## Transaction summary
The rail processed 949.0M UPI transactions on Wednesday — a steady mid-week day — down 119.1M on the same day last week. Success landed at 99.58% and settlement at 99.8%, held back by live issues on Bank of Baroda (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 949.0  (▼36.0 d/d, ▼119.1 w/w, ▲204.1 m/m)
- **Success Rate:** 99.58%  (▲0.37 d/d, ▲1.17 w/w, ▼0.02 m/m)
- **Settlement Success:** 99.8%  (▼0.18 d/d, ▼0.09 w/w, ▲0.37 m/m)
- **Technical Declines:** 0.27%  (▼0.05 w/w, ▼0.18 m/m)
- **Business Declines:** 0.17%  (▼0.02 d/d, ▼0.04 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,111  (▼59 d/d, ▼74 w/w, ▼831 m/m)
- **Merchant Complaints:** 154  (▼33 d/d, ▼40 w/w, ▼57 m/m)
- **Fraud Alerts:** 744  (▼15 d/d, ▼14 w/w, ▼307 m/m)
- **Risk Score:** 20  (▼1 w/w, ▼11 m/m)
- **Response Time:** 573 ms  (▼3 d/d, ▼25 w/w, ▼169 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 305.1 | 99.5% |
| HDFC Bank | 104.7 | 99.55% |
| Bank of Baroda | 75.3 | 99.19% |
| Union Bank of India | 65.4 | 99.43% |
| ICICI Bank | 58.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 452.7 | 99.14% | 231 ms |
| Google Pay | 310.0 | 99.17% | 316 ms |
| Paytm | 76.6 | 99.06% | 192 ms |
| Navi | 35.0 | 99.17% | 225 ms |
| SuperMoney | 18.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 355.9 |
| Person to Person | 336.9 |
| QR Payments | 90.2 |
| UPI Lite | 45.6 |
| UPI Autopay | 31.3 |

## Failure analysis
- INC-2026-20 — merchant settlement delay on Bank of Baroda (day 2 of 2); see INC-2026-20.

## Recommendations
Stay on the open incident: keep recovery monitoring on Bank of Baroda and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D136-MON) and any meetings/emails on 04 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D136-MON, RPT-D135-DAILY, INC-2026-20

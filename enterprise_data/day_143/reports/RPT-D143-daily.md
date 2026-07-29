---
id: RPT-D143-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-11T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 11 Nov 2026)

**Report ID:** RPT-D143-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 11 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 143 of 180)

## Transaction summary
The rail processed 1000.9M UPI transactions on Wednesday — a steady mid-week day — up 51.9M on the same day last week. Success landed at 99.74% and settlement at 99.98%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1000.9  (▲6.8 d/d, ▲51.9 w/w, ▲256.0 m/m)
- **Success Rate:** 99.74%  (▲0.74 d/d, ▲0.16 w/w, ▲0.14 m/m)
- **Settlement Success:** 99.98%  (▲0.18 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.27%  (▼0.01 d/d, ▼0.18 m/m)
- **Business Declines:** 0.14%  (▼0.03 w/w, ▼0.06 m/m)
- **Customer Complaints:** 1,007  (▼40 d/d, ▼104 w/w, ▼935 m/m)
- **Merchant Complaints:** 101  (▼53 w/w, ▼110 m/m)
- **Fraud Alerts:** 732  (▼11 d/d, ▼12 w/w, ▼319 m/m)
- **Risk Score:** 20  (▼11 m/m)
- **Response Time:** 574 ms  (▼3 d/d, ▲1 w/w, ▼168 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 321.8 | 99.5% |
| HDFC Bank | 110.4 | 99.55% |
| Bank of Baroda | 79.4 | 99.64% |
| Union Bank of India | 69.0 | 99.43% |
| ICICI Bank | 61.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 477.5 | 99.14% | 231 ms |
| Google Pay | 326.9 | 99.17% | 316 ms |
| Paytm | 80.7 | 99.06% | 192 ms |
| Navi | 36.9 | 99.17% | 225 ms |
| SuperMoney | 19.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 375.3 |
| Person to Person | 355.3 |
| QR Payments | 95.1 |
| UPI Lite | 48.0 |
| UPI Autopay | 33.0 |

## Failure analysis
- INC-2026-25 — PSP callback latency increase on BHIM (day 5 of 5); see RCA-2026-25.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D143-MON) and any meetings/emails on 11 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D143-MON, RPT-D142-DAILY, INC-2026-25, RCA-2026-25

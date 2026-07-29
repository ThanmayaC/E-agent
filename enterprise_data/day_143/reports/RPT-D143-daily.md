---
id: RPT-D143-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-27T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 27 May 2026)

**Report ID:** RPT-D143-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 27 May 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 143 of 206)

## Transaction summary
The rail processed 712.3M UPI transactions on Wednesday — a steady mid-week day — down 155.7M on the same day last week. Success landed at 99.59% and settlement at 99.98%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 712.3  (▼10.5 d/d, ▼155.7 w/w, ▼83.6 m/m)
- **Success Rate:** 99.59%  (▲0.86 d/d, ▲0.41 w/w, ▲0.46 m/m)
- **Settlement Success:** 99.98%  (▲0.03 m/m)
- **Technical Declines:** 0.32%  (▼0.01 w/w, ▼0.23 m/m)
- **Business Declines:** 0.19%  (▼0.02 d/d, ▲0.02 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,157  (▼87 d/d, ▲23 w/w, ▼985 m/m)
- **Merchant Complaints:** 113  (▼1 d/d, ▼3 w/w, ▼121 m/m)
- **Fraud Alerts:** 859  (▼43 d/d, ▲31 w/w, ▼301 m/m)
- **Risk Score:** 25  (▼3 d/d, ▲3 w/w, ▼9 m/m)
- **Response Time:** 586 ms  (▼2 d/d, ▼2 w/w, ▼167 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 231.9 | 99.67% |
| HDFC Bank | 76.2 | 99.42% |
| Bank of Baroda | 54.8 | 99.26% |
| Union Bank of India | 48.1 | 99.63% |
| Axis Bank | 43.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 340.2 | 99.51% | 198 ms |
| Google Pay | 232.9 | 99.35% | 241 ms |
| Paytm | 56.5 | 99.53% | 201 ms |
| Navi | 26.2 | 99.53% | 304 ms |
| SuperMoney | 13.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 263.6 |
| Person to Person | 252.9 |
| QR Payments | 67.7 |
| UPI Lite | 34.2 |
| UPI Autopay | 23.5 |

## Failure analysis
- INC-2026-18 — fraud / risk spike on BHIM (day 4 of 4); see RCA-2026-18.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D143-MON) and any meetings/emails on 27 May.

Refs: upi_kpis_month.xlsx, TEAMS-D143-MON, RPT-D142-DAILY, INC-2026-18, RCA-2026-18

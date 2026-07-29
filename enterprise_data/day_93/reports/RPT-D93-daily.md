---
id: RPT-D93-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-07T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 07 Apr 2026)

**Report ID:** RPT-D93-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 07 Apr 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 93 of 206)

## Transaction summary
The rail processed 691.1M UPI transactions on Tuesday — a steady mid-week day — down 96.4M on the same day last week. Success landed at 99.01% and settlement at 99.84%, held back by live issues on State Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 691.1  (▼5.4 d/d, ▼96.4 w/w, ▼104.8 m/m)
- **Success Rate:** 99.01%  (▲0.84 d/d, ▲0.34 w/w, ▼0.12 m/m)
- **Settlement Success:** 99.84%  (▲0.51 d/d, ▼0.14 w/w, ▼0.11 m/m)
- **Technical Declines:** 0.64%  (▼0.16 d/d, ▲0.25 w/w, ▲0.09 m/m)
- **Business Declines:** 0.19%  (▼0.05 m/m)
- **Customer Complaints:** 1,985  (▼380 d/d, ▲550 w/w, ▼157 m/m)
- **Merchant Complaints:** 244  (▼64 d/d, ▲92 w/w, ▲10 m/m)
- **Fraud Alerts:** 918  (▲3 d/d, ▼21 w/w, ▼242 m/m)
- **Risk Score:** 26  (▼8 m/m)
- **Response Time:** 704 ms  (▼47 d/d, ▲49 w/w, ▼49 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 225.0 | 98.3% |
| HDFC Bank | 73.9 | 99.42% |
| Bank of Baroda | 53.2 | 99.26% |
| Union Bank of India | 46.6 | 99.63% |
| Axis Bank | 42.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 330.1 | 99.51% | 198 ms |
| Google Pay | 226.0 | 99.35% | 241 ms |
| Paytm | 54.8 | 99.53% | 201 ms |
| Navi | 25.4 | 99.53% | 304 ms |
| SuperMoney | 13.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 255.7 |
| Person to Person | 245.3 |
| QR Payments | 65.7 |
| UPI Lite | 33.2 |
| UPI Autopay | 22.8 |

## Failure analysis
- INC-2026-04 — bank timeout / 5xx spike on State Bank of India (day 2 of 4); see RCA-2026-04.

## Recommendations
Stay on the open incident: keep recovery monitoring on State Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D93-MON) and any meetings/emails on 07 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D93-MON, RPT-D92-DAILY, INC-2026-04, RCA-2026-04

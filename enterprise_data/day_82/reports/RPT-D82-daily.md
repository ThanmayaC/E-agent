---
id: RPT-D82-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-27T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 27 Mar 2026)

**Report ID:** RPT-D82-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 27 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 82 of 206)

## Transaction summary
The rail processed 694.6M UPI transactions on Friday — a steady mid-week day — down 3.8M on the same day last week. Success landed at 99.98% and settlement at 99.98%, held back by live issues on RuPay Credit on UPI (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 694.6  (▲2.6 d/d, ▼3.8 w/w, ▼101.3 m/m)
- **Success Rate:** 99.98%  (▲0.72 d/d, ▲0.03 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.03 m/m)
- **Technical Declines:** 0.47%  (▼0.06 d/d, ▲0.06 w/w, ▼0.08 m/m)
- **Business Declines:** 0.2%  (▼0.04 m/m)
- **Customer Complaints:** 1,627  (▼122 d/d, ▲96 w/w, ▼515 m/m)
- **Merchant Complaints:** 155  (▼1 d/d, ▼6 w/w, ▼79 m/m)
- **Fraud Alerts:** 943  (▲1 d/d, ▼5 w/w, ▼217 m/m)
- **Risk Score:** 26  (▼1 w/w, ▼8 m/m)
- **Response Time:** 665 ms  (▼15 d/d, ▼3 w/w, ▼88 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 226.1 | 99.67% |
| HDFC Bank | 74.3 | 99.42% |
| Bank of Baroda | 53.5 | 99.26% |
| Union Bank of India | 46.9 | 99.63% |
| Axis Bank | 42.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 331.8 | 99.51% | 198 ms |
| Google Pay | 227.2 | 99.35% | 241 ms |
| Paytm | 55.1 | 99.53% | 201 ms |
| Navi | 25.5 | 99.53% | 304 ms |
| SuperMoney | 13.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 257.0 |
| Person to Person | 246.6 |
| QR Payments | 66.0 |
| UPI Lite | 33.3 |
| UPI Autopay | 22.9 |

## Failure analysis
- INC-2026-21 — feature-level degradation on RuPay Credit on UPI (day 3 of 4); see RCA-2026-21.

## Recommendations
Stay on the open incident: keep recovery monitoring on RuPay Credit on UPI and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D82-MON) and any meetings/emails on 27 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D82-MON, RPT-D81-DAILY, INC-2026-21, RCA-2026-21

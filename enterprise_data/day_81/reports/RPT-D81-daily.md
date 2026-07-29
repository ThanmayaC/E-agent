---
id: RPT-D81-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-26T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 26 Mar 2026)

**Report ID:** RPT-D81-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Thursday 26 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 81 of 206)

## Transaction summary
The rail processed 692.0M UPI transactions on Thursday — a steady mid-week day — down 5.1M on the same day last week. Success landed at 99.26% and settlement at 99.98%, held back by live issues on RuPay Credit on UPI (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 692.0  (▲6.9 d/d, ▼5.1 w/w, ▼103.9 m/m)
- **Success Rate:** 99.26%  (▼0.3 d/d, ▼0.37 w/w, ▲0.13 m/m)
- **Settlement Success:** 99.98%  (▲1.04 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.53%  (▼0.07 d/d, ▲0.12 w/w, ▼0.02 m/m)
- **Business Declines:** 0.2%  (▼0.04 m/m)
- **Customer Complaints:** 1,749  (▼167 d/d, ▲234 w/w, ▼393 m/m)
- **Merchant Complaints:** 156  (▲1 d/d, ▼5 w/w, ▼78 m/m)
- **Fraud Alerts:** 942  (▲7 d/d, ▼20 w/w, ▼218 m/m)
- **Risk Score:** 26  (▼1 d/d, ▼1 w/w, ▼8 m/m)
- **Response Time:** 680 ms  (▼22 d/d, ▲22 w/w, ▼73 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 225.2 | 99.67% |
| HDFC Bank | 74.0 | 99.42% |
| Bank of Baroda | 53.3 | 99.26% |
| Union Bank of India | 46.7 | 99.63% |
| Axis Bank | 42.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 330.5 | 99.51% | 198 ms |
| Google Pay | 226.3 | 99.35% | 241 ms |
| Paytm | 54.9 | 99.53% | 201 ms |
| Navi | 25.4 | 99.53% | 304 ms |
| SuperMoney | 13.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 256.0 |
| Person to Person | 245.7 |
| QR Payments | 65.7 |
| UPI Lite | 33.2 |
| UPI Autopay | 22.8 |

## Failure analysis
- INC-2026-21 — feature-level degradation on RuPay Credit on UPI (day 2 of 4); see RCA-2026-21.

## Recommendations
Stay on the open incident: keep recovery monitoring on RuPay Credit on UPI and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D81-MON) and any meetings/emails on 26 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D81-MON, RPT-D80-DAILY, INC-2026-21, RCA-2026-21

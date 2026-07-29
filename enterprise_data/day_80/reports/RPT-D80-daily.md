---
id: RPT-D80-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-25T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 25 Mar 2026)

**Report ID:** RPT-D80-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 25 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 80 of 206)

## Transaction summary
The rail processed 685.1M UPI transactions on Wednesday — a steady mid-week day — down 19.1M on the same day last week. Success landed at 99.56% and settlement at 98.94%, held back by live issues on RuPay Credit on UPI (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 685.1  (▼8.6 d/d, ▼19.1 w/w, ▼110.8 m/m)
- **Success Rate:** 99.56%  (▲0.38 d/d, ▼0.42 w/w, ▲0.43 m/m)
- **Settlement Success:** 98.94%  (▼0.47 d/d, ▼1.04 w/w, ▼1.01 m/m)
- **Technical Declines:** 0.6%  (▲0.11 d/d, ▲0.18 w/w, ▲0.05 m/m)
- **Business Declines:** 0.2%  (▼0.04 m/m)
- **Customer Complaints:** 1,916  (▲191 d/d, ▲389 w/w, ▼226 m/m)
- **Merchant Complaints:** 155  (▼2 d/d, ▼7 w/w, ▼79 m/m)
- **Fraud Alerts:** 935  (▼14 d/d, ▼36 w/w, ▼225 m/m)
- **Risk Score:** 27  (▼7 m/m)
- **Response Time:** 702 ms  (▼8 d/d, ▲36 w/w, ▼51 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 223.0 | 99.67% |
| HDFC Bank | 73.2 | 99.42% |
| Bank of Baroda | 52.7 | 99.26% |
| Union Bank of India | 46.2 | 99.63% |
| Axis Bank | 42.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 327.2 | 99.51% | 198 ms |
| Google Pay | 224.1 | 99.35% | 241 ms |
| Paytm | 54.3 | 99.53% | 201 ms |
| Navi | 25.2 | 99.53% | 304 ms |
| SuperMoney | 13.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 253.5 |
| Person to Person | 243.2 |
| QR Payments | 65.1 |
| UPI Lite | 32.9 |
| UPI Autopay | 22.6 |

## Failure analysis
- INC-2026-21 — feature-level degradation on RuPay Credit on UPI (day 1 of 4); see RCA-2026-21.

## Recommendations
Stay on the open incident: keep recovery monitoring on RuPay Credit on UPI and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D80-MON) and any meetings/emails on 25 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D80-MON, RPT-D79-DAILY, INC-2026-21, RCA-2026-21

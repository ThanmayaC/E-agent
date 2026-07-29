---
id: RPT-D188-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-11T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 11 Jul 2026)

**Report ID:** RPT-D188-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 11 Jul 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 188 of 206)

## Transaction summary
The rail processed 660.0M UPI transactions on Saturday — a lighter Saturday — down 13.2M on the same day last week. Success landed at 99.98% and settlement at 99.98%, held back by live issues on UPI 123Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 660.0  (▼90.3 d/d, ▼13.2 w/w, ▼135.9 m/m)
- **Success Rate:** 99.98%  (▲0.35 d/d, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.67 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.28%  (▼0.01 d/d, ▼0.27 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 912  (▼29 d/d, ▼7 w/w, ▼1230 m/m)
- **Merchant Complaints:** 89  (▼3 w/w, ▼145 m/m)
- **Fraud Alerts:** 727  (▼3 d/d, ▼7 w/w, ▼433 m/m)
- **Risk Score:** 19  (▼15 m/m)
- **Response Time:** 538 ms  (▼6 d/d, ▼2 w/w, ▼215 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 214.8 | 99.67% |
| HDFC Bank | 70.6 | 99.42% |
| Bank of Baroda | 50.8 | 99.26% |
| Union Bank of India | 44.5 | 99.63% |
| Axis Bank | 40.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 315.3 | 99.51% | 198 ms |
| Google Pay | 215.8 | 99.35% | 241 ms |
| Paytm | 52.4 | 99.53% | 201 ms |
| Navi | 24.3 | 99.53% | 304 ms |
| SuperMoney | 12.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 244.2 |
| Person to Person | 234.3 |
| QR Payments | 62.7 |
| UPI Lite | 31.7 |
| UPI Autopay | 21.8 |

## Failure analysis
- INC-2026-10 — feature-level degradation on UPI 123Pay (day 5 of 5); see RCA-2026-10.

## Recommendations
Stay on the open incident: keep recovery monitoring on UPI 123Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D188-MON) and any meetings/emails on 11 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D188-MON, RPT-D187-DAILY, INC-2026-10, RCA-2026-10

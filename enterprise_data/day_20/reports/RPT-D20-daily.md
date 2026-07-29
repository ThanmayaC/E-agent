---
id: RPT-D20-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-24T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 24 Jan 2026)

**Report ID:** RPT-D20-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 24 Jan 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 20 of 206)

## Transaction summary
The rail processed 586.8M UPI transactions on Saturday — a lighter Saturday — down 24.5M on the same day last week. Success landed at 98.52% and settlement at 99.67%, held back by live issues on UPI Lite (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 586.8  (▼68.9 d/d, ▼24.5 w/w, ▼209.1 m/m)
- **Success Rate:** 98.52%  (▼0.09 d/d, ▲0.17 w/w, ▼0.61 m/m)
- **Settlement Success:** 99.67%  (▼0.18 d/d, ▼0.26 w/w, ▼0.28 m/m)
- **Technical Declines:** 0.59%  (▼0.08 d/d, ▲0.06 w/w, ▲0.04 m/m)
- **Business Declines:** 0.23%  (▼0.01 m/m)
- **Customer Complaints:** 2,166  (▼179 d/d, ▲126 w/w, ▲24 m/m)
- **Merchant Complaints:** 213  (▼6 w/w, ▼21 m/m)
- **Fraud Alerts:** 1,101  (▲10 d/d, ▼4 w/w, ▼59 m/m)
- **Risk Score:** 32  (▼1 w/w, ▼2 m/m)
- **Response Time:** 758 ms  (▼5 d/d, ▲22 w/w, ▲5 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 191.0 | 99.67% |
| HDFC Bank | 62.7 | 99.42% |
| Bank of Baroda | 45.2 | 99.26% |
| Union Bank of India | 39.6 | 99.63% |
| Axis Bank | 36.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 280.3 | 99.51% | 198 ms |
| Google Pay | 191.9 | 99.35% | 241 ms |
| Paytm | 46.5 | 99.53% | 201 ms |
| Navi | 21.6 | 99.53% | 304 ms |
| SuperMoney | 11.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 217.1 |
| Person to Person | 208.3 |
| QR Payments | 55.7 |
| UPI Lite | 28.2 |
| UPI Autopay | 19.4 |

## Failure analysis
- INC-2026-24 — feature-level degradation on UPI Lite (day 3 of 3); see RCA-2026-24.

## Recommendations
Stay on the open incident: keep recovery monitoring on UPI Lite and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D20-MON) and any meetings/emails on 24 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D20-MON, RPT-D19-DAILY, INC-2026-24, RCA-2026-24

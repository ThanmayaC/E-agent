---
id: RPT-D51-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-24T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 24 Feb 2026)

**Report ID:** RPT-D51-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 24 Feb 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 51 of 206)

## Transaction summary
The rail processed 830.0M UPI transactions on Tuesday — a campaign-driven high-volume day — up 144.2M on the same day last week. Success landed at 99.29% and settlement at 99.98%, held back by live issues on Google Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 830.0  (▲172.6 d/d, ▲144.2 w/w, ▲34.1 m/m)
- **Success Rate:** 99.29%  (▼0.07 d/d, ▼0.69 w/w, ▲0.16 m/m)
- **Settlement Success:** 99.98%  (▲0.81 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.45%  (▼0.01 d/d, ▼0.02 w/w, ▼0.1 m/m)
- **Business Declines:** 0.31%  (▼0.06 d/d, ▲0.09 w/w, ▲0.07 m/m)
- **Customer Complaints:** 2,056  (▼236 d/d, ▲285 w/w, ▼86 m/m)
- **Merchant Complaints:** 181  (▼2 d/d, ▼6 w/w, ▼53 m/m)
- **Fraud Alerts:** 1,234  (▼124 d/d, ▲201 w/w, ▲74 m/m)
- **Risk Score:** 44  (▼10 d/d, ▲14 w/w, ▲10 m/m)
- **Response Time:** 696 ms  (▲3 d/d, ▼57 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 270.2 | 99.67% |
| HDFC Bank | 88.7 | 99.42% |
| Bank of Baroda | 63.9 | 99.26% |
| Union Bank of India | 56.0 | 99.63% |
| Axis Bank | 51.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 396.5 | 99.51% | 198 ms |
| Google Pay | 271.4 | 98.73% | 480 ms |
| Paytm | 65.8 | 99.53% | 201 ms |
| Navi | 30.5 | 99.53% | 304 ms |
| SuperMoney | 16.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 307.1 |
| Person to Person | 294.6 |
| QR Payments | 78.8 |
| UPI Lite | 39.8 |
| UPI Autopay | 27.4 |

## Failure analysis
- INC-2026-19 — fraud / risk spike on Google Pay (day 2 of 3); see RCA-2026-19.

## Recommendations
Stay on the open incident: keep recovery monitoring on Google Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D51-MON) and any meetings/emails on 24 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D51-MON, RPT-D50-DAILY, INC-2026-19, RCA-2026-19

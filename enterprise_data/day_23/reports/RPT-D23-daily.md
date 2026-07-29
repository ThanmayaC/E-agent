---
id: RPT-D23-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-27T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 27 Jan 2026)

**Report ID:** RPT-D23-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 27 Jan 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 23 of 206)

## Transaction summary
The rail processed 674.7M UPI transactions on Tuesday — a steady mid-week day — up 5.5M on the same day last week. Success landed at 99.32% and settlement at 99.98%, held back by live issues on FamApp (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 674.7  (▲11.4 d/d, ▲5.5 w/w, ▼121.2 m/m)
- **Success Rate:** 99.32%  (▲1.23 d/d, ▼0.04 w/w, ▲0.19 m/m)
- **Settlement Success:** 99.98%  (▲0.11 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.51%  (▼0.01 w/w, ▼0.04 m/m)
- **Business Declines:** 0.34%  (▼0.06 d/d, ▲0.11 w/w, ▲0.1 m/m)
- **Customer Complaints:** 2,348  (▼261 d/d, ▲330 w/w, ▲206 m/m)
- **Merchant Complaints:** 209  (▼10 w/w, ▼25 m/m)
- **Fraud Alerts:** 1,324  (▼131 d/d, ▲213 w/w, ▲164 m/m)
- **Risk Score:** 48  (▼11 d/d, ▲16 w/w, ▲14 m/m)
- **Response Time:** 735 ms  (▲7 d/d, ▼10 w/w, ▼18 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 219.6 | 99.67% |
| HDFC Bank | 72.1 | 99.42% |
| Bank of Baroda | 51.9 | 99.26% |
| Union Bank of India | 45.5 | 99.63% |
| Axis Bank | 41.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 322.3 | 99.51% | 198 ms |
| Google Pay | 220.7 | 99.35% | 241 ms |
| Paytm | 53.5 | 99.53% | 201 ms |
| Navi | 24.8 | 99.53% | 304 ms |
| SuperMoney | 13.2 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 249.6 |
| Person to Person | 239.5 |
| QR Payments | 64.1 |
| UPI Lite | 32.4 |
| UPI Autopay | 22.3 |

## Failure analysis
- INC-2026-15 — fraud / risk spike on FamApp (day 2 of 3); see RCA-2026-15.

## Recommendations
Stay on the open incident: keep recovery monitoring on FamApp and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D23-MON) and any meetings/emails on 27 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D23-MON, RPT-D22-DAILY, INC-2026-15, RCA-2026-15

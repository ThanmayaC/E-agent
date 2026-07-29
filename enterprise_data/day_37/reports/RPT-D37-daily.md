---
id: RPT-D37-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-10T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 10 Feb 2026)

**Report ID:** RPT-D37-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 10 Feb 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 37 of 206)

## Transaction summary
The rail processed 681.3M UPI transactions on Tuesday — a steady mid-week day — up 11.3M on the same day last week. Success landed at 99.93% and settlement at 99.57%, held back by live issues on WhatsApp Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 681.3  (▲36.8 d/d, ▲11.3 w/w, ▼114.6 m/m)
- **Success Rate:** 99.93%  (▲0.98 d/d, ▲0.39 w/w, ▲0.8 m/m)
- **Settlement Success:** 99.57%  (▲0.86 d/d, ▲0.22 w/w, ▼0.38 m/m)
- **Technical Declines:** 0.48%  (▼0.02 w/w, ▼0.07 m/m)
- **Business Declines:** 0.24%  (▼0.01 d/d, ▲0.02 w/w)
- **Customer Complaints:** 1,862  (▼74 d/d, ▲1 w/w, ▼280 m/m)
- **Merchant Complaints:** 194  (▼2 d/d, ▼8 w/w, ▼40 m/m)
- **Fraud Alerts:** 1,079  (▼55 d/d, ▼1 w/w, ▼81 m/m)
- **Risk Score:** 33  (▼3 d/d, ▲2 w/w, ▼1 m/m)
- **Response Time:** 709 ms  (▼6 d/d, ▼5 w/w, ▼44 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 221.8 | 99.67% |
| HDFC Bank | 72.8 | 99.42% |
| Bank of Baroda | 52.4 | 99.26% |
| Union Bank of India | 46.0 | 99.63% |
| Axis Bank | 42.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 325.4 | 99.51% | 198 ms |
| Google Pay | 222.8 | 99.35% | 241 ms |
| Paytm | 54.0 | 99.53% | 201 ms |
| Navi | 25.0 | 99.53% | 304 ms |
| SuperMoney | 13.3 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 252.1 |
| Person to Person | 241.9 |
| QR Payments | 64.7 |
| UPI Lite | 32.7 |
| UPI Autopay | 22.5 |

## Failure analysis
- INC-2026-08 — fraud / risk spike on WhatsApp Pay (day 4 of 5); see RCA-2026-08.

## Recommendations
Stay on the open incident: keep recovery monitoring on WhatsApp Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D37-MON) and any meetings/emails on 10 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D37-MON, RPT-D36-DAILY, INC-2026-08, RCA-2026-08

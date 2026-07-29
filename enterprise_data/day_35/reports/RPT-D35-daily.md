---
id: RPT-D35-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-08T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 08 Feb 2026)

**Report ID:** RPT-D35-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 08 Feb 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 35 of 206)

## Transaction summary
The rail processed 562.4M UPI transactions on Sunday — a quiet Sunday — up 14.0M on the same day last week. Success landed at 99.66% and settlement at 99.52%, held back by live issues on HDFC MobileBanking, WhatsApp Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 562.4  (▼47.4 d/d, ▲14.0 w/w, ▼233.5 m/m)
- **Success Rate:** 99.66%  (▲0.79 d/d, ▼0.32 w/w, ▲0.53 m/m)
- **Settlement Success:** 99.52%  (▼0.46 d/d, ▼0.46 w/w, ▼0.43 m/m)
- **Technical Declines:** 0.48%  (▼0.01 d/d, ▼0.02 w/w, ▼0.07 m/m)
- **Business Declines:** 0.3%  (▼0.05 d/d, ▲0.08 w/w, ▲0.06 m/m)
- **Customer Complaints:** 2,095  (▼235 d/d, ▲207 w/w, ▼47 m/m)
- **Merchant Complaints:** 197  (▼2 d/d, ▼5 w/w, ▼37 m/m)
- **Fraud Alerts:** 1,212  (▼108 d/d, ▲146 w/w, ▲52 m/m)
- **Risk Score:** 42  (▼9 d/d, ▲11 w/w, ▲8 m/m)
- **Response Time:** 714 ms  (▼2 d/d, ▼12 w/w, ▼39 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 183.1 | 99.67% |
| HDFC Bank | 60.1 | 99.42% |
| Bank of Baroda | 43.3 | 99.26% |
| Union Bank of India | 37.9 | 99.63% |
| Axis Bank | 34.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 268.6 | 99.51% | 198 ms |
| Google Pay | 183.9 | 99.35% | 241 ms |
| Paytm | 44.6 | 99.53% | 201 ms |
| Navi | 20.7 | 99.53% | 304 ms |
| SuperMoney | 11.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 208.1 |
| Person to Person | 199.7 |
| QR Payments | 53.4 |
| UPI Lite | 27.0 |
| UPI Autopay | 18.6 |

## Failure analysis
- INC-2026-02 — fraud / risk spike on HDFC MobileBanking (day 5 of 5); see RCA-2026-02.
- INC-2026-08 — fraud / risk spike on WhatsApp Pay (day 2 of 5); see RCA-2026-08.

## Recommendations
Stay on the open incidents: keep recovery monitoring on HDFC MobileBanking, WhatsApp Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D35-MON) and any meetings/emails on 08 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D35-MON, RPT-D34-DAILY, INC-2026-02, INC-2026-08, RCA-2026-02, RCA-2026-08

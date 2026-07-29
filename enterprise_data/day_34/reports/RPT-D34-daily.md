---
id: RPT-D34-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-07T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 07 Feb 2026)

**Report ID:** RPT-D34-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 07 Feb 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 34 of 206)

## Transaction summary
The rail processed 609.8M UPI transactions on Saturday — a lighter Saturday — down 145.3M on the same day last week. Success landed at 98.87% and settlement at 99.98%, held back by live issues on HDFC MobileBanking, WhatsApp Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 609.8  (▼62.9 d/d, ▼145.3 w/w, ▼186.1 m/m)
- **Success Rate:** 98.87%  (▼0.54 d/d, ▼0.75 w/w, ▼0.26 m/m)
- **Settlement Success:** 99.98%  (▲1.22 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.49%  (▼0.01 w/w, ▼0.06 m/m)
- **Business Declines:** 0.35%  (▲0.07 d/d, ▲0.12 w/w, ▲0.11 m/m)
- **Customer Complaints:** 2,330  (▲276 d/d, ▲445 w/w, ▲188 m/m)
- **Merchant Complaints:** 199  (▲1 d/d, ▼5 w/w, ▼35 m/m)
- **Fraud Alerts:** 1,320  (▲143 d/d, ▲235 w/w, ▲160 m/m)
- **Risk Score:** 51  (▲11 d/d, ▲20 w/w, ▲17 m/m)
- **Response Time:** 716 ms  (▼3 d/d, ▼5 w/w, ▼37 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 198.5 | 99.67% |
| HDFC Bank | 65.2 | 99.42% |
| Bank of Baroda | 46.9 | 99.26% |
| Union Bank of India | 41.1 | 99.63% |
| Axis Bank | 37.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 291.3 | 99.51% | 198 ms |
| Google Pay | 199.4 | 99.35% | 241 ms |
| Paytm | 48.4 | 99.53% | 201 ms |
| Navi | 22.4 | 99.53% | 304 ms |
| SuperMoney | 11.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 225.6 |
| Person to Person | 216.5 |
| QR Payments | 57.9 |
| UPI Lite | 29.3 |
| UPI Autopay | 20.1 |

## Failure analysis
- INC-2026-02 — fraud / risk spike on HDFC MobileBanking (day 4 of 5); see RCA-2026-02.
- INC-2026-08 — fraud / risk spike on WhatsApp Pay (day 1 of 5); see RCA-2026-08.

## Recommendations
Stay on the open incidents: keep recovery monitoring on HDFC MobileBanking, WhatsApp Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D34-MON) and any meetings/emails on 07 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D34-MON, RPT-D33-DAILY, INC-2026-02, INC-2026-08, RCA-2026-02, RCA-2026-08

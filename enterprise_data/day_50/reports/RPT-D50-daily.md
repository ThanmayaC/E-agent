---
id: RPT-D50-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-23T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 23 Feb 2026)

**Report ID:** RPT-D50-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 23 Feb 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 50 of 206)

## Transaction summary
The rail processed 657.4M UPI transactions on Monday — the Monday ramp-up after the weekend — down 10.7M on the same day last week. Success landed at 99.36% and settlement at 99.17%, held back by live issues on Google Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 657.4  (▲93.4 d/d, ▼10.7 w/w, ▼138.5 m/m)
- **Success Rate:** 99.36%  (▼0.25 d/d, ▲0.49 w/w, ▲0.23 m/m)
- **Settlement Success:** 99.17%  (▲0.54 d/d, ▲0.36 w/w, ▼0.78 m/m)
- **Technical Declines:** 0.46%  (▼0.01 w/w, ▼0.09 m/m)
- **Business Declines:** 0.37%  (▲0.16 d/d, ▲0.15 w/w, ▲0.13 m/m)
- **Customer Complaints:** 2,292  (▲593 d/d, ▲526 w/w, ▲150 m/m)
- **Merchant Complaints:** 183  (▼1 d/d, ▼7 w/w, ▼51 m/m)
- **Fraud Alerts:** 1,358  (▲332 d/d, ▲324 w/w, ▲198 m/m)
- **Risk Score:** 54  (▲25 d/d, ▲24 w/w, ▲20 m/m)
- **Response Time:** 693 ms  (▼14 w/w, ▼60 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 214.0 | 99.67% |
| HDFC Bank | 70.3 | 99.42% |
| Bank of Baroda | 50.6 | 99.26% |
| Union Bank of India | 44.3 | 99.63% |
| Axis Bank | 40.5 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 314.0 | 99.51% | 198 ms |
| Google Pay | 215.0 | 98.35% | 626 ms |
| Paytm | 52.1 | 99.53% | 201 ms |
| Navi | 24.2 | 99.53% | 304 ms |
| SuperMoney | 12.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 243.2 |
| Person to Person | 233.4 |
| QR Payments | 62.5 |
| UPI Lite | 31.6 |
| UPI Autopay | 21.7 |

## Failure analysis
- INC-2026-19 — fraud / risk spike on Google Pay (day 1 of 3); see RCA-2026-19.

## Recommendations
Stay on the open incident: keep recovery monitoring on Google Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D50-MON) and any meetings/emails on 23 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D50-MON, RPT-D49-DAILY, INC-2026-19, RCA-2026-19

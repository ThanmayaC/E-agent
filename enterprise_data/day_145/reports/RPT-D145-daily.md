---
id: RPT-D145-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-29T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 29 May 2026)

**Report ID:** RPT-D145-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 29 May 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 145 of 206)

## Transaction summary
The rail processed 808.9M UPI transactions on Friday — the month-end surge as salary and bill-pay flows land — up 100.1M on the same day last week. Success landed at 99.62% and settlement at 99.5%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 808.9  (▲13.0 d/d, ▲100.1 w/w, ▲13.0 m/m)
- **Success Rate:** 99.62%  (▼0.36 d/d, ▲0.39 w/w, ▲0.49 m/m)
- **Settlement Success:** 99.5%  (▲0.49 d/d, ▼0.39 w/w, ▼0.45 m/m)
- **Technical Declines:** 0.38%  (▼0.04 d/d, ▲0.05 w/w, ▼0.17 m/m)
- **Business Declines:** 0.17%  (▼0.05 w/w, ▼0.07 m/m)
- **Customer Complaints:** 1,268  (▼110 d/d, ▲8 w/w, ▼874 m/m)
- **Merchant Complaints:** 112  (▼94 w/w, ▼122 m/m)
- **Fraud Alerts:** 800  (▼11 d/d, ▼22 w/w, ▼360 m/m)
- **Risk Score:** 22  (▼12 m/m)
- **Response Time:** 625 ms  (▼41 d/d, ▲32 w/w, ▼128 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 263.3 | 99.67% |
| HDFC Bank | 86.5 | 99.42% |
| Bank of Baroda | 62.3 | 99.26% |
| Union Bank of India | 54.6 | 99.63% |
| Axis Bank | 49.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 386.4 | 99.51% | 198 ms |
| Google Pay | 264.5 | 99.35% | 241 ms |
| Paytm | 64.2 | 99.53% | 201 ms |
| Navi | 29.7 | 99.53% | 304 ms |
| SuperMoney | 15.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 299.3 |
| Person to Person | 287.2 |
| QR Payments | 76.8 |
| UPI Lite | 38.8 |
| UPI Autopay | 26.7 |

## Failure analysis
- INC-2026-14 — PSP callback latency increase on BHIM (day 2 of 5); see RCA-2026-14.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D145-MON) and any meetings/emails on 29 May.

Refs: upi_kpis_month.xlsx, TEAMS-D145-MON, RPT-D144-DAILY, INC-2026-14, RCA-2026-14

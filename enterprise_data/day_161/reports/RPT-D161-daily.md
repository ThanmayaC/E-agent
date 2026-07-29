---
id: RPT-D161-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-14T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 14 Jun 2026)

**Report ID:** RPT-D161-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 14 Jun 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 161 of 206)

## Transaction summary
The rail processed 608.1M UPI transactions on Sunday — a quiet Sunday — up 7.2M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 608.1  (▼63.4 d/d, ▲7.2 w/w, ▼187.8 m/m)
- **Success Rate:** 99.98%  (▲0.28 d/d, ▲0.87 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.25 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.3%  (▼0.25 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 1,001  (▼4 d/d, ▼51 w/w, ▼1141 m/m)
- **Merchant Complaints:** 103  (▼1 d/d, ▼2 w/w, ▼131 m/m)
- **Fraud Alerts:** 768  (▼13 d/d, ▼20 w/w, ▼392 m/m)
- **Risk Score:** 21  (▼13 m/m)
- **Response Time:** 569 ms  (▲5 d/d, ▼5 w/w, ▼184 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 197.9 | 99.67% |
| HDFC Bank | 65.0 | 99.42% |
| Bank of Baroda | 46.8 | 99.26% |
| Union Bank of India | 41.0 | 99.63% |
| Axis Bank | 37.5 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 290.5 | 99.51% | 198 ms |
| Google Pay | 198.9 | 99.35% | 241 ms |
| Paytm | 48.2 | 99.53% | 201 ms |
| Navi | 22.4 | 99.53% | 304 ms |
| SuperMoney | 11.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 225.0 |
| Person to Person | 215.9 |
| QR Payments | 57.8 |
| UPI Lite | 29.2 |
| UPI Autopay | 20.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D161-MON) and any meetings/emails on 14 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D161-MON, RPT-D160-DAILY

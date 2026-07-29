---
id: RPT-D49-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-22T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 22 Feb 2026)

**Report ID:** RPT-D49-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 22 Feb 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 49 of 206)

## Transaction summary
The rail processed 564.0M UPI transactions on Sunday — a quiet Sunday — up 9.8M on the same day last week. Success held at 99.61% and settlement at 98.63%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 564.0  (▼43.8 d/d, ▲9.8 w/w, ▼231.9 m/m)
- **Success Rate:** 99.61%  (▲0.27 d/d, ▲1.06 w/w, ▲0.48 m/m)
- **Settlement Success:** 98.63%  (▼1.19 d/d, ▼1.35 w/w, ▼1.32 m/m)
- **Technical Declines:** 0.46%  (▼0.01 w/w, ▼0.09 m/m)
- **Business Declines:** 0.21%  (▼0.01 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,699  (▼29 d/d, ▼79 w/w, ▼443 m/m)
- **Merchant Complaints:** 184  (▼6 w/w, ▼50 m/m)
- **Fraud Alerts:** 1,026  (▼4 d/d, ▼22 w/w, ▼134 m/m)
- **Risk Score:** 29  (▼1 d/d, ▼1 w/w, ▼5 m/m)
- **Response Time:** 693 ms  (▼6 d/d, ▼16 w/w, ▼60 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 183.6 | 99.67% |
| HDFC Bank | 60.3 | 99.42% |
| Bank of Baroda | 43.4 | 99.26% |
| Union Bank of India | 38.0 | 99.63% |
| Axis Bank | 34.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 269.4 | 99.51% | 198 ms |
| Google Pay | 184.4 | 99.35% | 241 ms |
| Paytm | 44.7 | 99.53% | 201 ms |
| Navi | 20.7 | 99.53% | 304 ms |
| SuperMoney | 11.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 208.7 |
| Person to Person | 200.2 |
| QR Payments | 53.6 |
| UPI Lite | 27.1 |
| UPI Autopay | 18.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.46% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D49-MON) and any meetings/emails on 22 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D49-MON, RPT-D48-DAILY

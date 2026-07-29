---
id: RPT-D91-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-05T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 05 Apr 2026)

**Report ID:** RPT-D91-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 05 Apr 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 91 of 206)

## Transaction summary
The rail processed 577.6M UPI transactions on Sunday — a quiet Sunday — down 211.7M on the same day last week. Success held at 99.98% and settlement at 98.96%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 577.6  (▼43.0 d/d, ▼211.7 w/w, ▼218.3 m/m)
- **Success Rate:** 99.98%  (▲0.65 d/d, ▲0.38 w/w, ▲0.85 m/m)
- **Settlement Success:** 98.96%  (▼0.64 d/d, ▼0.98 w/w, ▼0.99 m/m)
- **Technical Declines:** 0.39%  (▼0.01 w/w, ▼0.16 m/m)
- **Business Declines:** 0.19%  (▼0.01 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,398  (▼22 d/d, ▼50 w/w, ▼744 m/m)
- **Merchant Complaints:** 146  (▼1 d/d, ▼8 w/w, ▼88 m/m)
- **Fraud Alerts:** 915  (▼13 d/d, ▼27 w/w, ▼245 m/m)
- **Risk Score:** 25  (▼1 d/d, ▼1 w/w, ▼9 m/m)
- **Response Time:** 649 ms  (▲1 d/d, ▼4 w/w, ▼104 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 188.0 | 99.67% |
| HDFC Bank | 61.8 | 99.42% |
| Bank of Baroda | 44.5 | 99.26% |
| Union Bank of India | 39.0 | 99.63% |
| Axis Bank | 35.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 275.9 | 99.51% | 198 ms |
| Google Pay | 188.9 | 99.35% | 241 ms |
| Paytm | 45.8 | 99.53% | 201 ms |
| Navi | 21.2 | 99.53% | 304 ms |
| SuperMoney | 11.3 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 213.7 |
| Person to Person | 205.0 |
| QR Payments | 54.9 |
| UPI Lite | 27.7 |
| UPI Autopay | 19.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.39% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D91-MON) and any meetings/emails on 05 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D91-MON, RPT-D90-DAILY

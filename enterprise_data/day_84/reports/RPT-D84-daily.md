---
id: RPT-D84-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-29T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 29 Mar 2026)

**Report ID:** RPT-D84-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 29 Mar 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 84 of 206)

## Transaction summary
The rail processed 789.3M UPI transactions on Sunday — the month-end surge as salary and bill-pay flows land — up 232.5M on the same day last week. Success held at 99.6% and settlement at 99.94%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 789.3  (▲1.1 d/d, ▲232.5 w/w, ▼6.6 m/m)
- **Success Rate:** 99.6%  (▲0.53 d/d, ▼0.03 w/w, ▲0.47 m/m)
- **Settlement Success:** 99.94%  (▼0.04 d/d, ▲0.2 w/w, ▼0.01 m/m)
- **Technical Declines:** 0.4%  (▼0.04 d/d, ▼0.1 w/w, ▼0.15 m/m)
- **Business Declines:** 0.2%  (▼0.04 m/m)
- **Customer Complaints:** 1,448  (▼86 d/d, ▼295 w/w, ▼694 m/m)
- **Merchant Complaints:** 154  (▼1 d/d, ▼5 w/w, ▼80 m/m)
- **Fraud Alerts:** 942  (▲13 d/d, ▼8 w/w, ▼218 m/m)
- **Risk Score:** 26  (▼1 w/w, ▼8 m/m)
- **Response Time:** 653 ms  (▼8 d/d, ▼64 w/w, ▼100 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 256.9 | 99.67% |
| HDFC Bank | 84.4 | 99.42% |
| Bank of Baroda | 60.7 | 99.26% |
| Union Bank of India | 53.2 | 99.63% |
| Axis Bank | 48.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 377.0 | 99.51% | 198 ms |
| Google Pay | 258.1 | 99.35% | 241 ms |
| Paytm | 62.6 | 99.53% | 201 ms |
| Navi | 29.0 | 99.53% | 304 ms |
| SuperMoney | 15.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 292.0 |
| Person to Person | 280.2 |
| QR Payments | 75.0 |
| UPI Lite | 37.9 |
| UPI Autopay | 26.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.4% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D84-MON) and any meetings/emails on 29 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D84-MON, RPT-D83-DAILY

---
id: RPT-D196-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-19T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 19 Jul 2026)

**Report ID:** RPT-D196-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 19 Jul 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 196 of 206)

## Transaction summary
The rail processed 616.4M UPI transactions on Sunday — a quiet Sunday — up 0.5M on the same day last week. Success held at 99.07% and settlement at 99.71%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 616.4  (▼57.7 d/d, ▲0.5 w/w, ▼179.5 m/m)
- **Success Rate:** 99.07%  (▼0.91 d/d, ▼0.91 w/w, ▼0.06 m/m)
- **Settlement Success:** 99.71%  (▼0.04 d/d, ▲0.19 w/w, ▼0.24 m/m)
- **Technical Declines:** 0.26%  (▼0.01 d/d, ▼0.01 w/w, ▼0.29 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 860  (▼3 d/d, ▼23 w/w, ▼1282 m/m)
- **Merchant Complaints:** 85  (▼2 d/d, ▼4 w/w, ▼149 m/m)
- **Fraud Alerts:** 703  (▼1 d/d, ▼24 w/w, ▼457 m/m)
- **Risk Score:** 18  (▼1 w/w, ▼16 m/m)
- **Response Time:** 527 ms  (▼1 d/d, ▼10 w/w, ▼226 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 200.6 | 99.67% |
| HDFC Bank | 65.9 | 99.42% |
| Bank of Baroda | 47.4 | 99.26% |
| Union Bank of India | 41.6 | 99.63% |
| Axis Bank | 38.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 294.4 | 99.51% | 198 ms |
| Google Pay | 201.6 | 99.35% | 241 ms |
| Paytm | 48.9 | 99.53% | 201 ms |
| Navi | 22.7 | 99.53% | 304 ms |
| SuperMoney | 12.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 228.1 |
| Person to Person | 218.8 |
| QR Payments | 58.6 |
| UPI Lite | 29.6 |
| UPI Autopay | 20.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.26% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D196-MON) and any meetings/emails on 19 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D196-MON, RPT-D195-DAILY

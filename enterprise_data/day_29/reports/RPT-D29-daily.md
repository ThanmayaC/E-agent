---
id: RPT-D29-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-02T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 02 Feb 2026)

**Report ID:** RPT-D29-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 02 Feb 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 29 of 206)

## Transaction summary
The rail processed 663.4M UPI transactions on Monday — the Monday ramp-up after the weekend — up 0.1M on the same day last week. Success held at 98.48% and settlement at 99.82%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 663.4  (▲115.0 d/d, ▲0.1 w/w, ▼132.5 m/m)
- **Success Rate:** 98.48%  (▼1.5 d/d, ▲0.39 w/w, ▼0.65 m/m)
- **Settlement Success:** 99.82%  (▼0.16 d/d, ▼0.16 w/w, ▼0.13 m/m)
- **Technical Declines:** 0.5%  (▼0.01 w/w, ▼0.05 m/m)
- **Business Declines:** 0.22%  (▼0.18 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,866  (▼22 d/d, ▼743 w/w, ▼276 m/m)
- **Merchant Complaints:** 204  (▲2 d/d, ▼5 w/w, ▼30 m/m)
- **Fraud Alerts:** 1,074  (▲8 d/d, ▼381 w/w, ▼86 m/m)
- **Risk Score:** 31  (▼28 w/w, ▼3 m/m)
- **Response Time:** 726 ms  (▼2 w/w, ▼27 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 215.9 | 99.67% |
| HDFC Bank | 70.9 | 99.42% |
| Bank of Baroda | 51.1 | 99.26% |
| Union Bank of India | 44.8 | 99.63% |
| Axis Bank | 40.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 316.9 | 99.51% | 198 ms |
| Google Pay | 217.0 | 99.35% | 241 ms |
| Paytm | 52.6 | 99.53% | 201 ms |
| Navi | 24.4 | 99.53% | 304 ms |
| SuperMoney | 12.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 245.5 |
| Person to Person | 235.5 |
| QR Payments | 63.0 |
| UPI Lite | 31.8 |
| UPI Autopay | 21.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.5% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D29-MON) and any meetings/emails on 02 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D29-MON, RPT-D28-DAILY

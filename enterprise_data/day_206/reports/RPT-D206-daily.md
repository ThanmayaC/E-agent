---
id: RPT-D206-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-29T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 29 Jul 2026)

**Report ID:** RPT-D206-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 29 Jul 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 206 of 206)

## Transaction summary
The rail processed 854.9M UPI transactions on Wednesday — the month-end surge as salary and bill-pay flows land — up 98.5M on the same day last week. Success held at 99.98% and settlement at 99.85%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 854.9  (▼71.4 d/d, ▲98.5 w/w, ▲59.0 m/m)
- **Success Rate:** 99.98%  (▲0.85 m/m)
- **Settlement Success:** 99.85%  (▼0.13 d/d, ▲0.65 w/w, ▼0.1 m/m)
- **Technical Declines:** 0.25%  (▼0.01 w/w, ▼0.3 m/m)
- **Business Declines:** 0.14%  (▼0.01 w/w, ▼0.1 m/m)
- **Customer Complaints:** 821  (▼6 d/d, ▼27 w/w, ▼1321 m/m)
- **Merchant Complaints:** 81  (▼1 d/d, ▼3 w/w, ▼153 m/m)
- **Fraud Alerts:** 689  (▲2 d/d, ▼14 w/w, ▼471 m/m)
- **Risk Score:** 18  (▼16 m/m)
- **Response Time:** 525 ms  (▲2 d/d, ▼4 w/w, ▼228 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 278.3 | 99.67% |
| HDFC Bank | 91.4 | 99.42% |
| Bank of Baroda | 65.8 | 99.26% |
| Union Bank of India | 57.7 | 99.63% |
| Axis Bank | 52.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 408.3 | 99.51% | 198 ms |
| Google Pay | 279.6 | 99.35% | 241 ms |
| Paytm | 67.8 | 99.53% | 201 ms |
| Navi | 31.4 | 99.53% | 304 ms |
| SuperMoney | 16.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 316.3 |
| Person to Person | 303.5 |
| QR Payments | 81.2 |
| UPI Lite | 41.0 |
| UPI Autopay | 28.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.25% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D206-MON) and any meetings/emails on 29 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D206-MON, RPT-D205-DAILY

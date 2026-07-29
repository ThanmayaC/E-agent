---
id: RPT-D42-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-15T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 15 Feb 2026)

**Report ID:** RPT-D42-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 15 Feb 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 42 of 206)

## Transaction summary
The rail processed 554.2M UPI transactions on Sunday — a quiet Sunday — down 8.2M on the same day last week. Success held at 98.55% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 554.2  (▼51.2 d/d, ▼8.2 w/w, ▼241.7 m/m)
- **Success Rate:** 98.55%  (▼0.99 d/d, ▼1.11 w/w, ▼0.58 m/m)
- **Settlement Success:** 99.98%  (▲0.46 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.47%  (▼0.01 w/w, ▼0.08 m/m)
- **Business Declines:** 0.22%  (▼0.08 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,778  (▼5 d/d, ▼317 w/w, ▼364 m/m)
- **Merchant Complaints:** 190  (▼3 d/d, ▼7 w/w, ▼44 m/m)
- **Fraud Alerts:** 1,048  (▲11 d/d, ▼164 w/w, ▼112 m/m)
- **Risk Score:** 30  (▼12 w/w, ▼4 m/m)
- **Response Time:** 709 ms  (▲10 d/d, ▼5 w/w, ▼44 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 180.4 | 99.67% |
| HDFC Bank | 59.3 | 99.42% |
| Bank of Baroda | 42.7 | 99.26% |
| Union Bank of India | 37.4 | 99.63% |
| Axis Bank | 34.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 264.7 | 99.51% | 198 ms |
| Google Pay | 181.2 | 99.35% | 241 ms |
| Paytm | 44.0 | 99.53% | 201 ms |
| Navi | 20.4 | 99.53% | 304 ms |
| SuperMoney | 10.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 205.1 |
| Person to Person | 196.7 |
| QR Payments | 52.6 |
| UPI Lite | 26.6 |
| UPI Autopay | 18.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.47% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D42-MON) and any meetings/emails on 15 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D42-MON, RPT-D41-DAILY

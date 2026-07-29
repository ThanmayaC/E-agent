---
id: RPT-D178-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-01T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 01 Jul 2026)

**Report ID:** RPT-D178-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 01 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 178 of 206)

## Transaction summary
The rail processed 752.5M UPI transactions on Wednesday — a steady mid-week day — up 26.2M on the same day last week. Success held at 99.49% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 752.5  (▼79.0 d/d, ▲26.2 w/w, ▼43.4 m/m)
- **Success Rate:** 99.49%  (▼0.13 d/d, ▼0.49 w/w, ▲0.36 m/m)
- **Settlement Success:** 99.98%  (▲0.03 m/m)
- **Technical Declines:** 0.28%  (▼0.01 w/w, ▼0.27 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 926  (▼5 d/d, ▼44 w/w, ▼1216 m/m)
- **Merchant Complaints:** 95  (▲2 d/d, ▼3 w/w, ▼139 m/m)
- **Fraud Alerts:** 733  (▼9 d/d, ▼14 w/w, ▼427 m/m)
- **Risk Score:** 19  (▼1 d/d, ▼1 w/w, ▼15 m/m)
- **Response Time:** 544 ms  (▼5 d/d, ▼14 w/w, ▼209 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 244.9 | 99.67% |
| HDFC Bank | 80.5 | 99.42% |
| Bank of Baroda | 57.9 | 99.26% |
| Union Bank of India | 50.8 | 99.63% |
| Axis Bank | 46.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 359.4 | 99.51% | 198 ms |
| Google Pay | 246.1 | 99.35% | 241 ms |
| Paytm | 59.7 | 99.53% | 201 ms |
| Navi | 27.7 | 99.53% | 304 ms |
| SuperMoney | 14.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 278.4 |
| Person to Person | 267.1 |
| QR Payments | 71.5 |
| UPI Lite | 36.1 |
| UPI Autopay | 24.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.28% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D178-MON) and any meetings/emails on 01 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D178-MON, RPT-D177-DAILY

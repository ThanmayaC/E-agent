---
id: RPT-D198-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-21T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 21 Jul 2026)

**Report ID:** RPT-D198-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 21 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 198 of 206)

## Transaction summary
The rail processed 768.7M UPI transactions on Tuesday — a steady mid-week day — up 25.1M on the same day last week. Success held at 99.4% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 768.7  (▲38.3 d/d, ▲25.1 w/w, ▼27.2 m/m)
- **Success Rate:** 99.4%  (▼0.58 d/d, ▲0.21 w/w, ▲0.27 m/m)
- **Settlement Success:** 99.98%  (▲0.02 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.26%  (▼0.01 w/w, ▼0.29 m/m)
- **Business Declines:** 0.15%  (▼0.09 m/m)
- **Customer Complaints:** 846  (▼28 w/w, ▼1296 m/m)
- **Merchant Complaints:** 85  (▲1 d/d, ▼2 w/w, ▼149 m/m)
- **Fraud Alerts:** 698  (▼12 d/d, ▼15 w/w, ▼462 m/m)
- **Risk Score:** 18  (▼1 w/w, ▼16 m/m)
- **Response Time:** 527 ms  (▼3 d/d, ▼12 w/w, ▼226 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 250.2 | 99.67% |
| HDFC Bank | 82.2 | 99.42% |
| Bank of Baroda | 59.2 | 99.26% |
| Union Bank of India | 51.9 | 99.63% |
| Axis Bank | 47.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 367.2 | 99.51% | 198 ms |
| Google Pay | 251.4 | 99.35% | 241 ms |
| Paytm | 61.0 | 99.53% | 201 ms |
| Navi | 28.3 | 99.53% | 304 ms |
| SuperMoney | 15.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 284.4 |
| Person to Person | 272.9 |
| QR Payments | 73.0 |
| UPI Lite | 36.9 |
| UPI Autopay | 25.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.26% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D198-MON) and any meetings/emails on 21 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D198-MON, RPT-D197-DAILY

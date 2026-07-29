---
id: RPT-D30-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-03T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 03 Feb 2026)

**Report ID:** RPT-D30-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 03 Feb 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 30 of 206)

## Transaction summary
The rail processed 670.0M UPI transactions on Tuesday — a steady mid-week day — down 4.7M on the same day last week. Success held at 99.54% and settlement at 99.35%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 670.0  (▲6.6 d/d, ▼4.7 w/w, ▼125.9 m/m)
- **Success Rate:** 99.54%  (▲1.06 d/d, ▲0.22 w/w, ▲0.41 m/m)
- **Settlement Success:** 99.35%  (▼0.47 d/d, ▼0.63 w/w, ▼0.6 m/m)
- **Technical Declines:** 0.5%  (▼0.01 w/w, ▼0.05 m/m)
- **Business Declines:** 0.22%  (▼0.12 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,861  (▼5 d/d, ▼487 w/w, ▼281 m/m)
- **Merchant Complaints:** 202  (▼2 d/d, ▼7 w/w, ▼32 m/m)
- **Fraud Alerts:** 1,080  (▲6 d/d, ▼244 w/w, ▼80 m/m)
- **Risk Score:** 31  (▼17 w/w, ▼3 m/m)
- **Response Time:** 714 ms  (▼12 d/d, ▼21 w/w, ▼39 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 218.1 | 99.67% |
| HDFC Bank | 71.6 | 99.42% |
| Bank of Baroda | 51.6 | 99.26% |
| Union Bank of India | 45.2 | 99.63% |
| Axis Bank | 41.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 320.0 | 99.51% | 198 ms |
| Google Pay | 219.1 | 99.35% | 241 ms |
| Paytm | 53.1 | 99.53% | 201 ms |
| Navi | 24.6 | 99.53% | 304 ms |
| SuperMoney | 13.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 247.9 |
| Person to Person | 237.8 |
| QR Payments | 63.6 |
| UPI Lite | 32.2 |
| UPI Autopay | 22.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.5% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D30-MON) and any meetings/emails on 03 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D30-MON, RPT-D29-DAILY

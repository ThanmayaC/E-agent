---
id: RPT-D121-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-05-05T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 05 May 2026)

**Report ID:** RPT-D121-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 05 May 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 121 of 206)

## Transaction summary
The rail processed 724.1M UPI transactions on Tuesday — a steady mid-week day — down 67.9M on the same day last week. Success held at 98.83% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 724.1  (▲41.0 d/d, ▼67.9 w/w, ▼71.8 m/m)
- **Success Rate:** 98.83%  (▼1.11 d/d, ▼1.07 w/w, ▼0.3 m/m)
- **Settlement Success:** 99.98%  (▲0.89 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.35%  (▼0.23 w/w, ▼0.2 m/m)
- **Business Declines:** 0.18%  (▼0.06 m/m)
- **Customer Complaints:** 1,210  (▼21 d/d, ▼592 w/w, ▼932 m/m)
- **Merchant Complaints:** 127  (▼91 w/w, ▼107 m/m)
- **Fraud Alerts:** 846  (▼12 d/d, ▼23 w/w, ▼314 m/m)
- **Risk Score:** 23  (▼1 d/d, ▼1 w/w, ▼11 m/m)
- **Response Time:** 603 ms  (▼4 d/d, ▼75 w/w, ▼150 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 235.7 | 99.67% |
| HDFC Bank | 77.4 | 99.42% |
| Bank of Baroda | 55.7 | 99.26% |
| Union Bank of India | 48.8 | 99.63% |
| Axis Bank | 44.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 345.9 | 99.51% | 198 ms |
| Google Pay | 236.8 | 99.35% | 241 ms |
| Paytm | 57.4 | 99.53% | 201 ms |
| Navi | 26.6 | 99.53% | 304 ms |
| SuperMoney | 14.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 267.9 |
| Person to Person | 257.1 |
| QR Payments | 68.8 |
| UPI Lite | 34.8 |
| UPI Autopay | 23.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.35% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D121-MON) and any meetings/emails on 05 May.

Refs: upi_kpis_month.xlsx, TEAMS-D121-MON, RPT-D120-DAILY

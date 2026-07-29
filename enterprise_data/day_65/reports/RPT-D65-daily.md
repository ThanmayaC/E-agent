---
id: RPT-D65-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-10T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 10 Mar 2026)

**Report ID:** RPT-D65-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 10 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 65 of 206)

## Transaction summary
The rail processed 708.7M UPI transactions on Tuesday — a steady mid-week day — up 12.1M on the same day last week. Success held at 99.46% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 708.7  (▼140.0 d/d, ▲12.1 w/w, ▼87.2 m/m)
- **Success Rate:** 99.46%  (▼0.34 d/d, ▼0.41 w/w, ▲0.33 m/m)
- **Settlement Success:** 99.98%  (▲1.22 d/d, ▲0.03 m/m)
- **Technical Declines:** 0.43%  (▼0.01 w/w, ▼0.12 m/m)
- **Business Declines:** 0.21%  (▲0.01 d/d, ▼0.03 m/m)
- **Customer Complaints:** 1,588  (▼1 d/d, ▼39 w/w, ▼554 m/m)
- **Merchant Complaints:** 168  (▼8 w/w, ▼66 m/m)
- **Fraud Alerts:** 983  (▲1 d/d, ▼22 w/w, ▼177 m/m)
- **Risk Score:** 28  (▼6 m/m)
- **Response Time:** 679 ms  (▼2 d/d, ▼10 w/w, ▼74 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 230.7 | 99.67% |
| HDFC Bank | 75.8 | 99.42% |
| Bank of Baroda | 54.5 | 99.26% |
| Union Bank of India | 47.8 | 99.63% |
| Axis Bank | 43.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 338.5 | 99.51% | 198 ms |
| Google Pay | 231.8 | 99.35% | 241 ms |
| Paytm | 56.2 | 99.53% | 201 ms |
| Navi | 26.1 | 99.53% | 304 ms |
| SuperMoney | 13.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 262.2 |
| Person to Person | 251.6 |
| QR Payments | 67.3 |
| UPI Lite | 34.0 |
| UPI Autopay | 23.4 |

## Failure analysis
- No incidents open. Technical declines are within the 0.43% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D65-MON) and any meetings/emails on 10 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D65-MON, RPT-D64-DAILY

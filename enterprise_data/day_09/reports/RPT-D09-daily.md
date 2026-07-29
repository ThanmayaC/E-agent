---
id: RPT-D09-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-13T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 13 Jan 2026)

**Report ID:** RPT-D09-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 13 Jan 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 9 of 206)

## Transaction summary
The rail processed 654.7M UPI transactions on Tuesday — a steady mid-week day — up 2.9M on the same day last week. Success held at 99.96% and settlement at 99.77%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 654.7  (▲10.4 d/d, ▲2.9 w/w, ▼141.2 m/m)
- **Success Rate:** 99.96%  (▲1.18 d/d, ▲0.24 w/w, ▲0.83 m/m)
- **Settlement Success:** 99.77%  (▼0.21 d/d, ▲0.32 w/w, ▼0.18 m/m)
- **Technical Declines:** 0.54%  (▼0.09 d/d, ▼0.01 w/w, ▼0.01 m/m)
- **Business Declines:** 0.24%
- **Customer Complaints:** 2,054  (▼237 d/d, ▼69 w/w, ▼88 m/m)
- **Merchant Complaints:** 225  (▼43 d/d, ▼10 w/w, ▼9 m/m)
- **Fraud Alerts:** 1,127  (▼1 d/d, ▼22 w/w, ▼33 m/m)
- **Risk Score:** 33  (▼1 d/d, ▼1 w/w, ▼1 m/m)
- **Response Time:** 748 ms  (▼16 d/d, ▼15 w/w, ▼5 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 213.1 | 99.67% |
| HDFC Bank | 70.0 | 99.42% |
| Bank of Baroda | 50.4 | 99.26% |
| Union Bank of India | 44.2 | 99.63% |
| Axis Bank | 40.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 312.7 | 99.51% | 198 ms |
| Google Pay | 214.1 | 99.35% | 241 ms |
| Paytm | 51.9 | 99.53% | 201 ms |
| Navi | 24.1 | 99.53% | 304 ms |
| SuperMoney | 12.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 242.2 |
| Person to Person | 232.4 |
| QR Payments | 62.2 |
| UPI Lite | 31.4 |
| UPI Autopay | 21.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.54% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D09-MON) and any meetings/emails on 13 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D09-MON, RPT-D08-DAILY

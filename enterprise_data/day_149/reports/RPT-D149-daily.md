---
id: RPT-D149-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-02T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 02 Jun 2026)

**Report ID:** RPT-D149-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 02 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 149 of 206)

## Transaction summary
The rail processed 736.3M UPI transactions on Tuesday — a steady mid-week day — up 13.5M on the same day last week. Success held at 99.73% and settlement at 99.41%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 736.3  (▲36.2 d/d, ▲13.5 w/w, ▼59.6 m/m)
- **Success Rate:** 99.73%  (▲0.23 d/d, ▲1.0 w/w, ▲0.6 m/m)
- **Settlement Success:** 99.41%  (▼0.33 d/d, ▼0.57 w/w, ▼0.54 m/m)
- **Technical Declines:** 0.31%  (▼0.01 d/d, ▼0.01 w/w, ▼0.24 m/m)
- **Business Declines:** 0.17%  (▼0.04 d/d, ▼0.04 w/w, ▼0.07 m/m)
- **Customer Complaints:** 1,061  (▼36 d/d, ▼183 w/w, ▼1081 m/m)
- **Merchant Complaints:** 110  (▼42 d/d, ▼4 w/w, ▼124 m/m)
- **Fraud Alerts:** 798  (▲7 d/d, ▼104 w/w, ▼362 m/m)
- **Risk Score:** 21  (▼7 w/w, ▼13 m/m)
- **Response Time:** 579 ms  (▼11 d/d, ▼9 w/w, ▼174 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 239.7 | 99.67% |
| HDFC Bank | 78.7 | 99.42% |
| Bank of Baroda | 56.7 | 99.26% |
| Union Bank of India | 49.7 | 99.63% |
| Axis Bank | 45.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 351.7 | 99.51% | 198 ms |
| Google Pay | 240.8 | 99.35% | 241 ms |
| Paytm | 58.4 | 99.53% | 201 ms |
| Navi | 27.1 | 99.53% | 304 ms |
| SuperMoney | 14.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 272.4 |
| Person to Person | 261.4 |
| QR Payments | 69.9 |
| UPI Lite | 35.3 |
| UPI Autopay | 24.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.31% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D149-MON) and any meetings/emails on 02 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D149-MON, RPT-D148-DAILY

---
id: RPT-D173-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-26T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 26 Jun 2026)

**Report ID:** RPT-D173-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 26 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 173 of 206)

## Transaction summary
The rail processed 750.4M UPI transactions on Friday — a steady mid-week day — up 12.9M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 750.4  (▼141.9 d/d, ▲12.9 w/w, ▼45.5 m/m)
- **Success Rate:** 99.98%  (▲1.09 d/d, ▲0.43 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.99 d/d, ▲0.7 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.29%  (▼0.26 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 951  (▼2 d/d, ▼42 w/w, ▼1191 m/m)
- **Merchant Complaints:** 97  (▼3 w/w, ▼137 m/m)
- **Fraud Alerts:** 745  (▼11 d/d, ▼12 w/w, ▼415 m/m)
- **Risk Score:** 20  (▼14 m/m)
- **Response Time:** 552 ms  (▼4 d/d, ▼4 w/w, ▼201 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 244.3 | 99.67% |
| HDFC Bank | 80.2 | 99.42% |
| Bank of Baroda | 57.8 | 99.26% |
| Union Bank of India | 50.6 | 99.63% |
| Axis Bank | 46.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 358.4 | 99.51% | 198 ms |
| Google Pay | 245.4 | 99.35% | 241 ms |
| Paytm | 59.5 | 99.53% | 201 ms |
| Navi | 27.6 | 99.53% | 304 ms |
| SuperMoney | 14.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 277.6 |
| Person to Person | 266.4 |
| QR Payments | 71.3 |
| UPI Lite | 36.0 |
| UPI Autopay | 24.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.29% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D173-MON) and any meetings/emails on 26 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D173-MON, RPT-D172-DAILY

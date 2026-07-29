---
id: RPT-D85-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-30T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 30 Mar 2026)

**Report ID:** RPT-D85-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 30 Mar 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 85 of 206)

## Transaction summary
The rail processed 776.5M UPI transactions on Monday — the month-end surge as salary and bill-pay flows land — up 100.6M on the same day last week. Success held at 98.55% and settlement at 99.9%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 776.5  (▼12.8 d/d, ▲100.6 w/w, ▼19.4 m/m)
- **Success Rate:** 98.55%  (▼1.05 d/d, ▼0.16 w/w, ▼0.58 m/m)
- **Settlement Success:** 99.9%  (▼0.04 d/d, ▲0.24 w/w, ▼0.05 m/m)
- **Technical Declines:** 0.4%  (▼0.19 w/w, ▼0.15 m/m)
- **Business Declines:** 0.19%  (▼0.01 d/d, ▼0.01 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,460  (▲12 d/d, ▼589 w/w, ▼682 m/m)
- **Merchant Complaints:** 151  (▼3 d/d, ▼7 w/w, ▼83 m/m)
- **Fraud Alerts:** 934  (▼8 d/d, ▼19 w/w, ▼226 m/m)
- **Risk Score:** 26  (▼8 m/m)
- **Response Time:** 657 ms  (▲4 d/d, ▼111 w/w, ▼96 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 252.8 | 99.67% |
| HDFC Bank | 83.0 | 99.42% |
| Bank of Baroda | 59.8 | 99.26% |
| Union Bank of India | 52.4 | 99.63% |
| Axis Bank | 47.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 370.9 | 99.51% | 198 ms |
| Google Pay | 253.9 | 99.35% | 241 ms |
| Paytm | 61.6 | 99.53% | 201 ms |
| Navi | 28.5 | 99.53% | 304 ms |
| SuperMoney | 15.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 287.3 |
| Person to Person | 275.7 |
| QR Payments | 73.8 |
| UPI Lite | 37.3 |
| UPI Autopay | 25.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.4% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D85-MON) and any meetings/emails on 30 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D85-MON, RPT-D84-DAILY

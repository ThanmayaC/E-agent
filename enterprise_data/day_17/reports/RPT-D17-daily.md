---
id: RPT-D17-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-21T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 21 Jan 2026)

**Report ID:** RPT-D17-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 21 Jan 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 17 of 206)

## Transaction summary
The rail processed 669.4M UPI transactions on Wednesday — a steady mid-week day — down 9.6M on the same day last week. Success held at 98.34% and settlement at 99.32%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 669.4  (▲0.2 d/d, ▼9.6 w/w, ▼126.5 m/m)
- **Success Rate:** 98.34%  (▼1.02 d/d, ▲0.08 w/w, ▼0.79 m/m)
- **Settlement Success:** 99.32%  (▼0.55 d/d, ▲0.47 w/w, ▼0.63 m/m)
- **Technical Declines:** 0.52%  (▼0.01 w/w, ▼0.03 m/m)
- **Business Declines:** 0.23%  (▼0.01 w/w, ▼0.01 m/m)
- **Customer Complaints:** 1,979  (▼39 d/d, ▼100 w/w, ▼163 m/m)
- **Merchant Complaints:** 218  (▼1 d/d, ▼7 w/w, ▼16 m/m)
- **Fraud Alerts:** 1,110  (▼1 d/d, ▼4 w/w, ▼50 m/m)
- **Risk Score:** 32  (▼1 w/w, ▼2 m/m)
- **Response Time:** 731 ms  (▼14 d/d, ▼18 w/w, ▼22 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 217.9 | 99.67% |
| HDFC Bank | 71.6 | 99.42% |
| Bank of Baroda | 51.5 | 99.26% |
| Union Bank of India | 45.2 | 99.63% |
| Axis Bank | 41.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 319.7 | 99.51% | 198 ms |
| Google Pay | 218.9 | 99.35% | 241 ms |
| Paytm | 53.1 | 99.53% | 201 ms |
| Navi | 24.6 | 99.53% | 304 ms |
| SuperMoney | 13.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 247.7 |
| Person to Person | 237.6 |
| QR Payments | 63.6 |
| UPI Lite | 32.1 |
| UPI Autopay | 22.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.52% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D17-MON) and any meetings/emails on 21 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D17-MON, RPT-D16-DAILY

---
id: RPT-D13-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-17T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 17 Jan 2026)

**Report ID:** RPT-D13-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 17 Jan 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 13 of 206)

## Transaction summary
The rail processed 611.3M UPI transactions on Saturday — a lighter Saturday — up 21.4M on the same day last week. Success held at 98.35% and settlement at 99.93%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 611.3  (▼51.7 d/d, ▲21.4 w/w, ▼184.6 m/m)
- **Success Rate:** 98.35%  (▼0.98 d/d, ▼0.47 w/w, ▼0.78 m/m)
- **Settlement Success:** 99.93%  (▲0.07 d/d, ▼0.05 w/w, ▼0.02 m/m)
- **Technical Declines:** 0.53%  (▼0.35 w/w, ▼0.02 m/m)
- **Business Declines:** 0.23%  (▼0.01 w/w, ▼0.01 m/m)
- **Customer Complaints:** 2,040  (▲15 d/d, ▼943 w/w, ▼102 m/m)
- **Merchant Complaints:** 219  (▼1 d/d, ▼170 w/w, ▼15 m/m)
- **Fraud Alerts:** 1,105  (▼19 d/d, ▼34 w/w, ▼55 m/m)
- **Risk Score:** 33  (▼1 w/w, ▼1 m/m)
- **Response Time:** 736 ms  (▼8 d/d, ▼92 w/w, ▼17 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 199.0 | 99.67% |
| HDFC Bank | 65.4 | 99.42% |
| Bank of Baroda | 47.0 | 99.26% |
| Union Bank of India | 41.2 | 99.63% |
| Axis Bank | 37.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 292.0 | 99.51% | 198 ms |
| Google Pay | 199.9 | 99.35% | 241 ms |
| Paytm | 48.5 | 99.53% | 201 ms |
| Navi | 22.5 | 99.53% | 304 ms |
| SuperMoney | 11.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 226.2 |
| Person to Person | 217.0 |
| QR Payments | 58.1 |
| UPI Lite | 29.3 |
| UPI Autopay | 20.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.53% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D13-MON) and any meetings/emails on 17 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D13-MON, RPT-D12-DAILY

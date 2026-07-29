---
id: RPT-D21-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-25T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 25 Jan 2026)

**Report ID:** RPT-D21-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 25 Jan 2026  ·  **Day archetype:** Sunday (quiet) · maintenance window
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 21 of 206)

## Transaction summary
The rail processed 553.1M UPI transactions on Sunday — a quiet Sunday with a scheduled maintenance window — up 13.9M on the same day last week. Success held at 98.79% and settlement at 99.35%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 553.1  (▼33.7 d/d, ▲13.9 w/w, ▼242.8 m/m)
- **Success Rate:** 98.79%  (▲0.27 d/d, ▼0.24 w/w, ▼0.34 m/m)
- **Settlement Success:** 99.35%  (▼0.32 d/d, ▼0.63 w/w, ▼0.6 m/m)
- **Technical Declines:** 0.51%  (▼0.08 d/d, ▼0.01 w/w, ▼0.04 m/m)
- **Business Declines:** 0.23%  (▼0.01 m/m)
- **Customer Complaints:** 1,941  (▼225 d/d, ▼100 w/w, ▼201 m/m)
- **Merchant Complaints:** 214  (▲1 d/d, ▼7 w/w, ▼20 m/m)
- **Fraud Alerts:** 1,097  (▼4 d/d, ▼8 w/w, ▼63 m/m)
- **Risk Score:** 32  (▼2 m/m)
- **Response Time:** 729 ms  (▼29 d/d, ▼18 w/w, ▼24 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 180.0 | 99.67% |
| HDFC Bank | 59.1 | 99.42% |
| Bank of Baroda | 42.6 | 99.26% |
| Union Bank of India | 37.3 | 99.63% |
| Axis Bank | 34.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 264.2 | 99.51% | 198 ms |
| Google Pay | 180.9 | 99.35% | 241 ms |
| Paytm | 43.9 | 99.53% | 201 ms |
| Navi | 20.3 | 99.53% | 304 ms |
| SuperMoney | 10.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 204.6 |
| Person to Person | 196.4 |
| QR Payments | 52.5 |
| UPI Lite | 26.5 |
| UPI Autopay | 18.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.51% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D21-MON) and any meetings/emails on 25 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D21-MON, RPT-D20-DAILY

---
id: RPT-D100-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-14T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 14 Apr 2026)

**Report ID:** RPT-D100-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 14 Apr 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 100 of 206)

## Transaction summary
The rail processed 710.8M UPI transactions on Tuesday — a steady mid-week day — up 19.7M on the same day last week. Success held at 99.32% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 710.8  (▲23.4 d/d, ▲19.7 w/w, ▼85.1 m/m)
- **Success Rate:** 99.32%  (▼0.66 d/d, ▲0.31 w/w, ▲0.19 m/m)
- **Settlement Success:** 99.98%  (▲0.29 d/d, ▲0.14 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.37%  (▼0.01 d/d, ▼0.27 w/w, ▼0.18 m/m)
- **Business Declines:** 0.19%  (▼0.05 m/m)
- **Customer Complaints:** 1,352  (▲4 d/d, ▼633 w/w, ▼790 m/m)
- **Merchant Complaints:** 142  (▲1 d/d, ▼102 w/w, ▼92 m/m)
- **Fraud Alerts:** 898  (▼11 d/d, ▼20 w/w, ▼262 m/m)
- **Risk Score:** 25  (▼1 w/w, ▼9 m/m)
- **Response Time:** 628 ms  (▼5 d/d, ▼76 w/w, ▼125 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 231.4 | 99.67% |
| HDFC Bank | 76.0 | 99.42% |
| Bank of Baroda | 54.7 | 99.26% |
| Union Bank of India | 48.0 | 99.63% |
| Axis Bank | 43.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 339.5 | 99.51% | 198 ms |
| Google Pay | 232.5 | 99.35% | 241 ms |
| Paytm | 56.4 | 99.53% | 201 ms |
| Navi | 26.1 | 99.53% | 304 ms |
| SuperMoney | 13.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 263.0 |
| Person to Person | 252.3 |
| QR Payments | 67.5 |
| UPI Lite | 34.1 |
| UPI Autopay | 23.5 |

## Failure analysis
- No incidents open. Technical declines are within the 0.37% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D100-MON) and any meetings/emails on 14 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D100-MON, RPT-D99-DAILY

---
id: RPT-D40-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-13T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 13 Feb 2026)

**Report ID:** RPT-D40-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 13 Feb 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 40 of 206)

## Transaction summary
The rail processed 667.5M UPI transactions on Friday — a steady mid-week day — down 5.2M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 667.5  (▼17.1 d/d, ▼5.2 w/w, ▼128.4 m/m)
- **Success Rate:** 99.98%  (▲1.02 d/d, ▲0.57 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲1.22 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.47%  (▼0.01 d/d, ▼0.02 w/w, ▼0.08 m/m)
- **Business Declines:** 0.22%  (▼0.06 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,801  (▲11 d/d, ▼253 w/w, ▼341 m/m)
- **Merchant Complaints:** 194  (▲2 d/d, ▼4 w/w, ▼40 m/m)
- **Fraud Alerts:** 1,048  (▼2 d/d, ▼129 w/w, ▼112 m/m)
- **Risk Score:** 30  (▼10 w/w, ▼4 m/m)
- **Response Time:** 701 ms  (▼9 d/d, ▼18 w/w, ▼52 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 217.3 | 99.67% |
| HDFC Bank | 71.4 | 99.42% |
| Bank of Baroda | 51.4 | 99.26% |
| Union Bank of India | 45.0 | 99.63% |
| Axis Bank | 41.1 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 318.8 | 99.51% | 198 ms |
| Google Pay | 218.3 | 99.35% | 241 ms |
| Paytm | 52.9 | 99.53% | 201 ms |
| Navi | 24.5 | 99.53% | 304 ms |
| SuperMoney | 13.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 247.0 |
| Person to Person | 237.0 |
| QR Payments | 63.4 |
| UPI Lite | 32.0 |
| UPI Autopay | 22.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.47% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D40-MON) and any meetings/emails on 13 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D40-MON, RPT-D39-DAILY

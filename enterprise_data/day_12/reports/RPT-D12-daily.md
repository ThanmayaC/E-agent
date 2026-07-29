---
id: RPT-D12-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-01-16T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 16 Jan 2026)

**Report ID:** RPT-D12-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 16 Jan 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 12 of 206)

## Transaction summary
The rail processed 663.0M UPI transactions on Friday — a steady mid-week day — up 4.4M on the same day last week. Success held at 99.33% and settlement at 99.86%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 663.0  (▲9.0 d/d, ▲4.4 w/w, ▼132.9 m/m)
- **Success Rate:** 99.33%  (▲0.34 d/d, ▲0.61 w/w, ▲0.2 m/m)
- **Settlement Success:** 99.86%  (▲0.26 d/d, ▲1.0 w/w, ▼0.09 m/m)
- **Technical Declines:** 0.53%  (▼0.58 w/w, ▼0.02 m/m)
- **Business Declines:** 0.23%  (▼0.01 d/d, ▼0.01 w/w, ▼0.01 m/m)
- **Customer Complaints:** 2,025  (▼33 d/d, ▼1571 w/w, ▼117 m/m)
- **Merchant Complaints:** 220  (▼3 d/d, ▼262 w/w, ▼14 m/m)
- **Fraud Alerts:** 1,124  (▼5 d/d, ▼25 w/w, ▼36 m/m)
- **Risk Score:** 33  (▼1 w/w, ▼1 m/m)
- **Response Time:** 744 ms  (▲2 d/d, ▼134 w/w, ▼9 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 215.8 | 99.67% |
| HDFC Bank | 70.9 | 99.42% |
| Bank of Baroda | 51.0 | 99.26% |
| Union Bank of India | 44.7 | 99.63% |
| Axis Bank | 40.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 316.7 | 99.51% | 198 ms |
| Google Pay | 216.8 | 99.35% | 241 ms |
| Paytm | 52.6 | 99.53% | 201 ms |
| Navi | 24.4 | 99.53% | 304 ms |
| SuperMoney | 12.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 245.3 |
| Person to Person | 235.4 |
| QR Payments | 63.0 |
| UPI Lite | 31.8 |
| UPI Autopay | 21.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.53% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D12-MON) and any meetings/emails on 16 Jan.

Refs: upi_kpis_month.xlsx, TEAMS-D12-MON, RPT-D11-DAILY

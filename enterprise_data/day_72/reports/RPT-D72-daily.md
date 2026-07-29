---
id: RPT-D72-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-17T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 17 Mar 2026)

**Report ID:** RPT-D72-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Tuesday 17 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 72 of 206)

## Transaction summary
The rail processed 691.4M UPI transactions on Tuesday — a steady mid-week day — down 17.3M on the same day last week. Success held at 99.03% and settlement at 99.38%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 691.4  (▲10.6 d/d, ▼17.3 w/w, ▼104.5 m/m)
- **Success Rate:** 99.03%  (▼0.38 d/d, ▼0.43 w/w, ▼0.1 m/m)
- **Settlement Success:** 99.38%  (▲0.01 d/d, ▼0.6 w/w, ▼0.57 m/m)
- **Technical Declines:** 0.42%  (▼0.01 w/w, ▼0.13 m/m)
- **Business Declines:** 0.2%  (▼0.01 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,541  (▼13 d/d, ▼47 w/w, ▼601 m/m)
- **Merchant Complaints:** 164  (▲1 d/d, ▼4 w/w, ▼70 m/m)
- **Fraud Alerts:** 954  (▼8 d/d, ▼29 w/w, ▼206 m/m)
- **Risk Score:** 27  (▼1 w/w, ▼7 m/m)
- **Response Time:** 661 ms  (▼4 d/d, ▼18 w/w, ▼92 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 225.1 | 99.67% |
| HDFC Bank | 73.9 | 99.42% |
| Bank of Baroda | 53.2 | 99.26% |
| Union Bank of India | 46.6 | 99.63% |
| Axis Bank | 42.6 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 330.3 | 99.51% | 198 ms |
| Google Pay | 226.1 | 99.35% | 241 ms |
| Paytm | 54.8 | 99.53% | 201 ms |
| Navi | 25.4 | 99.53% | 304 ms |
| SuperMoney | 13.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 255.8 |
| Person to Person | 245.4 |
| QR Payments | 65.7 |
| UPI Lite | 33.2 |
| UPI Autopay | 22.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.42% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D72-MON) and any meetings/emails on 17 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D72-MON, RPT-D71-DAILY

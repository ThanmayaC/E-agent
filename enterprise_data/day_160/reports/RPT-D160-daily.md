---
id: RPT-D160-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-13T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 13 Jun 2026)

**Report ID:** RPT-D160-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 13 Jun 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 160 of 206)

## Transaction summary
The rail processed 671.5M UPI transactions on Saturday — a lighter Saturday — up 23.8M on the same day last week. Success held at 99.7% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 671.5  (▼67.9 d/d, ▲23.8 w/w, ▼124.4 m/m)
- **Success Rate:** 99.7%  (▲0.45 d/d, ▲0.64 w/w, ▲0.57 m/m)
- **Settlement Success:** 99.98%  (▲0.99 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.3%  (▼0.12 w/w, ▼0.25 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 1,005  (▼16 d/d, ▼287 w/w, ▼1137 m/m)
- **Merchant Complaints:** 104  (▲1 d/d, ▼44 w/w, ▼130 m/m)
- **Fraud Alerts:** 781  (▲12 d/d, ▼5 w/w, ▼379 m/m)
- **Risk Score:** 21  (▼13 m/m)
- **Response Time:** 564 ms  (▼1 d/d, ▼45 w/w, ▼189 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 218.6 | 99.67% |
| HDFC Bank | 71.8 | 99.42% |
| Bank of Baroda | 51.7 | 99.26% |
| Union Bank of India | 45.3 | 99.63% |
| Axis Bank | 41.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 320.7 | 99.51% | 198 ms |
| Google Pay | 219.6 | 99.35% | 241 ms |
| Paytm | 53.3 | 99.53% | 201 ms |
| Navi | 24.7 | 99.53% | 304 ms |
| SuperMoney | 13.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 248.5 |
| Person to Person | 238.4 |
| QR Payments | 63.8 |
| UPI Lite | 32.2 |
| UPI Autopay | 22.2 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D160-MON) and any meetings/emails on 13 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D160-MON, RPT-D159-DAILY

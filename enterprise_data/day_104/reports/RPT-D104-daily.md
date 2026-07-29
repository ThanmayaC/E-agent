---
id: RPT-D104-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-18T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 18 Apr 2026)

**Report ID:** RPT-D104-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 18 Apr 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 104 of 206)

## Transaction summary
The rail processed 640.4M UPI transactions on Saturday — a lighter Saturday — down 0.3M on the same day last week. Success held at 99.14% and settlement at 99.25%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 640.4  (▼62.8 d/d, ▼0.3 w/w, ▼155.5 m/m)
- **Success Rate:** 99.14%  (▼0.1 d/d, ▼0.72 w/w, ▲0.01 m/m)
- **Settlement Success:** 99.25%  (▼0.73 d/d, ▼0.13 w/w, ▼0.7 m/m)
- **Technical Declines:** 0.37%  (▼0.01 w/w, ▼0.18 m/m)
- **Business Declines:** 0.19%  (▼0.01 d/d, ▼0.05 m/m)
- **Customer Complaints:** 1,320  (▼76 d/d, ▼56 w/w, ▼822 m/m)
- **Merchant Complaints:** 138  (▼37 d/d, ▼5 w/w, ▼96 m/m)
- **Fraud Alerts:** 888  (▼25 w/w, ▼272 m/m)
- **Risk Score:** 25  (▼9 m/m)
- **Response Time:** 629 ms  (▼5 d/d, ▼4 w/w, ▼124 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 208.4 | 99.67% |
| HDFC Bank | 68.5 | 99.42% |
| Bank of Baroda | 49.3 | 99.26% |
| Union Bank of India | 43.2 | 99.63% |
| Axis Bank | 39.5 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 305.9 | 99.51% | 198 ms |
| Google Pay | 209.4 | 99.35% | 241 ms |
| Paytm | 50.8 | 99.53% | 201 ms |
| Navi | 23.5 | 99.53% | 304 ms |
| SuperMoney | 12.5 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 236.9 |
| Person to Person | 227.3 |
| QR Payments | 60.8 |
| UPI Lite | 30.7 |
| UPI Autopay | 21.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.37% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D104-MON) and any meetings/emails on 18 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D104-MON, RPT-D103-DAILY

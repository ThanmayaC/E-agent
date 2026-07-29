---
id: RPT-D113-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-27T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 27 Apr 2026)

**Report ID:** RPT-D113-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 27 Apr 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 113 of 206)

## Transaction summary
The rail processed 686.7M UPI transactions on Monday — the Monday ramp-up after the weekend — down 7.5M on the same day last week. Success held at 99.49% and settlement at 99.43%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 686.7  (▲98.9 d/d, ▼7.5 w/w, ▼109.2 m/m)
- **Success Rate:** 99.49%  (▼0.21 d/d, ▼0.49 w/w, ▲0.36 m/m)
- **Settlement Success:** 99.43%  (▼0.55 d/d, ▼0.32 w/w, ▼0.52 m/m)
- **Technical Declines:** 0.36%  (▼0.01 w/w, ▼0.19 m/m)
- **Business Declines:** 0.18%  (▼0.01 d/d, ▼0.01 w/w, ▼0.06 m/m)
- **Customer Complaints:** 1,274  (▼7 d/d, ▼40 w/w, ▼868 m/m)
- **Merchant Complaints:** 132  (▼12 d/d, ▼5 w/w, ▼102 m/m)
- **Fraud Alerts:** 870  (▼4 d/d, ▼14 w/w, ▼290 m/m)
- **Risk Score:** 24  (▼10 m/m)
- **Response Time:** 612 ms  (▼7 d/d, ▼13 w/w, ▼141 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 223.5 | 99.67% |
| HDFC Bank | 73.4 | 99.42% |
| Bank of Baroda | 52.8 | 99.26% |
| Union Bank of India | 46.3 | 99.63% |
| Axis Bank | 42.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 328.0 | 99.51% | 198 ms |
| Google Pay | 224.6 | 99.35% | 241 ms |
| Paytm | 54.5 | 99.53% | 201 ms |
| Navi | 25.2 | 99.53% | 304 ms |
| SuperMoney | 13.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 254.1 |
| Person to Person | 243.8 |
| QR Payments | 65.2 |
| UPI Lite | 33.0 |
| UPI Autopay | 22.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.36% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D113-MON) and any meetings/emails on 27 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D113-MON, RPT-D112-DAILY

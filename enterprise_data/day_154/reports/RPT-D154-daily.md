---
id: RPT-D154-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-07T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 07 Jun 2026)

**Report ID:** RPT-D154-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 07 Jun 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 154 of 206)

## Transaction summary
The rail processed 600.9M UPI transactions on Sunday — a quiet Sunday — down 224.0M on the same day last week. Success held at 99.11% and settlement at 99.73%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 600.9  (▼46.8 d/d, ▼224.0 w/w, ▼195.0 m/m)
- **Success Rate:** 99.11%  (▲0.05 d/d, ▼0.09 w/w, ▼0.02 m/m)
- **Settlement Success:** 99.73%  (▲0.74 d/d, ▼0.25 w/w, ▼0.22 m/m)
- **Technical Declines:** 0.3%  (▼0.12 d/d, ▼0.03 w/w, ▼0.25 m/m)
- **Business Declines:** 0.16%  (▼0.08 w/w, ▼0.08 m/m)
- **Customer Complaints:** 1,052  (▼240 d/d, ▼81 w/w, ▼1090 m/m)
- **Merchant Complaints:** 105  (▼43 d/d, ▼73 w/w, ▼129 m/m)
- **Fraud Alerts:** 788  (▲2 d/d, ▼15 w/w, ▼372 m/m)
- **Risk Score:** 21  (▼13 m/m)
- **Response Time:** 574 ms  (▼35 d/d, ▼12 w/w, ▼179 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 195.6 | 99.67% |
| HDFC Bank | 64.2 | 99.42% |
| Bank of Baroda | 46.2 | 99.26% |
| Union Bank of India | 40.5 | 99.63% |
| Axis Bank | 37.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 287.0 | 99.51% | 198 ms |
| Google Pay | 196.5 | 99.35% | 241 ms |
| Paytm | 47.7 | 99.53% | 201 ms |
| Navi | 22.1 | 99.53% | 304 ms |
| SuperMoney | 11.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 222.3 |
| Person to Person | 213.3 |
| QR Payments | 57.1 |
| UPI Lite | 28.8 |
| UPI Autopay | 19.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D154-MON) and any meetings/emails on 07 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D154-MON, RPT-D153-DAILY

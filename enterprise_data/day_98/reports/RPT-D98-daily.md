---
id: RPT-D98-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-04-12T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 12 Apr 2026)

**Report ID:** RPT-D98-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 12 Apr 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 98 of 206)

## Transaction summary
The rail processed 563.8M UPI transactions on Sunday — a quiet Sunday — down 13.8M on the same day last week. Success held at 98.65% and settlement at 99.6%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 563.8  (▼76.9 d/d, ▼13.8 w/w, ▼232.1 m/m)
- **Success Rate:** 98.65%  (▼1.21 d/d, ▼1.33 w/w, ▼0.48 m/m)
- **Settlement Success:** 99.6%  (▲0.22 d/d, ▲0.64 w/w, ▼0.35 m/m)
- **Technical Declines:** 0.38%  (▼0.01 w/w, ▼0.17 m/m)
- **Business Declines:** 0.19%  (▼0.05 m/m)
- **Customer Complaints:** 1,355  (▼21 d/d, ▼43 w/w, ▼787 m/m)
- **Merchant Complaints:** 142  (▼1 d/d, ▼4 w/w, ▼92 m/m)
- **Fraud Alerts:** 902  (▼11 d/d, ▼13 w/w, ▼258 m/m)
- **Risk Score:** 25  (▼9 m/m)
- **Response Time:** 638 ms  (▲5 d/d, ▼11 w/w, ▼115 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 183.5 | 99.67% |
| HDFC Bank | 60.3 | 99.42% |
| Bank of Baroda | 43.4 | 99.26% |
| Union Bank of India | 38.0 | 99.63% |
| Axis Bank | 34.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 269.3 | 99.51% | 198 ms |
| Google Pay | 184.4 | 99.35% | 241 ms |
| Paytm | 44.7 | 99.53% | 201 ms |
| Navi | 20.7 | 99.53% | 304 ms |
| SuperMoney | 11.0 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 208.6 |
| Person to Person | 200.1 |
| QR Payments | 53.6 |
| UPI Lite | 27.1 |
| UPI Autopay | 18.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.38% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D98-MON) and any meetings/emails on 12 Apr.

Refs: upi_kpis_month.xlsx, TEAMS-D98-MON, RPT-D97-DAILY

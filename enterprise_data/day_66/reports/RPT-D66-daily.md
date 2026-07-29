---
id: RPT-D66-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-11T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 11 Mar 2026)

**Report ID:** RPT-D66-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 11 Mar 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 66 of 206)

## Transaction summary
The rail processed 827.8M UPI transactions on Wednesday — a campaign-driven high-volume day — up 152.1M on the same day last week. Success held at 98.59% and settlement at 99.01%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 827.8  (▲119.1 d/d, ▲152.1 w/w, ▲31.9 m/m)
- **Success Rate:** 98.59%  (▼0.87 d/d, ▼1.25 w/w, ▼0.54 m/m)
- **Settlement Success:** 99.01%  (▼0.97 d/d, ▼0.37 w/w, ▼0.94 m/m)
- **Technical Declines:** 0.43%  (▼0.01 w/w, ▼0.12 m/m)
- **Business Declines:** 0.2%  (▼0.01 d/d, ▼0.17 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,572  (▼16 d/d, ▼629 w/w, ▼570 m/m)
- **Merchant Complaints:** 167  (▼1 d/d, ▼7 w/w, ▼67 m/m)
- **Fraud Alerts:** 981  (▼2 d/d, ▼344 w/w, ▼179 m/m)
- **Risk Score:** 28  (▼25 w/w, ▼6 m/m)
- **Response Time:** 678 ms  (▼1 d/d, ▼11 w/w, ▼75 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 269.4 | 99.67% |
| HDFC Bank | 88.5 | 99.42% |
| Bank of Baroda | 63.7 | 99.26% |
| Union Bank of India | 55.8 | 99.63% |
| Axis Bank | 51.0 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 395.4 | 99.51% | 198 ms |
| Google Pay | 270.7 | 99.35% | 241 ms |
| Paytm | 65.7 | 99.53% | 201 ms |
| Navi | 30.4 | 99.53% | 304 ms |
| SuperMoney | 16.1 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 306.3 |
| Person to Person | 293.9 |
| QR Payments | 78.6 |
| UPI Lite | 39.7 |
| UPI Autopay | 27.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.43% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D66-MON) and any meetings/emails on 11 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D66-MON, RPT-D65-DAILY

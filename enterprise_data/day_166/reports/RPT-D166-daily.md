---
id: RPT-D166-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-19T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 19 Jun 2026)

**Report ID:** RPT-D166-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 19 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 166 of 206)

## Transaction summary
The rail processed 737.5M UPI transactions on Friday — a steady mid-week day — down 1.9M on the same day last week. Success held at 99.55% and settlement at 99.28%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 737.5  (▲0.1 d/d, ▼1.9 w/w, ▼58.4 m/m)
- **Success Rate:** 99.55%  (▼0.43 d/d, ▲0.3 w/w, ▲0.42 m/m)
- **Settlement Success:** 99.28%  (▼0.7 d/d, ▼0.7 w/w, ▼0.67 m/m)
- **Technical Declines:** 0.29%  (▼0.01 d/d, ▼0.01 w/w, ▼0.26 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 993  (▲6 d/d, ▼28 w/w, ▼1149 m/m)
- **Merchant Complaints:** 100  (▼3 w/w, ▼134 m/m)
- **Fraud Alerts:** 757  (▼5 d/d, ▼12 w/w, ▼403 m/m)
- **Risk Score:** 20  (▼1 w/w, ▼14 m/m)
- **Response Time:** 556 ms  (▼5 d/d, ▼9 w/w, ▼197 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 240.1 | 99.67% |
| HDFC Bank | 78.9 | 99.42% |
| Bank of Baroda | 56.8 | 99.26% |
| Union Bank of India | 49.8 | 99.63% |
| Axis Bank | 45.4 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 352.3 | 99.51% | 198 ms |
| Google Pay | 241.2 | 99.35% | 241 ms |
| Paytm | 58.5 | 99.53% | 201 ms |
| Navi | 27.1 | 99.53% | 304 ms |
| SuperMoney | 14.4 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 272.9 |
| Person to Person | 261.8 |
| QR Payments | 70.1 |
| UPI Lite | 35.4 |
| UPI Autopay | 24.3 |

## Failure analysis
- No incidents open. Technical declines are within the 0.29% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — use the quieter window to progress capacity planning before the next peak.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D166-MON) and any meetings/emails on 19 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D166-MON, RPT-D165-DAILY

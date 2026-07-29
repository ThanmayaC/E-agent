---
id: RPT-D68-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-03-13T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 13 Mar 2026)

**Report ID:** RPT-D68-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Friday 13 Mar 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 68 of 206)

## Transaction summary
The rail processed 684.4M UPI transactions on Friday — a steady mid-week day — up 5.5M on the same day last week. Success held at 99.97% and settlement at 98.82%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 684.4  (▲12.5 d/d, ▲5.5 w/w, ▼111.5 m/m)
- **Success Rate:** 99.97%  (▲1.07 d/d, ▲0.03 w/w, ▲0.84 m/m)
- **Settlement Success:** 98.82%  (▼0.02 d/d, ▲0.24 w/w, ▼1.13 m/m)
- **Technical Declines:** 0.43%  (▼0.01 w/w, ▼0.12 m/m)
- **Business Declines:** 0.2%  (▼0.12 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,560  (▼15 d/d, ▼436 w/w, ▼582 m/m)
- **Merchant Complaints:** 165  (▼1 d/d, ▼143 w/w, ▼69 m/m)
- **Fraud Alerts:** 964  (▼8 d/d, ▼130 w/w, ▼196 m/m)
- **Risk Score:** 28  (▼9 w/w, ▼6 m/m)
- **Response Time:** 665 ms  (▼4 d/d, ▼9 w/w, ▼88 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 222.8 | 99.67% |
| HDFC Bank | 73.2 | 99.42% |
| Bank of Baroda | 52.7 | 99.26% |
| Union Bank of India | 46.2 | 99.63% |
| Axis Bank | 42.2 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 326.9 | 99.51% | 198 ms |
| Google Pay | 223.8 | 99.35% | 241 ms |
| Paytm | 54.3 | 99.53% | 201 ms |
| Navi | 25.2 | 99.53% | 304 ms |
| SuperMoney | 13.3 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 253.2 |
| Person to Person | 243.0 |
| QR Payments | 65.0 |
| UPI Lite | 32.9 |
| UPI Autopay | 22.6 |

## Failure analysis
- No incidents open. Technical declines are within the 0.43% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D68-MON) and any meetings/emails on 13 Mar.

Refs: upi_kpis_month.xlsx, TEAMS-D68-MON, RPT-D67-DAILY

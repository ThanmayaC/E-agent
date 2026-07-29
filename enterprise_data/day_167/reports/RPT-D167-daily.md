---
id: RPT-D167-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-20T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 20 Jun 2026)

**Report ID:** RPT-D167-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 20 Jun 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 167 of 206)

## Transaction summary
The rail processed 663.7M UPI transactions on Saturday — a lighter Saturday — down 7.8M on the same day last week. Success held at 99.98% and settlement at 99.28%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 663.7  (▼73.8 d/d, ▼7.8 w/w, ▼132.2 m/m)
- **Success Rate:** 99.98%  (▲0.43 d/d, ▲0.28 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.28%  (▼0.7 w/w, ▼0.67 m/m)
- **Technical Declines:** 0.29%  (▼0.01 w/w, ▼0.26 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 981  (▼12 d/d, ▼24 w/w, ▼1161 m/m)
- **Merchant Complaints:** 99  (▼1 d/d, ▼5 w/w, ▼135 m/m)
- **Fraud Alerts:** 761  (▲4 d/d, ▼20 w/w, ▼399 m/m)
- **Risk Score:** 20  (▼1 w/w, ▼14 m/m)
- **Response Time:** 562 ms  (▲6 d/d, ▼2 w/w, ▼191 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 216.0 | 99.67% |
| HDFC Bank | 71.0 | 99.42% |
| Bank of Baroda | 51.1 | 99.26% |
| Union Bank of India | 44.8 | 99.63% |
| Axis Bank | 40.9 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 317.0 | 99.51% | 198 ms |
| Google Pay | 217.1 | 99.35% | 241 ms |
| Paytm | 52.6 | 99.53% | 201 ms |
| Navi | 24.4 | 99.53% | 304 ms |
| SuperMoney | 12.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 245.6 |
| Person to Person | 235.6 |
| QR Payments | 63.1 |
| UPI Lite | 31.9 |
| UPI Autopay | 21.9 |

## Failure analysis
- No incidents open. Technical declines are within the 0.29% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — hold the monitoring line and work down the merchant-onboarding backlog.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D167-MON) and any meetings/emails on 20 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D167-MON, RPT-D166-DAILY

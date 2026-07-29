---
id: RPT-D41-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-14T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 14 Feb 2026)

**Report ID:** RPT-D41-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 14 Feb 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 41 of 206)

## Transaction summary
The rail processed 605.4M UPI transactions on Saturday — a lighter Saturday — down 4.4M on the same day last week. Success held at 99.54% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 605.4  (▼62.1 d/d, ▼4.4 w/w, ▼190.5 m/m)
- **Success Rate:** 99.54%  (▼0.44 d/d, ▲0.67 w/w, ▲0.41 m/m)
- **Settlement Success:** 99.98%  (▲0.03 m/m)
- **Technical Declines:** 0.47%  (▼0.02 w/w, ▼0.08 m/m)
- **Business Declines:** 0.22%  (▼0.13 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,783  (▼18 d/d, ▼547 w/w, ▼359 m/m)
- **Merchant Complaints:** 193  (▼1 d/d, ▼6 w/w, ▼41 m/m)
- **Fraud Alerts:** 1,037  (▼11 d/d, ▼283 w/w, ▼123 m/m)
- **Risk Score:** 30  (▼21 w/w, ▼4 m/m)
- **Response Time:** 699 ms  (▼2 d/d, ▼17 w/w, ▼54 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 197.1 | 99.67% |
| HDFC Bank | 64.7 | 99.42% |
| Bank of Baroda | 46.6 | 99.26% |
| Union Bank of India | 40.8 | 99.63% |
| Axis Bank | 37.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 289.2 | 99.51% | 198 ms |
| Google Pay | 198.0 | 99.35% | 241 ms |
| Paytm | 48.0 | 99.53% | 201 ms |
| Navi | 22.3 | 99.53% | 304 ms |
| SuperMoney | 11.8 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 224.0 |
| Person to Person | 214.9 |
| QR Payments | 57.5 |
| UPI Lite | 29.1 |
| UPI Autopay | 20.0 |

## Failure analysis
- No incidents open. Technical declines are within the 0.47% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — keep the standard monitoring cadence and let the adoption programmes run.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D41-MON) and any meetings/emails on 14 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D41-MON, RPT-D40-DAILY

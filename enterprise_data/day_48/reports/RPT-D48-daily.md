---
id: RPT-D48-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-21T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 21 Feb 2026)

**Report ID:** RPT-D48-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Saturday 21 Feb 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 48 of 206)

## Transaction summary
The rail processed 607.8M UPI transactions on Saturday — a lighter Saturday — up 2.4M on the same day last week. Success held at 99.34% and settlement at 99.82%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 607.8  (▼80.6 d/d, ▲2.4 w/w, ▼188.1 m/m)
- **Success Rate:** 99.34%  (▼0.2 d/d, ▼0.2 w/w, ▲0.21 m/m)
- **Settlement Success:** 99.82%  (▲0.76 d/d, ▼0.16 w/w, ▼0.13 m/m)
- **Technical Declines:** 0.46%  (▼0.01 w/w, ▼0.09 m/m)
- **Business Declines:** 0.21%  (▼0.01 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,728  (▲7 d/d, ▼55 w/w, ▼414 m/m)
- **Merchant Complaints:** 184  (▼3 d/d, ▼9 w/w, ▼50 m/m)
- **Fraud Alerts:** 1,030  (▲2 d/d, ▼7 w/w, ▼130 m/m)
- **Risk Score:** 30  (▲1 d/d, ▼4 m/m)
- **Response Time:** 699 ms  (▲3 d/d, ▼54 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 197.8 | 99.67% |
| HDFC Bank | 65.0 | 99.42% |
| Bank of Baroda | 46.8 | 99.26% |
| Union Bank of India | 41.0 | 99.63% |
| Axis Bank | 37.5 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 290.3 | 99.51% | 198 ms |
| Google Pay | 198.8 | 99.35% | 241 ms |
| Paytm | 48.2 | 99.53% | 201 ms |
| Navi | 22.3 | 99.53% | 304 ms |
| SuperMoney | 11.9 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 224.9 |
| Person to Person | 215.8 |
| QR Payments | 57.7 |
| UPI Lite | 29.2 |
| UPI Autopay | 20.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.46% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D48-MON) and any meetings/emails on 21 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D48-MON, RPT-D47-DAILY

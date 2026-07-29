---
id: RPT-D168-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-21T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 21 Jun 2026)

**Report ID:** RPT-D168-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 21 Jun 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 168 of 206)

## Transaction summary
The rail processed 597.7M UPI transactions on Sunday — a quiet Sunday — down 10.4M on the same day last week. Success held at 99.98% and settlement at 99.77%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 597.7  (▼66.0 d/d, ▼10.4 w/w, ▼198.2 m/m)
- **Success Rate:** 99.98%  (▲0.85 m/m)
- **Settlement Success:** 99.77%  (▲0.49 d/d, ▼0.21 w/w, ▼0.18 m/m)
- **Technical Declines:** 0.29%  (▼0.01 w/w, ▼0.26 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 983  (▲2 d/d, ▼18 w/w, ▼1159 m/m)
- **Merchant Complaints:** 99  (▼4 w/w, ▼135 m/m)
- **Fraud Alerts:** 752  (▼9 d/d, ▼16 w/w, ▼408 m/m)
- **Risk Score:** 20  (▼1 w/w, ▼14 m/m)
- **Response Time:** 562 ms  (▼7 w/w, ▼191 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 194.6 | 99.67% |
| HDFC Bank | 63.9 | 99.42% |
| Bank of Baroda | 46.0 | 99.26% |
| Union Bank of India | 40.3 | 99.63% |
| Axis Bank | 36.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 285.5 | 99.51% | 198 ms |
| Google Pay | 195.5 | 99.35% | 241 ms |
| Paytm | 47.4 | 99.53% | 201 ms |
| Navi | 22.0 | 99.53% | 304 ms |
| SuperMoney | 11.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 221.1 |
| Person to Person | 212.2 |
| QR Payments | 56.8 |
| UPI Lite | 28.7 |
| UPI Autopay | 19.7 |

## Failure analysis
- No incidents open. Technical declines are within the 0.29% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D168-MON) and any meetings/emails on 21 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D168-MON, RPT-D167-DAILY

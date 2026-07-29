---
id: RPT-D28-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-01T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 01 Feb 2026)

**Report ID:** RPT-D28-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Sunday 01 Feb 2026  ·  **Day archetype:** Sunday (quiet) · maintenance window
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 28 of 206)

## Transaction summary
The rail processed 548.4M UPI transactions on Sunday — a quiet Sunday with a scheduled maintenance window — down 4.7M on the same day last week. Success held at 99.98% and settlement at 99.98%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 548.4  (▼206.7 d/d, ▼4.7 w/w, ▼247.5 m/m)
- **Success Rate:** 99.98%  (▲0.36 d/d, ▲1.19 w/w, ▲0.85 m/m)
- **Settlement Success:** 99.98%  (▲0.63 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.5%  (▼0.01 w/w, ▼0.05 m/m)
- **Business Declines:** 0.22%  (▼0.01 d/d, ▼0.01 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,888  (▲3 d/d, ▼53 w/w, ▼254 m/m)
- **Merchant Complaints:** 202  (▼2 d/d, ▼12 w/w, ▼32 m/m)
- **Fraud Alerts:** 1,066  (▼19 d/d, ▼31 w/w, ▼94 m/m)
- **Risk Score:** 31  (▼1 w/w, ▼3 m/m)
- **Response Time:** 726 ms  (▲5 d/d, ▼3 w/w, ▼27 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 178.5 | 99.67% |
| HDFC Bank | 58.6 | 99.42% |
| Bank of Baroda | 42.2 | 99.26% |
| Union Bank of India | 37.0 | 99.63% |
| Axis Bank | 33.8 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 261.9 | 99.51% | 198 ms |
| Google Pay | 179.3 | 99.35% | 241 ms |
| Paytm | 43.5 | 99.53% | 201 ms |
| Navi | 20.2 | 99.53% | 304 ms |
| SuperMoney | 10.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 202.9 |
| Person to Person | 194.7 |
| QR Payments | 52.1 |
| UPI Lite | 26.3 |
| UPI Autopay | 18.1 |

## Failure analysis
- No incidents open. Technical declines are within the 0.5% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D28-MON) and any meetings/emails on 01 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D28-MON, RPT-D27-DAILY

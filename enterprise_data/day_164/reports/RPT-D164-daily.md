---
id: RPT-D164-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-06-17T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 17 Jun 2026)

**Report ID:** RPT-D164-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Wednesday 17 Jun 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 164 of 206)

## Transaction summary
The rail processed 751.4M UPI transactions on Wednesday — a steady mid-week day — down 167.2M on the same day last week. Success held at 99.36% and settlement at 99.7%; the softest bank was IDFC First Bank at 98.92%, still comfortably inside the normal band.

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 751.4  (▲29.9 d/d, ▼167.2 w/w, ▼44.5 m/m)
- **Success Rate:** 99.36%  (▲0.09 d/d, ▼0.27 w/w, ▲0.23 m/m)
- **Settlement Success:** 99.7%  (▲0.7 d/d, ▲0.54 w/w, ▼0.25 m/m)
- **Technical Declines:** 0.3%  (▼0.01 w/w, ▼0.25 m/m)
- **Business Declines:** 0.16%  (▼0.08 m/m)
- **Customer Complaints:** 996  (▼3 d/d, ▼42 w/w, ▼1146 m/m)
- **Merchant Complaints:** 101  (▼1 d/d, ▼4 w/w, ▼133 m/m)
- **Fraud Alerts:** 768  (▲6 d/d, ▼12 w/w, ▼392 m/m)
- **Risk Score:** 20  (▼1 d/d, ▼1 w/w, ▼14 m/m)
- **Response Time:** 557 ms  (▼7 d/d, ▼9 w/w, ▼196 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 244.6 | 99.67% |
| HDFC Bank | 80.3 | 99.42% |
| Bank of Baroda | 57.8 | 99.26% |
| Union Bank of India | 50.7 | 99.63% |
| Axis Bank | 46.3 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 358.9 | 99.51% | 198 ms |
| Google Pay | 245.7 | 99.35% | 241 ms |
| Paytm | 59.6 | 99.53% | 201 ms |
| Navi | 27.6 | 99.53% | 304 ms |
| SuperMoney | 14.7 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 278.0 |
| Person to Person | 266.7 |
| QR Payments | 71.4 |
| UPI Lite | 36.1 |
| UPI Autopay | 24.8 |

## Failure analysis
- No incidents open. Technical declines are within the 0.3% steady-state band; residual failures are routine bank/network timeouts.

## Recommendations
Steady state — no action beyond routine watch; pick up the SLA trend at the next sync.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D164-MON) and any meetings/emails on 17 Jun.

Refs: upi_kpis_month.xlsx, TEAMS-D164-MON, RPT-D163-DAILY

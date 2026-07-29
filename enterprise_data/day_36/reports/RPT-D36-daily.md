---
id: RPT-D36-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-02-09T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 09 Feb 2026)

**Report ID:** RPT-D36-DAILY  ·  **Prepared by:** Lakshmi Agarwal
**Date:** Monday 09 Feb 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 36 of 206)

## Transaction summary
The rail processed 644.5M UPI transactions on Monday — the Monday ramp-up after the weekend — down 18.9M on the same day last week. Success landed at 98.95% and settlement at 98.71%, held back by live issues on WhatsApp Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 644.5  (▲82.1 d/d, ▼18.9 w/w, ▼151.4 m/m)
- **Success Rate:** 98.95%  (▼0.71 d/d, ▲0.47 w/w, ▼0.18 m/m)
- **Settlement Success:** 98.71%  (▼0.81 d/d, ▼1.11 w/w, ▼1.24 m/m)
- **Technical Declines:** 0.48%  (▼0.02 w/w, ▼0.07 m/m)
- **Business Declines:** 0.25%  (▼0.05 d/d, ▲0.03 w/w, ▲0.01 m/m)
- **Customer Complaints:** 1,936  (▼159 d/d, ▲70 w/w, ▼206 m/m)
- **Merchant Complaints:** 196  (▼1 d/d, ▼8 w/w, ▼38 m/m)
- **Fraud Alerts:** 1,134  (▼78 d/d, ▲60 w/w, ▼26 m/m)
- **Risk Score:** 36  (▼6 d/d, ▲5 w/w, ▲2 m/m)
- **Response Time:** 715 ms  (▲1 d/d, ▼11 w/w, ▼38 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 209.8 | 99.67% |
| HDFC Bank | 68.9 | 99.42% |
| Bank of Baroda | 49.6 | 99.26% |
| Union Bank of India | 43.5 | 99.63% |
| Axis Bank | 39.7 | 99.39% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 307.8 | 99.51% | 198 ms |
| Google Pay | 210.8 | 99.35% | 241 ms |
| Paytm | 51.1 | 99.53% | 201 ms |
| Navi | 23.7 | 99.53% | 304 ms |
| SuperMoney | 12.6 | 99.22% | 327 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 238.5 |
| Person to Person | 228.8 |
| QR Payments | 61.2 |
| UPI Lite | 30.9 |
| UPI Autopay | 21.3 |

## Failure analysis
- INC-2026-08 — fraud / risk spike on WhatsApp Pay (day 3 of 5); see RCA-2026-08.

## Recommendations
Stay on the open incident: keep recovery monitoring on WhatsApp Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D36-MON) and any meetings/emails on 09 Feb.

Refs: upi_kpis_month.xlsx, TEAMS-D36-MON, RPT-D35-DAILY, INC-2026-08, RCA-2026-08

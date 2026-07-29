---
id: RPT-D168-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-06T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 06 Dec 2026)

**Report ID:** RPT-D168-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 06 Dec 2026  ·  **Day archetype:** Sunday (quiet) · maintenance window
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 168 of 180)

## Transaction summary
The rail processed 858.5M UPI transactions on Sunday — a quiet Sunday with a scheduled maintenance window — down 278.7M on the same day last week. Success landed at 99.98% and settlement at 99.98%, held back by live issues on QR Payments (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 858.5  (▼77.4 d/d, ▼278.7 w/w, ▲113.6 m/m)
- **Success Rate:** 99.98%  (▲0.04 d/d, ▲1.06 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.91 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.28%  (▼0.03 d/d, ▼0.12 w/w, ▼0.17 m/m)
- **Business Declines:** 0.13%  (▼0.07 m/m)
- **Customer Complaints:** 974  (▼73 d/d, ▼320 w/w, ▼968 m/m)
- **Merchant Complaints:** 89  (▼64 w/w, ▼122 m/m)
- **Fraud Alerts:** 691  (▲3 d/d, ▼17 w/w, ▼360 m/m)
- **Risk Score:** 18  (▼1 d/d, ▼1 w/w, ▼13 m/m)
- **Response Time:** 556 ms  (▼13 d/d, ▼41 w/w, ▼186 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 276.0 | 99.5% |
| HDFC Bank | 94.7 | 99.55% |
| Bank of Baroda | 68.1 | 99.64% |
| Union Bank of India | 59.1 | 99.43% |
| ICICI Bank | 52.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 409.6 | 99.14% | 231 ms |
| Google Pay | 280.4 | 99.17% | 316 ms |
| Paytm | 69.3 | 99.06% | 192 ms |
| Navi | 31.6 | 99.17% | 225 ms |
| SuperMoney | 16.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 321.9 |
| Person to Person | 304.8 |
| QR Payments | 81.6 |
| UPI Lite | 41.2 |
| UPI Autopay | 28.3 |

## Failure analysis
- INC-2026-21 — feature-level degradation on QR Payments (day 3 of 5); see RCA-2026-21.

## Recommendations
Stay on the open incident: keep recovery monitoring on QR Payments and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D168-MON) and any meetings/emails on 06 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D168-MON, RPT-D167-DAILY, INC-2026-21, RCA-2026-21

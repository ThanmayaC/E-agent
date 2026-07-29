---
id: RPT-D169-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-07T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 07 Dec 2026)

**Report ID:** RPT-D169-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 07 Dec 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 169 of 180)

## Transaction summary
The rail processed 1019.1M UPI transactions on Monday — the Monday ramp-up after the weekend — down 239.1M on the same day last week. Success landed at 99.98% and settlement at 99.34%, held back by live issues on QR Payments (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1019.1  (▲160.6 d/d, ▼239.1 w/w, ▲274.2 m/m)
- **Success Rate:** 99.98%  (▲0.38 m/m)
- **Settlement Success:** 99.34%  (▼0.64 d/d, ▼0.64 w/w, ▼0.09 m/m)
- **Technical Declines:** 0.26%  (▼0.02 d/d, ▼0.08 w/w, ▼0.19 m/m)
- **Business Declines:** 0.13%  (▼0.07 m/m)
- **Customer Complaints:** 916  (▼58 d/d, ▼233 w/w, ▼1026 m/m)
- **Merchant Complaints:** 88  (▼1 d/d, ▼41 w/w, ▼123 m/m)
- **Fraud Alerts:** 688  (▼3 d/d, ▼9 w/w, ▼363 m/m)
- **Risk Score:** 18  (▼1 w/w, ▼13 m/m)
- **Response Time:** 542 ms  (▼14 d/d, ▼34 w/w, ▼200 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 327.7 | 99.5% |
| HDFC Bank | 112.4 | 99.55% |
| Bank of Baroda | 80.8 | 99.64% |
| Union Bank of India | 70.2 | 99.43% |
| ICICI Bank | 62.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 486.2 | 99.14% | 231 ms |
| Google Pay | 332.9 | 99.17% | 316 ms |
| Paytm | 82.2 | 99.06% | 192 ms |
| Navi | 37.6 | 99.17% | 225 ms |
| SuperMoney | 19.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 382.2 |
| Person to Person | 361.8 |
| QR Payments | 96.8 |
| UPI Lite | 48.9 |
| UPI Autopay | 33.6 |

## Failure analysis
- INC-2026-21 — feature-level degradation on QR Payments (day 4 of 5); see RCA-2026-21.

## Recommendations
Stay on the open incident: keep recovery monitoring on QR Payments and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D169-MON) and any meetings/emails on 07 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D169-MON, RPT-D168-DAILY, INC-2026-21, RCA-2026-21

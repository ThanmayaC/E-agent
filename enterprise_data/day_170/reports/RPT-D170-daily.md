---
id: RPT-D170-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-08T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 08 Dec 2026)

**Report ID:** RPT-D170-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 08 Dec 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 170 of 180)

## Transaction summary
The rail processed 1050.0M UPI transactions on Tuesday — a steady mid-week day — up 0.4M on the same day last week. Success landed at 99.98% and settlement at 99.5%, held back by live issues on QR Payments (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1050.0  (▲30.9 d/d, ▲0.4 w/w, ▲305.1 m/m)
- **Success Rate:** 99.98%  (▲0.38 m/m)
- **Settlement Success:** 99.5%  (▲0.16 d/d, ▼0.03 w/w, ▲0.07 m/m)
- **Technical Declines:** 0.24%  (▼0.02 d/d, ▼0.21 m/m)
- **Business Declines:** 0.13%  (▼0.07 m/m)
- **Customer Complaints:** 899  (▼17 d/d, ▼6 w/w, ▼1043 m/m)
- **Merchant Complaints:** 88  (▼3 w/w, ▼123 m/m)
- **Fraud Alerts:** 687  (▼1 d/d, ▼12 w/w, ▼364 m/m)
- **Risk Score:** 18  (▼1 w/w, ▼13 m/m)
- **Response Time:** 545 ms  (▲3 d/d, ▲4 w/w, ▼197 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 337.6 | 99.5% |
| HDFC Bank | 115.8 | 99.55% |
| Bank of Baroda | 83.3 | 99.64% |
| Union Bank of India | 72.3 | 99.43% |
| ICICI Bank | 64.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 500.9 | 99.14% | 231 ms |
| Google Pay | 343.0 | 99.17% | 316 ms |
| Paytm | 84.7 | 99.06% | 192 ms |
| Navi | 38.7 | 99.17% | 225 ms |
| SuperMoney | 20.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 393.8 |
| Person to Person | 372.8 |
| QR Payments | 99.8 |
| UPI Lite | 50.4 |
| UPI Autopay | 34.6 |

## Failure analysis
- INC-2026-21 — feature-level degradation on QR Payments (day 5 of 5); see RCA-2026-21.

## Recommendations
Stay on the open incident: keep recovery monitoring on QR Payments and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D170-MON) and any meetings/emails on 08 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D170-MON, RPT-D169-DAILY, INC-2026-21, RCA-2026-21

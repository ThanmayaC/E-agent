---
id: RPT-D66-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-26T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 26 Aug 2026)

**Report ID:** RPT-D66-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 26 Aug 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 66 of 180)

## Transaction summary
The rail processed 870.1M UPI transactions on Wednesday — a steady mid-week day — up 32.5M on the same day last week. Success landed at 99.92% and settlement at 99.98%, held back by live issues on MetroRide, QuickBite (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 870.1  (▲14.1 d/d, ▲32.5 w/w, ▲125.2 m/m)
- **Success Rate:** 99.92%  (▲0.97 d/d, ▲1.12 w/w, ▲0.32 m/m)
- **Settlement Success:** 99.98%  (▲0.62 d/d, ▲0.63 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.35%  (▼0.01 d/d, ▼0.01 w/w, ▼0.1 m/m)
- **Business Declines:** 0.21%  (▼0.03 d/d, ▲0.01 w/w, ▲0.01 m/m)
- **Customer Complaints:** 1,448  (▲11 d/d, ▼150 w/w, ▼494 m/m)
- **Merchant Complaints:** 205  (▼37 d/d, ▼21 w/w, ▼6 m/m)
- **Fraud Alerts:** 897  (▼1 d/d, ▼14 w/w, ▼154 m/m)
- **Risk Score:** 25  (▼1 d/d, ▼1 w/w, ▼6 m/m)
- **Response Time:** 647 ms  (▼5 d/d, ▼12 w/w, ▼95 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 279.8 | 99.5% |
| HDFC Bank | 96.0 | 99.55% |
| Bank of Baroda | 69.0 | 99.64% |
| Union Bank of India | 59.9 | 99.43% |
| ICICI Bank | 53.6 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 415.1 | 99.14% | 231 ms |
| Google Pay | 284.2 | 99.17% | 316 ms |
| Paytm | 70.2 | 99.06% | 192 ms |
| Navi | 32.1 | 99.17% | 225 ms |
| SuperMoney | 17.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 326.3 |
| Person to Person | 308.9 |
| QR Payments | 82.7 |
| UPI Lite | 41.8 |
| UPI Autopay | 28.7 |

## Failure analysis
- INC-2026-18 — merchant decline-rate spike on MetroRide, QuickBite (day 2 of 2); see INC-2026-18.

## Recommendations
Stay on the open incident: keep recovery monitoring on MetroRide, QuickBite and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D66-MON) and any meetings/emails on 26 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D66-MON, RPT-D65-DAILY, INC-2026-18

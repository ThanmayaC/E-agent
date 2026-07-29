---
id: RPT-D65-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-25T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 25 Aug 2026)

**Report ID:** RPT-D65-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 25 Aug 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 65 of 180)

## Transaction summary
The rail processed 856.0M UPI transactions on Tuesday — a steady mid-week day — up 6.3M on the same day last week. Success landed at 98.95% and settlement at 99.36%, held back by live issues on MetroRide, QuickBite (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 856.0  (▲31.8 d/d, ▲6.3 w/w, ▲111.1 m/m)
- **Success Rate:** 98.95%  (▲0.04 d/d, ▼1.03 w/w, ▼0.65 m/m)
- **Settlement Success:** 99.36%  (▼0.62 d/d, ▲1.26 w/w, ▼0.07 m/m)
- **Technical Declines:** 0.36%  (▲0.01 d/d, ▼0.09 m/m)
- **Business Declines:** 0.24%  (▲0.07 d/d, ▲0.01 w/w, ▲0.04 m/m)
- **Customer Complaints:** 1,437  (▲2 d/d, ▼229 w/w, ▼505 m/m)
- **Merchant Complaints:** 242  (▲92 d/d, ▼40 w/w, ▲31 m/m)
- **Fraud Alerts:** 898  (▲9 d/d, ▼10 w/w, ▼153 m/m)
- **Risk Score:** 26  (▲1 d/d, ▼5 m/m)
- **Response Time:** 652 ms  (▼3 d/d, ▼4 w/w, ▼90 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 275.2 | 99.5% |
| HDFC Bank | 94.4 | 99.55% |
| Bank of Baroda | 67.9 | 99.64% |
| Union Bank of India | 59.0 | 99.43% |
| ICICI Bank | 52.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 408.4 | 99.14% | 231 ms |
| Google Pay | 279.6 | 99.17% | 316 ms |
| Paytm | 69.1 | 99.06% | 192 ms |
| Navi | 31.5 | 99.17% | 225 ms |
| SuperMoney | 16.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 321.0 |
| Person to Person | 303.9 |
| QR Payments | 81.3 |
| UPI Lite | 41.1 |
| UPI Autopay | 28.2 |

## Failure analysis
- INC-2026-18 — merchant decline-rate spike on MetroRide, QuickBite (day 1 of 2); see INC-2026-18.

## Recommendations
Stay on the open incident: keep recovery monitoring on MetroRide, QuickBite and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D65-MON) and any meetings/emails on 25 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D65-MON, RPT-D64-DAILY, INC-2026-18

---
id: RPT-D102-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-01T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 01 Oct 2026)

**Report ID:** RPT-D102-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 01 Oct 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 102 of 180)

## Transaction summary
The rail processed 926.2M UPI transactions on Thursday — a steady mid-week day — up 18.6M on the same day last week. Success landed at 99.98% and settlement at 98.81%, held back by live issues on State Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 926.2  (▼79.2 d/d, ▲18.6 w/w, ▲181.3 m/m)
- **Success Rate:** 99.98%  (▲0.27 w/w, ▲0.38 m/m)
- **Settlement Success:** 98.81%  (▼0.03 d/d, ▼0.15 w/w, ▼0.62 m/m)
- **Technical Declines:** 0.31%  (▼0.01 w/w, ▼0.14 m/m)
- **Business Declines:** 0.17%  (▼0.02 d/d, ▼0.11 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,259  (▼46 d/d, ▼434 w/w, ▼683 m/m)
- **Merchant Complaints:** 159  (▼28 d/d, ▲29 w/w, ▼52 m/m)
- **Fraud Alerts:** 814  (▼10 d/d, ▼289 w/w, ▼237 m/m)
- **Risk Score:** 23  (▼20 w/w, ▼8 m/m)
- **Response Time:** 610 ms  (▼6 d/d, ▼9 w/w, ▼132 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 297.8 | 99.26% |
| HDFC Bank | 102.2 | 99.55% |
| Bank of Baroda | 73.5 | 99.64% |
| Union Bank of India | 63.8 | 99.43% |
| ICICI Bank | 57.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 441.9 | 99.14% | 231 ms |
| Google Pay | 302.5 | 99.17% | 316 ms |
| Paytm | 74.7 | 99.06% | 192 ms |
| Navi | 34.1 | 99.17% | 225 ms |
| SuperMoney | 18.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 347.3 |
| Person to Person | 328.8 |
| QR Payments | 88.0 |
| UPI Lite | 44.5 |
| UPI Autopay | 30.6 |

## Failure analysis
- INC-2026-12 — merchant settlement delay on State Bank of India (day 3 of 5); see RCA-2026-12.

## Recommendations
Stay on the open incident: keep recovery monitoring on State Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D102-MON) and any meetings/emails on 01 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D102-MON, RPT-D101-DAILY, INC-2026-12, RCA-2026-12

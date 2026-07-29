---
id: RPT-D59-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-19T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 19 Aug 2026)

**Report ID:** RPT-D59-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 19 Aug 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 59 of 180)

## Transaction summary
The rail processed 837.6M UPI transactions on Wednesday — a steady mid-week day — up 6.8M on the same day last week. Success landed at 98.8% and settlement at 99.35%, held back by live issues on ICICI Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 837.6  (▼12.1 d/d, ▲6.8 w/w, ▲92.7 m/m)
- **Success Rate:** 98.8%  (▼1.18 d/d, ▼1.18 w/w, ▼0.8 m/m)
- **Settlement Success:** 99.35%  (▲1.25 d/d, ▼0.47 w/w, ▼0.08 m/m)
- **Technical Declines:** 0.36%  (▼0.01 w/w, ▼0.09 m/m)
- **Business Declines:** 0.2%  (▼0.03 d/d, ▲0.02 w/w)
- **Customer Complaints:** 1,598  (▼68 d/d, ▲65 w/w, ▼344 m/m)
- **Merchant Complaints:** 226  (▼56 d/d, ▲64 w/w, ▲15 m/m)
- **Fraud Alerts:** 911  (▲3 d/d, ▼19 w/w, ▼140 m/m)
- **Risk Score:** 26  (▼5 m/m)
- **Response Time:** 659 ms  (▲3 d/d, ▼8 w/w, ▼83 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 269.3 | 99.5% |
| HDFC Bank | 92.4 | 99.55% |
| Bank of Baroda | 66.4 | 99.64% |
| Union Bank of India | 57.7 | 99.43% |
| ICICI Bank | 51.6 | 98.65% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 399.6 | 99.14% | 231 ms |
| Google Pay | 273.6 | 99.17% | 316 ms |
| Paytm | 67.6 | 99.06% | 192 ms |
| Navi | 30.9 | 99.17% | 225 ms |
| SuperMoney | 16.3 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 314.1 |
| Person to Person | 297.3 |
| QR Payments | 79.6 |
| UPI Lite | 40.2 |
| UPI Autopay | 27.6 |

## Failure analysis
- INC-2026-03 — merchant settlement delay on ICICI Bank (day 3 of 4); see RCA-2026-03.

## Recommendations
Stay on the open incident: keep recovery monitoring on ICICI Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D59-MON) and any meetings/emails on 19 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D59-MON, RPT-D58-DAILY, INC-2026-03, RCA-2026-03

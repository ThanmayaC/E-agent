---
id: RPT-D145-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-13T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 13 Nov 2026)

**Report ID:** RPT-D145-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 13 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 145 of 180)

## Transaction summary
The rail processed 1010.1M UPI transactions on Friday — a steady mid-week day — down 188.5M on the same day last week. Success landed at 99.79% and settlement at 99.78%, held back by live issues on IndusInd Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1010.1  (▲20.8 d/d, ▼188.5 w/w, ▲265.2 m/m)
- **Success Rate:** 99.79%  (▼0.19 d/d, ▼0.1 w/w, ▲0.19 m/m)
- **Settlement Success:** 99.78%  (▼0.2 d/d, ▼0.2 w/w, ▲0.35 m/m)
- **Technical Declines:** 0.26%  (▼0.01 w/w, ▼0.19 m/m)
- **Business Declines:** 0.18%  (▲0.04 d/d, ▲0.04 w/w, ▼0.02 m/m)
- **Customer Complaints:** 1,105  (▲104 d/d, ▲80 w/w, ▼837 m/m)
- **Merchant Complaints:** 178  (▲78 d/d, ▲76 w/w, ▼33 m/m)
- **Fraud Alerts:** 728  (▼10 d/d, ▼19 w/w, ▼323 m/m)
- **Risk Score:** 20  (▼11 m/m)
- **Response Time:** 558 ms  (▼8 d/d, ▼12 w/w, ▼184 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 324.8 | 99.5% |
| HDFC Bank | 111.4 | 99.55% |
| Bank of Baroda | 80.1 | 99.64% |
| Union Bank of India | 69.6 | 99.43% |
| ICICI Bank | 62.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 481.9 | 99.14% | 231 ms |
| Google Pay | 329.9 | 99.17% | 316 ms |
| Paytm | 81.5 | 99.06% | 192 ms |
| Navi | 37.2 | 99.17% | 225 ms |
| SuperMoney | 19.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 378.8 |
| Person to Person | 358.6 |
| QR Payments | 96.0 |
| UPI Lite | 48.5 |
| UPI Autopay | 33.3 |

## Failure analysis
- INC-2026-17 — merchant settlement delay on IndusInd Bank (day 1 of 4); see RCA-2026-17.

## Recommendations
Stay on the open incident: keep recovery monitoring on IndusInd Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D145-MON) and any meetings/emails on 13 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D145-MON, RPT-D144-DAILY, INC-2026-17, RCA-2026-17

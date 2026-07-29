---
id: RPT-D58-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-18T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 18 Aug 2026)

**Report ID:** RPT-D58-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 18 Aug 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 58 of 180)

## Transaction summary
The rail processed 849.7M UPI transactions on Tuesday — a steady mid-week day — up 42.2M on the same day last week. Success landed at 99.98% and settlement at 98.1%, held back by live issues on ICICI Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 849.7  (▲29.2 d/d, ▲42.2 w/w, ▲104.8 m/m)
- **Success Rate:** 99.98%  (▲0.41 d/d, ▲0.38 m/m)
- **Settlement Success:** 98.1%  (▲0.16 d/d, ▼0.8 w/w, ▼1.33 m/m)
- **Technical Declines:** 0.36%  (▼0.01 w/w, ▼0.09 m/m)
- **Business Declines:** 0.23%  (▼0.03 d/d, ▲0.05 w/w, ▲0.03 m/m)
- **Customer Complaints:** 1,666  (▼148 d/d, ▲113 w/w, ▼276 m/m)
- **Merchant Complaints:** 282  (▼81 d/d, ▲119 w/w, ▲71 m/m)
- **Fraud Alerts:** 908  (▼12 d/d, ▼17 w/w, ▼143 m/m)
- **Risk Score:** 26  (▼1 w/w, ▼5 m/m)
- **Response Time:** 656 ms  (▼10 d/d, ▼8 w/w, ▼86 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 273.2 | 99.5% |
| HDFC Bank | 93.7 | 99.55% |
| Bank of Baroda | 67.4 | 99.64% |
| Union Bank of India | 58.5 | 99.43% |
| ICICI Bank | 52.4 | 98.04% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 405.4 | 99.14% | 231 ms |
| Google Pay | 277.5 | 99.17% | 316 ms |
| Paytm | 68.5 | 99.06% | 192 ms |
| Navi | 31.3 | 99.17% | 225 ms |
| SuperMoney | 16.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 318.6 |
| Person to Person | 301.6 |
| QR Payments | 80.7 |
| UPI Lite | 40.8 |
| UPI Autopay | 28.0 |

## Failure analysis
- INC-2026-03 — merchant settlement delay on ICICI Bank (day 2 of 4); see RCA-2026-03.

## Recommendations
Stay on the open incident: keep recovery monitoring on ICICI Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D58-MON) and any meetings/emails on 18 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D58-MON, RPT-D57-DAILY, INC-2026-03, RCA-2026-03

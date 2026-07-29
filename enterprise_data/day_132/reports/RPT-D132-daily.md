---
id: RPT-D132-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-31T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 31 Oct 2026)

**Report ID:** RPT-D132-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 31 Oct 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 132 of 180)

## Transaction summary
The rail processed 1074.1M UPI transactions on Saturday — the month-end surge as salary and bill-pay flows land — up 203.0M on the same day last week. Success landed at 99.98% and settlement at 98.94%, held back by live issues on TravelGo, InsureWell, Union Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1074.1  (▼15.8 d/d, ▲203.0 w/w, ▲329.2 m/m)
- **Success Rate:** 99.98%  (▲1.5 d/d, ▲0.2 w/w, ▲0.38 m/m)
- **Settlement Success:** 98.94%  (▼0.7 d/d, ▼1.04 w/w, ▼0.49 m/m)
- **Technical Declines:** 0.38%  (▼0.06 d/d, ▲0.1 w/w, ▼0.07 m/m)
- **Business Declines:** 0.15%  (▼0.01 d/d, ▼0.05 m/m)
- **Customer Complaints:** 1,335  (▼168 d/d, ▲242 w/w, ▼607 m/m)
- **Merchant Complaints:** 160  (▼41 d/d, ▲49 w/w, ▼51 m/m)
- **Fraud Alerts:** 760  (▼5 d/d, ▼8 w/w, ▼291 m/m)
- **Risk Score:** 20  (▼1 d/d, ▼1 w/w, ▼11 m/m)
- **Response Time:** 612 ms  (▼19 d/d, ▲24 w/w, ▼130 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 345.3 | 99.5% |
| HDFC Bank | 118.5 | 99.55% |
| Bank of Baroda | 85.2 | 99.64% |
| Union Bank of India | 74.0 | 98.99% |
| ICICI Bank | 66.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 512.4 | 99.14% | 231 ms |
| Google Pay | 350.8 | 99.17% | 316 ms |
| Paytm | 86.7 | 99.06% | 192 ms |
| Navi | 39.6 | 99.17% | 225 ms |
| SuperMoney | 20.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 402.8 |
| Person to Person | 381.3 |
| QR Payments | 102.0 |
| UPI Lite | 51.6 |
| UPI Autopay | 35.4 |

## Failure analysis
- INC-2026-24 — merchant decline-rate spike on TravelGo, InsureWell (day 4 of 5); see RCA-2026-24.
- INC-2026-10 — bank timeout / 5xx spike on Union Bank of India (day 2 of 2); see INC-2026-10.

## Recommendations
Stay on the open incidents: keep recovery monitoring on TravelGo, InsureWell, Union Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D132-MON) and any meetings/emails on 31 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D132-MON, RPT-D131-DAILY, INC-2026-24, INC-2026-10, RCA-2026-24

---
id: RPT-D174-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-12T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 12 Dec 2026)

**Report ID:** RPT-D174-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 12 Dec 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 174 of 180)

## Transaction summary
The rail processed 929.9M UPI transactions on Saturday — a lighter Saturday — down 6.0M on the same day last week. Success landed at 99.98% and settlement at 99.23%, held back by live issues on Bank of Baroda (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 929.9  (▼373.0 d/d, ▼6.0 w/w, ▲185.0 m/m)
- **Success Rate:** 99.98%  (▲0.8 d/d, ▲0.04 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.23%  (▼0.65 d/d, ▼0.75 w/w, ▼0.2 m/m)
- **Technical Declines:** 0.24%  (▲0.01 d/d, ▼0.07 w/w, ▼0.21 m/m)
- **Business Declines:** 0.14%  (▲0.01 w/w, ▼0.06 m/m)
- **Customer Complaints:** 870  (▼23 d/d, ▼177 w/w, ▼1072 m/m)
- **Merchant Complaints:** 97  (▼13 d/d, ▲8 w/w, ▼114 m/m)
- **Fraud Alerts:** 677  (▼10 d/d, ▼11 w/w, ▼374 m/m)
- **Risk Score:** 18  (▼1 w/w, ▼13 m/m)
- **Response Time:** 530 ms  (▼10 d/d, ▼39 w/w, ▼212 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 299.0 | 99.5% |
| HDFC Bank | 102.6 | 99.55% |
| Bank of Baroda | 73.7 | 99.52% |
| Union Bank of India | 64.1 | 99.43% |
| ICICI Bank | 57.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 443.6 | 99.14% | 231 ms |
| Google Pay | 303.7 | 99.17% | 316 ms |
| Paytm | 75.0 | 99.06% | 192 ms |
| Navi | 34.3 | 99.17% | 225 ms |
| SuperMoney | 18.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 348.7 |
| Person to Person | 330.1 |
| QR Payments | 88.3 |
| UPI Lite | 44.6 |
| UPI Autopay | 30.7 |

## Failure analysis
- INC-2026-15 — merchant settlement delay on Bank of Baroda (day 4 of 4); see RCA-2026-15.

## Recommendations
Stay on the open incident: keep recovery monitoring on Bank of Baroda and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D174-MON) and any meetings/emails on 12 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D174-MON, RPT-D173-DAILY, INC-2026-15, RCA-2026-15

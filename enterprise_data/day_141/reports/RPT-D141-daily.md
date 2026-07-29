---
id: RPT-D141-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-09T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 09 Nov 2026)

**Report ID:** RPT-D141-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 09 Nov 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 141 of 180)

## Transaction summary
The rail processed 950.4M UPI transactions on Monday — the Monday ramp-up after the weekend — up 3.7M on the same day last week. Success landed at 99.76% and settlement at 99.98%, held back by live issues on BHIM (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 950.4  (▲146.3 d/d, ▲3.7 w/w, ▲205.5 m/m)
- **Success Rate:** 99.76%  (▲0.44 d/d, ▲0.75 w/w, ▲0.16 m/m)
- **Settlement Success:** 99.98%  (▲0.94 d/d, ▲0.11 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.29%  (▼0.03 d/d, ▲0.02 w/w, ▼0.16 m/m)
- **Business Declines:** 0.14%  (▼0.06 m/m)
- **Customer Complaints:** 1,097  (▼76 d/d, ▲61 w/w, ▼845 m/m)
- **Merchant Complaints:** 102  (▼1 d/d, ▼3 w/w, ▼109 m/m)
- **Fraud Alerts:** 741  (▼1 d/d, ▼17 w/w, ▼310 m/m)
- **Risk Score:** 20  (▼11 m/m)
- **Response Time:** 589 ms  (▼25 d/d, ▲11 w/w, ▼153 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 305.6 | 99.5% |
| HDFC Bank | 104.8 | 99.55% |
| Bank of Baroda | 75.4 | 99.64% |
| Union Bank of India | 65.5 | 99.43% |
| ICICI Bank | 58.6 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 453.4 | 99.14% | 231 ms |
| Google Pay | 310.4 | 99.17% | 316 ms |
| Paytm | 76.7 | 99.06% | 192 ms |
| Navi | 35.0 | 99.17% | 225 ms |
| SuperMoney | 18.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 356.4 |
| Person to Person | 337.4 |
| QR Payments | 90.3 |
| UPI Lite | 45.6 |
| UPI Autopay | 31.4 |

## Failure analysis
- INC-2026-25 — PSP callback latency increase on BHIM (day 3 of 5); see RCA-2026-25.

## Recommendations
Stay on the open incident: keep recovery monitoring on BHIM and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D141-MON) and any meetings/emails on 09 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D141-MON, RPT-D140-DAILY, INC-2026-25, RCA-2026-25

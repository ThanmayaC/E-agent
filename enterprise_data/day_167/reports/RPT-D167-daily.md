---
id: RPT-D167-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-12-05T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 05 Dec 2026)

**Report ID:** RPT-D167-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 05 Dec 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 167 of 180)

## Transaction summary
The rail processed 935.9M UPI transactions on Saturday — a lighter Saturday — down 182.0M on the same day last week. Success landed at 99.94% and settlement at 99.98%, held back by live issues on QR Payments (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 935.9  (▼75.3 d/d, ▼182.0 w/w, ▲191.0 m/m)
- **Success Rate:** 99.94%  (▲0.01 d/d, ▼0.04 w/w, ▲0.34 m/m)
- **Settlement Success:** 99.98%  (▲0.55 m/m)
- **Technical Declines:** 0.31%  (▼0.05 d/d, ▲0.06 w/w, ▼0.14 m/m)
- **Business Declines:** 0.13%  (▼0.07 m/m)
- **Customer Complaints:** 1,047  (▼109 d/d, ▲124 w/w, ▼895 m/m)
- **Merchant Complaints:** 89  (▼3 w/w, ▼122 m/m)
- **Fraud Alerts:** 688  (▼6 d/d, ▼23 w/w, ▼363 m/m)
- **Risk Score:** 19  (▲1 d/d, ▼12 m/m)
- **Response Time:** 569 ms  (▼15 d/d, ▲25 w/w, ▼173 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 300.9 | 99.5% |
| HDFC Bank | 103.2 | 99.55% |
| Bank of Baroda | 74.2 | 99.64% |
| Union Bank of India | 64.5 | 99.43% |
| ICICI Bank | 57.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 446.5 | 99.14% | 231 ms |
| Google Pay | 305.7 | 99.17% | 316 ms |
| Paytm | 75.5 | 99.06% | 192 ms |
| Navi | 34.5 | 99.17% | 225 ms |
| SuperMoney | 18.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 351.0 |
| Person to Person | 332.2 |
| QR Payments | 88.9 |
| UPI Lite | 44.9 |
| UPI Autopay | 30.9 |

## Failure analysis
- INC-2026-21 — feature-level degradation on QR Payments (day 2 of 5); see RCA-2026-21.

## Recommendations
Stay on the open incident: keep recovery monitoring on QR Payments and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D167-MON) and any meetings/emails on 05 Dec.

Refs: upi_kpis_month.xlsx, TEAMS-D167-MON, RPT-D166-DAILY, INC-2026-21, RCA-2026-21

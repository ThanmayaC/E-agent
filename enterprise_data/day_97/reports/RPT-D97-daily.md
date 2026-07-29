---
id: RPT-D97-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-26T17:30:00
---

# UPI Products — Daily Operations Report (Saturday, 26 Sep 2026)

**Report ID:** RPT-D97-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Saturday 26 Sep 2026  ·  **Day archetype:** Saturday (lighter)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 97 of 180)

## Transaction summary
The rail processed 817.0M UPI transactions on Saturday — a lighter Saturday — up 26.3M on the same day last week. Success landed at 99.98% and settlement at 98.95%, held back by live issues on iMobile Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 817.0  (▼73.0 d/d, ▲26.3 w/w, ▲72.1 m/m)
- **Success Rate:** 99.98%  (▲1.15 d/d, ▲0.55 w/w, ▲0.38 m/m)
- **Settlement Success:** 98.95%  (▼0.97 d/d, ▼0.81 w/w, ▼0.48 m/m)
- **Technical Declines:** 0.31%  (▼0.01 w/w, ▼0.14 m/m)
- **Business Declines:** 0.2%  (▼0.03 d/d, ▲0.04 w/w)
- **Customer Complaints:** 1,399  (▼110 d/d, ▲109 w/w, ▼543 m/m)
- **Merchant Complaints:** 128  (▼1 d/d, ▼3 w/w, ▼83 m/m)
- **Fraud Alerts:** 922  (▼76 d/d, ▲79 w/w, ▼129 m/m)
- **Risk Score:** 29  (▼6 d/d, ▲6 w/w, ▼2 m/m)
- **Response Time:** 613 ms  (▲1 d/d, ▼13 w/w, ▼129 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 262.7 | 99.5% |
| HDFC Bank | 90.1 | 99.55% |
| Bank of Baroda | 64.8 | 99.64% |
| Union Bank of India | 56.3 | 99.43% |
| ICICI Bank | 50.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 389.8 | 99.14% | 231 ms |
| Google Pay | 266.9 | 99.17% | 316 ms |
| Paytm | 65.9 | 99.06% | 192 ms |
| Navi | 30.1 | 99.17% | 225 ms |
| SuperMoney | 15.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 306.4 |
| Person to Person | 290.0 |
| QR Payments | 77.6 |
| UPI Lite | 39.2 |
| UPI Autopay | 27.0 |

## Failure analysis
- INC-2026-04 — fraud / risk spike on iMobile Pay (day 3 of 5); see RCA-2026-04.

## Recommendations
Stay on the open incident: keep recovery monitoring on iMobile Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D97-MON) and any meetings/emails on 26 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D97-MON, RPT-D96-DAILY, INC-2026-04, RCA-2026-04

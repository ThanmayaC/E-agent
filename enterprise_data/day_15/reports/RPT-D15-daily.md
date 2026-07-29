---
id: RPT-D15-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-06T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 06 Jul 2026)

**Report ID:** RPT-D15-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 06 Jul 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 15 of 180)

## Transaction summary
The rail processed 743.9M UPI transactions on Monday — the Monday ramp-up after the weekend — down 117.9M on the same day last week. Success landed at 99.57% and settlement at 99.47%, held back by live issues on YONO SBI (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 743.9  (▲123.2 d/d, ▼117.9 w/w, ▼1.0 m/m)
- **Success Rate:** 99.57%  (▲0.94 d/d, ▼0.41 w/w, ▼0.03 m/m)
- **Settlement Success:** 99.47%  (▼0.51 d/d, ▼0.51 w/w, ▲0.04 m/m)
- **Technical Declines:** 0.43%  (▼0.02 d/d, ▼0.01 w/w, ▼0.02 m/m)
- **Business Declines:** 0.34%  (▲0.15 d/d, ▲0.14 w/w, ▲0.14 m/m)
- **Customer Complaints:** 2,484  (▲572 d/d, ▲589 w/w, ▲542 m/m)
- **Merchant Complaints:** 196  (▼2 d/d, ▼8 w/w, ▼15 m/m)
- **Fraud Alerts:** 1,348  (▲330 d/d, ▲323 w/w, ▲297 m/m)
- **Risk Score:** 55  (▲25 d/d, ▲25 w/w, ▲24 m/m)
- **Response Time:** 723 ms  (▼11 d/d, ▲4 w/w, ▼19 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 239.2 | 99.5% |
| HDFC Bank | 82.1 | 99.55% |
| Bank of Baroda | 59.0 | 99.64% |
| Union Bank of India | 51.2 | 99.43% |
| ICICI Bank | 45.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 354.9 | 99.14% | 231 ms |
| Google Pay | 243.0 | 99.17% | 316 ms |
| Paytm | 60.0 | 99.06% | 192 ms |
| Navi | 27.4 | 99.17% | 225 ms |
| SuperMoney | 14.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 279.0 |
| Person to Person | 264.1 |
| QR Payments | 70.7 |
| UPI Lite | 35.7 |
| UPI Autopay | 24.5 |

## Failure analysis
- INC-2026-09 — fraud / risk spike on YONO SBI (day 1 of 3); see RCA-2026-09.

## Recommendations
Stay on the open incident: keep recovery monitoring on YONO SBI and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D15-MON) and any meetings/emails on 06 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D15-MON, RPT-D14-DAILY, INC-2026-09, RCA-2026-09

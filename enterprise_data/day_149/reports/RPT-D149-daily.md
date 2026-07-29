---
id: RPT-D149-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-17T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 17 Nov 2026)

**Report ID:** RPT-D149-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 17 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 149 of 180)

## Transaction summary
The rail processed 1015.5M UPI transactions on Tuesday — a steady mid-week day — up 21.4M on the same day last week. Success landed at 99.69% and settlement at 99.98%, held back by live issues on FamApp (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1015.5  (▲64.1 d/d, ▲21.4 w/w, ▲270.6 m/m)
- **Success Rate:** 99.69%  (▲0.19 d/d, ▲0.69 w/w, ▲0.09 m/m)
- **Settlement Success:** 99.98%  (▲0.89 d/d, ▲0.55 m/m)
- **Technical Declines:** 0.26%  (▼0.02 w/w, ▼0.19 m/m)
- **Business Declines:** 0.17%  (▼0.04 d/d, ▲0.03 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,086  (▼115 d/d, ▲39 w/w, ▼856 m/m)
- **Merchant Complaints:** 98  (▼13 d/d, ▼3 w/w, ▼113 m/m)
- **Fraud Alerts:** 812  (▼66 d/d, ▲69 w/w, ▼239 m/m)
- **Risk Score:** 25  (▼5 d/d, ▲5 w/w, ▼6 m/m)
- **Response Time:** 560 ms  (▼2 d/d, ▼17 w/w, ▼182 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 326.5 | 99.5% |
| HDFC Bank | 112.0 | 99.55% |
| Bank of Baroda | 80.5 | 99.64% |
| Union Bank of India | 70.0 | 99.43% |
| ICICI Bank | 62.6 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 484.5 | 99.14% | 231 ms |
| Google Pay | 331.7 | 99.17% | 316 ms |
| Paytm | 81.9 | 99.06% | 192 ms |
| Navi | 37.4 | 99.17% | 225 ms |
| SuperMoney | 19.8 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 380.8 |
| Person to Person | 360.5 |
| QR Payments | 96.5 |
| UPI Lite | 48.7 |
| UPI Autopay | 33.5 |

## Failure analysis
- INC-2026-26 — fraud / risk spike on FamApp (day 3 of 3); see RCA-2026-26.

## Recommendations
Stay on the open incident: keep recovery monitoring on FamApp and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D149-MON) and any meetings/emails on 17 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D149-MON, RPT-D148-DAILY, INC-2026-26, RCA-2026-26

---
id: RPT-D128-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-27T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 27 Oct 2026)

**Report ID:** RPT-D128-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 27 Oct 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 128 of 180)

## Transaction summary
The rail processed 986.5M UPI transactions on Tuesday — a steady mid-week day — up 54.5M on the same day last week. Success landed at 99.98% and settlement at 99.72%, held back by live issues on Union Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 986.5  (▲61.2 d/d, ▲54.5 w/w, ▲241.6 m/m)
- **Success Rate:** 99.98%  (▲1.2 d/d, ▲0.22 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.72%  (▲0.83 d/d, ▲0.11 w/w, ▲0.29 m/m)
- **Technical Declines:** 0.37%  (▼0.09 d/d, ▲0.08 w/w, ▼0.08 m/m)
- **Business Declines:** 0.15%  (▼0.05 m/m)
- **Customer Complaints:** 1,319  (▼228 d/d, ▲214 w/w, ▼623 m/m)
- **Merchant Complaints:** 151  (▼32 d/d, ▲38 w/w, ▼60 m/m)
- **Fraud Alerts:** 772  (▲7 d/d, ▼3 w/w, ▼279 m/m)
- **Risk Score:** 21  (▼10 m/m)
- **Response Time:** 617 ms  (▼19 d/d, ▲24 w/w, ▼125 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 317.2 | 99.5% |
| HDFC Bank | 108.8 | 99.55% |
| Bank of Baroda | 78.2 | 99.64% |
| Union Bank of India | 68.0 | 98.69% |
| ICICI Bank | 60.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 470.6 | 99.14% | 231 ms |
| Google Pay | 322.2 | 99.17% | 316 ms |
| Paytm | 79.6 | 99.06% | 192 ms |
| Navi | 36.4 | 99.17% | 225 ms |
| SuperMoney | 19.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 369.9 |
| Person to Person | 350.2 |
| QR Payments | 93.7 |
| UPI Lite | 47.4 |
| UPI Autopay | 32.6 |

## Failure analysis
- INC-2026-05 — bank timeout / 5xx spike on Union Bank of India (day 3 of 5); see RCA-2026-05.

## Recommendations
Stay on the open incident: keep recovery monitoring on Union Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D128-MON) and any meetings/emails on 27 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D128-MON, RPT-D127-DAILY, INC-2026-05, RCA-2026-05

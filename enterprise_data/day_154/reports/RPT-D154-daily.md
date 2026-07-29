---
id: RPT-D154-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-22T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 22 Nov 2026)

**Report ID:** RPT-D154-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 22 Nov 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 154 of 180)

## Transaction summary
The rail processed 842.1M UPI transactions on Sunday — a quiet Sunday — up 39.7M on the same day last week. Success landed at 99.98% and settlement at 99.98%, held back by live issues on HDFC MobileBanking (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 842.1  (▼63.2 d/d, ▲39.7 w/w, ▲97.2 m/m)
- **Success Rate:** 99.98%  (▲0.68 d/d, ▲1.41 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲0.39 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.25%  (▼0.01 w/w, ▼0.2 m/m)
- **Business Declines:** 0.15%  (▼0.02 d/d, ▼0.11 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,001  (▼65 d/d, ▼353 w/w, ▼941 m/m)
- **Merchant Complaints:** 95  (▼1 d/d, ▼29 w/w, ▼116 m/m)
- **Fraud Alerts:** 753  (▼45 d/d, ▼231 w/w, ▼298 m/m)
- **Risk Score:** 22  (▼3 d/d, ▼14 w/w, ▼9 m/m)
- **Response Time:** 551 ms  (▼7 d/d, ▼8 w/w, ▼191 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 270.8 | 99.5% |
| HDFC Bank | 92.9 | 99.55% |
| Bank of Baroda | 66.8 | 99.64% |
| Union Bank of India | 58.0 | 99.43% |
| ICICI Bank | 51.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 401.7 | 99.14% | 231 ms |
| Google Pay | 275.1 | 99.17% | 316 ms |
| Paytm | 67.9 | 99.06% | 192 ms |
| Navi | 31.0 | 99.17% | 225 ms |
| SuperMoney | 16.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 315.8 |
| Person to Person | 298.9 |
| QR Payments | 80.0 |
| UPI Lite | 40.4 |
| UPI Autopay | 27.8 |

## Failure analysis
- INC-2026-06 — fraud / risk spike on HDFC MobileBanking (day 4 of 5); see RCA-2026-06.

## Recommendations
Stay on the open incident: keep recovery monitoring on HDFC MobileBanking and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D154-MON) and any meetings/emails on 22 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D154-MON, RPT-D153-DAILY, INC-2026-06, RCA-2026-06

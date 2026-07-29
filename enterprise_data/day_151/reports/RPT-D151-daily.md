---
id: RPT-D151-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-19T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 19 Nov 2026)

**Report ID:** RPT-D151-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 19 Nov 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 151 of 180)

## Transaction summary
The rail processed 993.4M UPI transactions on Thursday — a steady mid-week day — up 4.1M on the same day last week. Success landed at 99.92% and settlement at 99.98%, held back by live issues on HDFC MobileBanking (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 993.4  (▼4.0 d/d, ▲4.1 w/w, ▲248.5 m/m)
- **Success Rate:** 99.92%  (▼0.06 d/d, ▼0.06 w/w, ▲0.32 m/m)
- **Settlement Success:** 99.98%  (▲0.55 m/m)
- **Technical Declines:** 0.25%  (▼0.01 w/w, ▼0.2 m/m)
- **Business Declines:** 0.24%  (▲0.1 d/d, ▲0.1 w/w, ▲0.04 m/m)
- **Customer Complaints:** 1,288  (▲329 d/d, ▲287 w/w, ▼654 m/m)
- **Merchant Complaints:** 96  (▼1 d/d, ▼4 w/w, ▼115 m/m)
- **Fraud Alerts:** 969  (▲241 d/d, ▲231 w/w, ▼82 m/m)
- **Risk Score:** 36  (▲17 d/d, ▲16 w/w, ▲5 m/m)
- **Response Time:** 561 ms  (▲2 d/d, ▼5 w/w, ▼181 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 319.4 | 99.5% |
| HDFC Bank | 109.6 | 99.55% |
| Bank of Baroda | 78.8 | 99.64% |
| Union Bank of India | 68.4 | 99.43% |
| ICICI Bank | 61.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 473.9 | 99.14% | 231 ms |
| Google Pay | 324.5 | 99.17% | 316 ms |
| Paytm | 80.1 | 99.06% | 192 ms |
| Navi | 36.6 | 99.17% | 225 ms |
| SuperMoney | 19.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 372.5 |
| Person to Person | 352.7 |
| QR Payments | 94.4 |
| UPI Lite | 47.7 |
| UPI Autopay | 32.8 |

## Failure analysis
- INC-2026-06 — fraud / risk spike on HDFC MobileBanking (day 1 of 5); see RCA-2026-06.

## Recommendations
Stay on the open incident: keep recovery monitoring on HDFC MobileBanking and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D151-MON) and any meetings/emails on 19 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D151-MON, RPT-D150-DAILY, INC-2026-06, RCA-2026-06

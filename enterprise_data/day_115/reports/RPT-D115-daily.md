---
id: RPT-D115-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-14T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 14 Oct 2026)

**Report ID:** RPT-D115-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 14 Oct 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 115 of 180)

## Transaction summary
The rail processed 938.6M UPI transactions on Wednesday — a steady mid-week day — up 9.2M on the same day last week. Success landed at 99.2% and settlement at 99.93%, held back by live issues on WhatsApp Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 938.6  (▼16.2 d/d, ▲9.2 w/w, ▲193.7 m/m)
- **Success Rate:** 99.2%  (▲0.47 d/d, ▼0.78 w/w, ▼0.4 m/m)
- **Settlement Success:** 99.93%  (▼0.05 d/d, ▼0.05 w/w, ▲0.5 m/m)
- **Technical Declines:** 0.29%  (▼0.01 w/w, ▼0.16 m/m)
- **Business Declines:** 0.17%  (▼0.02 d/d, ▲0.02 w/w, ▼0.03 m/m)
- **Customer Complaints:** 1,230  (▼67 d/d, ▲49 w/w, ▼712 m/m)
- **Merchant Complaints:** 117  (▼1 d/d, ▼4 w/w, ▼94 m/m)
- **Fraud Alerts:** 848  (▼52 d/d, ▲47 w/w, ▼203 m/m)
- **Risk Score:** 26  (▼3 d/d, ▲4 w/w, ▼5 m/m)
- **Response Time:** 595 ms  (▼8 w/w, ▼147 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 301.8 | 99.5% |
| HDFC Bank | 103.5 | 99.55% |
| Bank of Baroda | 74.4 | 99.64% |
| Union Bank of India | 64.7 | 99.43% |
| ICICI Bank | 57.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 447.8 | 99.14% | 231 ms |
| Google Pay | 306.6 | 99.17% | 316 ms |
| Paytm | 75.7 | 99.06% | 192 ms |
| Navi | 34.6 | 99.17% | 225 ms |
| SuperMoney | 18.3 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 352.0 |
| Person to Person | 333.2 |
| QR Payments | 89.2 |
| UPI Lite | 45.1 |
| UPI Autopay | 31.0 |

## Failure analysis
- INC-2026-19 — fraud / risk spike on WhatsApp Pay (day 3 of 5); see RCA-2026-19.

## Recommendations
Stay on the open incident: keep recovery monitoring on WhatsApp Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D115-MON) and any meetings/emails on 14 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D115-MON, RPT-D114-DAILY, INC-2026-19, RCA-2026-19

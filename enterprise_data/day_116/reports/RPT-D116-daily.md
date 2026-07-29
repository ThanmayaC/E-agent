---
id: RPT-D116-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-15T17:30:00
---

# UPI Products — Daily Operations Report (Thursday, 15 Oct 2026)

**Report ID:** RPT-D116-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Thursday 15 Oct 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 116 of 180)

## Transaction summary
The rail processed 929.5M UPI transactions on Thursday — a steady mid-week day — up 15.3M on the same day last week. Success landed at 99.35% and settlement at 99.69%, held back by live issues on WhatsApp Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 929.5  (▼9.1 d/d, ▲15.3 w/w, ▲184.6 m/m)
- **Success Rate:** 99.35%  (▲0.15 d/d, ▼0.09 w/w, ▼0.25 m/m)
- **Settlement Success:** 99.69%  (▼0.24 d/d, ▲0.51 w/w, ▲0.26 m/m)
- **Technical Declines:** 0.29%  (▼0.01 w/w, ▼0.16 m/m)
- **Business Declines:** 0.16%  (▼0.01 d/d, ▲0.01 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,171  (▼59 d/d, ▲7 w/w, ▼771 m/m)
- **Merchant Complaints:** 116  (▼1 d/d, ▼5 w/w, ▼95 m/m)
- **Fraud Alerts:** 820  (▼28 d/d, ▲11 w/w, ▼231 m/m)
- **Risk Score:** 24  (▼2 d/d, ▲2 w/w, ▼7 m/m)
- **Response Time:** 597 ms  (▲2 d/d, ▼7 w/w, ▼145 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 298.9 | 99.5% |
| HDFC Bank | 102.5 | 99.55% |
| Bank of Baroda | 73.7 | 99.64% |
| Union Bank of India | 64.0 | 99.43% |
| ICICI Bank | 57.3 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 443.4 | 99.14% | 231 ms |
| Google Pay | 303.6 | 99.17% | 316 ms |
| Paytm | 75.0 | 99.06% | 192 ms |
| Navi | 34.3 | 99.17% | 225 ms |
| SuperMoney | 18.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 348.6 |
| Person to Person | 330.0 |
| QR Payments | 88.3 |
| UPI Lite | 44.6 |
| UPI Autopay | 30.7 |

## Failure analysis
- INC-2026-19 — fraud / risk spike on WhatsApp Pay (day 4 of 5); see RCA-2026-19.

## Recommendations
Stay on the open incident: keep recovery monitoring on WhatsApp Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D116-MON) and any meetings/emails on 15 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D116-MON, RPT-D115-DAILY, INC-2026-19, RCA-2026-19

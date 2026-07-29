---
id: RPT-D114-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-13T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 13 Oct 2026)

**Report ID:** RPT-D114-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 13 Oct 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 114 of 180)

## Transaction summary
The rail processed 954.8M UPI transactions on Tuesday — a steady mid-week day — up 19.5M on the same day last week. Success landed at 98.73% and settlement at 99.98%, held back by live issues on WhatsApp Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 954.8  (▲60.1 d/d, ▲19.5 w/w, ▲209.9 m/m)
- **Success Rate:** 98.73%  (▼1.18 d/d, ▼0.08 w/w, ▼0.87 m/m)
- **Settlement Success:** 99.98%  (▲0.02 d/d, ▲0.07 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.29%  (▼0.01 w/w, ▼0.16 m/m)
- **Business Declines:** 0.19%  (▼0.03 d/d, ▲0.04 w/w, ▼0.01 m/m)
- **Customer Complaints:** 1,297  (▼100 d/d, ▲125 w/w, ▼645 m/m)
- **Merchant Complaints:** 118  (▼3 w/w, ▼93 m/m)
- **Fraud Alerts:** 900  (▼55 d/d, ▲101 w/w, ▼151 m/m)
- **Risk Score:** 29  (▼4 d/d, ▲7 w/w, ▼2 m/m)
- **Response Time:** 595 ms  (▲1 d/d, ▼9 w/w, ▼147 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 307.0 | 99.5% |
| HDFC Bank | 105.3 | 99.55% |
| Bank of Baroda | 75.7 | 99.64% |
| Union Bank of India | 65.8 | 99.43% |
| ICICI Bank | 58.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 455.5 | 99.14% | 231 ms |
| Google Pay | 311.9 | 99.17% | 316 ms |
| Paytm | 77.0 | 99.06% | 192 ms |
| Navi | 35.2 | 99.17% | 225 ms |
| SuperMoney | 18.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 358.0 |
| Person to Person | 339.0 |
| QR Payments | 90.7 |
| UPI Lite | 45.8 |
| UPI Autopay | 31.5 |

## Failure analysis
- INC-2026-19 — fraud / risk spike on WhatsApp Pay (day 2 of 5); see RCA-2026-19.

## Recommendations
Stay on the open incident: keep recovery monitoring on WhatsApp Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D114-MON) and any meetings/emails on 13 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D114-MON, RPT-D113-DAILY, INC-2026-19, RCA-2026-19

---
id: RPT-D16-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-07T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 07 Jul 2026)

**Report ID:** RPT-D16-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 07 Jul 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 16 of 180)

## Transaction summary
The rail processed 760.3M UPI transactions on Tuesday — a steady mid-week day — down 90.1M on the same day last week. Success landed at 98.48% and settlement at 99.47%, held back by live issues on YONO SBI (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 760.3  (▲16.4 d/d, ▼90.1 w/w, ▲15.4 m/m)
- **Success Rate:** 98.48%  (▼1.09 d/d, ▼1.24 w/w, ▼1.12 m/m)
- **Settlement Success:** 99.47%  (▼0.51 w/w, ▲0.04 m/m)
- **Technical Declines:** 0.42%  (▼0.01 d/d, ▼0.16 w/w, ▼0.03 m/m)
- **Business Declines:** 0.28%  (▼0.06 d/d, ▲0.08 w/w, ▲0.08 m/m)
- **Customer Complaints:** 2,202  (▼282 d/d, ▼188 w/w, ▲260 m/m)
- **Merchant Complaints:** 195  (▼1 d/d, ▼5 w/w, ▼16 m/m)
- **Fraud Alerts:** 1,213  (▼135 d/d, ▲190 w/w, ▲162 m/m)
- **Risk Score:** 45  (▼10 d/d, ▲15 w/w, ▲14 m/m)
- **Response Time:** 711 ms  (▼12 d/d, ▼115 w/w, ▼31 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 244.5 | 99.5% |
| HDFC Bank | 83.9 | 99.55% |
| Bank of Baroda | 60.3 | 99.64% |
| Union Bank of India | 52.4 | 99.43% |
| ICICI Bank | 46.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 362.7 | 99.14% | 231 ms |
| Google Pay | 248.3 | 99.17% | 316 ms |
| Paytm | 61.3 | 99.06% | 192 ms |
| Navi | 28.0 | 99.17% | 225 ms |
| SuperMoney | 14.8 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 285.1 |
| Person to Person | 269.9 |
| QR Payments | 72.2 |
| UPI Lite | 36.5 |
| UPI Autopay | 25.1 |

## Failure analysis
- INC-2026-09 — fraud / risk spike on YONO SBI (day 2 of 3); see RCA-2026-09.

## Recommendations
Stay on the open incident: keep recovery monitoring on YONO SBI and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D16-MON) and any meetings/emails on 07 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D16-MON, RPT-D15-DAILY, INC-2026-09, RCA-2026-09

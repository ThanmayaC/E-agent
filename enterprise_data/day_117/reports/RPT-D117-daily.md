---
id: RPT-D117-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-16T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 16 Oct 2026)

**Report ID:** RPT-D117-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 16 Oct 2026  ·  **Day archetype:** Weekday (steady)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 117 of 180)

## Transaction summary
The rail processed 936.1M UPI transactions on Friday — a steady mid-week day — up 34.2M on the same day last week. Success landed at 99.25% and settlement at 99.83%, held back by live issues on CRED, WhatsApp Pay (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 936.1  (▲6.6 d/d, ▲34.2 w/w, ▲191.2 m/m)
- **Success Rate:** 99.25%  (▼0.1 d/d, ▼0.16 w/w, ▼0.35 m/m)
- **Settlement Success:** 99.83%  (▲0.14 d/d, ▼0.15 w/w, ▲0.4 m/m)
- **Technical Declines:** 0.39%  (▲0.1 d/d, ▲0.09 w/w, ▼0.06 m/m)
- **Business Declines:** 0.15%  (▼0.01 d/d, ▼0.05 m/m)
- **Customer Complaints:** 1,459  (▲288 d/d, ▲290 w/w, ▼483 m/m)
- **Merchant Complaints:** 114  (▼2 d/d, ▼5 w/w, ▼97 m/m)
- **Fraud Alerts:** 790  (▼30 d/d, ▼16 w/w, ▼261 m/m)
- **Risk Score:** 23  (▼1 d/d, ▲1 w/w, ▼8 m/m)
- **Response Time:** 675 ms  (▲78 d/d, ▲74 w/w, ▼67 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 301.0 | 99.5% |
| HDFC Bank | 103.3 | 99.55% |
| Bank of Baroda | 74.2 | 99.64% |
| Union Bank of India | 64.5 | 99.43% |
| ICICI Bank | 57.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 446.6 | 99.14% | 231 ms |
| Google Pay | 305.8 | 99.17% | 316 ms |
| Paytm | 75.5 | 99.06% | 192 ms |
| Navi | 34.5 | 99.17% | 225 ms |
| SuperMoney | 18.2 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 351.0 |
| Person to Person | 332.3 |
| QR Payments | 88.9 |
| UPI Lite | 44.9 |
| UPI Autopay | 30.9 |

## Failure analysis
- INC-2026-19 — fraud / risk spike on WhatsApp Pay (day 5 of 5); see RCA-2026-19.
- INC-2026-08 — PSP callback latency increase on CRED (day 1 of 4); see RCA-2026-08.

## Recommendations
Stay on the open incidents: keep recovery monitoring on CRED, WhatsApp Pay and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D117-MON) and any meetings/emails on 16 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D117-MON, RPT-D116-DAILY, INC-2026-19, INC-2026-08, RCA-2026-19, RCA-2026-08

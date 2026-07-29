---
id: RPT-D85-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-09-14T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 14 Sep 2026)

**Report ID:** RPT-D85-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 14 Sep 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 85 of 180)

## Transaction summary
The rail processed 842.8M UPI transactions on Monday — the Monday ramp-up after the weekend — down 12.4M on the same day last week. Success landed at 99.02% and settlement at 99.55%, held back by live issues on Axis Mobile (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 842.8  (▲127.3 d/d, ▼12.4 w/w, ▲97.9 m/m)
- **Success Rate:** 99.02%  (▲0.24 d/d, ▼0.96 w/w, ▼0.58 m/m)
- **Settlement Success:** 99.55%  (▼0.43 d/d, ▼0.43 w/w, ▲0.12 m/m)
- **Technical Declines:** 0.43%  (▲0.1 d/d, ▲0.09 w/w, ▼0.02 m/m)
- **Business Declines:** 0.16%  (▼0.04 m/m)
- **Customer Complaints:** 1,651  (▲344 d/d, ▲289 w/w, ▼291 m/m)
- **Merchant Complaints:** 136  (▼1 d/d, ▼4 w/w, ▼75 m/m)
- **Fraud Alerts:** 854  (▲6 d/d, ▼8 w/w, ▼197 m/m)
- **Risk Score:** 24  (▼7 m/m)
- **Response Time:** 707 ms  (▲74 d/d, ▲69 w/w, ▼35 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 271.0 | 99.5% |
| HDFC Bank | 93.0 | 99.55% |
| Bank of Baroda | 66.8 | 99.64% |
| Union Bank of India | 58.1 | 99.43% |
| ICICI Bank | 52.0 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 402.1 | 99.14% | 231 ms |
| Google Pay | 275.3 | 99.17% | 316 ms |
| Paytm | 68.0 | 99.06% | 192 ms |
| Navi | 31.1 | 99.17% | 225 ms |
| SuperMoney | 16.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 316.0 |
| Person to Person | 299.2 |
| QR Payments | 80.1 |
| UPI Lite | 40.5 |
| UPI Autopay | 27.8 |

## Failure analysis
- INC-2026-14 — PSP callback latency increase on Axis Mobile (day 1 of 5); see RCA-2026-14.

## Recommendations
Stay on the open incident: keep recovery monitoring on Axis Mobile and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D85-MON) and any meetings/emails on 14 Sep.

Refs: upi_kpis_month.xlsx, TEAMS-D85-MON, RPT-D84-DAILY, INC-2026-14, RCA-2026-14

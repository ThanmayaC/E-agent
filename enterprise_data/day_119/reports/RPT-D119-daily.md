---
id: RPT-D119-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-18T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 18 Oct 2026)

**Report ID:** RPT-D119-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 18 Oct 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 119 of 180)

## Transaction summary
The rail processed 764.5M UPI transactions on Sunday — a quiet Sunday — up 14.0M on the same day last week. Success landed at 99.98% and settlement at 99.46%, held back by live issues on CRED (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 764.5  (▼85.9 d/d, ▲14.0 w/w, ▲19.6 m/m)
- **Success Rate:** 99.98%  (▲0.38 m/m)
- **Settlement Success:** 99.46%  (▲0.47 d/d, ▼0.52 w/w, ▲0.03 m/m)
- **Technical Declines:** 0.32%  (▼0.03 d/d, ▲0.03 w/w, ▼0.13 m/m)
- **Business Declines:** 0.15%  (▼0.05 m/m)
- **Customer Complaints:** 1,210  (▼107 d/d, ▲64 w/w, ▼732 m/m)
- **Merchant Complaints:** 114  (▼1 d/d, ▼4 w/w, ▼97 m/m)
- **Fraud Alerts:** 782  (▲3 d/d, ▼8 w/w, ▼269 m/m)
- **Risk Score:** 21  (▼1 w/w, ▼10 m/m)
- **Response Time:** 613 ms  (▼24 d/d, ▲13 w/w, ▼129 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 245.8 | 99.5% |
| HDFC Bank | 84.3 | 99.55% |
| Bank of Baroda | 60.6 | 99.64% |
| Union Bank of India | 52.7 | 99.43% |
| ICICI Bank | 47.1 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 364.7 | 99.14% | 231 ms |
| Google Pay | 249.7 | 99.17% | 316 ms |
| Paytm | 61.7 | 99.06% | 192 ms |
| Navi | 28.2 | 99.17% | 225 ms |
| SuperMoney | 14.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 286.7 |
| Person to Person | 271.4 |
| QR Payments | 72.6 |
| UPI Lite | 36.7 |
| UPI Autopay | 25.2 |

## Failure analysis
- INC-2026-08 — PSP callback latency increase on CRED (day 3 of 4); see RCA-2026-08.

## Recommendations
Stay on the open incident: keep recovery monitoring on CRED and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D119-MON) and any meetings/emails on 18 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D119-MON, RPT-D118-DAILY, INC-2026-08, RCA-2026-08

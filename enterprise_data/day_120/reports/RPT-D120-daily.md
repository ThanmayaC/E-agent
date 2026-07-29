---
id: RPT-D120-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-19T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 19 Oct 2026)

**Report ID:** RPT-D120-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 19 Oct 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 120 of 180)

## Transaction summary
The rail processed 926.9M UPI transactions on Monday — the Monday ramp-up after the weekend — up 32.2M on the same day last week. Success landed at 99.29% and settlement at 99.98%, held back by live issues on CRED (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 926.9  (▲162.4 d/d, ▲32.2 w/w, ▲182.0 m/m)
- **Success Rate:** 99.29%  (▼0.69 d/d, ▼0.62 w/w, ▼0.31 m/m)
- **Settlement Success:** 99.98%  (▲0.52 d/d, ▲0.02 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.3%  (▼0.02 d/d, ▲0.01 w/w, ▼0.15 m/m)
- **Business Declines:** 0.15%  (▼0.07 w/w, ▼0.05 m/m)
- **Customer Complaints:** 1,154  (▼56 d/d, ▼243 w/w, ▼788 m/m)
- **Merchant Complaints:** 114  (▼4 w/w, ▼97 m/m)
- **Fraud Alerts:** 777  (▼5 d/d, ▼178 w/w, ▼274 m/m)
- **Risk Score:** 21  (▼12 w/w, ▼10 m/m)
- **Response Time:** 603 ms  (▼10 d/d, ▲9 w/w, ▼139 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 298.0 | 99.5% |
| HDFC Bank | 102.3 | 99.55% |
| Bank of Baroda | 73.5 | 99.64% |
| Union Bank of India | 63.9 | 99.43% |
| ICICI Bank | 57.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 442.2 | 99.14% | 231 ms |
| Google Pay | 302.8 | 99.17% | 316 ms |
| Paytm | 74.8 | 99.06% | 192 ms |
| Navi | 34.2 | 99.17% | 225 ms |
| SuperMoney | 18.1 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 347.6 |
| Person to Person | 329.0 |
| QR Payments | 88.1 |
| UPI Lite | 44.5 |
| UPI Autopay | 30.6 |

## Failure analysis
- INC-2026-08 — PSP callback latency increase on CRED (day 4 of 4); see RCA-2026-08.

## Recommendations
Stay on the open incident: keep recovery monitoring on CRED and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D120-MON) and any meetings/emails on 19 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D120-MON, RPT-D119-DAILY, INC-2026-08, RCA-2026-08

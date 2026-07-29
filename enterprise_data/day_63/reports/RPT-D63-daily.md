---
id: RPT-D63-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-23T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 23 Aug 2026)

**Report ID:** RPT-D63-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 23 Aug 2026  ·  **Day archetype:** Sunday (quiet)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 63 of 180)

## Transaction summary
The rail processed 694.0M UPI transactions on Sunday — a quiet Sunday — up 11.9M on the same day last week. Success landed at 99.38% and settlement at 98.85%, held back by live issues on Collect Requests (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 694.0  (▼60.5 d/d, ▲11.9 w/w, ▼50.9 m/m)
- **Success Rate:** 99.38%  (▼0.6 d/d, ▲0.13 w/w, ▼0.22 m/m)
- **Settlement Success:** 98.85%  (▼1.13 d/d, ▼0.06 w/w, ▼0.58 m/m)
- **Technical Declines:** 0.41%  (▼0.05 d/d, ▲0.05 w/w, ▼0.04 m/m)
- **Business Declines:** 0.17%  (▼0.03 m/m)
- **Customer Complaints:** 1,617  (▼129 d/d, ▲104 w/w, ▼325 m/m)
- **Merchant Complaints:** 153  (▼5 w/w, ▼58 m/m)
- **Fraud Alerts:** 908  (▼2 d/d, ▲2 w/w, ▼143 m/m)
- **Risk Score:** 26  (▲1 d/d, ▼5 m/m)
- **Response Time:** 673 ms  (▼13 d/d, ▲13 w/w, ▼69 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 223.1 | 99.5% |
| HDFC Bank | 76.6 | 99.55% |
| Bank of Baroda | 55.0 | 99.64% |
| Union Bank of India | 47.8 | 99.43% |
| ICICI Bank | 42.8 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 331.1 | 99.14% | 231 ms |
| Google Pay | 226.7 | 99.17% | 316 ms |
| Paytm | 56.0 | 99.06% | 192 ms |
| Navi | 25.6 | 99.17% | 225 ms |
| SuperMoney | 13.5 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 260.2 |
| Person to Person | 246.4 |
| QR Payments | 65.9 |
| UPI Lite | 33.3 |
| UPI Autopay | 22.9 |

## Failure analysis
- INC-2026-28 — feature-level degradation on Collect Requests (day 3 of 3); see RCA-2026-28.

## Recommendations
Stay on the open incident: keep recovery monitoring on Collect Requests and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D63-MON) and any meetings/emails on 23 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D63-MON, RPT-D62-DAILY, INC-2026-28, RCA-2026-28

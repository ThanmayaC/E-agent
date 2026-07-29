---
id: RPT-D133-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-01T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 01 Nov 2026)

**Report ID:** RPT-D133-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 01 Nov 2026  ·  **Day archetype:** Sunday (quiet) · maintenance window
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 133 of 180)

## Transaction summary
The rail processed 785.0M UPI transactions on Sunday — a quiet Sunday with a scheduled maintenance window — up 3.6M on the same day last week. Success landed at 99.18% and settlement at 99.26%, held back by live issues on TravelGo, InsureWell (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 785.0  (▼289.1 d/d, ▲3.6 w/w, ▲40.1 m/m)
- **Success Rate:** 99.18%  (▼0.8 d/d, ▲0.96 w/w, ▼0.42 m/m)
- **Settlement Success:** 99.26%  (▲0.32 d/d, ▲0.18 w/w, ▼0.17 m/m)
- **Technical Declines:** 0.27%  (▼0.11 d/d, ▼0.31 w/w, ▼0.18 m/m)
- **Business Declines:** 0.15%  (▼0.05 m/m)
- **Customer Complaints:** 1,037  (▼298 d/d, ▼794 w/w, ▼905 m/m)
- **Merchant Complaints:** 111  (▼49 d/d, ▼118 w/w, ▼100 m/m)
- **Fraud Alerts:** 762  (▲2 d/d, ▼12 w/w, ▼289 m/m)
- **Risk Score:** 21  (▲1 d/d, ▼10 m/m)
- **Response Time:** 578 ms  (▼34 d/d, ▼104 w/w, ▼164 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 252.4 | 99.5% |
| HDFC Bank | 86.6 | 99.55% |
| Bank of Baroda | 62.3 | 99.64% |
| Union Bank of India | 54.1 | 99.43% |
| ICICI Bank | 48.4 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 374.5 | 99.14% | 231 ms |
| Google Pay | 256.4 | 99.17% | 316 ms |
| Paytm | 63.3 | 99.06% | 192 ms |
| Navi | 28.9 | 99.17% | 225 ms |
| SuperMoney | 15.3 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 294.4 |
| Person to Person | 278.7 |
| QR Payments | 74.6 |
| UPI Lite | 37.7 |
| UPI Autopay | 25.9 |

## Failure analysis
- INC-2026-24 — merchant decline-rate spike on TravelGo, InsureWell (day 5 of 5); see RCA-2026-24.

## Recommendations
Stay on the open incident: keep recovery monitoring on TravelGo, InsureWell and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D133-MON) and any meetings/emails on 01 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D133-MON, RPT-D132-DAILY, INC-2026-24, RCA-2026-24

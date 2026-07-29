---
id: RPT-D103-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-10-02T17:30:00
---

# UPI Products — Daily Operations Report (Friday, 02 Oct 2026)

**Report ID:** RPT-D103-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Friday 02 Oct 2026  ·  **Day archetype:** High-volume campaign day
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 103 of 180)

## Transaction summary
The rail processed 1130.7M UPI transactions on Friday — a campaign-driven high-volume day — up 240.7M on the same day last week. Success landed at 99.98% and settlement at 99.17%, held back by live issues on State Bank of India (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 1130.7  (▲204.5 d/d, ▲240.7 w/w, ▲385.8 m/m)
- **Success Rate:** 99.98%  (▲1.15 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.17%  (▲0.36 d/d, ▼0.75 w/w, ▼0.26 m/m)
- **Technical Declines:** 0.31%  (▼0.14 m/m)
- **Business Declines:** 0.16%  (▼0.01 d/d, ▼0.07 w/w, ▼0.04 m/m)
- **Customer Complaints:** 1,227  (▼32 d/d, ▼282 w/w, ▼715 m/m)
- **Merchant Complaints:** 140  (▼19 d/d, ▲11 w/w, ▼71 m/m)
- **Fraud Alerts:** 814  (▼184 w/w, ▼237 m/m)
- **Risk Score:** 22  (▼1 d/d, ▼13 w/w, ▼9 m/m)
- **Response Time:** 608 ms  (▼2 d/d, ▼4 w/w, ▼134 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 363.5 | 99.39% |
| HDFC Bank | 124.7 | 99.55% |
| Bank of Baroda | 89.7 | 99.64% |
| Union Bank of India | 77.9 | 99.43% |
| ICICI Bank | 69.7 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 539.4 | 99.14% | 231 ms |
| Google Pay | 369.3 | 99.17% | 316 ms |
| Paytm | 91.2 | 99.06% | 192 ms |
| Navi | 41.7 | 99.17% | 225 ms |
| SuperMoney | 22.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 424.0 |
| Person to Person | 401.4 |
| QR Payments | 107.4 |
| UPI Lite | 54.3 |
| UPI Autopay | 37.3 |

## Failure analysis
- INC-2026-12 — merchant settlement delay on State Bank of India (day 4 of 5); see RCA-2026-12.

## Recommendations
Stay on the open incident: keep recovery monitoring on State Bank of India and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D103-MON) and any meetings/emails on 02 Oct.

Refs: upi_kpis_month.xlsx, TEAMS-D103-MON, RPT-D102-DAILY, INC-2026-12, RCA-2026-12

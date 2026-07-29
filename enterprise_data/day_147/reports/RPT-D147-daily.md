---
id: RPT-D147-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-11-15T17:30:00
---

# UPI Products — Daily Operations Report (Sunday, 15 Nov 2026)

**Report ID:** RPT-D147-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Sunday 15 Nov 2026  ·  **Day archetype:** Sunday (quiet) · maintenance window
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 147 of 180)

## Transaction summary
The rail processed 802.4M UPI transactions on Sunday — a quiet Sunday with a scheduled maintenance window — down 1.7M on the same day last week. Success landed at 98.57% and settlement at 99.59%, held back by live issues on FamApp, IndusInd Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 802.4  (▼72.4 d/d, ▼1.7 w/w, ▲57.5 m/m)
- **Success Rate:** 98.57%  (▼1.41 d/d, ▼0.75 w/w, ▼1.03 m/m)
- **Settlement Success:** 99.59%  (▼0.39 d/d, ▲0.55 w/w, ▲0.16 m/m)
- **Technical Declines:** 0.26%  (▼0.06 w/w, ▼0.19 m/m)
- **Business Declines:** 0.26%  (▲0.1 d/d, ▲0.12 w/w, ▲0.06 m/m)
- **Customer Complaints:** 1,354  (▲296 d/d, ▲181 w/w, ▼588 m/m)
- **Merchant Complaints:** 124  (▼22 d/d, ▲21 w/w, ▼87 m/m)
- **Fraud Alerts:** 984  (▲256 d/d, ▲242 w/w, ▼67 m/m)
- **Risk Score:** 36  (▲16 d/d, ▲16 w/w, ▲5 m/m)
- **Response Time:** 559 ms  (▼1 d/d, ▼55 w/w, ▼183 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 258.0 | 99.5% |
| HDFC Bank | 88.5 | 99.55% |
| Bank of Baroda | 63.6 | 99.64% |
| Union Bank of India | 55.3 | 99.43% |
| ICICI Bank | 49.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 382.8 | 99.14% | 231 ms |
| Google Pay | 262.1 | 99.17% | 316 ms |
| Paytm | 64.7 | 99.06% | 192 ms |
| Navi | 29.6 | 99.17% | 225 ms |
| SuperMoney | 15.6 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 300.9 |
| Person to Person | 284.9 |
| QR Payments | 76.2 |
| UPI Lite | 38.5 |
| UPI Autopay | 26.5 |

## Failure analysis
- INC-2026-17 — merchant settlement delay on IndusInd Bank (day 3 of 4); see RCA-2026-17.
- INC-2026-26 — fraud / risk spike on FamApp (day 1 of 3); see RCA-2026-26.

## Recommendations
Stay on the open incidents: keep recovery monitoring on FamApp, IndusInd Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D147-MON) and any meetings/emails on 15 Nov.

Refs: upi_kpis_month.xlsx, TEAMS-D147-MON, RPT-D146-DAILY, INC-2026-17, INC-2026-26, RCA-2026-17, RCA-2026-26

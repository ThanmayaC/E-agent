---
id: RPT-D36-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-27T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 27 Jul 2026)

**Report ID:** RPT-D36-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 27 Jul 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 36 of 180)

## Transaction summary
The rail processed 792.6M UPI transactions on Monday — the Monday ramp-up after the weekend — down 181.6M on the same day last week. Success landed at 99.97% and settlement at 99.21%, held back by live issues on Amazon Pay, Axis Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 792.6  (▲129.7 d/d, ▼181.6 w/w, ▲47.7 m/m)
- **Success Rate:** 99.97%  (▲1.45 d/d, ▲0.06 w/w, ▲0.37 m/m)
- **Settlement Success:** 99.21%  (▼0.05 d/d, ▼0.77 w/w, ▼0.22 m/m)
- **Technical Declines:** 0.44%  (▼0.04 d/d, ▼0.05 w/w, ▼0.01 m/m)
- **Business Declines:** 0.27%  (▲0.09 d/d, ▲0.08 w/w, ▲0.07 m/m)
- **Customer Complaints:** 2,151  (▲219 d/d, ▲166 w/w, ▲209 m/m)
- **Merchant Complaints:** 405  (▲229 d/d, ▲224 w/w, ▲194 m/m)
- **Fraud Alerts:** 955  (▼4 d/d, ▼15 w/w, ▼96 m/m)
- **Risk Score:** 28  (▼1 w/w, ▼3 m/m)
- **Response Time:** 726 ms  (▼26 d/d, ▼33 w/w, ▼16 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 254.8 | 99.5% |
| HDFC Bank | 87.4 | 99.55% |
| Bank of Baroda | 62.9 | 99.64% |
| Union Bank of India | 54.6 | 99.43% |
| ICICI Bank | 48.9 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 378.1 | 99.14% | 231 ms |
| Google Pay | 258.9 | 99.17% | 316 ms |
| Paytm | 63.9 | 99.06% | 192 ms |
| Navi | 29.2 | 99.17% | 225 ms |
| SuperMoney | 15.4 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 297.2 |
| Person to Person | 281.4 |
| QR Payments | 75.3 |
| UPI Lite | 38.0 |
| UPI Autopay | 26.2 |

## Failure analysis
- INC-2026-27 — PSP callback latency increase on Amazon Pay (day 3 of 5); see RCA-2026-27.
- INC-2026-02 — merchant settlement delay on Axis Bank (day 1 of 3); see RCA-2026-02.

## Recommendations
Stay on the open incidents: keep recovery monitoring on Amazon Pay, Axis Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D36-MON) and any meetings/emails on 27 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D36-MON, RPT-D35-DAILY, INC-2026-27, INC-2026-02, RCA-2026-27, RCA-2026-02

---
id: RPT-D38-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-29T17:30:00
---

# UPI Products — Daily Operations Report (Wednesday, 29 Jul 2026)

**Report ID:** RPT-D38-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Wednesday 29 Jul 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 38 of 180)

## Transaction summary
The rail processed 910.7M UPI transactions on Wednesday — the month-end surge as salary and bill-pay flows land — up 102.0M on the same day last week. Success landed at 99.98% and settlement at 99.98%, held back by live issues on Amazon Pay, Axis Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 910.7  (▼5.9 d/d, ▲102.0 w/w, ▲165.8 m/m)
- **Success Rate:** 99.98%  (▲1.34 d/d, ▲0.36 w/w, ▲0.38 m/m)
- **Settlement Success:** 99.98%  (▲1.66 d/d, ▲0.78 w/w, ▲0.55 m/m)
- **Technical Declines:** 0.4%  (▼0.01 d/d, ▼0.05 m/m)
- **Business Declines:** 0.21%  (▼0.03 d/d, ▲0.02 w/w, ▲0.01 m/m)
- **Customer Complaints:** 1,796  (▼131 d/d, ▲90 w/w, ▼146 m/m)
- **Merchant Complaints:** 249  (▼65 d/d, ▲69 w/w, ▲38 m/m)
- **Fraud Alerts:** 965  (▲10 d/d, ▼4 w/w, ▼86 m/m)
- **Risk Score:** 28  (▲1 d/d, ▼3 m/m)
- **Response Time:** 687 ms  (▼16 d/d, ▼3 w/w, ▼55 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 292.8 | 99.5% |
| HDFC Bank | 100.5 | 99.55% |
| Bank of Baroda | 72.2 | 99.64% |
| Union Bank of India | 62.7 | 99.43% |
| ICICI Bank | 56.2 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 434.5 | 99.14% | 231 ms |
| Google Pay | 297.5 | 99.17% | 316 ms |
| Paytm | 73.5 | 99.06% | 192 ms |
| Navi | 33.6 | 99.17% | 225 ms |
| SuperMoney | 17.7 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 341.5 |
| Person to Person | 323.3 |
| QR Payments | 86.5 |
| UPI Lite | 43.7 |
| UPI Autopay | 30.1 |

## Failure analysis
- INC-2026-27 — PSP callback latency increase on Amazon Pay (day 5 of 5); see RCA-2026-27.
- INC-2026-02 — merchant settlement delay on Axis Bank (day 3 of 3); see RCA-2026-02.

## Recommendations
Stay on the open incidents: keep recovery monitoring on Amazon Pay, Axis Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D38-MON) and any meetings/emails on 29 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D38-MON, RPT-D37-DAILY, INC-2026-27, INC-2026-02, RCA-2026-27, RCA-2026-02

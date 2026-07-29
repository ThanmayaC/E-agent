---
id: RPT-D37-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-07-28T17:30:00
---

# UPI Products — Daily Operations Report (Tuesday, 28 Jul 2026)

**Report ID:** RPT-D37-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Tuesday 28 Jul 2026  ·  **Day archetype:** Month-end peak
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 37 of 180)

## Transaction summary
The rail processed 916.6M UPI transactions on Tuesday — the month-end surge as salary and bill-pay flows land — up 126.8M on the same day last week. Success landed at 98.64% and settlement at 98.32%, held back by live issues on Amazon Pay, Axis Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 916.6  (▲124.0 d/d, ▲126.8 w/w, ▲171.7 m/m)
- **Success Rate:** 98.64%  (▼1.33 d/d, ▼1.34 w/w, ▼0.96 m/m)
- **Settlement Success:** 98.32%  (▼0.89 d/d, ▼1.55 w/w, ▼1.11 m/m)
- **Technical Declines:** 0.41%  (▼0.03 d/d, ▲0.01 w/w, ▼0.04 m/m)
- **Business Declines:** 0.24%  (▼0.03 d/d, ▲0.06 w/w, ▲0.04 m/m)
- **Customer Complaints:** 1,927  (▼224 d/d, ▲227 w/w, ▼15 m/m)
- **Merchant Complaints:** 314  (▼91 d/d, ▲132 w/w, ▲103 m/m)
- **Fraud Alerts:** 955  (▼21 w/w, ▼96 m/m)
- **Risk Score:** 27  (▼1 d/d, ▼2 w/w, ▼4 m/m)
- **Response Time:** 703 ms  (▼23 d/d, ▲9 w/w, ▼39 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 294.7 | 99.5% |
| HDFC Bank | 101.1 | 99.55% |
| Bank of Baroda | 72.7 | 99.64% |
| Union Bank of India | 63.1 | 99.43% |
| ICICI Bank | 56.5 | 99.4% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 437.3 | 99.14% | 231 ms |
| Google Pay | 299.4 | 99.17% | 316 ms |
| Paytm | 73.9 | 99.06% | 192 ms |
| Navi | 33.8 | 99.17% | 225 ms |
| SuperMoney | 17.9 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 343.7 |
| Person to Person | 325.4 |
| QR Payments | 87.1 |
| UPI Lite | 44.0 |
| UPI Autopay | 30.2 |

## Failure analysis
- INC-2026-27 — PSP callback latency increase on Amazon Pay (day 4 of 5); see RCA-2026-27.
- INC-2026-02 — merchant settlement delay on Axis Bank (day 2 of 3); see RCA-2026-02.

## Recommendations
Stay on the open incidents: keep recovery monitoring on Amazon Pay, Axis Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D37-MON) and any meetings/emails on 28 Jul.

Refs: upi_kpis_month.xlsx, TEAMS-D37-MON, RPT-D36-DAILY, INC-2026-27, INC-2026-02, RCA-2026-27, RCA-2026-02

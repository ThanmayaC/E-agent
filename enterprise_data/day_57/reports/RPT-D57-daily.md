---
id: RPT-D57-DAILY
type: report
organization: NPCI (Synthetic Demonstration)
department: UPI Products
timestamp: 2026-08-17T17:30:00
---

# UPI Products — Daily Operations Report (Monday, 17 Aug 2026)

**Report ID:** RPT-D57-DAILY  ·  **Prepared by:** Farhan Subramanian
**Date:** Monday 17 Aug 2026  ·  **Day archetype:** Monday (ramp-up)
**Source:** upi_kpis_month.xlsx ("Monthly KPIs", day 57 of 180)

## Transaction summary
The rail processed 820.5M UPI transactions on Monday — the Monday ramp-up after the weekend — up 29.8M on the same day last week. Success landed at 99.57% and settlement at 97.94%, held back by live issues on ICICI Bank (detailed below).

## KPIs (today · vs yesterday / last week / month start)
- **UPI Transactions:** 820.5  (▲138.4 d/d, ▲29.8 w/w, ▲75.6 m/m)
- **Success Rate:** 99.57%  (▲0.32 d/d, ▼0.27 w/w, ▼0.03 m/m)
- **Settlement Success:** 97.94%  (▼0.97 d/d, ▼2.04 w/w, ▼1.49 m/m)
- **Technical Declines:** 0.36%  (▼0.01 w/w, ▼0.09 m/m)
- **Business Declines:** 0.26%  (▲0.09 d/d, ▲0.08 w/w, ▲0.06 m/m)
- **Customer Complaints:** 1,814  (▲301 d/d, ▲258 w/w, ▼128 m/m)
- **Merchant Complaints:** 363  (▲205 d/d, ▲200 w/w, ▲152 m/m)
- **Fraud Alerts:** 920  (▲14 d/d, ▼11 w/w, ▼131 m/m)
- **Risk Score:** 26  (▼5 m/m)
- **Response Time:** 666 ms  (▲6 d/d, ▼3 w/w, ▼76 m/m)

## Top banks (by volume)
| Bank | Txns (M/day) | Success |
|------|--------------|---------|
| State Bank of India | 263.8 | 99.5% |
| HDFC Bank | 90.5 | 99.55% |
| Bank of Baroda | 65.1 | 99.64% |
| Union Bank of India | 56.5 | 99.43% |
| ICICI Bank | 50.6 | 97.2% |

## Top UPI apps (by volume)
| App / PSP | Txns (M/day) | Success | Callback p95 |
|-----------|--------------|---------|--------------|
| PhonePe | 391.4 | 99.14% | 231 ms |
| Google Pay | 268.0 | 99.17% | 316 ms |
| Paytm | 66.2 | 99.06% | 192 ms |
| Navi | 30.2 | 99.17% | 225 ms |
| SuperMoney | 16.0 | 99.08% | 299 ms |

## Top features (by volume)
| Feature | Txns (M/day) |
|---------|--------------|
| Person to Merchant | 307.7 |
| Person to Person | 291.3 |
| QR Payments | 77.9 |
| UPI Lite | 39.4 |
| UPI Autopay | 27.1 |

## Failure analysis
- INC-2026-03 — merchant settlement delay on ICICI Bank (day 1 of 4); see RCA-2026-03.

## Recommendations
Stay on the open incident: keep recovery monitoring on ICICI Bank and hold the bank/PSP bridge until success clears the 99.2% floor and stays there through two clean hours.

## Notes
All figures read from upi_kpis_month.xlsx; they match the day's monitoring note
(TEAMS-D57-MON) and any meetings/emails on 17 Aug.

Refs: upi_kpis_month.xlsx, TEAMS-D57-MON, RPT-D56-DAILY, INC-2026-03, RCA-2026-03
